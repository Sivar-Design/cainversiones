#!/usr/bin/env python3
"""Convierte las páginas Divi archivadas (archive-raw/) en un sitio HTML estático
(site/) lo más fiel posible al original del 2018-08-05.

- Quita el código propio de WordPress que no funciona sin servidor (feeds,
  xmlrpc, oEmbed, emojis, Wordfence, analytics viejos).
- Reescribe todas las URLs de cainversiones.com a rutas relativas a la raíz.
- Copia solo los archivos que realmente se usan (CSS, JS, imágenes, fuentes),
  siguiendo también los url() dentro de los CSS.
- El formulario de contacto de Divi se convierte en mailto: (no hay PHP).
"""
import glob, os, re, shutil, sys
from urllib.parse import urlsplit, unquote, urljoin

RAW = "archive-raw"
OUT = "site"
EMAIL = "info@cainversiones.com"
PAGES = ["index.html",
         "condominio-altea-apartamentos-en-san-salvador/index.html",
         "torre-paseo-alto-colonia-escalon-san-salvador/index.html",
         "proyectos-vendidos/index.html"]
HOST_RE = r"(?:https?:)?(?:\\?/\\?/)(?:www\.)?cainversiones\.com(?::80)?"

missing = set()

def find_raw(path):
    """Ruta en archive-raw para una ruta web (sin query). Acepta variantes
    guardadas con sufijo de query (archivo__ver_x.css)."""
    path = unquote(path)
    if path.endswith("/") or "." not in os.path.basename(path):
        path = path.rstrip("/") + "/index.html"
    cand = os.path.join(RAW, path.lstrip("/"))
    if os.path.isfile(cand):
        return cand
    root, ext = os.path.splitext(cand)
    hits = sorted(glob.glob(glob.escape(root) + "__*" + ext))
    return hits[-1] if hits else None

def copy_asset(path):
    """Copia un asset a site/ y, si es CSS, procesa sus url()."""
    path = urlsplit(path).path
    dest = os.path.join(OUT, unquote(path).lstrip("/"))
    if os.path.exists(dest):
        return
    src = find_raw(path)
    if not src:
        missing.add(path)
        return
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if dest.endswith(".css"):
        css = open(src, encoding="utf-8", errors="ignore").read()
        css = rewrite_urls(css)
        open(dest, "w", encoding="utf-8").write(css)
        for u in re.findall(r"""url\(\s*['"]?([^'")]+)['"]?\s*\)""", css):
            if u.startswith("data:") or re.match(r"https?://", u):
                continue
            copy_asset(urljoin(path, u.split("#")[0].split("?")[0]))
    else:
        shutil.copyfile(src, dest)

def rewrite_urls(text):
    # URLs escapadas en JSON (http:\/\/cainversiones.com\/...)
    text = re.sub(r"https?:\\/\\/(?:www\.)?cainversiones\.com(?::80)?", "", text)
    # URLs normales: dejar ruta relativa a la raíz y quitar ?ver=...
    def repl(m):
        path = m.group(1) or "/"
        query = m.group(2) or ""
        if re.search(r"\.(css|js|png|jpe?g|gif|svg|woff2?|ttf|eot|ico|webp)$", path, re.I):
            query = ""
        return path + query
    text = re.sub(HOST_RE + r"(/[^\s\"'()<>?#]*)?(\?[^\s\"'()<>#]*)?", repl, text)
    text = text.replace("http://fonts.googleapis.com", "https://fonts.googleapis.com")
    return text

