#!/usr/bin/env python3
"""
Depuración de Quantum 12, *Singularidad Consciente* (2 de noviembre de 2026),
el octavo y último de la revisión completa de Quantum, con el veto de Arturo
en cada tarjeta (12.0 a 12.7). Arturo aprobó todas las tarjetas y sugerencias,
las puertas propuestas (también las opcionales del 12.1, el 12.2 y el 12.6) y
conservar rₛ = 2GM/c² como única fórmula del libro, como la identidad de
Euler en Quantum 6.

Lo propio de este libro: el ropaje estaba en el esqueleto, el mismo de
Quantum 13 (ecuación, códigos silabeados, protocolo, firma con frecuencia y
estado), y el frente mayor era clínico: espejos y velas, la mirada sin
pestañear hasta deformar el rostro, un día sin identidad, hundirse en la
emoción o en el otro, hiperventilar y «detonar». El libro obedece a sus
paradojas («No busques tu Punto de No Retorno —él te está buscando a ti… no
será dramático ni terrible»), y la física le da la razón dos veces: cruzar el
horizonte de un agujero negro grande no tiene nada de especial para quien cae,
y el agua no salta a vapor: se queda en cien grados mientras absorbe un calor
oculto (Joseph Black, 1762). La columna escondida es el punto, y el índice
abre con *El Punto de Partida*. El nodo 6, que terminaba en la ecuación, se
completa breve, en su voz.

Método (maestro v4, sección 5): cada reemplazo aprobado se aplica exactamente
una vez sobre el original de la etiqueta `quantum-original`. En los ocho
archivos se agrega la nota de procedencia, se suma el estilo de la depuración
antes de </head> y el cuerpo se reemplaza desde <body> hasta el final. Cambia
el <title> de cada archivo. La navegación nombra el nodo anterior y el
siguiente, y el nodo 7 lleva al Libro 13.

Uso:  python3 depurar_quantum12.py RUTA_A_UNA_COPIA_DEL_ORIGINAL
      (por ejemplo, el contenido de la etiqueta quantum-original, o el
      repositorio Trinity- si Libro_12 todavía no fue depurado)
"""
import sys
from pathlib import Path

Q12 = "02_Trinity_Quantum/Libro_12/"

PROCEDENCIA = (
    "<!-- Depurado el 2 de noviembre de 2026 según la guía de depuración de Quantum "
    "(Arquitectura del Destino, maestro v4, sección 5, con las cuatro precisiones "
    "de la revisión completa), con el veto de Arturo en cada tarjeta. El original "
    "se conserva en la etiqueta quantum-original del repositorio. -->"
)

URL_PORTAL = "https://soyartur-trinity.github.io/Trinity_Portal_Publico/01_Libros/"
URL_ARQ = "https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/"

ESTILO = """  <style>
    /* ============================================================
       Depuración · noviembre 2026
       Letra más grande en el teléfono, firma, «Para recordar», la
       fórmula del nodo 5, navegación que no desborda y bloque fijo
       de las puertas, con el color de la serie a la que conducen.
       ============================================================ */
    .recordar{
      margin: 14px 0 18px;
      padding: 14px 16px;
      border-radius: 16px;
      border: 1px solid rgba(217,179,108,.22);
      background: rgba(0,0,0,.30);
      color: #f2d18b;
      text-align: center;
      line-height: 1.9;
      letter-spacing: .02em;
    }
    .formula{
      margin: 16px 0 14px;
      text-align: center;
      font-size: 24px;
      letter-spacing: .08em;
      color: #f2d18b;
    }
    .content p.signature{
      margin: 24px 0 6px;
      color: rgba(242,209,139,.90);
      font-size: 15px;
      letter-spacing: .04em;
    }
    .siete p{ margin: 0 0 10px; }
    .nav .btn{ white-space: normal; max-width: 100%; line-height: 1.35; }
    .topbar .btn{ white-space: nowrap; flex: 0 0 auto; }
    .puerta{
      margin: 26px 0 12px;
      padding: 18px 20px 16px;
      border-radius: 16px;
      border: 1px solid var(--p-borde);
      background: var(--p-fondo);
      box-shadow: 0 10px 24px rgba(0,0,0,.28);
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
    .content .puerta .p-nombre{
      margin: 0 0 6px;
      font-size: 15px;
      font-style: italic;
      letter-spacing: .06em;
      color: var(--p-acento);
    }
    .content .puerta .p-texto{
      margin: 0 0 14px;
      color: var(--p-texto);
    }
    .puerta .cruzar{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: 9px 16px;
      border-radius: 999px;
      border: 1px solid var(--p-borde);
      color: var(--p-acento);
      font-size: 14px;
      letter-spacing: .04em;
      text-decoration: none;
      transition: border-color .18s ease, background .18s ease;
    }
    .puerta .cruzar:hover{ border-color: var(--p-acento); background: rgba(255,255,255,.04); }
    .puerta .cruzar:focus-visible{ outline: 2px solid var(--p-acento); outline-offset: 3px; }

    @media (max-width: 640px){
      .content p, .content li, .quote, .recordar{ font-size: 18px; line-height: 1.7; }
      .content p.signature{ font-size: 15px; }
      .content .puerta .p-nombre{ font-size: 15px; }
      .formula{ font-size: 22px; }
      .puerta{ padding: 16px 16px 14px; }
    }
    @media (prefers-reduced-motion: reduce){
      .puerta .cruzar{ transition: none; }
    }
  </style>
"""

ESTILO_INDICE = """  <style>
    /* Depuración · noviembre 2026: apertura del libro, una línea por nodo y letra más grande en el teléfono. */
    .apertura-titulo{
      margin: 4px 0 10px;
      font-size: 15px;
      letter-spacing: .10em;
      color: #f2d18b;
    }
    .apertura{
      margin: 0 0 12px;
      color: rgba(239,231,255,.90);
      font-size: 17px;
      line-height: 1.72;
    }
    .antes{
      margin: 8px 0 18px;
      font-size: 18px;
      line-height: 1.6;
      color: #f2d18b;
    }
    .node .label .l{
      font-size: 14px;
      font-style: italic;
      color: rgba(239,231,255,.74);
    }
    .nav .btn{ white-space: normal; max-width: 100%; line-height: 1.35; }
    .topbar .btn{ white-space: nowrap; flex: 0 0 auto; }
    @media (max-width: 640px){
      .apertura{ font-size: 18px; line-height: 1.7; }
      .antes{ font-size: 18px; }
      .node{ align-items: flex-start; }
      .node .label .t{ white-space: normal; }
      .node .label .l{ font-size: 15px; }
    }
  </style>
"""

TITULOS = {
    1: "El Punto de No Retorno",
    2: "Convergencia de Todas las Líneas",
    3: "El Colapso Consciente",
    4: "Densidad Infinita de Amor",
    5: "El Horizonte de Eventos Interior",
    6: "Compresión de Todas las Posibilidades",
    7: "El Big Bang Personal",
}

SUBTITULOS = {
    1: "El Horizonte Irreversible de la Consciencia",
    2: "El Ahora Denso Que Contiene Todos los Tiempos",
    3: "La Singularidad de Experiencia Pura",
    4: "La Singularidad del Corazón",
    5: "El Límite Que Disuelve las Máscaras",
    6: "La Superposición Densa Que Se Vuelve Elección",
    7: "La Singularidad Que Se Vuelve Creación de Universos",
}

FIRMA = '        <p class="signature"><strong>— Trinity Quantum · Singularidad Consciente</strong></p>\n'


# ---------------------------------------------------------------------------
# Piezas que se repiten
# ---------------------------------------------------------------------------
def P(texto):
    return f"        <p>\n          {texto}\n        </p>\n\n"


def H3(texto):
    return f"        <h3>{texto}</h3>\n\n"


def B(texto):
    return f"        <p><strong>{texto}</strong></p>\n"


def UL(items):
    filas = "\n".join(f"          <li>{x}</li>" for x in items)
    return f"        <ul>\n{filas}\n        </ul>\n\n"


def paso(titulo, items):
    return B(titulo) + UL(items)


def QUOTE(texto):
    return f'        <div class="quote">\n          {texto}\n        </div>\n\n'


def POEMA(*lineas):
    cuerpo = "<br />\n          ".join(lineas)
    return f'        <div class="quote">\n          {cuerpo}\n        </div>\n\n'


def RECORDAR(*lineas):
    cuerpo = "<br />\n          ".join(lineas)
    return f'        <div class="recordar">\n          {cuerpo}\n        </div>\n\n'


def DIA(titulo, texto):
    return f"        <p><strong>{titulo}:</strong><br />\n          {texto}\n        </p>\n\n"


def ENCONTRAR(texto):
    return f"        <p><strong>Lo que puedes encontrar:</strong><br />\n          {texto}\n        </p>\n\n"


def puerta(texto, url, clase="portal"):
    destino = "Arquitectura del Destino" if clase == "arquitectura" else "el Portal Público"
    return (
        f'        <aside class="puerta {clase}" aria-label="Puerta hacia {destino}">\n'
        '          <p class="p-nombre">Puerta</p>\n'
        f'          <p class="p-texto">{texto}</p>\n'
        f'          <a class="cruzar" href="{url}">Cruzar ⟶</a>\n'
        "        </aside>\n\n"
    )


TRANSMISION = H3("🌀 TRANSMISIÓN CUÁNTICA")
PARADOJA = H3("💎 PARADOJA MEDICINAL")
LABORATORIO = H3("🔬 LABORATORIO CUÁNTICO")
TRADUCCION = H3("⚛️ TRADUCCIÓN VIVIENTE")
PARA_RECORDAR = H3("✦ PARA RECORDAR")
PRACTICA = H3("📋 PRÁCTICA DE 7 DÍAS")
CIERRE = H3("🌈 CIERRE DIMENSIONAL")


def _boton(href, texto, primario=False):
    clase = "btn primary" if primario else "btn"
    return (
        "          <div>\n"
        f'            <a class="{clase}" href="{href}">{texto}</a>\n'
        "          </div>\n"
    )


