# Generador del Libro 13 de Arquitectura del Destino, Habitar (derivado del generador del Libro 12, octubre 2026)
# Diferencias: configuración del Libro 13, cierre del sistema; el movimiento lento es «el castillo de siete ventanas»
# (siete respiraciones: 4 s se toma aire, 6 s se suelta; con cada salida del aire se enciende una ventana y su morada,
# desde la muralla hacia el centro, y ninguna se apaga; al final se enciende el centro y aparece «Estoy aquí. Me quedo.»;
# tocarlo otra vez lo pausa; el brillo del centro corre solo mientras el dibujo está a la vista). El Umbral IV no lleva
# elemento interactivo. El umbral VII usa «*[Diario» con la casa que ya tienes (cuatro frases), los cuatro momentos de
# cada día, la ronda que fue visita, «Hoy estuve adentro cuando…» y, el séptimo día, la hora en la celda, a quién recibí
# y las cuatro líneas del cierre (Agradezco, Me perdono, Celebro, Dejo abierto).
# Uso: poner los borradores LNN_*_borrador.md en SRC (o en ARQ_SRC), ajustar la configuración y correr:
#   python3 gen_arq_L13.py
# En "Para ver", cada línea lleva el enlace al final entre comillas invertidas: · `https://...`
# Las "Puertas laterales" se resuelven con el diccionario PUERTAS (clave = texto antes de los dos puntos).
# El dibujo de la portada: el campo de puntos y la línea de siempre, que llega hasta el punto que respira y se cierra
# en un círculo a su alrededor. El cierre lleva, como siguiente, el primer libro de la serie.
import re, os, html

NUM = 13  # número de libro
PREF = 'L%02d' % NUM
SRC = os.environ.get('ARQ_SRC', '/mnt/user-data/outputs/arquitectura/' + PREF + '/fuentes')
SLUG = 'habitar'  # carpeta: libro-NN-slug
OUT = os.environ.get('ARQ_OUT', '/home/claude/arq_out/02_Arquitectura_del_Destino') + '/libro-%02d-%s' % (NUM, SLUG)
os.makedirs(OUT, exist_ok=True)

LIBRO = 'Habitar'
SUBT = 'la casa que ya tienes'
TESIS = 'Casa es donde recuerdas quién eres. El cierre no es volver: es quedarse despierto adentro.'
UMBRALES = [
    ('I', 'La ronda', 'estar cerca sin entrar'),
    ('II', 'Los dos que soñaron', 'el tesoro bajo la casa'),
    ('III', 'El hábito', 'la casa que se hace con los días'),
    ('IV', 'El centro en todas partes', 'casa sin paredes'),
    ('V', 'Los días malos también viven aquí', 'un hogar para todas tus partes'),
    ('VI', 'Marta y María', 'habitar no es retirarse'),
    ('VII', 'La operación', 'un día habitado'),
]
CIERRE = ('Adentro', 'lo que se gana al quedarse')

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
    'Trinity Origen, Libro XIII': 'https://soyartur-trinity.github.io/Trinity-/01_Trinity_Origen/Libro_13/index.html',
    'Trinity Origen, Libro XIII, Nodo 3': 'https://soyartur-trinity.github.io/Trinity-/01_Trinity_Origen/Libro_13/nodo_03.html',
    'Trinity Origen, Libro XIII, Nodo 5': 'https://soyartur-trinity.github.io/Trinity-/01_Trinity_Origen/Libro_13/nodo_05.html',
    'La Puerta, Nodo 13': 'https://soyartur-trinity.github.io/Trinity-/00_Portal_Trinity/nodo_13.html',
    'Trinity Quantum, Libro 13, Nodo 7': 'https://soyartur-trinity.github.io/Trinity-/02_Trinity_Quantum/Libro_13/nodo_07.html',
    'Trinity Infinito, Libro 13': 'https://soyartur-trinity.github.io/Trinity-/Trinity_Infinito/Libro_13/Libro_13.html',
    'Portal Público, Libro 39': '../../01_Libros/39_El_Campo/index.html',
    'Portal Público, Libro 28': '../../01_Libros/28_El_Vacio/index.html',
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

