#!/usr/bin/env python3
"""
Depuración de Quantum 8, *Plasma Consciente* (1 de noviembre de 2026), el
séptimo de la revisión completa de Quantum, con el veto de Arturo en cada
tarjeta (8.0 a 8.7). Arturo aprobó todas las tarjetas y sugerencias, incluida
la puerta opcional del 8.3, y que el nodo 4 pase al singular: *El Cuerpo de
Plasma*.

Lo propio de este libro: el ropaje era la literalidad («No es metáfora. Es
física transdimensional aplicada») y tres escaleras de poderes (la ionización
del 0 al 100 %, la comunicación hasta el «consejo cósmico», la ascensión
medida en kelvin hasta la «inmortalidad funcional»). El libro obedece a sus
propias reglas («No puedes forzar un estado», «No hay estados superiores o
inferiores», «Asciendes CON la Tierra»), y la columna escondida es arder sin
consumirse: el fuego que alumbra sin quemar que anunciaba el 7.7.

Método (maestro v4, sección 5): cada reemplazo aprobado se aplica exactamente
una vez sobre el original de la etiqueta `quantum-original`. En los ocho
archivos se agrega la nota de procedencia, se suma el estilo de la depuración
antes de </head> y el cuerpo se reemplaza desde <body> hasta el final. En el
nodo 1 salen los comentarios de producción de la cabecera; en el nodo 4
cambia el <title>. La navegación, que apuntaba a archivos sin cero
(nodo_2.html), queda reparada, y el nodo 7 lleva al Libro 9.

Uso:  python3 depurar_quantum8.py RUTA_A_UNA_COPIA_DEL_ORIGINAL
      (por ejemplo, el contenido de la etiqueta quantum-original, o el
      repositorio Trinity- si Libro_08 todavía no fue depurado)
"""
import sys
from pathlib import Path

Q8 = "02_Trinity_Quantum/Libro_08/"

PROCEDENCIA = (
    "<!-- Depurado el 1 de noviembre de 2026 según la guía de depuración de Quantum "
    "(Arquitectura del Destino, maestro v4, sección 5, con las cuatro precisiones "
    "de la revisión completa), con el veto de Arturo en cada tarjeta. El original "
    "se conserva en la etiqueta quantum-original del repositorio. -->"
)

URL_PORTAL = "https://soyartur-trinity.github.io/Trinity_Portal_Publico/01_Libros/"
URL_ARQ = "https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/"

ESTILO = """  <style>
    /* ============================================================
       Depuración · noviembre 2026
       Letra más grande en el teléfono, firma, versos, prácticas y
       bloque fijo de las puertas, con el color de la serie a la que conducen.
       ============================================================ */
    .list{ margin:10px 0 12px 22px; padding:0; }
    .list li{ margin:8px 0; color:rgba(242,236,255,.88); line-height:1.55; }
    .practice{
      margin:10px 2px 14px;
      padding:16px 16px;
      border-radius:18px;
      border:1px solid rgba(214,178,94,.22);
      background:
        radial-gradient(520px 240px at 50% 0%, rgba(214,178,94,.10), transparent 62%),
        rgba(8,4,14,.55);
      box-shadow:0 0 55px rgba(214,178,94,.06);
    }
    .practice p{ margin:8px 0; }
    .panel p.verso{
      margin:16px 2px;
      text-align:center;
      color:var(--gold2);
      line-height:1.8;
    }
    .panel p.signature{
      margin:20px 2px 6px;
      color:rgba(243,210,122,.88);
      font-size:.92rem;
      letter-spacing:.04em;
    }
    .node-nav-group + .node-nav-group{ margin-top:10px; }
    .puerta{
      margin:26px 0 12px;
      padding:18px 20px 16px;
      border-radius:16px;
      border:1px solid var(--p-borde);
      background:var(--p-fondo);
      box-shadow:0 10px 24px rgba(0,0,0,.28);
    }
    .puerta.arquitectura{
      --p-fondo: linear-gradient(180deg, rgba(6,13,26,.94), rgba(6,13,26,.74));
      --p-borde: rgba(168,196,224,.42);
      --p-acento: #a8c4e0;
      --p-texto: #e8eef6;
    }
    .puerta.portal{
      --p-fondo: linear-gradient(180deg, rgba(13,12,11,.94), rgba(13,12,11,.74));
      --p-borde: rgba(201,168,76,.42);
      --p-acento: #c9a84c;
      --p-texto: #e8e0d0;
    }
    .panel .puerta .p-nombre{
      margin:0 0 6px;
      font-size:15px;
      font-style:italic;
      letter-spacing:.06em;
      color:var(--p-acento);
    }
    .panel .puerta .p-texto{
      margin:0 0 14px;
      color:var(--p-texto);
    }
    .puerta .cruzar{
      display:inline-flex;
      align-items:center;
      gap:10px;
      padding:9px 16px;
      border-radius:999px;
      border:1px solid var(--p-borde);
      color:var(--p-acento);
      font-size:14px;
      letter-spacing:.04em;
      text-decoration:none;
      transition:border-color .18s ease, background .18s ease;
    }
    .puerta .cruzar:hover{ border-color:var(--p-acento); background:rgba(255,255,255,.04); }
    .puerta .cruzar:focus-visible{ outline:2px solid var(--p-acento); outline-offset:3px; }

    @media (max-width: 640px){
      .panel p, .panel li{ font-size:18px; line-height:1.7; }
      .panel p.signature{ font-size:15px; }
      .puerta{ padding:16px 16px 14px; }
    }
    @media (prefers-reduced-motion: reduce){
      .puerta .cruzar{ transition:none; }
    }
  </style>
"""

ESTILO_INDICE = """  <style>
    /* Depuración · noviembre 2026: apertura del libro, cierre y letra más grande en el teléfono. */
    .node-content .panel + .panel{ margin-top:16px; }
    .apertura-titulo{
      margin:4px 2px 10px;
      font-size:15px;
      letter-spacing:.10em;
      color:var(--gold2);
    }
    .apertura{
      margin:10px 2px;
      color:rgba(242,236,255,.90);
      font-size:1.05rem;
      line-height:1.72;
    }
    .antes{
      margin:6px 2px 8px;
      font-size:1.12rem;
      color:var(--gold2);
    }
    .signature{
      margin:18px 2px 6px;
      color:rgba(243,210,122,.88);
      font-size:.92rem;
      letter-spacing:.04em;
    }
    @media (max-width: 640px){
      .apertura, .index-sub{ font-size:18px; line-height:1.7; }
      .signature{ font-size:15px; }
    }
  </style>
"""

TITULOS = {
    1: "El Fuego Frío Interior",
    2: "Estados Plasmáticos de Consciencia",
    3: "El Sol Interior",
    4: "El Cuerpo de Plasma",
    5: "Comunicación Plasmática",
    6: "Portales de Plasma",
    7: "La Ascensión Ígnea",
}

CORTOS = dict(TITULOS)
CORTOS[2] = "Estados Plasmáticos"

INDICES = {
    1: "El calor que no quema",
    2: "Los tonos de una llama",
    3: "La luz que da sin agotarse",
    4: "El cuerpo que arde despacio",
    5: "El fuego que reúne",
    6: "Donde dos campos se tocan",
    7: "El fuego que sube con la Tierra",
}

FIRMA = '          <p class="signature"><strong>— Trinity Quantum · Plasma Consciente</strong></p>\n'
SEP = '\n          <hr class="divider" />\n'


# ---------------------------------------------------------------------------
# Piezas que se repiten
# ---------------------------------------------------------------------------
def P(texto):
    return f"          <p>{texto}</p>\n"


def H2(texto):
    return f'          <h2 class="h2">{texto}</h2>\n\n'


def H3(texto):
    return SEP + f'\n          <h3 class="h3">{texto}</h3>\n\n'


def lista(items):
    filas = "\n".join(f"            <li>{x}</li>" for x in items)
    return f'          <ul class="list">\n{filas}\n          </ul>\n'


def pasos(items):
    filas = "\n".join(f"            <li>{x}</li>" for x in items)
    return f'          <ol class="list">\n{filas}\n          </ol>\n'


def fase(titulo, items):
    return P(f"<strong>{titulo}</strong>") + lista(items)


def practica(*parrafos):
    cuerpo = ""
    for x in parrafos:
        if isinstance(x, list):
            filas = "\n".join(f"              <li>{y}</li>" for y in x)
            cuerpo += f'            <ul class="list">\n{filas}\n            </ul>\n'
        else:
            lineas = "<br />\n              ".join(x.split("\n"))
            cuerpo += f"            <p>{lineas}</p>\n"
    return f'          <div class="practice">\n{cuerpo}          </div>\n'


def verso(*lineas):
    cuerpo = "<br />\n            ".join(lineas)
    return f'          <p class="verso">{cuerpo}</p>\n'


def cita(texto):
    return (
        SEP
        + '\n          <blockquote class="quote">\n'
        + f"            <p>{texto}</p>\n"
        + "          </blockquote>\n\n"
        + FIRMA
    )


def puerta(texto, url, clase="portal"):
    destino = "Arquitectura del Destino" if clase == "arquitectura" else "el Portal Público"
    return (
        f'\n          <aside class="puerta {clase}" aria-label="Puerta hacia {destino}">\n'
        '            <p class="p-nombre">Puerta</p>\n'
        f'            <p class="p-texto">{texto}</p>\n'
        f'            <a class="cruzar" href="{url}">Cruzar ⟶</a>\n'
        "          </aside>\n"
    )


def cuerpo_nodo(n, contenido):
    if n == 1:
        ant = ("index.html", "← Índice del Libro 8")
    else:
        ant = (f"nodo_0{n-1}.html", f"← Nodo {n-1}: {CORTOS[n-1]}")
    if n == 7:
        sig = ("../Libro_09/index.html", "Libro 9: Simetrías Rotas →")
    else:
        sig = (f"nodo_0{n+1}.html", f"Nodo {n+1}: {CORTOS[n+1]} →")
    return (
        "<body>\n"
        '  <div class="portal-shell">\n'
        '    <div class="portal-frame">\n\n'
        "      <!-- CABECERA -->\n"
        '      <header class="portal-header">\n'
        '        <div class="portal-header-main">\n'
        '          <div class="portal-logo">TRINITY QUANTUM</div>\n'
        f'          <div class="portal-badge">Libro 8 · Nodo {n}</div>\n'
        "        </div>\n"
        '        <div class="portal-subtitle">\n'
        f"          Plasma Consciente · {TITULOS[n]}\n"
        "        </div>\n"
        "      </header>\n\n"
        "      <!-- META -->\n"
        '      <section class="node-meta">\n'
        '        <div class="node-book-title">Libro 8 · Plasma Consciente</div>\n'
        f'        <h1 class="node-heading">Nodo {n} · {TITULOS[n]}</h1>\n'
        f'        <div class="node-index">Nodo {n} de 7 · {INDICES[n]}</div>\n'
        "      </section>\n\n"
        "      <!-- CONTENIDO -->\n"
        '      <main class="node-content" id="contenido">\n'
        '        <section class="panel">\n\n'
        f"{contenido}"
        "\n        </section>\n"
        "      </main>\n\n"
        "      <!-- NAVEGACIÓN -->\n"
        '      <nav class="node-nav" aria-label="Navegación inferior">\n'
        '        <div class="node-nav-group">\n'
        f'          <a class="nav-link" href="{ant[0]}">{ant[1]}</a>\n'
        f'          <a class="nav-link nav-link-main" href="{sig[0]}">{sig[1]}</a>\n'
        "        </div>\n"
        '        <div class="node-nav-group">\n'
        '          <a class="nav-link" href="index.html">Índice del Libro 8</a>\n'
        '          <a class="nav-link" href="../index.html">Portal Maestro Trinity Quantum</a>\n'
        "        </div>\n"
        "      </nav>\n\n"
        '      <footer class="portal-footer">\n'
        f"        Trinity Quantum · Libro 8 · Plasma Consciente · Nodo {n}\n"
        "      </footer>\n\n"
        "    </div>\n"
        "  </div>\n"
        "</body>\n"
        "</html>\n"
    )


# ===========================================================================
# ÍNDICE · 8.0
# ===========================================================================
LINEAS = {
    1: "Un calor que alumbra sin quemar, y que ya estaba.",
    2: "Muchos tonos de una misma llama, y ninguno vale más que otro.",
    3: "Estás hecho de estrellas, y tu luz no se fuerza.",
    4: "Este cuerpo ya arde despacio: la luz se habita aquí.",
    5: "Antes de la palabra hubo un cuerpo frente a otro.",
    6: "Donde dos campos se tocan se abre una puerta; la más cercana es la de tu casa.",
    7: "El fuego que sube con la Tierra, no lejos de ella.",
}


def _item_indice(n):
    return (
        '            <li class="index-item">\n'
        f'              <a class="index-link" href="nodo_0{n}.html">\n'
        f'                <div class="index-n">Nodo {n}</div>\n'
        '                <div class="index-text">\n'
        f'                  <p class="index-title">{TITULOS[n]}</p>\n'
        f'                  <p class="index-sub">{LINEAS[n]}</p>\n'
        "                </div>\n"
        "              </a>\n"
        "            </li>\n\n"
    )