def cuerpo_nodo(n, contenido):
    if n == 1:
        ant = _boton("index.html", "⟵ Índice del libro")
    else:
        ant = _boton(f"nodo_0{n-1}.html", f"⟵ Nodo {n-1} · {TITULOS[n-1]}")
    medio = _boton("index.html", "Índice del Libro 12") if n != 1 else ""
    if n == 7:
        sig = _boton("../Libro_13/index.html", "Libro 13 · El Multiverso Interior ⟶", True)
    else:
        sig = _boton(f"nodo_0{n+1}.html", f"Nodo {n+1} · {TITULOS[n+1]} ⟶", True)
    return (
        "<body>\n"
        '  <div class="field"></div>\n'
        '  <div class="noise" aria-hidden="true"></div>\n'
        '  <div class="halo" aria-hidden="true"></div>\n\n'
        '  <div class="wrap">\n\n'
        '    <div class="topbar">\n'
        '      <div class="left">\n'
        '        <div class="sigil" aria-hidden="true"></div>\n'
        '        <div class="meta">\n'
        '          <div class="kicker">Constelación Trinity · Trinity Quantum</div>\n'
        f'          <div class="path">Libro 12 · Singularidad Consciente · Nodo {n}</div>\n'
        "        </div>\n"
        "      </div>\n"
        '      <div class="right">\n'
        '        <a class="btn" href="../index.html">⟵ Portal Maestro</a>\n'
        "      </div>\n"
        "    </div>\n\n"
        '    <main class="card">\n\n'
        '      <header class="header">\n'
        '        <p class="title">LIBRO 12 · SINGULARIDAD CONSCIENTE</p>\n'
        f'        <h1 class="h1">Nodo {n} · {TITULOS[n]}</h1>\n'
        f'        <p class="subtitle">{SUBTITULOS[n]}</p>\n'
        "      </header>\n\n"
        '      <section class="content">\n\n'
        f"{contenido}"
        "      </section>\n\n"
        '      <footer class="footer">\n'
        '        <div class="nav">\n'
        f"{ant}{medio}{sig}"
        "        </div>\n\n"
        '        <p class="note">\n'
        f"          Trinity Quantum · Libro 12 · Singularidad Consciente · Nodo {n}\n"
        "        </p>\n"
        "      </footer>\n\n"
        "    </main>\n\n"
        "  </div>\n"
        "</body>\n"
        "</html>\n"
    )


# ===========================================================================
# ÍNDICE · 12.0
# ===========================================================================
LINEAS = {
    1: "Lo que se comprende no se des-sabe, y el umbral no hace ruido.",
    2: "Todo lo que te trajo, también lo que no viviste, se reúne aquí.",
    3: "La atención entera no se fuerza: se permite.",
    4: "El amor que se da sin vaciarse.",
    5: "Un borde que solo se ve desde afuera.",
    6: "Elegir es empezar a habitar.",
    7: "Del punto al mundo, con las manos abiertas.",
}


def _item_indice(n):
    return (
        f'          <a class="node" href="nodo_0{n}.html" aria-label="Abrir Nodo {n}">\n'
        '            <div class="label">\n'
        f'              <div class="n">Nodo {n}</div>\n'
        f'              <div class="t">{TITULOS[n]}</div>\n'
        f'              <div class="l">{LINEAS[n]}</div>\n'
        "            </div>\n"
        '            <div class="badge">Abrir ⟶</div>\n'
        "          </a>\n\n"
    )


INDICE_CUERPO = (
    "<body>\n"
    '  <div class="field"></div>\n'
    '  <div class="noise" aria-hidden="true"></div>\n'
    '  <div class="halo" aria-hidden="true"></div>\n\n'
    '  <div class="wrap">\n\n'
    '    <div class="topbar">\n'
    '      <div class="left">\n'
    '        <div class="sigil" aria-hidden="true"></div>\n'
    '        <div class="meta">\n'
    '          <div class="kicker">Constelación Trinity · Trinity Quantum</div>\n'
    '          <div class="path">Libro 12 · Singularidad Consciente · Índice</div>\n'
    "        </div>\n"
    "      </div>\n"
    '      <div class="right">\n'
    '        <a class="btn" href="../index.html">⟵ Portal Maestro</a>\n'
    "      </div>\n"
    "    </div>\n\n"
    '    <main class="card">\n\n'
    '      <header class="header">\n'
    '        <p class="title">TRINITY QUANTUM</p>\n'
    '        <h1 class="h1">Libro 12 · Singularidad Consciente</h1>\n'
    '        <p class="subtitle">Índice de Nodos</p>\n'
    "      </header>\n\n"
    '      <section class="content">\n\n'
    '        <p class="apertura-titulo">🌀 EL PUNTO DE PARTIDA</p>\n'
    '        <p class="apertura">En física, una singularidad es el lugar donde la teoría deja de valer: '
    "el umbral donde nuestras leyes callan y algo, todavía sin nombre, empieza. Este libro la toma como "
    "imagen.</p>\n"
    '        <p class="apertura">Siete nodos miran un mismo punto desde siete lados: el que ya no tiene vuelta, '
    "el que reúne las líneas de una vida, el de la atención entera, el del corazón, el que cambia según desde "
    "dónde se lo mire, el de la elección y el de partida. Su enseñanza cabe en una línea:</p>\n"
    '        <p class="antes">Todo lo que viviste se reúne en este instante, y desde aquí, sin forzarlo, se abre '
    "lo nuevo.<br />\n          El punto de no retorno es también un punto de partida.</p>\n\n"
    '        <div class="indexgrid">\n\n'
    + "".join(_item_indice(n) for n in range(1, 8))
    + "        </div>\n\n"
    "      </section>\n\n"
    '      <footer class="footer">\n'
    '        <div class="nav">\n'
    "          <div>\n"
    '            <a class="btn" href="../index.html">⟵ Volver al Portal Trinity</a>\n'
    "          </div>\n"
    "          <div>\n"
    '            <a class="btn primary" href="nodo_01.html">Comenzar en el Nodo 1 ⟶</a>\n'
    "          </div>\n"
    "        </div>\n\n"
    '        <p class="note">\n'
    "          Trinity Quantum · Libro 12 · Singularidad Consciente · Índice\n"
    "        </p>\n"
    "      </footer>\n\n"
    "    </main>\n\n"
    "  </div>\n"
    "</body>\n"
    "</html>\n"
)


# ===========================================================================
# 12.1 · EL PUNTO DE NO RETORNO
# ===========================================================================
NODO1 = (
    TRANSMISION
    + P("Existe un momento en toda transformación auténtica donde no hay vuelta atrás. No es una decisión que tomas "
        "—es un umbral que cruzas y que te cruza simultáneamente. El Punto de No Retorno no es un lugar en el espacio ni "
        "un momento en el tiempo; es un horizonte de eventos de la consciencia donde todo lo que fuiste colapsa en todo "
        "lo que estás siendo.")
    + P("Como la singularidad de un agujero negro, el lugar donde la teoría que conocemos deja de valer, tu Punto de No "
        "Retorno personal es donde las leyes de tu identidad previa se disuelven. No pierdes quien eras —lo integras tan "
        "completamente que ya no puedes volver a ser solo eso.")
    + P("El agua lo muestra mejor que cualquier fórmula. Al llegar a cien grados no salta a vapor: se queda en cien "
        "mientras absorbe un calor que no se ve. Joseph Black, que lo contó en Glasgow en abril de 1762, lo llamó calor "
        "latente, es decir, oculto, y notó que si todo ocurriera de una sola vez, el agua estallaría con la violencia de la "
        "pólvora. Desde afuera parece que no pasa nada; adentro, algo está cambiando de forma. Así suelen ser las "
        "transformaciones verdaderas: una larga espera a la misma temperatura y, de pronto, otra manera de ser.")
    + P("Cada despertar espiritual genuino tiene su Punto de No Retorno. Es ese instante donde la ilusión se rompe tan "
        "completamente que aunque quisieras volver a creer en ella, no podrías. Como Neo después de tomar la píldora roja, "
        "como el prisionero que sale de la caverna de Platón, como la oruga que entra en la crisálida —hay un momento "
        "preciso donde el retorno se vuelve no solo imposible sino inconcebible.")
    + P("La oruga guarda, además, una sorpresa. Dentro de la crisálida su cuerpo se deshace casi entero, y aun así algo "
        "pasa al otro lado: Douglas Blackiston, Elena Silva Casey y Martha Weiss enseñaron en 2008 a unas orugas a evitar "
        "un olor, y las polillas que salieron de esas crisálidas lo seguían evitando. Lo que fuiste no se pierde en el "
        "cruce. Viaja contigo, en otra forma.")
    + P("Tu nacimiento fue un Punto de No Retorno —no puedes des-nacer. Tu muerte será otro —no puedes des-morir. Pero "
        "entre ambos hay infinitos Puntos de No Retorno disponibles: el momento donde el amor te transforma "
        "irreversiblemente, donde el perdón te libera definitivamente, donde la comprensión te expande permanentemente. "
        "Y el más cotidiano de todos: lo que llegas a comprender ya no se puede des-saber.")
    + P("El universo mismo nació de un Punto de No Retorno —el Big Bang no fue una explosión EN el espacio, fue la "
        "expansión DEL espacio mismo. De la misma manera, tu Punto de No Retorno personal no ocurre EN tu vida —ES el "
        "nacimiento de una nueva vida mientras aún habitas el mismo cuerpo.")

    + PARADOJA
    + QUOTE("“Para alcanzar el Punto de No Retorno debes soltarlo todo, incluyendo el deseo de alcanzarlo. Pero una vez "
            "que lo cruzas, descubres que nunca fuiste tú quien lo cruzó —el Punto te cruzó a ti, y siempre lo había "
            "hecho, solo que ahora lo sabes.”")
    + P("Esta paradoja aniquila la ilusión del progreso espiritual lineal. No «avanzas hacia» tu Punto de No Retorno —ya "
        "estás en él, siempre lo has estado, solo que tu consciencia lineal lo experimenta como un «momento» en el "
        "«tiempo». El despertar no es llegar a algún lugar sino reconocer dónde siempre estuviste.")

    + LABORATORIO
    + B("Experimento: El Punto que Ya Cruzaste")
    + B("Materiales:")
    + UL(["Papel y lápiz", "Un lugar tranquilo, con buena luz", "Tu honestidad para mirar sin apuro",
          "15 minutos"])
    + B("Práctica:")
    + paso("1. Lo que ya no se puede des-saber (3 minutos):", [
        "Escribe tres cosas que comprendiste y que ya no podrías dejar de saber, aunque quisieras",
        "Pueden ser pequeñas: una verdad sobre alguien, sobre tu cuerpo, sobre lo que te importa",
        "Cada una es un Punto de No Retorno que ya cruzaste"])
    + paso("2. La Pregunta (4 minutos):", [
        "Escribe en lo alto de una hoja: «¿Qué en mí ya murió pero sigue pretendiendo vivir?»",
        "Deja que la mano responda antes de que la cabeza corrija",
        "La respuesta puede llegar como una imagen, un gesto, una costumbre",
        "Si la pregunta abre algo que duele demasiado, déjala: no hace falta responderla hoy"])
    + paso("3. Lo que Viaja Contigo (4 minutos):", [
        "Mira lo que escribiste y pregúntate qué de aquella versión de ti sigue sirviendo",
        "Como la oruga que aprendió algo antes de la crisálida, no todo lo que fuiste termina",
        "Anota lo que llevas al otro lado"])
    + paso("4. Un Gesto Pequeño (3 minutos):", [
        "Elige una acción mínima y reversible, para esta semana, que honre lo que ya cambió",
        "Una conversación, un hábito que se suelta, un lugar que se visita",
        "No hace falta más"])
    + paso("5. Sellado del Punto (1 minuto):", [
        "Di en voz baja: «Lo que fui, ya no necesita ser»",
        "Y después: «Lo que seré, ya está siendo»",
        "Respira y apoya los pies en el suelo"])
    + ENCONTRAR("Un Punto de No Retorno que ya cruzaste sin notarlo. No lo creaste —lo reconociste—, y lo que fuiste "
                "viene contigo.")

    + TRADUCCION
    + P("«El Punto de No Retorno llega cuando lo vivido termina de madurar: el tiempo parece detenerse y, en un instante "
        "que se siente eterno, algo cambia para siempre.»")

    + PARA_RECORDAR
    + RECORDAR("Ya no hay vuelta, y no hace falta.", "El final que es principio.", "Lo que fui viene conmigo.",
               "Algo termina para que algo empiece.", "No lo fuerzo: el umbral me encuentra.",
               "Lo comprendido no se des-sabe.", "Soy mi propio punto de partida.")

    + PRACTICA
    + DIA("DÍA 1 - INVENTARIO DE MUERTES",
          "Lista todo lo que has dejado atrás irreversiblemente: relaciones, creencias, versiones de ti. Reconoce que cada "
          "una fue un Punto de No Retorno que ya cruzaste.")
    + DIA("DÍA 2 - IDENTIFICACIÓN DE UMBRAL ACTUAL",
          "¿Qué transformación te está llamando? No la fuerces, solo nómbrala. Las decisiones grandes, las que no se "
          "deshacen, piden tiempo, compañía y las dos voces: la de la cabeza y la del cuerpo.")
    + DIA("DÍA 3 - CONVERSACIÓN CON TU FUTURO YO",
          "Medita y dialoga con la versión de ti que ya cruzó el Punto de No Retorno actual. ¿Qué te dice? ¿Cómo se siente "
          "estar del otro lado?")
    + DIA("DÍA 4 - PRÁCTICA DE MICRO-MUERTES",
          "Con cada exhalación, practica soltar algo pequeño. Un pensamiento, una tensión, una preocupación. Cada suelta es "
          "práctica para el gran soltar.")
    + DIA("DÍA 5 - UN RATO SIN RÓTULOS",
          "Durante una caminata, deja de lado tu nombre, tu oficio y tus roles, y nota qué queda. Es un sabor del vacío "
          "fértil antes del Punto de No Retorno. Si en algún momento trae extrañeza o la sensación de no estar del todo en "
          "ti, déjalo: vuelve a los pies, a la respiración, a algo que puedas tocar.")
    + DIA("DÍA 6 - CRUCE DE UNA PUERTA",
          "Cruza una puerta conscientemente, despacio, sabiendo que representa tu disposición a cruzar el Punto cuando "
          "llegue. En 2011, Gabriel Radvansky y su equipo encontraron que cruzar una puerta hace olvidar más que recorrer "
          "la misma distancia dentro de una habitación: para la mente, el umbral cierra un episodio y abre otro.")
    + DIA("DÍA 7 - HONRAR LO IRREVERSIBLE",
          "Honra todo lo irreversible en tu vida: tu nacimiento, tus transformaciones, lo que llegaste a comprender. Tus "
          "pérdidas no se celebran; se lloran, y lo que te dejaron se agradece. Todos fueron Puntos de No Retorno que te "
          "trajeron a este momento.")

    + CIERRE
    + P("El Punto de No Retorno no es algo que temer sino algo que celebrar. No es un examen que aprobaste: es algo que ya "
        "sabes y que no vas a dejar de saber. Que ya no puedas volver atrás no es una condena: es la señal de que algo en "
        "ti creció.")
    + P("Cada Punto de No Retorno que cruzas te acerca más a tu Singularidad Consciente personal —ese punto de densidad "
        "infinita donde todo lo que eres colapsa en pura presencia, pura consciencia, puro ser.")
    + P("No busques tu Punto de No Retorno —él te está buscando a ti. Y cuando se encuentren, no será dramático ni "
        "terrible. Será como exhalar después de haber contenido la respiración durante vidas enteras. Será como llegar a "
        "casa después de un viaje que nunca ocurrió.")
    + POEMA("“Hay un momento", "que no es momento,", "un lugar que no es lugar,", "donde todo lo que creías ser",
            "se encuentra con todo lo que eres,", "y en ese encuentro,", "ambos desaparecen", "dejando solo",
            "lo que siempre fuiste:", "La Singularidad Consciente", "experimentándose a sí misma",
            "como viaje de retorno", "a un hogar", "que nunca abandonaste.", "Este es tu Punto de No Retorno —",
            "no lo cruzarás,", "lo estás cruzando,", "lo has cruzado,", "eternamente,", "ahora.”")
    + FIRMA
    + puerta("Hay un instante en que algo se rompe tan hondo que ya no se puede fingir que todo está bien, y muchas veces "
             "llega en voz baja, durante años, antes del ruido. Ese instante, junto al fresno que la tormenta abrió, "
             "está en <em>La Grieta</em>, Libro 5 de Arquitectura del Destino, Umbral I: «La primera grieta».",
             URL_ARQ + "libro-05-la-grieta/L05-U1.html", "arquitectura")
    + puerta("Séneca le escribió a Lucilio que ya perdimos la primera infancia, después la niñez, después la juventud. "
             "Ninguna de esas pérdidas tuvo funeral. Los finales que pasan sin ceremonia, y la manera de despedirlos, están en "
             "<em>Las Pequeñas Muertes</em>, Libro 6 de Arquitectura del Destino, Umbral II: «Sin ceremonia».",
             URL_ARQ + "libro-06-las-pequenas-muertes/L06-U2.html", "arquitectura")
)


