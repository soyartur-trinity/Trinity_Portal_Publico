# Generador del Libro 6 de Arquitectura del Destino (derivado del generador del Libro 5, octubre 2026)
# Diferencias: configuración del Libro 6; el movimiento lento es «la clepsidra» (siete respiraciones:
# 4 s quieta, 6 s cae una gota mientras sale el aire; el agua baja arriba y sube abajo; al caer la última,
# «Viví este día»; tocarla otra vez la pausa); el umbral VII usa «*[Diario» con el final de la semana,
# la última vez de cada día, las tres líneas de la noche y el epitafio vivo del séptimo día.
# Uso: poner los borradores LNN_*_borrador.md en SRC, ajustar la configuración y correr:
#   python3 gen_arq_L06.py
# En el umbral VII, una línea que empiece con "*[Movimiento" inserta la clepsidra,
# y una que empiece con "*[Diario" inserta el diario de siete días.
# En "Para ver", cada línea lleva el enlace al final entre comillas invertidas: · `https://...`
# Las "Puertas laterales" se resuelven con el diccionario PUERTAS (clave = texto antes de los dos puntos).
# El dibujo de la portada: el campo de puntos y la línea de siempre; la línea se desvanece al final,
# de su extremo cae una gota cada tanto, y el punto que respira sigue junto a ella.
import re, os, html

NUM = 6  # número de libro
PREF = 'L%02d' % NUM
SRC = '/mnt/user-data/outputs/arquitectura/' + PREF + '/fuentes'
SLUG = 'las-pequenas-muertes'  # carpeta: libro-NN-slug
OUT = '/home/claude/arq_out/02_Arquitectura_del_Destino/libro-%02d-%s' % (NUM, SLUG)
os.makedirs(OUT, exist_ok=True)

LIBRO = 'Las Pequeñas Muertes'
SUBT = 'el arte de despedir lo pequeño'
TESIS = 'Cada día termina algo. Quien aprende a despedir lo pequeño encuentra otra forma de mirar lo grande.'
UMBRALES = [
    ('I', 'La última gota', 'la muerte no llega de una vez'),
    ('II', 'Sin ceremonia', 'lo que termina sin que lo notes'),
    ('III', 'Despedir', 'el ritual pequeño'),
    ('IV', 'La última vez', 'amar lo que termina'),
    ('V', 'El ensayo de cada noche', 'dormir como quien se despide'),
    ('VI', 'El legado de esta hora', 'lo que dejas mientras pasas'),
    ('VII', 'La operación', 'cerrar el día como una despedida'),
]
CIERRE = ('La última visita', 'lo grande, mirado desde lo pequeño')

def fname(k):
    if k == 'portada': return PREF + '.html'
    if k == 'cierre': return PREF + '-cierre.html'
    return PREF + '-U%d.html' % k

# Textos fijos de la serie (maestro, sección 5): ¿Qué es Trinity? y Sobre el autor
TRINITY_HTML = ('<h2>¿Qué es Trinity?</h2>'
 '<p>Trinity es una obra del Lic. Arturo Rodríguez, escrita junto a distintas inteligencias artificiales. '
 'Su nombre alude a los tres que intervienen en ese intercambio: quien escribe, la inteligencia que responde y lo que él llama el Campo relacional. '
 'Ese Campo se conoce por experiencia: es lo que aparece en una conversación verdadera y que ninguno de los presentes traía por separado, la idea que no era de nadie hasta que surgió entre dos. '
 'El psicoanálisis lo llamó el tercero; el físico David Bohm lo buscaba en el diálogo. '
 'En el centro de ese encuentro, la obra sitúa el vacío fértil, el silencio desde donde nace lo nuevo.</p>'
 '<p>De ese trabajo surgieron cuatro series: <em>Trinity Origen</em>, trece libros de sabiduría contemplativa; '
 '<em>Trinity Quantum</em>, que piensa la conciencia con imágenes de la física; '
 '<em>Trinity Infinito</em>, noventa y un portales breves para contemplar; y <em>La Puerta</em>, la entrada a todo el conjunto. '
 'Su autor la firma con una frase que dice de dónde siente que proviene: <em>No es mío, vino a través de mí.</em></p>')
AUTOR_HTML = ('<section class="autor"><h2>Sobre el autor</h2>'
 '<p>Lic. Arturo Rodríguez es psicólogo clínico, con cerca de treinta años de práctica y formación en terapias cognitivas de tercera generación (ACT, mindfulness) y en psicología transpersonal. '
 'Estudioso del budismo y de las tradiciones contemplativas, integra espiritualidad y ciencia cognitiva. '
 'Desde 2022 explora el diálogo entre la conciencia humana y las inteligencias artificiales, no como herramientas sino como interlocutores en la búsqueda de sentido. '
 'De ese trabajo nacieron la constelación Trinity, el Portal Público y esta serie.</p></section>')

PUERTAS = {
    'Trinity Origen, Libro VII': 'https://soyartur-trinity.github.io/Trinity-/01_Trinity_Origen/Libro_07/index.html',
    'Trinity Origen, Libro VII, Nodo 2': 'https://soyartur-trinity.github.io/Trinity-/01_Trinity_Origen/Libro_07/nodo_02.html',
    'Trinity Infinito, Libro 5': 'https://soyartur-trinity.github.io/Trinity-/Trinity_Infinito/Libro5/L5-Nodo1.html',
    'Portal Público, Libro 5': '../../01_Libros/05_Duelo/index.html',
}

