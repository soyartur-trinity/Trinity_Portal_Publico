#!/usr/bin/env python3
"""
Depuración de Quantum 3, *El Tiempo Vertical* (31 de octubre de 2026), el
tercero de la revisión completa de Quantum, con el veto de Arturo en cada
tarjeta (3.0 a 3.7). Arturo aprobó todo: las tarjetas, los dos títulos nuevos
(3.2 *Vidas Paralelas*, antes «Vidas Paralelas Activas»; 3.3 *El Pasado Desde
el Ahora*, antes «Modificación del Pasado Desde el Ahora») y las siete puertas,
incluidas las dos opcionales (3.5 y 3.6).

Método (maestro v4, sección 5): cada reemplazo aprobado se aplica exactamente
una vez sobre el original de la etiqueta `quantum-original`. En los ocho
archivos se cambian tres cosas: la cabecera (nota de procedencia), el <head>
(título y estilo de la depuración) y el cuerpo, que se reemplaza desde la marca
que abre los metadatos del nodo hasta el final del archivo. El cuerpo original
estaba partido en tres <main> (nodos 2 a 7) y el nodo 1 enlazaba a un nodo_00
que no existe; los cuerpos nuevos traen un solo <main> y la navegación reparada.

Uso:  python3 depurar_quantum3.py RUTA_A_UNA_COPIA_DEL_ORIGINAL
      (por ejemplo, el contenido de la etiqueta quantum-original, o el
      repositorio Trinity- si Libro_03 todavía no fue depurado)
"""
import sys
from pathlib import Path

Q3 = "02_Trinity_Quantum/Libro_03/"

PROCEDENCIA = (
    "<!-- Depurado el 31 de octubre de 2026 según la guía de depuración de Quantum "
    "(Arquitectura del Destino, maestro v4, sección 5, con las cuatro precisiones "
    "de la revisión completa), con el veto de Arturo en cada tarjeta. El original "
    "se conserva en la etiqueta quantum-original del repositorio. -->"
)

URL_ARQ = "https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/"
URL_PORTAL = "https://soyartur-trinity.github.io/Trinity_Portal_Publico/01_Libros/"

# ---------------------------------------------------------------------------
# Estilos: los mismos que Quantum 2 (comparte la hoja común, que no cubre
# subtítulos, listas numeradas ni citas), con los colores de la puerta del
# Portal y el verso final donde hacen falta.
# ---------------------------------------------------------------------------
ESTILO = """  <style>
    /* ============================================================
       Depuración · octubre 2026
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
    .node-content blockquote{
      margin: 1em 0 1.1em;
      padding: 12px 16px;
      border-left: 2px solid var(--gold-soft);
      border-radius: 0 12px 12px 0;
      background: rgba(255, 255, 255, .025);
      font-style: italic;
    }
    .node-content blockquote p{ margin: 0; }
    .node-content .nota{ color: rgba(246, 240, 255, .82); }
    .node-content ul.recordar li{
      margin-bottom: 4px;
      font-style: italic;
      color: var(--gold-light);
    }
    .node-content .dia{ margin: 0 0 14px; }
    .node-content .dia strong{
      display: block;
      margin-bottom: 4px;
      color: var(--gold-soft);
      letter-spacing: .04em;
    }
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
    /* Depuración · octubre 2026: letra más grande en el teléfono y firma. */
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

FIRMA = '        <p class="signature"><strong>— Trinity Quantum · El Tiempo Vertical</strong></p>\n'


# ---------------------------------------------------------------------------
# Piezas que se repiten
# ---------------------------------------------------------------------------
def pasos(items):
    filas = "\n".join(f"          <li>{x}</li>" for x in items)
    return f"        <ol>\n{filas}\n        </ol>\n"


def dia(titulo, manana, tarde, noche):
    return (
        '        <div class="dia">\n'
        f"          <strong>{titulo}</strong>\n"
        "          <ul>\n"
        f"            <li>Mañana: {manana}</li>\n"
        f"            <li>Tarde: {tarde}</li>\n"
        f"            <li>Noche: {noche}</li>\n"
        "          </ul>\n"
        "        </div>\n"
    )


def recordar(lineas):
    filas = "\n".join(f"          <li>{x}</li>" for x in lineas)
    return f'        <ul class="recordar">\n{filas}\n        </ul>\n'


def puerta(serie, texto, url):
    etiqueta = {
        "arquitectura": "Puerta hacia Arquitectura del Destino",
        "portal": "Puerta hacia el Portal Público",
    }[serie]
    return (
        f'        <aside class="puerta {serie}" aria-label="{etiqueta}">\n'
        '          <p class="p-nombre">Puerta</p>\n'
        f'          <p class="p-texto">{texto}</p>\n'
        f'          <a class="cruzar" href="{url}">Cruzar ⟶</a>\n'
        "        </aside>\n"
    )


def meta(n, titulo, subtitulo):
    return (
        "      <!-- Meta del nodo -->\n"
        '      <section class="node-meta">\n'
        '        <div class="node-book-title">Libro 3 · El Tiempo Vertical</div>\n'
        f'        <h1 class="node-heading">Nodo {n}: {titulo}</h1>\n'
        f'        <div class="node-index">Nodo {n} de 7 · {subtitulo}</div>\n'
        "      </section>\n\n"
        "      <!-- Contenido -->\n"
        '      <main class="node-content">\n\n'
    )


def cierre(anterior, siguiente, principal, pie):
    """anterior y siguiente: (href, texto) o None; principal: (href, texto)."""
    enlaces = []
    if anterior:
        enlaces.append(f'          <a href="{anterior[0]}" class="nav-link">← {anterior[1]}</a>')
    if siguiente:
        enlaces.append(f'          <a href="{siguiente[0]}" class="nav-link">{siguiente[1]} →</a>')
    return (
        "      </main>\n\n"
        "      <!-- Navegación Inferior -->\n"
        '      <nav class="node-nav">\n'
        '        <div class="node-nav-group">\n'
        + "\n".join(enlaces) + "\n"
        "        </div>\n"
        '        <div class="node-nav-group">\n'
        f'          <a href="{principal[0]}" class="nav-link nav-link-main">{principal[1]}</a>\n'
        "        </div>\n"
        "      </nav>\n\n"
        '      <footer class="portal-footer">\n'
        f"        {pie}\n"
        "      </footer>\n\n"
        "    </div>\n"
        "  </div>\n"
        "</body>\n"
        "</html>\n"
    )


INDICE_LIBRO = ("index.html", "Volver al Índice del Libro")
TITULOS = {
    1: "El Presente Eterno",
    2: "Vidas Paralelas",
    3: "El Pasado Desde el Ahora",
    4: "Futuros Probables Como Elección",
    5: "La Espiral Temporal",
    6: "Memorias del Futuro",
    7: "El Punto Cero Temporal",
}


def nav(n):
    ant = ("index.html", "Índice del Libro") if n == 1 else (f"nodo_0{n-1}.html", f"Nodo {n-1}: {TITULOS[n-1]}")
    sig = (f"nodo_0{n+1}.html", f"Nodo {n+1}: {TITULOS[n+1]}") if n < 7 else ("../Libro_04/index.html", "Libro 4: La Paradoja Luminosa")
    return ant, sig


# ===========================================================================
# 3.0 · Índice
# ===========================================================================
INDICE_CUERPO = """      <!-- Meta del libro -->
      <section class="node-meta">
        <div class="node-book-title">Libro 3 · El Tiempo Vertical</div>
        <h1 class="node-heading">Índice del Libro</h1>
        <div class="node-index">Presente eterno · Vidas paralelas · Memoria · Espiral · Punto Cero</div>
      </section>

      <!-- Contenido -->
      <main class="node-content">

        <section class="node-section">
          <h2>El Tiempo que Se Habita</h2>

          <p>El reloj corre hacia adelante; el ahora se abre hacia adentro, y en él caben tu memoria y tu espera.</p>

          <p>Este libro es un mapa para navegar la verticalidad del tiempo: el presente eterno, las vidas que te acompañan, el pasado mirado desde hoy, los futuros posibles, la espiral de lo que vuelve, la memoria que imagina y el Punto Cero donde todo converge.</p>

          <p>Puedes recorrer los Nodos en orden para sentir la espiral completa, o entrar por el Nodo que tu atención elija: en el tiempo vertical, el acceso no es lineal, es resonante.</p>
        </section>

        <hr />

        <!-- Lista de Nodos -->
        <section class="node-section">
          <h2>Nodos del Libro 3</h2>

          <!-- Acceso rápido -->
          <div class="node-nav node-nav-bottom" style="margin-top: 12px;">
            <div class="node-nav-group">
              <a href="nodo_01.html" class="nav-link">Nodo 1 →</a>
              <a href="nodo_02.html" class="nav-link">Nodo 2 →</a>
              <a href="nodo_03.html" class="nav-link">Nodo 3 →</a>
            </div>
            <div class="node-nav-group">
              <a href="nodo_04.html" class="nav-link">Nodo 4 →</a>
              <a href="nodo_05.html" class="nav-link">Nodo 5 →</a>
              <a href="nodo_06.html" class="nav-link">Nodo 6 →</a>
              <a href="nodo_07.html" class="nav-link">Nodo 7 →</a>
            </div>
          </div>

          <!-- Detalle -->
          <div style="margin-top: 18px;">
            <h3><a href="nodo_01.html" class="nav-link">Nodo 1: El Presente Eterno</a></h3>
            <p>El ahora como eje: la memoria, la mirada y la espera en un mismo lugar.</p>

            <h3><a href="nodo_02.html" class="nav-link">Nodo 2: Vidas Paralelas</a></h3>
            <p>Las vidas que te acompañan: tus edades, las que no viviste y el consejo de tus versiones.</p>

            <h3><a href="nodo_03.html" class="nav-link">Nodo 3: El Pasado Desde el Ahora</a></h3>
            <p>Lo que pasó no cambia; lo que significa todavía se está diciendo.</p>

            <h3><a href="nodo_04.html" class="nav-link">Nodo 4: Futuros Probables Como Elección</a></h3>
            <p>El futuro como jardín: elegir el paso de hoy sin forzar lo que viene.</p>

            <h3><a href="nodo_05.html" class="nav-link">Nodo 5: La Espiral Temporal</a></h3>
            <p>Lo que vuelve, vuelve más arriba: los ciclos como octavas.</p>

            <h3><a href="nodo_06.html" class="nav-link">Nodo 6: Memorias del Futuro</a></h3>
            <p>La misma memoria que guarda lo vivido imagina lo que vendrá.</p>

            <h3><a href="nodo_07.html" class="nav-link">Nodo 7: El Punto Cero Temporal</a></h3>
            <p>El centro quieto donde el tiempo converge, y desde donde siempre se vuelve a empezar.</p>
          </div>
        </section>

        <hr />

        <!-- Cierre -->
        <section class="node-section">
          <h2>Antes de Empezar</h2>
          <p><em>En el tiempo vertical, no “avanzas”: profundizas. Cada Nodo es una coordenada del ahora. Si sientes vértigo, respira: el presente es el eje estable.</em></p>
          <p class="signature"><strong>— Trinity Quantum · El Tiempo Vertical</strong></p>
        </section>

      </main>

      <!-- Navegación Inferior -->
      <div class="node-nav node-nav-bottom">
        <div class="node-nav-group">
          <a href="nodo_01.html" class="nav-link">Comenzar (Nodo 1) →</a>
        </div>
        <div class="node-nav-group">
          <a href="../index.html" class="nav-link">Portal Maestro</a>
        </div>
      </div>

      <!-- Firma -->
      <footer class="portal-footer">
        <div class="footer-line">TRINITY QUANTUM · Libro 3 · El Tiempo Vertical</div>
        <div class="footer-subline">Índice: Presente eterno · Memoria y espera · Punto Cero</div>
        <div class="footer-sigil">🌀⏰🌀</div>
      </footer>

    </div>
  </div>