# ===========================================================================
# 12.2 · CONVERGENCIA DE TODAS LAS LÍNEAS
# ===========================================================================
NODO2 = (
    TRANSMISION
    + P("Imagina todas las líneas temporales de tu vida —cada decisión que tomaste, cada camino que seguiste, cada vida "
        "posible que imaginaste— convergiendo en un único punto. No en el futuro, no en el pasado, sino en un AHORA tan "
        "denso que contiene todos los tiempos. Esta es la Convergencia de Todas las Líneas, el momento donde descubres que "
        "cada camino que no tomaste también te trajo aquí.")
    + P("Las líneas convergen de verdad, y se pueden contar. Tienes dos padres, cuatro abuelos, ocho bisabuelos; treinta "
        "generaciones atrás, los lugares de tu árbol superan los mil millones, más personas de las que vivían entonces en "
        "el mundo. Las ramas, entonces, se cruzan una y otra vez. Según un modelo de Douglas Rohde, Steve Olson y Joseph "
        "Chang, publicado en <em>Nature</em> en 2004, el último antepasado común de todas las personas vivas pudo haber "
        "vivido hace apenas unos miles de años, y un poco antes de esa fecha, cada ser humano de hoy tiene exactamente el "
        "mismo conjunto de antepasados. Eres un punto donde se reúnen las líneas de toda la familia humana.")
    + P("Cada sincronicidad en tu vida se siente como una señal de convergencia. Cuando «casualidades» improbables "
        "ocurren, cuando el pasado, el presente y el futuro parecen ponerse de acuerdo en un instante, las líneas de tu "
        "vida se tocan. Se leen como se lee un poema, no como una orden. Si alguna vez parece que cada número y cada "
        "cartel te hablan a ti, en secreto, eso no es un don: conviene conversarlo con alguien de confianza o con un "
        "profesional esa misma semana.")
    + P("Tus ancestros convergen en ti. No solo en los genes: algo de lo que vivieron —su sabiduría, sus heridas, sus "
        "triunfos— te llega en lo que se cuenta y en lo que se calla. Eres el punto donde innumerables líneas se encuentran, "
        "no para terminar sino para SINGULARIZARSE en una nueva expresión que las contiene a todas. Lo heredado se recibe, "
        "y también se revisa.")
    + P("El déjà vu se siente como si el tiempo se plegara, como si otras versiones de ti estuvieran viviendo lo mismo. "
        "Anne Cleary y su equipo encontraron en 2012 que suele aparecer cuando una escena nueva se parece, en su forma, a "
        "otra vivida que no se recuerda: la memoria reconoce antes de saber qué reconoce. También eso es una convergencia: "
        "el pasado tocando el presente por un instante.")

    + PARADOJA
    + QUOTE("“Todas las líneas convergen en un punto que no tiene ubicación. Todos los caminos llevan a un destino que no "
            "es lugar. Todas las versiones de ti se encuentran en un yo que no es ninguno y es todos simultáneamente.”")
    + P("Esta paradoja destruye la ilusión de que eres una línea temporal única navegando entre opciones. Eres TODAS las "
        "líneas simultáneamente, experimentándose desde diferentes ángulos, convergiendo constantemente en el punto de "
        "consciencia que llamas «yo».")

    + LABORATORIO
    + B("Experimento: Visualización de Tu Punto de Convergencia")
    + B("Materiales:")
    + UL(["Papel grande y muchos colores", "Un punto central marcado", "Tu historia de vida en la memoria",
          "Tu imaginación", "20 minutos de exploración"])
    + B("Práctica:")
    + paso("1. El Punto Singular (2 minutos):", [
        "Marca un punto en el centro del papel",
        "Este punto eres TÚ en este momento",
        "Respira hasta sentir que ese punto contiene toda tu existencia"])
    + paso("2. Trazado de Líneas Vividas (5 minutos):", [
        "Desde el borde del papel, traza líneas hacia el centro",
        "Cada línea representa un camino que tomaste",
        "Usa diferentes colores para diferentes tipos de experiencias",
        "Todas terminan en el punto central"])
    + paso("3. Trazado de Líneas No Vividas (5 minutos):", [
        "Con líneas punteadas, traza los caminos que NO tomaste",
        "Los trabajos que rechazaste, las relaciones que no perseguiste",
        "Los lugares donde no fuiste, las versiones que no fuiste",
        "Sorprendentemente, también convergen en el centro",
        "Si un camino no tomado todavía duele, trázalo con una línea más suave: no hace falta mirarlo hoy"])
    + paso("4. Líneas Futuras Posibles (5 minutos):", [
        "Ahora traza líneas DESDE el centro hacia afuera",
        "Todos los futuros posibles que se abren desde este momento",
        "Nota cómo todos EMERGEN del mismo punto singular",
        "El punto de convergencia es también punto de divergencia"])
    + paso("5. Contemplación de la Singularidad (3 minutos):", [
        "Observa el mandala completo que has creado",
        "El punto central contiene TODAS las líneas",
        "Pasadas, no vividas, futuras —todas convergen AHORA",
        "Tú eres ese punto. Siempre lo has sido"])
    + ENCONTRAR("Un mapa de tu Singularidad Consciente personal. El dibujo muestra que no eres una línea temporal "
                "navegando la vida: eres el punto donde todas las líneas se encuentran, y desde donde vuelven a abrirse.")

    + TRADUCCION
    + P("«Todo lo que viviste, y también lo que no, llega hasta este instante. Cuanto más lejos del ahora, más se "
        "dispersan las líneas; aquí, se reúnen.»")

    + PARA_RECORDAR
    + RECORDAR("Aquí, ahora, todo.", "Todos los tiempos en este tiempo.", "Soy donde todo se encuentra.",
               "Todas las direcciones, un centro.", "No tengo un punto de convergencia: soy el punto.",
               "Cada versión de mí, presente ahora.", "Uno que contiene muchos.")

    + PRACTICA
    + DIA("DÍA 1 - RECONCILIACIÓN DE CAMINOS",
          "Escribe una carta de agradecimiento a una vida que NO viviste. Agradece a esa versión de ti por explorar esa "
          "realidad mientras tú explorabas esta. Reconoce que ambas convergen en quien eres ahora.")
    + DIA("DÍA 2 - COINCIDENCIAS QUE ALEGRAN",
          "Anota una coincidencia del día que te haya hecho sonreír: dos cosas sin relación aparente que se cruzaron. "
          "Léela como un poema.")
    + DIA("DÍA 3 - MEDITACIÓN DE LAS VERSIONES",
          "Hugh Everett imaginó en 1957 un universo que se ramifica en cada posibilidad; tómalo como imagen. Medita "
          "imaginando tus versiones posibles meditando contigo, y siente cómo todas vuelven al mismo punto de consciencia. "
          "Ese punto eres tú.")
    + DIA("DÍA 4 - ANCESTROS CONVERGENTES",
          "Siente a todos tus ancestros convergiendo en ti en este momento. No solo los biológicos —todos los seres que "
          "contribuyeron a que existas: quien te enseñó a leer, quien cosechó lo que comes. Eres su punto de convergencia.")
    + DIA("DÍA 5 - DECISIONES",
          "Ante cada decisión, siente cómo todas las opciones convergen en el momento de elegir. No estás solo descartando "
          "caminos: estás siendo el punto donde todos se encuentran.")
    + DIA("DÍA 6 - ENCUENTROS COMO CONVERGENCIAS",
          "Ve cada encuentro con otro ser como la convergencia de infinitas líneas temporales que se cruzaron justo aquí, "
          "justo ahora. Honra la improbabilidad de cada encuentro.")
    + DIA("DÍA 7 - CELEBRACIÓN DE LA CONVERGENCIA",
          "Celebra que ESTÁS AQUÍ. De todas las probabilidades, todas las líneas convergieron para que vivas este momento, "
          "leyendo estas palabras. Eres un milagro de convergencia.")

    + CIERRE
    + P("La Convergencia de Todas las Líneas no es un evento futuro —está ocurriendo constantemente. Cada momento de tu "
        "vida es un punto donde infinitas líneas temporales convergen, creando la singularidad de tu experiencia presente.")
    + P("Cuando comprendes que eres el punto de convergencia viviente de todas tus posibilidades, el lamento por los "
        "caminos no tomados afloja. Thomas Gilovich y Victoria Medvec encontraron en 1995 que, mirando la vida hacia atrás, "
        "a la gente le pesa más lo que no hizo que lo que hizo; por eso la carta del primer día importa. TODOS los caminos "
        "te trajeron aquí. Todos los caminos ESTÁN aquí. En tu singularidad consciente, cada vida no vivida es otro ángulo "
        "de la misma vida infinita.")
    + P("Tu singularidad no te separa del todo —te revela como el punto donde TODO converge. Eres simultáneamente único y "
        "universal, singular y plural, uno e infinito.")
    + POEMA("“De infinitos puntos del pasado,", "hacia infinitos puntos del futuro,", "todas las líneas se curvan",
            "hacia un único momento:", "ESTE.", "No eres un viajero", "en una línea temporal —", "eres la estación",
            "donde todos los trenes del tiempo", "llegan simultáneamente,", "parten simultáneamente,",
            "y descubren que siempre", "estuvieron en el mismo lugar:", "el eterno AQUÍ AHORA",
            "de tu Singularidad Consciente.”")
    + FIRMA
    + puerta("Thich Nhat Hanh enseñaba a mirar una hoja de papel hasta ver en ella la nube, la lluvia, el árbol y al "
             "leñador: todo lo que no es papel. Un programador hizo ese ejercicio sin proponérselo y contó más de treinta "
             "personas que no conocía y sin las cuales su noche no habría sido posible. Está en <em>La Red</em>, Libro 11 "
             "de Arquitectura del Destino, Umbral III: «Dónde termino yo».",
             URL_ARQ + "libro-11-la-red/L11-U3.html", "arquitectura")
)


