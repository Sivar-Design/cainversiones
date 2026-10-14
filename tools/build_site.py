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
import glob, json, os, re, shutil, sys
from urllib.parse import urlsplit, unquote, urljoin
from PIL import Image, ImageDraw, ImageFont

RAW = "archive-raw"
OUT = "site"
EMAIL = "info@cainversiones.com"
PAGES = ["index.html",
         "condominio-altea-apartamentos-en-san-salvador/index.html",
         "torre-paseo-alto-colonia-escalon-san-salvador/index.html",
         "proyectos-vendidos/index.html"]
HOST_RE = r"(?:https?:)?(?:\\?/\\?/)(?:www\.)?cainversiones\.com(?::80)?"

missing = set()
placeholders = set()
SUST = json.load(open("tools/static/sustituciones.json", encoding="utf-8"))["sustituciones"]
RECON_CSS = "/assets/css/reconstruccion-2018.css"
THUMB = re.compile(r"-(\d+)x(\d+)(\.\w+)$")

def placeholder(size):
    """Imagen de marca para fotos que no existen en ningún archivo."""
    w, h = size
    im = Image.new("RGB", size, (239, 239, 239))
    logo = Image.open(os.path.join(RAW, "wp-content/uploads/2018/03/Logo-Cromeyer-Avila-2018-wide.png")).convert("RGBA")
    lw = int(w * 0.5)
    logo = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)
    im.paste(logo, ((w - lw) // 2, int(h * 0.38) - logo.height // 2), logo)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", max(12, w // 32))
    except OSError:
        font = ImageFont.load_default()
    txt = "Fotografía no disponible"
    d = ImageDraw.Draw(im)
    tw = d.textlength(txt, font=font)
    d.text(((w - tw) / 2, int(h * 0.62)), txt, fill=(150, 150, 150), font=font)
    return im

def recover_image(path, dest):
    """Imagen de 2018 que Wayback no guardó: sustituye con la misma obra de
    versiones anteriores, recorta miniaturas, o genera un placeholder."""
    m = THUMB.search(path)
    base = THUMB.sub(r"\3", path) if m else path
    if base in SUST:
        im = Image.open(os.path.join(RAW, SUST[base])).convert("RGB")
    elif not m:
        im = None
    else:
        base_src = find_raw(base)
        im = Image.open(base_src).convert("RGB") if base_src else None
    if im is None:
        placeholders.add(base)
        im = placeholder((1200, 852))
    if m:  # miniatura recortada al centro, como hace WordPress
        tw, th = int(m.group(1)), int(m.group(2))
        scale = max(tw / im.width, th / im.height)
        im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
        l, t = (im.width - tw) // 2, (im.height - th) // 2
        im = im.crop((l, t, l + tw, t + th))
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    im.save(dest, quality=85)

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
    if path.startswith("/assets/"):
        return  # archivos propios de la reconstrucción
    dest = os.path.join(OUT, unquote(path).lstrip("/"))
    if os.path.exists(dest):
        return
    src = find_raw(path)
    if not src and path.startswith("/wp-content/uploads/") and re.search(r"\.(jpe?g|png)$", path, re.I):
        recover_image(path, dest)
        return
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

def global_customizer_css():
    """/proyectos-vendidos/ se archivó con el CSS global del personalizador de
    Divi en línea. Es el mismo para todo el sitio: se reutiliza en las demás."""
    t = open(os.path.join(RAW, "proyectos-vendidos/index.html"), encoding="utf-8").read()
    return re.search(r'<style id="et-divi-customizer-global-cached-inline-styles">.*?</style>', t, re.S).group(0)

def build_page(rel):
    html = open(os.path.join(RAW, rel), encoding="utf-8").read()
    if "et-divi-customizer-global-cached-inline-styles" not in html:
        html = html.replace('<link rel="stylesheet" id="et-core-unified-cached-inline-styles"',
                            global_customizer_css() + '\n<link rel="stylesheet" id="et-core-unified-cached-inline-styles"')
    for pat in REMOVE:
        html = re.sub(pat, "", html, flags=re.S)
    html = re.sub(r'\s+onerror="et_core_page_resource_fallback\(this, true\)" onload="et_core_page_resource_fallback\(this\)"', "", html)
    html = rewrite_urls(html)
    # El CSS por página de Divi (et-core-unified) no se archivó: estilos reconstruidos
    html = re.sub(r"/wp-content/cache/et/\d+/et-core-unified-\d+\.min\.css", RECON_CSS, html)
    # La vista nocturna de Altea no existe en ningún archivo: se quita del
    # slider para que abra con la foto real (en la galería de proyectos
    # vendidos los faltantes se dejan como placeholder para conservar la lista).
    html = re.sub(r'<div class="et_pb_gallery_item et_pb_bg_layout_light">\s*<div class=\'et_pb_gallery_image landscape\'>\s*'
                  r'<a href="/wp-content/uploads/2018/05/Condominio-Altea-vista-nocturna[^"]*".*?</a>\s*</div></div>', "", html, flags=re.S)
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
    os.makedirs(os.path.join(OUT, "assets/css"), exist_ok=True)
    shutil.copyfile("tools/static/reconstruccion-2018.css", os.path.join(OUT, RECON_CSS.lstrip("/")))
    for u in re.findall(r"url\(['\"]?(/[^'\")]+)", open("tools/static/reconstruccion-2018.css").read()):
        copy_asset(u)
    shutil.copyfile("tools/static/_redirects", os.path.join(OUT, "_redirects"))
    shutil.copyfile("tools/static/404.html", os.path.join(OUT, "404.html"))
    if placeholders:
        print("Placeholder (sin foto en ningún archivo):", *sorted(placeholders), sep="\n  ")
    if missing:
        print("No encontrados en el archivo:", *sorted(missing), sep="\n  ")
    n = sum(len(f) for _, _, f in os.walk(OUT))
    print(f"site/ listo: {n} archivos")