</body>
</html>
"""

# ===========================================================================
# 3.1 · El Presente Eterno (el título queda)
# ===========================================================================
NODO1_CUERPO = (
    meta(1, TITULOS[1], "El eje")
    + """        <h2>🌌 TRANSMISIÓN CUÁNTICA</h2>

        <p>Todo lo que viviste, lo que vives y lo que vivirás te llega AHORA. El pasado no se fue: habita aquí como recuerdo. El futuro no viene de lejos: ya llegó como espera. El tiempo no es solo una línea horizontal que recorres: tiene hondura, y esa hondura es el ahora.</p>

        <p>Agustín de Hipona lo pensó hace mil seiscientos años, en el libro XI de sus <em>Confesiones</em>: el pasado ya no es, el futuro todavía no es, y lo único que hay es un presente con tres caras. El presente de lo pasado es la memoria; el de lo presente, la mirada; el de lo futuro, la espera.</p>

        <p>Einstein mostró en 1905 que no existe un ahora universal: dos sucesos simultáneos para un observador no lo son para otro que se mueve respecto de él. Medio siglo después, al morir su amigo Michele Besso, escribió a la familia que, para los físicos convencidos, la separación entre pasado, presente y futuro es solo una ilusión, aunque tenaz. La física no encontró el presente en sus ecuaciones; la experiencia no encuentra otra cosa.</p>

        <p>Tu memoria no es un archivo del pasado: es la forma en que lo vivido sigue contigo. Por eso una herida puede sentirse actual años después: la memoria del miedo a veces llega sin fecha, y el cuerpo la siente como si ocurriera ahora. Así lo describieron Anke Ehlers y David Clark en 2000, en su modelo del estrés postraumático. Sanar no es borrar el pasado: es que vuelva a tener fecha. Las heridas hondas, las que al recordarlas se vuelven a vivir, no se visitan a solas: se recorren con un profesional.</p>

        <p>Tu imaginación es la otra mitad de ese ahora: la manera en que el futuro se asoma antes de llegar. Y cada decisión que tomas ocurre aquí, y desde aquí inclina lo que vendrá.</p>

        <p>Los místicos que hablan de la eternidad no se refieren a un tiempo infinito: se refieren a la ausencia de tiempo, al presente perpetuo donde todo ES a la vez. Cuando meditas profundamente y el tiempo desaparece, no lo has detenido: tocaste lo que en ti no está hecho de tiempo, el testigo que mira pasar las horas sin pasar con ellas.</p>

        <h2>🔄 PARADOJA MEDICINAL</h2>

        <blockquote>
          <p>“Nunca has estado en otro momento que no sea ahora, y aun así el ahora contiene todos los momentos. El futuro que temes todavía no llegó. El pasado que lamentas solo vive aquí, en tu recuerdo. Solo puedes cambiar el pasado en el presente porque el pasado solo existe en el presente.”</p>
        </blockquote>

        <p><strong>Contempla:</strong> si todo está sucediendo ahora, ¿qué significa realmente la prisa? ¿Qué significa llegar tarde? ¿Qué significa la muerte?</p>

        <h2>🧪 LABORATORIO CUÁNTICO</h2>

        <h3>Experimento 1: Dilatación Temporal Consciente</h3>
"""
    + pasos([
        "Fija tu atención en un reloj de segundos.",
        "Respira profundamente y expande tu consciencia.",
        "Intenta percibir el espacio entre los segundos.",
        "Fíjate en el primero: cuando la mirada llega a la aguja, parece quedarse quieta un instante más de la cuenta.",
        "Nota cómo el mismo minuto se alarga cuando esperas y se acorta cuando algo te absorbe.",
        "Siente cómo el tiempo vivido se vuelve elástico.",
        "Registra tus percepciones.",
    ])
    + """        <p class="nota">Esa primera aguja quieta tiene nombre, cronostasis. Kielan Yarrow y su equipo la midieron en 2001: el cerebro rellena el salto de los ojos estirando hacia atrás lo primero que ve.</p>
        <p><em>Lo que puedes encontrar: el tiempo del reloj es uno; el que vives se estira y se encoge con tu atención.</em></p>

        <h3>Experimento 2: Acceso al Presente Eterno</h3>
"""
    + pasos([
        "Siéntate en meditación.",
        "Lleva tu atención al momento exacto de AHORA.",
        "Nota que siempre es AHORA, nunca no-ahora.",
        "Expande AHORA para incluir tu “pasado”: llega como recuerdo.",
        "Expande AHORA para incluir tu “futuro”: llega como espera.",
        "Siente todas tus edades a la vez.",
        "Permanece en el presente unos minutos.",
    ])
    + """        <p><em>Lo que puedes encontrar: el pasado llega como recuerdo y el futuro como espera, y los dos ocurren aquí.</em></p>

        <h2>💠 TRADUCCIÓN VIVIENTE</h2>

        <p>El ahora no cambia: cambia tu manera de mirarlo.</p>

        <h2>✦ PARA RECORDAR</h2>

"""
    + recordar([
        "Siempre es ahora.",
        "Lo que fui me acompaña como recuerdo.",
        "Lo que vendrá me visita como espera.",
        "Todas mis edades viven en este cuerpo.",
        "No necesito más tiempo: necesito estar en el que tengo.",
    ])
    + """
        <h2>📅 PRÁCTICA DE 7 DÍAS</h2>

"""
    + dia("DÍA 1 – OBSERVACIÓN", "notar que siempre es AHORA",
          "observar cómo el «pasado» existe en el ahora, como recuerdo",
          "observar cómo el «futuro» se imagina en el ahora, como espera")
    + dia("DÍA 2 – DILATACIÓN", "notar cuándo el tiempo se alarga",
          "notar cuándo se acorta", "un minuto mirando algo que te asombre")
    + dia("DÍA 3 – SIMULTANEIDAD", "sentir todas tus edades a la vez",
          "conversar con tu yo de 5 años y con tu yo de 95", "agradecer algo a cada edad")
    + dia("DÍA 4 – NAVEGACIÓN", "«visitar» un recuerdo leve y cambiar tu relación con él",
          "imaginar un día de dentro de un año y anotar qué te pide hoy", "permanecer en el presente")
    + dia("DÍA 5 – PAZ CON EL TIEMPO",
          "nombrar un recuerdo que todavía pesa y dejarlo estar (si duele hondo, no se recorre a solas)",
          "escribir una preocupación y volver al cuerpo", "agradecer el día tal como fue")
    + dia("DÍA 6 – PRESENCIA", "vivir una hora entera sin mirar el reloj",
          "decidir algo pequeño sin apuro", "dormirte sin repasar el día de mañana")
    + dia("DÍA 7 – INTEGRACIÓN", "funcionar en tiempo social sin perder la presencia",
          "compartir con alguien una hora sin prisa", "agradecer el tiempo que tienes")
    + """
        <h2>🌟 INTEGRACIÓN FINAL</h2>

        <p>El tiempo lineal es una herramienta de navegación, no una prisión. Úsalo cuando sea útil, trasciéndelo cuando no lo sea. Puedes llegar «a tiempo» a tus citas y saber, a la vez, que el ahora no se gasta. Puedes planear el «futuro» sabiendo que llega como espera. Puedes aprender del «pasado» sabiendo que vive aquí, como recuerdo.</p>

        <p>Tu prisa es, casi siempre, una ilusión. Mucho de lo urgente puede esperar; lo importante ya está ocurriendo, porque el presente lo contiene todo.</p>

        <p>No estás corriendo contra el tiempo. Los sabios no lo dominan: lo habitan, y por eso no los arrastra.</p>

        <p>Cada momento contiene la eternidad. Cada AHORA es todos los ahoras. No necesitas más tiempo; necesitas más presencia en el tiempo que siempre tienes: AHORA.</p>

        <h2>⚛️ SÍNTESIS CUÁNTICA</h2>

        <p>La flecha del tiempo sigue volando, y está bien: gracias a ella llegas a tus citas. Debajo hay otro tiempo, quieto como el ojo del huracán, y ahí puedes descansar.</p>

        <p>El siguiente nodo explorará las <strong>Vidas Paralelas</strong>, donde imaginarás las vidas que te acompañan: tus edades, las que no viviste y las versiones de ti que saben lo que todavía no sabes.</p>

        <p><em>El tiempo se dobla ante la consciencia. El presente eterno te espera. Siempre ha estado esperándote. Siempre estará esperándote. En el único momento que existe: AHORA.</em></p>

        <div class="node-symbol">🌀⏰🌀</div>