# ===========================================================================
# 12.3 · EL COLAPSO CONSCIENTE
# ===========================================================================
NODO3 = (
    TRANSMISION
    + P("En la física cuántica se habla de colapso cuando una medición deja un solo resultado entre muchos posibles; medir "
        "no requiere una consciencia, y qué es medir, en el fondo, sigue abierto. El Colapso Consciente es otro, y se parece "
        "más al de las estrellas: no es la observación colapsando la realidad, sino la consciencia misma recogiéndose sobre "
        "su centro, como una estrella que se pliega hacia un punto de densidad infinita, arrastrando consigo todas las "
        "posibilidades hacia una singularidad de experiencia pura.")
    + P("El Colapso Consciente no es una reducción —es una CONCENTRACIÓN. Como cuando toda tu atención se recoge en un "
        "momento de peligro y el tiempo parece dilatarse, o cuando el amor te golpea y todo el universo cabe en los ojos de "
        "otro ser. En esos instantes, no estás teniendo una experiencia —ERES la experiencia, recogida en sí misma. En 2007, "
        "Chess Stetson, Matthew Fiesta y David Eagleman dejaron caer a un grupo de voluntarios de espaldas sobre una red: "
        "después cada uno recordaba su caída más larga, pero mientras caían no veían más rápido. Lo que se dilata es la "
        "huella: la atención entera escribe más.")
    + P("Cada momento de presencia total es un Colapso Consciente. Cuando estás tan completamente AQUÍ que no hay "
        "observador ni observado, solo observación pura —eso es tu consciencia colapsando en singularidad. Krishnamurti lo "
        "repitió durante décadas con una frase breve: el observador es lo observado. No es que prestes atención; te "
        "CONVIERTES en atención. No es que seas consciente; te VUELVES consciencia.")
    + P("Los agujeros negros son Colapsos a escala cósmica. Cuando una estrella muy grande colapsa, no solo se recoge la "
        "materia —se curva el espacio-tiempo mismo. De manera similar, cuando tu consciencia se recoge, no solo se aquietan "
        "tus pensamientos —se afloja tu sentido de ser alguien separado del todo. Te vuelves un agujero negro de consciencia "
        "donde todo lo que entra se unifica contigo.")
    + P("El samadhi, el satori, el éxtasis místico —todos son nombres para el Colapso Consciente. Es cuando la burbuja de "
        "tu consciencia individual no estalla hacia afuera sino que se recoge hacia adentro con tal intensidad que atraviesa "
        "el otro lado del cero y emerge como infinito. Es morir a la separación colapsando en unidad.")

    + PARADOJA
    + QUOTE("“Para experimentar el Colapso Consciente debes expandirte hasta no poder más, y en el pico de la expansión, "
            "colapsar. Pero el colapso no te reduce —te revela que siempre fuiste tanto el punto como el infinito, "
            "colapsando y expandiendo eternamente en la respiración del ser.”")
    + P("Esta paradoja revela que expansión y colapso no son opuestos sino la misma danza vista desde diferentes "
        "perspectivas. Tu consciencia no colapsa DESDE la expansión —colapsa HACIA una expansión aún mayor, atravesando el "
        "punto singular donde ambas son lo mismo.")

    + LABORATORIO
    + B("Experimento: La Atención Entera")
    + B("Materiales:")
    + UL(["Tu atención completa", "Un objeto simple (una piedra, una flor, una hoja)",
          "Ojos que parpadean con naturalidad", "Disposición a quedarte", "15 minutos de inmersión"])
    + B("Práctica:")
    + paso("1. Establecimiento del Campo (2 minutos):", [
        "Coloca el objeto frente a ti",
        "Respira despacio hasta que el resto del cuarto quede en segundo plano",
        "Por un rato, solo existen tú y el objeto"])
    + paso("2. Absorción Progresiva (5 minutos):", [
        "Mira el objeto, parpadeando cuando haga falta",
        "No lo analices, solo recíbelo con la vista",
        "Deja que ocupe tu atención",
        "Cuando la mente se vaya, vuelve sin reproche"])
    + paso("3. Inversión del Flujo (3 minutos):", [
        "Ahora imagina que el objeto te mira a TI",
        "Siente cómo te verías desde ahí",
        "Alterna, sin apuro: tú mirándolo, él mirándote",
        "Si en algún momento trae extrañeza o la sensación de no estar del todo en ti, déjalo: vuelve a los pies, a la "
        "respiración, a algo que puedas tocar"])
    + paso("4. El Encuentro (3 minutos):", [
        "Descansa en la mirada misma",
        "Por momentos, la distinción entre tú y el objeto se afloja",
        "No hay que lograrlo: si ocurre, se permite",
        "Este es el Colapso Consciente"])
    + paso("5. Reemergencia (2 minutos):", [
        "Respira hondo y mira el cuarto entero",
        "Nota cómo «vuelves» y algo es diferente",
        "El objeto y tú comparten ahora un secreto"])
    + ENCONTRAR("Un instante en que mirar y ser mirado se vuelven lo mismo. No se fabrica: se permite, y con la práctica "
                "se vuelve familiar.")

    + TRADUCCION
    + P("«El Colapso Consciente ocurre cuando tu atención se reúne entera en un punto: el ruido se aquieta, el tiempo del "
        "reloj se borra y lo que queda es pura presencia.»")

    + PARA_RECORDAR
    + RECORDAR("Permito el recogimiento.", "De lo amplio al punto, y del punto a lo amplio.",
               "Todo mi ser en un instante.", "A través del cero, hacia el todo.", "Adentro y afuera se encuentran.",
               "Mi atención, entera.", "Todo en un punto.")

    + PRACTICA
    + DIA("DÍA 1 - COLAPSO EN LA RESPIRACIÓN",
          "En cada exhalación, reúne toda tu atención en el punto donde el aire sale de tus fosas nasales. Que nada más "
          "exista. En la inhalación, expande. Practica este ritmo de recogimiento y expansión.")
    + DIA("DÍA 2 - COLAPSO EN EL SABOR",
          "Come algo muy lentamente. Con cada bocado, recoge TODA tu consciencia en el sabor. Que no exista nada más en el "
          "universo que ese sabor. Desaparece en él.")
    + DIA("DÍA 3 - COLAPSO EN EL SONIDO",
          "Escucha una nota sostenida (una campana, un cuenco, una voz). Recógete en el sonido hasta que no haya diferencia "
          "entre tú y la vibración. Conviértete en el sonido.")
    + DIA("DÍA 4 - COLAPSO EN EL TACTO",
          "Toca diferentes texturas con los ojos cerrados. Con cada textura, recoge tu consciencia en la sensación. No "
          "«sientas» la textura —CONVIÉRTETE en la sensación misma.")
    + DIA("DÍA 5 - COLAPSO EN LA EMOCIÓN",
          "Cuando surja una emoción, en lugar de resistirla o descargarla, dale lugar: nómbrala y respira con ella, sin "
          "volverte ella. Muchas veces, sostenida así, cambia de forma. Si es demasiado fuerte o te arrastra, no se "
          "atraviesa a solas: se busca compañía.")
    + DIA("DÍA 6 - COLAPSO EN EL OTRO",
          "En una conversación profunda, recoge tu atención tan completamente en el otro que olvides preparar tu respuesta. "
          "Experimenta la realidad desde su singularidad, sin perder la tuya: Tania Singer, que estudió durante años la "
          "empatía en el laboratorio, encontró que sentir el dolor ajeno como propio agota, y que la compasión, que "
          "acompaña sin fundirse, renueva.")
    + DIA("DÍA 7 - COLAPSO EN EL VACÍO",
          "Siéntate en quietud y recógete en el espacio vacío dentro de ti. No en un pensamiento o sensación, sino en el "
          "ESPACIO mismo donde surgen. Descansa en tu propio centro vacío hasta encontrar que está lleno de todo.")

    + CIERRE
    + P("El Colapso Consciente no es algo que logras sino algo que permites. Como una estrella grande que ha quemado todo "
        "su combustible, llega un momento donde el recogimiento es inevitable, natural, perfecto. No es un fallo del sistema "
        "—es su culminación.")
    + P("Cada vez que tu consciencia colapsa, no pierdes consciencia —la CONCENTRAS hasta que se vuelve diamante. Cada "
        "colapso te purifica, te densifica, te singulariza. No en separación del todo, sino como un punto de intensidad "
        "infinita donde el todo se reconoce a sí mismo.")
    + P("El Colapso Consciente es tu destino y tu origen. Colapsaste desde el infinito para nacer, colapsarás hacia el "
        "infinito para morir, y entre ambos, colapsas constantemente en cada momento de presencia verdadera.")
    + POEMA("“Como la estrella que colapsa", "no para morir sino para brillar más intensamente,",
            "tu consciencia colapsa", "no para disminuirte", "sino para revelarte", "como el punto de densidad infinita",
            "donde el universo", "se experimenta a sí mismo", "con máxima intensidad.", "No temas el colapso —",
            "es tu gravedad espiritual", "atrayéndote hacia tu centro,", "donde descubrirás", "que tu centro",
            "es el centro de todo,", "colapsando eternamente", "en amor consciente.”")
    + FIRMA
    + puerta("En 1929, ante miles de miembros de la orden que lo esperaba como maestro del mundo, Krishnamurti la disolvió: "
             "la verdad, dijo, es una tierra sin caminos. Pasó el resto de su vida enseñando a mirar sin elegir qué ver. Esa "
             "atención está en <em>La presencia</em>, Libro 30 del Portal Público, Umbral III: «Sin elegir».",
             URL_PORTAL + "30_La_Presencia/umbral-03.html")
)