/* el barro */
.barro{margin:2rem 0;display:flex;flex-direction:column;align-items:center;gap:.9rem}
.barro button{appearance:none;width:100%;max-width:21rem;border:1px solid var(--border);border-radius:16px;background:var(--panel);padding:1.2rem 1rem 1.05rem;cursor:pointer;color:var(--plata-clara);font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;font-size:1.3rem;display:flex;flex-direction:column;align-items:center;gap:.7rem}
.barro button:hover{border-color:var(--border-strong)}
.barro svg{display:block;width:15rem;max-width:100%;height:auto}
.barro .fondo{fill:rgba(168,196,224,.05)}
.barro .plato{fill:rgba(168,196,224,.10);stroke:rgba(168,196,224,.45);stroke-width:1}
.barro .giro{fill:none;stroke:var(--plata);stroke-width:1;stroke-dasharray:6 10;opacity:.55;animation:gira 2.4s linear infinite}
.barro .masa path.cuerpo{fill:#8a6e5a;stroke:rgba(212,228,244,.32);stroke-width:1}
.barro .surco{fill:none;stroke:rgba(212,228,244,.28);stroke-width:1;stroke-dasharray:14 20;animation:gira 1.7s linear infinite}
.barro .cuenta{font-family:'Inter',sans-serif;font-size:.84rem;color:var(--text-faint);min-height:1.2em;text-align:center}
@keyframes gira{to{stroke-dashoffset:-32}}
.campo-svg .linea.pesada{stroke-width:2.8}
.campo-svg .linea.leve{stroke-width:1.2;opacity:.9}
.campo-svg .linea.pesada.dibuja{animation:traza 1.9s ease-in .4s forwards}
.campo-svg .linea.leve.dibuja{animation:traza 1.7s ease-out 2.3s forwards}
.campo-svg .torno{fill:none;stroke:rgba(168,196,224,.6);stroke-width:1;stroke-dasharray:4 7;opacity:0;transform-origin:center;transform-box:fill-box;animation:aparece .8s ease-out 3.6s forwards,torno 22s linear 3.6s infinite}
@keyframes torno{to{transform:rotate(360deg)}}
.diario .marca{display:flex;align-items:center;gap:.55rem;font-size:.92rem;color:var(--text-soft);margin:.7rem 0 .2rem;cursor:pointer}
.diario .marca input{width:1.05rem;height:1.05rem;accent-color:var(--plata)}

/* la máscara */
.mascara{margin:2rem 0;display:flex;flex-direction:column;align-items:center;gap:.9rem}
.mascara button{appearance:none;width:100%;max-width:21rem;border:1px solid var(--border);border-radius:16px;background:var(--panel);padding:1.2rem 1rem 1.05rem;cursor:pointer;color:var(--plata-clara);font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;font-size:1.3rem;display:flex;flex-direction:column;align-items:center;gap:.7rem}
.mascara button:hover{border-color:var(--border-strong)}
.mascara svg{display:block;width:13rem;max-width:100%;height:auto}
.mascara .fondo{fill:rgba(168,196,224,.05)}
.mascara .luz{fill:var(--ambar)}
.mascara .aura{fill:none;stroke:var(--ambar);stroke-width:1.2;opacity:.25;transform-origin:center;transform-box:fill-box}
.mascara.vista .aura{animation:halo 10s ease-in-out infinite}
.mascara .cara{fill:url(#mascara-tono);fill-rule:evenodd}
.mascara .contorno{fill:none;stroke:var(--plata-clara);stroke-width:1.3;stroke-linecap:round;opacity:.7;transition:opacity 1.2s ease}
.mascara.fin .contorno{opacity:.95}
.mascara .cuenta{font-family:'Inter',sans-serif;font-size:.84rem;color:var(--text-faint);min-height:1.2em;text-align:center}
.campo-svg .mascara-p{fill:rgba(168,196,224,.82);fill-rule:evenodd;opacity:0;animation:aparece .8s ease-out 3.2s forwards,destapa 2.6s ease-in-out 4.4s forwards}
.campo-svg .mascara-c{fill:none;stroke:var(--plata-clara);stroke-width:1.1;opacity:0;animation:aparece .8s ease-out 3.2s forwards}
@keyframes destapa{from{opacity:1}to{opacity:.12}}
@media (prefers-reduced-motion:reduce){
  .mascara.vista .aura{animation:none}
  .campo-svg .mascara-p{animation:none;opacity:.12}
  .campo-svg .mascara-c{animation:none;opacity:1}
}
@media (prefers-reduced-motion:reduce){
  .barro .giro,.barro .surco{animation:none}
  .campo-svg .torno{animation:none;opacity:.55}
}
@media (prefers-reduced-motion:reduce){
  .fisura .oro{transition:none!important}
  .campo-svg .costura.dibuja{animation:none;stroke-dashoffset:0}
  .campo-svg .corte{animation:none;opacity:1}
  .campo-svg .linea.dibuja{animation:none;stroke-dashoffset:0}
  .respira.activa .aro{animation:none;transform:scale(.94)}
  .campo-svg .halo{animation:none;opacity:.35}
}

/* la orilla */
.orilla{margin:2rem 0;display:flex;flex-direction:column;align-items:center;gap:.9rem}
.orilla button{appearance:none;width:100%;max-width:21rem;border:1px solid var(--border);border-radius:16px;background:var(--panel);padding:1.2rem 1rem 1.05rem;cursor:pointer;color:var(--plata-clara);font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;font-size:1.3rem;display:flex;flex-direction:column;align-items:center;gap:.7rem}
.orilla button:hover{border-color:var(--border-strong)}
.orilla svg{display:block;width:13rem;max-width:100%;height:auto}
.orilla .mar{fill:rgba(120,160,210,.09)}
.orilla .arena{fill:rgba(222,196,146,.24)}
.orilla .canal{fill:rgba(3,8,20,.55)}
.orilla .tira{fill:none;stroke:rgba(168,196,224,.38);stroke-width:1;stroke-dasharray:3 6}
.orilla.vista .tira{animation:tira 3.2s linear infinite}
@keyframes tira{to{stroke-dashoffset:-18}}
.orilla .ola{fill:none;stroke:rgba(212,228,244,.6);stroke-width:1.2;stroke-linecap:round;opacity:.55}
.orilla.vista .ola{animation:ola 4.5s ease-in-out infinite}
@keyframes ola{0%,100%{opacity:.4}50%{opacity:.85}}
.orilla .luz{fill:var(--ambar)}
.orilla .aura{fill:none;stroke:var(--ambar);stroke-width:1.2;opacity:.25;transform-origin:center;transform-box:fill-box}
.orilla.vista .aura{animation:halo 10s ease-in-out infinite}
.orilla .cuenta{font-family:'Inter',sans-serif;font-size:.84rem;color:var(--text-faint);min-height:1.2em;text-align:center}
.campo-svg .corr path{fill:none;stroke:rgba(168,196,224,.5);stroke-width:1;stroke-dasharray:6 8;opacity:0;animation:aparece .8s ease-out 2.6s forwards,fluye 7s linear 2.6s infinite}
@keyframes fluye{to{stroke-dashoffset:-56}}
@media (prefers-reduced-motion:reduce){
  .orilla.vista .tira,.orilla.vista .ola,.orilla.vista .aura{animation:none}
  .campo-svg .corr path{animation:none;opacity:.5}
}

/* la red de Indra */
.indra{margin:2rem 0;display:flex;flex-direction:column;align-items:center;gap:.9rem}
.indra>button:not(.apagar){appearance:none;width:100%;max-width:22rem;border:1px solid var(--border);border-radius:16px;background:var(--panel);padding:1.1rem 1rem 1.05rem;cursor:pointer;color:var(--plata-clara);font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;font-size:1.3rem;display:flex;flex-direction:column;align-items:center;gap:.7rem}
.indra>button:not(.apagar):hover{border-color:var(--border-strong)}
.indra svg{display:block;width:16rem;max-width:100%;height:auto}
.joyas{margin:2rem 0;padding:1.1rem 1rem 1rem;border:1px solid var(--border);border-radius:16px;background:var(--panel)}
.joyas svg{width:19rem;touch-action:manipulation}
.indra .hilo{stroke:rgba(168,196,224,.24);stroke-width:.8;transition:stroke .6s ease,stroke-width .6s ease}
.indra .hilo.tocado{stroke:rgba(217,179,108,.34)}
.indra .hilo.vivo{stroke:rgba(217,179,108,.9);stroke-width:1.3}
.indra .joya{fill:rgba(8,15,31,.96);stroke:rgba(168,196,224,.55);stroke-width:.9;transition:fill .8s ease,stroke .8s ease}
.indra .nodo.luz .joya{fill:rgba(217,179,108,.16);stroke:var(--ambar)}
.indra .r{fill:rgba(168,196,224,.22);transition:fill .7s ease}
.indra .r.on{fill:var(--ambar)}
.indra .brillo{fill:none;stroke:var(--ambar);stroke-width:.7;opacity:0;transform-origin:center;transform-box:fill-box}
.indra .nodo.luz .brillo{opacity:.45}
.indra.vista .nodo.luz .brillo{animation:halo 10s ease-in-out infinite}
.indra .toque{fill:transparent;cursor:pointer}
.indra .nodo{outline:none}
.indra .nodo:focus-visible .joya{stroke:var(--plata-clara);stroke-width:1.8}
.indra .cuenta{font-family:'Inter',sans-serif;font-size:.84rem;color:var(--text-faint);min-height:1.2em;text-align:center;margin:0}
.joyas .apagar{display:block;margin:.7rem auto 0;font:inherit;font-family:'Inter',sans-serif;font-size:.8rem;color:var(--text-soft);background:none;border:1px solid var(--border);border-radius:999px;padding:.45rem .9rem;cursor:pointer}
.joyas .apagar:hover{color:var(--plata-clara);border-color:var(--border-strong)}
.campo-svg .hilo{fill:none;stroke:rgba(217,179,108,.5);stroke-width:1;stroke-dasharray:120;stroke-dashoffset:120;animation:traza 1.4s ease-out forwards}
.campo-svg .nudo{fill:var(--ambar);opacity:0;animation:aparece .7s ease-out forwards}
.campo-svg .nudo.lejos{fill:var(--plata-clara)}
@media (prefers-reduced-motion:reduce){
  .indra.vista .nodo.luz .brillo{animation:none}
  .indra .hilo,.indra .joya,.indra .r{transition:none}
  .campo-svg .hilo{animation:none;stroke-dashoffset:0}
  .campo-svg .nudo{animation:none;opacity:.8}
}
/* el castillo de siete ventanas */
.castillo{margin:2rem 0;display:flex;flex-direction:column;align-items:center;gap:.9rem}
.castillo button{appearance:none;width:100%;max-width:22rem;border:1px solid var(--border);border-radius:16px;background:var(--panel);padding:1.1rem 1rem 1.05rem;cursor:pointer;color:var(--plata-clara);font-family:'Cormorant Garamond',Georgia,serif;font-style:italic;font-size:1.3rem;display:flex;flex-direction:column;align-items:center;gap:.7rem}
.castillo button:hover{border-color:var(--border-strong)}
.castillo svg{display:block;width:15rem;max-width:100%;height:auto}
.castillo .morada{fill:none;stroke:rgba(168,196,224,.30);stroke-width:.9;transition:stroke 1.4s ease}
.castillo .morada.on{stroke:rgba(217,179,108,.55)}
.castillo .ventana{fill:var(--bg);stroke:rgba(168,196,224,.50);stroke-width:.7;transition:fill 1.1s ease,stroke 1.1s ease}
.castillo .ventana.on{fill:var(--ambar);stroke:var(--ambar)}
.castillo .centro{fill:rgba(168,196,224,.35);transition:fill 1.4s ease}
.castillo .centro-halo{fill:url(#g-centro);opacity:0;transition:opacity 1.6s ease}
.castillo.fin .centro{fill:var(--ambar)}
.castillo.fin .centro-halo{opacity:1}
.castillo.vista.fin .centro-halo{animation:respira 5s ease-in-out infinite}
@keyframes respira{0%,100%{opacity:.65}50%{opacity:1}}
.castillo .cuenta{font-family:'Inter',sans-serif;font-size:.84rem;color:var(--text-faint);min-height:1.2em;text-align:center}
.campo-svg .circulo{fill:none;stroke:var(--ambar);stroke-width:1.2;opacity:.85}
.campo-svg .circulo.dibuja{stroke-dasharray:280;stroke-dashoffset:280;animation:traza 2.6s ease-in-out 3.2s forwards}
@media (prefers-reduced-motion:reduce){
  .castillo.vista.fin .centro-halo{animation:none}
  .castillo .morada,.castillo .ventana,.castillo .centro,.castillo .centro-halo{transition:none}
  .campo-svg .circulo.dibuja{animation:none;stroke-dashoffset:0}
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

def castillo_svg():
    out = []
    c = 100
    for i in range(7):
        s = 92 - i * 12
        out.append('<rect class="morada" data-i="%d" x="%d" y="%d" width="%d" height="%d" rx="%d"/>' % (i, c - s, c - s, 2 * s, 2 * s, max(4, 12 - i)))
    for i in range(7):
        s = 92 - i * 12
        lado = i % 4  # arriba, derecha, abajo, izquierda: las moradas «unas en lo alto, otras embajo, otras a los lados»
        if lado == 0: x, y, w, h = c - 3.5, c - s - 4.5, 7, 9
        elif lado == 1: x, y, w, h = c + s - 4.5, c - 3.5, 9, 7
        elif lado == 2: x, y, w, h = c - 3.5, c + s - 4.5, 7, 9
        else: x, y, w, h = c - s - 4.5, c - 3.5, 9, 7
        out.append('<rect class="ventana" data-i="%d" x="%.1f" y="%.1f" width="%d" height="%d" rx="1.5"/>' % (i, x, y, w, h))
    out.append('<circle class="centro-halo" cx="100" cy="100" r="16"/><circle class="centro" cx="100" cy="100" r="4.5"/>')
    defs = '<defs><radialGradient id="g-centro"><stop offset="0" stop-color="#d9b36c" stop-opacity=".6"/><stop offset="1" stop-color="#d9b36c" stop-opacity="0"/></radialGradient></defs>'
    return '<svg viewBox="0 0 200 200" aria-hidden="true">%s%s</svg>' % (defs, ''.join(out))

RESPIRA = """<div class="castillo" id="castillo">
  <button type="button" aria-describedby="castillo-cuenta">%s<span class="frase">Toca el castillo para empezar</span></button>
  <div class="cuenta" id="castillo-cuenta" aria-live="polite">Siete respiraciones. Con cada salida del aire se enciende una ventana, desde la muralla hacia el centro, y ninguna se apaga.</div>
</div>""" % castillo_svg()

JOYAS = ''
SCRIPT_U4 = ''

DIA_T = """
  <details{OPEN}><summary>Día {D}</summary><div class="dia">
    <label class="marca"><input type="checkbox" data-k="d{D}-m1"> Al despertar</label>
    <label class="marca"><input type="checkbox" data-k="d{D}-m2"> Al mediodía</label>
    <label class="marca"><input type="checkbox" data-k="d{D}-m3"> Cuando algo pesó</label>
    <label class="marca"><input type="checkbox" data-k="d{D}-m4"> Al caer la tarde: «Estoy aquí. Me quedo.»</label>
    <label for="d{D}-visita">La ronda que fue visita</label><input type="text" id="d{D}-visita" data-k="d{D}-visita" placeholder="La cerradura, el teléfono, un cuando…">
    <label for="d{D}-adentro">Hoy estuve adentro cuando…</label><textarea id="d{D}-adentro" data-k="d{D}-adentro" rows="2"></textarea>
  </div></details>"""
DIAS = ''.join(DIA_T.replace('{OPEN}', ' open' if d == 1 else '').replace('{D}', str(d)) for d in range(1, 8))
DIARIO = """<div class="diario" id="diario">
  <span class="rotulo">La casa que ya tienes</span>
  <label for="c-1">Al despertar</label><input type="text" id="c-1" data-k="c-1" placeholder="Tu frase de despertar">
  <label for="c-2">Al mediodía</label><input type="text" id="c-2" data-k="c-2" placeholder="Tu frase de encarnar">
  <label for="c-3">Cuando algo pese</label><input type="text" id="c-3" data-k="c-3" placeholder="Tu frase de soltar">
  <label for="c-4">Al caer la tarde</label><input type="text" id="c-4" data-k="c-4" placeholder="Tu frase de pertenecer">%s
  <label class="rotulo" for="celda" style="margin-top:1.2rem">El séptimo día, la hora en mi celda</label>
  <textarea id="celda" data-k="celda" rows="3" placeholder="Dónde estuve y qué apareció"></textarea>
  <label for="recibi">A quién recibí</label><input type="text" id="recibi" data-k="recibi" placeholder="Un nombre">
  <label for="cierre-1">Agradezco…</label><textarea id="cierre-1" data-k="cierre-1" rows="2"></textarea>
  <label for="cierre-2">Me perdono…</label><textarea id="cierre-2" data-k="cierre-2" rows="2"></textarea>
  <label for="cierre-3">Celebro…</label><textarea id="cierre-3" data-k="cierre-3" rows="2"></textarea>
  <label for="cierre-4">Dejo abierto…</label><textarea id="cierre-4" data-k="cierre-4" rows="2"></textarea>
  <div class="acciones"><button type="button" id="copiar">Copiar mis notas</button><button type="button" id="borrar">Borrar mis notas</button></div>
  <p class="estado" id="estado" aria-live="polite">Lo que escribes se guarda solo en este dispositivo. Nadie más lo ve.</p>
</div>""" % DIAS

SCRIPT_OP = r"""<script>
(function(){
  var mm=document.getElementById('castillo'); if(mm){
    var moradas=[].slice.call(mm.querySelectorAll('.morada')), ventanas=[].slice.call(mm.querySelectorAll('.ventana')), b=mm.querySelector('button'), fr=mm.querySelector('.frase'), cu=document.getElementById('castillo-cuenta'), red=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var CICLOS=7, k=0, estado='quieto', timers=[];
    if('IntersectionObserver' in window){ new IntersectionObserver(function(e){ mm.classList.toggle('vista',e[0].isIntersecting); }).observe(mm); } else { mm.classList.add('vista'); }
    function limpiar(){ timers.forEach(function(x){ clearTimeout(x); }); timers=[]; }
    function reiniciar(){ moradas.concat(ventanas).forEach(function(v){ v.classList.remove('on'); }); mm.classList.remove('fin'); }
    function encender(i){ timers.push(setTimeout(function(){ ventanas[i].classList.add('on'); moradas[i].classList.add('on'); }, red?0:900)); }
    function fin(){ limpiar(); estado='fin'; moradas.concat(ventanas).forEach(function(v){ v.classList.add('on'); }); mm.classList.add('fin'); fr.textContent='Estoy aquí. Me quedo.'; cu.textContent='Siete ventanas encendidas, y el centro también. Que descanses.'; }
    function ciclo(){
      if(k>=CICLOS){ fin(); return; }
      fr.textContent='Toma aire…'; cu.textContent='Respiración '+(k+1)+' de '+CICLOS+'.';
      timers.push(setTimeout(function(){
        fr.textContent='Suelta el aire despacio…';
        encender(k); k++;
        timers.push(setTimeout(ciclo,6000));
      },4000));
    }
    b.addEventListener('click',function(){
      if(estado==='corre'){ limpiar(); estado='pausa'; fr.textContent='En pausa'; cu.textContent='Toca otra vez para seguir. La ventana espera.'; return; }
      if(estado==='quieto'||estado==='fin'){ k=0; reiniciar(); }
      estado='corre'; ciclo();
    });
  }
  var K='arq-'+document.documentElement.getAttribute('data-libro')+'-habitar-v1', d={};
  try{ d=JSON.parse(localStorage.getItem(K)||'{}')||{}; }catch(e){ d={}; }
  function guardar(){ try{ localStorage.setItem(K,JSON.stringify(d)); }catch(e){} }
  var campos=document.querySelectorAll('#diario [data-k]');
  campos.forEach(function(el){
    var k=el.getAttribute('data-k');
    if(el.tagName==='OUTPUT'){ el.textContent=String(d[k]||0); }
    else if(el.type==='checkbox'){ if(d[k]){ el.checked=true; } el.addEventListener('change',function(){ d[k]=el.checked; guardar(); }); }
    else { if(d[k]){ el.value=d[k]; } el.addEventListener('input',function(){ d[k]=el.value; guardar(); }); }
  });
  function cuenta(k,delta){ var v=Math.max(0,(d[k]||0)+delta); d[k]=v; guardar(); var o=document.querySelector('#diario output[data-k="'+k+'"]'); if(o){ o.textContent=String(v); } }
  document.querySelectorAll('#diario [data-mas]').forEach(function(x){ x.addEventListener('click',function(){ cuenta(x.getAttribute('data-mas'),1); }); });
  document.querySelectorAll('#diario [data-menos]').forEach(function(x){ x.addEventListener('click',function(){ cuenta(x.getAttribute('data-menos'),-1); }); });
  var est=document.getElementById('estado');
  var cp=document.getElementById('copiar'); if(cp){ cp.addEventListener('click',function(){
    var txt=[];
    var casa=[['c-1','Al despertar'],['c-2','Al mediodía'],['c-3','Cuando algo pese'],['c-4','Al caer la tarde']];
    var cs=casa.filter(function(m){ return d[m[0]]; }).map(function(m){ return m[1]+': '+d[m[0]]; });
    if(cs.length){ txt.push('La casa que ya tienes:\n'+cs.join('\n')); }
    var nm=['Al despertar','Al mediodía','Cuando algo pesó','Al caer la tarde'];
    for(var i=1;i<=7;i++){ var ms=[]; for(var j=1;j<=4;j++){ if(d['d'+i+'-m'+j]){ ms.push(nm[j-1]); } } var vi=d['d'+i+'-visita']||'', ad=d['d'+i+'-adentro']||'';
      if(ms.length||vi||ad){ txt.push('Día '+i+(ms.length?'\nMomentos: '+ms.join(', ')+'.':'')+(vi?'\nLa ronda que fue visita: '+vi:'')+(ad?'\nHoy estuve adentro cuando '+ad:'')); } }
    if(d['celda']){ txt.push('El séptimo día, la hora en mi celda:\n'+d['celda']); }
    if(d['recibi']){ txt.push('A quién recibí: '+d['recibi']); }
    [['cierre-1','Agradezco'],['cierre-2','Me perdono'],['cierre-3','Celebro'],['cierre-4','Dejo abierto']].forEach(function(m){ if(d[m[0]]){ txt.push(m[1]+' '+d[m[0]]); } });
    var s=txt.join('\n\n')||'Todavía no escribiste nada.';
    if(navigator.clipboard){ navigator.clipboard.writeText(s).then(function(){ est.textContent='Notas copiadas.'; },function(){ est.textContent='No se pudieron copiar. Selecciona el texto a mano.'; }); }
    else { est.textContent='Este navegador no permite copiar automáticamente.'; }
  }); }
  var br=document.getElementById('borrar'); if(br){ br.addEventListener('click',function(){
    if(!confirm('¿Borrar las notas de esta semana? No se pueden recuperar.')){ return; }
    d={}; guardar(); campos.forEach(function(el){ if(el.tagName==='OUTPUT'){ el.textContent='0'; } else if(el.type==='checkbox'){ el.checked=false; } else { el.value=''; } }); est.textContent='Notas borradas.';
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
        if s.startswith('*[Red de Indra'):
            fl_para(); fl_list(); out.append(JOYAS); continue
        if s.startswith('*[Movimiento'):
            fl_para(); fl_list(); out.append(RESPIRA); continue
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
    body = barra(('../index.html', 'Arquitectura del Destino'), (fname('portada'), 'Índice del libro')) + '<div class="wrap">' + head + '<main>' + main + '</main></div><footer class="pie">Libro ' + str(NUM) + ' de 13. Lic. Arturo Rodríguez, Campo Trinity.</footer>' + (SCRIPT_OP if k == 7 else (SCRIPT_U4 if k == 4 else ''))
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
main += '<div class="sigue"><a href="%s">Anterior: %s</a><a class="prox" href="../libro-01-el-campo/L01.html">Empezar otra vez: El Campo</a></div>' % (fname(7), UMBRALES[6][1])
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
linea = 'M20 150 C 90 152, 160 132, 250 128'
svg = ('<svg class="campo-svg" viewBox="0 0 600 210" role="img" aria-label="Un campo de puntos y una línea que llega hasta el punto que respira y se cierra en un círculo a su alrededor">'
       '%s<path class="linea dibuja" d="%s"/>'
       '<circle class="circulo dibuja" cx="250" cy="128" r="44" transform="rotate(180 250 128)"/>'
       '<circle class="halo" cx="250" cy="128" r="16"/><circle class="punto late" cx="250" cy="128" r="3.2"/></svg>') % (''.join(pts), linea)
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