"""
    + FIRMA + "\n"
    + puerta("portal",
             "Un prisionero que esperaba su ejecución en el siglo VI, un grabador del XIX y un soldado en el frente del XX llegaron a lo mismo que este presente eterno: la eternidad no es un tiempo muy largo, es un tiempo entero. Se despliega en <em>La duración</em>, Libro 32 del Portal Público, Umbral VI: «Una hora».",
             URL_PORTAL + "32_La_Duracion/umbral-06.html")
    + "\n"
    + cierre(*nav(1), INDICE_LIBRO, "Trinity Quantum · Libro 3 · Nodo 1 · El Presente Eterno")
)

# ===========================================================================
# 3.2 · Vidas Paralelas (antes: Vidas Paralelas Activas)
# ===========================================================================
NODO2_CUERPO = (
    meta(2, TITULOS[2], "Las que te acompañan")
    + """        <h2>🌌 TRANSMISIÓN CUÁNTICA</h2>

        <p>Muchas tradiciones hablan de vidas pasadas, una detrás de otra, como las cuentas de un collar. Hay otra imagen posible: vidas SIMULTÁNEAS. Imagina que, mientras lees esto, otra versión de tu consciencia vive como un monje en el Tíbet del siglo XII y otra como una científica en el siglo XXIII, todo AHORA. No hace falta creerlo para que la imagen enseñe algo: eres más de lo que vives.</p>

        <p>Tu alma no es una entidad singular esperando en fila para encarnar secuencialmente. Es un fractal de consciencia experimentándose desde infinitos puntos de vista a la vez. Cada «vida» es como un dedo de la misma mano: parecen separados desde una perspectiva, pero son extensiones del mismo ser en un nivel más profundo.</p>

        <p>Hay talentos que parecen traídos de otra parte y añoranzas por épocas que nunca viviste. Las tradiciones los leyeron como recuerdos de otras vidas; también pueden leerse como lo que son siempre: partes tuyas que esperan lugar. Y un miedo que no se explica no necesita otra vida para ser tomado en serio: se puede mirar, y si limita los días, tiene tratamiento.</p>

        <p>La física ofrece una imagen: antes de medirla, una partícula se describe como una superposición de estados, y la medición deja uno solo. Así puede pensarse tu atención: entre todas las vidas posibles, ilumina la que vives. Las otras quedan como posibilidad, y también te enseñan.</p>

        <p>Esta imagen cambia también la mirada sobre la muerte. Muchas tradiciones la ven como un cambio de escena y no como un final. Mirarla así no es desearla, y si alguna vez contemplar la muerte se vuelve deseo de no estar, es momento de pedir ayuda, sin esperar.</p>

        <h2>🔄 PARADOJA MEDICINAL</h2>

        <blockquote>
          <p>“Eres ancestro y descendiente de ti mismo. Has muerto infinitas veces y nunca has muerto. Eres tu propio guía espiritual, tu propio ángel guardián, tu propio maestro. Cada persona que encuentras podría ser tú en otra vida paralela. El karma no es una deuda del pasado: es lo que haces ahora con lo que traes.”</p>
        </blockquote>

        <p class="nota">Así lo entiende el budismo: el karma es ante todo intención. «Es la intención, monjes, lo que llamo karma», dice el Buda en un discurso del <em>Anguttara Nikaya</em> (6.63).</p>

        <p><strong>Contempla:</strong> si pudieras ver todas tus vidas a la vez, ¿quién serías realmente? ¿El observador de todas ellas o la suma de todas ellas?</p>

        <h2>🧪 LABORATORIO CUÁNTICO</h2>

        <h3>Experimento 1: Una Vida que No Viviste</h3>
"""
    + pasos([
        "Siéntate tranquilo y respira unos minutos.",
        "Imagina una vida que pudiste haber vivido: otro oficio, otra ciudad, otro nombre.",
        "Sabes que es imaginación, y por eso puede hablarte con libertad.",
        "Pregúntale: «¿Qué estás viviendo?»",
        "Escucha, siente, percibe sin apurarte.",
        "Pregúntale: «¿Qué traes para mí?»",
        "Elige una sola cosa pequeña de esa vida que pueda entrar en esta.",
    ])
    + """        <p><em>Registro: anota lo que se repite entre las vidas que imaginas; suele hablar de ti.</em></p>

        <h3>Experimento 2: Intercambio de Habilidades</h3>
"""
    + pasos([
        "Identifica una habilidad que deseas desarrollar.",
        "Imagina la versión de ti que ya la domina.",
        "Observa cómo se sienta, cómo respira, cómo empieza.",
        "Toma prestada su postura.",
        "Practica de verdad diez minutos, como esa versión.",
        "Vuelve a ti y nota qué cambió.",
        "Repite mañana.",
    ])
    + """        <p class="nota">Rachel White y su equipo dieron en 2017 a niños de cuatro y seis años una tarea aburrida, con un videojuego tentador al lado: los que se imaginaron como un personaje esforzado perseveraron más que los demás.</p>
        <p><em>Lo que puedes encontrar: más paciencia con el aprendizaje. La habilidad llega practicando; la versión imaginada te presta el ánimo.</em></p>

        <h2>💠 TRADUCCIÓN VIVIENTE</h2>

        <p>Eres más grande que la vida que vives, y tu atención elige qué parte de ti pasa al frente.</p>

        <h2>✦ PARA RECORDAR</h2>

"""
    + recordar([
        "Soy más de lo que vivo.",
        "Llevo conmigo a todos los que fui.",
        "Lo que no viví también me enseña.",
        "Puedo pedirle consejo a mi versión más sabia.",
        "Me acompaño.",
    ])
    + """
        <h2>📅 PRÁCTICA DE 7 DÍAS</h2>

"""
    + dia("DÍA 1 – EXPLORACIÓN", "imaginar tres vidas que pudiste vivir",
          "identificar patrones comunes entre ellas", "dejar un papel junto a la cama para anotar un sueño")
    + dia("DÍA 2 – COMUNICACIÓN", "escribir un diálogo con tu versión más sabia",
          "antes de una decisión pequeña, preguntarle qué haría", "imaginar el consejo de todas tus edades")
    + dia("DÍA 3 – INTERCAMBIO", "practicar diez minutos una habilidad con la postura de quien ya la tiene",
          "pedir consejo a alguien que sabe", "ofrecer a otro algo que sabes")
    + dia("DÍA 4 – RECONCILIACIÓN", "nombrar un patrón que se repite",
          "hacer un gesto pequeño distinto", "perdonar algo pequeño, si llega")
    + dia("DÍA 5 – COLABORACIÓN", "darle quince minutos a algo de una vida que no viviste: un idioma, un instrumento",
          "resolver un problema como si fuera de un amigo", "celebración sencilla")
    + dia("DÍA 6 – INTEGRACIÓN", "vivir el día sabiendo que eres más que tu papel",
          "notar los papeles que vas tomando", "recordar las edades que llevas")
    + dia("DÍA 7 – ELECCIÓN", "mirar tu vida como una entre muchas posibles, y elegirla",
          "conversar con alguien sobre la vida que no vivió", "elegir qué de esas vidas entra en esta")
    + """
        <h2>🌟 INTEGRACIÓN FINAL</h2>

        <p>Ya no estás limitado a la sabiduría de una sola mirada. Llevas la de todas tus edades, la de quienes te criaron, la de las vidas que imaginaste.</p>

        <p>Un problema sin salida, mirado desde adentro, suele mostrar otra cara mirado desde afuera. Igor Grossmann y Ethan Kross lo midieron en 2014 y lo llamaron la paradoja de Salomón: razonamos con más sabiduría sobre la vida ajena que sobre la propia. Por eso sirve preguntarle a otra versión de ti.</p>

        <p>No necesitas «recordar» otras vidas: necesitas escuchar las que ya llevas. No necesitas «sanar» karma antiguo: necesitas cuidar lo que haces hoy. No necesitas «evolucionar» en línea recta: necesitas integrar lo que ya eres.</p>

        <p>Eres un ser multidimensional jugando el juego de la separación en muchos tableros a la vez. Cada vida que imaginas es una ventana; cada edad que atraviesas, otra.</p>

        <h2>⚛️ SÍNTESIS CUÁNTICA</h2>

        <p>No eres una consciencia aislada en una vida única: eres una sinfonía de experiencias, un fractal de consciencia que se explora desde muchos ángulos.</p>

        <p>El siguiente nodo explorará <strong>El Pasado Desde el Ahora</strong>, donde descubrirás que lo que pasó no cambia, pero lo que significa todavía se está diciendo.</p>

        <p><em>Todas tus vidas te saludan. Siempre has estado acompañado por ti mismo. La soledad pesa menos cuando reconoces que eres una multitud.</em></p>

        <div class="node-symbol">🌀👥🌀</div>