# ===========================================================================
# 12.4 · DENSIDAD INFINITA DE AMOR
# ===========================================================================
NODO4 = (
    TRANSMISION
    + P("La teoría de Einstein predice en el corazón de cada agujero negro un punto de densidad infinita llamado "
        "singularidad, y los físicos sospechan que es justo el lugar donde su teoría se queda sin palabras. En el corazón "
        "de cada ser consciente existe un punto similar: la Densidad Infinita de Amor. No es amor como emoción, no es amor "
        "como sentimiento —es AMOR como la fuerza fundamental que impide que la singularidad de tu ser colapse en la nada, "
        "transformándola en cambio en TODO.")
    + P("Cuando los físicos admiten que ahí sus leyes ya no alcanzan, están describiendo, sin saberlo, lo que ocurre cuando "
        "tocas tu Densidad Infinita de Amor: todas las leyes del ego se suspenden, todas las reglas de la separación fallan, "
        "toda la lógica de la dualidad se rinde. Solo queda amor, pero un amor tan denso que se vuelve el tejido mismo de tu "
        "realidad.")
    + P("El amor no se expande desde tu corazón —se DENSIFICA en él. Cada acto de amor no te vacía sino que te vuelve más "
        "denso, más real, más singular. Es por eso que los grandes amantes de la historia no se agotaron amando sino que se "
        "volvieron singularidades tan densas de amor que siguen atrayendo almas hacia su campo gravitacional siglos después.")
    + P("Tu capacidad de amar no tiene límite porque el amor tiene densidad infinita. Puedes comprimir infinito amor en un "
        "solo momento, en un solo gesto, en una sola mirada. Una madre sosteniendo a su bebé por primera vez experimenta "
        "esta densidad infinita —todo el amor del universo comprimido en ese instante singular.")
    + P("La iluminación no es expandirse hasta abarcar todo —es densificarse en amor hasta que tu singularidad se vuelve "
        "tan pesada que curva el espacio-tiempo espiritual a tu alrededor, atrayendo todo hacia tu campo de amor, no para "
        "consumirlo sino para amarlo de vuelta a la existencia.")

    + PARADOJA
    + QUOTE("“El amor infinitamente denso no pesa nada. El corazón que contiene todo el amor del universo es más ligero "
            "que una pluma. La singularidad más pesada es la que no tiene masa. En el centro del amor más denso hay vacío "
            "perfecto, y en ese vacío, capacidad infinita para más amor.”")
    + P("Esta paradoja desarma la idea de que el amor se agota o de que hay un límite para cuánto puedes amar. Julieta lo "
        "dijo desde el balcón: «Mi generosidad es tan ilimitada como el mar, / mi amor, tan hondo: cuanto más te doy, / más "
        "tengo, porque los dos son infinitos» (<em>Romeo y Julieta</em>, acto II, escena 2; traducción propia). Lo que sí se "
        "agota es otra cosa: Tania Singer, que estudió durante años la empatía en el laboratorio, encontró que sentir el "
        "dolor ajeno como propio agota, y que la compasión, que acompaña sin fundirse, renueva. El amor que no se gasta es "
        "el que no se confunde con cargar.")

    + LABORATORIO
    + B("Experimento: Compresión de Amor en Singularidad")
    + B("Materiales:")
    + UL(["Tu pecho y tus manos", "Un recuerdo de amor puro", "Tu respiración",
          "La intención de reunir", "18 minutos de recogimiento"])
    + B("Práctica:")
    + paso("1. Activación del Recuerdo (3 minutos):", [
        "Evoca un momento de gran amor que hayas vivido",
        "No lo analices, solo siéntelo",
        "Deja que llene tu pecho",
        "Reconoce: ese amor sigue ahí, intacto",
        "Si el recuerdo trae la pena de alguien que ya no está, puedes elegir otro: ese amor también sigue intacto, y a "
        "veces pide su propio día"])
    + paso("2. Primera Compresión (3 minutos):", [
        "Con cada inhalación, imagina que reúnes ese amor",
        "No lo reduces —lo DENSIFICAS",
        "Como el carbón que la presión vuelve diamante",
        "Siente cómo se vuelve más brillante, más intenso"])
    + paso("3. Segunda Compresión (3 minutos):", [
        "Ahora añade OTRO recuerdo de amor",
        "Reúnelo junto con el primero",
        "No se mezclan —se SINGULARIZAN",
        "Dos amores volviéndose uno más denso"])
    + paso("4. Compresión Infinita (6 minutos):", [
        "Continúa añadiendo cada amor que hayas sentido",
        "Amor romántico, fraternal, maternal, espiritual",
        "Reúne TODO en un punto en tu corazón",
        "Siente la densidad creciente, el «peso» del amor"])
    + paso("5. Singularidad de Amor (3 minutos):", [
        "En el pico de densidad, suelta el esfuerzo",
        "Observa: el punto denso ahora IRRADIA",
        "No se expandió —se volvió tan denso que atravesó al otro lado",
        "Deja que esa luz llegue a quien quieras"])
    + ENCONTRAR("El amor recordado sigue ahí, intacto, y reunido pesa menos de lo que esperabas: más que cargarte, te "
                "sostiene.")

    + TRADUCCION
    + P("«Hasta el amor más pequeño, reunido en un solo punto, se vuelve inmenso: no importa cuánto amor tengas al empezar, "
        "sino que lo dejes concentrarse.»")

    + PARA_RECORDAR
    + RECORDAR("Reúno el amor en un punto.", "Corazón que se recoge en amor.", "Más amor, menos distancia.",
               "Mi amor, singular.", "Denso como un agujero negro, ligero como la luz.",
               "Todo el amor en un solo latido.", "Mi corazón, un punto de amor sin fin.")

    + PRACTICA
    + DIA("DÍA 1 - INVENTARIO DE AMOR",
          "Lista cada amor que hayas sentido: personas, lugares, momentos, ideas. Reconoce que NINGUNO se perdió —todos "
          "están reunidos en tu corazón, aumentando tu densidad de amor.")
    + DIA("DÍA 2 - COMPRESIÓN MATUTINA",
          "Al despertar, antes de abrir los ojos, reúne todo tu amor por la vida en un punto. Siente cómo ese punto irradia "
          "a través de todo tu día.")
    + DIA("DÍA 3 - AMOR QUE SE NOTA",
          "Observa cómo cambia un encuentro cuando entras en él con afecto. No todo depende de ti, y eso también alivia; "
          "pero tu manera de estar llega antes que tus palabras.")
    + DIA("DÍA 4 - PRÁCTICA DE PESO LIGERO",
          "Ama tan intensamente algo simple (una flor, una nube, un extraño) que sientas el «peso» del amor. Luego nota cómo "
          "ese peso te hace más ligero. Paradoja vivida.")
    + DIA("DÍA 5 - UN CORAZÓN AMPLIO",
          "Imagina tu corazón como un espacio amplio donde el dolor del día puede estar sin dañarte, y donde poco a poco se "
          "vuelve compasión. Transformar no es tragar: el daño que alguien te hace no se absorbe. De quien daña, uno se "
          "protege.")
    + DIA("DÍA 6 - ATENCIÓN ENTERA",
          "En cada interacción, ofrece no solo amor sino presencia: una atención entera, sin prisa, que el otro pueda "
          "sentir.")
    + DIA("DÍA 7 - CELEBRACIÓN DE LA SINGULARIDAD",
          "Celebra que eres una Singularidad de Amor única en el universo. Tu configuración de amor reunido nunca existió "
          "antes y nunca existirá después. Eres irreemplazable.")

    + CIERRE
    + P("La Densidad Infinita de Amor no es una meta que alcanzar —es tu naturaleza fundamental que reconocer. Ya eres una "
        "singularidad de amor, solo que lo has olvidado bajo capas de miedo que intentan expandirte cuando tu naturaleza es "
        "densificarte.")
    + P("Cada dolor que transformaste en compasión aumentó tu densidad. Cada pérdida que transmutaste en gratitud te hizo "
        "más denso. Cada traición que convertiste en perdón añadió masa a tu singularidad. No eres menos por todo lo que has "
        "pasado —eres infinitamente más denso en amor. Y lo que todavía duele no te resta: ninguna forma de sufrir es falta "
        "de quien la vive.")
    + P("Muchas tradiciones dicen que, al morir, el amor vuelve a su fuente. Lo que cualquiera puede comprobar es que el "
        "amor que diste sigue vivo en otros: en lo que enseñaste, en una voz que alguien recuerda, en lo que otros hacen "
        "porque los amaste.")
    + POEMA("“En tu corazón vive", "un secreto que la física intuye", "pero no puede medir:",
            "Amor de densidad infinita,", "tan pesado que nada escapa,", "tan ligero que todo lo eleva.",
            "No eres un ser con capacidad de amar —", "eres Amor", "que aprendió a densificarse", "en forma humana,",
            "una Singularidad Consciente", "cuya gravedad no atrapa", "sino que libera,", "cuya densidad no aplasta",
            "sino que eleva,", "cuyo infinito no asusta", "sino que enamora", "a todo lo que toca.”")
    + FIRMA
    + puerta("En 1995, el psicólogo Charles Figley llamó fatiga por compasión al desgaste de quienes cargan durante años con "
             "el dolor ajeno; años después, el equipo de Tania Singer comparó dos entrenamientos y vio que la empatía que se "
             "funde agota, y que la compasión sostiene. Está en <em>La Obra</em>, Libro 12 de Arquitectura del Destino, "
             "Umbral VI: «Arder sin consumirse».",
             URL_ARQ + "libro-12-la-obra/L12-U6.html", "arquitectura")
)