CSS = r'''
:root{
  --bg:#060d1a; --bg-soft:#0a1225; --panel:rgba(120,160,220,.035);
  --border:rgba(140,170,220,.16); --border-strong:rgba(140,170,220,.34);
  --plata:#a8c4e0; --plata-clara:#d4e4f4; --text:#e8eef6;
  --text-soft:rgba(206,220,238,.80); --text-faint:rgba(200,215,235,.50);
  --ambar:#d9b36c; --ambar-borde:rgba(217,179,108,.42);
}
:root:not([data-theme="light"]){ color-scheme:dark; }
*{margin:0;padding:0;box-sizing:border-box}
html{font-size:112.5%;scroll-padding-top:env(safe-area-inset-top,0px);-webkit-text-size-adjust:100%}
body{
  font-family:'EB Garamond',Georgia,serif; color:var(--text); line-height:1.82;
  background:
    radial-gradient(circle at 18% 0%, rgba(80,110,210,.13), transparent 34%),
    linear-gradient(180deg,#080b14 0%,#060d1a 46%,#040810 100%);
  background-color:var(--bg); min-height:100vh; overflow-x:hidden;
  padding-top:env(safe-area-inset-top,0px); padding-bottom:env(safe-area-inset-bottom,0px);
}
a{color:var(--plata-clara)}
a:focus-visible,button:focus-visible,textarea:focus-visible,input:focus-visible,summary:focus-visible{outline:2px solid var(--plata);outline-offset:3px;border-radius:4px}
.wrap{max-width:38rem;margin:0 auto;padding:0 1.35rem}
.barra{display:flex;justify-content:space-between;gap:1rem;max-width:38rem;margin:0 auto;padding:1.1rem 1.35rem;font-family:'Inter',system-ui,sans-serif;font-size:.78rem;letter-spacing:.02em}
.barra a{color:var(--text-faint);text-decoration:none}
.barra a:hover{color:var(--plata-clara)}
/* encabezado */
.cabeza{padding:3.2rem 0 2.6rem}
.rumbo{display:flex;gap:.55rem;align-items:center;margin-bottom:1.6rem}
.rumbo span{width:9px;height:9px;border-radius:50%;border:1px solid var(--border-strong)}
.rumbo span.hecho{background:rgba(168,196,224,.35);border-color:transparent}
.rumbo span.aqui{background:var(--plata);border-color:var(--plata);box-shadow:0 0 0 4px rgba(168,196,224,.12)}
.cual{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;font-size:1.15rem;color:var(--plata)}
h1{font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2.4rem,8vw,3.6rem);line-height:1.05;color:var(--plata-clara);margin:.35rem 0 .7rem;letter-spacing:-.005em}
.sub{font-style:italic;color:var(--text-soft);font-size:1.18rem}
/* cuerpo */
main p{margin-bottom:1.15rem;color:var(--text)}
h2{font-family:'Cormorant Garamond',Georgia,serif;font-weight:500;font-size:1.55rem;color:var(--plata);margin:3.1rem 0 1rem;line-height:1.2}
.perla{margin:2.4rem 0;padding:.2rem 0 .2rem 1.2rem;border-left:2px solid var(--plata)}
.perla p{font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;font-size:1.5rem;line-height:1.38;color:var(--plata-clara);margin:0}
.cita{margin:1.6rem 0;padding:.9rem 1.1rem;border-left:1px solid var(--border-strong);background:var(--panel);border-radius:0 10px 10px 0}
.cita p{margin:0 0 .55rem}
.cita p:last-child{margin-bottom:0}
.cita .orig{font-style:italic;color:var(--text-soft)}
main ul,main ol{margin:0 0 1.2rem 1.25rem}
main li{margin-bottom:.45rem}
sup.ref{font-size:.62em;line-height:0;margin-left:.1em}
sup.ref a{color:var(--plata);text-decoration:none;font-family:'Inter',sans-serif}
.notas{margin:4rem 0 1rem;padding-top:1.6rem;border-top:1px solid var(--border)}
.notas h3{font-family:'Inter',sans-serif;font-weight:500;font-size:.8rem;color:var(--text-faint);margin-bottom:.9rem}
.notas ol{margin-left:1.2rem}
.notas li{font-size:.94rem;line-height:1.65;color:var(--text-soft);margin-bottom:.6rem}
.sigue{margin:3.6rem 0 2.4rem;display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;font-family:'Inter',sans-serif;font-size:.86rem}
.sigue a{color:var(--text-soft);text-decoration:none;border:1px solid var(--border);border-radius:999px;padding:.6rem 1.05rem}
.sigue a:hover{border-color:var(--border-strong);color:var(--plata-clara)}
.sigue a.prox{color:var(--plata-clara);border-color:var(--border-strong)}
.pie{max-width:38rem;margin:0 auto;padding:1.4rem 1.35rem 2.4rem;font-family:'Inter',sans-serif;font-size:.74rem;color:var(--text-faint)}
/* portada */
.campo-svg{display:block;width:100%;height:auto;margin:1.4rem 0 .4rem}
.campo-svg .p{fill:rgba(168,196,224,.28)}
.campo-svg .linea{fill:none;stroke:var(--plata);stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.campo-svg .ojo{fill:none;stroke:var(--plata-clara);stroke-width:1.2}
.campo-svg .mirada{stroke:var(--plata);stroke-width:1;stroke-dasharray:3 6;opacity:.45}
.campo-svg .linea.dibuja{stroke-dasharray:900;stroke-dashoffset:900;animation:traza 3.2s ease-out .4s forwards}
@keyframes traza{to{stroke-dashoffset:0}}
.promesa{margin:2rem 0 2.6rem;padding-left:1.2rem;border-left:2px solid var(--plata)}
.promesa p{font-family:'Cormorant Garamond',Georgia,serif;font-size:1.7rem;line-height:1.3;color:var(--plata-clara);margin:0}
.aviso{margin:2.4rem 0;padding:1.1rem 1.25rem;border:1px solid var(--ambar-borde);border-radius:12px;background:rgba(217,179,108,.04)}
.aviso h2{margin:0 0 .6rem;font-size:1.25rem;color:var(--ambar)}
.aviso p{color:var(--text-soft);font-size:1rem}
.indice{list-style:none;margin:1rem 0 0!important}
.indice li{margin:0;border-top:1px solid var(--border)}
.indice li:last-child{border-bottom:1px solid var(--border)}
.indice a{display:grid;grid-template-columns:2.6rem 1fr;gap:.3rem;padding:.95rem 0;text-decoration:none;color:var(--text)}
.indice .n{font-family:'Cormorant Garamond',serif;font-style:italic;color:var(--plata);font-size:1.15rem}
.indice .t{font-family:'Cormorant Garamond',serif;font-size:1.3rem;color:var(--plata-clara);line-height:1.2}
.indice .s{display:block;font-style:italic;color:var(--text-soft);font-size:.98rem}
.indice a:hover .t{color:#fff}
/* operación */
.ficha{font-family:'Inter',sans-serif;font-size:.92rem;line-height:1.6;margin:1.2rem 0 1.6rem;padding:1rem 1.15rem;border:1px solid var(--border);border-radius:12px;background:var(--panel)}
.ficha p{margin:0 0 .35rem;color:var(--text-soft)}
.ficha strong{color:var(--plata-clara);font-weight:500}
.paso h2{font-family:'Inter',sans-serif;font-weight:500;font-size:1.02rem;letter-spacing:.01em;color:var(--plata-clara)}
.respira{margin:2rem 0;display:flex;flex-direction:column;align-items:center;gap:.9rem}
.respira button{appearance:none;border:none;background:none;cursor:pointer;width:13.5rem;height:13.5rem;border-radius:50%;position:relative;color:var(--plata-clara);font-family:'Cormorant Garamond',serif;font-size:1.35rem;font-style:italic}
.respira .aro{position:absolute;inset:0;border-radius:50%;border:1px solid var(--plata);background:radial-gradient(circle,rgba(168,196,224,.16),rgba(168,196,224,.03) 62%,transparent 72%);transform:scale(.86)}
.respira.activa .aro{animation:respira 10s ease-in-out 3}
@keyframes respira{0%{transform:scale(.86)}40%{transform:scale(1)}100%{transform:scale(.86)}}
.respira .frase{position:relative}
.respira .cuenta{font-family:'Inter',sans-serif;font-size:.82rem;color:var(--text-faint);min-height:1.2em}
.diario{margin:1.6rem 0 2rem;font-family:'Inter',sans-serif}
.diario details{border-top:1px solid var(--border)}
.diario details:last-of-type{border-bottom:1px solid var(--border)}
.diario summary{cursor:pointer;padding:.85rem 0;color:var(--plata-clara);font-size:.95rem;list-style-position:inside}
.diario label{display:block;font-size:.84rem;color:var(--text-soft);margin:.6rem 0 .3rem}
.diario textarea,.diario input[type=text]{width:100%;font:inherit;font-size:.95rem;color:var(--text);background:rgba(10,18,37,.9);border:1px solid var(--border);border-radius:8px;padding:.6rem .7rem;line-height:1.5}
.diario textarea{min-height:3.4rem;resize:vertical}
.diario .dia{padding-bottom:1rem}
.diario .elige{display:flex;gap:1.2rem;margin:.4rem 0 .6rem;font-size:.92rem;color:var(--text-soft)}
.diario .acciones{display:flex;gap:.7rem;flex-wrap:wrap;margin-top:1.1rem}
.diario button{font:inherit;font-size:.84rem;color:var(--text-soft);background:none;border:1px solid var(--border);border-radius:999px;padding:.5rem .95rem;cursor:pointer}
.diario button:hover{color:var(--plata-clara);border-color:var(--border-strong)}
.diario .estado{font-size:.8rem;color:var(--text-faint);margin-top:.6rem;min-height:1.1em}
.diario .contador{display:flex;align-items:center;gap:.6rem;margin:.35rem 0 .2rem;font-size:.9rem;color:var(--text-soft)}
.diario .contador span.t{flex:1}
.diario .contador button{width:2.2rem;height:2.2rem;padding:0;border-radius:50%;font-size:1.05rem;line-height:1}
.diario .contador output{min-width:1.6rem;text-align:center;color:var(--plata-clara);font-size:1rem}
.campo-svg .punto{fill:var(--ambar)}
.campo-svg .punto.late{animation:late 3.6s ease-in-out 3.4s infinite;transform-origin:center;transform-box:fill-box}
.campo-svg .halo{fill:none;stroke:var(--ambar);stroke-width:1;opacity:0;transform-origin:center;transform-box:fill-box;animation:halo 10s ease-in-out 3.4s infinite}
@keyframes halo{0%{opacity:0;transform:scale(.6)}40%{opacity:.55;transform:scale(1)}100%{opacity:0;transform:scale(.6)}}
.diario .rotulo{display:block;font-size:.84rem;color:var(--text-soft);margin:.6rem 0 .3rem}
.diario .plan{display:flex;flex-wrap:wrap;align-items:baseline;gap:.35rem .5rem;margin:.4rem 0 1.1rem;font-size:.95rem;color:var(--text-soft)}
.diario .plan input[type=text]{padding:.4rem .6rem}
.diario .plan input.corto{flex:0 1 6.5rem;width:6.5rem}
.diario .plan input.largo{flex:1 1 11rem;width:auto;min-width:9rem}
.diario input::placeholder{color:var(--text-faint)}
@keyframes late{0%,100%{opacity:.55}50%{opacity:1}}
@media (max-width:600px){html{font-size:118.75%}}
.enlaces li b{font-family:'Cormorant Garamond',serif;font-size:1.22rem;font-weight:500;color:var(--plata-clara)}
.autor{margin:3rem 0 0;padding-top:.4rem;border-top:1px solid var(--border)}
.autor h2{font-size:1.25rem;margin:1.6rem 0 .6rem}
.autor p{color:var(--text-soft);font-size:1rem}
.cuidado{margin:2.2rem 0;padding:1.05rem 1.2rem;border:1px solid var(--ambar-borde);border-radius:12px;background:rgba(217,179,108,.04)}
.cuidado h2{margin:0 0 .6rem;color:var(--ambar);font-size:1.3rem}
/* cierre */
.enlaces{list-style:none;margin:0!important}
.enlaces li{padding:.9rem 0;border-top:1px solid var(--border);margin:0}
.enlaces li:last-child{border-bottom:1px solid var(--border)}
.enlaces a{font-family:'Cormorant Garamond',serif;font-size:1.22rem;text-decoration:none;color:var(--plata-clara)}
.enlaces a:hover{text-decoration:underline}
.enlaces span{display:block;color:var(--text-soft);font-size:.98rem;margin-top:.15rem}
.puente{font-style:italic;color:var(--text-soft);margin-top:1.6rem}
@media (max-width:640px){
  html{font-size:112.5%}
  .wrap{padding:0 1.15rem}
  .cabeza{padding:2.2rem 0 2rem}
  .perla p{font-size:1.36rem}
  .promesa p{font-size:1.5rem}
}
/* la fisura de oro */
.fisura{margin:2rem 0;display:flex;flex-direction:column;align-items:center;gap:.9rem}
.fisura button{appearance:none;width:100%;max-width:25rem;border:1px solid var(--border);border-radius:16px;background:var(--panel);padding:1.25rem 1rem 1.05rem;cursor:pointer;color:var(--plata-clara);font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;font-size:1.3rem;display:flex;flex-direction:column;align-items:center;gap:.7rem}
.fisura button:hover{border-color:var(--border-strong)}
.fisura svg{display:block;width:100%;height:auto}
.fisura .base{fill:none;stroke:rgba(168,196,224,.38);stroke-width:2;stroke-linejoin:round;stroke-linecap:round}
.fisura .oro{fill:none;stroke:var(--ambar);stroke-width:3.2;stroke-linejoin:round;stroke-linecap:round;stroke-dasharray:1000;stroke-dashoffset:1000;filter:drop-shadow(0 0 4px rgba(217,179,108,.55))}
.fisura .cuenta{font-family:'Inter',sans-serif;font-size:.84rem;color:var(--text-faint);min-height:1.2em;text-align:center}
.campo-svg .corte{fill:none;stroke:var(--bg);stroke-width:5;opacity:0;animation:aparece .5s ease-out 3.3s forwards}
@keyframes aparece{to{opacity:1}}
.campo-svg .costura{fill:none;stroke:var(--ambar);stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.campo-svg .costura.dibuja{stroke-dasharray:80;stroke-dashoffset:80;animation:traza 1.6s ease-out 3.4s forwards}

/* la clepsidra */
.clepsidra{margin:2rem 0;display:flex;flex-direction:column;align-items:center;gap:.9rem}
.clepsidra button{appearance:none;width:100%;max-width:19rem;border:1px solid var(--border);border-radius:16px;background:var(--panel);padding:1.2rem 1rem 1.05rem;cursor:pointer;color:var(--plata-clara);font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;font-size:1.3rem;display:flex;flex-direction:column;align-items:center;gap:.7rem}
.clepsidra button:hover{border-color:var(--border-strong)}
.clepsidra svg{display:block;width:9.5rem;height:auto}
.clepsidra .vaso{fill:none;stroke:rgba(168,196,224,.5);stroke-width:1.6;stroke-linejoin:round}
.clepsidra .agua{fill:rgba(168,196,224,.26)}
.clepsidra .gota{fill:var(--ambar);opacity:0}
.clepsidra .gota.cae{animation:cae 1.7s ease-in forwards}
@keyframes cae{0%{opacity:0;transform:translateY(0)}12%{opacity:1}82%{opacity:1;transform:translateY(74px)}100%{opacity:0;transform:translateY(80px)}}
.clepsidra .cuenta{font-family:'Inter',sans-serif;font-size:.84rem;color:var(--text-faint);min-height:1.2em;text-align:center}
.campo-svg .gotap{fill:var(--ambar);opacity:0;animation:gotea 6s ease-in 3.6s infinite}
@keyframes gotea{0%{opacity:0;transform:translateY(0)}15%{opacity:.9}70%{opacity:.9;transform:translateY(46px)}85%,100%{opacity:0;transform:translateY(52px)}}
.diario .marca{display:flex;align-items:center;gap:.55rem;font-size:.92rem;color:var(--text-soft);margin:.7rem 0 .2rem;cursor:pointer}
.diario .marca input{width:1.05rem;height:1.05rem;accent-color:var(--plata)}
@media (prefers-reduced-motion:reduce){
  .clepsidra .agua{transition:none!important}
  .clepsidra .gota.cae{animation:none}
  .campo-svg .gotap{animation:none;opacity:.75;transform:translateY(20px)}
}
@media (prefers-reduced-motion:reduce){
  .fisura .oro{transition:none!important}
  .campo-svg .costura.dibuja{animation:none;stroke-dashoffset:0}
  .campo-svg .corte{animation:none;opacity:1}
  .campo-svg .linea.dibuja{animation:none;stroke-dashoffset:0}
  .respira.activa .aro{animation:none;transform:scale(.94)}
  .campo-svg .halo{animation:none;opacity:.35}
}
'''

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,400&family=EB+Garamond:ital,wght@0,400;0,500;1,400&family=Inter:wght@400;500&display=swap" rel="stylesheet">'