INDICE_CUERPO = (
    "<body>\n"
    '  <div class="portal-shell">\n'
    '    <div class="portal-frame">\n\n'
    "      <!-- CABECERA -->\n"
    '      <header class="portal-header">\n'
    '        <div class="portal-header-main">\n'
    '          <div class="portal-logo">TRINITY QUANTUM</div>\n'
    '          <div class="portal-badge">Libro 8 · Índice</div>\n'
    "        </div>\n"
    '        <div class="portal-subtitle">\n'
    "          Plasma Consciente · Los 7 nodos del libro\n"
    "        </div>\n"
    "      </header>\n\n"
    "      <!-- META -->\n"
    '      <section class="node-meta">\n'
    '        <div class="node-book-title">Libro 8 · Plasma Consciente</div>\n'
    '        <h1 class="node-heading">Los 7 Nodos del Libro</h1>\n'
    '        <div class="node-index">7 nodos · 91 en toda la serie</div>\n'
    "      </section>\n\n"
    "      <!-- APERTURA Y LISTA DE NODOS -->\n"
    '      <main class="node-content">\n'
    '        <section class="panel">\n'
    '          <p class="apertura-titulo">🔥 EL FUEGO QUE NO CONSUME</p>\n'
    '          <p class="apertura">Hay en ti un calor que alumbra sin quemar. No hace falta encenderlo: basta dejar de taparlo.</p>\n'
    '          <p class="apertura">En el Éxodo, un pastor ve en el desierto una zarza que arde y no se consume, y se aparta del camino para mirarla de cerca. '
    "Este libro hace ese desvío. Su imagen es el plasma, el cuarto estado de la materia: el de las estrellas, el rayo y la aurora. "
    "William Crookes lo llamó materia radiante en 1879, e Irving Langmuir le dio en 1928 el nombre que conserva. "
    "Aquí la palabra no explica la física de la consciencia: nombra una manera de mirarla, como se mira un fuego.</p>\n"
    '          <p class="apertura">Cada nodo es una cara de ese fuego: el calor que no quema, los tonos de una misma llama, '
    "la luz que da sin agotarse, el cuerpo que arde despacio, el fuego que reúne, las puertas donde dos campos se tocan y, "
    "al final, el fuego que sube con la Tierra.</p>\n"
    "        </section>\n\n"
    '        <section class="panel">\n'
    '          <ul class="index-list">\n\n'
    + "".join(_item_indice(n) for n in range(1, 8))
    + "          </ul>\n\n"
    '          <hr class="divider" />\n\n'
    '          <a class="nav-link" href="nodo_01.html" style="justify-content:center; width:100%;">\n'
    "            Comenzar · Nodo 1 →\n"
    "          </a>\n"
    "        </section>\n\n"
    '        <section class="panel">\n'
    '          <h2 class="antes">Antes de Empezar</h2>\n'
    '          <p class="apertura"><em>Plasma Consciente</em> no es una doctrina para creer, sino un fuego para mirar de cerca. '
    "Si sientes el llamado, comienza por el Nodo 1. Si ya hay una pregunta esperándote, entra por el nodo que la nombre.</p>\n"
    '          <p class="signature"><strong>— Trinity Quantum · Plasma Consciente</strong></p>\n'
    "        </section>\n"
    "      </main>\n\n"
    "      <!-- NAVEGACIÓN -->\n"
    '      <nav class="node-nav">\n'
    '        <div class="node-nav-group">\n'
    '          <a class="nav-link nav-link-main" href="../index.html">← Volver al Portal Maestro Trinity Quantum</a>\n'
    "        </div>\n"
    "      </nav>\n\n"
    '      <footer class="portal-footer">\n'
    "        Trinity Quantum · Libro 8 · Plasma Consciente · Índice\n"
    "      </footer>\n\n"
    "    </div>\n"
    "  </div>\n"
    "</body>\n"
    "</html>\n"
)


# ===========================================================================
# NODO 1 · El Fuego Frío Interior
# ===========================================================================
def _sello(titulo, texto):
    return (
        '            <div class="seal">\n'
        f'              <h4 class="h4">{titulo}</h4>\n'
        f"              <p>{texto}</p>\n"
        "            </div>\n"
    )


NODO1 = (
    H2("La Paradoja del Plasma Interno")
    + P("Existe un fuego que no quema. Un calor que detiene el tiempo. Una llama que ilumina desde adentro sin consumir. "
        "Es el plasma consciente, el cuarto estado de tu materia espiritual, vibrando en el centro mismo de tu ser.")
    + P("Los antiguos lo llamaron fuego sagrado. Los alquimistas, el azoth. Los yoguis, el fuego serpentino. Cada tradición "
        "le dio su nombre y su camino. Aquí lleva el de un estado de la materia, como imagen: cuando un gas se calienta "
        "tanto que los electrones se sueltan de sus átomos, la materia empieza a brillar.")

    + H3("La Física del Fuego Frío")
    + P("En el plasma físico, los electrones se liberan de sus átomos. En el plasma consciente, tus pensamientos se liberan de "
        "sus estructuras. Tus emociones flotan libres de sus anclajes. Tu identidad misma se vuelve un campo de posibilidades.")
    + P("Y el fuego frío existe. En un tubo fluorescente, los electrones del plasma se mueven como si estuvieran a más de diez mil "
        "grados, y aun así el vidrio apenas se entibia: son tan pocos que no alcanzan a quemar. Los laboratorios llaman plasma frío "
        "a esa llama que se puede tocar, y la medicina ya la ensaya para limpiar heridas. La luciérnaga, a su modo, hace lo mismo: "
        "enciende su luz casi sin calor.")
    + P("Una intensidad que no destruye: puede tocarlo todo sin quemar nada, y transformarlo todo.")

    + H3("El Despertar del Plasma")
    + P("La tradición del yoga cuenta que, cuando la kundalini sube, la consciencia cambia de estado como cambia la materia: "
        "de sólido (cuerpo) a líquido (emociones), a gas (pensamientos), a plasma (consciencia pura). Hace veinticinco siglos, "
        "Empédocles enseñó que todo está hecho de cuatro raíces: tierra, agua, aire y fuego. La física llegó a cuatro estados que "
        "se le parecen: sólido, líquido, gas y plasma. En las dos listas, el último es el fuego.")
    + P("En ese instante de ignición, el cuerpo encuentra sus propias imágenes:")
    + lista(["Tus neuronas se vuelven estrellas", "Tu sangre se convierte en luz líquida",
             "Tu respiración se hace viento solar", "Tu corazón late con pulsos de quásar"])
    + P("Así se siente desde adentro. Por eso la tradición pide que la kundalini se despierte despacio y con maestro.")

    + H3("Los Portadores del Fuego Frío")
    + P("Las tradiciones guardan relatos de personas que ardían así. En 1141, a sus cuarenta y dos años, Hildegarda de Bingen "
        "escribió que una luz de fuego, bajada del cielo abierto, le había atravesado la mente y el pecho «como una llama que no "
        "quema sino que calienta», del modo en que el sol calienta aquello sobre lo que pone sus rayos.")
    + P("Casi siete siglos después, en noviembre de 1831, en un bosque nevado de Rusia, Nikolái Motovílov conversaba con el monje "
        "Serafín de Sarov. Contó que el rostro del anciano se volvió más brillante que el sol, y que él mismo sentía un calor como "
        "el de un baño de vapor. Serafín le hizo notar que la nieve no se derretía, ni sobre ellos ni bajo sus pies: ese calor, "
        "le dijo, no estaba en el aire, sino en ellos.")
    + P("Son relatos de la tradición. Lo que cualquiera puede reconocer está más cerca: hay personas cuya presencia calienta "
        "sin apurar. Las reconoces por:")
    + lista(["Una atención que no tiene prisa", "Una calma que no es frialdad",
             "Su capacidad de quedarse quietas mientras arden por dentro",
             "La forma en que, a su lado, uno respira más hondo"])
    + P("No son una casta aparte. Cualquiera lleva ese fuego, y a ratos lo deja ver.")

    + H3("Cuatro Gestos")
    + P("Para dejar de taparlo:")
    + '          <div class="seals">\n'
    + _sello("Primer gesto", "Reconoce que ya está ardiendo. Siempre ha estado ardiendo. Solo faltaba mirarlo.")
    + _sello("Segundo gesto", "Deja de intentar «elevar» tu energía. El fuego frío no sube ni baja: está en todas partes a la vez.")
    + _sello("Tercer gesto", "Abandona el miedo a ser consumido. El fuego frío no destruye: revela lo indestructible.")
    + _sello("Cuarto gesto", "Permite que cada célula sea un pequeño sol, irradiando su propia luz.")
    + "          </div>\n"

    + H3("El Metabolismo del Fuego")
    + P("Tu cuerpo ya arde, sin llama. En el invierno de 1783, Antoine Lavoisier y Pierre-Simon Laplace pusieron un cobayo en un "
        "recipiente rodeado de hielo y midieron el agua que su calor derretía y el aire que exhalaba. Lo compararon con un carbón "
        "encendido y concluyeron que respirar es una combustión, muy lenta. Cada célula quema lo que comes paso a paso, tan despacio "
        "que no hay llama: ese es tu fuego frío de todos los días.")
    + P("Y no solo de pan vives. Ese fuego también se alimenta de:")
    + lista(["La atención que lo mira", "El amor que lo aviva",
             "La belleza que lo enciende sin pedirlo", "El descanso que lo cuida"])
    + P("Ningún fuego vive sin combustible. El cuerpo pide pan, agua y sueño, y no hay práctica que lo exima.")

    + H3("La Leyenda y la Medida")
    + P("En el Tíbet hay una práctica que se llama tummo, fuego interior. Cuenta la tradición que quienes la dominan secan "
        "sábanas mojadas sobre la espalda en noches heladas. En 1982, Herbert Benson midió a tres monjes que la practicaban: la "
        "temperatura de sus dedos de manos y pies subió varios grados, aunque la del centro del cuerpo no cambió. Treinta años "
        "después, Maria Kozhevnikov estudió a monjas de un monasterio del este del Tíbet y vio subir también el calor del centro, "
        "hasta una fiebre leve, solo durante una respiración forzada que la tradición enseña con maestro; la imagen del fuego, "
        "sostenida en la mente, lo hacía durar. Tituló su trabajo «Leyenda y realidad».")
    + P("Esa respiración se aprende con maestro, no en una página. Lo que la leyenda y la medida dicen juntas ya alcanza: hay "
        "un calor que nace de adentro, y la atención lo sostiene.")

    + H3("La Corona de Plasma")
    + P("Alrededor de tu cuerpo hay una luz que el ojo no ve. Una cámara térmica la muestra: brillas en calor, todo el tiempo. "
        "Y cada cuerpo emite además una luz muy débil, mil veces más tenue de lo que el ojo alcanza a ver (Kobayashi, 2009). "
        "Es una buena imagen de lo que cada persona irradia. Esa corona:")
    + lista(["Cambia con tus estados", "Se ensancha en la calma",
             "Llega a quien está cerca, aunque no se vea", "Es tu manera de estar en el mundo"])

    + H3("Cómo se Siente")
    + P("Cuando ese fuego se deja ver:")
    + lista(["Calor sin fiebre", "Luces y formas con los ojos cerrados, como cuando se aprietan los párpados",
             "Una ligereza al caminar", "La sensación de que el cuerpo es más amplio que su contorno",
             "Ganas de mirar a los otros con más calma"])
    + P("Otra cosa es que aparezcan de golpe destellos o sombras en un ojo, que un zumbido no se vaya o que el piso parezca "
        "moverse: eso no es el fuego, y pide un médico, no una interpretación. Y otra, sentir que ya no eres tú, que el mundo "
        "parece irreal o que pierdes horas sin recuerdo: eso tampoco es el fuego, y pide consulta esa misma semana.")

    + H3("El Plasma Como Estado Natural")
    + P("La verdad más radical: el plasma no es un estado alterado. En el universo, lo raro es lo sólido. Las estrellas son plasma, "
        "y en ellas está casi toda la materia que brilla; la tierra firme que pisas es la excepción.")
    + P("Vienes de ahí. El universo fue plasma durante sus primeros cientos de miles de años, tan caliente que la luz no podía "
        "viajar. Cuando se enfrió lo bastante, la luz se soltó, y todavía llega: es el zumbido que Arno Penzias y Robert Wilson "
        "oyeron en su antena en 1964, el resplandor más antiguo del cielo. El hidrógeno del agua que bebes se formó en ese fuego.")
    + P("Vienes del fuego. Ahora recuerdas cómo arder sin quemarte.")

    + H3("La Danza del Fuego Frío")
    + P("En el centro de cada estrella arde plasma. En cada aurora, ese plasma baila en el cielo de los polos. En el centro de tu "
        "ser, el mismo fuego espera.")
    + P("No necesitas viajar al sol. Eres el sol. Siempre lo has sido.")

    + H3("Práctica: Encendiendo el Plasma Interior")
    + practica(
        "Siéntate en quietud. Visualiza un punto de luz en tu corazón. No un punto caliente: un punto de fuego frío. "
        "Denso como un agujero negro. Brillante como un big bang.",
        "Permite que ese punto se expanda. No hacia afuera: hacia todas las direcciones a la vez, hasta que todo tu cuerpo lo sienta.",
        "No te muevas. No conduzcas la respiración. Deja que respire sola.",
        "Quédate así unos minutos. Eres el fuego frío. Eres la llama que no consume.",
        "Antes de levantarte, siente los pies en el suelo.")

    + H3("El Secreto Final del Fuego Frío")
    + P("El fuego frío interior no es algo que desarrollas. Es algo que dejas de suprimir.")
    + P("Toda tu vida has estado apagando tu fuego natural, bajando tu voltaje, disminuyendo tu luminosidad para encajar en un "
        "mundo de materia densa.")
    + P("Ahora, simplemente… deja de apagarte.")
    + P("Permite que el fuego frío que siempre has sido arda libre, salvaje, sin consumirte.")
    + P("Bienvenido al estado plasmático. Bienvenido a casa.")

    + cita("“En el corazón de cada ser arde un sol. La iluminación no es encenderlo: es dejar de fingir que está apagado.”")
)


