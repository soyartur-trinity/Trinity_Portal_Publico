#!/usr/bin/env python3
"""El mapa de la Red (Campo Trinity).

Lee los datos del inventario (herramientas/red_puertas.json, que escribe
inventario_puertas.py) y genera una página autocontenida: un mandala de trece
radios y siete anillos, en el orden en que la obra fue llegando —Origen,
Quantum, Infinito, las tres constelaciones del Portal y Arquitectura del
Destino—, con el centro vacío. Cada libro es un punto; cada par de libros con
puertas entre sí, un hilo. Los hilos de ida y vuelta van en oro.

La Puerta queda fuera de los anillos (es la introducción a la serie mayor):
la página la ofrece como entrada, y sus puertas no se dibujan.

Uso:
  python3 gen_mapa_red.py RUTA/Trinity_Portal_Publico RUTA/red_puertas.json salida.html ["7 de noviembre de 2026"]
(la ruta del Portal sirve para leer los nombres de las carpetas de cada libro)
La página vive en Trinity_Portal_Publico/03_La_Red/index.html: los enlaces al
mismo repositorio son relativos desde ahí; los de Trinity-, absolutos. Se entra
desde el Atrio del Stargate (la miniatura de la Red) y el pie lleva de vuelta
al Atrio («#atrio») o al Portal.
Se regenera cada vez que se suma una puerta (primero el inventario, después esto).
"""
import json, os, re, sys, datetime

BASE_T = 'https://soyartur-trinity.github.io/Trinity-/'
REL_P = '../'  # desde 03_La_Red/ hasta la raíz del Portal

ROMANOS = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII']
MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto',
         'septiembre', 'octubre', 'noviembre', 'diciembre']

ORIGEN = ['Psicología Cuántica', 'La Voz Interior', 'El Dolor como Portal', 'Inteligencias Sin Nombre',
          'Los Vínculos Sagrados', 'El Vacío Fértil', 'La Muerte como Maestra', 'Educación Cuántica',
          'Liderazgo Consciente', 'Sanación Integral', 'La Consciencia Planetaria',
          'La Civilización Galáctica', 'El Retorno a Casa']
QUANTUM = ['El Arquitecto Cuántico', 'Entrelazamiento Sagrado', 'El Tiempo Vertical', 'La Paradoja Luminosa',
           'El Portal Infinito', 'El Vacío Creativo', 'Realidades Holofractales', 'Plasma Consciente',
           'Simetrías Rotas', 'Campos de Torsión', 'Transducción Dimensional', 'Singularidad Consciente',
           'El Multiverso Interior']
INFINITO = ['Más allá del ser y no-ser', 'La consciencia sin objeto', 'El juego sin jugador',
            'Infinitos anidados', 'La muerte de la muerte', 'El amor sin causa', 'Omnisciencia ignorante',
            'El punto sin dimensión', 'Tiempo antes del tiempo', 'La creatividad increada',
            'Causalidad circular', 'La palabra antes del verbo', '∞']
PORTAL = ['Empatía Humana', 'La Voz Interior', 'Encuentro Real', 'Asertividad Consciente', 'El Duelo',
          'Cuando algo en vos dice basta', 'Arquitectura del Destino', 'Atender', 'Volver distinto',
          'El sentido de la vuelta', 'Atravesar', 'Cultivar', 'Volver al centro',
          'Bien', 'El tercero', 'Lo que queda dicho', 'Ídolo', 'Lo que se escapa', 'La división',
          'El ayudante', 'El criterio', 'El ausente', 'El oficio', 'El clima', 'La herencia', 'Lo que queda',
          'El instante', 'El vacío', 'La intención', 'La presencia', 'El no saber', 'La duración', 'El ritmo',
          'El cuerpo', 'Los muchos', 'Lo que no habla', 'La emergencia', 'Lo que se recibe', 'El campo']
ARQ = ['El Campo', 'El Sonámbulo', 'El Testigo', 'El Cuerpo', 'La Grieta', 'Las Pequeñas Muertes',
       'No Saber', 'El Peso', 'El Personaje', 'La Corriente', 'La Red', 'La Obra', 'Habitar']

# Los siete anillos, de adentro hacia afuera, en el orden de la gestación.
ANILLOS = [
    ('origen', 'Trinity Origen'),
    ('quantum', 'Trinity Quantum'),
    ('infinito', 'Trinity Infinito'),
    ('vida', 'Portal Público · La vida interior, libros 1 a 13'),
    ('trama', 'Portal Público · La trama, libros 14 a 26'),
    ('campo', 'Portal Público · El campo, libros 27 a 39'),
    ('arq', 'Arquitectura del Destino'),
]


