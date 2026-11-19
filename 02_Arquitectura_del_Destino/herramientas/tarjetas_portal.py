#!/usr/bin/env python3
"""
Las tarjetas para compartir de los 39 libros del Portal Público (19 de noviembre de 2026).

Cuando alguien comparte un libro por WhatsApp, Facebook o LinkedIn, la red muestra esta imagen.
Es la misma familia que la tarjeta del Portal (assets/og/portal-publico.jpg): tres anillos de trece
puntos, uno por constelación (adentro La vida interior, en el medio La trama, afuera El campo). El
anillo del libro se tiñe con el color de su constelación y su punto se enciende en oro. Debajo van
«Portal Público · constelación · Libro N», el título y el subtítulo de la portada del libro.

Los textos salen de lo publicado: número y título, de la tarjeta del libro en el index general; el
subtítulo, de la portada del libro (SUB lo fija donde la portada no lo marca con una clase); la
descripción para redes, de la tarjeta del index general.

Escribe assets/og/libro-NN.jpg (1200 × 630) y agrega a cada 01_Libros/*/index.html las etiquetas
og:… y twitter:… (y la descripción, si el libro no la tenía). Se puede correr de nuevo: reemplaza
el bloque que escribió antes.

Necesita Playwright con Chrome y la tipografía Gelasio: npm install @fontsource/gelasio.
Uso:
  FUENTES=RUTA/node_modules/@fontsource/gelasio/files python3 tarjetas_portal.py RUTA/Trinity_Portal_Publico
"""
import asyncio, base64, html, math, os, re, sys
from playwright.async_api import async_playwright

P = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/trinity_portal_publico'
F = os.environ.get('FUENTES', '/home/claude/work/fuentes/node_modules/@fontsource/gelasio/files')
CHROME = os.environ.get('CHROME', '/usr/bin/google-chrome')
BASE = 'https://soyartur-trinity.github.io/Trinity_Portal_Publico/'

CONST = [  # nombre, color del anillo y de la línea superior, brillo de fondo
    ('La vida interior', '#c9a84c', 'rgba(150,110,50,.20)', '#0d0c0b'),
    ('La trama',         '#c3a9dd', 'rgba(111,78,144,.30)', '#0d0b10'),
    ('El campo',         '#c3d0e6', 'rgba(70,100,150,.32)', '#0c1220'),
]

# Subtítulos que la portada no marca con una clase: se toman del texto de la portada.
SUB = {
    2: 'Escuchar, dialogar y transformar las voces que habitan en ti',
    5: 'Portal de continuidad',
    7: 'Ninguno es una verdad absoluta. Todos son espejos.',
    10: 'Se vuelve siempre a lo mismo. Se trata de a qué altura se vuelve.',
}
# Subtítulos escritos con mayúscula en cada palabra: en la tarjeta, como frase.
FRASE = {4: 'Comunicar desde el centro en tiempos de ruido'}

INI, FIN = '<!-- tarjeta para compartir -->', '<!-- /tarjeta para compartir -->'


def txt(s):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()