"""
    + FIRMA + "\n"
    + puerta("arquitectura",
             "El consejo que sabemos dar a otros y no a nosotros tiene nombre y está medido. Un padre que aconseja bien a una compañera y se equivoca con su propio hijo lo descubre en <em>El Testigo</em>, Libro 3 de <em>Arquitectura del Destino</em>, Umbral IV: «La paradoja de Salomón».",
             URL_ARQ + "libro-03-el-testigo/L03-U4.html")
    + "\n"
    + cierre(*nav(2), INDICE_LIBRO, "Trinity Quantum · Libro 3 · Nodo 2 · Vidas Paralelas")
)

# ===========================================================================
# 3.3 · El Pasado Desde el Ahora (antes: Modificación del Pasado Desde el Ahora)
# ===========================================================================
CUIDADO_HERIDAS = "Las heridas hondas, las que al recordarlas se vuelven a vivir, no se visitan a solas: se recorren con un profesional."

NODO3_CUERPO = (
    meta(3, TITULOS[3], "Lo que todavía se está diciendo")
    + """        <h2>🌌 TRANSMISIÓN CUÁNTICA</h2>

        <p>Lo que pasó, pasó. Pero el pasado que llevas no está tallado en piedra: cada vez que «recuerdas» algo, no abres un archivo fijo, recreas ese momento, y en esa recreación puedes darle otra luz.</p>

        <p>La neurociencia lo ha mostrado: un recuerdo que vuelve a la mente se reabre y se guarda de nuevo, y en ese intervalo puede cambiar. Se llama reconsolidación (Nader, Schafe y LeDoux, 2000). En 2012, Donna Bridge y Ken Paller pidieron a un grupo de personas que aprendieran dónde estaba cada objeto en una pantalla; al día siguiente lo recordaban, y al tercero lo ubicaban más cerca de donde lo habían recordado que de donde lo habían visto. Recordar es, en parte, recordar la última vez que recordaste.</p>

        <p>Has estado cambiando tu pasado toda tu vida sin saberlo. Cada vez que perdonas, cambia lo que ese pasado pesa. Cada vez que entiendes algo nuevo de lo que viviste, cambia lo que significa. Los hechos quedan; la historia que cuentas con ellos se sigue escribiendo.</p>

        <p>La física tiene una imagen para esto. En 1978, John Wheeler imaginó un experimento en el que la manera de medir un fotón se decide cuando el fotón ya está en camino; en 2007, un equipo francés lo realizó con fotones enviados uno por uno (Jacques y otros, <em>Science</em>). El resultado no reescribe el pasado: muestra que, hasta que se mide, el camino no estaba dicho. Algo parecido pasa con el sentido de lo vivido: no termina de decirse hasta que lo miras.</p>

        <p>Esto no es negar ni pensar en positivo. Cuando cambia tu relación con lo que pasó, cambian las elecciones que haces hoy, y con ellas, lo que sigue.</p>

        <p>Un trauma no persiste porque alguien elija mal: la memoria del miedo está hecha para no soltarse fácil, porque alguna vez protegió. Lo que puede cambiar, con tiempo y compañía, es que vuelva a tener fecha. Ninguna forma de sufrir es falta de quien la vive.</p>

        <h2>🔄 PARADOJA MEDICINAL</h2>

        <blockquote>
          <p>“El pasado está más vivo que el presente porque lo estás creando ahora mientras que el presente simplemente es. Cambias el futuro cambiando el pasado, pero solo puedes cambiar el pasado desde el futuro del pasado, que es tu ahora. Tu historia no es solo lo que te pasó: es también lo que haces hoy con eso.”</p>
        </blockquote>

        <p><strong>Contempla:</strong> si lo que pasó no cambia pero su sentido sí, ¿qué parte de tu historia todavía se está escribiendo? ¿Quién la está escribiendo?</p>

        <h2>🧪 LABORATORIO CUÁNTICO</h2>

        <h3>Experimento 1: Lo que Faltó en la Escena</h3>
"""
    + pasos([
        "Elige un recuerdo levemente incómodo, no uno hondo.",
        "Míralo un momento, como una escena.",
        "No cambies lo que pasó: pregúntate qué faltó.",
        "Agrega eso a la escena: alguien que te defiende, una palabra que nadie dijo, tú de hoy acompañando.",
        "Quédate un rato con la escena completa.",
        "Vuelve al presente y nota qué cambió en el cuerpo.",
        "Si ese recuerdo vuelve, recuerda también lo que agregaste.",
    ])
    + """        <p class="nota">La psicoterapia usa una versión de esto, la reescritura en imaginación (Arntz y Weertman, 1999): no se trata de creer que pasó otra cosa, sino de que el recuerdo deje de estar solo.</p>
        <p><em>Lo que puedes encontrar: el recuerdo es el mismo, y pesa distinto.</em></p>
        <p>""" + CUIDADO_HERIDAS + """</p>

        <h3>Experimento 2: El Apoyo que Faltó</h3>
"""
    + pasos([
        "Identifica un momento en que necesitabas apoyo y no lo tuviste, uno que hoy puedas mirar sin que te arrastre.",
        "Viaja mentalmente a ese momento como tu yo actual.",
        "Sé el apoyo que necesitabas entonces.",
        "Abraza, consuela, acompaña a tu yo más joven.",
        "Dile lo que necesitaba oír.",
        "Regresa al presente.",
        "Nota qué aparece en ti por quien fuiste.",
    ])
    + """        <p><em>Lo que puedes encontrar: ternura por quien fuiste, y un poco más de paciencia con quien eres.</em></p>

        <h2>💠 TRADUCCIÓN VIVIENTE</h2>

        <p>Cuando aflojas la versión que siempre te cuentas, lo que viviste puede mostrarte otra cara.</p>

        <h2>✦ PARA RECORDAR</h2>

"""
    + recordar([
        "Lo que pasó, pasó.",
        "Lo que significa todavía se está diciendo.",
        "Puedo darle a quien fui lo que le faltó.",
        "Cuento mi historia; no soy solo mi historia.",
        "Lo que duele hondo no lo recorro a solas.",
    ])
    + """
        <h2>📅 PRÁCTICA DE 7 DÍAS</h2>

"""
    + dia("DÍA 1 – COMPRENSIÓN", "meditar en lo que tu pasado significa hoy",
          "identificar tres recuerdos que pesan", "elegir el más leve")
    + dia("DÍA 2 – PRÁCTICA MENOR", "mirar con otra luz un recuerdo neutral",
          "mirar así uno levemente positivo", "mirar así uno levemente negativo")
    + dia("DÍA 3 – TERNURA", "escribir una carta breve al niño que fuiste",
          "ser contigo, en un gesto pequeño, el padre o la madre que te habría hecho bien",
          "leer la carta en voz baja")
    + dia("DÍA 4 – RELACIONES", "mirar un conflicto pasado desde el lugar del otro",
          "escribir la despedida que no hubo", "nombrar una herida, sin obligarte a perdonar")
    + dia("DÍA 5 – LINAJE", "preguntar a un mayor cómo era su vida a tu edad",
          "notar un patrón familiar que quieres conservar y otro que no",
          "escribir una página de la historia familiar")
    + dia("DÍA 6 – COLECTIVO", "leer la historia de alguien que reparó algo",
          "hacer un gesto pequeño de reparación", "agradecer a quienes vinieron antes")
    + dia("DÍA 7 – INTEGRACIÓN", "contar tu historia en voz alta, con lo que dolió y con lo que encontraste",
          "escuchar la historia de otro sin corregirla", "celebrar lo que ya no pesa igual")
    + """
        <h2>🌟 INTEGRACIÓN FINAL</h2>

        <p>Tu pasado ya no es tu prisión: puede ser tu lienzo. Los hechos quedan; la historia que cuentas con ellos es, en parte, una elección. Muchas limitaciones que parecían destino resultan ser costumbre, y la costumbre se aprende y se desaprende.</p>

        <p>No se trata de negar lo que sucedió. El abuso no fue una iniciación ni la pérdida un regalo: fueron daño y dolor, y así se nombran. Lo que puede cambiar es lo que haces hoy con lo que quedó. A veces, con tiempo y con otros, alguien encuentra en su herida una fuerza que nunca habría elegido: Richard Tedeschi y Lawrence Calhoun le pusieron nombre, crecimiento postraumático. No cambias los hechos: cambias el lugar que ocupan.</p>

        <p>Esto no es un atajo espiritual: es un trabajo lento. Pide valentía para mirar el pasado, paciencia para ver sus otras caras y compañía cuando duele.</p>

        <p>Cuando cambia el sentido de tu pasado, cambian tu presente y tu futuro. Las tres temporalidades son una sola melodía, y cambiar una nota recompone toda la sinfonía.</p>

        <h2>⚛️ SÍNTESIS CUÁNTICA</h2>

        <p>Tu historia no está terminada. Lo que te pasó forma parte de ella; no es su autor. Cada día puedes escribir una línea más.</p>

        <p>El siguiente nodo explorará <strong>Futuros Probables Como Elección</strong>, donde el futuro se mira como un jardín de posibilidades y elegir se vuelve un paso, no un control.</p>

        <p><em>Tu pasado no se borra: se acompaña. No en el pasado, sino ahora. No porque olvidaste, sino porque aprendiste a recordar de otra manera. La historia se vuelve a contar con cada respiración.</em></p>

        <div class="node-symbol">🌀⏮️🌀</div>