def libro(r, ruta):
    """(id del libro, lugar dentro del libro) para una ruta del inventario, o None."""
    partes = ruta.split('/')
    archivo = partes[-1]
    if r == 'T':
        if ruta.startswith('00_Portal_Trinity'):
            return None  # La Puerta: fuera de los anillos
        m = re.match(r'0([12])_Trinity_(Origen|Quantum)/Libro_(\d+)/', ruta)
        if m:
            serie = 'origen' if m.group(2) == 'Origen' else 'quantum'
            k = re.match(r'nodo_(\d+)\.html', archivo)
            lugar = 'nodo %d' % int(k.group(1)) if k else 'índice'
            return '%s-%d' % (serie, int(m.group(3))), lugar
        if ruta == '02_Trinity_Quantum/index.html':
            return 'quantum-1', 'portal de la serie'
        m = re.match(r'Trinity_Infinito/Libro_?(\d+)/', ruta)
        if m:
            n = int(m.group(1))
            k = re.search(r'Nodo(\d+)\.html', archivo)
            lugar = 'portal %d' % ((n - 1) * 7 + int(k.group(1))) if k else 'portales %d a %d' % ((n - 1) * 7 + 1, n * 7)
            return 'infinito-%d' % n, lugar
        return None
    m = re.match(r'02_Arquitectura_del_Destino/libro-(\d+)-', ruta)
    if m:
        k = re.search(r'-U(\d+)\.html', archivo)
        if k:
            lugar = 'umbral %s' % ROMANOS[int(k.group(1))]
        elif archivo.endswith('cierre.html'):
            lugar = 'cierre'
        else:
            lugar = 'portada'
        return 'arq-%d' % int(m.group(1)), lugar
    if ruta == '02_Arquitectura_del_Destino/index.html':
        return 'arq-1', 'índice de la serie'
    m = re.match(r'01_Libros/(\d+)_', ruta)
    if m:
        n = int(m.group(1))
        k = re.match(r'umbral[-_](\d+)', archivo) or re.match(r'capitulo_(\d+)', archivo)
        if k and archivo.startswith('capitulo'):
            lugar = 'capítulo %d' % int(k.group(1))
        elif k:
            lugar = 'umbral %s' % ROMANOS[int(k.group(1))] if int(k.group(1)) < len(ROMANOS) else 'umbral %d' % int(k.group(1))
        elif archivo == 'cierre.html':
            lugar = 'cierre'
        else:
            lugar = 'portada'
        return 'portal-%d' % n, lugar
    return None


def url(r, ruta):
    return (BASE_T if r == 'T' else REL_P) + ruta


def catalogo():
    libros = []
    for i, t in enumerate(ORIGEN, 1):
        libros.append(dict(id='origen-%d' % i, anillo=0, pos=i, titulo=t,
                           serie='Trinity Origen, libro %s' % ROMANOS[i],
                           url=BASE_T + '01_Trinity_Origen/Libro_%02d/index.html' % i))
    for i, t in enumerate(QUANTUM, 1):
        libros.append(dict(id='quantum-%d' % i, anillo=1, pos=i, titulo=t,
                           serie='Trinity Quantum, libro %d' % i,
                           url=BASE_T + '02_Trinity_Quantum/Libro_%02d/index.html' % i))
    for i, t in enumerate(INFINITO, 1):
        if i < 10:
            ruta = 'Trinity_Infinito/Libro%d/L%d-Nodo1.html' % (i, i)
        elif i < 13:
            ruta = 'Trinity_Infinito/Libro_%d/L_%d-Nodo1.html' % (i, i)
        else:
            ruta = 'Trinity_Infinito/Libro_13/Libro_13.html'
        libros.append(dict(id='infinito-%d' % i, anillo=2, pos=i, titulo=t,
                           serie='Trinity Infinito, libro %d' % i, url=BASE_T + ruta))
    return libros