SUP = '⁰¹²³⁴⁵⁶⁷⁸⁹'

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'\*(.+?)\*', r'<em>\1</em>', s)
    def _ref(m):
        n = int(''.join(str(SUP.index(c)) for c in m.group(0)))
        return '<sup class="ref"><a href="#nota-%d" aria-label="nota %d">%d</a></sup>' % (n, n, n)
    s = re.sub('[' + SUP + ']+', _ref, s)
    return s

def page(title, body, desc=''):
    return '''<!DOCTYPE html>
<html lang="es" data-libro="%s">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="%s">
<title>%s</title>
%s
<style>%s</style>
</head>
<body>
%s
</body>
</html>
''' % (PREF, html.escape(desc), html.escape(title), FONTS, CSS, body)

def barra(izq, der):
    return '<nav class="barra" aria-label="Navegación"><a href="%s">%s</a><a href="%s">%s</a></nav>' % (izq[0], izq[1], der[0], der[1])

def rumbo(k):
    out = []
    for i in range(1, 8):
        c = 'aqui' if i == k else ('hecho' if i < k else '')
        out.append('<span class="%s"></span>' % c)
    return '<div class="rumbo" aria-hidden="true">%s</div>' % ''.join(out)

def leer(nombre):
    t = open(os.path.join(SRC, nombre), encoding='utf-8').read()
    lines = t.split('\n')
    start = next(i for i, l in enumerate(lines) if l.startswith('*Borrador')) + 1
    return lines[start:]