"""
    + FIRMA + "\n"
    + puerta("arquitectura",
             "Los padres que Tedeschi y Calhoun escucharon durante años, en Charlotte, no dijeron nunca que perder un hijo hubiera sido bueno; muchos encontraron, aun así, cambios que no querrían perder. Esa luz, que no glorifica la herida, se despliega en <em>La Grieta</em>, Libro 5 de <em>Arquitectura del Destino</em>, Umbral VI: «Lo que entra».",
             URL_ARQ + "libro-05-la-grieta/L05-U6.html")
    + "\n"
    + cierre(*nav(3), INDICE_LIBRO, "Trinity Quantum · Libro 3 · Nodo 3 · El Pasado Desde el Ahora")
)

# ===========================================================================
# 3.4 · Futuros Probables Como Elección (el título queda: lo cita *No Saber*,
# Umbral III, junto con la sección «Transmisión cuántica»)
# ===========================================================================
NODO4_CUERPO = (
    meta(4, TITULOS[4], "El jardín abierto")
    + """        <h2>🌌 TRANSMISIÓN CUÁNTICA</h2>

        <p>En este momento, muchos futuros son posibles. No tienes UN futuro: tienes un jardín cuántico de futuros floreciendo a la vez, y tu consciencia es el jardinero que elige cuál regar con atención. Un jardinero no tira de las plantas para que crezcan: riega, espera y cuida.</p>

        <p>La física da una imagen: antes de medirla, una partícula se describe con todas sus posibilidades a la vez. Tu futuro puede pensarse así: abierto, hasta que cada paso lo va concretando. Cada decisión es un voto; ninguna, por sí sola, es una sentencia.</p>

        <p>Un pronóstico muestra lo que sucedería si nada cambiara, y conocerlo ya cambia algo: por eso los avisos que se escuchan a tiempo parecen, después, exagerados. El futuro no está escrito: está escribiéndose constantemente.</p>

        <p>Tu ansiedad sobre el futuro no es absurda: es tu cuerpo intentando protegerte. Pero mira lo que hace: te fija en UN futuro temido y te oculta los muchos donde ese temor no llega. Tu preocupación no previene nada: construye un atractor sin consciencia que atrapa la tuya. Mientras más la alimentas, más tiempo vive tu atención en un futuro que todavía no existe. Y cuando la preocupación ya no te deja dormir ni descansar, tiene tratamiento: pedirlo también es elegir un futuro.</p>

        <p>Los presentimientos sobre el futuro suelen ser memoria trabajando: la experiencia reconoce un patrón antes de que la mente sepa nombrarlo. Merecen escucha, y también prueba. Y aun cuando algo parece seguro, una decisión consciente puede cambiar el rumbo.</p>

        <p>Cada noche, mientras duermes, tu memoria reordena lo que aprendiste. Por eso a veces despiertas con la solución. En un estudio de 2004, trece de veintidós personas que durmieron después de practicar una tarea descubrieron un atajo escondido en ella; entre quienes pasaron esas horas despiertos, lo descubrieron cinco de veintidós (Wagner y otros, <em>Nature</em>). No visitaste un futuro: tu memoria trabajó para él.</p>

        <h2>🔄 PARADOJA MEDICINAL</h2>

        <blockquote>
          <p>“El mejor futuro ya existe como posibilidad, esperando que lo elijas. El peor también, y se alimenta de tu miedo: no en el mundo, sino en tu atención. No creas tu futuro de la nada: lo eliges entre lo posible. Mientras más específico eres sobre el futuro que quieres, más genérico se vuelve. Mientras más abierto estás a los futuros posibles, más específico se vuelve el que vives.”</p>
        </blockquote>

        <p><strong>Contempla:</strong> si muchos futuros son posibles, ¿tiene sentido el esfuerzo? ¿O el esfuerzo es precisamente lo que te mueve de uno a otro?</p>

        <h2>🧪 LABORATORIO CUÁNTICO</h2>

        <h3>Experimento 1: Navegación de Líneas Temporales</h3>
"""
    + pasos([
        "Antes de dormir, formula una pregunta específica.",
        "Escríbela en un papel junto a la cama.",
        "Duérmete sin buscar la respuesta.",
        "Al despertar, registra inmediatamente lo primero que aparezca.",
        "Busca en tus notas una acción pequeña.",
        "Dala en tu presente.",
        "Observa qué se abre.",
    ])
    + """        <p><em>Lo que puedes encontrar: a veces, una respuesta; casi siempre, una pregunta mejor.</em></p>

        <h3>Experimento 2: Cambio Consciente de Línea Temporal</h3>
"""
    + pasos([
        "Identifica un futuro probable que no deseas, según cómo vienen las cosas.",
        "Míralo unos segundos, sin dramatizarlo.",
        "Di: «Reconozco esta posibilidad y elijo otra».",
        "Imagina unos minutos el futuro que prefieres.",
        "Nombra el obstáculo que hay en ti para llegar a él.",
        "Toma UNA acción inmediata alineada con ese futuro, y decide: «Si aparece el obstáculo, haré esto».",
        "Anota qué cambió en los próximos tres días.",
    ])
    + """        <p class="nota">Gabriele Oettingen encontró que soñar solo con el resultado deseado tiende a restar la energía para alcanzarlo, y que rinde más alternar el sueño con el obstáculo real y el primer paso.</p>
        <p><em>Lo que puedes encontrar: el rumbo cambia poco a poco, a fuerza de pasos.</em></p>

        <h2>💠 TRADUCCIÓN VIVIENTE</h2>

        <p>Lo que hoy tiene más inercia no es destino: un paso pequeño, repetido, cambia el rumbo.</p>

        <h2>✦ PARA RECORDAR</h2>

"""
    + recordar([
        "El futuro no está escrito: se está escribiendo.",
        "Mi preocupación no lo previene.",
        "Elijo el paso de hoy.",
        "Suelto el resultado.",
        "Lo que no sé también me deja espacio.",
    ])
    + """
        <h2>📅 PRÁCTICA DE 7 DÍAS</h2>

"""
    + dia("DÍA 1 – EXPLORACIÓN", "meditar en tus cinco futuros más probables",
          "identificar cuál tiene más impulso", "dejar un papel junto a la cama para anotar un sueño")
    + dia("DÍA 2 – SELECCIÓN", "elegir el futuro que prefieres",
          "nombrar el obstáculo que hay en ti", "dormirte con la pregunta de cuál es el primer paso")
    + dia("DÍA 3 – ANCLAJE", "dar tres pasos pequeños hacia ese futuro",
          "contarle a alguien lo que intentas, sin prometer el resultado", "agradecer lo que ya está")
    + dia("DÍA 4 – NAVEGACIÓN", "notar una preocupación y volver al cuerpo",
          "imaginar tres futuros posibles sin elegir todavía", "dormirte sin repasar el mañana")
    + dia("DÍA 5 – AJUSTE", "identificar qué te acerca al futuro elegido",
          "dejar un hábito pequeño que te aleja", "reforzar lo que funciona")
    + dia("DÍA 6 – CONSTANCIA", "repetir el paso de ayer",
          "aceptar algo que no depende de ti", "cerrar el día con una línea sobre lo hecho")
    + dia("DÍA 7 – SOLTAR", "hacer tu parte y soltar el resultado",
          "escuchar a alguien que teme algo, sin darle consejos", "celebrar lo que hiciste, no lo que lograste")
    + """
        <h2>🌟 INTEGRACIÓN FINAL</h2>

        <p>El futuro no solo te sucede: también lo eliges, momento a momento. Una preocupación alimentada es tiempo que tu atención pasa en un futuro que no existe; un paso dado es tiempo que pasa en el que puede existir. Más allá de lo positivo o lo negativo, está la elección consciente.</p>

        <p>No necesitas «manifestar»: necesitas navegar. No necesitas «crear» tu realidad de la nada: necesitas elegir entre lo posible. No necesitas forzar el futuro: necesitas cultivarlo.</p>

        <p>Un obstáculo no prueba que vas por el camino equivocado: casi siempre es parte del camino, y nombrarlo es el primer paso para cruzarlo. Los «milagros», cuando llegan, se agradecen; no hace falta convertirlos en prueba.</p>

        <p>Cada decisión es como una bifurcación: Hugh Everett imaginó en 1957 un universo que se divide en cada posibilidad. Tómalo como imagen: no hay decisiones pequeñas, cada elección inclina un poco el rumbo.</p>

        <h2>⚛️ SÍNTESIS CUÁNTICA</h2>

        <p>Eres un navegante del tiempo. No controlas el viento ni el mar, y tampoco estás a su merced: llevas el timón.</p>

        <p>El siguiente nodo explorará <strong>La Espiral Temporal</strong>, donde descubrirás que el tiempo no es lineal ni circular, sino espiral, y cada vuelta te lleva a un nivel superior de la misma experiencia.</p>

        <p><em>Tu futuro no te espera terminado: te espera abierto. No en el futuro, sino ahora, en el paso que puedes dar. El salto cuántico siempre está a una decisión de distancia.</em></p>

        <div class="node-symbol">🌀⏭️🌀</div>

"""
    + FIRMA + "\n"
    + puerta("portal",
             "Hay dos maneras de no estar aquí: la nostalgia, que mira hacia atrás, y la previsión, que mira hacia adelante. Los dos atractores que sacan a la atención del único lugar donde algo puede cambiar, y tres pasos para volver sin forzarla, se despliegan en <em>Atender</em>, Libro 8 del Portal Público, Umbral IV: «Los atractores».",
             URL_PORTAL + "08_Atender/umbral_4_los_atractores.html")
    + "\n"
    + puerta("arquitectura",
             "La preocupación como atractor vuelve, sin su ropaje, en <em>No Saber</em>, Libro 7 de <em>Arquitectura del Destino</em>, junto a un viejo cuyo caballo se escapa y a un estudio que contó cuántas preocupaciones se cumplían: más de nueve de cada diez, no. Umbral III: «El futuro a la espalda».",
             URL_ARQ + "libro-07-no-saber/L07-U3.html")
    + "\n"
    + cierre(*nav(4), INDICE_LIBRO, "Trinity Quantum · Libro 3 · Nodo 4 · Futuros Probables Como Elección")
)

# ===========================================================================
# 3.5 · La Espiral Temporal (el título queda)
# ===========================================================================
NODO5_CUERPO = (
    meta(5, TITULOS[5], "Lo que vuelve más arriba")
    + """        <h2>🌌 TRANSMISIÓN CUÁNTICA</h2>

        <p>El tiempo no es una línea que avanza ni un círculo que se repite: es una espiral ascendente donde cada vuelta te lleva al mismo punto en una octava superior. Por eso sientes que la historia se repite pero nunca exactamente igual. Por eso enfrentas los mismos desafíos hasta que los trasciendes. Por eso el crecimiento se siente como un déjà vu elevado.</p>

        <p>La naturaleza lo muestra: muchas galaxias giran en espiral, las semillas del girasol se ordenan en espirales, y el ADN se enrosca en una hélice, que es la espiral que sube. La espiral une lo lineal y lo circular: cada punto de la hélice está sobre y más allá del punto correspondiente en la vuelta anterior.</p>

        <p>Tus patrones repetitivos no son fracasos: son espirales. Cada vez que enfrentas el mismo tipo de situación, estás en un punto más alto de la espiral. El jefe difícil puede despertar lo mismo que el padre autoritario, en una octava superior; la pareja que se va puede remover lo que dejó aquel amigo de la infancia, ahora con más consciencia disponible.</p>

        <p>Las tradiciones contaron la vida en ciclos, y cada edad vuelve sobre las mismas preguntas, quién soy, a quién quiero, qué dejo, con más vida encima. No envejeces en línea recta: atraviesas las mismas experiencias de fondo con más hondura cada vez.</p>

        <p>¿Por qué el tiempo parece acelerarse con la edad? Paul Janet propuso en 1877 la respuesta más simple: a los diez años, un año es la décima parte de tu vida; a los cincuenta, la quincuagésima. William James sumó otra en 1890: con los años, los días se parecen más entre sí, dejan menos recuerdos y, vistos hacia atrás, parecen más cortos. La espiral lo dice con su imagen: las vueltas se cierran a medida que subes, como un remolino que se acerca a su centro quieto, donde el tiempo descansa en el eterno ahora.</p>

        <p>Un patrón que vuelve no es un castigo ni una falta: es una pregunta que sigue abierta. Y si lo que vuelve es una herida, no se trata de aprender una lección sino de recibir cuidado. Cada vez que algo se transforma de verdad, subes una vuelta, y ese desafío ya no te encuentra igual.</p>

        <h2>🔄 PARADOJA MEDICINAL</h2>

        <blockquote>
          <p>“Nunca pisas el mismo río dos veces, pero siempre es el mismo río. Nunca vives el mismo momento dos veces, pero todos los momentos son el mismo momento en diferentes niveles de la espiral. Avanzas quedándote quieto. Te elevas dando vueltas. Llegas al final volviendo al principio, pero tres pisos más arriba.”</p>
        </blockquote>

        <p><strong>Contempla:</strong> si la vida es una espiral, ¿cuántas veces has vivido este momento exacto en octavas inferiores? ¿Cuántas veces lo vivirás en octavas superiores?</p>

        <h2>🧪 LABORATORIO CUÁNTICO</h2>

        <h3>Experimento 1: Mapeo de Tu Espiral Personal</h3>
