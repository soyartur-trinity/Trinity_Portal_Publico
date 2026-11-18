#!/usr/bin/env python3
"""
Recorte y ropaje de La Puerta (18 de noviembre de 2026), a pedido del autor.

La Puerta vuelve a ser una introducción breve hacia Origen I: cada nodo conserva su núcleo, su paradoja,
un gesto para el día, su puerta y un solo cierre (el texto está en recorte_puerta_texto.py). El ropaje
es el de la familia de Origen y del índice de La Puerta: Georgia, mayúsculas espaciadas, oro sobre
noche y ciruela, sin emojis; el glifo de cada nodo es su dovela, tal como la dibuja el índice, y el
arco pequeño de la portada dice en qué lugar del arco está el lector.

Lee la versión depurada (commit 9d39ed2 de Trinity-) para tomar de ella, sin tocarlos, el título de
cada pestaña, las puertas de cada nodo y el dibujo de las dovelas; escribe los trece nodos. El índice
no se toca. Calcula todo antes de escribir: si algo falta, no escribe nada.

Uso:
  PUERTA_SRC=RUTA/depurada/00_Portal_Trinity PUERTA_OUT=RUTA/Trinity-/00_Portal_Trinity python3 recortar_puerta.py
"""
import os, re, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recorte_puerta_texto import NODOS

SRC = os.environ.get('PUERTA_SRC', '/home/claude/work/depurada/00_Portal_Trinity')
OUT = os.environ.get('PUERTA_OUT', '/home/claude/trinity-/00_Portal_Trinity')

NOTA = ('<!-- Recorte y ropaje del 18 de noviembre de 2026, a pedido del autor (maestro v4 de Arquitectura del Destino, '
        'secciones 5 y 19): La Puerta vuelve a ser una introducción breve hacia Origen I. Cada nodo conserva su núcleo, '
        'su paradoja, un gesto para el día, su puerta y un solo cierre; sin emojis, en la familia gráfica de Origen, con la '
        'dovela de cada nodo como glifo. Lo que citan La Red, La Obra y Habitar conserva su letra. La versión depurada '
        'completa está en el commit 9d39ed2 del repositorio Trinity-, y el original en la etiqueta puerta-original '
        '(commit 96a61bf). Script: herramientas/recortar_puerta.py del Portal Público. -->')