def libros():
    ix = open(os.path.join(P, 'index.html'), encoding='utf-8').read()
    out = []
    for d, c in re.findall(r'<a href="01_Libros/([^/]+)/index.html" class="libro-card[^"]*">(.*?)</a>', ix, re.S):
        n = int(d[:2])
        tit = txt(re.search(r'libro-titulo">(.*?)</h2>', c, re.S).group(1))
        desc = txt(re.search(r'libro-descripcion">(.*?)</p>', c, re.S).group(1))
        b = open(os.path.join(P, '01_Libros', d, 'index.html'), encoding='utf-8').read()
        b = re.sub(r'<style.*?</style>|<script.*?</script>', '', b, flags=re.S)
        m = re.search(r'class="(subtitulo[\w-]*)"[^>]*>(.*?)</(p|h2|h3|div|span)>', b, re.S)
        sub = SUB.get(n) or FRASE.get(n) or (txt(m.group(2)) if m else '')
        assert sub, d
        out.append(dict(n=n, d=d, tit=tit, sub=sub, desc=desc, c=(n - 1) // 13, k=(n - 1) % 13))
    assert [l['n'] for l in out] == list(range(1, 40)), 'faltan libros en el index'
    return out


def corta(desc, tope=200):
    if len(desc) <= tope:
        return desc
    frases = re.split(r'(?<=[.!?])\s+', desc)
    s = ''
    for f in frases:
        if len(s) + len(f) + 1 > tope:
            break
        s = (s + ' ' + f).strip()
    if not s:
        s = desc[:tope].rsplit(' ', 1)[0] + '…'
    return s


def anillos(lib):
    cx, cy = 600, 160
    radios = [54, 88, 122]
    p = []
    for i, r in enumerate(radios):
        propio = i == lib['c']
        col = CONST[i][1]
        p.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-opacity="%s" stroke-width="1"/>'
                 % (cx, cy, r, col if propio else '#ffffff', '.35' if propio else '.06'))
        for j in range(13):
            a = -math.pi / 2 + 2 * math.pi * j / 13
            x, y = cx + r * math.cos(a), cy + r * math.sin(a)
            if propio and j == lib['k']:
                p.append('<circle cx="%.1f" cy="%.1f" r="16" fill="url(#halo)"/>' % (x, y))
                p.append('<circle cx="%.1f" cy="%.1f" r="6.5" fill="#ecc96e"/>' % (x, y))
            elif propio:
                p.append('<circle cx="%.1f" cy="%.1f" r="3.4" fill="%s" fill-opacity=".85"/>' % (x, y, col))
            else:
                p.append('<circle cx="%.1f" cy="%.1f" r="2.6" fill="#c9a84c" fill-opacity=".28"/>' % (x, y))
    return ('<svg width="1200" height="320" viewBox="0 0 1200 320" xmlns="http://www.w3.org/2000/svg">'
            '<defs><radialGradient id="halo"><stop offset="0" stop-color="#ecc96e" stop-opacity=".55"/>'
            '<stop offset="1" stop-color="#ecc96e" stop-opacity="0"/></radialGradient></defs>'
            + ''.join(p) + '</svg>')


def pagina(lib):
    nombre, col, brillo, fondo = CONST[lib['c']]
    f400 = b64('gelasio-latin-400-normal.woff2')
    f400i = b64('gelasio-latin-400-italic.woff2')
    e = html.escape
    return f'''<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><style>
@font-face{{font-family:G;src:url({f400}) format('woff2');font-weight:400;font-style:normal}}
@font-face{{font-family:G;src:url({f400i}) format('woff2');font-weight:400;font-style:italic}}
html,body{{margin:0;width:1200px;height:630px;overflow:hidden}}
body{{background:radial-gradient(ellipse 900px 420px at 50% -60px,{brillo},transparent 70%),{fondo};
font-family:G,Georgia,serif;color:#efe7d6;text-align:center;position:relative}}
.anillos{{position:absolute;top:0;left:0}}
.kicker{{position:absolute;top:316px;width:100%;font-size:15px;letter-spacing:.42em;text-transform:uppercase;color:{col};opacity:.85}}
h1{{position:absolute;top:350px;left:60px;right:60px;margin:0;font-weight:400;font-size:62px;line-height:1.1;letter-spacing:.02em;white-space:nowrap}}
.sub{{position:absolute;top:444px;left:150px;right:150px;font-style:italic;font-size:28px;line-height:1.35;color:#d9b866}}
.pie{{position:absolute;bottom:34px;width:100%;font-size:15px;letter-spacing:.06em;color:#8f8676}}
.pie b{{font-weight:400;color:#b49a5c}}
</style></head><body>
<div class="anillos">{anillos(lib)}</div>
<div class="kicker">Portal Público · {e(nombre)} · Libro {lib['n']}</div>
<h1 id="t">{e(lib['tit'])}</h1>
<div class="sub" id="s">{e(lib['sub'])}</div>
<div class="pie"><b>soyartur-trinity.github.io/Trinity_Portal_Publico</b> · Obra libre y gratuita · © Lic. Arturo Rodríguez · CC BY-NC-SA 4.0</div>
</body></html>'''


def b64(nombre):
    return 'data:font/woff2;base64,' + base64.b64encode(open(os.path.join(F, nombre), 'rb').read()).decode()


def etiquetas(lib, html_libro):
    e = lambda s: html.escape(s, quote=True)
    url = BASE + '01_Libros/%s/' % lib['d']
    img = BASE + 'assets/og/libro-%02d.jpg' % lib['n']
    titulo = '%s · Libro %d · Portal Público Trinity' % (lib['tit'], lib['n'])
    desc = corta(lib['desc'])
    alt = 'Tres anillos de trece puntos, uno por constelación; encendido, el del libro %d, %s.' % (lib['n'], lib['tit'])
    l = [INI]
    if not re.search(r'<meta\s+name="description"', html_libro):
        l.append('<meta name="description" content="%s">' % e(desc))
    l += ['<meta property="og:type" content="article">',
          '<meta property="og:site_name" content="Trinity · Portal Público">',
          '<meta property="og:locale" content="es_LA">',
          '<meta property="og:title" content="%s">' % e(titulo),
          '<meta property="og:description" content="%s">' % e(desc),
          '<meta property="og:url" content="%s">' % url,
          '<meta property="og:image" content="%s">' % img,
          '<meta property="og:image:width" content="1200">',
          '<meta property="og:image:height" content="630">',
          '<meta property="og:image:alt" content="%s">' % e(alt),
          '<meta name="twitter:card" content="summary_large_image">',
          FIN]
    return '\n    '.join(l)


def escribe_etiquetas(lib):
    ruta = os.path.join(P, '01_Libros', lib['d'], 'index.html')
    h = open(ruta, encoding='utf-8').read()
    h = re.sub(r'\n?\s*' + re.escape(INI) + r'.*?' + re.escape(FIN), '', h, flags=re.S)
    assert 'og:image' not in h, ruta
    bloque = etiquetas(lib, h)
    m = re.search(r'</title>', h)
    assert m and m.start() < h.index('</head>'), ruta
    h = h[:m.end()] + '\n    ' + bloque + h[m.end():]
    open(ruta, 'w', encoding='utf-8').write(h)


async def main():
    ls = libros()
    os.makedirs(os.path.join(P, 'assets/og'), exist_ok=True)
    async with async_playwright() as pw:
        b = await pw.chromium.launch(executable_path=CHROME)
        pg = await b.new_page(viewport={'width': 1200, 'height': 630})
        for lib in ls:
            await pg.set_content(pagina(lib))
            await pg.evaluate('document.fonts.ready')
            # el título, en una línea: se achica hasta que entre
            await pg.evaluate('''() => {const t=document.getElementById('t');let f=62;
                while(t.scrollWidth>t.clientWidth && f>36){f-=2;t.style.fontSize=f+'px'}}''')
            alto = await pg.evaluate("document.getElementById('s').getBoundingClientRect().height")
            assert alto < 120, (lib['d'], alto)
            await pg.screenshot(path=os.path.join(P, 'assets/og/libro-%02d.jpg' % lib['n']), type='jpeg', quality=88)
            escribe_etiquetas(lib)
            print('libro %02d · %s' % (lib['n'], lib['tit']))
        await b.close()

asyncio.run(main())