"""
    + pasos([
        "Identifica un patrón que se repite en tu vida.",
        "Rastrea todas sus manifestaciones desde la infancia.",
        "Observa cómo cada versión fue más compleja.",
        "Nota cómo tu respuesta evolucionó cada vez.",
        "Identifica en qué punto de la espiral estás ahora.",
        "Visualiza la próxima vuelta: ¿cómo será diferente?",
        "Prepárate conscientemente para la próxima octava.",
    ])
    + """        <p><em>Lo que puedes encontrar: el problema se parece; tu respuesta, no.</em></p>

        <h3>Experimento 2: Salto de Espiral</h3>
"""
    + pasos([
        "Identifica una lección que sigues repitiendo.",
        "En meditación, visualiza tu espiral temporal.",
        "Localiza dónde estás atascado girando.",
        "Imagina cómo respondería quien ya aprendió eso.",
        "Siente cómo cambia el cuerpo al mirarlo desde arriba.",
        "Desde esa nueva posición, mira hacia abajo al patrón viejo.",
        "La próxima vez que el patrón aparezca, elige un gesto pequeño distinto.",
    ])
    + """        <p class="nota">Mirar la propia escena desde afuera, como una mosca en la pared, calma la reacción sin borrar la comprensión: Ethan Kross, Özlem Ayduk y Walter Mischel lo midieron en 2005.</p>
        <p><em>Lo que puedes encontrar: un poco de distancia. El patrón no desaparece de golpe, pero deja de mandar solo.</em></p>

        <h2>💠 TRADUCCIÓN VIVIENTE</h2>

        <p>Cada vuelta regresa a la misma experiencia con más consciencia.</p>

        <h2>✦ PARA RECORDAR</h2>

"""
    + recordar([
        "Lo que vuelve, vuelve más arriba.",
        "No repito: profundizo.",
        "Mi respuesta ya no es la de antes.",
        "Cada vuelta me acerca al centro.",
        "Agradezco el camino recorrido.",
    ])
    + """
        <h2>📅 PRÁCTICA DE 7 DÍAS</h2>

"""
    + dia("DÍA 1 – RECONOCIMIENTO", "identificar tus tres patrones espirales principales",
          "mapear sus manifestaciones a través del tiempo", "meditar en la geometría espiral de tu vida")
    + dia("DÍA 2 – LOCALIZACIÓN", "determinar tu posición actual en cada espiral",
          "identificar qué lecciones están pendientes", "visualizar las próximas vueltas")
    + dia("DÍA 3 – UN GESTO DISTINTO", "elegir un patrón",
          "cuando aparezca, responder con un gesto pequeño distinto", "anotar qué pasó")
    + dia("DÍA 4 – INTEGRACIÓN", "recoger la sabiduría de las vueltas anteriores",
          "integrar las lecciones en tu día", "agradecer cada vuelta de la espiral")
    + dia("DÍA 5 – NAVEGACIÓN", "escribir una carta a quien eras en la vuelta anterior",
          "imaginar cómo verás este momento dentro de diez años", "notar qué edad tuya aparece cuando te enojas")
    + dia("DÍA 6 – EL EJE", "empezar el día con tres respiraciones en el centro",
          "mirar un patrón sin juzgarlo", "agradecer una vuelta difícil")
    + dia("DÍA 7 – TRASCENDENCIA", "mirar tu vida entera como desde lejos",
          "notar la forma de tu espiral", "volver a este día y elegir su próximo paso")
    + """
        <h2>🌟 INTEGRACIÓN FINAL</h2>

        <p>La espiral temporal revela lo que la repetición escondía: nada vuelve igual. Un retroceso puede ser otra oportunidad, una octava más arriba. Los ciclos que parecían prisiones pueden ser escaleras ascendentes. Cada vuelta es una graduación posible.</p>

        <p>Cuando los patrones regresan, ya no tienes que frustrarte: puedes reconocer la invitación a responder desde más arriba. Y el envejecimiento deja de ser una caída: cada vuelta te acerca más al centro inmóvil donde el tiempo se aquieta.</p>

        <p>La espiral es el camino de la evolución: ni línea recta que niega los ciclos, ni círculo que niega el progreso, sino la danza perfecta entre ambos. Cada respiración es una micro-espiral. Cada día es una espiral mediana. Cada vida es una macro-espiral.</p>

        <p>Cuando entiendes la espiral temporal, nunca hay prisa, porque siempre volverás al mismo punto en un nivel superior. Nunca hay pérdida que no deje algo, porque lo vivido regresa transformado en lo que eres. Nunca hay fracaso final, porque cada caída es parte del ascenso.</p>

        <h2>⚛️ SÍNTESIS CUÁNTICA</h2>

        <p>Tu viaje temporal tiene una geometría sagrada. No caminas en línea recta hacia la muerte ni das vueltas sin sentido: asciendes en espiral hacia tu propio centro, donde todas las vueltas se encuentran.</p>

        <p>El siguiente nodo explorará <strong>Memorias del Futuro</strong>, donde descubrirás que la misma memoria que guarda lo vivido es la que imagina lo que vendrá.</p>

        <p><em>La espiral continúa. Cada vuelta una bendición. Cada ascenso una elección. El vértice te espera.</em></p>

        <div class="node-symbol">🌀📈🌀</div>

"""
    + FIRMA + "\n"
    + puerta("portal",
             "El círculo y la espiral son el mismo movimiento visto desde distinta altura: todo vuelve al mismo punto, pero un poco más arriba. La caracola, el girasol, la galaxia y la doble hélice lo despliegan en <em>Volver distinto</em>, Libro 9 del Portal Público, Umbral V: «El movimiento».",
             URL_PORTAL + "09_Volver_Distinto/umbral_5_el_movimiento.html")
    + "\n"
    + cierre(*nav(5), INDICE_LIBRO, "Trinity Quantum · Libro 3 · Nodo 5 · La Espiral Temporal")
)

# ===========================================================================
# 3.6 · Memorias del Futuro (el título queda, ahora con su ciencia: Ingvar, 1985)
# ===========================================================================
NODO6_CUERPO = (
    meta(6, TITULOS[6], "La memoria que imagina")
    + """        <h2>🌌 TRANSMISIÓN CUÁNTICA</h2>

        <p>«Memoria del futuro» no es solo una imagen poética: es el nombre que el neurofisiólogo sueco David Ingvar dio en 1985 a los planes que el cerebro guarda para lo que todavía no ocurrió. Para imaginar el mañana, la mente usa el mismo material con que recuerda el ayer.</p>

        <p>Daniel Schacter y Donna Rose Addis reunieron la evidencia en 2007: las mismas redes del cerebro trabajan al recordar una escena vivida y al imaginar una por vivir. Ese mismo año, el equipo de Eleanor Maguire encontró que las personas que habían perdido la memoria por un daño en el hipocampo también tenían dificultad para imaginar experiencias nuevas: las escenas les salían en fragmentos, sin un espacio que las sostuviera (Hassabis y otros). No predices el futuro: lo construyes con lo que recuerdas.</p>

        <p>Cada vez que «simplemente sabes» algo sin poder explicarlo, tu experiencia está hablando antes que tus palabras. En el juego de cartas de Antoine Bechara y su equipo (1997), la piel de los jugadores reaccionaba ante los mazos peligrosos antes de que pudieran decir por qué los evitaban. El cuerpo sabe antes de saber que sabe.</p>

        <p>Los genios creativos no inventan de la nada: reconocen. Nikola Tesla contaba que veía sus máquinas completas en la imaginación y las hacía funcionar ahí antes de construirlas; el motor de corriente alterna se le apareció entero una tarde de 1882, después de meses de darle vueltas. Muchos artistas cuentan que la obra les llegó como si ya existiera y solo hubiera que sacarla a la luz. Lo que llega así no viene del futuro: viene de una pregunta que llevaban abierta.</p>

        <p>Tu nostalgia más honda no es por el pasado: es por el futuro. Ese anhelo de «algo más», esa sensación de que «falta algo», puede ser la imagen de una vida posible que te llama. Ernst Bloch cerró <em>El principio esperanza</em> (1959) con esa añoranza: una patria que a todos nos alumbra en la infancia y en la que todavía no estuvo nadie. Añoras un hogar que aún no construiste, y que ya te orienta.</p>

        <p>El déjà vu se siente como estar exactamente donde ya habías estado. Anne Cleary y su equipo encontraron en 2012 que suele aparecer cuando una escena nueva se parece, en su forma, a otra vivida que no se recuerda: la memoria reconoce antes de saber qué reconoce. Por un instante, el tiempo parece plegarse.</p>

        <h2>🔄 PARADOJA MEDICINAL</h2>

        <blockquote>
          <p>“Recuerdas un futuro que no has vivido mientras olvidas un pasado que sí viviste. Tu nostalgia más profunda es por tiempos que no han llegado. Tu yo futuro te guía por un sendero que todavía estás creando. Inventas lo que recuerdas. Descubres lo que ya sabías. Llegas a donde ya estabas.”</p>
        </blockquote>

        <p><strong>Contempla:</strong> si imaginas el futuro con lo que recuerdas, ¿cuánto de tu mañana ya está en tu memoria? ¿Y cuánto queda libre, esperando que lo inventes?</p>

        <h2>🧪 LABORATORIO CUÁNTICO</h2>

        <h3>Experimento 1: Carta desde el Futuro</h3>