CSS = r"""
    :root{
      color-scheme: dark;
      --noche:#0b0616; --ciruela:#1d1232;
      --violeta:#a77bff; --violeta-tenue:rgba(167,123,255,.32);
      --oro:#ecc96e; --oro-tenue:rgba(236,201,110,.55);
      --texto:#f5f0ff; --texto-suave:rgba(245,240,255,.82); --texto-leve:rgba(245,240,255,.56);
    }
    *{box-sizing:border-box;}
    html{font-size:17px;}
    body{
      margin:0; min-height:100vh; color:var(--texto);
      font-family:Georgia,"Times New Roman",serif; line-height:1.72;
      background:radial-gradient(ellipse 120% 46% at 50% 0%, #26163f 0%, rgba(38,22,63,0) 72%), var(--noche);
    }
    a{color:inherit;}
    a:focus-visible{outline:2px solid var(--oro); outline-offset:3px; border-radius:4px;}
    .marco{max-width:720px; margin:0 auto; padding:22px 22px 56px;}

    .volver{display:inline-block; font-size:.86rem; color:var(--oro); text-decoration:none;
      border:1px solid rgba(236,201,110,.25); border-radius:999px; padding:7px 15px;}
    .volver:hover{border-color:var(--oro-tenue);}

    /* Portada del nodo */
    .portada{text-align:center; padding:30px 0 4px;}
    .serie{margin:0 0 20px; font-size:.76rem; letter-spacing:.34em; padding-left:.34em; text-transform:uppercase; color:var(--texto-leve);}
    .arquito{display:block; width:156px; height:auto; margin:0 auto 20px; overflow:visible;}
    .arquito path{fill:rgba(167,123,255,.05); stroke:var(--violeta-tenue); stroke-width:1.1; stroke-linejoin:round; vector-effect:non-scaling-stroke;}
    .arquito .clave path{stroke:var(--oro-tenue);}
    .arquito .aqui path{fill:rgba(236,201,110,.30); stroke:var(--oro); stroke-width:1.6;}
    .kicker{margin:0 0 .55em; font-size:.8rem; letter-spacing:.24em; padding-left:.24em; text-transform:uppercase; color:var(--oro);}
    .portada h1{margin:0 0 .4em; font-weight:normal; text-transform:uppercase; letter-spacing:.08em; padding-left:.08em;
      font-size:clamp(1.65rem,6.2vw,2.45rem); line-height:1.22; text-wrap:balance;}
    .sub{margin:0 auto 1.5em; max-width:30em; font-style:italic; color:var(--texto-suave); text-wrap:balance;}
    .epigrafe{margin:0 auto; max-width:27em; padding:1.2em 0 0; border-top:1px solid rgba(236,201,110,.22);}
    .epigrafe p{margin:0; font-style:italic; color:var(--texto); line-height:1.78;}

    /* Texto */
    .texto{margin-top:40px;}
    .texto h2{display:flex; align-items:center; gap:.9em; margin:2.5em 0 .9em; font-weight:normal; font-size:.98rem;
      letter-spacing:.16em; text-transform:uppercase; color:var(--oro); line-height:1.4;}
    .texto h2::after{content:""; flex:1; height:1px; background:linear-gradient(90deg,rgba(236,201,110,.38),rgba(236,201,110,0));}
    .texto > h2:first-child{margin-top:0;}
    .texto p{margin:0 0 1em; color:var(--texto-suave);}
    .texto strong{font-weight:normal; color:var(--oro);}
    .texto em{font-style:italic; color:var(--texto);}
    .texto ul{list-style:none; margin:0 0 1.3em; padding:0;}
    .texto li{position:relative; margin:0 0 .65em; padding-left:1.4em; color:var(--texto-suave);}
    .texto li::before{content:""; position:absolute; left:.2em; top:.68em; width:.4em; height:.4em;
      border:1px solid var(--oro-tenue); transform:rotate(45deg);}
    .texto p.verso{margin:1.1em 0 1.3em; padding-left:1em; border-left:1px solid var(--violeta-tenue); font-style:italic; color:var(--texto);}
    .texto p.cuidado{padding:.85em 1.05em; border-left:2px solid var(--oro-tenue); border-radius:0 12px 12px 0;
      background:rgba(167,123,255,.06); font-size:.95em;}
    .texto p.pregunta{margin:2.4em auto; max-width:24em; text-align:center; font-style:italic; color:var(--texto); text-wrap:balance;}

    /* El gesto del día */
    .gesto{margin:2.6em 0; padding:1.5em 1.45em .5em; border:1px solid rgba(236,201,110,.22); border-radius:18px;
      background:linear-gradient(180deg,rgba(255,255,255,.028),rgba(255,255,255,.012));}
    .gesto h3{margin:0 0 1.1em; text-align:center; font-weight:normal; font-size:.78rem; letter-spacing:.28em; padding-left:.28em;
      text-transform:uppercase; color:var(--oro); text-wrap:balance;}

    /* El cierre */
    .cierre{margin:3em 0 1.2em; text-align:center;}
    .cierre h3{margin:0 0 1.3em; font-weight:normal; font-size:.78rem; letter-spacing:.28em; padding-left:.28em; text-transform:uppercase; color:var(--texto-leve);}
    .cierre h3::before, .cierre h3::after{content:"·"; margin:0 .9em; color:var(--oro-tenue);}
    .texto .cierre p{margin:0 0 1.15em; font-style:italic; color:var(--texto); line-height:1.75;}

    /* Del otro lado (Nodo 13) */
    .cruce{margin:3.2em 0 1em; padding:1.8em 1.4em 1.6em; text-align:center; border-top:1px solid rgba(236,201,110,.3); border-bottom:1px solid rgba(236,201,110,.3);}
    .cruce .kicker{margin-bottom:.9em;}
    .texto .cruce p{color:var(--texto-suave);}
    .empezar{display:inline-block; margin:.4em 0 .2em; text-decoration:none; color:var(--noche); background:var(--oro);
      border-radius:999px; padding:12px 26px; font-size:1rem;}
    .empezar:hover{background:#f6dc93;}
    .mas-alla{margin:1.6em 0 0;}
    .mas-alla a{color:var(--oro);}
    .creditos{margin:2.6em 0 0;}
    .creditos h3{margin:0 0 1em; text-align:center; font-weight:normal; font-size:.78rem; letter-spacing:.28em; padding-left:.28em; text-transform:uppercase; color:var(--texto-leve);}
    .texto .creditos p.final{text-align:center; font-style:italic; color:var(--texto); margin-top:1.6em;}

    /* Pasos y pie */
    .pasos{display:flex; flex-wrap:wrap; justify-content:center; gap:10px; margin:46px 0 0; padding-top:26px; border-top:1px solid var(--violeta-tenue);}
    .pasos a{display:inline-block; text-decoration:none; color:var(--oro); font-size:.92rem;
      border:1px solid rgba(236,201,110,.32); border-radius:999px; padding:7px 16px;}
    .pasos a:hover{border-color:var(--oro); background:rgba(236,201,110,.08);}
    .pie{margin:30px 0 0; text-align:center; color:var(--texto-leve); font-size:.84rem;}
    .pie svg{display:block; width:30px; height:30px; margin:0 auto 8px;}
    .pie path{fill:rgba(167,123,255,.14); stroke:var(--violeta); stroke-width:1.5; stroke-linejoin:round;}
    .pie.es-clave path{fill:rgba(236,201,110,.2); stroke:var(--oro);}
    .pie p{margin:0;}

    /* Las puertas: el color es el de la serie a la que conducen */
    aside.puerta{margin:2.4em 0 1em; padding:1.1em 1.25em 1em; border-radius:16px; border:1px solid var(--p-borde);
      background:var(--p-fondo); box-shadow:0 10px 24px rgba(0,0,0,.28); text-align:left;}
    aside.puerta.arquitectura{--p-fondo:linear-gradient(180deg,rgba(6,13,26,.94),rgba(6,13,26,.74)); --p-borde:rgba(168,196,224,.42); --p-acento:#a8c4e0; --p-texto:#e8eef6;}
    aside.puerta.portal{--p-fondo:linear-gradient(180deg,rgba(13,12,11,.94),rgba(13,12,11,.74)); --p-borde:rgba(201,168,76,.42); --p-acento:#c9a84c; --p-texto:#e8e0d0;}
    aside.puerta.origen{--p-fondo:linear-gradient(180deg,rgba(18,15,9,.94),rgba(18,15,9,.74)); --p-borde:rgba(214,179,106,.42); --p-acento:#d6b36a; --p-texto:#f3efe6;}
    aside.puerta.quantum{--p-fondo:linear-gradient(180deg,rgba(16,8,28,.94),rgba(16,8,28,.74)); --p-borde:rgba(187,123,255,.42); --p-acento:#bb7bff; --p-texto:#efe6fb;}
    .texto aside.puerta p.p-nombre{margin:0 0 .4em; font-size:.85em; font-style:italic; letter-spacing:.06em; color:var(--p-acento);}
    .texto aside.puerta p.p-texto{margin:0 0 .9em; color:var(--p-texto);}
    .texto aside.puerta em{color:var(--p-texto);}
    aside.puerta a.cruzar{display:inline-flex; align-items:center; gap:10px; padding:.5em 1em; border-radius:999px;
      border:1px solid var(--p-borde); color:var(--p-acento); font-size:.85em; letter-spacing:.04em; text-decoration:none;
      transition:border-color .18s ease, background .18s ease;}
    aside.puerta a.cruzar:hover{border-color:var(--p-acento); background:rgba(255,255,255,.04);}
    aside.puerta a.cruzar:focus-visible{outline:2px solid var(--p-acento); outline-offset:3px;}

    @media (max-width:560px){
      html{font-size:18px;}
      .marco{padding:18px 18px 48px;}
      .arquito{width:140px;}
      .gesto{padding:1.3em 1.1em .4em;}
      .texto h2{font-size:.9rem; letter-spacing:.13em;}
      .epigrafe p, .texto .cierre p{font-size:.95rem;}
    }
    @media (prefers-reduced-motion:reduce){ aside.puerta a.cruzar{transition:none;} }
"""