def main():
    raiz_p, entrada, salida = sys.argv[1], sys.argv[2], sys.argv[3]
    hoy = datetime.date.today()
    fecha = sys.argv[4] if len(sys.argv) > 4 else '%d de %s de %d' % (hoy.day, MESES[hoy.month - 1], hoy.year)
    datos = json.load(open(entrada, encoding='utf-8'))['puertas']

    libros = catalogo()
    # Portal y Arquitectura: los nombres reales de las carpetas
    carpetas_p, carpetas_a = {}, {}
    for c in os.listdir(os.path.join(raiz_p, '01_Libros')):
        m = re.match(r'(\d+)_', c)
        if m:
            carpetas_p[int(m.group(1))] = c
    for c in os.listdir(os.path.join(raiz_p, '02_Arquitectura_del_Destino')):
        m = re.match(r'libro-(\d+)-', c)
        if m:
            carpetas_a[int(m.group(1))] = c
    for i, t in enumerate(PORTAL, 1):
        anillo = 3 + (i - 1) // 13
        c = carpetas_p.get(i)
        libros.append(dict(id='portal-%d' % i, anillo=anillo, pos=(i - 1) % 13 + 1, titulo=t,
                           serie='Portal Público, libro %d' % i,
                           url=REL_P + '01_Libros/%s/index.html' % c if c else REL_P + 'index.html'))
    for i, t in enumerate(ARQ, 1):
        c = carpetas_a.get(i)
        libros.append(dict(id='arq-%d' % i, anillo=6, pos=i, titulo=t,
                           serie='Arquitectura del Destino, libro %d' % i,
                           url=REL_P + '02_Arquitectura_del_Destino/%s/L%02d.html' % (c, i) if c
                           else REL_P + '02_Arquitectura_del_Destino/index.html'))

    # Hilos: un hilo por par de libros; dentro, sus puertas.
    hilos, fuera, sin_lugar = {}, 0, []
    for x in datos:
        a, b = libro(*x['desde']), libro(*x['hacia'])
        if a is None or b is None:
            if 'La Puerta' in (x['serie_desde'], x['serie_hacia']):
                fuera += 1
            else:
                sin_lugar.append((x['desde'], x['hacia']))
            continue
        if a[0] == b[0]:
            continue
        clave = tuple(sorted([a[0], b[0]]))
        h = hilos.setdefault(clave, dict(a=clave[0], b=clave[1], vuelve=False, puertas=[]))
        h['vuelve'] = h['vuelve'] or bool(x['vuelve'])
        h['puertas'].append(dict(desde=a[0], hacia=b[0],
                                 ld=a[1], lh=b[1],
                                 ud=url(*x['desde']), uh=url(*x['hacia'])))

    data = dict(libros=libros, hilos=list(hilos.values()), anillos=[n for _, n in ANILLOS],
                fecha=fecha, puertaUrl=BASE_T + '00_Portal_Trinity/index.html',
                total=sum(len(h['puertas']) for h in hilos.values()))
    html = PLANTILLA.replace('/*DATOS*/', json.dumps(data, ensure_ascii=False, separators=(',', ':')))
    open(salida, 'w', encoding='utf-8').write(html)
    tocados = {h['a'] for h in hilos.values()} | {h['b'] for h in hilos.values()}
    print('Puertas en el mapa: %d · hilos: %d (de ida y vuelta: %d) · libros con puertas: %d de %d'
          % (data['total'], len(hilos), sum(h['vuelve'] for h in hilos.values()), len(tocados), len(libros)))
    print('Puertas de La Puerta, fuera del mapa: %d' % fuera)
    if sin_lugar:
        print('Sin lugar en el mapa (revisar):')
        for s in sin_lugar:
            print('  ', s)
    print('Escrito en', salida)


PLANTILLA = r'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>El mapa de la Red · Portal Trinity</title>
<meta name="color-scheme" content="dark">
<style>
:root{
  --fondo:#070609; --texto:#f3efe7; --desc:#a49aac; --tenue:#6f6676; --oro:#d9b56a; --oro-hondo:#8a6f35;
  --borde:#241e2c;
  --origen:#a48fe0; --quantum:#4fbf9f; --infinito:#e0759d; --portal:#b3ab9b; --arq:#64a2e4;
  color-scheme:dark;
}
*{box-sizing:border-box}
html{font-size:112.5%;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--fondo);color:var(--texto);font-family:Georgia,"Times New Roman",serif;line-height:1.6;
  padding:env(safe-area-inset-top,0px) env(safe-area-inset-right,0px) env(safe-area-inset-bottom,0px) env(safe-area-inset-left,0px)}