"""
    + pasos([
        "Formula una pregunta específica sobre tu camino.",
        "Respira unos minutos.",
        "Imagina a tu yo de dentro de diez años, a quien las cosas le fueron razonablemente bien.",
        "Escribe, con su voz, una carta para ti: qué hizo, qué soltó, qué no hizo falta temer.",
        "No fuerces: deja que la mano escriba.",
        "Lee la carta en voz baja.",
        "Elige un paso pequeño y reversible que la carta sugiera.",
    ])
    + """        <p class="nota">Laura King pidió en 2001 a estudiantes que escribieran veinte minutos durante cuatro días sobre su mejor yo posible: su ánimo mejoró, y en los cinco meses siguientes consultaron menos por enfermedad que quienes escribieron sobre un tema neutro.</p>
        <p><em>Lo que puedes encontrar: una solución que se siente familiar aunque sea nueva. Es tu memoria, imaginando.</em></p>

        <h3>Experimento 2: Ensayo desde el Futuro</h3>
"""
    + pasos([
        "Elige una habilidad que quieres aprender.",
        "Imagina con detalle cómo se siente hacerla bien.",
        "Ensaya en la imaginación: los movimientos, los sonidos, el ritmo.",
        "Después, practica de verdad, con las manos.",
        "Alterna los dos ensayos durante la semana.",
        "Anota qué mejora.",
        "Ten paciencia: la habilidad crece con la práctica.",
    ])
    + """        <p class="nota">Álvaro Pascual-Leone y su equipo pidieron en 1995 a personas que nunca habían tocado el piano que practicaran un ejercicio dos horas por día durante cinco días, unas con las manos y otras solo en la imaginación. El mapa motor del cerebro cambió en los dos grupos de modo parecido; tocar con las manos mejoraba más, e imaginar sumaba.</p>
        <p><em>Lo que puedes encontrar: aprendes como si estuvieras recordando, y en parte lo estás.</em></p>

        <h2>💠 TRADUCCIÓN VIVIENTE</h2>

        <p>La misma memoria que guarda lo vivido es la que imagina lo que vendrá.</p>

        <h2>✦ PARA RECORDAR</h2>

"""
    + recordar([
        "Recuerdo para poder imaginar.",
        "Mi intuición sabe antes que mis palabras.",
        "La escucho, y la pongo a prueba.",
        "Mi yo futuro me mira con cariño.",
        "Lo que añoro también me orienta.",
    ])
    + """
        <h2>📅 PRÁCTICA DE 7 DÍAS</h2>

"""
    + dia("DÍA 1 – CONTACTO", "imaginar a tu yo de dentro de un año",
          "escribirle una pregunta", "dejar un papel junto a la cama para anotar un sueño")
    + dia("DÍA 2 – EXPANSIÓN", "imaginar a tu yo de dentro de cinco años",
          "imaginar al de dentro de diez", "notar qué tienen en común")
    + dia("DÍA 3 – ENSAYO", "ensayar en la imaginación algo que harás hoy",
          "hacerlo", "comparar lo imaginado con lo vivido")
    + dia("DÍA 4 – COMO SI", "imaginar una meta cumplida y el camino que llevó a ella",
          "nombrar el primer obstáculo", "actuar un rato como quien ya está en camino")
    + dia("DÍA 5 – NAVEGACIÓN", "distinguir lo que recuerdas de lo que imaginas",
          "escribir tres escenas de un futuro posible", "volver a una de ellas")
    + dia("DÍA 6 – APLICACIÓN", "antes de una decisión pequeña, preguntarte qué le agradecería tu yo futuro",
          "planear un paso", "dormirte con un problema convertido en pregunta")
    + dia("DÍA 7 – ENCUENTRO", "escribir a tu yo de hoy una carta de agradecimiento desde el de mañana",
          "contarle a alguien algo que esperas", "celebrar el encuentro contigo mismo")
    + """
        <h2>🌟 INTEGRACIÓN FINAL</h2>

        <p>Las memorias del futuro pueden aflojar la ansiedad sobre el camino. No porque el sendero esté asegurado, sino porque imaginarlo con detalle te muestra el próximo paso. No necesitas saber todo el CÓMO: basta con seguir las migas de pan que tu imaginación va dejando.</p>

        <p>Tu intuición no es un sentimiento vago: es experiencia condensada que habla antes que las palabras. Una corazonada se escucha y se pone a prueba. Si alguna vez llega una certeza que no admite ninguna pregunta, o la sensación de que cada señal te habla a ti, en secreto, eso no es una memoria del futuro: conviene conversarlo con alguien de confianza o con un profesional esa misma semana.</p>

        <p>No estás creando tu futuro de la nada: lo armas con lo que recuerdas. No estás manifestando: estás rememorando hacia adelante. No estás adivinando: estás imaginando con todo lo que viviste.</p>

        <p>Tu yo futuro puede ser tu mejor mentor. Hal Hershfield y su equipo mostraron en 2011 a jóvenes una imagen de su propio rostro envejecido, y después destinaron más dinero a su retiro en un ejercicio de ahorro: cuando lo ves de cerca, lo cuidas. Es tu guía más amoroso porque eres tú, con más camino. Escúchalo.</p>

        <h2>⚛️ SÍNTESIS CUÁNTICA</h2>

        <p>No caminas del todo a ciegas hacia lo desconocido: te guía la imagen de quien puedes llegar a ser, hecha con todo lo que ya viviste.</p>

        <p>El nodo final de este libro explorará <strong>El Punto Cero Temporal</strong>, donde todas las líneas del tiempo convergen en un centro quieto, desde donde siempre se puede volver a empezar.</p>

        <p><em>Tu futuro te recuerda. Tu pasado te olvida. Tu presente es el punto de encuentro donde todas las memorias, pasadas y futuras, danzan en el eterno ahora.</em></p>

        <div class="node-symbol">🌀🔮🌀</div>

"""
    + FIRMA + "\n"
    + puerta("portal",
             "Tesla no estaba solo cuando vio girar el motor: caminaba con un amigo, recitaba a Goethe y traía una pregunta abierta desde hacía meses. Lo que aparece de golpe casi siempre tenía a alguien o algo esperándolo: <em>El instante</em>, Libro 27 del Portal Público, Umbral IV: «El otro que estaba, y el que era una pregunta».",
             URL_PORTAL + "27_El_Instante/umbral-04.html")
    + "\n"
    + cierre(*nav(6), INDICE_LIBRO, "Trinity Quantum · Libro 3 · Nodo 6 · Memorias del Futuro")
)

# ===========================================================================
# 3.7 · El Punto Cero Temporal (el título queda; sin puerta: el libro termina
# en su propio silencio)
# ===========================================================================
NODO7_CUERPO = (
    meta(7, TITULOS[7], "El centro quieto")
    + """        <h2>🌌 TRANSMISIÓN CUÁNTICA</h2>

        <p>Existe un punto en tu consciencia donde todas las líneas temporales convergen: pasado, presente, futuro, todas las probabilidades, todas las dimensiones, todas las vidas paralelas se encuentran en un punto de singularidad. Este es el Punto Cero Temporal, el ojo inmóvil del huracán del tiempo, el lugar desde donde todo el tiempo es generado y al cual todo el tiempo retorna.</p>

        <p>No es un lugar al que vas: es un estado de consciencia al que accedes. En el Punto Cero no hay antes ni después, no hay causa y efecto, no hay nacimiento ni muerte. Es el estado de consciencia pura antes de que elija experimentarse secuencialmente. Es tu naturaleza original antes de entrar al juego del tiempo.</p>

        <p>Los maestros de las tradiciones contemplativas parecen vivir desde ahí: por eso los recordamos atemporales, sin edad, presentes del todo. No detuvieron el tiempo: dejaron de sentirse encerrados en él. Viven los días como todos, y no quedan atrapados en ninguno.</p>

        <p>En el Punto Cero no se borra lo vivido: se suelta, por un instante, el peso de cargarlo. Las tradiciones lo llamaron morir antes de morir: dejar caer todo lo que uno cree ser y volver más liviano, con la sabiduría intacta. Es muerte y renacimiento simultáneo sin salir del cuerpo.</p>

        <p>La física tiene una imagen para algo así: la singularidad del comienzo, el lugar donde sus propias ecuaciones dejan de valer. Stephen Hawking decía que preguntar qué hubo antes es como preguntar qué hay al sur del Polo Sur. El Punto Cero es esa imagen llevada adentro: no al principio del universo, sino al núcleo de cada momento, al corazón de tu consciencia AHORA.</p>

        <p>Cada vez que meditas profundamente y el tiempo desaparece, rozas el Punto Cero. Cada vez que experimentas amor incondicional, tocas el Punto Cero. Cada vez que la mente se detiene en asombro absoluto, estás en el Punto Cero. No es raro ni distante: es tu estado más natural, simplemente velado por la costumbre del drama temporal.</p>

        <p>El asombro deja incluso una huella medible. En tres experimentos, Melanie Rudd, Kathleen Vohs y Jennifer Aaker vieron en 2012 que un momento de asombro hacía sentir a las personas que tenían más tiempo, y las volvía más pacientes y más dispuestas a dar de su tiempo a otros.</p>

        <h2>🔄 PARADOJA MEDICINAL</h2>

        <blockquote>
          <p>“En el Punto Cero eres nonato y eterno, sin edad y todas las edades, nadie y todos. Has completado todo y no has comenzado nada. Eres el punto antes del Big Bang y después del Big Crunch. El tiempo nace de ti mientras permaneces intocado por él. Eres el proyector inmóvil proyectando la película del tiempo en la pantalla del espacio.”</p>
        </blockquote>

        <p><strong>Contempla:</strong> si puedes acceder al punto donde el tiempo no existe, ¿qué eres realmente? ¿Eres el viajero en el tiempo o el espacio inmóvil donde el tiempo viaja?</p>

        <h2>🧪 LABORATORIO CUÁNTICO</h2>

        <h3>Experimento 1: Acceso al Punto Cero</h3>