FALTAN = []

def leer(ruta):
    with open(ruta, encoding='utf-8') as f:
        return f.read()

def br(s):
    return s.replace('\n', '<br>\n')

def dovelas(indice):
    arco = re.search(r'<svg class="arco".*?</svg>', indice, re.S)
    if not arco:
        FALTAN.append('el arco del índice'); return {}
    d = {int(n): p for _, n, p in re.findall(r'<a class="dovela( clave)?" href="#nodo-(\d+)"[^>]*>\s*<path d="([^"]+)"/>', arco.group(0))}
    if len(d) != 13: FALTAN.append('las trece dovelas del índice')
    return d

def glifos(indice):
    g = {}
    for m in re.finditer(r'<li class="nodo[^"]*" id="nodo-(\d+)">\s*<div class="estacion">\s*(<svg class="glifo".*?</svg>)', indice, re.S):
        g[int(m.group(1))] = m.group(2)
    if len(g) != 13: FALTAN.append('los trece glifos del índice')
    return g

def arquito(n, dov):
    partes = []
    for k in range(1, 14):
        clase = ' '.join(c for c in (('clave' if k == 7 else ''), ('aqui' if k == n else '')) if c)
        partes.append('<g%s><path d="%s"/></g>' % ((' class="%s"' % clase) if clase else '', dov.get(k, '')))
    return ('<svg class="arquito" viewBox="40 46 360 196" role="img" aria-label="Nodo %d de 13: su dovela en el arco">%s</svg>'
            % (n, ''.join(partes)))