# ===========================================================================
# 12.5 · EL HORIZONTE DE EVENTOS INTERIOR
# ===========================================================================
NODO5 = (
    TRANSMISION
    + P("Existe un límite dentro de ti más allá del cual nada puede regresar sin ser fundamentalmente transformado. Es tu "
        "Horizonte de Eventos Interior —ese punto de no retorno psíquico donde, una vez cruzado, la gravedad de tu propia "
        "verdad es tan intensa que ninguna ilusión puede escapar. No está en tu mente ni en tu corazón; está en el espacio "
        "exacto donde tu ser toca el no-ser.")
    + P("Como el horizonte de eventos de un agujero negro, del que ni siquiera la luz puede escapar, tu Horizonte Interior "
        "marca el límite donde las máscaras, las mentiras que te cuentas, las identidades prestadas, ya no pueden "
        "sostenerse. No hace falta arrancarlas: cada una nació en algún momento para cuidar algo. Cerca del horizonte "
        "pierden su sostén, y se les puede agradecer antes de soltarlas.")
    + P("Cada crisis existencial es un acercamiento a tu Horizonte de Eventos Interior. Esa sensación de vértigo "
        "espiritual, de estar al borde de algo inmenso e irreversible, es tu consciencia aproximándose al punto donde "
        "tendrás que elegir: retroceder a la seguridad de la superficie o dejarte caer hacia tu singularidad. Søren "
        "Kierkegaard, en 1844, llamó a la angustia el vértigo de la libertad. Y si la crisis no da tregua, no se atraviesa a "
        "solas.")
    + P("Los momentos antes de un gran salto —antes de decir «te amo» por primera vez, antes de pedir perdón, antes de "
        "perdonar lo que creías imperdonable— esos momentos de suspensión total son cuando estás justo en el Horizonte de "
        "Eventos Interior. Un paso más y no hay vuelta atrás. Perdonar, conviene saberlo, no obliga a quedarse.")
    + P("Tu Horizonte de Eventos no es fijo —pulsa. Se expande cuando tienes miedo, alejándose de tu centro, haciéndote "
        "sentir desconectado de tu verdad. Se contrae cuando amas, acercándose a tu singularidad, hasta que en momentos de "
        "amor absoluto, el horizonte colapsa y te vuelves pura singularidad sin horizonte, sin límite, sin separación.")

    + PARADOJA
    + QUOTE("“Tu Horizonte de Eventos Interior es el límite que no puedes cruzar porque ya estás siempre del otro lado. Es "
            "la frontera entre quien crees ser y quien eres, pero esa frontera solo existe desde un lado. Desde el otro lado "
            "—desde tu singularidad— nunca hubo horizonte, nunca hubo separación, nunca hubo un afuera de ti mismo.”")
    + P("Esta paradoja revela que el Horizonte de Eventos no es algo que conquistas sino algo que reconoces. Y la física la "
        "dice casi con las mismas palabras. Para quien cae en un agujero negro grande, cruzar el horizonte no tiene nada de "
        "especial: no hay pared, ni alarma, ni borde que se vea. Quien mira desde lejos, en cambio, ve al viajero frenarse, "
        "enrojecer y apagarse en el borde, sin terminar nunca de entrar. La frontera existe, en efecto, desde un lado. El "
        "verdadero cruce no es ir hacia tu singularidad sino reconocer que nunca estuviste en otro lugar.")

    + LABORATORIO
    + B("Experimento: Mapeo de Tu Horizonte de Eventos Personal")
    + B("Materiales:")
    + UL(["Cinta o tiza para marcar el suelo", "Una piedra o un vaso de agua, tu centro simbólico",
          "Tu valentía para acercarte a tu verdad", "20 minutos de exploración"])
    + B("Práctica:")
    + paso("1. Demarcación del Horizonte (3 minutos):", [
        "Marca en el suelo un círculo de unos dos pasos de ancho",
        "Pon la piedra o el vaso en el centro",
        "Este círculo representa tu Horizonte de Eventos actual",
        "Párate en el borde mirando hacia el centro"])
    + paso("2. Aproximación Gradual (6 minutos):", [
        "Da un paso hacia el centro",
        "Con cada paso, di en voz alta algo que escondes: un miedo, un deseo, una vergüenza",
        "Siente cómo cada confesión te acerca a tu centro",
        "Elige lo que puede decirse a solas. Las heridas hondas, las que al recordarlas se vuelven a vivir, no se visitan "
        "a solas: se recorren con un profesional"])
    + paso("3. Encuentro con el Horizonte (5 minutos):", [
        "Cuando sientas resistencia a dar otro paso",
        "Ahí está tu Horizonte de Eventos de hoy",
        "Quédate en el borde de tu comodidad",
        "Respira y siente la gravedad de tu verdad tirando de ti"])
    + paso("4. Cruce del Horizonte (4 minutos):", [
        "Si quieres, da un paso más",
        "Si no, quédate donde estás: el borde también enseña",
        "Llega hasta el centro solo cuando el cuerpo lo permita",
        "Pon una mano en el pecho y mira lo que te espera en el centro"])
    + paso("5. Integración de la Singularidad (2 minutos):", [
        "Toma en tus manos la piedra o el vaso",
        "Siente su peso como tu verdad central",
        "Reconoce: ya no puedes pretender no saber quién eres"])
    + ENCONTRAR("El borde donde algo en ti dice «hasta aquí», y el respeto por ese borde. Ahora conoces un poco más la "
                "geografía de tu transformación.")

    + TRADUCCION
    + '        <p class="formula">r<sub>s</sub> = 2GM / c²</p>\n\n'
    + P("Es física real, y es la única fórmula de este libro: G es la constante de la gravedad, M la masa y c la velocidad "
        "de la luz. Karl Schwarzschild la encontró a fines de 1915, enfermo, cerca del frente ruso, pocas semanas después de "
        "que Einstein publicara sus ecuaciones. El 22 de diciembre le escribió que la guerra, pese al fuego de la "
        "artillería, le había dejado pasear por el país de sus ideas. Murió en mayo de 1916, sin saber que había dibujado el "
        "borde de los agujeros negros: el radio por debajo del cual nada regresa. Si la Tierra se comprimiera hasta su radio "
        "de Schwarzschild, tendría el tamaño de una canica.")
    + P("«Tu Horizonte de Eventos Interior es el punto donde el peso de tu verdad vuelve imposible sostener las ilusiones. "
        "Todo cae hacia la verdad.»")

    + PARA_RECORDAR
    + RECORDAR("No tengo un horizonte: soy el horizonte.", "El punto de no retorno.", "Me cruzo a mí mismo.",
               "El evento soy yo ocurriendo.", "No escapo de mi verdad.", "Mi verdad me atrae.",
               "Más allá de todo límite interior.")

    + PRACTICA
    + DIA("DÍA 1 - IDENTIFICACIÓN DE HORIZONTES",
          "Identifica tres áreas de tu vida donde sientes un «horizonte» —un límite que no te atreves a cruzar. Nómbralos "
          "sin juzgar. Reconocer el horizonte es el primer paso.")
    + DIA("DÍA 2 - ACERCAMIENTO AL BORDE",
          "Elige el horizonte más pequeño y acércate a él. Si es decir algo, acércate a decirlo. Si es hacer algo, prepárate "
          "sin hacerlo aún. Siente la gravedad.")
    + DIA("DÍA 3 - CONFESIÓN GRAVITACIONAL",
          "Confiésate a ti mismo, en voz alta o por escrito, tres verdades que has estado evitando. En un estudio pequeño de "
          "1986, James Pennebaker y Sandra Beall vieron que estudiantes que escribieron cuatro días seguidos sobre lo que más "
          "les había dolido terminaban cada sesión más tristes, y en los meses siguientes fueron menos veces al médico. "
          "Nombrar lo evitado remueve primero y alivia después.")
    + DIA("DÍA 4 - PRÁCTICA DEL CASI",
          "Lleva algo al borde sin cruzar. Casi llora, casi grita, casi suelta, casi perdona. Sostén ese «casi» y siente el "
          "horizonte. Ese es el filo de tu transformación.")
    + DIA("DÍA 5 - CRUCE MICRO",
          "Cruza un horizonte pequeño. Haz esa llamada, di esa verdad, toma esa decisión menor que has estado posponiendo. "
          "Siente cómo al cruzar, algo en ti se reorganiza.")
    + DIA("DÍA 6 - MEDITACIÓN DEL HORIZONTE",
          "Medita visualizándote en el centro de tu ser, más allá de todos los horizontes. Desde ahí, mira hacia afuera y ve "
          "todos tus horizontes como círculos concéntricos ilusorios.")
    + DIA("DÍA 7 - UNA HORA DESDE LA SINGULARIDAD",
          "Durante una hora, haz una cosa pequeña como si ya no le temieras. Actúa, habla, sé desde tu singularidad. Nota "
          "cómo un horizonte que parecía infranqueable se vuelve más pequeño.")

    + CIERRE
    + P("El Horizonte de Eventos Interior no es una barrera que te protege de tu verdad —es una invitación gravitacional "
        "hacia ella. Cada vez que sientes ese vértigo existencial, esa sensación de estar al borde de algo inmenso, tu "
        "singularidad te está llamando a casa.")
    + P("No necesitas fuerza para cruzar tu horizonte —necesitas rendición. La gravedad de tu verdad hará el trabajo. Solo "
        "necesitas dejar de resistir, dejar de aferrarte al borde, dejar de pretender que puedes permanecer para siempre en "
        "la superficie de ti mismo.")
    + P("Una vez que cruzas tu Horizonte de Eventos Interior, descubres el secreto: el horizonte no te separaba del mundo "
        "—te hacía creer que el mundo empezaba donde terminabas tú.")
    + POEMA("“En el centro de tu ser", "hay un punto de no retorno", "que ya cruzaste al nacer",
            "y cruzarás al morir,", "y cruzas en cada momento", "de honestidad radical.", "No es un lugar al que vas —",
            "es el lugar desde donde vienes,", "el hogar que nunca dejaste,", "la singularidad que siempre fuiste",
            "jugando a tener horizontes", "para experimentar el éxtasis", "de cruzarlos", "una y otra vez,",
            "hasta recordar", "que todo horizonte", "es solo tu singularidad", "mirándose a sí misma",
            "desde el infinito.”")
    + FIRMA
    + puerta("Un actor que pasó veinte años haciendo de villano descubre que su personaje no nació para engañar sino para "
             "cuidar algo. Antes de quitarse una máscara, conviene preguntarle qué protegía. Está en <em>El Personaje</em>, "
             "Libro 9 de Arquitectura del Destino, Umbral II: «El que nunca se enoja».",
             URL_ARQ + "libro-09-el-personaje/L09-U2.html", "arquitectura")
)