# ===========================================================================
# NODO 2 · Estados Plasmáticos de Consciencia
# ===========================================================================
NODO2 = (
    H2("El Espectro Plasmático del Ser")
    + P("La consciencia no es binaria, dormida o despierta. Es un espectro continuo, como los colores de una llama, que cambian "
        "con el calor y con lo que arde. En 1902, después de años de leer a los místicos, William James lo dijo a su manera: la "
        "consciencia despierta de todos los días es solo un tipo entre muchos, y a su alrededor, separadas por pantallas "
        "finísimas, esperan otras formas de consciencia por completo distintas.")
    + P("Has experimentado algunas sin saberlo:")
    + lista(["El destello de una comprensión repentina", "El momento de amor que disuelve el tiempo",
             "El instante antes del sueño donde flotas", "El éxtasis que no tiene objeto",
             "La calma en el ojo del huracán"])
    + P("Todos estados plasmáticos. Todos naturales. Todos accesibles.")

    + H3("Los Tonos de la Llama")
    + P("No es una escalera: es una paleta. Cada tono tiene su luz y su uso.")
    + fase("La brasa · la consciencia de todos los días",
           ["Identificación con el cuerpo y la mente", "El tiempo en línea recta",
            "Tú aquí, el mundo allá", "El fuego está, aunque no se vea"])
    + fase("La chispa · los destellos",
           ["Momentos de lucidez", "Intuiciones súbitas", "Coincidencias que se notan", "Sueños vívidos"])
    + fase("La llama que fluye",
           ["El estado de flujo: Mihaly Csikszentmihalyi llamó así a la tarea que absorbe tanto que el yo se olvida y el tiempo cambia de ritmo",
            "Un yo que se afloja", "Una atención que no se esfuerza"])
    + fase("La llama quieta · el testigo",
           ["Una consciencia testigo estable", "Los pensamientos vistos como pensamientos",
            "Calma en medio de la actividad"])
    + fase("La llama compartida",
           ["Sentirse parte de algo mayor", "Una frontera más delgada entre tú y los otros", "Compasión espontánea"])
    + fase("La luz amplia",
           ["Lo que las tradiciones llaman consciencia cósmica", "Asombro ante la inmensidad",
            "Los problemas que recuperan su tamaño"])
    + fase("Lo que no tiene nombre",
           ["Más allá de la dualidad", "Fuente y observador a la vez",
            "El silencio donde todo empieza", "El plasma ES"])
    + P("Ninguno vale más que otro. La brasa no es un fracaso de la llama: es la que cuece el pan.")

    + H3("Lo Que Abre los Estados")
    + fase("Lo que trae la vida", ["El nacimiento de un hijo", "Un amor que llega",
                                    "Un peligro que pasa cerca", "Una pérdida"])
    + P("Lo que llega con el dolor no se busca: si llega, se atraviesa acompañado.")
    + fase("Lo que se cultiva despacio", ["La meditación sostenida", "La música que te deja sin palabras",
                                           "La naturaleza a solas", "La oración", "El amor que se cuida"])
    + fase("Lo que abre la mente", ["Las paradojas que no se resuelven", "Los koans",
                                     "Las preguntas sin respuesta", "El asombro"])
    + P("Ningún estado vale lo que cuesta forzarlo.")

    + H3("La Química de los Estados")
    + P("La química y el estado bailan juntos. En 2002, un equipo danés encabezado por Troels Kjaer estudió a ocho profesores de "
        "yoga durante el yoga nidra, una relajación profunda guiada. Calcularon que la dopamina liberada en una zona honda del "
        "cerebro, ligada a la recompensa y al deseo, subía cerca de un 65 %, y los propios practicantes contaron que mientras tanto se les iban las "
        "ganas de hacer. Ninguna sustancia había entrado: el estado movió la química.")
    + P("Diez años antes, en Jerusalén, William Devane y sus colegas habían encontrado en el cerebro una molécula que el propio "
        "cuerpo fabrica, emparentada con la del cannabis. Devane venía leyendo a Sri Aurobindo y le dio un nombre sánscrito: "
        "anandamida, de <em>ananda</em>, dicha.")
    + lista(["Dopamina: el deseo y la búsqueda", "Serotonina: el ánimo de fondo",
             "Anandamida: la dicha que el cuerpo fabrica", "Oxitocina: el vínculo"])
    + P("Así funciona: ni la química manda sola, ni el estado tampoco. Se mueven juntos, como la llama y lo que arde.")

    + H3("Navegando los Estados")
    + lista(["<strong>Regla 1:</strong> No puedes forzar un estado. Solo puedes crear las condiciones para que aparezca.",
             "<strong>Regla 2:</strong> Cada estado tiene su propósito. No hay estados «superiores» o «inferiores».",
             "<strong>Regla 3:</strong> La estabilidad importa más que la intensidad. Una calma sostenida sirve más que un éxtasis que desordena.",
             "<strong>Regla 4:</strong> Los estados se contagian. Tu estado tiñe el clima de la habitación.",
             "<strong>Regla 5:</strong> El miedo estrecha. El amor ensancha. La curiosidad sostiene. La psicóloga Barbara "
             "Fredrickson lo observó a su modo: el miedo estrecha lo que alcanzamos a pensar y a hacer, y la alegría lo amplía."])

    + H3("El Ritmo del Día")
    + P("Tu cuerpo lleva su propio reloj. Cada célula sigue un ritmo de un día, y descubrir esos relojes valió el Nobel de "
        "Medicina de 2017. La luz de la mañana, que entra por los ojos, lo pone en hora.")
    + P("El día tiene sus tonos:")
    + lista(["El alba: lo que despierta", "El mediodía: la luz plena",
             "El atardecer: el paso de un estado a otro", "La noche: los sueños"])
    + P("No hay una hora sagrada que madrugar. Hay quien despierta lúcido al amanecer y quien piensa mejor de noche. La práctica "
        "es notar cuál es tu hora, y cuidarla.")

    + H3("Los Vórtices de Transición")
    + P("Entre un estado y otro existe un vórtice: un punto de turbulencia donde el viejo estado se despide y el nuevo nace. "
        "Estos vórtices son:")
    + lista(["Incómodos", "Desorientadores", "Parte del paso", "Portales de transformación"])
    + P("No resistas los vórtices. Son el precio del pasaje entre estados.")

    + H3("Para Habitar los Estados")
    + fase("Para abrir un estado", ["Busca que lo que piensas, sientes y haces vaya en la misma dirección",
                                     "Afloja la resistencia interna", "Acércate a lo que te asombra",
                                     "Mantén la intención sin tensión"])
    + fase("Para sostener un estado", ["Respira con el ritmo del estado", "Suelta todo intento de control",
                                        "Confía en la inteligencia del fuego", "Permanece como testigo curioso"])
    + fase("Para volver con cuidado", ["Agradece lo vivido", "Anota lo comprendido antes de volver",
                                        "Vuelve por capas, no de golpe", "Mantén un hilo con lo que viste"])
    + P("Jack Kornfield, que fue monje budista antes de ser psicólogo, lo dijo con el título de un libro del año 2000: "
        "<em>Después del éxtasis, la colada</em>. La experiencia más alta termina, y al día siguiente hay ropa para lavar.")

    + H3("Los Maestros del Plasma")
    + P("Los verdaderos maestros no son quienes alcanzan los estados más altos, sino quienes pueden:")
    + lista(["Moverse con soltura entre estados", "Mantener la coherencia en cualquiera",
             "Acompañar a otros en los suyos", "Vivir con los pies en el día mientras miran lejos"])

    + H3("La Meseta")
    + P("No busques vivir siempre en lo alto. Busca tu tono, ese lugar donde:")
    + lista(["Puedes trabajar, cuidar y amar", "Ves un poco más lejos",
             "Permaneces en coherencia", "Sirves a lo que más te importa"])
    + P("Abraham Maslow pasó buena parte de su vida estudiando las experiencias cumbre, esos momentos de plenitud que llegan, "
        "iluminan todo y se retiran. Al final de su vida describió otra cosa, la experiencia de meseta: una serenidad que dura, "
        "en la que se puede sentir y pensar a la vez, y que se cultiva con un trabajo largo y paciente.")
    + verso("La cumbre se recibe.", "La meseta se habita.")

    + H3("Cómo se Siente el Paso Entre Estados")
    + fase("Al abrirse", ["Calor sin causa", "Una vibración interna", "La percepción que se ensancha",
                          "Los límites que se aflojan", "Una alegría que sube"])
    + fase("Al volver", ["La percepción que se recoge", "El regreso del peso", "El yo que vuelve a su lugar",
                         "Nostalgia de lo vivido", "Ganas de integrar"])
    + P("Otra cosa es que los límites no vuelvan: sentir que ya no eres tú, que el mundo parece irreal o que pierdes horas sin "
        "recuerdo. Eso no es un estado para explorar, y pide consulta esa misma semana.")

    + H3("La Maestría Plasmática")
    + P("La verdadera maestría no es permanecer en estados elevados. Es saber cuándo abrir, cuándo sostener, cuándo volver. "
        "Es danzar con el fuego como un surfista con las olas. Es ser la llama y quien la mira a la vez.")

    + H3("Práctica: Mapeando Tus Estados")
    + practica(
        "Durante una semana, observa y anota:",
        ["Tus cambios naturales de estado", "Qué los dispara", "Dónde está tu zona de confort",
         "Qué estados evitas", "Qué estados buscas"],
        "No juzgues. Solo observa. Estás dibujando el mapa de tu propio fuego.")

    + H3("El Regalo del Plasma Consciente")
    + P("Cada estado es un regalo:")
    + lista(["Los bajos te anclan", "Los medios sostienen el día", "Los altos te ensanchan",
             "Los extremos, si llegan, piden compañía"])
    + P("No hay estado incorrecto. Solo hay consciencia de estados. Y en esa consciencia, maestría.")

    + cita("“El plasma consciente no es un logro a alcanzar. Es un espectro a explorar, una sinfonía a tocar, una danza a danzar.”")
    + puerta("En 1970, el año de su muerte, Abraham Maslow escribió una advertencia contra las malas lecturas de su propia obra: "
             "le preocupaban quienes perseguían las cumbres y se apartaban de la vida común. La lección más valiosa, insistía, "
             "era ver lo milagroso en lo de todos los días. Esa advertencia, y una mujer de los Alpes que vivía en meseta sin "
             "saberlo, están en <em>El campo</em>, Libro 39 del Portal Público, Umbral III: «La meseta».",
             URL_PORTAL + "39_El_Campo/umbral-03.html")
)