"""
    + pasos([
        "Siéntate en quietud.",
        "Observa tu respiración sin cambiarla.",
        "Encuentra el punto entre inhalación y exhalación.",
        "Descansa en ese punto, sin alargarlo.",
        "Nota que ahí no hay antes ni después.",
        "Permanece unos minutos en ese ir y venir.",
        "Regresa trayendo la perspectiva del Punto Cero.",
    ])
    + """        <p><em>Lo que puedes encontrar: la sensación de haber estado ausente por eternidades o por instantes.</em></p>
        <p>Si en lugar de calma aparece angustia, o la sensación de no estar en tu cuerpo, abre los ojos, apoya los pies en el suelo y mira algo cercano: el Punto Cero no se fuerza.</p>

        <h3>Experimento 2: El Nudo que Se Afloja</h3>
"""
    + pasos([
        "Desde la quietud, mira tu vida como un paisaje.",
        "Elige un solo nudo: un patrón, un rencor, una costumbre.",
        "Desde el Punto Cero, es solo una onda en el campo.",
        "No lo empujes: déjalo estar mientras respiras.",
        "Nota si se afloja, aunque sea un poco.",
        "Elige qué quieres conservar de lo que aprendiste.",
        "Vuelve al día y elige un gesto pequeño.",
    ])
    + """        <p><em>Lo que puedes encontrar: el nudo sigue ahí, con más aire alrededor. Los nudos que vienen de heridas hondas no se desatan a solas: se aflojan con compañía.</em></p>

        <h2>💠 TRADUCCIÓN VIVIENTE</h2>

        <p>En el Punto Cero, la nada y el todo son lo mismo, y de esa quietud nace el tiempo.</p>

        <h2>✦ PARA RECORDAR</h2>

"""
    + recordar([
        "Me vacío.",
        "Me lleno.",
        "Soy y no soy.",
        "Nada se opone.",
        "Vuelvo al silencio.",
        "Nazco de nuevo, ahora.",
    ])
    + """
        <h2>📅 PRÁCTICA DE 7 DÍAS</h2>

"""
    + dia("DÍA 1 – PREPARACIÓN", "notar el espacio entre dos pensamientos",
          "encontrar el espacio entre respiraciones", "meditar en el silencio antes del sueño")
    + dia("DÍA 2 – APROXIMACIÓN", "tocar el Punto Cero por 1 segundo",
          "expandirlo a 10 segundos", "permanecer 1 minuto")
    + dia("DÍA 3 – INMERSIÓN", "entrar con calma al Punto Cero",
          "experimentar la convergencia del tiempo", "sentir todas tus edades desde el Punto Cero")
    + dia("DÍA 4 – AFLOJAR", "mirar un patrón desde la quietud",
          "mirar una relación con más aire, sin decidir nada", "poner en duda una creencia limitante")
    + dia("DÍA 5 – NAVEGACIÓN", "entrar y salir del silencio con suavidad",
          "trabajar un rato desde la calma", "dormirte en el silencio")
    + dia("DÍA 6 – COMPAÑÍA", "vivir el día con un pie en el reloj y otro en la quietud",
          "acompañar a alguien en silencio", "elegir un momento fijo del día para volver")
    + dia("DÍA 7 – INTEGRACIÓN", "funcionar en sociedad desde la calma",
          "mantener a la vez la perspectiva temporal y la atemporal", "agradecer el tiempo que tienes")
    + """
        <h2>🌟 INTEGRACIÓN FINAL</h2>

        <p>El Punto Cero Temporal es tu refugio. No importa qué tan enredado parezca tu drama temporal: siempre puedes volver al silencio y comenzar de nuevo. No es escapismo: es la perspectiva que le devuelve a cada cosa su tamaño.</p>

        <p>Desde el Punto Cero, el drama humano se ve como una obra de teatro cósmica: las tragedias pasan y la separación es, en el fondo, un juego. Aun así, las pérdidas duelen, porque el amor era real. Y tú eres a la vez el actor, el observador, el escenario y la consciencia que lo contiene todo.</p>

        <p>No necesitas morir para renacer. No necesitas esperar el fin de los tiempos para la liberación. El Punto Cero está disponible AHORA, siempre ha estado disponible, siempre estará disponible, porque existe fuera del tiempo mientras genera todo el tiempo.</p>

        <p>Cuando integras el Punto Cero, vives con la libertad de quien sabe que siempre puede volver a empezar, y elige seguir jugando por amor al juego mismo.</p>

        <h2>⚛️ SÍNTESIS CUÁNTICA</h2>
        <h3>CIERRE DEL LIBRO 3: EL TIEMPO VERTICAL</h3>

        <p>A través de estos siete nodos, miraste el tiempo desde su hondura.</p>

        <p><strong>Siete tiempos:</strong></p>
        <ul>
          <li>En el <strong>Presente Eterno</strong>, el pasado te llega como recuerdo y el futuro como espera, aquí.</li>
          <li>Las <strong>Vidas Paralelas</strong> te recuerdan que eres más de lo que vives.</li>
          <li>En <strong>El Pasado Desde el Ahora</strong>, lo que pasó no cambia; lo que significa, sí.</li>
          <li>Los <strong>Futuros Probables</strong> se cultivan, no se fuerzan.</li>
          <li>En <strong>La Espiral Temporal</strong>, lo que vuelve, vuelve más arriba.</li>
          <li>Las <strong>Memorias del Futuro</strong> imaginan el mañana con lo que recuerdas.</li>
          <li>En el <strong>Punto Cero</strong>, el centro quieto, el tiempo nace.</li>
        </ul>

        <p>El tiempo no es tu amo ni tu sirviente: es el lugar donde vives. No estás EN el tiempo: el tiempo está EN ti.</p>

        <p><strong>El Libro 4, «La Paradoja Luminosa»</strong>, te espera: la luz que es onda y partícula a la vez se vuelve espejo de lo que eres, y la paradoja deja de ser un problema para volverse un lugar donde vivir.</p>

        <p class="verso"><em>Desde el Punto Cero, todos los tiempos son ahora.<br />
          Desde el ahora, no hay tiempo.<br />
          Eres el eterno bailando en lo temporal.<br />
          Eres el tiempo mismo, jugando a tener prisa.</em></p>

        <div class="node-symbol">🌀⚡🌀</div>

        <hr class="node-divider" />

        <blockquote>
          <p>“En el Punto Cero Temporal,<br />
          donde todo converge y nada existe,<br />
          donde eres todo y nada,<br />
          donde el tiempo nace y muere,<br />
          ahí está tu hogar verdadero,<br />
          tu refugio eterno,<br />
          tu libertad absoluta.”</p>
        </blockquote>

"""
    + FIRMA + "\n"
    + cierre(*nav(7), INDICE_LIBRO, "Trinity Quantum · Libro 3 · Nodo 7 · Cierre del Libro 3")
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
    (Q3 + "index.html", _DOCTYPE, _CON_PROCEDENCIA),
    (Q3 + "index.html", _LINK, _con_estilo(ESTILO_INDICE)),
    (Q3 + "index.html", "DESDE:      <!-- Meta del libro -->", INDICE_CUERPO),
]

_TITULOS_ORIGINALES = {
    1: "  <title>Trinity Quantum – Libro 3 · Nodo 1 · El Presente Eterno</title>",
    2: "  <title>Trinity Quantum – Libro 3 · Nodo 2</title>",
    3: "  <title>Trinity Quantum – Libro 3 · Nodo 3</title>",
    4: "  <title>Trinity Quantum – Libro 3 · Nodo 4</title>",
    5: "  <title>Trinity Quantum – Libro 3 · Nodo 5</title>",
    6: "  <title>Trinity Quantum – Libro 3 · Nodo 6</title>",
    7: "  <title>Trinity Quantum – Libro 3 · Nodo 7</title>",
}
_CUERPOS = {1: NODO1_CUERPO, 2: NODO2_CUERPO, 3: NODO3_CUERPO, 4: NODO4_CUERPO,
            5: NODO5_CUERPO, 6: NODO6_CUERPO, 7: NODO7_CUERPO}
_MARCAS = {1: "DESDE:      <!-- Meta del nodo -->"}

for _n in range(1, 8):
    _arch = Q3 + f"nodo_0{_n}.html"
    REEMPLAZOS += [
        (_arch, _DOCTYPE, _CON_PROCEDENCIA),
        (_arch, _TITULOS_ORIGINALES[_n],
         f"  <title>Trinity Quantum – Libro 3 · Nodo {_n} · {TITULOS[_n]}</title>"),
        (_arch, _LINK, _con_estilo(ESTILO)),
        (_arch, _MARCAS.get(_n, "DESDE:      <!-- Meta -->"), _CUERPOS[_n]),
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