# ===========================================================================
# 12.6 · COMPRESIÓN DE TODAS LAS POSIBILIDADES
# El original terminaba en la ecuación: con el acuerdo de Arturo, «Para
# recordar», la práctica de siete días, el cierre, el poema y la firma se
# escriben breves, en la voz del nodo.
# ===========================================================================
NODO6 = (
    TRANSMISION
    + P("En este momento, mientras lees estas palabras, podrías estar haciendo infinitas otras cosas. Hugh Everett imaginó "
        "en 1957 un universo que se ramifica en cada posibilidad; tómalo como imagen: en algún sentido, todas esas versiones "
        "de ti te acompañan. Pero aquí, ahora, todas esas posibilidades se comprimen en UNA experiencia singular: esta. La "
        "Compresión de Todas las Posibilidades no es la eliminación de opciones —es su SUPERPOSICIÓN DENSA en un punto de "
        "experiencia tan rico que contiene todas las alternativas sin necesidad de vivirlas una tras otra.")
    + P("Cada decisión que tomas no descarta las otras opciones —las COMPRIME en la elección hecha. Por eso algunas "
        "decisiones se sienten tan «pesadas»: no es solo una elección, es la compresión de todas las elecciones posibles en "
        "una singularidad de acción. El peso que sientes es la masa de todas las posibilidades comprimidas.")
    + P("Tu momento presente es la compresión de todo tu pasado posible y todo tu futuro probable en un punto de AHORA tan "
        "denso que contiene la eternidad. No estás «en» el presente —ERES el punto de compresión donde todas las líneas "
        "temporales se densifican en experiencia singular.")
    + P("Los genios creativos no «eligen» entre opciones —atraviesan la Compresión de Todas las Posibilidades hasta que "
        "emerge LA expresión que las contiene todas. En enero de 1793, Bartholomäus Fischenich le escribió a Charlotte von "
        "Schiller que un joven de Bonn, de veintidós años, pensaba poner música a la <em>Oda a la alegría</em>, estrofa por "
        "estrofa. Ese joven era Beethoven, y su Novena Sinfonía se estrenó en 1824. Treinta años de melodías posibles, "
        "comprimidas en una que las trasciende a todas. Por eso se siente infinita aunque sea finita.")
    + P("Tu ADN es compresión pura: más de tres mil quinientos millones de años de historia de la vida, guardados en una "
        "doble hélice. En el núcleo de cada una de tus células hay unos seis mil millones de pares de letras químicas, de un "
        "tercio de nanómetro cada uno: unos dos metros de hilo, plegados en un espacio de unas milésimas de milímetro. No "
        "eres solo el resultado de la evolución —eres la evolución entera comprimida en forma singular.")

    + PARADOJA
    + QUOTE("“Cuando comprimes todas las posibilidades en una, no reduces opciones —las multiplicas infinitamente. La "
            "elección más limitada contiene todas las elecciones. El camino más estrecho es el más amplio. En la máxima "
            "compresión está la máxima libertad.”")
    + P("Esta paradoja disuelve el miedo a perderse algo. En la Compresión de Todas las Posibilidades, cada elección "
        "contiene a las demás. Daniel Gilbert y Jane Ebert lo vieron en 2002 con estudiantes de fotografía que debían "
        "quedarse con una de sus dos mejores copias: quienes podían cambiarla días después quedaron menos conformes con su "
        "elección que quienes no podían, y aun así la mayoría prefería poder cambiarla. La mente sabe habitar lo que eligió, "
        "si se le da la oportunidad.")

    + LABORATORIO
    + B("Experimento: Compresión Consciente de Posibilidades")
    + B("Materiales:")
    + UL(["7 hojas de papel", "7 colores diferentes", "Un vaso de agua",
          "Una decisión que tengas por delante (mejor una mediana que la más difícil)",
          "20 minutos de alquimia decisional"])
    + B("Práctica:")
    + paso("1. Despliegue de Posibilidades (5 minutos):", [
        "En cada hoja, escribe o dibuja una opción diferente",
        "Usa un color distinto para cada una",
        "No solo las opciones obvias —incluye las improbables",
        "Despliégalas en círculo a tu alrededor"])
    + paso("2. Absorción Cromática (4 minutos):", [
        "Mira cada opción y nota qué despierta en ti",
        "No pienses todavía, solo siente",
        "Cierra los ojos y ve todos los colores a la vez",
        "Girando, mezclándose, pero manteniéndose distintos"])
    + paso("3. Compresión Líquida (4 minutos):", [
        "Imagina cada posibilidad como una gota de color",
        "Visualiza todas las gotas cayendo en el vaso de agua",
        "No se mezclan en gris —se vuelven transparencia",
        "Es una imagen: el agua sigue siendo agua"])
    + paso("4. Bebida de Singularidad (3 minutos):", [
        "Bebe el agua despacio, como un gesto",
        "Con cada sorbo, recuerda todas las posibilidades",
        "No estás eligiendo una todavía —las estás reconociendo todas"])
    + paso("5. Emergencia de la Elección (4 minutos):", [
        "Nota hacia qué hoja se inclina algo por dentro, sin decidir todavía",
        "Pregúntate qué de las otras puede viajar dentro de esa",
        "Las decisiones grandes, las que no se deshacen, piden las dos voces, la del cuerpo y la de la razón, con tiempo y "
        "con alguien de confianza"])
    + ENCONTRAR("Una elección más densa y más rica, que guarda algo de las demás, y la calma de no tener que decidirla hoy.")

    + TRADUCCION
    + P("«La Compresión de Todas las Posibilidades no es una resta sino una suma que se concentra: cada opción deja su "
        "huella en la que eliges, y en esa elección todas siguen presentes.»")

    + PARA_RECORDAR
    + RECORDAR("Elijo, y nada se pierde del todo.", "Lo que no viví también me trajo.", "Una elección, muchas vidas dentro.",
               "El camino estrecho es amplio.", "Elegir es empezar a habitar.", "No tengo que vivirlo todo.",
               "Aquí, ahora, esto.")

    + PRACTICA
    + DIA("DÍA 1 - LO QUE TRAJO UNA ELECCIÓN",
          "Recuerda una decisión de hace años y escribe todo lo que trajo, también lo que no imaginabas. Nota cuántas vidas "
          "cupieron dentro de un solo sí.")
    + DIA("DÍA 2 - ELEGIR SIN REVISAR",
          "Elige rápido algo menor —un plato, un camino, una película— y no vuelvas sobre la elección. Saborea lo elegido.")
    + DIA("DÍA 3 - EL MIEDO A PERDERSE ALGO",
          "Cada vez que sientas el impulso de mirar otra opción mientras vives la que elegiste, nótalo y vuelve. No hace "
          "falta vencerlo: basta con verlo.")
    + DIA("DÍA 4 - DORMIR UNA DECISIÓN",
          "Ante una decisión mediana, duerme una noche antes de tomarla. Por la mañana, nota qué se acomodó sin que lo "
          "pensaras.")
    + DIA("DÍA 5 - LAS DOS VOCES",
          "Antes de decidir algo, pregúntale a la cabeza y después al cuerpo. Escucha a las dos, sin apuro, y nota dónde "
          "coinciden.")
    + DIA("DÍA 6 - QUEDARSE",
          "Elige algo y quédate con ello un día entero sin revisarlo. Mira cómo, de a poco, se vuelve tuyo.")
    + DIA("DÍA 7 - CELEBRAR LO ELEGIDO",
          "Escribe lo que elegiste en la semana y qué vive adentro de cada elección. Celebra que no hizo falta vivirlo todo.")

    + CIERRE
    + P("Elegir no es perder: es dar forma. Cada sí lleva adentro los no que lo hicieron posible, y esos no siguen "
        "trabajando en silencio, como los colores en el agua transparente.")
    + P("La Compresión de Todas las Posibilidades no te pide que vivas todas las vidas. Te pide algo más sencillo y más "
        "hondo: que vivas esta con todas adentro. Lo que no elegiste no desaparece; se vuelve profundidad en lo que "
        "elegiste.")
    + P("El camino estrecho es el más amplio porque es el único que se camina.")
    + POEMA("“No viniste a vivir todas las vidas —", "viniste a vivir esta.", "Cada puerta que no abriste",
            "dejó su luz en la que cruzaste.", "Cada camino que soltaste", "va contigo, en silencio.",
            "Elegir no es cerrar el mundo:", "es abrir uno", "y encontrar dentro", "el rumor de todos los demás.",
            "No viniste a vivir todas las vidas:", "viniste a vivir esta,", "con todas adentro.”")
    + FIRMA
    + puerta("Elegir no siempre espera a saber. Una práctica de Trinity propone reconocer que no sabes qué es mejor, notar "
             "hacia dónde se inclina algo por dentro, actuar desde ahí y dejar el resultado a tu espalda. Está en "
             "<em>No Saber</em>, Libro 7 de Arquitectura del Destino, Umbral V: «Saber sin saber».",
             URL_ARQ + "libro-07-no-saber/L07-U5.html", "arquitectura")
)