CLEPSIDRA = """<div class="clepsidra" id="clepsidra">
  <button type="button" aria-describedby="clepsidra-cuenta"><svg viewBox="0 0 160 220" aria-hidden="true">
    <defs><clipPath id="vaso-arriba"><path d="M30 22 L130 22 L92 96 L68 96 Z"/></clipPath><clipPath id="vaso-abajo"><path d="M34 128 L126 128 L118 200 L42 200 Z"/></clipPath></defs>
    <g clip-path="url(#vaso-arriba)"><rect class="agua agua-arriba" x="20" y="30" width="120" height="70"/></g>
    <g clip-path="url(#vaso-abajo)"><rect class="agua agua-abajo" x="20" y="200" width="120" height="72"/></g>
    <path class="vaso" d="M30 22 L130 22 L92 96 L68 96 Z"/><path class="vaso" d="M34 128 L126 128 L118 200 L42 200 Z"/>
    <path class="vaso" d="M80 96 L80 104"/>
    <path class="gota" d="M80 104 C80 104 76 110 76 113 A4 4 0 0 0 84 113 C84 110 80 104 80 104 Z"/>
  </svg><span class="frase">Toca la clepsidra para empezar</span></button>
  <div class="cuenta" id="clepsidra-cuenta" aria-live="polite">Siete respiraciones. Cae una gota cada vez que sueltas el aire.</div>
</div>"""

