#!/usr/bin/env python3
"""Segunda pasada: descarga todo lo que referencian las páginas Divi de 2018
(CSS de caché por página, imágenes, srcset, url() dentro de CSS, fuentes) y
que no quedó en archive-raw/ en la primera pasada. Repite hasta no encontrar
nada nuevo."""
import json, os, re, sys, time
from urllib.parse import urlsplit, unquote, urljoin
import requests

OUT = sys.argv[1] if len(sys.argv) > 1 else "archive-raw"
TS = "20180805010424"
PAGES = ["index.html",
         "condominio-altea-apartamentos-en-san-salvador/index.html",
         "torre-paseo-alto-colonia-escalon-san-salvador/index.html",
         "proyectos-vendidos/index.html"]
HOST = re.compile(r"^https?://(www\.)?cainversiones\.com(:80)?", re.I)
SKIP = re.compile(r"(xmlrpc|/feed/|wp-json|wordfence|/\?|wlwmanifest)", re.I)

s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (site recovery for owner)"

def local_path(url):
    p = urlsplit(url)
    path = unquote(p.path) or "/"
    if path.endswith("/") or "." not in os.path.basename(path):
        path = path.rstrip("/") + "/index.html"
    if p.query:
        root, ext = os.path.splitext(path)
        path = root + "__" + re.sub(r"[^A-Za-z0-9._-]", "_", p.query)[:80] + (ext or ".html")
    return os.path.join(OUT, path.lstrip("/"))

def exists(url):
    if os.path.exists(local_path(url)):
        return True
    bare = urlsplit(url)._replace(query="").geturl()
    return os.path.exists(local_path(bare))

def refs(text, base):
    found = set()
    for m in re.finditer(r"""(?:src|href|data-src|data-bg|data-image|poster)\s*=\s*["']([^"']+)["']""", text):
        found.add(m.group(1))
    for m in re.finditer(r"""srcset\s*=\s*["']([^"']+)["']""", text):
        for part in m.group(1).split(","):
            if part.strip():
                found.add(part.strip().split()[0])
    for m in re.finditer(r"""url\(\s*['"]?([^'")]+)['"]?\s*\)""", text):
        found.add(m.group(1))
    out = set()
    for u in found:
        u = u.replace("&#038;", "&").replace("&amp;", "&").replace("\\/", "/")
        if u.startswith("data:") or u.startswith("#"):
            continue
        full = urljoin(base, u)
        if HOST.match(full) and not SKIP.search(full):
            out.add(full.split("#")[0])
    return out

def fetch(url):
    for i in range(5):
        try:
            r = s.get(f"https://web.archive.org/web/{TS}id_/{url}", timeout=90)
            if r.status_code in (429, 502, 503, 504):
                raise requests.RequestException(r.status_code)
            return r
        except requests.RequestException as e:
            time.sleep(5 * 2 ** i)
    return None

queue = []
for p in PAGES:
    queue.append(("http://cainversiones.com/" + os.path.dirname(p) + "/").replace(".com//", ".com/"))
scanned, failed, log = set(), [], []
todo = set()
for p in PAGES:
    base = "http://cainversiones.com/" + (os.path.dirname(p) + "/" if os.path.dirname(p) else "")
    todo |= refs(open(os.path.join(OUT, p), encoding="utf-8", errors="ignore").read(), base)

seen = set()
while todo:
    url = todo.pop()
    if url in seen:
        continue
    seen.add(url)
    path = local_path(url)
    if not exists(url):
        r = fetch(url)
        if not r or r.status_code != 200:
            failed.append(url); print("FAIL", url, r.status_code if r else "net", flush=True)
            continue
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "wb").write(r.content)
        log.append(url); print("OK", url, len(r.content), flush=True)
        time.sleep(1.0)
    elif not os.path.exists(path):
        path = local_path(urlsplit(url)._replace(query="").geturl())
    if path.endswith(".css"):
        todo |= refs(open(path, encoding="utf-8", errors="ignore").read(), url) - seen

json.dump({"downloaded": log, "failed": failed}, open(os.path.join(OUT, "_deps.json"), "w"), indent=1)
print("downloaded", len(log), "failed", len(failed))