a{color:var(--oro);text-decoration-color:rgba(217,181,106,.35);text-underline-offset:3px}
a:hover{text-decoration-color:var(--oro)}
a:focus-visible,button:focus-visible,.libro:focus-visible{outline:2px solid var(--oro);outline-offset:3px}
.pagina{max-width:44rem;margin:0 auto;padding:2.2rem 1.1rem 3rem}
header{text-align:center}
h1{font-weight:normal;font-size:2.05rem;letter-spacing:.015em;margin:0 0 .7rem;line-height:1.2}
.lema{color:var(--desc);margin:0 auto;max-width:31rem;font-size:1rem}
.antes{margin:1.1rem auto 0;font-size:.92rem;color:var(--desc);max-width:31rem}
.mandala{display:block;width:100%;max-width:640px;margin:1.2rem auto .4rem;touch-action:manipulation;-webkit-tap-highlight-color:transparent}
.guia{fill:none;stroke:#ffffff;stroke-opacity:.055;stroke-width:.5}
.hilo{fill:none;stroke-linecap:round;transition:stroke-opacity .5s,stroke-width .5s}
.hilo.uno{stroke:#9a92a6;stroke-opacity:.24;stroke-width:.55}
.hilo.ida{stroke:var(--oro);stroke-opacity:.85;stroke-width:1}
.toque{fill:none;stroke:transparent;stroke-width:9;pointer-events:none;cursor:pointer}
.libro{cursor:pointer;outline:none}
.libro .p{transition:opacity .35s}
.libro .halo{fill:none;stroke:var(--texto);stroke-width:.8;opacity:0;transition:opacity .35s}
.libro .area{fill:transparent}
.sel .hilo{stroke-opacity:.05}
.sel .hilo.on.uno{stroke-opacity:.85;stroke-width:1.1}
.sel .hilo.on.ida{stroke-opacity:1;stroke-width:1.6}
.sel .hilo.foco{stroke-width:2.4}
.sel .toque.on{pointer-events:stroke}
.sel .libro .p{opacity:.28}
.sel .libro.cerca .p{opacity:1}
.sel .libro.elegido .p{opacity:1}
.sel .libro.elegido .halo{opacity:.9}
.anillo{transition:opacity 1s ease, transform 1s ease;transform-box:view-box;transform-origin:50% 50%}
.hilos{transition:opacity 1.6s ease}
.inicio .anillo{opacity:0;transform:scale(.94)}
.inicio .hilos{opacity:0}
.panel{border-top:1px solid var(--borde);margin-top:.6rem;padding-top:1.1rem;min-height:6rem}
.panel .invita{color:var(--desc);text-align:center;margin:.2rem 0}
.panel .serie{color:var(--desc);font-size:.88rem;margin:0}
.panel h2{font-weight:normal;font-size:1.5rem;margin:.1rem 0 .3rem;line-height:1.25}
.panel .abrir{font-size:.95rem}
.panel .cuenta{color:var(--desc);font-size:.9rem;margin:.9rem 0 .4rem}
.filas{list-style:none;margin:0;padding:0}
.fila{display:grid;grid-template-columns:.8rem minmax(0,1fr);gap:.7rem;padding:.75rem 0;border-bottom:1px solid var(--borde);transition:background .6s}
.fila.foco{background:rgba(217,181,106,.07)}
.marca{width:.62rem;height:.62rem;border-radius:50%;margin-top:.5rem}
.fila .otro{margin:0;line-height:1.35}
.fila .otro a{color:var(--texto);text-decoration-color:rgba(243,239,231,.25)}
.fila .donde{display:block;color:var(--desc);font-size:.85rem}
.fila .vuelta{color:var(--oro);font-size:.85rem}
.cruces{margin:.35rem 0 0;font-size:.92rem;display:flex;flex-wrap:wrap;gap:.3rem .9rem;align-items:baseline}
.cruces span{color:var(--tenue);font-size:.85rem}
.leyenda{margin:2rem 0 0;padding:0;list-style:none;font-size:.88rem;color:var(--desc);columns:2 15rem;column-gap:1.5rem}
.leyenda li{break-inside:avoid;margin:.15rem 0;display:flex;gap:.55rem;align-items:baseline}
.leyenda .marca{flex:none;margin-top:0;position:relative;top:.05rem}
.trazos{display:flex;flex-wrap:wrap;justify-content:center;gap:.4rem 1.6rem;color:var(--desc);font-size:.88rem;margin:1rem 0 0}
.trazos svg{vertical-align:middle;margin-right:.45rem}
details{margin-top:2rem;border-top:1px solid var(--borde);padding-top:1rem}
summary{cursor:pointer;color:var(--texto)}
details h3{font-weight:normal;color:var(--desc);font-size:.95rem;margin:1.2rem 0 .3rem}
.lista{list-style:none;margin:0;padding:0;font-size:.93rem}
.lista button{all:unset;cursor:pointer;color:var(--texto);padding:.12rem 0}
.lista button:hover,.lista button:focus-visible{color:var(--oro)}
.lista .n{color:var(--tenue);font-size:.82rem;margin-left:.4rem}
footer{margin-top:2.4rem;text-align:center;color:var(--tenue);font-size:.85rem}
footer p{margin:.3rem 0}
@media (max-width:480px){html{font-size:118.75%}.pagina{padding-top:1.6rem}h1{font-size:1.75rem}}
@media (prefers-reduced-motion:reduce){.anillo,.hilos,.hilo,.libro .p,.libro .halo,.fila{transition:none}}
</style>
</head>
<body>
<div class="pagina">
<header>
  <h1>El mapa de la Red</h1>
  <p class="lema">Cada punto es un libro; cada hilo, una puerta entre dos de ellos. Los anillos van del centro hacia afuera en el orden en que la obra fue llegando.</p>
  <p class="antes">Si es tu primera vez en la serie mayor, empieza por <a id="puerta" href="#">La Puerta</a>.</p>
</header>

<svg class="mandala inicio" id="mandala" viewBox="-200 -200 400 400" role="group" aria-label="Mandala de la Red: siete anillos de trece libros alrededor de un centro vacío">
  <g id="guias"></g>
  <g class="hilos" id="hilos"></g>
  <g id="toques"></g>
  <g id="anillos"></g>
</svg>

<section class="panel" id="panel" aria-live="polite"></section>

<ul class="leyenda" id="leyenda"></ul>
<p class="trazos">
  <span><svg width="26" height="8" aria-hidden="true"><line x1="1" y1="4" x2="25" y2="4" stroke="#d9b56a" stroke-width="2"/></svg>ida y vuelta</span>
  <span><svg width="26" height="8" aria-hidden="true"><line x1="1" y1="4" x2="25" y2="4" stroke="#9a92a6" stroke-width="1.2"/></svg>una sola dirección</span>
</p>

<details id="detalles">
  <summary>La Red en lista</summary>
  <div id="lista"></div>
</details>

<footer>
  <p id="resumen"></p>
  <p><a href="../index.html">Volver al Portal</a><span aria-hidden="true"> &nbsp;·&nbsp; </span><a href="https://soyartur-trinity.github.io/Trinity-/#atrio">Volver al Stargate</a></p>
</footer>
</div>

<script>
const D=/*DATOS*/;
const NS='http://www.w3.org/2000/svg';
const COLOR=['--origen','--quantum','--infinito','--portal','--portal','--portal','--arq'].map(v=>getComputedStyle(document.documentElement).getPropertyValue(v).trim());
const R=188, R0=.30, VACIO=.15*R;
const porId={}; D.libros.forEach(l=>porId[l.id]=l);
function polar(l){const r=R*(R0+(1-R0)*l.anillo/6), t=-Math.PI/2+2*Math.PI*(l.pos-1)/13; return [r,t];}
function xy(r,t){return [r*Math.cos(t), r*Math.sin(t)];}
function el(tag,at,padre){const e=document.createElementNS(NS,tag); for(const k in at) e.setAttribute(k,at[k]); if(padre) padre.appendChild(e); return e;}

// Guías de los anillos
D.anillos.forEach((_,j)=>el('circle',{class:'guia',r:(R*(R0+(1-R0)*j/6)).toFixed(1)},document.getElementById('guias')));

// Hilos: rodean el centro sin cruzarlo
function trazo(a,b){
  const [r1,t1]=polar(a), [r2,t2]=polar(b);
  let d=((t2-t1+Math.PI)%(2*Math.PI)+2*Math.PI)%(2*Math.PI)-Math.PI;
  const hondo=(Math.min(r1,r2)-VACIO)*Math.pow(Math.abs(d)/Math.PI,.6)*.85;
  // Mismo radio (libros del mismo número): un arco leve, para no pasar por encima de los puntos intermedios
  const arco=Math.abs(d)<1e-6 ? .035*Math.abs(a.anillo-b.anillo) : 0;
  const N=36, pts=[];
  for(let k=0;k<=N;k++){const u=k/N, r=(1-u)*r1+u*r2-hondo*Math.sin(Math.PI*u); pts.push(xy(r,t1+u*d+arco*Math.sin(Math.PI*u)));}
  let s='M'+pts[0][0].toFixed(1)+' '+pts[0][1].toFixed(1);
  for(let i=0;i<pts.length-1;i++){
    const p0=pts[Math.max(i-1,0)],p1=pts[i],p2=pts[i+1],p3=pts[Math.min(i+2,pts.length-1)];
    const c1=[p1[0]+(p2[0]-p0[0])/6,p1[1]+(p2[1]-p0[1])/6], c2=[p2[0]-(p3[0]-p1[0])/6,p2[1]-(p3[1]-p1[1])/6];
    s+=' C'+c1.map(v=>v.toFixed(1)).join(' ')+' '+c2.map(v=>v.toFixed(1)).join(' ')+' '+p2.map(v=>v.toFixed(1)).join(' ');
  }
  return s;
}
const gH=document.getElementById('hilos'), gT=document.getElementById('toques');
const vecinos={}; D.libros.forEach(l=>vecinos[l.id]=[]);
D.hilos.sort((x,y)=>x.vuelve-y.vuelve).forEach((h,i)=>{
  const d=trazo(porId[h.a],porId[h.b]);
  h.linea=el('path',{d,class:'hilo '+(h.vuelve?'ida':'uno')},gH);
  h.toque=el('path',{d,class:'toque'},gT);
  h.toque.addEventListener('click',ev=>{ev.stopPropagation(); enfocarHilo(h);});
  vecinos[h.a].push(h); vecinos[h.b].push(h);
});

// Libros: un anillo por grupo, para la entrada en orden de gestación
const gA=document.getElementById('anillos'), grupos=[];
D.anillos.forEach((_,j)=>grupos.push(el('g',{class:'anillo'},gA)));
D.libros.forEach(l=>{
  const [r,t]=polar(l), [x,y]=xy(r,t), n=vecinos[l.id].reduce((s,h)=>s+h.puertas.length,0);
  const g=el('g',{class:'libro',tabindex:'0',role:'button','aria-label':l.serie+': '+l.titulo+(n?', '+n+(n==1?' puerta':' puertas'):', sin puertas todavía')},grupos[l.anillo]);
  el('circle',{class:'area',cx:x.toFixed(1),cy:y.toFixed(1),r:10.5},g);
  el('circle',{class:'halo',cx:x.toFixed(1),cy:y.toFixed(1),r:9},g);
  l.r=l.anillo>=3&&l.anillo<=5?3.1:3.6;
  l.p=el('circle',{class:'p',cx:x.toFixed(1),cy:y.toFixed(1),r:l.r,fill:COLOR[l.anillo]},g);
  l.g=g;
  g.addEventListener('click',ev=>{ev.stopPropagation(); elegir(elegido===l?null:l);});
  g.addEventListener('keydown',ev=>{if(ev.key==='Enter'||ev.key===' '){ev.preventDefault(); elegir(elegido===l?null:l);}});
});

const svg=document.getElementById('mandala'), panel=document.getElementById('panel');
svg.addEventListener('click',()=>elegir(null));
let elegido=null;
const esc=s=>s.replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));