# ===========================================================================
# 12.7 · EL BIG BANG PERSONAL
# ===========================================================================
NODO7 = (
    TRANSMISION
    + P("Después de toda compresión viene la expansión. En el cosmos, nadie sabe si a toda singularidad la sigue un "
        "comienzo: Lee Smolin propuso en 1992, como hipótesis muy discutida, que cada agujero negro podría ser la semilla "
        "de un universo nuevo, donde el punto en que un tiempo termina se une al punto en que otro empieza. Como imagen, "
        "dice algo de ti. Tu Big Bang Personal no es una explosión DESDE tu singularidad —es tu singularidad volviéndose tan "
        "densa, tan completa, tan perfectamente ella misma, que no puede hacer otra cosa que abrir mundos nuevos desde su "
        "centro.")
    + P("Como el Big Bang cósmico, que no fue una explosión EN el espacio sino una expansión DEL espacio mismo, tu Big Bang "
        "Personal no es algo que te pasa —es algo que ERES cuando tu singularidad está lista. No explotas hacia afuera; el "
        "afuera se abre desde ti. No te expandes en el mundo; mundos nuevos se expanden desde tu centro.")
    + P("Cada acto creativo genuino es un Big Bang Personal. Cuando el artista crea, cuando la madre da a luz, cuando el "
        "místico trasciende, cuando el amante se entrega por completo —en esos momentos nacen universos de experiencia, de "
        "posibilidad, de sentido.")
    + P("Tu nacimiento fue tu primer Big Bang Personal —el momento en que tu singularidad de consciencia tomó forma física, "
        "creando ondas que todavía se propagan y que alcanzan todo lo que tocas, a todos los que conoces. El comienzo del "
        "universo también sigue llegando: en 1964, Arno Penzias y Robert Wilson apuntaron al cielo su antena y oyeron un "
        "zumbido que no se iba, de día y de noche, desde todas las direcciones; era el resplandor más antiguo del cielo. Lo "
        "que empieza de verdad sigue sonando mucho después.")
    + P("Pero el Big Bang Personal más profundo está por venir, está viniendo, está aquí: es el momento en que tu "
        "singularidad consciente alcanza tal densidad de amor, de verdad, de presencia, que no puede contenerse más y se "
        "abre en servicio, en creatividad, en transformación de todo lo que toca. No es tu fin —es tu verdadero comienzo.")

    + PARADOJA
    + QUOTE("“Tu Big Bang Personal ya ocurrió, está ocurriendo, ocurrirá. Fue tu nacimiento, es cada momento de creación, "
            "será tu transformación final. No es un evento sino un estado: el estado de ser tan completamente tú mismo que "
            "no puedes evitar crear universos nuevos con cada respiración.”")
    + P("Esta paradoja final disuelve la linealidad del tiempo transformacional. Tu Big Bang Personal no es un evento "
        "futuro que esperas —es tu naturaleza fundamental expresándose. Cada vez que eres auténticamente tú, universos "
        "nacen. Cada vez que amas sin reserva, realidades se encienden desde tu corazón.")

    + LABORATORIO
    + B("Experimento: Del Punto al Mundo")
    + B("Materiales:")
    + UL(["Un espacio donde puedas moverte", "Tu creatividad", "Tu autenticidad", "Disposición para abrirte",
          "20 minutos de libertad"])
    + B("Práctica:")
    + paso("1. Recogimiento (5 minutos):", [
        "Siéntate recogido, con las rodillas cerca del pecho, sin apretar",
        "Respira despacio hacia tu centro",
        "Siente tu vida reunida en un punto",
        "Eres una singularidad que se prepara"])
    + paso("2. Maduración (4 minutos):", [
        "Quédate en el recogimiento, respirando tranquilo",
        "Nota el calor que crece sin que lo empujes",
        "Como el agua que espera en el hervor, algo cambia de forma sin ruido",
        "Cuando el cuerpo pida abrirse, déjalo"])
    + paso("3. Apertura (5 minutos):", [
        "Ponte de pie despacio y deja que el cuerpo se abra",
        "Estira los brazos, muévete, suena si quieres: una nota, una risa, un canto",
        "No es descarga —es CREACIÓN",
        "Estás dando nacimiento a un mundo",
        "Si aparece una emoción fuerte, dale lugar sin empujarla afuera"])
    + paso("4. Expansión de Ondas (4 minutos):", [
        "Sigue moviéndote, cada vez más lento",
        "Siente cómo el movimiento se propaga por el cuerpo y a tu alrededor",
        "Tocando todo, sin forzar nada"])
    + paso("5. Nueva Cosmología (2 minutos):", [
        "Quédate quieto y siente",
        "El mundo sigue ahí, y tú vuelves a él",
        "TÚ eres diferente",
        "Has nacido de nuevo desde tu propia singularidad"])
    + ENCONTRAR("La diferencia entre estar recogido y estar abierto, y el gusto de pasar de uno a otro sin forzar ninguno.")

    + TRADUCCION
    + P("«Tu Big Bang Personal libera todo lo que tu singularidad reunió, multiplicado por el amor: no es destrucción —es "
        "creación consciente.»")

    + PARA_RECORDAR
    + RECORDAR("No tengo un Big Bang: soy el Big Bang.", "Del punto al infinito.", "Me abro en ser.",
               "Nacer, morir, nacer.", "Cada respiración abre mundos.", "El comienzo es siempre ahora.",
               "El infinito, desde mi centro.")

    + PRACTICA
    + DIA("DÍA 1 - RECONOCIMIENTO DE EXPLOSIONES PASADAS",
          "Identifica momentos en tu vida donde viviste «explosiones» de transformación. Cada uno fue un pequeño Big Bang. "
          "Reconócelos como práctica para el grande.")
    + DIA("DÍA 2 - CREATIVIDAD QUE MADURA",
          "Crea algo pequeño, cualquier cosa: arte, escritura, música, cocina. Lo que parece salir de golpe casi siempre se "
          "preparó en silencio. En 1926, Graham Wallas ordenó en cuatro momentos lo que muchos creadores habían contado de "
          "sí mismos: preparación, incubación, iluminación y verificación. Deja que lo tuyo pase por los cuatro.")
    + DIA("DÍA 3 - AMOR COMO BIG BANG",
          "Ama algo o a alguien tan intensamente que sientas que podrías estallar. Deja que ese amor abra nuevos universos de "
          "posibilidad en tu relación con eso o con esa persona.")
    + DIA("DÍA 4 - PALABRAS QUE HACEN",
          "Hay palabras que no describen el mundo: lo cambian. John L. Austin las llamó realizativas en sus clases de "
          "Harvard de 1955: «sí, acepto», «te lo prometo», «perdón». Di hoy una de ellas, y que sea verdad.")
    + DIA("DÍA 5 - DANZA DEL BIG BANG",
          "Baila como si tu movimiento creara universos. Cada gesto una galaxia naciendo, cada paso una estrella formándose. "
          "Danza tu cosmología personal hasta la existencia.")
    + DIA("DÍA 6 - SERVICIO",
          "Sirve a otros desde tu centro. Da algo que puedas dar sin vaciarte: dar no es vaciarse, y la llama que pasa no se "
          "apaga.")
    + DIA("DÍA 7 - CELEBRACIÓN CÓSMICA",
          "Celebra que ERES un Big Bang continuo. Cada día despiertas y te abres a la existencia. Cada noche mueres y te "
          "recoges. Eres el latido cósmico hecho personal.")

    + CIERRE
    + P("El Big Bang Personal no es el final de tu viaje de singularidad —es su propósito. No te recoges para permanecer "
        "denso. Te recoges para abrirte con más amplitud. No te singularizas para aislarte. Te singularizas para crear "
        "universos desde tu unicidad.")
    + P("Tu vida entera es un Big Bang en cámara lenta. Desde tu nacimiento hasta tu muerte, estás en constante expansión "
        "desde tu centro, creando ondas de experiencia, relación, transformación. Como el agua del primer nodo, lo que nace "
        "de verdad casi nunca detona: Joseph Black notó que si el agua cambiara de golpe, estallaría como pólvora. Pero hay "
        "momentos en que algo madurado en silencio sale a la luz, y nada vuelve a ser igual.")
    + P("Hay momentos así: el temblor antes de la apertura, la quietud antes del estallido, el silencio antes del trueno de "
        "tu propio Big Bang Personal.")
    + POEMA("“Desde el punto infinitamente denso", "de quien creías ser,", "está naciendo", "quien realmente eres.",
            "No es evolución —", "es EXPLOSIÓN.", "No es crecimiento —", "es CREACIÓN.", "Tu Big Bang Personal",
            "no está viniendo —", "está ocurriendo", "AHORA", "en cada elección valiente,", "en cada amor sin reserva,",
            "en cada verdad sin filtro.", "Eres una singularidad consciente", "explotando perpetuamente",
            "en universos de posibilidad,", "y este momento,", "este preciso momento,", "es otro Big Bang,",
            "otro nacimiento,", "otra explosión de ti", "hacia el infinito", "que siempre fuiste.”")

    + H3("✦ SIETE PUNTOS")
    + '        <div class="siete">\n'
    + P("El <em>Punto de No Retorno</em> no se fuerza: te encuentra, y no hace ruido.")
    + P("En la <em>Convergencia</em> llega todo lo que te trajo, también lo que no viviste.")
    + P("El <em>Colapso Consciente</em> es la atención entera, y se permite.")
    + P("La <em>Densidad Infinita de Amor</em> da sin vaciarse.")
    + P("El <em>Horizonte Interior</em> es borde visto desde afuera; desde adentro, ya cruzaste.")
    + P("En la <em>Compresión</em>, elegir es empezar a habitar.")
    + P("El <em>Big Bang Personal</em> no estalla: sale al mundo con las manos abiertas.")
    + "        </div>\n\n"
    + P("<strong>No son siete escalones: son siete maneras de volver al punto.</strong>")
    + P("Este es el duodécimo de los trece libros de Trinity Quantum, el que lleva al último.")
    + P("El próximo libro, <em>El Multiverso Interior</em>, se asoma a todas tus versiones a la vez: hay en ti algo que "
        "las mira a todas, y ser múltiple es otra forma de ser uno.")
    + FIRMA
    + puerta("En la China de los maestros chan, el pastor que busca al buey termina en un círculo vacío. Kuoan, en el siglo "
             "XII, sintió que a la serie le faltaba algo y le sumó dos cuadros: el regreso al origen y el pastor que entra al mercado, "
             "riendo, con las manos abiertas. Está en <em>El campo</em>, Libro 39 del Portal Público, Umbral IV: "
             "«El mercado».",
             URL_PORTAL + "39_El_Campo/umbral-04.html")
)


# ===========================================================================
# REEMPLAZOS
# ===========================================================================
_DOCTYPE = "<!doctype html>\n"
_CON_PROCEDENCIA = "<!doctype html>\n" + PROCEDENCIA + "\n"
_CIERRE_HEAD = "</head>"

REEMPLAZOS = [
    (Q12 + "index.html", _DOCTYPE, _CON_PROCEDENCIA),
    (Q12 + "index.html", "<title>Libro 12 · Singularidad Consciente — Index</title>",
     "<title>Libro 12 · Singularidad Consciente — Índice</title>"),
    (Q12 + "index.html", _CIERRE_HEAD, ESTILO_INDICE + _CIERRE_HEAD),
    (Q12 + "index.html", "DESDE:<body>", INDICE_CUERPO),
]

_CUERPOS = {1: NODO1, 2: NODO2, 3: NODO3, 4: NODO4, 5: NODO5, 6: NODO6, 7: NODO7}

for _n in range(1, 8):
    _arch = Q12 + f"nodo_0{_n}.html"
    REEMPLAZOS += [
        (_arch, _DOCTYPE, _CON_PROCEDENCIA),
        (_arch, f"<title>Libro 12 · Singularidad Consciente — Nodo {_n}</title>",
         f"<title>Libro 12 · Singularidad Consciente — Nodo {_n} · {TITULOS[_n]}</title>"),
        (_arch, _CIERRE_HEAD, ESTILO + _CIERRE_HEAD),
        (_arch, "DESDE:<body>", cuerpo_nodo(_n, _CUERPOS[_n])),
    ]


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