REMOVE = [
    r'<link rel="pingback"[^>]*>',
    r"<!--\[if lt IE 9\]>.*?<!\[endif\]-->",
    r"<script>var et_site_url=.*?</script>",
    r"<link rel='dns-prefetch'[^>]*>",
    r'<link rel="alternate"[^>]*>',
    r"<script type=\"text/javascript\">\s*window\._wpemojiSettings.*?</script>",
    r'<style type="text/css">\s*img\.wp-smiley.*?</style>',
    r'<meta[^>]+name="generator"[^>]*/?>',
    r'<meta name="generator"[^>]*/?>',
    r"<link rel='https://api.w.org/'[^>]*>",
    r'<link rel="EditURI"[^>]*>',
    r'<link rel="wlwmanifest"[^>]*>',
    r"<link rel='shortlink'[^>]*>",
    r'<link rel="canonical"[^>]*>',
    r"<script type=\"text/javascript\">\s*\(function\(url\)\{.*?wordfence_lh.*?</script>",
    r"<!-- BEGIN ExactMetrics.*?<!-- END ExactMetrics Universal Analytics -->",
    r"<!-- Global site tag \(gtag\.js\).*?</script>\s*<script>.*?</script>",
    r"<script type='text/javascript' src='[^']*wp-embed\.min\.js[^']*'></script>",
    r"<link rel='stylesheet' id='dashicons-css'[^>]*>",
]

FORM_JS = """<script>
/* Sitio estático: el formulario de contacto abre el correo del visitante. */
document.querySelectorAll('form.et_pb_contact_form').forEach(function (form) {
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var get = function (sel) { var el = form.querySelector(sel); return el ? el.value.trim() : ''; };
    var nombre = get('input[id*="name"]'), email = get('input[id*="email"]'), msg = get('textarea');
    var asunto = document.title.split('|')[0].trim() + ' - Solicitud de información';
    var cuerpo = 'Nombre: ' + nombre + '\\nEmail: ' + email + '\\n\\n' + msg;
    window.location.href = 'mailto:%s?subject=' + encodeURIComponent(asunto) + '&body=' + encodeURIComponent(cuerpo);
  }, true);
});
</script>
""" % EMAIL

def build_page(rel):
    html = open(os.path.join(RAW, rel), encoding="utf-8").read()
    for pat in REMOVE:
        html = re.sub(pat, "", html, flags=re.S)
    html = re.sub(r'\s+onerror="et_core_page_resource_fallback\(this, true\)" onload="et_core_page_resource_fallback\(this\)"', "", html)
    html = rewrite_urls(html)
    # Formulario de búsqueda y de contacto sin backend
    html = html.replace('class="et-search-form" action="/"', 'class="et-search-form" action="#"')
    html = re.sub(r'(<form class="et_pb_contact_form clearfix" method="post" action=")[^"]*"', r'\1#"', html)
    if "et_pb_contact_form" in html:
        html = html.replace("</body>", FORM_JS + "</body>")
    html = re.sub(r"<!DOCTYPE html>.*?<head>", "<!DOCTYPE html>\n<html lang=\"es\">\n<head>", html, count=1, flags=re.S)
    html = re.sub(r"\n\s*\n+", "\n", html)
    dest = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(dest) or OUT, exist_ok=True)
    open(dest, "w", encoding="utf-8").write(html)
    # Assets referenciados
    refs = set(re.findall(r"""(?:src|href|data-[a-z-]+)\s*=\s*["'](/[^"'#]*)["']""", html))
    for m in re.findall(r"""srcset\s*=\s*["']([^"']+)["']""", html):
        refs |= {p.strip().split()[0] for p in m.split(",") if p.strip()}
    refs |= set(re.findall(r"""url\(\s*['"]?(/[^'")]+)['"]?\s*\)""", html))
    for r in refs:
        p = urlsplit(r).path
        if p.endswith("/") or "." not in os.path.basename(p):
            continue  # enlace a otra página
        copy_asset(p)

if __name__ == "__main__":
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    for p in PAGES:
        build_page(p)
    for extra in ["/favicon.ico"]:
        copy_asset(extra)
    shutil.copyfile("tools/static/_redirects", os.path.join(OUT, "_redirects"))
    shutil.copyfile("tools/static/404.html", os.path.join(OUT, "404.html"))
    if missing:
        print("No encontrados en el archivo:", *sorted(missing), sep="\n  ")
    n = sum(len(f) for _, _, f in os.walk(OUT))
    print(f"site/ listo: {n} archivos")
