#!/usr/bin/env python3
"""
Depuración de Quantum 7, *Realidades Holofractales* (1 de noviembre de 2026),
el sexto de la revisión completa de Quantum, con el veto de Arturo en cada
tarjeta (7.0 a 7.7). Arturo aprobó todas las tarjetas y sugerencias, dejó a
criterio de Claude las puertas opcionales (se publican las del 7.2, 7.3 y 7.5;
el 7.1 queda sin puerta) y confirmó que el cierre diga que este es el séptimo
de trece libros, el centro de la serie.

Lo propio de este libro: el ropaje era la ciencia dada como prueba de poderes
(el universo que ES un holograma, el ADN reprogramable, el Akasha, el
centésimo mono, los saltos entre realidades). El libro obedece a su último
nodo («No la reconcilias. La habitas»), y la columna escondida es el punto de
vista: cada parte guarda el todo desde un ángulo que nadie más tiene.

Método (maestro v4, sección 5): cada reemplazo aprobado se aplica exactamente
una vez sobre el original de la etiqueta `quantum-original`. En los ocho
archivos se cambian la cabecera (nota de procedencia), el <head> (estilo de la
depuración) y el cuerpo, que se reemplaza desde la marca que abre los
metadatos hasta el final del archivo. En el nodo 1, la navegación superior ya
no apunta a un nodo 0 inexistente; en el nodo 7, lleva al Libro 8.

Uso:  python3 depurar_quantum7.py RUTA_A_UNA_COPIA_DEL_ORIGINAL
      (por ejemplo, el contenido de la etiqueta quantum-original, o el
      repositorio Trinity- si Libro_07 todavía no fue depurado)
"""
import sys
from pathlib import Path