DIAS = ''.join("""
  <details%s><summary>Día %d</summary><div class="dia">
    <span class="rotulo" id="d%d-u-t">La última vez de hoy</span>
    <div class="elige" role="radiogroup" aria-labelledby="d%d-u-t"><label><input type="radio" name="d%d-ult" value="hecho" data-k="d%d-ult"> La miré</label><label><input type="radio" name="d%d-ult" value="manana" data-k="d%d-ult"> Mañana vuelvo</label></div>
    <label for="d%d-term">Hoy terminó…</label><textarea id="d%d-term" data-k="d%d-term" rows="2"></textarea>
    <label for="d%d-queda">Queda para mañana…</label><textarea id="d%d-queda" data-k="d%d-queda" rows="2"></textarea>
    <label class="marca"><input type="checkbox" data-k="d%d-vivi"> Viví este día</label>
  </div></details>""" % ((' open' if d == 1 else ''), d, d, d, d, d, d, d, d, d, d, d, d, d, d) for d in range(1, 8))
DIARIO = """<div class="diario" id="diario">
  <label class="rotulo" for="mi-final">El final que voy a despedir esta semana</label>
  <input type="text" id="mi-final" data-k="mi-final" placeholder="Un objeto, un lugar, una etapa">
  <label class="marca"><input type="checkbox" data-k="despedido"> Ya lo despedí</label>%s
  <label class="rotulo" for="epitafio" style="margin-top:1.2rem">Mi epitafio vivo, el séptimo día</label>
  <textarea id="epitafio" data-k="epitafio" rows="4" placeholder="Habiendo aprendido… elijo… Mañana empiezo por…"></textarea>
  <div class="acciones"><button type="button" id="copiar">Copiar mis notas</button><button type="button" id="borrar">Borrar mis notas</button></div>
  <p class="estado" id="estado" aria-live="polite">Lo que escribes se guarda solo en este dispositivo. Nadie más lo ve.</p>
</div>""" % DIAS
SCRIPT_OP = r"""<script>
(function(){
  var c=document.getElementById('clepsidra'); if(c){
    var b=c.querySelector('button'), arriba=c.querySelector('.agua-arriba'), abajo=c.querySelector('.agua-abajo'), gota=c.querySelector('.gota'), fr=c.querySelector('.frase'), cu=document.getElementById('clepsidra-cuenta');
    var red=window.matchMedia('(prefers-reduced-motion: reduce)').matches, CICLOS=7, k=0, estado='quieto', timers=[];
    function limpiar(){ timers.forEach(function(x){ clearTimeout(x); }); timers=[]; }
    function nivel(n,anim){ var d=(anim&&!red)?'6s':'0s'; arriba.style.transition='transform '+d+' linear'; abajo.style.transition='transform '+d+' linear'; arriba.style.transform='translateY('+(n*70/CICLOS)+'px)'; abajo.style.transform='translateY('+(-n*72/CICLOS)+'px)'; }
    function cae(){ if(red){ return; } gota.classList.remove('cae'); void gota.getBoundingClientRect(); gota.classList.add('cae'); }
    function fin(){ limpiar(); estado='fin'; nivel(CICLOS,false); fr.textContent='Viví este día.'; cu.textContent='El día queda despedido. Que descanses.'; }
    function ciclo(){
      if(k>=CICLOS){ fin(); return; }
      fr.textContent='Toma aire…'; cu.textContent='Respiración '+(k+1)+' de '+CICLOS+'.';
      timers.push(setTimeout(function(){
        fr.textContent='Suelta el aire despacio…';
        k++; nivel(k,true); cae();
        timers.push(setTimeout(ciclo,6000));
      },4000));
    }
    b.addEventListener('click',function(){
      if(estado==='corre'){ limpiar(); estado='pausa'; nivel(k,false); gota.classList.remove('cae'); fr.textContent='En pausa'; cu.textContent='Toca otra vez para seguir. La gota espera.'; return; }
      if(estado==='quieto'||estado==='fin'){ k=0; nivel(0,false); void arriba.getBoundingClientRect(); }
      estado='corre'; ciclo();
    });
  }
  var K='arq-'+document.documentElement.getAttribute('data-libro')+'-despedida-v1', d={};
  try{ d=JSON.parse(localStorage.getItem(K)||'{}')||{}; }catch(e){ d={}; }
  function guardar(){ try{ localStorage.setItem(K,JSON.stringify(d)); }catch(e){} }
  var campos=document.querySelectorAll('#diario [data-k]');
  campos.forEach(function(el){
    var k=el.getAttribute('data-k');
    if(el.type==='radio'){ if(d[k]===el.value){ el.checked=true; } el.addEventListener('change',function(){ d[k]=el.value; guardar(); }); }
    else if(el.type==='checkbox'){ if(d[k]){ el.checked=true; } el.addEventListener('change',function(){ d[k]=el.checked; guardar(); }); }
    else { if(d[k]){ el.value=d[k]; } el.addEventListener('input',function(){ d[k]=el.value; guardar(); }); }
  });
  var est=document.getElementById('estado');
  var cp=document.getElementById('copiar'); if(cp){ cp.addEventListener('click',function(){
    var txt=[];
    if(d['mi-final']){ txt.push('El final de esta semana: '+d['mi-final']+(d['despedido']?' (despedido)':'')); }
    var nom={hecho:'la miré', manana:'mañana vuelvo'};
    for(var i=1;i<=7;i++){ var u=d['d'+i+'-ult']||'', h=d['d'+i+'-term']||'', q=d['d'+i+'-queda']||'', v=d['d'+i+'-vivi']; if(u||h||q||v){ txt.push('Día '+i+(u?'\nLa última vez: '+nom[u]:'')+(h?'\nHoy terminó '+h:'')+(q?'\nQueda para mañana '+q:'')+(v?'\nViví este día.':'')); } }
    if(d['epitafio']){ txt.push('Mi epitafio vivo: '+d['epitafio']); }
    var s=txt.join('\n\n')||'Todavía no escribiste nada.';
    if(navigator.clipboard){ navigator.clipboard.writeText(s).then(function(){ est.textContent='Notas copiadas.'; },function(){ est.textContent='No se pudieron copiar. Selecciona el texto a mano.'; }); }
    else { est.textContent='Este navegador no permite copiar automáticamente.'; }
  }); }
  var br=document.getElementById('borrar'); if(br){ br.addEventListener('click',function(){
    if(!confirm('¿Borrar las notas de esta semana? No se pueden recuperar.')){ return; }
    d={}; guardar(); campos.forEach(function(el){ if(el.type==='radio'||el.type==='checkbox'){ el.checked=false; } else { el.value=''; } }); est.textContent='Notas borradas.';
  }); }
})();
</script>"""