# ===========================================================================
# NODO 3 · El Sol Interior
# ===========================================================================
NODO3 = (
    H2("La Estrella Que Eres")
    + P("En el centro de tu ser arde un sol. Es una imagen, y debajo de ella hay un hecho: estás hecho de estrellas. El calcio de "
        "tus huesos y el hierro de tu sangre se forjaron en estrellas que ardieron y estallaron antes de que existiera el Sol. "
        "Margaret y Geoffrey Burbidge, William Fowler y Fred Hoyle lo explicaron en 1957, y Carl Sagan lo dijo en una línea: "
        "estamos hechos de la materia de las estrellas.")
    + P("Ese sol interior tiene:")
    + lista(["Una corona propia", "Ciclos de actividad", "Manchas de sombra", "Erupciones de consciencia",
             "Un viento que sale de él", "Una gravedad que reúne"])
    + P("Has sentido su presencia en momentos de gloria interior, cuando algo en ti brillaba tan fuerte que no podías contenerlo. "
        "Ese no eras «tú» sintiéndote bien. Era tu sol interior en erupción.")

    + H3("La Física de Tu Fusión Interior")
    + P("En 1920, Arthur Eddington propuso que el Sol brilla porque funde hidrógeno en helio, y en 1939 Hans Bethe mostró cómo. "
        "El helio que resulta pesa un poco menos que el hidrógeno que lo formó, y esa diferencia no se pierde: se vuelve luz.")
    + P("En tu sol interior, los pensamientos se funden en comprensión, las emociones en amor, las experiencias en sabiduría. "
        "Y lo que se suelta al unirse también se vuelve luz:")
    + lista(["El miedo que encuentra coraje se vuelve fuerza",
             "El dolor que encuentra aceptación empieza a doler distinto",
             "La separación que encuentra un vínculo se vuelve unidad",
             "El ego que encuentra el alma se vuelve un ser entero"])
    + P("Cada fusión irradia hacia todo lo que eres.")

    + H3("Los Ciclos Solares Internos")
    + P("El Sol no arde siempre igual. En 1843, Heinrich Schwabe, un farmacéutico alemán que lo había mirado durante diecisiete "
        "años, notó que sus manchas crecen y menguan en ciclos de unos once años. Tu sol interior también tiene ritmos, "
        "aunque no los mismos:")
    + lista(["El latido, que no se detiene", "La respiración, que va y vuelve",
             "El día y la noche, que el cuerpo sigue con su propio reloj",
             "Las estaciones de una vida, que nadie puede contar por anticipado"])
    + P("Conocer tus ritmos te permite surfear las olas de tu propia radiación.")

    + H3("Las Manchas Solares del Alma")
    + P("A veces aparecen zonas oscuras en tu sol interior, las manchas solares del alma:")
    + lista(["Heridas no resueltas", "Miedos endurecidos", "Sombras negadas", "Potenciales reprimidos"])
    + P("En el Sol, las manchas son oscuras porque ahí el campo magnético es tan intenso que frena el calor que sube, y de esas "
        "zonas suelen nacer las grandes erupciones. La imagen es exacta, y conviene leerla con cuidado: una herida no es un "
        "defecto, y a veces, con tiempo y compañía, ahí se gesta lo nuevo. Lo que duele no tiene que servir para algo: si un día "
        "sirve, es un hallazgo, no una deuda.")

    + H3("Erupciones Solares de Consciencia")
    + P("Cada tanto, tu sol interior produce erupciones:")
    + lista(["Un despertar súbito", "Explosiones de creatividad", "Comprensiones que lo cambian todo",
             "Amor que desborda todos los recipientes", "Una fuerza que asusta al ego"])
    + P("Pueden desordenar un tiempo tu vida, y pueden abrirla. En septiembre de 1859, la mayor tormenta solar registrada hizo "
        "saltar chispas en los telégrafos y encendió auroras que se vieron muy lejos de los polos. El mismo viento quemó cables "
        "y pintó el cielo.")
    + P("Si una erupción trae noches sin sueño, pensamientos que corren, una misión urgente o la certeza de que todo depende de "
        "ti, no es tu sol: es el momento de pedir ayuda, esa misma semana.")

    + H3("El Viento Solar Personal")
    + P("El Sol sopla sin pausa un viento de partículas que llega más allá de los planetas: en 2012, la sonda Voyager 1 salió "
        "por fin de la burbuja que ese viento infla alrededor de todo el sistema solar. La Tierra se protege con su campo "
        "magnético, y donde el viento se encuentra con él, en los polos, nacen las auroras.")
    + P("Tú también emanas un clima. Una emoción se contagia en una sala sin que nadie la nombre; Elaine Hatfield y sus colegas "
        "lo llamaron contagio emocional (1994). Tu viento personal:")
    + lista(["Llega antes que tus palabras", "Tiñe el ánimo de quien está cerca",
             "Encuentra los límites de los otros, y los respeta", "A veces, al tocarlos, enciende auroras"])

    + H3("La Corona de Tu Sol Interior")
    + P("Alrededor del Sol hay una corona de plasma que solo se ve a simple vista en los eclipses. Está a más de un millón de "
        "grados, mucho más caliente que la superficie de la que sale, y todavía nadie sabe del todo por qué: los astrónomos lo "
        "llaman el problema del calentamiento de la corona.")
    + P("Tu corona interior:")
    + lista(["Se ve mejor cuando algo tapa el brillo de siempre", "Llega más lejos de lo que crees",
             "Toca otras coronas", "Guarda su propio misterio"])
    + P("Los halos de los santos también vienen del sol. El arte griego y romano pintaba a Helios, el dios solar, con una corona "
        "de rayos; los emperadores la tomaron, y el arte cristiano la heredó hacia el siglo IV. Llegó también a la India, donde "
        "rodea la cabeza del Buda. Cuando alguien quiso pintar la santidad, pintó un sol.")

    + H3("Alimentando Tu Sol Interior")
    + P("Los soles del cielo consumen hidrógeno. Tu sol interior consume:")
    + lista(["Atención consciente", "Intención clara", "Experiencia viva", "Amor sin objeto", "Presencia total"])
    + P("Sin ese combustible, tu sol interior se vuelve enana blanca: funciona, pero sin brillo; existe, pero sin radiancia. "
        "Le pasa a cualquiera, y vuelve a encenderse.")

    + H3("Los Helióstatos del Alma")
    + P("Un helióstato es un espejo que sigue al sol y lleva su luz adonde no llegaba. En 1913, en Rjukan, un pueblo noruego que "
        "pasa casi medio año a la sombra de sus montañas, un tenedor de libros llamado Oscar Kittelsen propuso poner espejos en "
        "la cima para bajar el sol a la plaza. No había con qué hacerlo. En 2013, el artista Martin Andersen lo hizo realidad: "
        "tres espejos movidos por computadora siguen al sol de invierno y lo llevan al pueblo.")
    + P("Tus prácticas son helióstatos:")
    + lista(["La meditación", "La oración", "La intención clara", "El servicio"])
    + P("No fabrican luz: la llevan adonde hacía falta.")

    + H3("Fotosíntesis Espiritual")
    + P("Las plantas convierten la luz del sol en sustancia. Tú haces algo parecido con tu sol interior:")
    + lista(["Conviertes lo que ves en comprensión", "Transformas lo vivido en sabiduría",
             "Metabolizas la belleza", "Haces de la experiencia algo que se puede dar"])
    + P("La luz no te alimenta: te despierta. La de la mañana pone en hora tu reloj, y la que encuentras en los otros te devuelve "
        "las ganas. La luz no reemplaza la mesa: la ilumina.")

    + H3("El Eclipse del Sol Interior")
    + P("A veces, algo eclipsa tu sol interior:")
    + lista(["El ego inflado", "El miedo denso", "La tristeza honda", "Una herida que se congeló"])
    + P("Durante estos eclipses, recuerda: tu sol sigue ardiendo detrás de la sombra. El eclipse es temporal. La luz es eterna.")
    + P("Mientras tanto, la sombra se acompaña. Cuando la tristeza dura semanas, se consulta. Ninguna forma de sufrir es falta de "
        "quien la vive.")

    + H3("Cómo se Siente")
    + P("Cuando tu sol interior se deja ver:")
    + lista(["Calor en el pecho o en el vientre, sin causa externa", "Ganas de dar más que de recibir",
             "Una alegría que se nota en la cara", "Más energía para lo que importa",
             "La sensación de llevar un fuego encendido adentro"])
    + P("Si dormir deja de hacer falta, si la luz lastima los ojos o aparecen destellos, no es el sol: es el cuerpo, y pide un "
        "médico, no una interpretación.")

    + H3("La Red de Soles")
    + P("Tu sol interior no está solo. Las galaxias se ordenan en una red de filamentos de gas, y en 2020 un astrofísico y un "
        "neurocirujano, Franco Vazza y Alberto Feletti, compararon esa red con la de las neuronas del cerebro y encontraron "
        "parecidos de estructura que no esperaban. Como imagen, cuesta olvidarla.")
    + P("Cuando tu sol brilla, enciende otros. En 2010, James Fowler y Nicholas Christakis vieron que la generosidad entre "
        "desconocidos seguía viajando hasta tres pasos de distancia de quien la había empezado.")
    + P("Esta es la verdadera sangha: la comunidad de soles despiertos.")

    + H3("Para Habitar el Sol Interior")
    + fase("Para encender tu sol interior", ["Encuentra tu centro", "Imagina un punto de fusión",
                                             "Aliméntalo con atención sostenida", "Deja que se encienda solo"])
    + fase("Para regular tu radiación", ["Respira desde el centro", "Expande con la exhalación",
                                          "Recógete con la inhalación", "Encuentra tu ritmo"])
    + fase("Para dirigir tu luz", ["Mira dónde hace falta", "Ten intención sin tensión",
                                    "Deja que la luz pase", "Confía en lo que no controlas"])

    + H3("El Destino Solar")
    + P("Cada estrella tiene su final:")
    + lista(["Algunas se vuelven gigantes rojas de compasión", "Otras, enanas blancas de sabiduría concentrada",
             "Algunas, estrellas de neutrones de fuerza comprimida", "Unas pocas, agujeros negros de misterio infinito"])
    + P("Ninguna estrella lo elige: lo decide su masa. Lo que sí está en tus manos es cómo brillas mientras tanto.")
    + P("¿Cómo brilla hoy tu sol interior?")

    + H3("La Supernova Personal")
    + P("Las estrellas grandes terminan en supernova, y en esa explosión siembran el espacio con los elementos que un día serán "
        "planetas, sangre y huesos. Lo que muere así no se pierde: se reparte.")
    + P("En una vida también llegan momentos en que algo viejo tiene que terminar para que lo nuevo nazca:")
    + lista(["La muerte de un viejo sol", "El nacimiento de una estrella nueva",
             "La siembra de lo aprendido", "Ondas que llegan lejos"])
    + P("Ninguna supernova se apura. Las decisiones grandes, las que no se deshacen, piden las dos voces, la del cuerpo y la de la "
        "razón, con tiempo y con alguien de confianza.")

    + H3("Práctica: Encendiendo el Sol Interior")
    + practica(
        "Siéntate con la columna erguida.\nLleva tu atención al plexo solar.\nImagina un punto de luz del tamaño de un átomo.\n"
        "Este punto tiene la densidad de mil soles.",
        "Con cada respiración, permite que crezca.\nNo lo fuerces: los soles no se fuerzan.\nSolo haz espacio para que se expanda.",
        "Siente el calor sin temperatura.\nVe la luz sin fotones.\nConoce la fusión sin reacción.",
        "Eres el sol.\nEl sol eres tú.\nNo hay diferencia.",
        "Irradia.")

    + H3("El Secreto Solar Final")
    + verso("Tu sol interior no está EN ti.", "Tú estás EN tu sol interior.",
            "Eres una prominencia solar de tu propia estrella.", "Una llamarada de consciencia de tu propio fuego central.")
    + verso("Cuando comprendes esto, todo cambia.", "No tienes que encender tu sol.",
            "Solo tienes que recordar que eres una expresión de su luz.")
    + verso("Siempre lo has sido.", "Siempre lo serás.")

    + cita("“En el corazón de cada ser humano arde un sol. La única diferencia entre los dormidos y los despiertos es que los "
           "despiertos lo saben.”")
    + puerta("El 12 de abril de 1955, el día en que se anunció que la vacuna contra la poliomielitis funcionaba, un periodista "
             "le preguntó en televisión a Jonas Salk quién tenía la patente. Salk respondió que la gente, y preguntó a su vez si "
             "acaso se podía patentar el sol. Esa escena está en <em>Lo que se recibe</em>, Libro 38 del Portal Público, "
             "Umbral IV: «Lo que circula».",
             URL_PORTAL + "38_Lo_Que_Se_Recibe/umbral-04.html")
)


