#!/usr/bin/env python3
"""
Las tarjetas para compartir de los trece nodos de La Puerta (18 de noviembre de 2026).

Cuando alguien comparte un nodo por WhatsApp, Facebook o LinkedIn, la red muestra esta imagen: la misma
familia que la tarjeta del índice (assets/og/la-puerta.jpg), el arco de trece dovelas con la del nodo
encendida en oro, y debajo «Trinity · La Puerta · Nodo N de 13», el título y el subtítulo del nodo.
Las etiquetas og:… de cada nodo las escribe recortar_puerta.py.

Toma el dibujo del arco del índice de La Puerta y los títulos de recorte_puerta_texto.py. Necesita
Playwright con Chrome y la tipografía Gelasio (la de métrica de Georgia): npm install @fontsource/gelasio.
Uso:
  FUENTES=RUTA/node_modules/@fontsource/gelasio/files python3 tarjetas_puerta.py RUTA/Trinity-
Escribe Trinity-/assets/og/la-puerta-nodo-01.jpg … -13.jpg (1200 × 630).
"""
import asyncio, base64, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recorte_puerta_texto import NODOS
from playwright.async_api import async_playwright

T = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/trinity-'
F = os.environ.get('FUENTES', '/home/claude/work/fuentes/node_modules/@fontsource/gelasio/files')
CHROME = os.environ.get('CHROME', '/usr/bin/google-chrome')

def b64(nombre):
    return 'data:font/woff2;base64,' + base64.b64encode(open(os.path.join(F, nombre), 'rb').read()).decode()

def arco(n):
    ix = open(os.path.join(T, '00_Portal_Trinity/index.html'), encoding='utf-8').read()
    s = re.search(r'<svg class="arco".*?</svg>', ix, re.S).group(0)
    s = re.sub(r'<title[^>]*>.*?</title>', '', s, flags=re.S)
    s = re.sub(r'\saria-labelledby="[^"]*"', '', s)
    # las dovelas como grupos, sin enlaces; la del nodo, encendida
    def dov(m):
        clases, k = m.group(1) or '', int(m.group(2))
        c = 'dovela' + clases + (' aqui' if k == n else '')
        return '<g class="%s">' % c
    s = re.sub(r'<a class="dovela( clave)?" href="#nodo-(\d+)"[^>]*>', dov, s)
    s = s.replace('</a>', '</g>')
    if s.count('class="dovela') != 13 or s.count(' aqui') != 1:
        sys.exit('No se pudo leer el arco del índice.')
    return s

CSS = """
@font-face{font-family:G;src:url('%s');font-style:normal}
@font-face{font-family:G;src:url('%s');font-style:italic}
html,body{margin:0;width:1200px;height:630px;overflow:hidden}
body{box-sizing:border-box;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;padding-top:92px;
  font-family:G,Georgia,serif;color:#f5f0ff;
  background:radial-gradient(ellipse 85%% 75%% at 50%% 0%%,#2b1a48 0%%,rgba(43,26,72,0) 70%%),#0a0614}
.arco{width:330px;height:auto;overflow:visible}
.vano{fill:url(#luz);opacity:.85}
.jamba{fill:rgba(167,123,255,.05);stroke:rgba(167,123,255,.32);stroke-width:1}
.imposta,.piso{stroke:rgba(167,123,255,.32);stroke-width:1.2}
.umbral{fill:rgba(236,201,110,.16);stroke:rgba(236,201,110,.55);stroke-width:.8}
.centro-aro{fill:none;stroke:rgba(236,201,110,.55);stroke-width:1}
.centro{fill:#ecc96e}
.dovela path{fill:#1d1232;stroke:#a77bff;stroke-width:1.3;stroke-linejoin:round}
.dovela text{fill:#f5f0ff;font-family:G,Georgia,serif;font-size:19px;text-anchor:middle}
.dovela.clave path{stroke:#ecc96e;stroke-width:1.9;fill:#2a1a3c}
.dovela.clave text{fill:#ecc96e}
.dovela.aqui path{fill:#5a4320;stroke:#ecc96e;stroke-width:2.4}
.dovela.aqui text{fill:#fff3cf}
.serie{margin:34px 0 0;font-size:18px;letter-spacing:.42em;padding-left:.42em;text-transform:uppercase;color:rgba(245,240,255,.56)}
h1{margin:14px 0 0;font-weight:normal;text-transform:uppercase;letter-spacing:.12em;padding-left:.12em;font-size:50px;line-height:1.15;
  white-space:nowrap;text-align:center}
.sub{margin:18px 0 0;font-style:italic;font-size:28px;color:#ecc96e;text-align:center;max-width:1000px}
"""

def pagina(n):
    d = NODOS[n]
    css = CSS % (b64('gelasio-latin-400-normal.woff2'), b64('gelasio-latin-400-italic.woff2'))
    return ('<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><style>%s</style></head><body>%s'
            '<p class="serie">Trinity · La Puerta · Nodo %d de 13</p><h1>%s</h1><p class="sub">%s</p></body></html>'
            % (css, arco(n), n, d['titulo'], d['sub']))

async def main():
    salida = os.path.join(T, 'assets/og')
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path=CHROME)
        c = await b.new_context(viewport={'width': 1200, 'height': 630}, device_scale_factor=1)
        for n in range(1, 14):
            pg = await c.new_page()
            await pg.set_content(pagina(n))
            await pg.evaluate('document.fonts.ready')
            # un título largo se achica hasta caber en una línea
            tam = await pg.evaluate("""()=>{const h=document.querySelector('h1');let s=50;
                while(h.scrollWidth>1100 && s>30){s-=1;h.style.fontSize=s+'px'} return s}""")
            ruta = os.path.join(salida, 'la-puerta-nodo-%02d.jpg' % n)
            await pg.screenshot(path=ruta, type='jpeg', quality=88)
            print(os.path.basename(ruta), tam, os.path.getsize(ruta) // 1024, 'KB')
            await pg.close()
        await b.close()

if __name__ == '__main__':
    asyncio.run(main())