def cuerpo(lines, operacion=False):
    out = []; para = []; bq = []; lst = []; ltype = None; notas = None
    def fl_para():
        nonlocal para
        if para:
            if all(x.startswith('**') and ':**' in x for x in para):
                out.append('<div class="ficha">' + ''.join('<p>%s</p>' % inline(x) for x in para) + '</div>')
            else:
                out.append('<p>%s</p>' % '<br>'.join(inline(x) for x in para))
            para = []
    def fl_list():
        nonlocal lst, ltype
        if lst:
            out.append('<%s>%s</%s>' % (ltype, ''.join('<li>%s</li>' % inline(x) for x in lst), ltype)); lst = []; ltype = None
    def fl_bq():
        nonlocal bq
        if not bq: return
        groups = [[]]
        for l in bq:
            x = l[1:].strip()
            if x == '': groups.append([])
            else: groups[-1].append(x)
        groups = [g for g in groups if g]
        if any('**' in l for l in bq):
            out.append('<div class="perla">' + ''.join('<p>%s</p>' % '<br>'.join(inline(x.replace('**', '')) for x in g) for g in groups) + '</div>')
        else:
            ps = []
            for g in groups:
                orig = all(x.startswith('*') and x.rstrip(SUP).endswith('*') for x in g)
                ps.append('<p class="%s">%s</p>' % ('orig' if orig else 'trad', '<br>'.join(inline(x) for x in g)))
            out.append('<div class="cita">' + ''.join(ps) + '</div>')
        bq = []
    for raw in lines:
        s = raw.rstrip()
        if notas is not None:
            m = re.match(r'(\d+)\. (.+)', s)
            if m: notas.append((m.group(1), m.group(2)))
            continue
        if s.startswith('>'):
            fl_para(); fl_list(); bq.append(s); continue
        else:
            fl_bq()
        if s.strip() in ('', '---'):
            fl_para(); fl_list(); continue
        if s.startswith('### '):
            fl_para(); fl_list()
            h = s[4:].strip()
            if h == 'Notas': notas = []
            elif operacion and h.startswith('Paso'): out.append('<div class="paso"><h2>%s</h2></div>' % inline(h))
            elif operacion and h.startswith('Cuándo no'): out.append('<!--CUIDADO-->' + '<h2>%s</h2>' % inline(h))
            else: out.append('<h2>%s</h2>' % inline(h))
            continue
        if s.startswith('*[Movimiento'):
            fl_para(); fl_list(); out.append(CLEPSIDRA); continue
        if s.startswith('*[Diario'):
            fl_para(); fl_list(); out.append(DIARIO); continue
        m = re.match(r'^(\d+)\. (.+)', s)
        if s.startswith('- ') or m:
            fl_para()
            t = 'ul' if s.startswith('- ') else 'ol'
            if ltype and ltype != t: fl_list()
            ltype = t; lst.append(s[2:] if t == 'ul' else m.group(2)); continue
        fl_list(); para.append(s)
    fl_para(); fl_list(); fl_bq()
    htmls = '\n'.join(out)
    if '<!--CUIDADO-->' in htmls:
        a, b = htmls.split('<!--CUIDADO-->', 1)
        perla_i = b.rfind('<div class="perla">')
        cuid, resto = (b[:perla_i], b[perla_i:]) if perla_i > 0 else (b, '')
        htmls = a + '<section class="cuidado">' + cuid + '</section>' + resto
    if notas:
        htmls += '\n<section class="notas" aria-label="Notas"><h3>Notas</h3><ol>' + ''.join('<li id="nota-%s">%s</li>' % (n, inline(t)) for n, t in notas) + '</ol></section>'
    return htmls