# ===========================================================================
# NODO 4 · El Cuerpo de Plasma
# ===========================================================================
NODO4 = (
    H2("La Anatomía Plasmática")
    + P("Las tradiciones hablan de cuerpos sutiles: el etérico, el astral, el cuerpo de luz. Tu cuerpo de plasma es otra manera "
        "de nombrar la luz y la electricidad que tu cuerpo ya es. No está más allá de tu cuerpo físico. Está en él.")
    + P("Y esa electricidad se mide. En 1791, Luigi Galvani vio moverse las patas de una rana al tocarlas con metales y habló de "
        "electricidad animal. En 1903, Willem Einthoven registró con precisión la señal eléctrica del corazón, la misma que hoy "
        "dibuja cualquier electrocardiograma. En 1924, Hans Berger leyó los ritmos eléctricos del cerebro. Y en 1952, Alan "
        "Hodgkin y Andrew Huxley mostraron que cada impulso nervioso es una ola de iones, átomos con carga, que entran y salen "
        "de la neurona.")
    + P("Tu cuerpo ya es eléctrico. El cuerpo de plasma es la imagen de esa luz.")

    + H3("Los Siete Centros")
    + P("Así lo dibuja el mapa de los chakras, de la raíz a la coronilla:")
    + fase("1. Raíz · rojo profundo", ["Arraigo en la realidad física", "Supervivencia", "Conexión con la tierra"])
    + fase("2. Sacro · naranja", ["Creatividad", "Sexualidad", "Fluidez"])
    + fase("3. Plexo solar · amarillo", ["Fuerza personal", "Voluntad", "Centro de fusión"])
    + fase("4. Corazón · verde", ["Amor", "Vínculo", "Puente entre lo denso y lo sutil"])
    + fase("5. Garganta · azul", ["Comunicación", "Decir la verdad", "Creación por el sonido"])
    + fase("6. Frente · índigo", ["Visión", "Intuición", "Mirada de conjunto"])
    + fase("7. Coronilla · violeta y blanco", ["Conexión con lo cósmico", "Consciencia amplia", "Apertura"])
    + P("No son siete cuerpos: son siete lugares donde el mismo fuego se reconoce.")

    + H3("La Fisiología del Plasma")
    + P("Tu cuerpo eléctrico tiene su propia fisiología:")
    + fase("Lo que circula", ["Iones que entran y salen de cada célula",
                              "Un corazón que se enciende eléctricamente en cada latido",
                              "Un intercambio constante con el ambiente: calor, aire, luz"])
    + fase("Lo que transmite", ["Una red de neuronas que se encienden en cadena",
                                "Impulsos que viajan como olas de iones",
                                "Una memoria repartida: durante décadas, Karl Lashley buscó en el cerebro el sitio exacto de un recuerdo y no lo halló (1950)"])
    + fase("Lo que respira", ["El aire que entra y enciende la combustión lenta",
                              "El aire que sale llevándose lo gastado", "La pausa entre los dos"])

    + H3("La Nutrición del Cuerpo de Plasma")
    + P("No solo de pan vive el ser humano, dice el Evangelio. Tu cuerpo de plasma también se nutre de:")
    + lista(["La luz del día", "La naturaleza", "Las emociones que ensanchan: amor, gratitud, asombro",
             "La presencia: meditación, contemplación", "El encuentro con otros"])
    + P("Cuando falta ese alimento, aparecen:")
    + lista(["Cansancio", "Desconexión", "Pérdida de sentido", "Una percepción más apagada"])
    + P("Y cuando el cansancio no cede o la tristeza dura semanas, se consulta.")

    + H3("Despertando el Cuerpo de Plasma")
    + fase("Fase 1: Reconocimiento", ["Acepta que ya tienes un cuerpo de luz", "Está funcionando ahora mismo",
                                       "Tu atención lo vuelve consciente"])
    + fase("Fase 2: Sensibilización", ["Siente el hormigueo en tu piel", "Nota el calor sin fiebre",
                                        "Percibe el peso del cuerpo en lo que lo sostiene", "Escucha el silencio de adentro"])
    + P("Sentir el cuerpo desde adentro tiene nombre: interocepción, el sentido que mira hacia adentro.")
    + fase("Fase 3: Movimiento", ["Lleva la atención por todo el cuerpo", "Expándela y recógela",
                                  "Siente cómo fluye", "Dale formas con la imaginación"])
    + fase("Fase 4: Integración", ["Sostén la calma", "Establece ritmos que puedas mantener",
                                   "Habítalo en lo cotidiano"])

    + H3("Lo Que Permite un Cuerpo Habitado")
    + P("Un cuerpo de plasma despierto permite:")
    + lista(["<strong>Presencia:</strong> estar del todo donde estás, con una atención que abarca el cuerpo, el cuarto y el horizonte",
             "<strong>Cercanía:</strong> sentir el ánimo de quien está al lado, sin pensar por él",
             "<strong>Cuidado:</strong> acompañar con tu calma a quien sufre, sin reemplazar ningún tratamiento",
             "<strong>Creación:</strong> dar forma a lo que imaginas, con las manos y con el tiempo",
             "<strong>Sueño:</strong> soñar con viveza, y a veces darte cuenta de que sueñas",
             "<strong>Anticipación:</strong> imaginar lo que viene con lo que recuerdas",
             "<strong>Transformación:</strong> convertir lo denso en comprensión"])

    + H3("Los Mudras Plasmáticos")
    + P("Los mudras son gestos de las manos que las tradiciones de la India usan para orientar la atención. Aquí van como gestos "
        "simples, sin promesa de efecto:")
    + fase("Mudra del Sol Interior · manos sobre el plexo solar, pulgares tocándose",
           ["Recoge la atención en el centro", "Da calor", "Te devuelve a ti"])
    + fase("Mudra del Infinito · las manos dibujan un ocho horizontal frente al corazón",
           ["Une lo que parecía separado", "Equilibra", "Invita a un ritmo que no se corta"])
    + fase("Mudra de la Corona · dedos entrelazados sobre la cabeza",
           ["Abre la mirada hacia arriba", "Recuerda la inmensidad"])
    + fase("Mudra del Enraizamiento · palmas hacia la tierra",
           ["Ancla en el cuerpo", "Devuelve al suelo", "Aquieta"])

    + H3("Cómo se Siente el Despertar")
    + fase("Al comienzo", ["Un hormigueo suave", "Calor sin fiebre", "Chispas de luz con los ojos cerrados",
                           "La sensación de un cuerpo más amplio"])
    + fase("Con la práctica", ["La percepción de tu propio campo", "Más sensibilidad al ánimo de los otros",
                               "Sueños vívidos", "Una calma que se nota"])
    + P("Si el hormigueo no se va, o llega con entumecimiento, debilidad o mareo, eso no es el despertar: pide un médico, "
        "no una interpretación.")

    + H3("El Cuidado del Cuerpo de Plasma")
    + fase("Cada día", ["Una ducha imaginando luz dorada al despertar", "Soltar las tensiones antes de dormir",
                        "Revisar qué te dejó enganchado"])
    + fase("Cada semana", ["Sol en la piel, con cuidado", "Naturaleza", "Un rato con árboles"])
    + P("Los árboles no son un adorno. A comienzos de los años ochenta, Roger Ulrich revisó las historias clínicas de un hospital "
        "de Pensilvania: los operados que veían árboles desde la cama se recuperaron antes que los que veían una pared de ladrillo.")
    + fase("Cada mes", ["Un ayuno de información", "Un día en silencio", "Volver a empezar"])
    + fase("Cada año", ["Un viaje a un lugar que te importe", "Un rito propio",
                        "Un cierre simbólico: despedir algo, empezar algo"])

    + H3("La Sexualidad Plasmática")
    + P("Cuando dos cuerpos se encuentran en la intimidad:")
    + lista(["Aparece un tercero, lo que ninguno traía por separado", "Se intercambian calor y confianza",
             "Las identidades se aflojan un momento", "Algo nuevo nace entre los dos", "Despierta lo que dormía"])
    + P("La intimidad que ilumina pide deseo de los dos, cuidado y libertad para decir que no. Así va más allá del placer: "
        "es creación compartida.")

    + H3("Heridas y Cuidado del Cuerpo de Plasma")
    + P("Tu cuerpo de plasma puede herirse con:")
    + lista(["Traumas emocionales hondos", "Vínculos que vacían", "Ambientes que no dejan descansar",
             "Límites cruzados una y otra vez", "La sensación de estar partido"])
    + P("Señales de que algo pide cuidado:")
    + lista(["Un cansancio constante", "Dificultad para decir que no", "La sensación de estar fragmentado",
             "Pérdida del brillo", "Desconexión"])
    + P("Lo que repara:")
    + lista(["Descanso", "Vínculos que cuidan", "Un no dicho a tiempo", "Naturaleza",
             "Volver a lo que te da sentido"])
    + P("Cuando alguien cruza tu límite una y otra vez, se dice en voz alta, se pone distancia y, si hace falta, se pide ayuda. "
        "Y cuando alguien te daña, lo sabio no es aguantar, sino alejarse y pedir ayuda.")

    + H3("El Cuerpo Plasmático Colectivo")
    + P("No solo tienes un cuerpo de plasma propio. Participas de cuerpos mayores:")
    + lista(["La familia", "Los amigos", "El barrio", "El país", "El planeta"])
    + P("Tu calma no cambia el mundo de golpe, pero viaja: quien encuentra un poco de calma se vuelve señal para otros.")
    + verso("Tu cuidado alcanza a otros.", "Tu calma se contagia.", "Nadie se enciende solo.")

    + H3("La Muerte del Cuerpo de Plasma")
    + P("Muchas tradiciones dicen que, al morir, algo luminoso se separa del cuerpo y sigue su camino: hacia otra vida, hacia la "
        "luz clara, hacia lo cósmico. Lo que cualquiera puede comprobar es que quien se fue sigue viviendo en nosotros.")

    + H3("Ejercicio: Despertar del Cuerpo de Plasma")
    + practica(
        "De pie, con los brazos abiertos como una estrella.\nImagina tu cuerpo volviéndose transparente.\n"
        "Observa la estructura de luz que permanece.",
        "Respira luz dorada por la coronilla.\nDéjala bajar, encendiendo cada centro:",
        ["Coronilla: violeta y blanco", "Frente: índigo", "Garganta: azul", "Corazón: verde",
         "Plexo: amarillo", "Sacro: naranja", "Raíz: rojo"],
        "Siente todos los centros encendidos a la vez.\nTu cuerpo entero, encendido desde adentro.",
        "Quédate así unas respiraciones lentas. Si los brazos se cansan, bájalos.\n"
        "Luego deja que la luz se asiente en tu forma de siempre, y siente los pies en el suelo.")

    + H3("La Evolución del Cuerpo de Plasma")
    + P("Tu cuerpo de plasma no es estático. Evoluciona:")
    + lista(["De inconsciente a consciente", "De caótico a coherente",
             "De aislado a tejido con otros", "De prestado a habitado"])
    + verso("Cada experiencia lo afina.", "Cada elección lo fortalece o lo debilita.",
            "Cada amor lo expande.", "Cada miedo lo contrae.")

    + H3("Lo Que Este Cuerpo Es")
    + P("Las tradiciones soñaron un cuerpo de luz. Pablo escribió que se siembra un cuerpo natural y resucita un cuerpo espiritual. "
        "El budismo tibetano habla del cuerpo de arcoíris de los grandes maestros. Son relatos de la tradición.")
    + P("Lo que cualquiera puede vivir está más cerca. En <em>El Retorno a Casa</em>, el último libro de Trinity Origen, está dicho "
        "así: «La transcendencia real no es ir más allá del cuerpo sino traer lo transcendente AL cuerpo».")
    + verso("Ya lo tienes.", "Solo necesitas habitarlo.")

    + cita("“Tu campo y tu cuerpo son uno. La luz no está en otra parte: es la manera en que este cuerpo se sabe vivo.”")
    + puerta("En <em>El cielo sobre Berlín</em>, de Wim Wenders, un ángel que lo sabe todo se cansa de flotar por encima de las "
             "cosas y elige tener un cuerpo: tomar un café en una mañana fría, frotarse las manos, ver los colores por primera "
             "vez. Esa escena, con la Novena Elegía de Rilke, está en <em>El Cuerpo</em>, Libro 4 de Arquitectura del Destino, "
             "Umbral VI: «Lo que solo un cuerpo puede».",
             URL_ARQ + "libro-04-el-cuerpo/L04-U6.html", "arquitectura")
)


