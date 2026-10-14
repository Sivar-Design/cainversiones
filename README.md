# cainversiones.com — recuperación del sitio 2018

Copia estática del sitio de **Cromeyer Ávila Inversiones** tal como estaba el
**5 de agosto de 2018** (WordPress + tema Divi 3.0.103), recuperada de la
[Wayback Machine](https://web.archive.org/web/20180805010424/http://cainversiones.com/).
Sirve de punto de partida para el rediseño.

## Estructura

| Carpeta | Qué contiene |
|---|---|
| `site/` | **El sitio publicable** (HTML/CSS/JS/imágenes). Es lo que se sube a Cloudflare Pages. |
| `archive-raw/` | Todo lo descargado de la Wayback Machine, sin tocar, incluidas versiones anteriores del sitio (temas *ElegantEstate*, *inspired* 2010–2017). `_manifest.json` lista URL original y fecha de cada captura. |
| `tools/` | Scripts: `wayback_fetch.py` y `wayback_deps.py` (descarga) y `build_site.py` (genera `site/`). |

## Páginas recuperadas (2018)

- `/` — Home
- `/condominio-altea-apartamentos-en-san-salvador/` — Condominio Altea
- `/torre-paseo-alto-colonia-escalon-san-salvador/` — Torre Paseo Alto
- `/proyectos-vendidos/` — Proyectos vendidos (galería de 34 proyectos)

## Qué es original y qué es reconstrucción

**Original (tal cual del archivo):** HTML y textos de las 4 páginas, tema Divi
3.0.103 (CSS/JS/fuentes de íconos), CSS global del personalizador de Divi
(colores, tipografías Ropa Sans/Montserrat, cabecera y pie cobre `#b37647`),
logotipos, fotos de Altea y Torre Paseo Alto, fondos de 2018.

**Reconstruido:**

- `tools/static/reconstruccion-2018.css` — Wayback no guardó el CSS por
  módulo de Home, Altea y Torre Paseo Alto (`et-core-unified-*.min.css`).
  Se aproximó con los colores y fondos originales de 2018.
- Fotos de proyectos vendidos — 26 de 34 no se archivaron en su versión de 2018;
  se usan las mismas obras desde versiones anteriores del sitio (2010–2014,
  ver `tools/static/sustituciones.json`).
- 8 proyectos sin foto en ningún archivo (Torre Spazio, San Benito 21,
  Portofino, La Capilla 560, Villas de San Michelle, Torre del Paseo I,
  Bella Vista, Los Castaños) muestran un placeholder de marca.
- La vista nocturna de Altea (galería) no existe en ningún archivo: se quitó
  del slider.

## Otras diferencias con el original

- El formulario de contacto de Divi necesitaba PHP. Ahora abre el correo del
  visitante con el mensaje dirigido a `info@cainversiones.com`.
- Se quitaron feeds, xmlrpc, oEmbed, emojis, Wordfence y los Google Analytics
  antiguos (UA-37259051-1, ya dado de baja por Google).
- `noindex` se mantiene: es una copia temporal y no debe competir en Google.
- `_redirects` envía las URLs antiguas (2010–2017) a la página equivalente.

## Regenerar

```bash
python3 tools/build_site.py
```

La descarga desde Wayback corre en GitHub Actions
(`.github/workflows/wayback-fetch.yml`) porque el entorno de trabajo no tiene
acceso directo a web.archive.org.

## Publicar en Cloudflare Pages

Workers & Pages → Create → Pages → Connect to Git → `Sivar-Design/cainversiones`

- Production branch: la rama de trabajo (o `main` cuando se fusione)
- Framework preset: *None*
- Build command: *(vacío)*
- Build output directory: `site`