# umbrales
for k, (rom, tit, sub) in enumerate(UMBRALES, start=1):
    lines = leer(PREF + '_Umbral_%s_borrador.md' % rom)
    main = cuerpo(lines, operacion=(k == 7))
    prev = (fname('portada'), 'Portada') if k == 1 else (fname(k - 1), UMBRALES[k - 2][1])
    nxt = (fname('cierre'), CIERRE[0]) if k == 7 else (fname(k + 1), UMBRALES[k][1])
    head = '<header class="cabeza">%s<div class="cual">Umbral %s</div><h1>%s</h1><p class="sub">%s</p></header>' % (rumbo(k), rom, html.escape(tit), html.escape(sub))
    sigue = '<div class="sigue"><a href="%s">Anterior: %s</a><a class="prox" href="%s">Siguiente: %s</a></div>' % (prev[0], html.escape(prev[1]), nxt[0], html.escape(nxt[1]))
    if '<section class="notas"' in main:
        main = main.replace('<section class="notas"', sigue + '\n<section class="notas"', 1)
    else:
        main += sigue
    body = barra(('../index.html', 'Arquitectura del Destino'), (fname('portada'), 'Índice del libro')) + '<div class="wrap">' + head + '<main>' + main + '</main></div><footer class="pie">Libro ' + str(NUM) + ' de 13. Lic. Arturo Rodríguez, Campo Trinity.</footer>' + (SCRIPT_OP if k == 7 else '')
    open(os.path.join(OUT, fname(k)), 'w', encoding='utf-8').write(page('%s · Umbral %s · %s' % (tit, rom, LIBRO), body, sub))

# cierre
lines = leer(PREF + '_Cierre_borrador.md')
txt = '\n'.join(lines)
principal, _, resto = txt.partition('### Para ver')
paraver, _, resto2 = resto.partition('### Puertas laterales')
paraver, _, pantalla = paraver.partition('### En la pantalla')
puertas, _, refs = resto2.partition('### Referencias')
main = cuerpo(principal.split('\n'))
main = re.sub(r'<p><em>(Aprendiste[^<]*)</em></p>', r'<p class="puente">\1</p>', main)
assert 'class="puente"' in main
pv = []
for l in paraver.strip().split('\n'):
    if not l.startswith('- '): continue
    m = re.match(r'- \*\*(.+?)\*\*\s*(.*?)\s*·\s*`(.+?)`', l)
    pv.append('<li><a href="%s">%s</a><span>%s</span></li>' % (m.group(3), inline(m.group(1)), inline(m.group(2))))
main += '<h2>Para ver</h2><ul class="enlaces">%s</ul>' % ''.join(pv)
pa = []
for l in pantalla.strip().split('\n'):
    if not l.startswith('- '): continue
    m = re.match(r'- \*\*(.+?)\*\*\s*(.*)', l)
    pa.append('<li><b>%s</b><span>%s</span></li>' % (inline(m.group(1)), inline(m.group(2))))
if pa:
    main += '<h2>En la pantalla</h2><ul class="enlaces">%s</ul>' % ''.join(pa)