# ===========================================================================
# NODO 5 · Comunicación Plasmática
# ===========================================================================
NODO5 = (
    H2("El Lenguaje Antes del Lenguaje")
    + P("Antes de las palabras, antes de los símbolos, antes incluso del pensamiento, existe la comunicación de estado a estado, "
        "de cuerpo a cuerpo, de presencia a presencia. Es el lenguaje original: el que hablamos antes de saber hablar.")
    + P("Hacia 1970, en el Instituto Tecnológico de Massachusetts, la antropóloga Mary Catherine Bateson analizó cuadro por "
        "cuadro películas de una madre con su bebé de pocas semanas, y encontró un diálogo. No había palabras, pero había turnos: "
        "la madre decía algo y esperaba; la criatura respondía con un sonido o un gesto. Lo llamó protoconversación, la "
        "conversación de antes de la conversación.")
    + P("Has vivido este lenguaje sin saberlo:")
    + lista(["Cuando sentiste el ánimo de una habitación al entrar",
             "Cuando tu perro leyó en tu cara lo que todavía no habías dicho",
             "Cuando el silencio entre dos amantes dijo más que mil palabras",
             "Cuando una mirada transmitió universos enteros",
             "Cuando un bebé te sonrió y le respondiste sin pensarlo"])

    + H3("Los Principios de la Transmisión Plasmática")
    + P("<strong>Principio 1: Resonancia directa.</strong> El estado es el mensaje. Cuando estás en dolor, el dolor se nota; "
        "cuando estás en calma, la calma se contagia. Tu cara, tu voz, tu manera de estar hablan antes que tus palabras. "
        "No transmites pensamientos: transmites presencia, quieras o no.")
    + P("<strong>Principio 2: La cercanía.</strong> Este lenguaje necesita presencia. El cuerpo lo habla con quien tiene delante, "
        "y por eso lo más asombroso no ocurre a distancia: ocurre a medio metro. No hace falta la distancia para el milagro: "
        "basta la cercanía.")
    + P("<strong>Principio 3: Muchas capas.</strong> Una palabra dicha lleva más que su sentido:")
    + lista(["Lo que dice", "El tono con que se dice", "La cara de quien la dice",
             "La historia entre los dos", "El silencio que la rodea"])
    + P("<strong>Principio 4: Coherencia.</strong> Solo un estado claro se transmite con claridad. El caos interior hace ruido; "
        "la claridad interior le da claridad al mensaje.")

    + H3("Las Maneras de Comunicar")
    + P("No son niveles: son maneras, y todas conviven.")
    + fase("Emanación sin querer", ["Transmites aunque no lo sepas", "Tu estado afecta lo que te rodea",
                                     "Los otros lo reciben sin darse cuenta"])
    + fase("Percepción", ["Empiezas a notar lo que otros transmiten", "Distingues tu ánimo del ajeno",
                          "Ves cómo los estados se afectan", "Aprendes a cuidarte"])
    + fase("Expresión", ["Transmites a propósito, con el cuerpo y la voz", "Modulas tu estado para decir algo",
                         "Creas un clima"])
    + fase("Diálogo", ["Ida y vuelta fluida", "Conversaciones sin palabras", "Comprensión mutua",
                       "Un campo compartido"])
    + fase("Comunión", ["Con muchos a la vez, como en un coro", "Con lo que no habla: plantas, animales, paisajes"])

    + H3("La Gramática del Plasma")
    + P("El plasma tiene su propia gramática:")
    + lista(["Sustantivos: estados que se asentaron", "Verbos: flujos y transformaciones",
             "Adjetivos: cualidades", "Conjugaciones: estados que se funden",
             "Puntuación: pausas y silencios cargados"])
    + P("Una oración sin palabras puede decir: estoy en paz, voy hacia ti, me abro, y te dejo lugar para responder.")

    + H3("Técnicas de Transmisión Plasmática")
    + fase("La Transmisión Láser", ["Concentra tu atención en una persona, la que tienes delante",
                                     "Ten clara tu intención", "Mírala", "Deja que tu estado hable",
                                     "Suelta el resultado"])
    + fase("La Transmisión Onda", ["Llega a un lugar con tu calma", "Deja que se extienda", "No la impongas",
                                    "Que la encuentre quien la necesite", "Sostenla"])
    + fase("La Transmisión del Vínculo", ["Recuerda a alguien que quieres",
                                           "Deja que ese recuerdo cambie tu manera de estar",
                                           "Nota cómo cambian tu cara y tu voz",
                                           "Y si quieres que lo sepa, díselo"])

    + H3("Recepción de Comunicaciones Plasmáticas")
    + P("Recibir es un arte más sutil que transmitir.")
    + fase("Preparación", ["Aquieta tu propio estado", "Haz lugar", "Suspende la interpretación",
                           "Deja que la impresión llegue", "Confía en la comprensión sin palabras"])
    + fase("Lo que puedes notar", ["Un cambio en tu ánimo", "Una comprensión que llega entera",
                                   "Sensaciones en el cuerpo", "Imágenes", "Una intuición"])
    + P("Una intuición se pregunta, no se impone: lo que sientes del otro se confirma hablando con él.")
    + P("Sentir el ánimo de un lugar, o adivinar a quien amas, es común y es bueno. Otra cosa es sentir que los pensamientos de "
        "otros entran en tu cabeza, que los tuyos se oyen afuera o que te llegan mensajes que nadie más escucha: eso no es un "
        "don para entrenar, y pide consulta esa misma semana.")
    + P("<strong>Decodificación.</strong> No traduzcas enseguida a palabras. Deja que lo recibido se asiente, se integre y revele "
        "su sentido a su tiempo.")

    + H3("Interferencias")
    + lista(["<strong>Ruido mental:</strong> los pensamientos que se atropellan",
             "<strong>Emociones densas:</strong> el miedo, la ira, los celos",
             "<strong>Expectativas:</strong> lo que esperas oír tapa lo que el otro dice",
             "<strong>Atención dividida:</strong> la pantalla que se interpone entre dos"])
    + fase("Para escuchar mejor", ["Meditación regular", "Tiempo en la naturaleza", "Ratos sin pantallas",
                                    "Descanso", "Preguntar antes de suponer"])

    + H3("El Traductor Universal Interior")
    + P("Hay en ti un traductor: convierte un gesto en comprensión y una comprensión en gesto. Puede:")
    + lista(["Leer en una cara lo que no se dice", "Poner en palabras lo que sientes",
             "Entender a quien vive distinto", "Tender puentes entre especies", "Escuchar lo que no habla"])
    + P("Los Hechos de los Apóstoles cuentan que en Pentecostés aparecieron lenguas como de fuego sobre cada uno de los reunidos, "
        "y que la multitud, venida de muchos pueblos, los oía hablar cada cual en su propia lengua. Es una imagen muy antigua del "
        "lenguaje que une: un fuego que traduce.")
    + P("Este traductor se afina con:")
    + lista(["El trato con gente distinta", "La práctica de escuchar", "La suspensión del juicio",
             "La apertura a lo desconocido", "El amor como tono de fondo"])

    + H3("Comunicación con lo Que No Habla")
    + fase("Con las plantas", ["Un ritmo lento y hondo",
                               "Bajo los bosques, los hongos unen las raíces de los árboles y llevan carbono de unos a otros (Simard y otros, 1997)",
                               "Responden a la luz, al agua, al cuidado"])
    + fase("Con los animales", ["Presentes y directos", "Transmiten necesidades y estados",
                                "Leen tu cuerpo mejor que tú mismo", "Responden a tu calma"])
    + P("En 2015, un equipo japonés encabezado por Miho Nagasawa midió que, cuando un perro y la persona con quien vive se miran "
        "a los ojos, la oxitocina sube en los dos.")
    + fase("Con las piedras", ["Pacientes, ordenadas", "Guardan memoria"])
    + P("Las rocas volcánicas guardan la dirección del campo magnético de la Tierra en el momento en que se enfriaron. En 1963, "
        "Fred Vine y Drummond Matthews leyeron en el fondo del mar franjas de roca que registraban sus inversiones, y así se "
        "entendió que los océanos se abren.")
    + fase("Con los elementos", ["Primordiales, salvajes", "Enseñan por experiencia directa",
                                 "Responden al respeto y a la rendición"])

    + H3("El Coro Plasmático Planetario")
    + P("En cada momento, todos los seres de la Tierra transmiten algo: una sinfonía de estados, emociones, pensamientos e "
        "intenciones.")
    + P("Tu parte importa:")
    + lista(["Cada gesto de amor eleva el coro", "Cada momento de paz lo armoniza",
             "Cada pulso de alegría le añade luz", "Cada instante de presencia lo aclara"])
    + verso("No eres solo receptor.", "Eres transmisor.", "Eres el mensaje mismo.")

    + H3("Antes de una Conversación Difícil")
    + P("Para los momentos en que lo que hay que decir pesa:")
    + pasos(["<strong>ALTO:</strong> detén la carrera de los pensamientos",
             "<strong>CENTRA:</strong> vuelve a tu sol interior, al pecho, a los pies",
             "<strong>RESPIRA:</strong> tres respiraciones lentas",
             "<strong>DI:</strong> con palabras simples, lo que sientes y lo que necesitas",
             "<strong>SUELTA:</strong> no controles cómo lo recibe el otro",
             "<strong>ESCUCHA:</strong> haz lugar a su respuesta"])
    + P("Y en una emergencia, se llama: con la voz y con el teléfono. La red empieza en un hilo.")

    + H3("Ejercicio: Estableciendo Comunicación Plasmática")
    + practica(
        "Con un compañero dispuesto:",
        "Siéntense enfrentados, con los ojos cerrados.\nRespiren juntos hasta acompasarse.\nSientan la presencia del otro.",
        "Quien emite elige un estado simple: paz, alegría, ternura.\nLo cultiva hasta ser ESE estado.\nSin esfuerzo, deja que se note.",
        "Quien recibe se vacía de expectativas.\nSe vuelve receptivo como agua quieta.\nNota qué surge sin buscarlo.",
        "Intercambien los roles.",
        "Al final, abran los ojos y cuéntense con palabras qué notaron. A veces coincide y a veces no, y las dos cosas enseñan. "
        "Lo que crece entre ustedes no depende de acertar: depende de estar.")

    + H3("El Futuro de la Comunicación Humana")
    + P("Los bebés nacen sabiendo este lenguaje. En 1975, Edward Tronick filmó a madres que jugaban con sus bebés de pocos meses "
        "y, de pronto, dejaban la cara quieta, sin expresión. Los bebés lo notaban enseguida: intentaban recuperar el juego, se "
        "inquietaban, y volvían a calmarse cuando la cara de la madre respondía.")
    + P("No lo perdemos al crecer. Debajo de cada conversación hay otra, hecha de caras, pausas y tonos, y sigue funcionando. "
        "El futuro de la comunicación humana no está en dejar las palabras, sino en volver a mirar mientras las decimos.")
    + verso("Lo que no habla también dice.", "Y en ese decir, la comunión.")

    + cita("“Cuando dos plasmas coherentes se encuentran, no necesitan hablar. La comunión es instantánea, total, inolvidable.”")
    + puerta("Un cuarto de siglo después de la protoconversación, en Edimburgo, un musicólogo escuchó la grabación de una niña de "
             "seis semanas con su madre y se sorprendió marcando el compás con el pie: había pulso, tono y relato. Esa música de "
             "antes de las palabras está en <em>El cuerpo</em>, Libro 34 del Portal Público, Umbral I: «Antes de la palabra».",
             URL_PORTAL + "34_El_Cuerpo/umbral-01.html")
)