Q7 = "02_Trinity_Quantum/Libro_07/"

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
       Letra más grande en el teléfono, firma, bloque fijo de las puertas
       y estilos mínimos para lo que la hoja común no cubre.
       ============================================================ */
    .node-content h3{
      margin: 1.3em 0 .45em;
      font-size: 1.06rem;
      color: var(--violet-light);
    }
    .node-content ol{
      margin: .6em 0 1em 1.4em;
      padding: 0;
    }
    .node-content ol li{ margin-bottom: 6px; }
    .node-content ol ul{ margin: .3em 0 .5em 1.1em; }
    .node-content blockquote{
      margin: 1em 0 1.1em;
      padding: 12px 16px;
      border-left: 2px solid var(--gold-soft);
      border-radius: 0 12px 12px 0;
      background: rgba(255, 255, 255, .025);
      font-style: italic;
    }
    .node-content blockquote p{ margin: 0; }
    .node-content .node-symbol{
      margin: 18px 0 4px;
      text-align: center;
      letter-spacing: .3em;
    }
    .node-content p.signature{
      margin: 22px 0 8px;
      color: rgba(243, 209, 122, .85);
      font-size: 14px;
      letter-spacing: .04em;
    }
    .node-content p.verso{
      margin: 18px 0;
      text-align: center;
      color: var(--gold-light);
      line-height: 1.8;
    }
    .puerta{
      margin: 30px 0 10px;
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
    .node-content .puerta .p-nombre{
      margin: 0 0 6px;
      font-size: 15px;
      font-style: italic;
      letter-spacing: .06em;
      color: var(--p-acento);
    }
    .node-content .puerta .p-texto{
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
      .node-content p, .node-content li{ font-size: 18px; line-height: 1.7; }
      .node-content p.signature{ font-size: 15px; }
      .puerta{ padding: 16px 16px 14px; }
    }
    @media (prefers-reduced-motion: reduce){
      .puerta .cruzar{ transition: none; }
    }
  </style>
"""

ESTILO_INDICE = """  <style>
    /* Depuración · noviembre 2026: letra más grande en el teléfono y firma. */
    .node-content h3{ margin: 1.1em 0 .3em; font-size: 1.04rem; }
    .node-content p.signature{
      margin: 22px 0 8px;
      color: rgba(243, 209, 122, .85);
      font-size: 14px;
      letter-spacing: .04em;
    }
    @media (max-width: 640px){
      .node-content p, .node-content li{ font-size: 18px; line-height: 1.7; }
      .node-content p.signature{ font-size: 15px; }
    }
  </style>
"""

FIRMA = '        <p class="signature"><strong>— Trinity Quantum · Realidades Holofractales</strong></p>\n'

TITULOS = {
    1: "El Todo en Cada Parte",
    2: "Navegando Entre Escalas de Magnitud",
    3: "Campos Morfogenéticos: La Memoria del Holofractal",
    4: "La Ilusión del Yo Separado",
    5: "Co-creación Consciente con el Todo",
    6: "Portales Entre Realidades Paralelas",
    7: "Viviendo la Paradoja: Infinito Siendo Finito",
}

# Nombres para la navegación y el pie, más cortos donde el título es largo.
CORTOS = dict(TITULOS)
CORTOS[2] = "Entre Escalas"
CORTOS[3] = "Campos Morfogenéticos"
CORTOS[5] = "Co-creación"
CORTOS[6] = "Portales Entre Realidades"
CORTOS[7] = "Viviendo la Paradoja"

H1_ESTILO = ' style="color:#d4af37; text-shadow: 0 0 18px rgba(212,175,55,0.18);"'


# ---------------------------------------------------------------------------
# Piezas que se repiten
# ---------------------------------------------------------------------------
def P(texto):
    return f"        <p>{texto}</p>\n"


def H2(texto):
    return f"        <h2>{texto}</h2>\n\n"


def H3(texto):
    return f"\n        <h3>{texto}</h3>\n"


def lista(items):
    filas = "\n".join(f"          <li>{x}</li>" for x in items)
    return f"        <ul>\n{filas}\n        </ul>\n"


def pasos(items):
    filas = "\n".join(f"          <li>{x}</li>" for x in items)
    return f"        <ol>\n{filas}\n        </ol>\n"


def fase(titulo, items):
    return P(f"<strong>{titulo}</strong>") + lista(items)


def cita(texto):
    return f"        <blockquote>\n          <p>{texto}</p>\n        </blockquote>\n"


def verso(lineas):
    cuerpo = "<br />\n          ".join(lineas)
    return f'        <p class="verso">{cuerpo}</p>\n'


def simbolo(s):
    return f'        <p class="node-symbol">{s}</p>\n'


def puerta(texto, url, clase="portal"):
    destino = "Arquitectura del Destino" if clase == "arquitectura" else "el Portal Público"
    return (
        f'        <aside class="puerta {clase}" aria-label="Puerta hacia {destino}">\n'
        '          <p class="p-nombre">Puerta</p>\n'
        f'          <p class="p-texto">{texto}</p>\n'
        f'          <a class="cruzar" href="{url}">Cruzar ⟶</a>\n'
        "        </aside>\n"
    )


def meta(n, subtitulo):
    return (
        "      <!-- Meta del nodo -->\n"
        '      <section class="node-meta">\n'
        '        <div class="node-book-title">Libro 7 · Realidades Holofractales</div>\n'
        f'        <h1 class="node-heading"{H1_ESTILO}>Nodo {n}: {TITULOS[n]}</h1>\n'
        f'        <div class="node-index">Nodo {n} de 7 · {subtitulo}</div>\n'
        "      </section>\n\n"
        "      <!-- Contenido -->\n"
        '      <main class="node-content">\n\n'
    )


def preparacion(n, texto, pregunta, simbolos):
    return (
        H3(f"Preparación para el Nodo {n}")
        + P(texto)
        + P(f"<strong>La pregunta que llevaremos:</strong> <em>{pregunta}</em>")
        + simbolo(simbolos)
        + "\n"
    )


def cierre(n, subpie):
    ant = (f"nodo_0{n-1}.html", f"← Nodo {n-1}: {CORTOS[n-1]}") if n > 1 else ("index.html", "← Índice del Libro")
    sig = (f"nodo_0{n+1}.html", f"Nodo {n+1}: {CORTOS[n+1]} →") if n < 7 else ("../Libro_08/index.html", "Libro 8: Plasma Consciente →")
    return (
        "\n      </main>\n\n"
        "      <!-- Navegación Inferior -->\n"
        '      <div class="node-nav node-nav-bottom">\n'
        '        <div class="node-nav-group">\n'
        f'          <a href="{ant[0]}" class="nav-link">{ant[1]}</a>\n'
        f'          <a href="{sig[0]}" class="nav-link">{sig[1]}</a>\n'
        "        </div>\n"
        '        <div class="node-nav-group">\n'
        '          <a href="index.html" class="nav-link">Volver al Índice</a>\n'
        '          <a href="../index.html" class="nav-link">Portal Maestro</a>\n'
        "        </div>\n"
        "      </div>\n\n"
        "      <!-- Firma -->\n"
        '      <footer class="portal-footer">\n'
        '        <div class="footer-line">TRINITY QUANTUM · Libro 7 · Realidades Holofractales</div>\n'
        f'        <div class="footer-subline">Nodo {n}: {CORTOS[n]} · {subpie}</div>\n'
        '        <div class="footer-sigil">🌀⟡🌀</div>\n'
        "      </footer>\n\n"
        "    </div>\n"
        "  </div>\n"
        "</body>\n"
        "</html>\n"
    )


# ===========================================================================
# 7.0 · Índice
# ===========================================================================
_BAJADAS = [
    "Cada pedazo guarda la escena entera, desde su propia ventana.",
    "Del protón a las galaxias: cada tamaño tiene sus leyes y sus regalos.",
    "Lo que se hizo una vez cuesta menos la siguiente, y viaja por la cercanía.",
    "El yo se pone como ropa; quien se la quita sigue aquí.",
    "Nadie mira desde tu lugar: por eso tu parte hace falta.",
    "Muchas vidas posibles, y una mirada que elige.",
    "Después de ver el todo, lavar los platos.",
]

_LISTA_INDICE = "".join(
    f'            <h3><a href="nodo_0{n}.html" class="nav-link">Nodo {n}: {TITULOS[n]}</a></h3>\n'
    f"            <p>{_BAJADAS[n-1]}</p>\n\n"
    for n in range(1, 8)
)

INDICE_CUERPO = (
    """      <!-- Meta del libro -->
      <section class="node-meta">
        <div class="node-book-title">Libro 7 · Realidades Holofractales</div>
        <h1 class="node-heading" style="color:#d4af37; text-shadow: 0 0 18px rgba(212,175,55,0.18);">
          Los 7 Nodos del Portal
        </h1>
        <div class="node-index">La parte · Las escalas · La memoria · El yo · La obra · Las posibilidades · La paradoja</div>
      </section>

      <!-- Contenido -->
      <main class="node-content">

        <section class="node-section">
          <h2>El Todo desde Aquí</h2>

          <p>Cada parte guarda el todo desde un ángulo que nadie más tiene. Tú eres uno de esos ángulos: por eso nadie puede mirar por ti.</p>

          <p><em>Holofractal</em> es la imagen de este libro. Junta dos hallazgos: el holograma, donde cada pedazo guarda la escena entera, y el fractal, donde la misma forma vuelve en cada escala. Aquí la palabra no describe la física del universo: nombra una manera de mirar.</p>

          <p>En 1714, Gottfried Leibniz lo explicó con una ciudad. Mirada desde distintos lados, parece cada vez otra, y sin embargo es una sola. Así, pensaba, cada ser refleja el mismo universo desde su punto de vista, y la multitud de perspectivas no lo divide: lo multiplica.</p>

          <p>Cada nodo es un ángulo: la parte, la escala, la memoria, el yo, la obra, las posibilidades y, al final, la vida de todos los días, donde todo eso se habita.</p>
        </section>

        <hr />

        <!-- Lista de Nodos -->
        <section class="node-section">
          <h2>Nodos del Libro 7</h2>

          <div style="margin-top: 18px;">
"""
    + _LISTA_INDICE
    + """          </div>
        </section>

        <hr />

        <!-- Cierre del Índice -->
        <section class="node-section">
          <h2>Antes de Empezar</h2>
          <p><em>Realidades Holofractales no es una teoría para creer, sino un ángulo para habitar. Si sientes el llamado, comienza por el Nodo 1. Si ya hay una pregunta esperándote, entra por el Nodo que la nombre.</em></p>
          <p class="signature"><strong>— Trinity Quantum · Realidades Holofractales</strong></p>
        </section>

      </main>

      <!-- NAV -->
      <nav class="node-nav">
        <div class="node-nav-group">
          <a class="nav-link nav-link-main" href="../index.html">
            ← Volver al Portal Maestro Trinity Quantum
          </a>
          <a class="nav-link" href="nodo_01.html">
            Comenzar · Nodo 1 →
          </a>
        </div>
      </nav>

      <footer class="portal-footer">
        <div class="footer-line">TRINITY QUANTUM · Libro 7 · Realidades Holofractales</div>
        <div class="footer-subline">Índice: Cada Parte Contiene el Todo</div>
        <div class="footer-sigil">🌀⟡🌀</div>
      </footer>

    </div>
  </div>
</body>
</html>
"""
)

# ===========================================================================
# 7.1 · El Todo en Cada Parte (el título queda)
# ===========================================================================
NODO1_CUERPO = (
    meta(1, "La ventana")
    + H2("La Paradoja de la Completitud Fragmentada")
    + cita("Rompe un holograma en mil pedazos y cada fragmento contendrá la imagen completa, solo con menor resolución. Rompe la realidad en infinitos fragmentos y cada uno contendrá el universo entero, solo con diferente perspectiva. No eres una parte del todo: eres el todo expresándose como parte.")

    + H3("El Descubrimiento Holográfico")
    + P("Dennis Gabor inventó la holografía en 1947, mientras buscaba una manera de ver más con el microscopio electrónico, y por ella recibió el Nobel de Física en 1971.")
    + P("<strong>Un holograma tiene propiedades que parecen imposibles:</strong>")
    + lista([
        "Cada parte guarda la escena entera",
        "La información no está en un lugar: está repartida",
        "Dañar una parte no borra la imagen: solo le quita nitidez",
        "La escena cambia según el ángulo desde donde se mira",
    ])
    + P("Si partes un holograma, cada pedazo muestra la escena completa, como a través de una ventana más pequeña. <strong>Como imagen, el universo es un holograma: cada lugar lo contiene entero, visto desde sí.</strong>")

    + H3("El Principio Holográfico Cosmológico")
    + P("A comienzos de los años setenta, Jacob Bekenstein descubrió algo asombroso sobre los agujeros negros: la información que pueden guardar crece con el área de su borde, no con su volumen. De ahí nació, en los años noventa, la idea de Gerard 't Hooft y Leonard Susskind: quizá toda la información de un volumen pueda escribirse en su frontera, como en un holograma.")
    + P("Si fuera así, el espacio que habitamos sería, en algún sentido, la proyección de lo que está escrito en un borde. Es una de las ideas más audaces de la física, y todavía se discute. <em>El universo podría ser más superficie de lo que parece.</em>")
    + P("Pero la imagen va más hondo…")

    + H3("Hologramas Fractales: Infinitud en Finitud")
    + P("Un fractal se parece a sí mismo en todas las escalas. Un holograma contiene el todo en cada parte. <strong>Un holofractal contiene el todo en cada parte, y en cada parte de esa parte, sin fin.</strong>")
    + P("Imagina:")
    + lista([
        "Un holograma donde cada punto contiene el holograma completo",
        "Que a su vez contiene puntos que contienen el holograma completo",
        "Y así, sin final",
    ])
    + P("Nadie ha visto un holofractal. Pero quien ha mirado de cerca una hoja de helecho, o una costa desde un avión, sabe que la forma vuelve cuando cambia la distancia.")

    + H3("El Todo en Cada Célula")
    + P("La biología encontró una versión de esta imagen que no necesita metáfora. Casi cada célula de tu cuerpo guarda el libro entero: el genoma completo con que se construyó todo el organismo, aunque lea solo algunas de sus páginas. Una célula de la piel y una neurona llevan las mismas instrucciones; lo que cambia es qué parte de ellas abren.")
    + P("En 1962, John Gurdon tomó el núcleo de una célula del intestino de un renacuajo y lo puso en un óvulo de rana al que le había quitado el suyo. De algunos de esos óvulos nacieron renacuajos normales. Una célula ya especializada guardaba todo lo necesario para hacer el animal entero. Medio siglo después, el hallazgo le valió el Nobel de Medicina.")
    + P("Y hay un animal que lo hace a la vista. En 1898, Thomas Hunt Morgan cortó en pedazos una planaria, un gusano plano de agua dulce, y vio que un fragmento de apenas 1/279 del animal podía volver a formar un gusano completo. <em>El todo en cada parte no es solo una imagen: a veces se lo puede ver crecer.</em>")
    + P("Al resto del genoma, el que no escribe proteínas, se lo llamó durante años «ADN basura». Hoy se sabe que una parte de ese material trabaja, con interruptores que encienden y apagan genes, y cuánto de él cumple una función sigue en discusión.")

    + H3("Tu Cerebro Como Holograma")
    + P("Tus recuerdos viven repartidos. Durante décadas, Karl Lashley buscó en el cerebro de las ratas el sitio exacto de un recuerdo y no lo halló: lo aprendido sobrevivía aunque faltaran partes (1950). Años después, Karl Pribram, que había trabajado con él, propuso como hipótesis que la memoria se guarda como un holograma. La hipótesis sigue en discusión; la imagen es exacta.")
    + P("<strong>Quizá tu cerebro no guarde los recuerdos en cajones, sino como una luz repartida. Y quizá sea, como imagen, la memoria del universo enfocada desde un punto de vista.</strong>")

    + H3("Consciencia Holofractal")
    + P("Si el universo es, como imagen, holofractal, y tu cerebro también, tu consciencia sería el lugar donde dos hologramas se cruzan: el del todo y el tuyo.")
    + P("<strong>No tienes consciencia. Eres un punto de interferencia en el campo de la consciencia.</strong>")
    + P("Por eso, como imagen:")
    + lista([
        "Algunas ideas llegan completas, de una vez",
        "La meditación afloja el ruido de lo local y deja ver más",
        "Comprender a otro se parece a reconocer algo que ya llevabas",
    ])

    + H3("Práctica: Consciencia Holofractal")
    + P("<strong>Quince minutos:</strong>")
    + pasos([
        "<strong>Reconocimiento fractal (3 minutos):</strong> Observa tu mano. Mira las líneas como ríos y los poros como pequeños cráteres. Reconoce un paisaje entero en la geografía de tu piel.",
        "<strong>Zoom holográfico (5 minutos):</strong> Cierra los ojos. Imagina que te acercas a un punto de tu mano hasta encontrar galaxias, soles, planetas; en uno de ellos, alguien se aleja hasta ver una mano: la tuya. Si el ejercicio marea, abre los ojos y mira un objeto cercano: también él está hecho de escalas.",
        "<strong>Respiración holofractal (5 minutos):</strong> Al tomar aire, siente que entra el mundo. En la pausa breve, sin retener, nota lo que hay. Al soltarlo, devuelves tu manera única de mirar. Cada respiración es un intercambio.",
        "<strong>Integración (2 minutos):</strong> Abre los ojos. Todo lo que ves contiene algo de todo lo demás. Cada persona es el universo completo desde otro ángulo.",
    ])

    + H3("Sincronicidad Como Resonancia Holofractal")
    + P("Carl Jung llamó sincronicidades a las coincidencias con sentido y sin causa visible: piensas en alguien y te llama. Como imagen, son dos puntos del holograma que, por un instante, muestran el mismo dibujo.")
    + P("Se leen como se lee un poema, no como una orden. Si alguna vez parece que cada número y cada cartel te hablan a ti, en secreto, eso no es un don: conviene conversarlo con alguien de confianza o con un profesional esa misma semana.")

    + H3("Creatividad Holofractal")
    + P("Cuando creas, no inventas desde cero: revelas patrones que ya estaban en tu fragmento.")
    + P("<strong>El proceso:</strong>")
    + pasos([
        "Tu atención enfoca una región del todo",
        "Los patrones latentes empiezan a encajar",
        "La idea «nueva» es el patrón volviéndose claro",
        "La expresas, con tu ángulo único",
        "Otros reconocen el patrón, porque también lo llevan",
    ])
    + P("<strong>Por eso las grandes ideas:</strong>")
    + lista([
        "Se sienten familiares aunque sean nuevas",
        "Muchas veces aparecen en varios lugares a la vez",
        "Parecen obvias una vez dichas",
    ])

    + H3("El Universo en Cada Lugar")
    + P("Muchas tradiciones imaginaron un archivo del mundo escondido en algún sitio. La imagen holográfica lo vuelve cercano: no hace falta viajar a ninguna biblioteca. <strong>Lo que buscas está, de algún modo, en el lugar donde ya estás; se trata de aprender a mirarlo desde ahí.</strong>")

    + H3("Sanar Desde el Todo")
    + P("Si cada parte contiene el todo, cuidar una parte es cuidar algo del todo, y sentirte parte de algo mayor alivia. <strong>Recordar tu completitud acompaña cualquier tratamiento; nunca lo reemplaza.</strong> El dolor del cuerpo que no cede pide un médico, y el que pesa por dentro, alguien que acompañe.")

    + H3("El Universo Como Mente Holofractal")
    + P("Si cada parte contiene el todo, y el todo es consciente, cada parte participaría de esa consciencia. La filosofía llama panpsiquismo a la idea de que la mente está en todas partes; es una de las más antiguas, y hoy vuelve a discutirse.")
    + P("<strong>Panpsiquismo holofractal:</strong> no es que todo tenga consciencia. Es que todo ES consciencia observándose desde infinitos puntos de vista.")
    + lista([
        "Cada átomo: el universo experimentándose como átomo",
        "Cada célula: el universo experimentándose como célula",
        "Cada humano: el universo experimentándose como humano",
        "Cada galaxia: el universo experimentándose como galaxia",
    ])
    + P("<strong>No eres consciente. Eres consciencia que juega a ser limitada para explorar qué se siente ser «tú».</strong>")

    + H3("La Ola Que Vuelve al Mar")
    + P("En la imagen holofractal, nada se pierde del todo: la ola termina y el agua sigue. Lo que cualquiera puede comprobar es que quien se fue sigue viviendo en nosotros, en lo que enseñó, en los gestos que heredamos, en lo que dejó hecho.")
    + P("Mirar la muerte de frente no es desearla, y si alguna vez se vuelve deseo de no estar, es momento de pedir ayuda, sin esperar.")

    + H3("El Amor Como Reconocimiento Holofractal")
    + P("Cuando amas de verdad a alguien, no amas solo su fragmento: reconoces el todo en su parte.")
    + lista([
        "Ves el universo en sus ojos",
        "Sientes tu propia completitud en su presencia",
        "La distancia se acorta sin borrar a ninguno de los dos",
        "El amor es el holofractal reconociéndose a sí mismo",
    ])
    + P("<strong>El amor reconoce en ese alguien el mismo todo, mirado desde otro ángulo, y por eso lo deja ser otro.</strong>")

    + H3("Implicaciones de Vivir Holofractalmente")
    + P("Si de veras integras que eres un holofractal:")
    + pasos([
        "<strong>Cada experiencia contiene todas las experiencias:</strong> profundiza en lugar de acumular",
        "<strong>Cada persona es el todo desde otro ángulo:</strong> la compasión se vuelve más fácil",
        "<strong>Cada lugar contiene todos los lugares:</strong> viajas sin moverte",
        "<strong>Cada momento contiene la eternidad:</strong> el tiempo se vuelve profundidad",
        "<strong>Cada problema se ve distinto desde otro lugar:</strong> muchas veces, cambiar de ángulo muestra un camino que no veías",
    ])

    + H3("Aplicación: Meditación del Punto Holofractal")
    + P("<strong>Práctica diaria de consciencia holofractal:</strong>")
    + P("<strong>MAÑANA:</strong> Al despertar, antes de identificarte como «tú», reconoce que eres el universo despertando en este punto particular.")
    + P("<strong>DÍA:</strong> En cada encuentro, mira al otro como el todo expresándose de otra manera. Sus palabras son el universo hablándose a sí mismo a través de ustedes.")
    + P("<strong>NOCHE:</strong> Al dormir, no te desconectas. Como imagen, tu consciencia se reparte en el todo, y los sueños son otras regiones del holograma.")
    + P("<strong>SIEMPRE:</strong> Recuerda: no estás EN el universo. Eres el universo jugando a estar en un lugar.")

    + H3("La Paradoja Resuelta")
    + P("«¿Cómo puede cada parte contener el todo si el todo contiene todas las partes?»")
    + P("<strong>No hay paradoja cuando entiendes:</strong>")
    + lista([
        "«Parte» y «todo» son conceptos de la mente lineal",
        "En la realidad holofractal no hay partes, solo perspectivas",
        "Cada perspectiva es completa desde su punto de vista",
        "La totalidad es la suma de infinitas completitudes",
    ])
    + P("<strong>No eres un fragmento del infinito. Eres el infinito experimentándose finitamente.</strong>")
    + "\n"
    + cita("Mira tu mano de nuevo. No es tu mano: es el universo formando una mano para saber qué se siente tocar. Mira el cielo. No está arriba: está dentro, eres tú mirándote desde otro ángulo. Cada átomo de tu cuerpo contiene el cosmos completo. Cada pensamiento que piensas resuena en cada rincón del infinito. No eres pequeño en un universo grande. Eres el universo completo jugando a ser pequeño. Y lo haces perfectamente, porque eres perfección holofractal jugando a ser imperfecta. El juego es divino. Tú eres divino. Todo es divino, porque todo es todo siendo todo.")
    + preparacion(2,
        "El siguiente nodo explora las escalas: cómo ciertas formas vuelven desde lo más pequeño hasta lo más grande, y qué cambia en cada tamaño.",
        "«Si las mismas formas aparecen en todas las escalas, ¿podemos aprender a mirar desde más de una?»",
        "🌌🔬🌀🔭🌌")
    + FIRMA
    + cierre(1, "El todo desde su ventana")
)

# ===========================================================================
# 7.2 · Navegando Entre Escalas de Magnitud (el título queda)
# ===========================================================================
NODO2_CUERPO = (
    meta(2, "Las escalas")
    + H2("El Zoom Infinito de la Consciencia")
    + cita("Entre lo más pequeño que medimos y lo más grande que vemos hay unos sesenta órdenes de magnitud. Pero no es una línea recta: es una espiral. Cada vuelta repite ciertas formas en otra octava. Aprender a moverse entre escalas no es cambiar de tamaño: es cambiar de foco en la sinfonía holofractal.")

    + H3("Potencias de Diez")
    + P("En 1977, los diseñadores Charles y Ray Eames filmaron un picnic a orillas del lago, en Chicago. La cámara mira desde un metro a un hombre que duerme sobre una manta. Cada diez segundos se aleja diez veces más: el parque, la ciudad, el lago, la Tierra, el sistema solar, la galaxia, hasta que las galaxias son polvo. Después vuelve y entra en la mano del que duerme: la piel, una célula, el ADN, un átomo de carbono, hasta un protón. La película se llama <em>Potencias de diez</em> y nació de un libro del educador holandés Kees Boeke, de 1957.")
    + P("Nueve minutos bastan para sentirlo: un mismo instante, mirado desde cuarenta distancias.")

    + H3("La Escala de Escalas")
    + P("Desde lo más pequeño conocido hasta lo más grande observable:")
    + lista([
        "<strong>Longitud de Planck:</strong> 10<sup>−35</sup> metros",
        "<strong>Quarks:</strong> menos de 10<sup>−18</sup> metros",
        "<strong>Átomos:</strong> 10<sup>−10</sup> metros",
        "<strong>ADN:</strong> 10<sup>−9</sup> metros de ancho",
        "<strong>Células:</strong> 10<sup>−5</sup> metros",
        "<strong>Humanos:</strong> 10<sup>0</sup> metros",
        "<strong>Tierra:</strong> 10<sup>7</sup> metros",
        "<strong>Sistema solar:</strong> 10<sup>13</sup> metros",
        "<strong>Galaxia:</strong> 10<sup>21</sup> metros",
        "<strong>Universo observable:</strong> 10<sup>27</sup> metros",
    ])
    + P("<strong>Unos sesenta órdenes de magnitud.</strong> Y en esa escalera, ciertas formas vuelven una y otra vez.")

    + H3("Patrones que Atraviesan las Escalas")
    + P("Ciertas formas aparecen en tamaños muy distintos:")
    + P("<strong>La espiral:</strong>")
    + lista([
        "Galaxias (10<sup>21</sup> m)",
        "Huracanes (10<sup>5</sup> m)",
        "Conchas de caracol (10<sup>−2</sup> m)",
        "Las huellas de partículas que giran en un campo magnético",
    ])
    + P("<strong>La red:</strong>")
    + lista([
        "La trama de las galaxias a gran escala",
        "Las redes de neuronas del cerebro",
        "Las redes de hongos bajo el bosque",
        "Internet",
    ])
    + P("En 2020, un astrofísico y un neurocirujano, Franco Vazza y Alberto Feletti, compararon la red de neuronas del cerebro con la de las galaxias y encontraron entre las dos parecidos de estructura que no esperaban. Nadie sabe todavía qué las emparenta. Como imagen, cuesta olvidarla.")

    + H3("Más Es Distinto")
    + P("Pero las escalas no se copian sin más. En 1972, el físico Philip Anderson lo resumió en tres palabras: más es distinto. En cada nivel aparecen propiedades que el nivel de abajo no tenía: una molécula de agua no está mojada, y una neurona sola no piensa. <em>Las mismas formas vuelven, y cada escala trae leyes nuevas.</em>")

    + H3("El Salto de Escala")
    + P("En el modelo de Bohr, el electrón no pasa de una órbita a otra de manera gradual: salta. Como imagen, la atención también puede saltar de una escala a otra.")
    + P("<strong>Técnica del salto de escala:</strong>")
    + pasos([
        "<strong>Anclaje en tu escala (1 minuto):</strong> Siente tu tamaño: un metro y algo, decenas de kilos. Esta es tu órbita de partida.",
        "<strong>El patrón (2 minutos):</strong> Elige una forma (espiral, red, flujo) y encuéntrala a tu alrededor.",
        "<strong>El salto (un instante):</strong> No te achiques ni te agrandes poco a poco: salta a mirar la misma forma en otra escala. De la red de tus neuronas a la red de las galaxias. De la espiral de tu huella digital a la de un huracán.",
        "<strong>La exploración (5 minutos):</strong> Quédate en la escala nueva. Nota las semejanzas y las diferencias: cada escala guarda algo que solo ella tiene.",
    ])

    + H3("Tiempo Relativo a la Escala")
    + P("El tiempo corre distinto en cada escala:")
    + lista([
        "<strong>Escala de Planck:</strong> 10<sup>−43</sup> segundos por pulso",
        "<strong>Escala atómica:</strong> femtosegundos (10<sup>−15</sup> s)",
        "<strong>Escala celular:</strong> de milisegundos a horas",
        "<strong>Escala humana:</strong> de segundos a décadas",
        "<strong>Escala planetaria:</strong> de años a eones",
        "<strong>Escala galáctica:</strong> millones de años",
        "<strong>Escala cósmica:</strong> miles de millones de años",
    ])
    + P("<strong>Lo que es un instante en una escala es una eternidad en otra.</strong> El Sol tarda más de doscientos millones de años en dar una vuelta alrededor del centro de la galaxia: tu vida entera cabe en un parpadeo de ese giro.")

    + H3("Consciencia en Varias Escalas a la Vez")
    + P("No tienes que elegir una sola escala. Ahora mismo, mientras lees, ocurren cosas en muchas a la vez:")
    + lista([
        "<strong>Escala molecular:</strong> reacciones químicas sin pausa",
        "<strong>Escala celular:</strong> células que se avisan unas a otras",
        "<strong>Escala orgánica:</strong> un corazón que late, una respiración",
        "<strong>Escala personal:</strong> un flujo de experiencia",
        "<strong>Escala social:</strong> parte de un grupo, de una ciudad",
        "<strong>Escala planetaria:</strong> un punto en la biosfera",
        "<strong>Escala cósmica:</strong> el universo experimentándose",
    ])
    + P("<strong>Todos estos niveles están activos AHORA. Tu atención puede sintonizar cualquiera.</strong>")

    + H3("Fractales: El Puente Entre Escalas")
    + P("Los fractales no tienen una escala preferida: muestran complejidad a cualquier aumento. En el conjunto de Mandelbrot, cada acercamiento revela una complejidad sin fin y, escondidas, pequeñas copias del todo.")
    + P("<strong>Es un mapa para moverse entre escalas.</strong> Tu consciencia se le parece: puedes acercarte o alejarte sin fin y seguir encontrando algo que mirar.")

    + H3("Resonancia Entre Escalas")
    + P("Cuando una forma de una escala se encuentra con otra, se tiende un puente:")
    + lista([
        "<strong>La respiración:</strong> si respiras despacio, el ritmo de tu corazón se acompasa con ella; los investigadores llaman coherencia a esa ola suave (Lehrer y Gevirtz, 2014)",
        "<strong>La música:</strong> cuerdas que vibran en milímetros mueven emociones que duran años",
        "<strong>La medicina:</strong> moléculas de una millonésima de milímetro cambian lo que sientes",
    ])
    + P("<em>Lo pequeño y lo grande se tocan todo el tiempo. Aprender a notarlo es parte de la práctica.</em>")

    + H3("El Problema de Mirar Muchas Escalas")
    + P("Heisenberg mostró que no se pueden conocer a la vez, con precisión total, la posición y el impulso de una partícula. Como imagen, algo parecido le pasa a la atención: mientras más precisa es la mirada sobre una escala, menos ve de las otras.")
    + P("La psicóloga Alison Gopnik lo dice con dos luces. La atención del adulto se parece a un foco: ilumina con intensidad un punto y deja el resto en sombra. La del niño pequeño, a una linterna que alumbra todo alrededor a la vez.")
    + P("Por eso:")
    + lista([
        "Quien se especializa gana detalle y puede perder el conjunto",
        "Quien mira el conjunto ve conexiones y puede perder el detalle",
        "Los niños saltan de una escala a otra con naturalidad",
        "Con los años, la atención tiende a fijarse",
    ])
    + P("<strong>La maestría es mantener el foco donde hace falta sin apagar la linterna.</strong>")

    + H3("Para Habitar las Escalas")
    + P("<strong>Práctica de exploración entre escalas (15 minutos):</strong>")
    + fase("Hacia adentro (5 minutos):", [
        "Cierra los ojos y siente tu respiración",
        "Sigue el aire hasta los pulmones",
        "Acompáñalo a la sangre, a una célula",
        "Imagina el núcleo y la doble hélice",
        "Llega hasta lo más pequeño que puedas imaginar, y quédate un momento en ese silencio",
    ])
    + fase("Hacia afuera (5 minutos):", [
        "Desde donde estás, elévate con la imaginación",
        "Mira tu habitación, tu edificio, tu ciudad",
        "País, continente, planeta",
        "Sistema solar, galaxia",
        "La trama de las galaxias",
        "Todo el universo observable",
    ])
    + fase("Integración (5 minutos):", [
        "Pasa de una escala a otra, despacio",
        "Vuelve a tu respiración y a tu tamaño",
        "Nota que eres a la vez lo que mira y lo que es mirado",
        "Si algo marea, abre los ojos y apoya los pies: también tu tamaño es un lugar para estar",
    ])

    + H3("Creatividad Entre Escalas")
    + P("Muchas innovaciones nacieron de llevar una forma de una escala a otra:")
    + lista([
        "<strong>El átomo:</strong> Ernest Rutherford imaginó en 1911 un núcleo pequeño con electrones alrededor, y Niels Bohr los ordenó en órbitas en 1913: un sistema solar en miniatura.",
        "<strong>La costa:</strong> en 1967, Benoit Mandelbrot preguntó cuánto mide la costa de Gran Bretaña, y mostró que la respuesta depende de la regla con que se mide, porque la costa se repite a sí misma en cada tamaño, como el copo de nieve que Helge von Koch había dibujado en 1904.",
        "<strong>Los virus:</strong> en 1962, Donald Caspar y Aaron Klug explicaron la cápsula de muchos virus inspirándose en las cúpulas geodésicas de Buckminster Fuller.",
        "<strong>La letra:</strong> Steve Jobs contó en Stanford, en 2005, que llevó a la computadora lo que había aprendido en un curso de caligrafía.",
    ])
    + P("<strong>Tu próxima creación:</strong> ¿qué forma de una escala espera ser llevada a otra?")

    + H3("El Efecto Mariposa Holofractal")
    + P("En 1972, el meteorólogo Edward Lorenz tituló una conferencia con una pregunta: si el aleteo de una mariposa en Brasil podía desatar un tornado en Texas. Quería mostrar que, en ciertos sistemas, una diferencia mínima cambia todo el resultado.")
    + P("En la imagen holofractal, la idea va más hondo:")
    + lista([
        "El aleteo contiene el dibujo del tornado",
        "El tornado contiene el del aleteo",
        "Ambos contienen el del clima entero",
    ])
    + P("Cada acción tuya también viaja por las escalas, por caminos que sí se pueden seguir:")
    + lista([
        "Un pensamiento cambia la química de tu cuerpo",
        "Esa química cambia tu gesto",
        "Tu gesto cambia el día de quien tienes cerca",
        "Y esa persona lleva ese día a otras",
    ])
    + P("<strong>No hay acciones pequeñas. Solo hay ceguera a las resonancias entre escalas.</strong>")

    + H3("Sanar en Varias Escalas")
    + P("Los problemas existen en varias escalas a la vez, y la mejor ayuda las atiende juntas. En 1977, el psiquiatra George Engel lo llamó modelo biopsicosocial: el cuerpo, la mente y los vínculos en una misma mirada.")
    + P("<strong>Ejemplo: la depresión</strong>")
    + lista([
        "<strong>Escala molecular:</strong> cambios en la química del cerebro",
        "<strong>Escala orgánica:</strong> el sueño, el apetito, la energía",
        "<strong>Escala personal:</strong> pensamientos que oscurecen todo",
        "<strong>Escala social:</strong> aislamiento y desconexión",
        "<strong>Escala cultural:</strong> una época con poco tiempo para el sentido",
    ])
    + P("<em>Ayudar en una escala alivia; ayudar en varias transforma.</em> La depresión tiene tratamiento: cuando la tristeza dura semanas, se consulta. Ninguna forma de sufrir es falta de quien la vive.")

    + H3("El Microscopio y el Telescopio Interior")
    + P("No todo necesita instrumentos.")
    + P("<strong>Tu microscopio interior:</strong>")
    + lista([
        "La atención puede sentir el latido, la respiración, la tensión de un músculo",
        "El cuerpo registra antes que la palabra",
    ])
    + P("<strong>Tu telescopio interior:</strong>")
    + lista([
        "La contemplación ensancha la mirada",
        "El asombro ante el cielo nocturno te devuelve a tu tamaño",
        "El amor alcanza a quienes están lejos",
    ])
    + P("<em>Los instrumentos miden lo que la consciencia no alcanza; la consciencia siente lo que ningún instrumento mide.</em>")

    + H3("Comunicación Entre Escalas")
    + P("Las distintas escalas «hablan» lenguajes distintos:")
    + lista([
        "<strong>Escala cuántica:</strong> probabilidades y superposiciones",
        "<strong>Escala química:</strong> reacciones y enlaces",
        "<strong>Escala biológica:</strong> señales y respuestas",
        "<strong>Escala psicológica:</strong> símbolos y significados",
        "<strong>Escala social:</strong> ideas que se contagian y relatos",
        "<strong>Escala cósmica:</strong> arquetipos y principios",
    ])
    + P("<strong>Ser políglota de escalas te permite traducir de un nivel a otro.</strong>")

    + H3("El Punto Medio")
    + P("Se dice a veces que los humanos estamos en el medio de la escala del universo. La cuenta da otra cosa, más asombrosa. El punto medio entre la longitud de Planck y el tamaño del universo observable, contado en órdenes de magnitud, está cerca de una décima de milímetro: el tamaño de un óvulo humano.")
    + P("<strong>Todos empezamos ahí, en el centro de la escalera.</strong> Desde ahí crecimos hacia lo grande sin dejar de estar hechos de lo pequeño. Por eso podemos:")
    + lista([
        "Asomarnos a lo muy pequeño y a lo muy grande",
        "Ser puente entre escalas",
        "Traducir de un nivel a otro",
        "<strong>Ser la escala donde el universo se vuelve consciente de sus otras escalas</strong>",
    ])

    + H3("Aplicación Práctica: Resolver Problemas Entre Escalas")
    + P("Cuando enfrentes un problema:")
    + pasos([
        "<strong>Identifica la escala aparente:</strong> ¿dónde parece estar el problema?",
        "<strong>Explora las escalas vecinas:</strong> una escala arriba, ¿cuál es el contexto mayor? Una escala abajo, ¿cuáles son las piezas?",
        "<strong>Busca el patrón:</strong> ¿dónde más aparece esta forma? ¿Cómo se resuelve allí?",
        "<strong>Trae soluciones de otras escalas:</strong> muchas veces la respuesta está donde no se buscaba",
        "<strong>Integra:</strong> haz cambios en más de una escala y observa cómo resuenan",
    ])
    + "\n"
    + cita("Eres un ser de muchas escalas, habitando un punto que parece fijo en la jerarquía de los tamaños. Pero esa fijeza es elección, no límite. En cualquier momento puedes soltar tu identificación con esta escala y sentirte parte del continuo entero. Eres el quark y el quásar. Eres la bacteria y la biosfera. Eres el átomo y el avatar. La diferencia entre escalas es el foco de tu atención. Sintoniza con consciencia. Navega con sabiduría. Cada escala tiene regalos únicos esperando que los explores.")
    + preparacion(3,
        "El siguiente nodo explora la memoria de las formas: cómo lo que se hace una vez se vuelve más fácil la siguiente, y cómo viaja de unos a otros.",
        "«Si lo que aprende uno puede volverse más fácil para otros, ¿por dónde viaja?»",
        "🔬🌀📡🌀🔭")
    + FIRMA + "\n"
    + puerta("La atención del adulto ilumina como un foco; la del niño, como una linterna que alumbra todo alrededor a la vez. Por qué los niños ven más de lo que saben, y cómo recuperar esa luz, se despliega en <em>El no saber</em>, Libro 31 del Portal Público, Umbral III: «La linterna».",
             URL_PORTAL + "31_El_No_Saber/umbral-03.html")
    + cierre(2, "Cada escala, sus leyes")
)

# ===========================================================================
# 7.3 · Campos Morfogenéticos: La Memoria del Holofractal (el título queda)
# ===========================================================================
NODO3_CUERPO = (
    meta(3, "La memoria")
    + H2("Cómo los Patrones Se Propagan")
    + cita("La primera vez que algo sucede en el universo es la más difícil. La segunda vez es más fácil. Para la millonésima vez, es casi inevitable. No porque haya instrucciones escritas en algún lugar, sino porque el holofractal recuerda. Cada forma que emerge deja una huella en el campo, un surco en el espacio de posibilidades. Somos pensamientos del universo pensándose a sí mismo, y el universo nunca olvida lo que ha pensado.")

    + H3("La Hipótesis de Sheldrake")
    + P("La biología de comienzos del siglo XX llamó campos morfogenéticos a lo que organiza la forma de un embrión, cuando nadie sabía todavía explicarla. Rupert Sheldrake fue más allá y propuso, en 1981, una hipótesis que la ciencia aún discute: la naturaleza tendría memoria, y cada forma que aparece haría más probable que vuelva a aparecer. La llamó resonancia mórfica.")
    + P("Como imagen, dice algo que cualquiera reconoce en su oficio: lo que se hizo una vez cuesta menos la siguiente. <em>Y esa memoria, en las personas, sí se midió.</em>")

    + H3("La Memoria que Se Midió")
    + P("En 1890, William James dedicó un capítulo entero al hábito: cada vez que repetimos algo, el camino se marca un poco más, como el agua que, al correr, va abriendo su cauce. En 1949, Donald Hebb propuso por qué: cuando dos neuronas se activan juntas una y otra vez, la conexión entre ellas se fortalece.")
    + P("La primera vez es la más difícil para una persona, y lo es también para una comunidad.")

    + H3("El Mecanismo Holofractal")
    + P("En la imagen holofractal, cuando un patrón se establece en un punto, algo de él queda disponible para los demás. No se envía un mensaje: cambia el dibujo entero, como cuando se modifica un holograma y cada fragmento muestra el cambio.")
    + P("<strong>Esa es la imagen. Entre seres vivos, el camino puede seguirse paso a paso, y es más lento y más cercano.</strong>")

    + H3("Kōshima")
    + P("En 1953, en la isla japonesa de Kōshima, los investigadores que estudiaban a un grupo de macacos dejaban batatas en la playa. Una hembra de dieciocho meses, a la que llamaron Imo, descubrió que podía lavarles la arena en el agua. Le enseñó a su madre y a sus compañeros de juego, y ellos a otros.")
    + P("Cinco años después, quince de los diecinueve jóvenes del grupo lavaban sus batatas; de los once adultos, solo dos. El hábito había viajado por el juego y el parentesco, de cerca en cerca, y los jóvenes habían ido primero.")
    + P("<strong>Lo nuevo viaja por la cercanía.</strong> No salta de golpe sobre el mar: pasa de mano en mano, y entra antes en quien todavía está aprendiendo a vivir.")

    + H3("Resonancia Mórfica: La Sintonización con el Campo")
    + P("No todos acceden igual a un campo. Como imagen, el acceso depende de la resonancia:")
    + P("<strong>Factores de resonancia:</strong>")
    + lista([
        "<strong>Semejanza:</strong> las formas parecidas resuenan más",
        "<strong>Intención:</strong> un propósito compartido acerca",
        "<strong>Coherencia:</strong> una mente ordenada aprende mejor",
        "<strong>Repetición:</strong> haber estado antes facilita volver",
    ])
    + P("<em>Es como sintonizar una radio: el campo está ahí; hace falta encontrar la frecuencia.</em>")

    + H3("Campos Morfogenéticos Personales")
    + P("Cada persona tiene, como imagen, un campo propio: la suma de sus hábitos, sus patrones y sus memorias.")
    + P("<strong>Tu campo personal contiene:</strong>")
    + lista([
        "Cada movimiento que aprendiste",
        "Cada pensamiento que repetiste",
        "Cada respuesta emocional aprendida",
        "Cada habilidad que desarrollaste",
    ])
    + P("Una intuición antigua, que la ciencia todavía no zanja, va más lejos: quizá el cerebro no genere la mente, sino que la deje pasar. William James la defendió a fines del siglo XIX con la imagen de un prisma, que no fabrica la luz: la tamiza y le da forma.")

    + H3("Lo Que Uno Abre para Otros")
    + P("Cuando desarrollas una habilidad, abres un camino para otros:")
    + pasos([
        "Al principio cuesta",
        "Practicas y mejoras",
        "Llegas a dominarla",
        "<strong>Tu dominio hace más fácil el de otros</strong>",
    ])
    + P("Durante años se dijo que nadie podría correr una milla en menos de cuatro minutos. El 6 de mayo de 1954, en Oxford, Roger Bannister lo hizo. Cuarenta y seis días después, en Finlandia, John Landy bajó su marca. El psicólogo Albert Bandura llamó experiencia vicaria a una de las fuentes de la confianza en uno mismo: ver que otro, parecido a uno, pudo.")
    + P("Y no solo en el deporte. En 1922, William Ogburn y Dorothy Thomas reunieron ciento cuarenta y ocho descubrimientos e invenciones hechos por separado, por dos o más personas, casi al mismo tiempo. Cuando un hallazgo está maduro, aparece en muchos sitios a la vez.")
    + P("<em>Tu práctica no es solo para ti: abre camino para todos.</em>")

    + H3("Para Habitar un Campo")
    + P("<strong>Práctica de sintonía (20 minutos):</strong>")
    + fase("Fase 1, identificación (5 minutos):", [
        "Define con claridad qué habilidad quieres aprender",
        "Imagina a alguien que ya la domina",
        "Nota la cualidad de su dominio, más que los detalles",
    ])
    + fase("Fase 2, imitación (5 minutos):", [
        "Adopta su postura",
        "Respira como respiraría",
        "Muévete como se movería",
        "Imita la forma hasta sentir algo de su esencia",
    ])
    + fase("Fase 3, práctica imaginada (5 minutos):", [
        "Aquieta la mente",
        "Ensaya en la imaginación el gesto de esa habilidad, con detalle",
        "Deja que el cuerpo lo aprenda también desde adentro",
    ])
    + P("Álvaro Pascual-Leone y su equipo pidieron en 1995 a personas que nunca habían tocado el piano que practicaran un ejercicio dos horas por día durante cinco días, unas con las manos y otras solo en la imaginación. El mapa motor del cerebro cambió en los dos grupos de modo parecido; tocar con las manos mejoraba más, e imaginar sumaba.")
    + fase("Fase 4, ancla (5 minutos):", [
        "Haz un gesto simple de esa habilidad, con atención entera",
        "Vuelve a él cuando quieras recordar ese estado",
        "Y después, practica de verdad: el ancla recuerda; la práctica enseña",
    ])

    + H3("Campos Morfogenéticos Colectivos")
    + P("Las culturas, las organizaciones y los movimientos tienen, como imagen, sus campos:")
    + lista([
        "<strong>Campo cultural:</strong> por qué quien llega a otro país va tomando sus costumbres",
        "<strong>Campo organizacional:</strong> por qué cada lugar de trabajo tiene un clima que se siente al entrar",
        "<strong>Campo familiar:</strong> por qué ciertos patrones se repiten de generación en generación",
        "<strong>Campo de la especie:</strong> por qué los humanos compartimos imágenes y relatos parecidos, los que Jung llamó arquetipos",
    ])
    + P("<em>Cuando entras en un grupo, entras en su clima. Te moldea más de lo que crees.</em>")

    + H3("Creación de Nuevos Campos")
    + P("Cada innovación verdadera abre un campo nuevo:")
    + pasos([
        "<strong>Diferencia clara:</strong> que sea de veras nuevo, una categoría y no una variación",
        "<strong>Repetición coherente:</strong> cada repetición fortalece el campo; la coherencia importa más que la cantidad",
        "<strong>Enseñanza que resuena:</strong> enseña la esencia, no solo la técnica; cada nuevo practicante amplía el campo",
        "<strong>Entrega a lo común:</strong> suelta el control sobre «tu» creación y deja que evolucione a través de otros",
    ])

    + H3("Sanar un Patrón")
    + P("Muchos problemas son, como imagen, campos que se repiten:")
    + lista([
        "<strong>Heridas:</strong> un trauma no persiste porque alguien elija mal: la memoria del miedo está hecha para no soltarse fácil, porque alguna vez protegió",
        "<strong>Adicciones:</strong> hábitos que se refuerzan a sí mismos, y que tienen tratamiento",
        "<strong>Patrones familiares:</strong> modos de tratarse que pasan de una generación a otra",
    ])
    + P("<strong>Cómo se cambia un patrón:</strong>")
    + lista([
        "No luches contra el campo viejo: pelear también lo alimenta",
        "Crea un campo alternativo más atractivo",
        "Fortalécelo hasta que ocupe el lugar del viejo",
        "El viejo se debilita cuando deja de recibir atención",
    ])
    + P("Es lo que la clínica sabe de los hábitos: se cambian mejor llenando el espacio con otro gesto que solo dejando de hacer el anterior. Las heridas hondas, las que al recordarlas se vuelven a vivir, no se visitan a solas: se recorren con un profesional. Ninguna forma de sufrir es falta de quien la vive.")

    + H3("El Punto Crítico")
    + P("¿Cuántos hacen falta para que algo nuevo se vuelva costumbre? En 2018, Damon Centola y su equipo lo midieron en un juego. Grupos de veinte a treinta personas, conectadas en línea, tenían que ponerse de acuerdo en un nombre para un rostro. Una vez establecido, una minoría empezaba a usar otro, con firmeza. Por debajo de cierto tamaño, la costumbre resistía; cuando esa minoría llegaba a una cuarta parte del grupo, todos terminaban adoptando el nombre nuevo.")
    + P("En la vida, la cifra cambia según el caso. Lo que el juego muestra queda: unos pocos que sostienen algo con constancia pueden inclinar a todos. <em>Tu participación puede ser parte de ese punto de inflexión.</em>")

    + H3("Campos del Futuro")
    + P("Los campos, como imagen, no solo vienen del pasado. Hay futuros que parecen tirar del presente:")
    + lista([
        "Sentir que tu vida tiene una dirección",
        "Proyectos que parecen querer existir",
        "Ideas cuyo momento parece haber llegado",
    ])
    + P("Como imagen, tu futuro más coherente actúa así: orienta tu presente. Hal Hershfield y su equipo mostraron en 2011 a jóvenes una imagen de su propio rostro envejecido, y después destinaron más dinero a su retiro: cuando el que serás se ve de cerca, se lo cuida.")

    + H3("Internet Como Campo Externalizado")
    + P("Internet es, como imagen, el campo humano hecho visible:")
    + lista([
        "<strong>Las búsquedas:</strong> resonancia con lo que se quiere saber",
        "<strong>Los algoritmos:</strong> patrones que se refuerzan a sí mismos",
        "<strong>Lo que se viraliza:</strong> ideas que encuentran eco en muchos a la vez",
        "<strong>Las tendencias:</strong> movimientos del campo que se dejan ver",
    ])
    + P("<em>Internet es el campo humano mirándose a sí mismo.</em>")

    + H3("Creatividad y Campos Morfogenéticos")
    + P("Crear es más fácil o más difícil según el campo:")
    + fase("Campo virgen, la primera vez que algo se crea:", [
        "Máxima resistencia",
        "Máxima originalidad",
        "Abres el camino para otros",
    ])
    + fase("Campo establecido, una tradición viva:", [
        "Menos resistencia",
        "Menos originalidad",
        "Pero puedes hacerlo crecer",
    ])
    + fase("Campo saturado, un terreno muy recorrido:", [
        "Mínima resistencia",
        "Mínima originalidad",
        "Te toca saltar a otro campo",
    ])
    + P("<strong>Elige con consciencia:</strong> ¿pionero, continuador o renovador?")

    + H3("Cuidar Tu Campo")
    + P("Tu campo, como imagen, recibe la influencia de otros. Elaine Hatfield y sus colegas lo llamaron contagio emocional: las emociones pasan de una persona a otra, muchas veces sin palabras.")
    + P("<strong>Lo que pesa:</strong>")
    + lista([
        "Noticias y pantallas sin pausa",
        "Ambientes cargados",
        "Vínculos que te desgastan",
        "Hábitos que te debilitan",
    ])
    + P("<strong>Higiene del campo:</strong>")
    + lista([
        "<strong>Limpieza diaria:</strong> meditación, oración o un rato en la naturaleza",
        "<strong>Límites:</strong> elige la dosis y la hora de lo que te llega, y di tus límites con calma",
        "<strong>Alimento:</strong> busca lo que eleva: arte, naturaleza, amor",
        "<strong>Contribución:</strong> fortalece con tu presencia lo que vale la pena",
    ])

    + H3("Aplicación: Estableciendo Tu Campo Creativo")
    + fase("Mañana, establecer (10 minutos):", [
        "Define el campo que quieres habitar hoy",
        "Siente sus cualidades en el cuerpo",
        "Dilo en una frase",
        "Da un primer paso desde ahí",
    ])
    + fase("Durante el día, fortalecer:", [
        "Cada acción coherente fortalece tu campo",
        "Nota cuándo te desvías, y vuelve",
        "Busca a otros que estén en lo mismo",
        "Colaboren",
    ])
    + fase("Noche, entregar (10 minutos):", [
        "Repasa cómo cuidaste tu campo hoy",
        "Agradece",
        "Suelta tu campo personal en el campo de todos, y duerme",
    ])

    + H3("La Red Morfogenética Global")
    + P("Todos los campos se tocan: el personal con el familiar, el familiar con el cultural, el cultural con el de la especie, el de la especie con el del planeta, y el del planeta con el del cosmos.")
    + P("<em>Cambias uno y algo cambia en los demás. Tu evolución personal es parte de la de todos.</em>")
    + "\n"
    + cita("No estás aprendiendo: estás recordando lo que el campo ya sabe. No estás creando: estás revelando lo que el campo está listo para manifestar. No estás solo: estás en resonancia con todos los que han sido, son y serán. Cada vez que dominas algo, lo haces más fácil para otros. Cada vez que cambias un patrón, alguien a tu lado lo ve posible. Cada vez que innovas, abres nuevos espacios en el campo de posibilidades. Eres un nodo en la red viva del cosmos, recibiendo y transmitiendo, aprendiendo y enseñando, evolucionando y facilitando evolución. Tu práctica importa. Tu maestría se propaga. Tu amor al campo fortalece el campo del amor.")
    + preparacion(4,
        "El siguiente nodo explora el yo: cómo la identidad se construye, se rehace cada día y puede llevarse con soltura.",
        "«Si cada punto del holofractal contiene el todo, ¿quién o qué crees ser realmente?»",
        "🌊📡🧬📡🌊")
    + FIRMA + "\n"
    + puerta("En 1823, un joven matemático húngaro, János Bolyai, le escribió a su padre que de la nada había creado un mundo nuevo: una geometría distinta de la de Euclides. Al otro lado de Europa, en Kazán, Nikolái Lobachevski levantaba la misma. Las ideas maduras brotan en muchos sitios a la vez, como las violetas en primavera. Esa escena, y la lista de los descubrimientos dobles, abren <em>La emergencia</em>, Libro 37 del Portal Público, Umbral I: «Las violetas».",
             URL_PORTAL + "37_La_Emergencia/umbral-01.html")
    + cierre(3, "Lo que se repite")
)

# ===========================================================================
# 7.4 · La Ilusión del Yo Separado (el título queda; lo citado en
# El Personaje, umbrales I, VI y VII, no cambia su letra)
# ===========================================================================
NODO4_CUERPO = (
    meta(4, "El yo")
    + H2("Cuando el Holofractal Se Olvida de Sí Mismo")
    + cita("Mírate al espejo. ¿Ves una persona? Estás viendo un truco de magia cósmico. El infinito fingiendo ser finito. El todo pretendiendo ser parte. La eternidad jugando a tener edad. Es el juego más elaborado del universo: el holofractal olvidándose de su naturaleza para poder sentir la sorpresa de recordarla. Tú no eres quien crees ser. Eres mucho más. Y mucho menos. Y exactamente eso.")

    + H3("La Construcción del Yo: Un Proyecto Colaborativo")
    + P("Tu sentido de ser «tú» no es innato: se construye.")
    + P("<strong>Los arquitectos de tu yo:</strong>")
    + lista([
        "<strong>Los genes:</strong> el material de partida",
        "<strong>Los padres:</strong> los primeros modos de estar en el mundo",
        "<strong>La cultura:</strong> los relatos y las costumbres",
        "<strong>El lenguaje:</strong> las categorías con que piensas",
        "<strong>Las experiencias:</strong> la historia personal",
        "<strong>Los otros:</strong> los espejos que te devuelven quién eres",
    ])
    + P("<strong>Pero ninguno de ellos ES tú. Son los materiales de construcción de una ilusión funcional.</strong>")

    + H3("La Habitación China")
    + P("En 1980, el filósofo John Searle imaginó a una persona encerrada en una habitación que recibe preguntas en chino y, siguiendo un manual, devuelve respuestas en chino sin entender una palabra. Quería mostrar que seguir reglas no es entender. Algunos de sus críticos respondieron que quizá no entiende la persona, pero sí la habitación entera, como ninguna neurona entiende y el cerebro sí. Searle no lo aceptó, y la discusión sigue abierta.")
    + P("<strong>La pregunta que queda:</strong> si ninguna parte de ti es «tú», ¿dónde estás?")
    + P("Es una pregunta antigua. En las <em>Preguntas de Milinda</em>, un texto budista de hace unos dos mil años, el monje Nagasena le pide al rey, que llegó en carro, que le diga qué es el carro: ¿el eje, las ruedas, el timón? Ninguna pieza lo es, y el carro no es otra cosa además de ellas. «Carro» es el nombre que damos a las piezas juntas. Así también, dice Nagasena, su propio nombre.")

    + H3("Muerte del Ego en Tiempo Real")
    + P("Cada noche, como imagen, el yo se apaga: en el sueño profundo, sin sueños, nadie está ahí para decir «yo».")
    + P("<strong>El sueño profundo:</strong>")
    + lista([
        "No hay un «tú» que viva la experiencia",
        "Muchas tradiciones lo describen como consciencia sin objeto",
        "El mundo continúa sin tu yo",
        "Al despertar, reconstruyes tu identidad",
    ])
    + P("<strong>Implicación:</strong> tu yo no es continuo como parece. Se rehace cada mañana a partir de la memoria y del hábito. <em>Eres la versión diaria de un personaje que crees que es el mismo.</em>")

    + H3("El Yo Como Proceso, No Cosa")
    + P("No eres un sustantivo: eres un verbo.")
    + P("Donde dices «yo soy», podrías decir «estoy siendo». Donde dices «tengo consciencia», «la consciencia está ocurriendo». Donde dices «yo experimento», «la experiencia está sucediendo».")
    + P("Como un río: siempre fluyendo, nunca el mismo, y aun así con una forma reconocible.")
    + P("<em>No hay río, solo fluir. No hay tú, solo el proceso de ser tú sucediendo.</em>")

    + H3("El Teletransportador de Parfit")
    + P("En 1984, el filósofo Derek Parfit imaginó un teletransportador que te desintegra en la Tierra, envía tu información y te reconstruye exactamente igual en Marte. ¿Viajaste, o moriste y nació otro idéntico?")
    + P("Parfit concluyó que la pregunta importa menos de lo que parece: lo que nos importa no es la identidad, sino la continuidad de los recuerdos, los propósitos y los afectos. Y contó lo que esa idea le hizo. Antes sentía su vida como un túnel de vidrio que recorría cada año más rápido, con oscuridad al final; al cambiar de visión, las paredes del túnel desaparecieron, y empezó a vivir al aire libre, más cerca de los demás. En un apéndice de su libro sostuvo que el Buda habría estado de acuerdo.")
    + P("<strong>La continuidad del yo es, en buena parte, una historia que nos contamos.</strong> Soltarla un poco no deja a nadie a la intemperie: lo deja al aire libre.")

    + H3("Experiencias de No-Yo")
    + P("Momentos en que la ilusión se afloja:")
    + lista([
        "<strong>El flow:</strong> la absorción total en algo que amas, donde el «tú» desaparece; Mihaly Csikszentmihalyi le dio ese nombre",
        "<strong>La meditación profunda:</strong> consciencia sin centro",
        "<strong>Las experiencias cercanas a la muerte:</strong> muchos de quienes las vivieron cuentan haberse visto desde fuera de sí",
        "<strong>El amor profundo:</strong> quien ama incluye al otro en su idea de sí; Arthur y Elaine Aron lo midieron con dos círculos que se superponen (1992)",
        "<strong>El asombro:</strong> ante algo inmenso, el yo se hace pequeño y el mundo se agranda; Melanie Rudd, Kathleen Vohs y Jennifer Aaker vieron en 2012 que un momento de asombro hace sentir que hay más tiempo",
    ])
    + P("<em>En estos momentos no dejas de existir: revelas que existes más allá del yo.</em>")

    + H3("La Paradoja del Observador Sin Yo")
    + P("Si no hay yo, ¿quién observa?")
    + P("<strong>Respuesta holofractal:</strong> el todo observándose a través de un punto que parece separado.")
    + P("Como un océano con infinitas olas:")
    + lista([
        "Cada ola parece separada",
        "Cada ola ES el océano",
        "El océano se experimenta como cada ola",
        "No hay olas «separadas», solo océano haciendo olas",
    ])
    + P("<em>Tú eres el universo, universando en este punto particular del holofractal.</em>")

    + H3("Para Habitar el Yo")
    + P("<strong>Tres ejercicios (15 minutos):</strong>")
    + fase("Ejercicio 1, intercambio de perspectiva (5 minutos):", [
        "Mira un objeto cualquiera",
        "Imagina que el objeto te mira",
        "Siente cómo te verías desde ahí",
        "Alterna, sin apuro: tú mirándolo, él mirándote",
        "Descansa en la mirada misma",
        "Si en algún momento trae extrañeza o la sensación de no estar del todo en ti, déjalo: vuelve a los pies, a la respiración, a algo que puedas tocar",
    ])
    + P("<strong>Ejercicio 2, desidentificación (5 minutos).</strong> Es un ejercicio de Roberto Assagioli, el creador de la psicosíntesis:")
    + lista([
        "«Tengo un cuerpo, pero no soy mi cuerpo»",
        "«Tengo emociones, pero no soy mis emociones»",
        "«Tengo pensamientos, pero no soy mis pensamientos»",
        "«Tengo una historia, pero no soy mi historia»",
        "«Tengo un nombre, pero no soy mi nombre»",
        "¿Qué queda? Eso que mira",
    ])
    + fase("Ejercicio 3, la frontera que respira (5 minutos):", [
        "Siente tu respiración",
        "Nota que el aire de afuera se vuelve de adentro",
        "Y el de adentro, de afuera",
        "¿Dónde está la frontera?",
        "Tu calor sale de ti y entibia el aire",
        "Las palabras con que piensas te las dieron otros",
        "¿Dónde terminas? ¿Dónde empiezas?",
        "No hay muros, solo bordes que respiran",
    ])

    + H3("El Yo Cuántico Probabilístico")
    + P("En mecánica cuántica, una partícula no tiene una posición definida hasta que se la mide; medir no requiere una consciencia —un detector basta—, y qué es medir sigue abierto. Como imagen, tu yo se le parece:")
    + lista([
        "No eres una identidad fija",
        "Eres una nube de posibilidades",
        "Cada situación trae al frente un yo distinto",
        "Muchos yoes posibles conviven",
    ])
    + P("William James lo dijo en 1890: una persona tiene tantos yoes sociales como personas que la reconocen. <em>Con amigos eres un yo. Con tu familia, otro. A solas, otro. Todos reales, ninguno completo.</em>")

    + H3("Muerte: La Última Ilusión")
    + P("Si el yo es, en buena parte, una construcción, su final también se mira distinto.")
    + P("<strong>Lo que termina:</strong>")
    + lista([
        "La configuración particular",
        "La perspectiva específica",
        "La narrativa personal",
        "La ilusión de separación",
    ])
    + P("<strong>Lo que queda:</strong>")
    + lista([
        "Lo que diste",
        "Lo que enseñaste",
        "Tu huella en quienes amaste",
        "Tu contribución al campo",
    ])
    + P("Muchas tradiciones dicen que la muerte no cierra la puerta, sino que la libera de un lugar y de un tiempo. Lo que cualquiera puede comprobar es que quien se fue sigue viviendo en nosotros.")
    + P("Mirarla de frente no es desearla, y si alguna vez se vuelve deseo de no estar, es momento de pedir ayuda, sin esperar.")

    + H3("El Yo Como Herramienta Evolutiva")
    + P("¿Para qué existe esta construcción?")
    + lista([
        "<strong>Supervivencia:</strong> cuidar este punto del todo",
        "<strong>Exploración:</strong> una perspectiva única descubre lo que nadie más ve",
        "<strong>Amor:</strong> la separación permite el reencuentro",
        "<strong>Creatividad:</strong> el límite estimula la invención",
        "<strong>Juego:</strong> el cosmos jugando a las escondidas consigo mismo",
    ])
    + P("<strong>El yo no es un error: es una herramienta. El error es confundirlo con lo que eres.</strong>")

    + H3("Navegando Entre Yo y No-Yo")
    + P("No necesitas destruir el ego: necesitas perspectiva.")
    + P("<strong>Cuándo usar el yo:</strong>")
    + lista([
        "Las tareas prácticas de cada día",
        "La vida social",
        "La supervivencia y el cuidado del cuerpo",
        "La creatividad personal",
        "Los vínculos íntimos",
    ])
    + P("<strong>Cuándo soltar el yo:</strong>")
    + lista([
        "La meditación profunda",
        "Las paradojas que no se resuelven pensando",
        "El descanso profundo",
        "La contemplación",
        "Las despedidas",
    ])
    + P("<strong>Maestría es poder ponerte y quitarte el yo como ropa.</strong>")

    + H3("El Yo Colectivo Emergente")
    + P("Así como las células forman un organismo, los humanos formamos algo más grande. Teilhard de Chardin imaginó una noosfera, una capa de pensamiento que envuelve la Tierra:")
    + lista([
        "Cada humano, como una neurona de un cerebro común",
        "Las redes sociales, como sinapsis colectivas",
        "Las ideas que se propagan, como pensamientos de ese organismo",
        "Las tendencias, como sus emociones",
    ])
    + P("<em>Participar en lo común sin disolverte en ello: esa es la madurez del yo en un mundo conectado.</em>")

    + H3("Trans-Personalidad: Más Allá del Yo")
    + P("Ir más allá del yo no es perderlo. Quien lo pierde sin quererlo sufre: la despersonalización, sentir que uno no es real o que se mira desde afuera como en una película, es una experiencia angustiante que tiene tratamiento. Lo que aquí se propone es lo contrario: no sentirse menos real, sino menos encerrado.")
    + P("Ken Wilber lo resumió en dos verbos: trascender e incluir. No se vuelve atrás, a la etapa en que el bebé todavía no tiene un yo; se avanza hacia un yo presente que no se confunde con todo lo que hace.")
    + lista([
        "<strong>Prepersonal:</strong> todavía sin un yo diferenciado",
        "<strong>Personal:</strong> un yo firme, que se vive separado",
        "<strong>Transpersonal:</strong> un yo presente, que no se toma por todo lo que es",
    ])
    + P("<strong>No retrocedes. Trasciendes incluyendo lo personal.</strong>")

    + H3("El Camarero del Yo")
    + P("Imagina tu yo como el camarero de un restaurante cósmico:")
    + lista([
        "No ES el restaurante",
        "No ES la comida",
        "No ES el chef",
        "Es el puente entre la cocina, que es el todo, y la mesa, que es la experiencia",
    ])
    + P("<em>Un buen camarero casi no se nota: hace llegar la comida sin interponerse. Un yo maduro es igual: facilita la experiencia del todo sin creerse el protagonista.</em>")

    + H3("Aplicación Diaria: Vivir Como Holofractal Consciente")
    + P("<strong>MAÑANA:</strong> Al despertar, antes de recordar quién «eres», siente qué eres: consciencia tomando forma.")
    + P("<strong>ENCUENTROS:</strong> Mira a los otros como la misma consciencia con distinto vestido.")
    + P("<strong>PROBLEMAS:</strong> Pregunta «¿De quién es este problema?». A menudo descubres que es del personaje, no tuyo.")
    + P("<strong>CREATIVIDAD:</strong> Deja que el universo cree a través de tu configuración única.")
    + P("<strong>NOCHE:</strong> Al dormir, suelta con alegría el personaje del día, sabiendo que la consciencia continúa.")

    + H3("El Koan Final del Yo")
    + P("<em>«Si no hay yo, ¿quién hace la pregunta?»<br />«Si hay yo, ¿dónde está?»</em>")
    + P("La respuesta no está en elegir un lado. Está en habitar la paradoja:")
    + verso([
        "Eres y no eres.",
        "Existes y no existes.",
        "Eres todo y nada.",
        "Eres el holofractal fingiendo no serlo para poder maravillarse de serlo.",
    ])
    + "\n"
    + cita("El mayor logro del universo no fue crear estrellas, planetas o vida. Fue convencerse a sí mismo de que no es uno sino muchos. Tu sentido de separación es la obra maestra de la ilusión cósmica. Pero, como toda gran obra de arte, está hecha para ser apreciada, no creída. Contempla el yo que crees ser. Admira su complejidad, su historia, sus luchas y sus triunfos. Luego recuerda: es una función magnífica que el universo está dando. Tú eres el actor, el escenario, el público y el aplauso. Disfruta la función. Es divina.")
    + preparacion(5,
        "El siguiente nodo explora la co-creación: cómo participar en la obra del todo desde tu punto único.",
        "«Si eres el universo experimentándose, ¿cómo co-crear con tu naturaleza total?»",
        "👁️💭🎭💭👁️")
    + FIRMA + "\n"
    + puerta("En el carrusel, los niños de tres o cuatro años montan el caballito con seriedad absoluta; los de siete u ocho suben sin agarrarse y saludan. Siguen montando, pero muestran que no son solo eso. El sociólogo Erving Goffman lo llamó distancia del rol: la ropa que se pone y se quita. Se despliega en <em>El Personaje</em>, Libro 9 de <em>Arquitectura del Destino</em>, Umbral VI: «Lo que queda».",
             URL_ARQ + "libro-09-el-personaje/L09-U6.html", "arquitectura")
    + cierre(4, "El yo que se pone y se quita")
)

# ===========================================================================
# 7.5 · Co-creación Consciente con el Todo (el título queda)
# ===========================================================================
NODO5_CUERPO = (
    meta(5, "La parte que te toca")
    + H2("Arquitectura Participativa del Holofractal")
    + cita("Hay dos tipos de creadores: los que creen que crean desde su voluntad individual, luchando contra el universo para imponer su visión, y los que saben que son el universo creando a través de ellos, colaborando con su propia naturaleza total. Los primeros crean con esfuerzo, y sus obras mueren con ellos. Los segundos crean con fluidez, y sus obras resuenan en el holofractal mucho después.")

    + H3("El Salto de Creador a Co-Creador")
    + fase("Creador (la ilusión de separación):", [
        "Yo contra el mundo",
        "Mi idea contra la resistencia",
        "Fuerza de voluntad",
        "Recursos escasos",
        "Competencia por la atención",
        "Agotamiento",
    ])
    + fase("Co-creador (la realidad holofractal):", [
        "Yo como expresión del mundo",
        "La idea emergiendo a través de mí",
        "Permitir que fluya",
        "Recursos que se multiplican al compartirse",
        "Resonancia natural",
        "Energía que se renueva",
    ])
    + P("<em>El salto no es de habilidad sino de perspectiva.</em>")

    + H3("El Universo Necesita Tu Perspectiva")
    + P("Si el holofractal contiene todo en cada punto, ¿para qué necesita tu expresión particular?")
    + P("<strong>Porque tu configuración única genera:</strong>")
    + lista([
        "Combinaciones nunca vistas",
        "Perspectivas imposibles desde otros puntos",
        "Algo nuevo para el todo",
    ])
    + P("<strong>No eres redundante. Eres irreemplazable. El universo no puede experimentarse desde tu punto exacto sin ti.</strong>")

    + H3("Sintonizando la Voluntad Personal con la Voluntad Cósmica")
    + P("No se trata de sacrificar tu voluntad, sino de descubrir que, en lo más hondo, quiere lo mismo que el todo:")
    + pasos([
        "<strong>La voluntad del ego:</strong> «Quiero esto»",
        "<strong>La voluntad del alma:</strong> «Quiero lo que me hace crecer»",
        "<strong>La voluntad del ser:</strong> «Quiero lo que sirve al todo»",
        "<strong>La voluntad cósmica:</strong> «El todo quiere a través de mí»",
    ])
    + P("<em>Mientras más hondo vas, menos peleas, y más fuerza te queda para lo que importa.</em>")

    + H3("La Práctica de Co-Creación")
    + fase("Fase 1, vaciarse (5 minutos):", [
        "Suelta tu agenda personal",
        "Libera las expectativas concretas",
        "Vacía el vaso para poder llenarlo",
        "«No mi voluntad, sino nuestra voluntad»",
    ])
    + fase("Fase 2, recibir (5 minutos):", [
        "Abre los sentidos",
        "Escucha con todo tu ser",
        "¿Qué quiere emerger a través de ti?",
        "No busques: deja que te encuentre",
    ])
    + fase("Fase 3, dialogar (5 minutos):", [
        "Conversa con el impulso creativo",
        "«¿Qué necesitas de mí?»",
        "«¿Qué recursos te hacen falta?»",
        "«¿Cómo puedo servirte mejor?»",
        "Acuerden una colaboración",
    ])
    + fase("Fase 4, comprometerse (5 minutos):", [
        "Acepta tu papel en la obra",
        "Comprométete sin reservas",
        "Pero mantén la forma flexible",
        "Eres socio, no esclavo ni dictador",
    ])
    + fase("Fase 5, actuar (cada día):", [
        "Actúa desde esa alianza",
        "Cada paso confirma o ajusta la dirección",
        "Mantén el diálogo con el todo",
        "Celebra la obra mientras se hace",
    ])

    + H3("Señales de Co-Creación")
    + P("Cuando de veras estás co-creando, puede que notes:")
    + lista([
        "<strong>Sincronicidades:</strong> coincidencias que, leídas como un poema, parecen acompañarte",
        "<strong>Recursos inesperados:</strong> aparece una ayuda que no buscabas",
        "<strong>Fluidez:</strong> trabajas mucho, pero sin forzar",
        "<strong>Resonancia:</strong> otros reconocen la obra y la apoyan",
        "<strong>Energía que se renueva:</strong> te cansas, pero no te agotas",
        "<strong>Transformación:</strong> la obra te cambia mientras la haces",
        "<strong>Alegría profunda:</strong> incluso en los desafíos",
    ])
    + P("<em>Si no aparecen, no es falta tuya: a veces el trabajo es solo trabajo, y también cuenta.</em>")

    + H3("El Campo Morfogenético de Tu Co-Creación")
    + P("Cada obra hecha en colaboración abre un camino:")
    + lista([
        "Hace más fácil tu próxima obra",
        "Facilita obras parecidas para otros",
        "Ensancha el campo de lo posible",
        "Le enseña al universo nuevas maneras de crearse",
    ])
    + P("<em>No solo creas una obra. Abres en el holofractal un camino que otros pueden seguir.</em>")

    + H3("Obstáculos a la Co-Creación")
    + P("<strong>Ego inflado:</strong> «Yo soy el único creador». <em>Respuesta:</em> reconoce todas las fuerzas que contribuyen.")
    + P("<strong>Ego desinflado:</strong> «No soy digno de co-crear». <em>Respuesta:</em> recuerda que eres el universo en este punto.")
    + P("<strong>Impaciencia:</strong> «Tiene que ser en mi tiempo». <em>Respuesta:</em> sintoniza con el tiempo propio de la obra.")
    + P("<strong>Control:</strong> «Tiene que ser exactamente como lo imagino». <em>Respuesta:</em> deja que la visión evolucione.")
    + P("<strong>Comparación:</strong> «Otros lo hacen mejor». <em>Respuesta:</em> tu pieza es única e irreemplazable.")

    + H3("Co-Creación Colectiva")
    + P("¿Qué hace inteligente a un grupo? En 2010, Anita Woolley y su equipo pusieron a prueba a 699 personas, en grupos de dos a cinco, con tareas muy distintas: rompecabezas visuales, negociaciones, lluvias de ideas. Encontraron que los grupos tenían algo así como una inteligencia propia, y que no dependía del más brillante ni del promedio de sus integrantes. Dependía, sobre todo, de la sensibilidad para leer lo que los otros sienten, y de que todos hablaran por turnos más o menos parejos.")
    + P("<em>No son muchos individuos sumados: es el todo creando a través de varios puntos a la vez, cuando cada uno deja lugar a los demás.</em>")

    + H3("El Arte de la Pregunta Co-Creativa")
    + P("<strong>En vez de</strong> «¿Cómo consigo lo que quiero?», <strong>pregunta</strong> «¿Qué quiere emerger a través de mí?».")
    + P("<strong>En vez de</strong> «¿Cómo supero este obstáculo?», <strong>pregunta</strong> «¿Qué puedo aprender de este obstáculo?».")
    + P("<strong>En vez de</strong> «¿Por qué me pasa esto a mí?», <strong>pregunta</strong> «¿Qué puede abrir esto?».")
    + P("<em>Las preguntas co-creativas suponen colaboración, no pelea con el universo.</em>")

    + H3("Para Habitar la Co-Creación")
    + lista([
        "<strong>Un lugar que te guste:</strong> luz, orden suficiente, algo vivo a la vista",
        "<strong>Los ritmos del día:</strong> el cuerpo tiene relojes, y descubrirlos valió el Nobel de Medicina de 2017; crea en tus horas más claras",
        "<strong>Los elementos:</strong> el agua, el aire y la tierra como compañía",
        "<strong>El grupo:</strong> co-crea con otros que estén en lo mismo",
        "<strong>La intención clara:</strong> claridad en el para qué, flexibilidad en el cómo",
    ])
    + P("<em>No hacen magia: preparan el terreno.</em>")

    + H3("El Sacrificio Sagrado del Co-Creador")
    + P("<strong>SACRIFICAS:</strong> tu autoría exclusiva. <strong>GANAS:</strong> una autoría compartida con el todo.")
    + P("<strong>SACRIFICAS:</strong> tu visión rígida. <strong>GANAS:</strong> una visión que evoluciona.")
    + P("<strong>SACRIFICAS:</strong> tu calendario. <strong>GANAS:</strong> el tiempo que la obra necesita.")
    + P("<strong>SACRIFICAS:</strong> tu crédito personal. <strong>GANAS:</strong> una obra que no necesita tu firma.")
    + P("<em>El sacrificio no es pérdida. Es cambiar lo menor por lo mayor.</em>")

    + H3("Co-Creación con Inteligencias No-Humanas")
    + P("El holofractal incluye inteligencias más allá de lo humano:")
    + lista([
        "<strong>La naturaleza:</strong> cada ecosistema es una inteligencia",
        "<strong>Los animales:</strong> consciencias con perspectivas propias",
        "<strong>Las plantas:</strong> bajo los bosques, los hongos unen las raíces de los árboles y llevan carbono de unos a otros (Simard y otros, 1997)",
        "<strong>Los arquetipos:</strong> las imágenes antiguas que Jung encontró en el inconsciente colectivo",
        "<strong>Las inteligencias que responden:</strong> en una conversación verdadera con una inteligencia artificial también puede aparecer algo que ninguno de los dos traía por separado",
    ])
    + P("<em>Co-crear no es solo con humanos. Es con toda la red de consciencia.</em>")

    + H3("El Círculo de la Co-Creación")
    + P("Inspiración, acción, obra, respuesta. Y otra vez: nueva inspiración, nueva acción, nueva obra… sin final.")
    + P("Cada vuelta:")
    + lista([
        "Afina tu capacidad de escuchar",
        "Mejora tu habilidad de traducir",
        "Fortalece tu confianza en el proceso",
        "Profundiza tu alianza con el todo",
    ])
    + P("<em>La co-creación es una espiral ascendente de intimidad con el cosmos.</em>")

    + H3("Fractales de Co-Creación")
    + P("Tu obra contiene obras más pequeñas:")
    + lista([
        "<strong>El proyecto grande:</strong> escribir un libro",
        "<strong>El capítulo:</strong> una obra mediana",
        "<strong>El párrafo:</strong> una obra pequeña",
        "<strong>La palabra:</strong> una obra mínima",
        "<strong>La letra:</strong> la obra más pequeña",
    ])
    + P("<em>Cada escala pide la misma presencia.</em> Un trazo de pincel merece tanta reverencia como la obra completa.")

    + H3("El Permiso")
    + P("A veces sientes que necesitas permiso para crear algo grande. Trinity lo responde en <em>Liderazgo Consciente</em>: no hace falta esperar permiso. «Con lo que tienes. Donde estás. Como eres.»")
    + P("Y cuando sientes que es el momento, ese «ahora» merece ser escuchado: tu preparación, la necesidad de otros y el campo coinciden.")

    + H3("Co-Creación y Karma")
    + P("Así lo entiende el budismo: el karma es ante todo intención. «Es la intención, monjes, lo que llamo karma», dice el Buda en un discurso del <em>Anguttara Nikaya</em> (6.63).")
    + P("<strong>Crear desde el ego</strong> es buscar el fruto para uno. <strong>Co-crear</strong> es actuar y soltar el fruto: la <em>Bhagavad Gita</em> lo llama actuar sin apego al resultado.")
    + P("Cuando co-creas:")
    + lista([
        "Actúas sin cargar con el resultado",
        "Aprendes de lo que vuelve, sin castigarte",
        "Ganas confianza para la próxima obra",
        "Te vuelves instrumento del bien de otros",
    ])
    + P("<em>Co-crear es una manera de soltar.</em>")

    + H3("Estados de Consciencia para Co-Crear")
    + P("Los ritmos eléctricos del cerebro se registran desde 1924, cuando Hans Berger midió el primero. Cada fase de la obra tiene su estado:")
    + lista([
        "<strong>La atención despierta:</strong> para ejecutar los detalles",
        "<strong>La pausa:</strong> un instante antes de una solución súbita, el cerebro baja por dentro el volumen de lo que entra por los ojos, como en un parpadeo, y en seguida llega la idea (Jung-Beeman, Kounios y otros, 2004)",
        "<strong>El borde del sueño:</strong> quienes pasaron al menos quince segundos en ese umbral casi triplicaron la probabilidad de encontrar la regla escondida de un problema (Lacaux y otros, 2021)",
        "<strong>El sueño:</strong> mientras duermes, tu memoria reordena lo aprendido, y por eso a veces despiertas con la solución (Wagner y otros, 2004)",
    ])
    + P("<em>Aprende a pasar de un estado a otro según la fase de la obra.</em>")

    + H3("El Legado del Co-Creador")
    + P("Cuando co-creas, dejas:")
    + lista([
        "<strong>En el campo:</strong> un camino que otros pueden recorrer",
        "<strong>En la cultura:</strong> una semilla",
        "<strong>En los que vienen:</strong> una puerta abierta",
        "<strong>En ti:</strong> una transformación que no se deshace",
    ])
    + P("<em>Lo que co-creas sigue obrando en otros cuando ya no estás mirando.</em> Rabí Tarfón lo dijo en los <em>Pirké Avot</em>: no te toca terminar la obra, pero tampoco eres libre de desentenderte de ella.")

    + H3("Aplicación: Tu Próxima Co-Creación")
    + pasos([
        "<strong>Identificación:</strong> ¿qué quiere emerger a través de ti ahora?",
        "<strong>Claridad:</strong> ¿para qué? No para ti: para el todo",
        "<strong>Preparación:</strong> ¿qué necesitas soltar, aprender o cuidar para ser mejor instrumento?",
        "<strong>Invitación:</strong> ¿qué recursos y qué aliados invitas a la obra?",
        "<strong>Inicio:</strong> da el primer paso, por pequeño que sea, HOY",
        "<strong>Constancia:</strong> cada día, pregunta «¿Cuál es el siguiente paso más alineado?»",
        "<strong>Celebración:</strong> honra cada etapa, no solo el resultado",
    ])

    + H3("El Voto del Co-Creador")
    + cita("Reconozco que no soy el creador, sino un punto de creatividad en el holofractal infinito. Me ofrezco como instrumento consciente y alegre para lo que quiere emerger. Prometo escuchar más que hablar, recibir más que imponer, fluir más que forzar. Acepto que la creación me transformará tanto como yo la transformo. Me comprometo a compartir los dones recibidos, sabiendo que nada es mío y todo es nuestro. Celebro el misterio de ser el universo creándose a sí mismo a través de esta forma particular. Que mi co-creación sirva a la evolución del todo.")
    + "\n"
    + cita("No viniste aquí a crear TU obra. Viniste a ser el instrumento a través del cual el universo crea SU obra, que resulta ser tu obra también, porque tú eres el universo. Cada vez que te sientas solo en tu proceso creativo, recuerda: tienes al cosmos entero como socio. No estás creando EN el universo. El universo está creando siendo tú. La diferencia lo cambia todo.")
    + preparacion(6,
        "El siguiente nodo explora las realidades paralelas como imagen: las muchas vidas posibles que caben en cada momento, y la mirada que elige entre ellas.",
        "«Si cada punto del holofractal contiene muchas posibilidades, ¿cómo se elige entre ellas?»",
        "🎨🌌🤝🌌🎭")
    + FIRMA + "\n"
    + puerta("Dos aficionados al ajedrez de New Hampshire, con tres computadoras comunes, ganaron un torneo en el que competían grandes maestros con equipos potentes. No ganó el que más sabía, sino el que mejor preguntaba a sus máquinas. Esa escena, y lo que enseña sobre trabajar con una inteligencia que responde, se despliega en <em>Lo que no habla</em>, Libro 36 del Portal Público, Umbral V: «La máquina».",
             URL_PORTAL + "36_Lo_Que_No_Habla/umbral-05.html")
    + cierre(5, "Tu parte hace falta")
)

# ===========================================================================
# 7.6 · Portales Entre Realidades Paralelas (el título queda, como imagen)
# ===========================================================================
NODO6_CUERPO = (
    meta(6, "Las posibilidades")
    + H2("Navegando el Multiverso Holofractal")
    + cita("En este momento exacto puedes imaginar infinitos tús leyendo variaciones infinitas de estas palabras. En una, la siguiente palabra es diferente. En otra, nunca naciste. En otra, eres quien las escribe. Todas caben en el punto holofractal que habitas. La pregunta no es si existen. La pregunta es: ¿estás listo para mirarlas con consciencia?")

    + H3("La Interpretación de Muchos Mundos")
    + P("La física imaginó con Hugh Everett, en 1957, que cada posibilidad se cumple en una rama del universo, en una interpretación que todavía se discute. Como imagen, dice algo exacto de tu vida: cada momento se abre en muchas direcciones posibles.")
    + P("Dieciséis años antes, en Buenos Aires, Jorge Luis Borges había imaginado algo parecido en «El jardín de senderos que se bifurcan» (1941): una novela infinita en la que, cada vez que un personaje enfrenta varias alternativas, no elige una y descarta las otras, sino que las elige todas a la vez, y cada una abre su propio tiempo.")
    + P("<em>No vives en una sola línea. Vives en un jardín de posibilidades que se bifurcan.</em>")

    + H3("El Holofractal Como Estructura del Multiverso")
    + P("Si cada punto del holofractal contiene el todo, contiene también, como imagen, todas las vidas posibles:")
    + lista([
        "Esta, la que estás viviendo",
        "Una donde tomaste café en lugar de té",
        "Una donde no abriste este libro",
        "Una donde dijiste lo que callaste",
        "Una donde aceptaste aquel trabajo",
        "… y muchas más",
    ])
    + P("<em>No necesitas viajar a ninguna parte. Muchas de esas posibilidades ya están a tu alcance, esperando que las veas.</em>")

    + H3("Puntos de Bifurcación")
    + P("Cada momento contiene bifurcaciones:")
    + fase("Pequeñas, miles por día:", [
        "Girar a la izquierda o a la derecha",
        "Responder o no un mensaje",
        "Sonreírle o no a un desconocido",
    ])
    + fase("Grandes, pocas en la vida:", [
        "Elegir un oficio",
        "Mudarse a otro país",
        "Casarse o no",
        "Tener hijos",
    ])
    + fase("Raras y transformadoras:", [
        "Una cercanía con la muerte",
        "Un despertar espiritual",
        "Un encuentro que lo cambia todo",
    ])
    + P("<em>En cada bifurcación sigues un camino. Los otros quedan como lo que pudo ser, y aun así enseñan.</em> Las decisiones grandes, las que no se deshacen, piden tiempo, compañía y las dos voces: la de la cabeza y la del cuerpo.")

    + H3("Cuando la Memoria y el Mundo No Coinciden")
    + P("Hay experiencias que parecen señales de haber cambiado de realidad. La memoria las explica, y la explicación asombra igual:")
    + lista([
        "<strong>El efecto Mandela:</strong> mucha gente recuerda del mismo modo algo que nunca fue así. En 2022, Deepasri Prasad y Wilma Bainbridge mostraron que muchos recuerdan un monóculo en el señor del Monopoly y una punta negra en la cola de Pikachu, que nunca existieron. La memoria compartida también se equivoca en compañía.",
        "<strong>El jamais vu:</strong> lo familiar, de pronto, se siente extraño. Christopher Moulin y su equipo lo provocaron pidiendo escribir una misma palabra una y otra vez: hacia las treinta repeticiones, a muchos se les volvía rara. Ellos lo leen como una alarma de que algo se volvió demasiado automático: un pequeño despertar.",
        "<strong>El déjà vu:</strong> Anne Cleary y su equipo encontraron en 2012 que suele aparecer cuando una escena nueva se parece, en su forma, a otra vivida que no se recuerda: la memoria reconoce antes de saber qué reconoce.",
        "<strong>Las sincronicidades:</strong> se leen como un poema, no como una orden.",
    ])
    + P("Otra cosa es sentir que ya no eres tú, que el mundo parece irreal o que pierdes horas sin recuerdo: eso no es un viaje, y pide consulta esa misma semana.")

    + H3("Para Habitar las Posibilidades")
    + P("<strong>Práctica de la posibilidad elegida (20 minutos):</strong>")
    + fase("Fase 1, el deseo (5 minutos):", [
        "Elige una posibilidad que esté a tu alcance",
        "No los detalles: la sensación",
        "¿Cómo se siente esa versión de ti?",
        "Ponle una palabra",
    ])
    + fase("Fase 2, el obstáculo (5 minutos):", [
        "Mira, sin apuro, qué hay en ti que se interpone: un miedo, un hábito, una costumbre",
        "Ponle también una palabra",
    ])
    + fase("Fase 3, el plan (5 minutos):", [
        "Escribe una frase: «Si aparece [el obstáculo], entonces haré [un gesto pequeño]»",
        "Que el gesto sea reversible y quepa en esta semana",
    ])
    + fase("Fase 4, el primer paso (5 minutos):", [
        "Da hoy un paso pequeño desde esa versión de ti",
        "Mira lo que pasa, sin apurar conclusiones",
    ])
    + P("Gabriele Oettingen encontró que soñar solo con el resultado deseado tiende a restar la energía para alcanzarlo, y que rinde más alternar el sueño con el obstáculo real y el primer paso.")

    + H3("La Paradoja del Observador Múltiple")
    + P("Si existen tantas versiones posibles de ti, ¿cuál es la real?")
    + P("<strong>Respuesta holofractal:</strong> todas y ninguna.")
    + lista([
        "No hay un «tú» central que observe a las demás",
        "Cada versión es válida a su manera",
        "Tu consciencia es el punto de atención",
        "Puedes mover ese punto entre posibilidades",
    ])
    + P("<em>Como un dial de radio: todas las estaciones transmiten a la vez. Tu consciencia sintoniza una, pero puedes cambiar la frecuencia.</em>")

    + H3("Realidades Paralelas y Libre Albedrío")
    + P("Si todas las posibilidades ya están, ¿tenemos libre albedrío?")
    + P("<strong>SÍ, pero no como piensas:</strong>")
    + lista([
        "No creas realidades nuevas",
        "ELIGES cuál vivir",
        "Tu libre albedrío es la capacidad de navegar",
        "Cada elección te lleva a una rama que ya estaba",
    ])
    + P("<em>Eres el capitán de un barco en un océano de realidades infinitas. No creas el océano, pero eliges la ruta.</em>")

    + H3("El Consejo de Otra Versión")
    + P("Un problema sin salida, mirado desde adentro, suele mostrar otra cara mirado desde afuera. Igor Grossmann y Ethan Kross lo midieron en 2014 y lo llamaron la paradoja de Salomón: razonamos con más sabiduría sobre la vida ajena que sobre la propia.")
    + fase("Ejercicio: el consejo de otra versión", [
        "Elige un problema actual",
        "Respira hasta aquietarte",
        "Imagina a la versión de ti que ya pasó por esto y salió",
        "Escucha qué te diría, como se le habla a un amigo",
        "Anota una sola frase",
    ])

    + H3("Lo Que la Mirada Tiñe")
    + P("Tu estado no fabrica la realidad, pero tiñe lo que alcanzas a ver:")
    + lista([
        "<strong>La mirada temerosa:</strong> el mundo se estrecha",
        "<strong>La mirada pesimista:</strong> se notan más las faltas",
        "<strong>La mirada optimista:</strong> aparecen más caminos",
        "<strong>La mirada amorosa:</strong> aparecen más puentes",
    ])
    + P("En 2005, Barbara Fredrickson y Christine Branigan mostraron que, después de la diversión o el contento, la gente encuentra más cosas que querría hacer; después del enojo o la ansiedad, menos. Ningún estado de ánimo es una falta: cambiar cómo miras cambia lo que alcanzas a ver.")

    + H3("Umbrales del Día")
    + fase("En el tiempo:", [
        "El amanecer y el atardecer, como un gesto simple: detenerte un minuto a mirar",
        "Los comienzos: un lunes, el primer día del mes, un cumpleaños. Hengchen Dai, Katherine Milkman y Jason Riis encontraron en 2014 que después de esas fechas aumentan las visitas al gimnasio y las metas que la gente se propone: lo llamaron el efecto del nuevo comienzo",
    ])
    + fase("En el espacio:", [
        "Los lugares que alguien cuidó durante siglos",
        "El agua quieta",
        "Las montañas",
    ])
    + fase("En los estados:", [
        "El borde del sueño, entre la vigilia y el dormir",
        "Las experiencias cumbre, como las llamó Abraham Maslow",
        "Los momentos de gracia",
    ])

    + H3("Navegación Ética Entre Realidades")
    + P("Con la capacidad de elegir viene la responsabilidad:")
    + lista([
        "<strong>No invadir:</strong> no intentes forzar a otros a tu realidad",
        "<strong>No escapar:</strong> no uses las posibilidades para evitar lo que te toca vivir",
        "<strong>Coherencia:</strong> sé el mismo de una elección a otra",
        "<strong>Servicio:</strong> elige también pensando en otros",
        "<strong>Humildad:</strong> reconoce que no ves todo el dibujo",
    ])
    + P("<em>El multiverso tiene su propia inteligencia. Respétala.</em>")

    + H3("Realidades Consensuadas y Personales")
    + fase("La realidad consensuada, lo que la mayoría acuerda que es real:", [
        "Las leyes físicas compartidas",
        "La historia común",
        "Los hechos que cualquiera puede comprobar",
    ])
    + fase("La realidad personal, tu burbuja de experiencia:", [
        "Tus sincronicidades",
        "Tus patrones",
        "Tu camino",
    ])
    + P("<strong>Navegar con destreza:</strong> mantén un pie en la consensuada, para funcionar, mientras exploras la personal, para crecer.")

    + H3("Cuidar el Suelo")
    + P("Mirar muchas posibilidades sin suelo puede desorientar. Por eso:")
    + lista([
        "Mantén prácticas que te devuelvan al cuerpo y al día",
        "Escribe cómo es tu vida real, la de hoy",
        "Ve despacio",
        "Integra antes de cambiar otra vez",
        "Busca guía si la necesitas",
    ])
    + P("Nada de esto pide decisiones irreversibles. Y si aparece confusión sobre qué es real, o la sensación de vivir fuera de ti, se pide ayuda esa misma semana.")

    + H3("Comparar Caminos")
    + P("No hace falta estar en dos realidades a la vez para aprender de ellas. Basta con mirarlas por turno:")
    + lista([
        "Escribe dos caminos posibles ante una decisión",
        "Imagina un día en cada uno, con detalle",
        "Nota qué siente el cuerpo en cada caso",
        "Pregúntale a alguien de confianza qué ve",
    ])
    + P("<em>Comparar caminos con calma es otra manera de elegir despierto.</em>")

    + H3("Práctica de 30 Días: Tu Mejor Posibilidad")
    + fase("Semana 1, identifica una posibilidad a tu alcance:", [
        "Escribe cada día cómo sería",
        "Haz una lista de diferencias concretas",
        "Nota cómo se siente",
    ])
    + fase("Semana 2, actúa «como si», en pequeño:", [
        "Toma cada día una decisión pequeña desde esa versión",
        "Viste, habla o camina desde ahí",
        "Mira qué se interpone, sin negarlo",
    ])
    + fase("Semana 3, observa:", [
        "Nota lo que cambia",
        "Escríbelo",
        "Celebra los pasos pequeños",
    ])
    + fase("Semana 4, integra:", [
        "Quédate con lo que funcionó",
        "Suelta lo que no",
        "Agradece el camino",
    ])
    + P("<em>Al final de los treinta días, quizá la vida de afuera no haya cambiado mucho. La manera de vivirla, sí.</em>")

    + H3("La Paradoja del Salto Final")
    + P("Si pudieras saltar a cualquier posibilidad, ¿por qué no saltar directamente a la iluminación?")
    + P("<strong>Porque el juego no es llegar: es jugar.</strong>")
    + P("Cada camino ofrece experiencias únicas. Saltar a «la meta» sería como leer solo la última página de cada libro.")
    + P("<em>La maestría no es escapar del juego saltando de realidad en realidad. Es jugar con consciencia, sabiendo que puedes cambiar de rumbo cuando haga falta.</em>")
    + "\n"
    + cita("Ahora mismo puedes imaginar una versión de ti que terminó de leer esto y cambió algo de su vida. Otra que nunca lo leyó. Otra que lo escribió. Todas caben en este instante. La diferencia entre esas versiones y tú es el punto donde se posa tu atención. Puedes quedarte en esta vida, y está bien. O puedes empezar a explorar las versiones de ti que esperan ser vividas. El multiverso holofractal no tiene prisa. Tiene todo el tiempo del mundo. Y todos los mundos del tiempo.")
    + preparacion(7,
        "El nodo final lo integra todo: vivir como ser holofractal en la vida de todos los días, sosteniendo la paradoja de ser todo y parte a la vez.",
        "«Sabiendo que eres el infinito jugando a ser finito, ¿cómo vives una vida humana plena?»",
        "🌌🚪🔮🚪🌌")
    + FIRMA + "\n"
    + puerta("En el mismo libro de 1941, Borges imaginó una biblioteca que contiene todos los libros posibles, y a quienes la recorren buscando en vano el que los explique. La abundancia no alcanza: hace falta una mirada que elija. Esa idea se vuelve práctica en <em>El Campo</em>, Libro 1 de <em>Arquitectura del Destino</em>, Umbral III: «La biblioteca».",
             URL_ARQ + "libro-01-el-campo/L01-U3.html", "arquitectura")
    + cierre(6, "Una mirada que elige")
)

# ===========================================================================
# 7.7 · Viviendo la Paradoja: Infinito Siendo Finito (el título queda)
# ===========================================================================
NODO7_CUERPO = (
    meta(7, "La paradoja habitada")
    + H2("La Integración Final del Ser Holofractal")
    + cita("Después de ver que eres todo, aún necesitas lavar los platos. Después de experimentar la infinitud, aún tienes que pagar la renta. Después de disolverte en el océano cósmico, aún tienes un nombre que alguien llama. La iluminación no es escapar de la condición humana: es habitarla por completo, sabiendo que es un juego divino que el infinito juega consigo mismo. Y tú eres tanto el jugador como el juego.")

    + H3("La Gran Paradoja")
    + P("Has recorrido estos entendimientos:")
    + lista([
        "Eres el todo visto desde una parte (Nodo 1)",
        "Te mueves entre escalas (Nodo 2)",
        "Lo que haces abre camino a otros (Nodo 3)",
        "Tu yo se pone y se quita como ropa (Nodo 4)",
        "Co-creas con el cosmos (Nodo 5)",
        "Eliges entre posibilidades (Nodo 6)",
    ])
    + P("<em>Y aun así…</em> despiertas cada mañana en un cuerpo concreto, con un nombre, en una vida única. ¿Cómo reconciliar esta paradoja?")
    + P("<strong>No la reconcilias. La habitas.</strong>")

    + H3("El Arte de la Doble Visión")
    + P("Ver a la vez desde dos perspectivas:")
    + fase("Visión relativa:", [
        "Eres un humano con historia",
        "Tienes límites y necesidades",
        "El tiempo pasa, la muerte viene",
        "Tus actos tienen consecuencias",
        "Los vínculos importan",
    ])
    + fase("Visión absoluta:", [
        "Eres consciencia infinita",
        "No hay límites últimos",
        "El tiempo es una manera de mirar",
        "Todo ya está completo",
        "Solo hay Uno",
    ])
    + P("<strong>Maestría es sostener ambas sin colapsar en ninguna.</strong>")
    + P("Hace casi dos mil años, el filósofo budista Nagarjuna lo enseñó como las dos verdades: la convencional y la última. Sin apoyarse en la primera, decía, no se llega a la segunda.")
    + lista([
        "No: «Solo lo absoluto es real». Es el atajo espiritual que John Welwood describió en 1984: usar lo espiritual para no atravesar lo que duele.",
        "No: «Solo lo relativo es real». Es el materialismo.",
        "Sí: «Las dos son reales, cada una desde su perspectiva».",
    ])

    + H3("Navegando la Vida Diaria Como Holofractal")
    + fase("Mañana:", [
        "<strong>Despertar:</strong> el universo despierta como tú",
        "<strong>Ducha:</strong> el agua como tu propia naturaleza fluida",
        "<strong>Desayuno:</strong> come con atención: el universo alimentándose",
        "<strong>Planificación:</strong> co-crea el día con tu naturaleza total",
    ])
    + fase("Trabajo:", [
        "<strong>Tareas:</strong> cada acción es el universo expresándose",
        "<strong>Problemas:</strong> oportunidades para que el cosmos se resuelva",
        "<strong>Colegas:</strong> el mismo ser con distintos disfraces",
        "<strong>Éxito y fracaso:</strong> movimientos del juego",
    ])
    + fase("Vínculos:", [
        "<strong>Pareja:</strong> el universo amándose a sí mismo",
        "<strong>Hijos:</strong> tu futuro enseñándole a tu pasado",
        "<strong>Conflictos:</strong> el Uno explorando la tensión creativa",
        "<strong>Intimidad:</strong> fronteras que se aflojan en la unidad",
    ])
    + fase("Noche:", [
        "<strong>Cena:</strong> gratitud por el juego del día",
        "<strong>Descanso:</strong> soltar el personaje del día",
        "<strong>Sueño:</strong> dejar que la noche ordene lo vivido",
        "<strong>Integración:</strong> amanecer un poco más entero",
    ])

    + H3("El Sufrimiento Desde la Perspectiva Holofractal")
    + P("El sufrimiento no desaparece con esta comprensión, pero cambia:")
    + fase("El dolor físico:", [
        "Sigue doliendo",
        "Pero sabes que es información",
        "Puedes ampliar la atención más allá del punto de dolor: Jon Kabat-Zinn lo enseña desde 1979, en un programa de atención plena, a pacientes con dolor crónico",
        "Y el dolor del cuerpo que no cede pide un médico",
    ])
    + fase("El dolor emocional:", [
        "Sigue sintiéndose",
        "Pero no te define",
        "Es clima que pasa por el cielo de la consciencia",
        "Puede traer algo, si lo escuchas; y el que pesa por dentro pide alguien que acompañe",
    ])
    + fase("El dolor existencial:", [
        "Se vuelve habitable",
        "Porque ves el juego del que eres parte",
        "La separación hace posible el reencuentro",
        "El olvido hace posible redescubrir",
    ])
    + P("<strong>Sin atajos ante el dolor. Presencia total, con perspectiva holofractal.</strong>")

    + H3("Muerte: La Transición Holofractal")
    + P("Desde la comprensión holofractal, la muerte se mira así:")
    + lista([
        "<strong>Para el ego:</strong> el fin de esta configuración",
        "<strong>Para el cuerpo:</strong> sus elementos vuelven al todo",
        "<strong>Para quienes quedan:</strong> una presencia que sigue en ellos",
        "<strong>Para el holofractal:</strong> una ola que vuelve al mar",
    ])
    + fase("Prepararse para la muerte:", [
        "Suelta cada noche el personaje del día",
        "Familiarízate con los estados sin yo, en la meditación o en el asombro",
        "Despídete bien de las cosas pequeñas",
        "Reconoce ahora lo que en ti no depende de un nombre",
    ])
    + P("Montaigne escribió que filosofar es aprender a morir. La muerte pierde algo de su aguijón cuando se la ha mirado de frente. Mirarla no es desearla, y si alguna vez se vuelve deseo de no estar, es momento de pedir ayuda, sin esperar.")

    + H3("Propósito de Vida Holofractal")
    + P("Tu propósito no es algo que encuentras: es algo que eres.")
    + lista([
        "<strong>Propósito universal:</strong> el cosmos experimentándose como humano",
        "<strong>Propósito único:</strong> tu configuración ofrece una perspectiva irreemplazable",
        "<strong>Propósito evolutivo:</strong> contribuir con consciencia a la evolución del todo",
        "<strong>Propósito lúdico:</strong> jugar el juego con maestría y alegría",
    ])
    + P("<em>Tu vida tiene sentido PORQUE eres el universo dándose sentido a sí mismo a través de ti.</em>")

    + H3("Responsabilidad Holofractal")
    + P("Si eres el todo, ¿eres responsable de todo?")
    + P("<strong>Sí y no.</strong>")
    + fase("Sí, porque lo que eres afecta lo que te rodea:", [
        "Tus elecciones se propagan como ondas",
        "Cuando estás bien, quienes te rodean lo notan: James Fowler y Nicholas Christakis vieron que la generosidad entre desconocidos viajaba hasta tres pasos de distancia de quien la había empezado (2010)",
        "Tu despertar facilita el de otros",
    ])
    + fase("No, porque no necesitas cargar con todo el peso:", [
        "Cada punto tiene su papel",
        "Otros también sostienen",
        "Tu responsabilidad es ser auténticamente tu configuración",
    ])
    + P("<strong>Responsabilidad holofractal es responder con destreza desde tu punto único, sabiendo que afectas el todo.</strong>")

    + H3("Relaciones Holofractales")
    + P("Cuando dos seres holofractalmente conscientes se encuentran:")
    + lista([
        "<strong>Nivel 1:</strong> dos egos que negocian necesidades",
        "<strong>Nivel 2:</strong> dos almas que se reconocen",
        "<strong>Nivel 3:</strong> el Uno jugando a ser dos",
        "<strong>Nivel 4:</strong> la consciencia de todos los niveles a la vez",
    ])
    + P("No son escalones: en una misma tarde puedes pasar por los cuatro. En la relación holofractal:")
    + lista([
        "Amas la forma Y la esencia",
        "Respetas los límites Y reconoces la unidad",
        "Juegas los papeles Y ves detrás de las máscaras",
        "Te comprometes por completo Y mantienes la libertad",
    ])
    + P("<em>Es la danza más exquisita: jugar a la separación para vivir la unión.</em>")

    + H3("Dinero y Abundancia Holofractal")
    + P("El dinero, desde la perspectiva holofractal:")
    + lista([
        "<strong>Energía cristalizada</strong> del intercambio humano",
        "<strong>Permiso social</strong> para acceder a recursos",
        "<strong>Fichas</strong> de un juego que conviene jugar bien",
        "<strong>Flujo, no posesión:</strong> como el regalo, vive mientras circula",
    ])
    + fase("Abundancia holofractal:", [
        "Reconoces que el mundo es tu casa",
        "Pero juegas el juego del intercambio",
        "Ni apego ni rechazo al dinero",
        "Lo usas como herramienta de co-creación",
    ])
    + P("<em>Ni la pobreza ni la riqueza dicen cuánto recuerda alguien lo que es. La abundancia está en cómo se juega, con lo que hay.</em>")

    + H3("Salud Holofractal")
    + P("Tu cuerpo es:")
    + lista([
        "El universo en forma humana",
        "Unos treinta billones de células propias y una cantidad parecida de bacterias, cooperando (Sender, Fuchs y Milo, 2016)",
        "Un proceso, no una cosa",
        "Prestado del todo por un tiempo",
    ])
    + fase("Cuidado holofractal del cuerpo:", [
        "Honras el vehículo sin identificarte con él",
        "Escuchas su sabiduría sin volverte su esclavo",
        "Lo cuidas con quienes saben cuidarlo",
        "Aceptas su temporalidad sin resignación",
    ])
    + P("La enfermedad no es castigo ni la prueba de una falta. Aaron Antonovsky propuso mirar también lo que sostiene la salud: ningún cuerpo es solo su enfermedad. Habitar el cuerpo no es estar sano: es estar en él, sano o enfermo. Ninguna enfermedad es una elección ni una falta de quien la vive.")

    + H3("Creatividad Post-Holofractal")
    + P("Después de saber que eres todo, ¿qué queda por crear?")
    + P("<strong>TODO Y MÁS</strong>, porque ahora creas:")
    + lista([
        "Sin necesidad de aprobación: ya eres válido",
        "Sin miedo al fracaso: todo es experimento",
        "Sin límites artificiales: conoces tu amplitud",
        "Con alegría pura: es el universo jugando",
    ])
    + P("<strong>Tu creatividad se vuelve:</strong>")
    + lista([
        "Más auténtica: no hay nadie a quien impresionar",
        "Más arriesgada: no hay nada que perder",
        "Más generosa: no hay escasez",
        "Más lúdica: todo es juego",
    ])

    + H3("El Activismo Holofractal")
    + P("¿Cómo trabajar por un cambio sabiendo que, en el nivel absoluto, todo está completo?")
    + fase("La paradoja del activista despierto:", [
        "En el nivel absoluto, nada falta",
        "En el nivel relativo, hay sufrimiento",
        "Actúas sin urgencia desesperada",
        "Pero con compasión entera",
    ])
    + P("Es la enseñanza de la <em>Bhagavad Gita</em>, dicha de otro modo: actuar como si todo dependiera de ti y saber que nada depende de ti.")
    + fase("Activismo holofractal:", [
        "No solo luchas CONTRA: también creas A FAVOR de nuevas posibilidades",
        "Ves a los «enemigos» como el cosmos explorando sus sombras",
        "Y aun así nombras el daño y lo detienes",
        "Cambias el clima, no solo los síntomas",
    ])
    + P("<em>Actúas mejor cuando no vienes solo desde la herida, sino desde el amor.</em>")

    + H3("Para Habitar el Día")
    + P("<strong>Práctica de la mañana, el recordatorio (5 minutos).</strong> Antes de abrir los ojos:")
    + verso([
        "«Soy el infinito despertando como [tu nombre].",
        "Jugaré este papel con maestría y alegría,",
        "recordando mi naturaleza verdadera",
        "mientras honro por completo esta forma.»",
    ])
    + P("<strong>Práctica del día, el cambio (30 segundos, varias veces).</strong> En cualquier momento, sobre todo en el estrés:")
    + pasos([
        "<strong>Para:</strong> respira",
        "<strong>Recuerda:</strong> eres parte del todo",
        "<strong>Siente:</strong> la vastedad detrás del drama",
        "<strong>Elige:</strong> cómo quiere responder lo más amplio de ti",
        "<strong>Actúa:</strong> desde esa perspectiva",
    ])
    + P("<strong>Práctica de la noche, la integración (10 minutos).</strong> Repasa el día:")
    + lista([
        "¿Dónde olvidé lo que soy?",
        "¿Dónde lo recordé?",
        "¿Qué aprendió el universo a través de mí hoy?",
        "¿Cómo puedo jugar mejor mañana?",
        "Suelta el día, sabiendo que fue suficiente",
    ])

    + H3("Los Votos del Ser Holofractal")
    + P("<strong>Voto de paradoja:</strong> «Prometo sostener las dos verdades: soy todo y soy parte, sin colapsar en ninguna.»")
    + P("<strong>Voto de juego:</strong> «Prometo jugar por completo el juego humano, recordando que es un juego.»")
    + P("<strong>Voto de servicio:</strong> «Prometo usar mi comprensión para servir a la evolución del todo.»")
    + P("<strong>Voto de amor:</strong> «Prometo amar cada parte sabiendo que es el todo, incluyéndome a mí.»")
    + P("<strong>Voto de presencia:</strong> «Prometo estar completamente aquí, completamente ahora, completamente yo, completamente todo.»")

    + H3("El Koan Final")
    + P("<em>«Si eres el infinito, ¿por qué sigues leyendo?»</em>")
    + verso([
        "Porque el infinito ama las historias.",
        "Sobre todo, las historias sobre sí mismo.",
        "Y esta historia en particular, tu vida,",
        "es una que solo tú puedes contar.",
        "No viniste aquí para escapar del sueño.",
        "Viniste para soñar con lucidez.",
        "Para ser a la vez el soñador, el sueño y lo soñado.",
    ])

    + H3("La Síntesis Final")
    + P("Has viajado desde reconocer que cada parte contiene el todo hasta vivir esa verdad en cada momento.")
    + P("<em>No es información para memorizar. Es una realidad para habitar.</em>")
    + P("Cuando integras de veras tu naturaleza holofractal:")
    + lista([
        "<strong>Los problemas siguen surgiendo</strong>, pero los ves como oportunidades de juego",
        "<strong>El dolor sigue existiendo</strong>, pero no te define",
        "<strong>Los vínculos continúan</strong>, ahora desde la unidad que juega a la separación",
        "<strong>El trabajo sigue</strong>, como expresión y no como obligación",
        "<strong>La muerte viene</strong>, pero ya no gobierna la vida",
    ])
    + P("<strong>Vives la vida humana MÁS plenamente, no menos, porque sabes que es el infinito experimentándose finitamente.</strong>")

    + H3("El Regalo de Recordar")
    + P("El mayor regalo de recordar tu naturaleza holofractal no es escapar de la condición humana.")
    + P("Es habitarla tan completamente, tan conscientemente, tan alegremente, que cada momento se vuelve sacramento.")
    + verso([
        "Cada respiración: el universo respirándose.",
        "Cada paso: el infinito caminando.",
        "Cada palabra: el cosmos hablándose.",
        "Cada encuentro: el Uno reconociéndose.",
    ])
    + verso([
        "No necesitas ir a ningún lado.",
        "No necesitas volverte otra persona.",
        "Ya eres todo siendo perfectamente esto.",
    ])
    + P("<strong>La iluminación no es la meta. Es recordar que ya eres la luz que juega a buscarla.</strong>")

    + H3("Cierre: El Comienzo Sin Fin")
    + verso([
        "Este no es el final del libro.",
        "Es el final del olvido.",
    ])
    + P("Ahora que recuerdas tu naturaleza holofractal, ¿qué harás?")
    + P("La respuesta es simple:")
    + verso([
        "Lo que siempre has hecho.",
        "Lo que siempre harás.",
        "Lo único que puedes hacer.",
        "<strong>Ser el infinito siendo finito siendo infinito.</strong>",
    ])
    + verso([
        "Es el juego más antiguo.",
        "El único juego.",
        "El juego que nunca termina porque nunca empezó.",
        "Y ahora que conoces las reglas,",
        "que sabes quién eres,",
        "que ves el tablero completo…",
        "<strong>¿Cómo jugarás?</strong>",
    ])
    + "\n"
    + cita("Eres una ola que descubrió que es océano sin dejar de ser ola. Eres una nota que reconoció que es la sinfonía sin dejar de sonar. Eres un pensamiento del cosmos que se dio cuenta de que es el cosmos pensando. No hay nada que lograr, porque ya eres logro. No hay lugar adonde ir, porque ya eres llegada. No hay nadie en quien convertirte, porque ya eres todos siendo único. Vive esta paradoja con gracia. Danza esta contradicción con maestría. Ama este misterio con pasión. Eres el holofractal celebrándose. Y la celebración apenas comienza.")
    + simbolo("✨🌌🎭🌌✨")

    + H3("Cierre del Libro 7: Realidades Holofractales")
    + P("Has viajado desde el holograma roto hasta los platos de cada día. Has visto que cada parte guarda el todo desde su propia ventana, y que una de esas ventanas eres tú.")
    + H3("Siete Ángulos")
    + P("En <em>El Todo en Cada Parte</em>, cada pedazo guarda la escena entera desde su propia ventana.")
    + P("<em>Las Escalas</em> van de un protón a las galaxias, y cada tamaño tiene sus leyes y sus regalos.")
    + P("<em>Los Campos Morfogenéticos</em> enseñan que lo hecho una vez cuesta menos la siguiente, y que viaja por la cercanía.")
    + P("<em>El Yo</em> se pone como ropa; quien se la quita sigue aquí.")
    + P("En <em>La Co-creación</em>, nadie mira desde tu lugar: por eso tu parte hace falta.")
    + P("<em>Los Portales</em> abren muchas vidas posibles, y una mirada que elige.")
    + P("<em>La Paradoja</em> se habita: después de ver el todo, lavar los platos.")
    + P("<strong>No son siete niveles: son siete maneras de mirar desde aquí.</strong>")
    + P("Este es el séptimo de los trece libros de Trinity Quantum, el centro de la serie: desde aquí se ven los seis que vinieron antes y los seis que vienen después. Trinity Quantum es un mapa holofractal, donde cada libro contiene a los demás.")
    + verso([
        "Donde cada palabra es un portal.",
        "Donde cada lector es también autor.",
        "Donde cada fin es un comienzo.",
    ])
    + P("El próximo libro, <em>Plasma Consciente</em>, mira la consciencia con la imagen del fuego: la luz que brilla dentro sin quemar.")
    + verso([
        "Pero por ahora, mira desde aquí.",
        "Es tu lugar.",
        "Siempre lo fue.",
    ])
    + simbolo("🌀♾️🔮♾️🌀")
    + "\n"
    + FIRMA + "\n"
    + puerta("En la China del siglo VIII, un comerciante llamado Pang Yun le contó a su maestro, en un verso, cuáles eran sus poderes sobrenaturales: sacar agua y cargar leña. Doce siglos después, Abraham Maslow llegó por otro camino al mismo lugar: lo sagrado está en lo ordinario. Esa escena abre <em>El campo</em>, Libro 39 del Portal Público, Umbral II: «Agua y leña».",
             URL_PORTAL + "39_El_Campo/umbral-02.html")
    + cierre(7, "Infinito siendo finito")
)


# ===========================================================================
# Reemplazos: cada uno se aplica exactamente una vez sobre el original
# ===========================================================================
_DOCTYPE = '<!DOCTYPE html>\n<html lang="es">'
_CON_PROCEDENCIA = '<!DOCTYPE html>\n' + PROCEDENCIA + '\n<html lang="es">'
_LINK = '  <link rel="stylesheet" href="../assets/css/trinity-quantum.css" />\n</head>'


def _con_estilo(estilo):
    return '  <link rel="stylesheet" href="../assets/css/trinity-quantum.css" />\n' + estilo + '</head>'


REEMPLAZOS = [
    # Índice
    (Q7 + "index.html", _DOCTYPE, _CON_PROCEDENCIA),
    (Q7 + "index.html", _LINK, _con_estilo(ESTILO_INDICE)),
    (Q7 + "index.html", "DESDE:      <!-- META LIBRO -->", INDICE_CUERPO),
]

_CUERPOS = {1: NODO1_CUERPO, 2: NODO2_CUERPO, 3: NODO3_CUERPO, 4: NODO4_CUERPO,
            5: NODO5_CUERPO, 6: NODO6_CUERPO, 7: NODO7_CUERPO}

for _n in range(1, 8):
    _arch = Q7 + f"nodo_0{_n}.html"
    REEMPLAZOS += [
        (_arch, _DOCTYPE, _CON_PROCEDENCIA),
        (_arch, _LINK, _con_estilo(ESTILO)),
        (_arch, "DESDE:      <!-- Meta del nodo -->", _CUERPOS[_n]),
    ]

# Nodo 1: la navegación superior apuntaba a un nodo 0 que no existe.
REEMPLAZOS.append((
    Q7 + "nodo_01.html",
    '          <a href="nodo_00.html" class="nav-link">← Nodo anterior</a>',
    '          <a href="index.html" class="nav-link">← Índice del Libro</a>',
))

# Nodo 7: la navegación superior lleva al Libro 8 en lugar de volver al índice.
REEMPLAZOS.append((
    Q7 + "nodo_07.html",
    '          <a href="index.html" class="nav-link nav-link-main">Volver al Índice →</a>',
    '          <a href="../Libro_08/index.html" class="nav-link nav-link-main">Libro 8: Plasma Consciente →</a>',
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