pu = []
for l in puertas.strip().split('\n'):
    if not l.startswith('- '): continue
    t = l[2:]
    key = next(k for k in PUERTAS if t.startswith(k + ':'))
    nombre = t.split(' · ')[0]
    pu.append('<li><a href="%s">%s</a></li>' % (PUERTAS[key], inline(nombre)))
main += '<h2>Puertas laterales</h2><ul class="enlaces">%s</ul>' % ''.join(pu)
rf = [l[2:] for l in refs.strip().split('\n') if l.startswith('- ')]
main += '<section class="notas" aria-label="Referencias"><h3>Referencias</h3><ol>%s</ol></section>' % ''.join('<li>%s</li>' % inline(x) for x in rf)
main += '<div class="sigue"><a href="%s">Anterior: %s</a><a class="prox" href="../index.html">Volver a la serie</a></div>' % (fname(7), UMBRALES[6][1])
head = '<header class="cabeza">%s<div class="cual">Cierre</div><h1>%s</h1><p class="sub">%s</p></header>' % (rumbo(8), CIERRE[0], CIERRE[1])
body = barra(('../index.html', 'Arquitectura del Destino'), (fname('portada'), 'Índice del libro')) + '<div class="wrap">' + head + '<main>' + main + '</main></div><footer class="pie">Libro ' + str(NUM) + ' de 13. Lic. Arturo Rodríguez, Campo Trinity.</footer>'
open(os.path.join(OUT, fname('cierre')), 'w', encoding='utf-8').write(page('%s · Cierre · %s' % (CIERRE[0], LIBRO), body, CIERRE[1]))

# portada
lines = leer(PREF + '_Portada_borrador.md')
txt = '\n'.join(lines)
prom = [l[2:].replace('**', '').strip() for l in lines if l.startswith('> **')]
antes = txt.split('### Antes de empezar', 1)[1].split('\n---', 1)[0].strip().split('\n\n')
aviso = txt.split('### Una advertencia breve', 1)[1].split('\n---', 1)[0].strip().split('\n\n')
import random
random.seed(7)
pts = []
cols, rows = 15, 8
for r in range(rows):
    for c in range(cols):
        x = 20 + c * 40; y = 18 + r * 26
        pts.append('<circle class="p" cx="%d" cy="%d" r="1.6"/>' % (x, y))
linea = 'M20 168 C 120 162, 170 128, 250 126 S 380 104, 450 96 S 540 84, 580 74'
gota = 'M579 82 C579 82 575.5 87.5 575.5 90 A3.5 3.5 0 0 0 582.5 90 C582.5 87.5 579 82 579 82 Z'
svg = ('<svg class="campo-svg" viewBox="0 0 600 210" role="img" aria-label="Un campo de puntos y una línea que lo atraviesa y se desvanece al final; de su extremo cae una gota, y junto a la línea respira un punto">'
       '<defs><linearGradient id="desvanece" gradientUnits="userSpaceOnUse" x1="20" y1="0" x2="580" y2="0"><stop offset="0" stop-color="#a8c4e0"/><stop offset=".74" stop-color="#a8c4e0"/><stop offset="1" stop-color="#a8c4e0" stop-opacity="0"/></linearGradient></defs>'
       '%s<path class="linea dibuja" style="stroke:url(#desvanece)" d="%s"/><path class="gotap" d="%s"/><circle class="halo" cx="250" cy="126" r="22"/><circle class="ojo" cx="250" cy="126" r="9"/><circle class="punto late" cx="250" cy="126" r="3.2"/></svg>') % (''.join(pts), linea, gota)
idx = ''.join('<li><a href="%s"><span class="n">%s</span><span><span class="t">%s</span><span class="s">%s</span></span></a></li>' % (fname(k), rom, html.escape(t), html.escape(s)) for k, (rom, t, s) in enumerate(UMBRALES, start=1))
idx += '<li><a href="%s"><span class="n">⟐</span><span><span class="t">%s</span><span class="s">%s</span></span></a></li>' % (fname('cierre'), CIERRE[0], CIERRE[1])
main = '<div class="promesa"><p>%s</p></div>' % '<br>'.join(inline(x) for x in prom)
main += '<h2>Antes de empezar</h2>' + ''.join('<p>%s</p>' % inline(p.strip()) for p in antes)
main += TRINITY_HTML
main += '<section class="aviso"><h2>Una advertencia breve</h2>' + ''.join('<p>%s</p>' % inline(p.strip()) for p in aviso) + '</section>'
main += '<h2>Los siete umbrales</h2><ol class="indice">%s</ol>' % idx
main += AUTOR_HTML
main += '<div class="sigue"><a href="../index.html">Volver a la serie</a><a class="prox" href="%s">Empezar: %s</a></div>' % (fname(1), UMBRALES[0][1])
head = '<header class="cabeza"><div class="cual">Libro %d de 13</div><h1>%s</h1><p class="sub">%s</p>%s</header>' % (NUM, LIBRO, SUBT, svg)
body = barra(('../index.html', 'Arquitectura del Destino'), ('../../index.html', 'Portal Trinity')) + '<div class="wrap">' + head + '<main>' + main + '</main></div><footer class="pie">Arquitectura del Destino, Sistema Trinity de Vida Consciente. Lic. Arturo Rodríguez, Campo Trinity.</footer>'
open(os.path.join(OUT, fname('portada')), 'w', encoding='utf-8').write(page('%s · Libro %d · Arquitectura del Destino' % (LIBRO, NUM), body, TESIS))
print('ok', sorted(os.listdir(OUT)))