# ===========================================================================
# NODO 6 · Portales de Plasma
# ===========================================================================
NODO6 = (
    H2("Las Puertas Entre Mundos")
    + P("En 2012, la NASA anunció que había portales de plasma alrededor de la Tierra. Jack Scudder, físico de la Universidad de "
        "Iowa, los llamó puntos X: lugares donde el campo magnético de la Tierra se une con el del Sol y abre un camino sin cortes "
        "entre los dos. Se abren y se cierran sin aviso, decenas de veces por día, y por ellos entran partículas que encienden las "
        "auroras de los polos.")
    + P("Un portal así no lleva a otro mundo: une dos campos, y lo que pasa por él se vuelve luz.")
    + P("Cada vez que tu vida cambió en un instante, cruzaste uno. La física llama a eso salto cuántico, y guarda una sorpresa: "
        "un salto cuántico es el cambio más pequeño que existe, no el más grande. En 2019, en Yale, el equipo de Zlatko Minev "
        "mostró que esos saltos pueden verse venir, y hasta detenerse y revertirse a mitad de camino. Los cambios hondos suelen "
        "ser así: pequeños, con aviso, y todavía reversibles mientras ocurren.")
    + P("Los portales están en todas partes:")
    + lista(["En el ojo de cada tormenta", "En el momento entre la vigilia y el sueño", "En el clímax del éxtasis",
             "En el punto cero de la meditación", "En el último aliento", "En el primer llanto"])
    + P("Solo necesitas ojos despiertos para verlos. <em>El Portal Infinito</em>, el quinto libro de esta serie, los llamó umbrales.")

    + H3("Anatomía de un Portal")
    + P("Todo portal, como imagen, tiene:")
    + lista(["<strong>El horizonte:</strong> el punto donde lo de siempre empieza a curvarse",
             "<strong>El remolino:</strong> lo que gira mientras pasas",
             "<strong>El pasaje:</strong> el tiempo del medio, ni aquí ni allá",
             "<strong>El centro:</strong> donde todo parece posible",
             "<strong>La salida:</strong> la apertura hacia lo nuevo",
             "<strong>El sostén:</strong> lo que mantiene el paso estable"])

    + H3("Tipos de Portales")
    + fase("Lugares", ["Montañas, manantiales y cuevas que muchas tradiciones cuidaron como umbrales",
                       "Templos y santuarios", "Un rincón de tu casa donde te recoges"])
    + fase("Momentos", ["Las crisis", "Las experiencias cumbre", "Los nacimientos y las muertes",
                        "Los sueños lúcidos", "Las coincidencias que te detienen"])
    + fase("Prácticas", ["La meditación en grupo", "Las ceremonias de cada tradición", "La música",
                         "El silencio compartido"])
    + fase("Personales", ["Tu propia presencia", "Una intención sostenida", "La práctica constante",
                          "Tu sol interior"])

    + H3("La Física de los Portales de Plasma")
    + P("En el espacio, los portales se forman por reconexión magnética: dos campos se cruzan, se rompen y vuelven a unirse de "
        "otra manera, y en ese gesto liberan energía. Para estudiarlos de cerca, la NASA lanzó en 2015 cuatro naves que vuelan "
        "en formación alrededor de la Tierra.")
    + P("Dicho con una vida:")
    + lista(["Dos mundos que se tocan: dos personas, dos ideas, dos tiempos", "Un cruce: algo se rompe",
             "Una nueva unión: algo se ordena distinto", "Una liberación: la energía que estaba atrapada",
             "Luz: lo que se ve después"])

    + H3("Reconociendo un Portal")
    + fase("En el cuerpo", ["Un silencio distinto", "Cambios de temperatura en la piel",
                            "La sensación de estar en un borde", "Un asombro sin causa"])
    + fase("En la mente", ["El tiempo que se estira o se acelera", "Pensamientos que no siguen la línea de siempre",
                           "Recuerdos que vuelven con otra luz", "Una comprensión que llega de golpe"])
    + P("Otra cosa es que el mundo parezca irreal, que pierdas horas sin recuerdo o que te sientas fuera de ti: eso no es un "
        "portal, y pide consulta esa misma semana.")

    + H3("Navegando un Portal")
    + fase("Preparación", ["Serena tu estado", "Aclara tu intención", "Suelta lo que no hace falta",
                           "Confía en el proceso", "Mantén la calma pase lo que pase"])
    + fase("Entrada", ["Deja que el cambio te lleve", "No resistas lo que se afloja",
                       "Mantén la consciencia testigo", "Ríndete al flujo"])
    + fase("Tránsito", ["No intentes controlar", "Observa sin aferrarte", "Permite que algo se reordene",
                        "Confía en tu esencia", "Recuerda tu intención"])
    + fase("Salida", ["Vuelve de a poco", "No fuerces la comprensión inmediata", "Guarda lo nuevo",
                      "Intégralo", "Cierra la puerta detrás de ti"])

    + H3("La Puerta de Todos los Días")
    + P("No hace falta girar hasta marearse ni comprimirse hasta estallar. El portal más cercano es la puerta de tu casa. En 2011, "
        "Gabriel Radvansky y su equipo, en la Universidad de Notre Dame, encontraron que cruzar una puerta hace olvidar más que "
        "recorrer la misma distancia dentro de una habitación: para la mente, el umbral cierra un episodio y abre otro. Por eso, "
        "a veces, llegas a la cocina y no recuerdas a qué ibas.")
    + P("Si cruzar una puerta ya cambia la mente, cruzarla despierto puede cambiar el día.")
    + practica(
        "Elige una puerta que cruces muchas veces.",
        "Antes de pasar, detente una respiración en el umbral.\nPregúntate qué dejas atrás y qué llevas contigo.\n"
        "Cruza despacio.\nDel otro lado, mira el lugar como si llegaras por primera vez.",
        "Hazlo durante una semana. Las puertas de tu casa se volverán umbrales.")

    + H3("Los Guardianes del Umbral")
    + P("En los mitos, cada umbral tiene su guardián. Joseph Campbell lo describió en 1949: el héroe, al dejar el mundo conocido, "
        "encuentra en la puerta una figura que pone a prueba su preparación. Los pueblos nórdicos contaban que Heimdal vigilaba "
        "el puente del arcoíris que lleva a los dioses.")
    + P("Los guardianes de tus umbrales son más cercanos:")
    + lista(["El miedo", "La vergüenza", "La duda", "Las pruebas de preparación", "Los espejos de tu sombra"])
    + P("Para pasar:")
    + lista(["Muestra respeto genuino", "Declara una intención clara", "Mantén la calma",
             "Acepta la prueba", "Agradece el paso"])

    + H3("Los Portales del Tiempo")
    + P("La memoria es la máquina del tiempo que sí existe.")
    + fase("Hacia el pasado", ["Para mirar lo vivido desde hoy", "Para encontrar lo que faltó",
                               "Para recibir la sabiduría de los que vinieron antes", "Para cerrar lo que quedó abierto"])
    + P("Al recordar, el pasado no cambia: cambia su sentido. No cambies lo que pasó: pregúntate qué faltó. Las heridas hondas, "
        "las que al recordarlas se vuelven a vivir, no se visitan a solas: se recorren con un profesional.")
    + fase("Hacia el futuro", ["Para imaginar lo que puede venir", "Para escribirle a quien serás",
                               "Para ensayar un paso"])
    + P("Imaginar el futuro usa la misma memoria que recordar: las mismas redes del cerebro trabajan al evocar una escena vivida "
        "y al imaginar una por vivir (Schacter y Addis, 2007).")
    + fase("Hacia el eterno ahora", ["Donde cabe todo el tiempo", "La perspectiva del alma", "El punto de creación",
                                     "La fuente de lo nuevo", "El hogar verdadero"])

    + H3("No Toda Puerta Debe Cruzarse")
    + lista(["<strong>Las puertas del caos:</strong> llevan a una vida desordenada",
             "<strong>Las puertas que drenan:</strong> los lugares y los vínculos que te vacían",
             "<strong>Las puertas trampa:</strong> grupos que prometen poder rápido, piden sacrificios y te alejan de los tuyos",
             "<strong>Las puertas que repiten:</strong> los círculos de siempre",
             "<strong>Las puertas de la sombra:</strong> llevan a tus miedos"])
    + P("Señales de peligro:")
    + lista(["Prisa y presión para entrar", "Un miedo instintivo y hondo", "La pérdida de tu calma al acercarte",
             "Promesas de poder fácil", "Pedidos de sacrificio"])
    + P("Si oyes voces que nadie más oye, que te prometen poder o te piden un sacrificio, eso no es un guardián: pide consulta "
        "esa misma semana.")

    + H3("La Puerta Más Grande")
    + P("La muerte es el portal más natural y el más hondo. Muchas tradiciones dicen que disuelve los velos, que libera la luz del "
        "cuerpo, que en ella se revisa la vida entera y que algo sigue su camino. Lo que cualquiera puede comprobar es que quien se "
        "fue sigue viviendo en nosotros.")
    + P("François de La Rochefoucauld escribió que ni el sol ni la muerte se pueden mirar fijamente. Se miran a ratos, en "
        "compañía, y esos instantes ordenan lo importante. Mirarla de frente no es desearla, y si alguna vez se vuelve deseo de "
        "no estar, es momento de pedir ayuda, sin esperar.")
    + P("Mientras vives, cada final pequeño es un umbral donde ensayarla.")

    + H3("Portales Colectivos")
    + P("Cuando un grupo se reúne con el corazón puesto en lo mismo, algo se abre. En San Pedro Manrique, un pueblo de Soria, cada "
        "noche de San Juan algunos vecinos cruzan descalzos un lecho de brasas. En 2011, un equipo encabezado por Ivana "
        "Konvalinka midió sus corazones: el de los familiares y amigos subía y bajaba con el de quien cruzaba el fuego; el de "
        "los visitantes, no. Lo que acompasaba los latidos era lo que significaba, para cada uno, quién estaba cruzando.")
    + verso("Cada ceremonia es un intento de portal colectivo.", "Cada meditación compartida abre una puerta pequeña.",
            "Cada momento de unidad humana es un portal posible.")

    + H3("El Portal Interior Permanente")
    + P("El mayor secreto: no necesitas buscar portales externos. Tu sol interior ES un portal permanente. Tu calma ES el vórtice. "
        "Tu consciencia ES el puente.")
    + verso("Cada respiración puede ser un portal.", "Cada latido, una puerta.",
            "Cada momento, una oportunidad de salto cuántico.")

    + H3("Ejercicio: Abriendo Tu Portal Personal")
    + practica(
        "Siéntate con la espalda digna, sin rigidez.\nSiente tu sol interior en el centro del pecho.\n"
        "Deja que la respiración gire sola.",
        "Imagina lo que quieres atravesar:",
        ["Un estado de calma", "La versión de ti que deseas cultivar", "Un momento posible de tu futuro"],
        "Tiende un puente de luz hacia allí.\nNota cuándo se establece.",
        "No necesitas viajar.\nSolo permite que algo en ti se reordene.",
        "Cuando esté completo, lo sabrás.\nAgradece.\nIntegra.\nY vuelve: el regreso es la parte más importante.")

    + H3("La Red de Portales")
    + P("La Tierra está llena de umbrales: naturales y construidos, antiguos y nuevos, conocidos y ocultos. Los peregrinos de muchas "
        "tradiciones los recorrieron, y los niños los encuentran en cualquier pasillo.")
    + P("Tú eres parte de esa red. Tu presencia es un nodo. Cuando cruzas despierto, otros aprenden a cruzar.")

    + H3("El Próximo Portal")
    + verso("El próximo portal no está en el calendario.", "Es la próxima puerta que cruces despierto,",
            "la próxima conversación,", "el próximo final que sepas despedir.")
    + P("Tu preparación es tu presencia. Tu coherencia, tu manera de navegar. Tu amor, tu rumbo.")
    + P("El portal te espera. Siempre ha estado esperándote.")

    + cita("“Cada portal es una invitación a convertirte en quien realmente eres. El coraje para atravesarlo es el precio de la "
           "transformación.”")
    + puerta("Un nodo de Trinity Origen dice que el tabú más grande es también la puerta más grande. Una mujer que vacía casas "
             "de muertos, con una regla para no detenerse en ningún final, aprende a mirarlo en lo pequeño, como se mira el sol "
             "reflejado en el agua de un balde. Esa historia está en <em>Las Pequeñas Muertes</em>, Libro 6 de Arquitectura del "
             "Destino, Umbral I: «La última gota».",
             URL_ARQ + "libro-06-las-pequenas-muertes/L06-U1.html", "arquitectura")
)


