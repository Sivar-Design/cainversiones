#!/usr/bin/env python3
"""Descarga el snapshot de cainversiones.com desde la Wayback Machine.

Usa la API CDX para listar todas las URLs archivadas del dominio, elige la
captura más cercana a la fecha objetivo y guarda el archivo original (modo id_)
en archive-raw/, conservando la ruta de la URL.
"""
import json, os, re, sys, time
from urllib.parse import urlsplit, unquote
import requests

DOMAIN = "cainversiones.com"
TARGET = "20180805010424"
OUT = sys.argv[1] if len(sys.argv) > 1 else "archive-raw"
MAX_FILES = 2500
SKIP = re.compile(r"(xmlrpc\.php|wp-json|/feed/?$|/comments/feed|wp-login|wp-admin|\?replytocom=|/embed/?$|oembed)", re.I)

s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (site recovery for owner)"

def get(url, **kw):
    for i in range(6):
        try:
            r = s.get(url, timeout=90, **kw)
            if r.status_code in (429, 502, 503, 504):
                raise requests.RequestException(f"HTTP {r.status_code}")
            return r
        except requests.RequestException as e:
            wait = 5 * (2 ** i)
            print(f"  retry {i+1} {url} ({e}); sleeping {wait}s", flush=True)
            time.sleep(wait)
    return None

def cdx(pattern):
    url = ("https://web.archive.org/cdx/search/cdx?url=" + pattern +
           "&output=json&fl=timestamp,original,mimetype,statuscode,digest"
           "&filter=statuscode:200&to=2019")
    r = get(url)
    if not r or r.status_code != 200 or not r.text.strip():
        return []
    rows = r.json()
    return rows[1:] if rows else []

rows = cdx(DOMAIN + "/*") + cdx("www." + DOMAIN + "/*")
print(f"CDX rows: {len(rows)}", flush=True)

def key(orig):
    p = urlsplit(orig)
    path = p.path or "/"
    return (path.rstrip("/") or "/") + (("?" + p.query) if p.query else "")

best = {}
for ts, orig, mime, st, dig in rows:
    if SKIP.search(orig):
        continue
    k = key(orig)
    d = abs(int(ts[:14].ljust(14, "0")) - int(TARGET))
    if k not in best or d < best[k][0]:
        best[k] = (d, ts, orig, mime)

items = sorted(best.items())[:MAX_FILES]
os.makedirs(OUT, exist_ok=True)
manifest = []
for i, (k, (d, ts, orig, mime)) in enumerate(items):
    p = urlsplit(orig)
    path = unquote(p.path) or "/"
    if path.endswith("/") or "." not in os.path.basename(path):
        path = path.rstrip("/") + "/index.html"
    if p.query:
        root, ext = os.path.splitext(path)
        path = root + "__" + re.sub(r"[^A-Za-z0-9._-]", "_", p.query)[:80] + (ext or ".html")
    local = os.path.join(OUT, path.lstrip("/"))
    entry = {"url": orig, "timestamp": ts, "mime": mime, "file": os.path.relpath(local, OUT)}
    if os.path.exists(local):
        manifest.append(entry); continue
    r = get(f"https://web.archive.org/web/{ts}id_/{orig}")
    if not r or r.status_code != 200:
        print(f"[{i+1}/{len(items)}] FAIL {orig}", flush=True)
        entry["error"] = r.status_code if r else "network"
        manifest.append(entry); continue
    os.makedirs(os.path.dirname(local), exist_ok=True)
    with open(local, "wb") as f:
        f.write(r.content)
    print(f"[{i+1}/{len(items)}] {ts} {orig} -> {entry['file']} ({len(r.content)} B)", flush=True)
    manifest.append(entry)
    time.sleep(1.2)

with open(os.path.join(OUT, "_manifest.json"), "w") as f:
    json.dump(manifest, f, indent=1)
print("done", len(manifest))