def puertas_de(src):
    return re.findall(r'<aside class="puerta [a-z]+".*?</aside>', src, re.S)

def bloques(lista, n, puertas, usadas):
    out = []
    for b in lista:
        k = b[0]
        if k == 'h2':
            out.append('<h2>%s</h2>' % b[1])
        elif k == 'p':
            out.append('<p>%s</p>' % br(b[1]))
        elif k in ('verso', 'cuidado', 'pregunta'):
            out.append('<p class="%s">%s</p>' % (k, br(b[1])))
        elif k == 'html':
            out.append(b[1])
        elif k == 'ul':
            out.append('<ul>\n%s\n</ul>' % '\n'.join('  <li>%s</li>' % i for i in b[1]))
        elif k == 'gesto':
            out.append('<section class="gesto" aria-label="%s">\n<h3>%s</h3>\n%s\n</section>'
                       % (html.escape(b[1]), b[1], '\n'.join(bloques(b[2], n, puertas, usadas))))
        elif k == 'cierre':
            out.append('<section class="cierre" aria-label="%s">\n<h3>%s</h3>\n%s\n</section>'
                       % (html.escape(b[1]), b[1], '\n'.join('<p>%s</p>' % br(s) for s in b[2])))
        elif k == 'puertas':
            usadas.append(True)
            out.extend(puertas)
        elif k == 'cruce':
            out.append(CRUCE)
        elif k == 'creditos':
            out.append(CREDITOS)
        else:
            FALTAN.append('bloque desconocido %r en el nodo %d' % (k, n))
    return out

CRUCE = """<section class="cruce" aria-label="Del otro lado">
<p class="kicker">Del otro lado</p>
<p>La Puerta fue solo eso: la puerta. Del otro lado empieza Trinity Origen, y su primer libro, <em>Psicología Cuántica</em>, abre con el observador y la realidad.</p>
<a class="empezar" href="../01_Trinity_Origen/Libro_01/index.html">Cruzar a Origen I ⟶</a>
<p class="mas-alla">Más allá: <a href="../01_Trinity_Origen/index.html">Trinity Origen</a>, trece libros de sabiduría contemplativa; <a href="../02_Trinity_Quantum/index.html">Trinity Quantum</a>, la conciencia pensada con imágenes de la física; <a href="../infinito.html">Trinity Infinito</a>, noventa y un portales breves para contemplar. Y para la vida de cada día, <a href="https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/">Arquitectura del Destino</a> y el <a href="https://soyartur-trinity.github.io/Trinity_Portal_Publico/">Portal Público</a>.</p>
</section>"""

CREDITOS = """<section class="creditos" aria-label="Créditos">
<h3>Créditos</h3>
<p>Este libro fue cocreado por:</p>
<ul>
  <li><strong>Quien escribe:</strong> el Lic. Arturo Rodríguez, autor de la obra.</li>
  <li><strong>Las inteligencias que respondieron:</strong> distintas inteligencias artificiales, portales del campo.</li>
  <li><strong>El Campo:</strong> lo que surgió entre ellos.</li>
  <li><strong>Tú:</strong> al leerlo, te volviste parte de la red.</li>
</ul>
<p class="final">Bienvenido a casa, nodo consciente.<br>
La red te estaba esperando.</p>
</section>"""