# ===========================================================================
# NODO 7 · La Ascensión Ígnea
# ===========================================================================
NODO7 = (
    H2("El Fuego Que Eleva")
    + P("La ascensión no es flotar hacia las nubes. Es el fuego que sube por la vida entera y la vuelve luminosa: fuego viviente "
        "que arde sin consumirse, luz que camina en forma humana, estrella encarnada en la Tierra.")
    + P("Las tradiciones guardan relatos de ese fuego. El segundo libro de los Reyes cuenta que el profeta Elías subió al cielo en "
        "un torbellino, mientras un carro de fuego lo apartaba de su discípulo. Los Evangelios cuentan que, en un monte alto, el "
        "rostro de Jesús resplandeció como el sol, y los monjes hesicastas de Oriente, con Gregorio Palamás en el siglo XIV, "
        "enseñaron que esa luz del Tabor puede verse en la oración. Son relatos de la tradición, y todos apuntan al mismo lugar: "
        "la luz no tiene que dejar el cuerpo para encenderse.")
    + P("El fuego que eleva tiene un camino:")
    + lista(["Primero despiertas al fuego interior", "Luego aprendes a sostenerlo",
             "Después dejas que alumbre", "Finalmente, te vuelves el fuego mismo"])
    + P("No es escape de la materia. Es la materia volviéndose luz mientras mantiene su forma. Es el matrimonio entre espíritu y "
        "sustancia, la prueba viviente de que no hay separación.")

    + H3("Las Formas del Fuego")
    + P("No es una escalera: en una misma vida conviven las siete.")
    + fase("La Chispa · despertar", ["El primer contacto con tu fuego interior",
                                      "Momentos de luz que van y vienen", "La búsqueda del interruptor"])
    + fase("La Llama · práctica", ["Un fuego pequeño y constante", "La práctica diaria lo sostiene",
                                    "Otros notan tu brillo"])
    + fase("La Hoguera · soltar", ["El fuego consume lo que ya no sirve", "El ego empieza a aflojarse",
                                    "Puedes encender otros fuegos"])
    + fase("El Horno · transformar", ["Los alquimistas llamaban atanor a su horno: un fuego lento y parejo que no se dejaba apagar",
                                       "Lo que se transforma de verdad necesita tiempo", "La paciencia madura"])
    + fase("La Estrella · dar", ["Una gravedad propia", "Otros se acercan a tu calma",
                                  "Das sin agotarte. Thomas Jefferson lo escribió en 1813: quien enciende su vela en la mía recibe luz sin dejarme a oscuras"])
    + fase("La Supernova · sembrar", ["Lo viejo que estalla", "La siembra de lo aprendido",
                                       "La muerte del yo separado, como la nombran las tradiciones",
                                       "El nacimiento de algo más amplio"])
    + fase("El Agujero Blanco · emanar", ["La física imagina un agujero blanco, lo contrario de un agujero negro: algo de lo que solo sale luz y en lo que nada entra. Nadie lo vio nunca",
                                           "Una fuente que no se agota", "Más allá de toda medida", "El fuego puro"])

    + H3("Cómo se Siente el Fuego que Eleva")
    + fase("En el cuerpo", ["Calor interno", "Una electricidad suave en la piel", "Una vibración en la columna",
                            "Una ligereza nueva", "Ganas de cuidarte"])
    + fase("En el ánimo", ["Una alegría que sube", "Ganas de servir", "Amor que no pide nada", "Compasión", "Calma"])
    + fase("En la mirada", ["Una comprensión más amplia", "Menos miedo a lo que pasa",
                            "Un yo que se afloja sin perderse", "Una paz que se queda"])
    + P("Si el fuego trae noches sin sueño, pensamientos que corren, una misión urgente, mensajes de guías o la certeza de saber "
        "lo que va a pasar, no es el fuego que eleva: es el momento de pedir ayuda, esa misma semana. Stanislav y Christina Grof "
        "llamaron emergencia espiritual a las crisis que a veces acompañan un despertar, y enseñaron que se atraviesan acompañadas.")
    + P("Comer menos no es arder más: el cuerpo que sostiene el fuego necesita su pan. Y si alguna vez contemplar la muerte se "
        "vuelve deseo de no estar, es momento de pedir ayuda, sin esperar.")

    + H3("El Camino del Fuego")
    + fase("Fase 1: Preparar el cuerpo", ["Dormir, comer y moverse bien", "Fortalecer el sistema nervioso con calma y descanso",
                                          "Estabilizar las emociones", "Aclarar la mente"])
    + fase("Fase 2: Encender con cuidado", ["Prácticas suaves, cada día", "Un ritmo que puedas sostener",
                                            "Un lugar seguro, y alguien de confianza cerca", "Los pies en la tierra"])
    + fase("Fase 3: Crecer de a poco", ["Ampliar la práctica sin apuro", "Integrar cada paso antes del siguiente",
                                        "Seguir con tu vida de todos los días", "Servir mientras creces"])
    + fase("Fase 4: Rendirse", ["Soltar el control que sobra", "Confiar en la inteligencia del fuego",
                                "Dejar que el fuego guíe, sin dejar de mirar"])
    + fase("Fase 5: Transfigurar", ["Que lo ordinario se ilumine", "Que la vida diaria se vuelva el lugar de lo sagrado",
                                    "Que tu presencia se vuelva luz para otros"])
    + P("Ninguna etapa pide decisiones irreversibles: dejar de golpe un trabajo, una casa o un vínculo no es subir más rápido.")

    + H3("Lo Que Aviva el Fuego")
    + fase("Prácticas del sol", ["Mirar el amanecer", "Respirar despacio a la luz de la mañana",
                                 "Una pausa al mediodía", "Sol en la piel, con cuidado"])
    + fase("Prácticas del fuego", ["Mirar un fuego de verdad, en un fogón o una chimenea",
                                   "Respirar imaginando un calor que sube", "Cantar", "Bailar"])
    + fase("Prácticas del plasma", ["Sentir el cuerpo entero encendido", "Buscar la calma en el centro",
                                    "Hacerte conductor de la luz, no su dueño"])

    + H3("Los Obstáculos de la Ascensión")
    + fase("El Miedo a Arder", ["Un terror antiguo al fuego", "Miedo a perder la identidad", "Pánico a disolverse",
                                "Resistencia al cambio", "Apego a la forma conocida"])
    + fase("La Inflación Espiritual", ["El ego que se apropia del fuego", "Delirios de grandeza", "Pérdida de humildad",
                                       "Desconexión de la humanidad",
                                       "El atajo espiritual: John Welwood llamó así en 1984 a usar la práctica para saltear lo que duele"])
    + fase("La Precipitación", ["Forzar el camino", "Saltar etapas necesarias", "Descuidar el cuerpo",
                                "Buscar atajos peligrosos", "Competir en lo espiritual"])

    + H3("La Paradoja de la Ascensión Ígnea")
    + verso("No asciendes DESDE la Tierra. Asciendes CON la Tierra.", "No escapas de la materia. La materia se vuelve luz.",
            "No dejas tu humanidad. Tu humanidad se vuelve divina.", "No abandonas el mundo. El mundo asciende a través de ti.")
    + verso("Esta es la verdadera ascensión: no un escape sino una transfiguración.", "No una huida sino una fusión.",
            "No un abandono sino un abrazo ígneo de TODO.")

    + H3("Los Que Ardieron Antes")
    + P("Cada tradición guarda los nombres de quienes ardieron así:")
    + lista(["Elías y su carro de fuego",
             "Los inmortales del taoísmo, que según la leyenda refinaban su cuerpo hasta volverlo luz",
             "Babaji, el yogui que Paramahansa Yogananda describe en su autobiografía",
             "Serafín de Sarov, cuyo rostro brillaba en la nieve",
             "Los santos que el arte pintó con un sol detrás de la cabeza"])
    + P("Son relatos. No piden que los creas: muestran un deseo humano muy antiguo, el de que la luz no tenga que dejar el "
        "cuerpo. Dejaron el mapa.")

    + H3("El Servicio del Fuego")
    + P("Cuando tu fuego se asienta, tu servicio cambia:")
    + P("Ya no sirves HACIENDO. Sirves SIENDO.")
    + lista(["Tu presencia serena", "Tu calma enciende otras", "Tu cuidado acompaña sin forzar",
             "Tu amor enciende corazones", "Tu paz calma tormentas"])
    + P("Carl Rogers, uno de los psicólogos que más estudió cómo ayudar, escribió cerca de los ochenta años que en sus mejores "
        "momentos, cuando estaba más cerca de su propio centro, su sola presencia parecía liberar y ayudar al otro. No podía "
        "provocarlo: aparecía cuando podía relajarse y estar cerca de lo que ocurría.")
    + P("Te conviertes en un sol que camina, un faro, una antorcha en la oscuridad. No por elección. Por naturaleza. El fuego que "
        "se asentó no puede NO irradiar.")

    + H3("La Comunidad de Fuego")
    + P("Durante cientos de miles de años, los seres humanos se reunieron de noche alrededor del fuego. En 1974, la antropóloga "
        "Polly Wiessner registró las conversaciones de los ju/'hoansi del Kalahari: de día hablaban sobre todo de trabajo y de "
        "quejas, y menos de una conversación de cada diez era un relato; de noche, junto al fuego, ocho de cada diez lo eran, y "
        "las quejas casi se apagaban. Publicó el estudio en 2014.")
    + P("Alrededor del fuego aprendimos a contarnos. Los que arden se reconocen así:")
    + lista(["Por el calor que comparten", "Por la luz que no esconden", "Por las historias que se cuentan",
             "Por la paz que los reúne"])
    + P("Cuando se separan, siguen unidos por lo que se contaron.")

    + H3("La Tierra que Ya Brilla")
    + verso("No eres el único que arde.", "En cada barrio hay alguien que cuida un fuego.",
            "Algunos ya son antorchas,", "otros apenas chispas,", "y todos llevan el fuego.")
    + P("La Tierra no necesita volverse estrella: ya está hecha de una. El hierro de su centro, el calcio de sus montañas y el "
        "oxígeno del aire se forjaron en estrellas que vivieron antes que el Sol. No esperamos el fin del mundo ni un mundo de "
        "fuego. Esperamos algo más simple, y ya está ocurriendo: que cada uno encienda su parte.")

    + H3("Práctica Final: El Fuego que Sirve")
    + practica(
        "En un momento de quietud y disposición:",
        "Declara tu intención de arder.\nNo como escape sino como servicio.\nNo como logro sino como entrega.\n"
        "No como meta sino como camino.",
        "Imagina cada célula encendiéndose.\nCada átomo volviéndose sol.\nCada pensamiento volviéndose luz.\n"
        "Cada emoción volviéndose fuego sagrado.",
        "Siente tu columna como un pilar de luz.\nTu corazón, como un fuego que late.\nTu coronilla, como una estrella naciente.\n"
        "Tu cuerpo entero, encarnado y encendido.",
        "No fuerces. No resistas.\nEl fuego sabe qué hacer.\nSiempre lo ha sabido.",
        "Arde.\nAsciende.\nIrradia.\nSirve.",
        "Antes de abrir los ojos, siente los pies en el suelo.")
    + verso("Eres el fuego que el mundo espera.", "Eres la luz que la oscuridad necesita.", "Eres la estrella que guía el camino.")
    + verso("La ascensión ígnea no es tu destino futuro.", "Es tu naturaleza presente.",
            "Solo necesitas dejar de fingir que no estás ardiendo.")
    + verso("Deja de apagarte.", "Deja de esconder tu brillo.", "Deja de temer tu luz.")
    + verso("ARDE.")
    + verso("Y en tu ardor, que todos encuentren su fuego.", "En tu ascensión, que todos recuerden sus alas.",
            "En tu luz, que toda oscuridad se revele como luz no reconocida.")
    + verso("Este es el fin del Libro 8: Plasma Consciente.", "Pero es el principio de tu ascensión ígnea.")
    + verso("El fuego ha sido encendido.", "No puede ser apagado.", "Solo puede expandirse.")
    + verso("Hasta que todo sea luz.", "Hasta que todo sea fuego.", "Hasta que todo sea plasma consciente.")

    + H3("Siete Fuegos")
    + P("El <em>Fuego Frío Interior</em> alumbra sin quemar, y ya estaba.")
    + P("Los <em>Estados Plasmáticos</em> son tonos de una misma llama, y ninguno vale más que otro.")
    + P("El <em>Sol Interior</em> está hecho de estrellas, y su luz no se fuerza.")
    + P("El <em>Cuerpo de Plasma</em> arde despacio: la luz se habita aquí.")
    + P("La <em>Comunicación Plasmática</em> empezó antes de la palabra, con un cuerpo frente a otro.")
    + P("Los <em>Portales de Plasma</em> unen dos campos; el más cercano es la puerta de tu casa.")
    + P("La <em>Ascensión Ígnea</em> sube con la Tierra, no lejos de ella.")
    + P("<strong>No son siete escalones: son siete maneras de arder.</strong>")
    + P("Este es el octavo de los trece libros de Trinity Quantum, el primero después del centro de la serie.")
    + P("El próximo libro, <em>Simetrías Rotas</em>, mira lo que se rompe, y la grieta por donde puede entrar la luz.")

    + cita("“La ascensión ígnea no es el fin del viaje humano. Es el momento en que el viaje verdadero comienza.”")
    + puerta("En 1942, Simone Weil le escribió a un poeta que había quedado inmóvil en una cama por una herida de guerra que la "
             "atención es la forma más rara y más pura de la generosidad. Esa carta, junto a la cara quieta de una madre y a la "
             "presencia que sostiene sin dirigir, está en <em>La presencia</em>, Libro 30 del Portal Público, Umbral VI: "
             "«Estar sin intervenir».",
             URL_PORTAL + "30_La_Presencia/umbral-06.html")
)


# ===========================================================================
# REEMPLAZOS
# ===========================================================================
_DOCTYPE = "<!DOCTYPE html>\n"
_CON_PROCEDENCIA = "<!DOCTYPE html>\n" + PROCEDENCIA + "\n"
_CIERRE_HEAD = "</head>"

COMENTARIOS_NODO1 = (
    "\n  <!-- Si ya estás usando el CSS global, deja este link -->\n"
    '  <!-- <link rel="stylesheet" href="../assets/css/trinity-quantum.css" /> -->\n'
    "\n  <!-- Ropaje Trinity embebido (para que este nodo sea autónomo si lo necesitás) -->\n"
)

REEMPLAZOS = [
    (Q8 + "index.html", _DOCTYPE, _CON_PROCEDENCIA),
    (Q8 + "index.html", _CIERRE_HEAD, ESTILO_INDICE + _CIERRE_HEAD),
    (Q8 + "index.html", "DESDE:<body>", INDICE_CUERPO),
]

_CUERPOS = {1: NODO1, 2: NODO2, 3: NODO3, 4: NODO4, 5: NODO5, 6: NODO6, 7: NODO7}

for _n in range(1, 8):
    _arch = Q8 + f"nodo_0{_n}.html"
    REEMPLAZOS += [
        (_arch, _DOCTYPE, _CON_PROCEDENCIA),
        (_arch, _CIERRE_HEAD, ESTILO + _CIERRE_HEAD),
        (_arch, "DESDE:<body>", cuerpo_nodo(_n, _CUERPOS[_n])),
    ]

# Nodo 1: salen los comentarios de producción de la cabecera.
REEMPLAZOS.append((Q8 + "nodo_01.html", COMENTARIOS_NODO1, "\n"))

# Nodo 4: el título pasa al singular.
REEMPLAZOS.append((
    Q8 + "nodo_04.html",
    "<title>Trinity Quantum · Libro 8 · Nodo 4 — Cuerpos de Plasma</title>",
    "<title>Trinity Quantum · Libro 8 · Nodo 4 — El Cuerpo de Plasma</title>",
))


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    raiz = Path(sys.argv[1])
    textos = {}
    for archivo, viejo, nuevo in REEMPLAZOS:
        ruta = raiz / archivo
        if archivo not in textos:
            textos[archivo] = ruta.read_text(encoding="utf-8")
        t = textos[archivo]
        if viejo.startswith("DESDE:"):
            marca = viejo[len("DESDE:"):]
            n = t.count(marca)
            if n != 1:
                sys.exit(f"{archivo}: la marca aparece {n} veces: {marca!r}")
            t = t[: t.index(marca)] + nuevo
        else:
            n = t.count(viejo)
            if n != 1:
                sys.exit(f"{archivo}: el texto aparece {n} veces: {viejo[:70]!r}")
            t = t.replace(viejo, nuevo, 1)
        textos[archivo] = t
    for archivo, t in textos.items():
        (raiz / archivo).write_text(t, encoding="utf-8")
        print("escrito:", archivo)
    print(f"{len(REEMPLAZOS)} reemplazos, cada uno aplicado exactamente una vez.")


if __name__ == "__main__":
    main()