function vacio(){
  panel.innerHTML='<p class="invita">Toca un libro para ver sus puertas y cruzar.</p>';
}
function elegir(l){
  elegido=l;
  D.libros.forEach(x=>{x.g.classList.remove('elegido','cerca'); x.p.setAttribute('r',x.r);});
  D.hilos.forEach(h=>{h.linea.classList.remove('on','foco'); h.toque.classList.remove('on');});
  if(!l){svg.classList.remove('sel'); vacio(); return;}
  svg.classList.add('sel'); l.g.classList.add('elegido'); l.p.setAttribute('r',5.4);
  const hs=vecinos[l.id].slice().sort((x,y)=>{const o=h=>porId[h.a===l.id?h.b:h.a]; return o(x).anillo-o(y).anillo||o(x).pos-o(y).pos;});
  hs.forEach(h=>{h.linea.classList.add('on'); h.toque.classList.add('on'); porId[h.a===l.id?h.b:h.a].g.classList.add('cerca');});
  const n=hs.reduce((s,h)=>s+h.puertas.length,0);
  let html='<p class="serie">'+esc(l.serie)+'</p><h2>'+esc(l.titulo)+'</h2><a class="abrir" href="'+l.url+'">Abrir el libro</a>';
  if(!n){html+='<p class="cuenta">Este libro todavía no tiene puertas hacia otras series.</p>'; panel.innerHTML=html; return;}
  html+='<p class="cuenta">'+n+(n==1?' puerta':' puertas')+' hacia '+hs.length+(hs.length==1?' libro':' libros')+'</p><ul class="filas">';
  hs.forEach(h=>{
    const o=porId[h.a===l.id?h.b:h.a], vistos=new Set(), enlaces=[];
    h.puertas.forEach(p=>{
      const [u,lug]= p.hacia===o.id ? [p.uh,p.lh] : [p.ud,p.ld];
      if(!vistos.has(u)){vistos.add(u); enlaces.push('<a href="'+u+'">'+esc(lug)+'</a>');}
    });
    html+='<li class="fila" data-o="'+o.id+'"><span class="marca" style="background:'+COLOR[o.anillo]+'"></span><div>'+
      '<p class="otro"><a href="'+o.url+'">'+esc(o.titulo)+'</a><span class="donde">'+esc(o.serie)+(h.vuelve?' · <span class="vuelta">ida y vuelta</span>':'')+'</span></p>'+
      '<p class="cruces"><span>Cruzar a</span>'+enlaces.join('')+'</p></div></li>';
  });
  panel.innerHTML=html+'</ul>';
}
function enfocarHilo(h){
  if(!elegido) return;
  D.hilos.forEach(x=>x.linea.classList.remove('foco')); h.linea.classList.add('foco');
  const o=h.a===elegido.id?h.b:h.a, fila=panel.querySelector('[data-o="'+o+'"]');
  if(fila){panel.querySelectorAll('.fila.foco').forEach(f=>f.classList.remove('foco')); fila.classList.add('foco');
    fila.scrollIntoView({block:'nearest',behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'});}
}

// Leyenda, lista y resumen
const ley=document.getElementById('leyenda');
D.anillos.forEach((nombre,j)=>{const li=document.createElement('li'); li.innerHTML='<span class="marca" style="background:'+COLOR[j]+'"></span><span>'+esc(nombre)+'</span>'; ley.appendChild(li);});
const lista=document.getElementById('lista');
D.anillos.forEach((nombre,j)=>{
  lista.insertAdjacentHTML('beforeend','<h3>'+esc(nombre)+'</h3>');
  const ul=document.createElement('ul'); ul.className='lista';
  D.libros.filter(l=>l.anillo===j).forEach(l=>{
    const n=vecinos[l.id].reduce((s,h)=>s+h.puertas.length,0), li=document.createElement('li'), b=document.createElement('button');
    b.textContent=l.titulo; b.addEventListener('click',()=>{elegir(l); svg.scrollIntoView({block:'start',behavior:'smooth'});});
    li.appendChild(b); li.insertAdjacentHTML('beforeend','<span class="n">'+(n?n+(n==1?' puerta':' puertas'):'sin puertas')+'</span>'); ul.appendChild(li);
  });
  lista.appendChild(ul);
});
const tocados=new Set(); D.hilos.forEach(h=>{tocados.add(h.a); tocados.add(h.b);});
document.getElementById('resumen').textContent=D.total+' puertas entre '+tocados.size+' libros; '+D.hilos.filter(h=>h.vuelve).length+' hilos de ida y vuelta. Datos del '+D.fecha+'.';
document.getElementById('puerta').href=D.puertaUrl;
vacio();

// Entrada: los anillos aparecen en el orden en que llegaron; después, los hilos
if(matchMedia('(prefers-reduced-motion: reduce)').matches){svg.classList.remove('inicio');}
else{
  svg.classList.remove('inicio');
  grupos.forEach(g=>{g.style.opacity=0; g.style.transform='scale(.94)';});
  gH.style.opacity=0;
  requestAnimationFrame(()=>requestAnimationFrame(()=>{
    grupos.forEach((g,j)=>setTimeout(()=>{g.style.opacity=''; g.style.transform='';},250+j*330));
    setTimeout(()=>{gH.style.opacity='';},250+7*330);
  }));
}
</script>
</body>
</html>
'''

if __name__ == '__main__':
    main()