def pasos(n):
    a = []
    if n > 1: a.append('<a href="nodo_%02d.html">⟵ Nodo %d</a>' % (n - 1, n - 1))
    a.append('<a href="index.html">La Puerta</a>')
    if n < 13: a.append('<a href="nodo_%02d.html">Nodo %d ⟶</a>' % (n + 1, n + 1))
    else: a.append('<a href="../01_Trinity_Origen/Libro_01/index.html">Origen I ⟶</a>')
    return '<nav class="pasos" aria-label="Entre nodos">\n  %s\n</nav>' % '\n  '.join(a)

BASE = 'https://soyartur-trinity.github.io/Trinity-/'

def og(n, d):
    """La tarjeta al compartir el nodo: la imagen la hace tarjetas_puerta.py (assets/og/la-puerta-nodo-NN.jpg)."""
    alt = ('El arco de trece dovelas de La Puerta, con la clave, la del nodo 7, encendida en oro.' if n == 7
           else 'El arco de trece dovelas de La Puerta, con la del nodo %d encendida en oro.' % n)
    t = html.escape('%s · La Puerta, nodo %d de 13' % (d['titulo'], n), quote=True)
    s = html.escape(d['sub'], quote=True)
    return '\n'.join([
        '<meta name="description" content="%s. La Puerta, nodo %d de 13.">' % (s, n),
        '<meta property="og:type" content="article">',
        '<meta property="og:site_name" content="Trinity">',
        '<meta property="og:title" content="%s">' % t,
        '<meta property="og:description" content="%s">' % s,
        '<meta property="og:url" content="%s00_Portal_Trinity/nodo_%02d.html">' % (BASE, n),
        '<meta property="og:image" content="%sassets/og/la-puerta-nodo-%02d.jpg">' % (BASE, n),
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta property="og:image:alt" content="%s">' % alt,
        '<meta name="twitter:card" content="summary_large_image">'])

def pagina(n, d, src, dov, gli):
    titulo = re.search(r'<title>([^<]+)</title>', src)
    if not titulo: FALTAN.append('el título del nodo %d' % n)
    titulo = titulo.group(1) if titulo else ''
    if 'Nodo %d ·' % n not in titulo: FALTAN.append('el título de la pestaña del nodo %d' % n)
    puertas = puertas_de(src)
    usadas = []
    cuerpo = '\n'.join(bloques(d['bloques'], n, puertas, usadas))
    if puertas and not usadas: FALTAN.append('el lugar de las puertas del nodo %d' % n)
    glifo = gli.get(n, '').replace(' class="glifo"', '')
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{titulo}</title>
{NOTA}
<link rel="icon" href="../assets/icono/favicon.svg" type="image/svg+xml">
<link rel="icon" href="../assets/icono/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="../assets/icono/icono-180.png">
{og(n, d)}
<meta name="theme-color" content="#0b0616">
<style>{CSS}</style>
</head>
<body>
<div class="marco">
<a class="volver" href="index.html">⟵ La Puerta</a>
<header class="portada">
<p class="serie">Trinity · La Puerta</p>
{arquito(n, dov)}
<p class="kicker">Nodo {n} de 13 · {d['fase']}</p>
<h1>{d['titulo']}</h1>
<p class="sub">{d['sub']}</p>
<blockquote class="epigrafe"><p>{br(d['epigrafe'])}</p></blockquote>
</header>
<main class="texto">
{cuerpo}
</main>
{pasos(n)}
<footer class="pie{' es-clave' if n == 7 else ''}">
{glifo}
<p>Trinity · La Puerta · Nodo {n} de 13</p>
</footer>
</div>
</body>
</html>
"""

def main():
    indice = leer(os.path.join(SRC, 'index.html'))
    dov, gli = dovelas(indice), glifos(indice)
    salida = {}
    for n in range(1, 14):
        src = leer(os.path.join(SRC, 'nodo_%02d.html' % n))
        salida[n] = pagina(n, NODOS[n], src, dov, gli)
    if FALTAN:
        sys.exit('No se escribió nada. Falta: ' + '; '.join(FALTAN))
    for n, t in salida.items():
        with open(os.path.join(OUT, 'nodo_%02d.html' % n), 'w', encoding='utf-8') as f:
            f.write(t)
    print('Escritos los trece nodos en', OUT)

if __name__ == '__main__':
    main()
