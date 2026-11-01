#!/usr/bin/env python3
"""
Depuración de Quantum 5, *El Portal Infinito* (31 de octubre de 2026), el
cuarto de la revisión completa de Quantum, con el veto de Arturo en cada
tarjeta (5.0 a 5.7). Arturo aprobó todo y dejó a criterio de Claude cómo
resolver la escalera de iniciaciones, con una condición: cada libro de Quantum
es parte de una serie y debe tener coherencia con los demás.

Lo decidido: el libro obedece su última instrucción («Olvida que eres portal.
Vive normalmente») y su propia advertencia («No son niveles secuenciales sino
dimensiones simultáneas»). Los títulos de sección quedan, como en Quantum 4 y
13; cambia lo de adentro. Cada «Portal al Siguiente Nodo» toma la fórmula de
Quantum 4 («No es un examen de ingreso; es una manera de llegar»), las frases
de cuidado repiten la letra de los libros anteriores y el 5.7 cierra con
«Siete puertas» y lleva al Libro 6.

Método (maestro v4, sección 5): cada reemplazo aprobado se aplica exactamente
una vez sobre el original de la etiqueta `quantum-original`. En los ocho
archivos se cambian la cabecera (nota de procedencia; en los nodos 2 y 3 sale
el comentario que estaba antes del DOCTYPE), el <head> (estilo de la
depuración) y el cuerpo, que se reemplaza desde la marca que abre los
metadatos hasta el final del archivo. En el nodo 7, además, la navegación
superior lleva al Libro 6.

Uso:  python3 depurar_quantum5.py RUTA_A_UNA_COPIA_DEL_ORIGINAL
      (por ejemplo, el contenido de la etiqueta quantum-original, o el
      repositorio Trinity- si Libro_05 todavía no fue depurado)
"""
import sys
from pathlib import Path

Q5 = "02_Trinity_Quantum/Libro_05/"

PROCEDENCIA = (
    "<!-- Depurado el 31 de octubre de 2026 según la guía de depuración de Quantum "
    "(Arquitectura del Destino, maestro v4, sección 5, con las cuatro precisiones "
    "de la revisión completa), con el veto de Arturo en cada tarjeta. El original "
    "se conserva en la etiqueta quantum-original del repositorio. -->"
)

URL_ARQ = "https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/"
URL_PORTAL = "https://soyartur-trinity.github.io/Trinity_Portal_Publico/01_Libros/"

# ---------------------------------------------------------------------------
# Estilos: los de Quantum 2 y 3 (Quantum 5 comparte la hoja común, que no
# cubre subtítulos, listas numeradas ni citas), con los dos colores de la
# puerta y el verso final.
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
    .node-content .nota{ color: rgba(246, 240, 255, .82); }
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

FIRMA = '        <p class="signature"><strong>— Trinity Quantum · El Portal Infinito</strong></p>\n'

TITULOS = {
    1: "La Arquitectura del Portal",
    2: "El Viajero Dimensional",
    3: "El Tejedor de Realidades",
    4: "El Guardián de los Umbrales",
    5: "El Arquitecto de Puentes",
    6: "El Alquimista del Vacío",
    7: "El Portal Viviente",
}


# ---------------------------------------------------------------------------
# Piezas que se repiten
# ---------------------------------------------------------------------------
def pasos(items):
    filas = "\n".join(f"          <li>{x}</li>" for x in items)
    return f"        <ol>\n{filas}\n        </ol>\n"


def lista(items):
    filas = "\n".join(f"          <li>{x}</li>" for x in items)
    return f"        <ul>\n{filas}\n        </ul>\n"


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


def meta(n, subtitulo):
    return (
        "      <!-- Meta del nodo -->\n"
        '      <section class="node-meta">\n'
        '        <div class="node-book-title">Libro 5 · El Portal Infinito</div>\n'
        f'        <h1 class="node-heading">Nodo {n}: {TITULOS[n]}</h1>\n'
        f'        <div class="node-index">Nodo {n} de 7 · {subtitulo}</div>\n'
        "      </section>\n\n"
        "      <!-- Contenido -->\n"
        '      <main class="node-content">\n\n'
    )


def cierre(n, subpie):
    ant = (f"nodo_0{n-1}.html", f"← Nodo {n-1}: {TITULOS[n-1]}") if n > 1 else ("index.html", "← Índice del Libro")
    sig = (f"nodo_0{n+1}.html", f"Nodo {n+1}: {TITULOS[n+1]} →") if n < 7 else ("../Libro_06/index.html", "Libro 6: El Vacío Creativo →")
    return (
        "      </main>\n\n"
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
        '        <div class="footer-line">TRINITY QUANTUM · Libro 5 · El Portal Infinito</div>\n'
        f'        <div class="footer-subline">Nodo {n}: {TITULOS[n]} · {subpie}</div>\n'
        '        <div class="footer-sigil">🌀⟡🌀</div>\n'
        "      </footer>\n\n"
        "    </div>\n"
        "  </div>\n"
        "</body>\n"
        "</html>\n"
    )


def siguiente(n, gesto, linea):
    ordinal = {2: "segundo", 3: "tercer", 4: "cuarto", 5: "quinto", 6: "sexto", 7: "séptimo y último"}[n]
    return (
        "        <h3>Portal al Siguiente Nodo</h3>\n"
        f"        <p>Antes del {ordinal} nodo, <em>{TITULOS[n]}</em>, puedes probar esto: {gesto} No es un examen de ingreso; es una manera de llegar.</p>\n"
        f"        <p>{linea}</p>\n\n"
    )


# ===========================================================================
# 5.0 · Índice
# ===========================================================================
INDICE_CUERPO = """      <!-- Meta del libro -->
      <section class="node-meta">
        <div class="node-book-title">Libro 5 · El Portal Infinito</div>
        <h1 class="node-heading">La Consciencia Como Puerta Dimensional</h1>
        <div class="node-index">Arquitectura · Viaje · Tejido · Custodia · Puentes · Vacío · Portal Viviente</div>
      </section>

      <!-- Contenido -->
      <main class="node-content">

        <section class="node-section">
          <h2>El Umbral que Eres</h2>

          <p>No eres un lugar al que llegan las cosas: eres el umbral por donde pasan. La práctica no es abrirlo; es dejar de cerrarlo.</p>

          <p>En este libro, una dimensión es un mundo de experiencia: el sueño y la vigilia, el amor y el miedo, la obra que te absorbe, la lengua en que recuerdas. Entras y sales de esos mundos muchas veces al día, casi siempre sin notarlo. Cada Nodo mira ese paso desde un lado distinto: la puerta, el viaje, el tejido, la custodia, el puente, el vacío y la vida entera vuelta umbral.</p>

          <p>Umbral, en latín, se dice <em>limen</em>. En 1909, el etnógrafo Arnold van Gennep eligió esa palabra para nombrar el tiempo del medio en los ritos de paso, porque en ellos casi todo ocurría ante una puerta: alguien se separa de lo que era, permanece un tiempo en el umbral y vuelve a los suyos transformado.</p>

          <p>Lee en orden si deseas la espiral completa; salta a un Nodo si el Portal te llama desde un punto específico. Los siete no son escalones: son siete caras de la misma puerta.</p>
        </section>

        <hr />

        <!-- Lista de Nodos -->
        <section class="node-section">
          <h2>Nodos del Libro 5</h2>

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

          <div style="margin-top: 18px;">
            <h3><a href="nodo_01.html" class="nav-link">Nodo 1: La Arquitectura del Portal</a></h3>
            <p>Ya eres umbral: cada percepción, cada recuerdo y cada encuentro pasan por ti.</p>

            <h3><a href="nodo_02.html" class="nav-link">Nodo 2: El Viajero Dimensional</a></h3>
            <p>Moverse entre los estados del día y saber volver: la vuelta es lo más importante del viaje.</p>

            <h3><a href="nodo_03.html" class="nav-link">Nodo 3: El Tejedor de Realidades</a></h3>
            <p>Tejer la vida con los hilos que tienes en las manos, a solas y con otros.</p>

            <h3><a href="nodo_04.html" class="nav-link">Nodo 4: El Guardián de los Umbrales</a></h3>
            <p>Los límites como cuidado: proteger sin cerrar, acompañar sin cruzar por nadie.</p>

            <h3><a href="nodo_05.html" class="nav-link">Nodo 5: El Arquitecto de Puentes</a></h3>
            <p>Puentes entre el corazón y la mente, entre personas, sobre lo que se rompió.</p>

            <h3><a href="nodo_06.html" class="nav-link">Nodo 6: El Alquimista del Vacío</a></h3>
            <p>El vacío como lugar fértil: no se llena a la fuerza; se habita.</p>

            <h3><a href="nodo_07.html" class="nav-link">Nodo 7: El Portal Viviente</a></h3>
            <p>La vida entera como puerta, vivida con naturalidad.</p>
          </div>
        </section>

        <hr />

        <!-- Cierre del Índice -->
        <section class="node-section">
          <h2>Antes de Empezar</h2>
          <p><em>Al abrir cualquiera de estos Nodos, abre también una parte de ti. Este Libro no se recorre: se encarna. Si sientes el llamado, comienza por el Nodo 1. Si sientes el umbral, elige el Nodo que te elija.</em></p>
          <p><strong>∞ El Portal Infinito ∞</strong></p>
          <p class="signature"><strong>— Trinity Quantum · El Portal Infinito</strong></p>
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
        <div class="footer-line">TRINITY QUANTUM · Libro 5 · El Portal Infinito</div>
        <div class="footer-subline">Índice: La Consciencia Como Puerta Dimensional</div>
        <div class="footer-sigil">🌀⟡🌀</div>
      </footer>

    </div>
  </div>
</body>
</html>
"""

# ===========================================================================
# 5.1 · La Arquitectura del Portal (el título queda)
# ===========================================================================
NODO1_CUERPO = (
    meta(1, "El umbral")
    + """        <h2>La Consciencia Como Puerta Dimensional</h2>

        <h3>Transmisión Inicial</h3>
        <p>Después de diseñar con la luz, reconocer los hilos que nos unen, habitar la hondura del tiempo y vivir la paradoja luminosa, llegamos al umbral donde la consciencia misma se revela como puerta entre todas las dimensiones.</p>
        <p>No eres un ser que tiene experiencias dimensionales. Eres el portal a través del cual las dimensiones se experimentan a sí mismas. Cada estado de consciencia es una puerta a un mundo entero. Cada percepción, un pasaje entre lo que está afuera y lo que se vuelve tuyo. Cada pensamiento abre o cierra un mundo posible.</p>
        <p>El Portal Infinito no es un lugar al que ir sino un reconocimiento de lo que ya eres: la apertura consciente entre todo lo que es, fue y será.</p>

        <hr />

        <h2>Cómo la Consciencia Crea Puertas Entre Mundos</h2>

        <h3>El Umbral Que Eres</h3>
        <p>En este preciso instante, mientras estos signos se vuelven sentido en ti, no estás leyendo sobre portales: estás siendo uno. Tu consciencia es la apertura por donde el universo de estas palabras se encuentra con el universo de tu comprensión. No hay solo transmisión de información: hay encuentro.</p>
        <p>Cada vez que percibes algo, abres una puerta entre quien observa y lo observado. Pero aquí está la revelación: no son dos mundos separados que se conectan. Es uno solo que se pliega sobre sí mismo, creando la ilusión de separación para poder vivir el éxtasis del encuentro.</p>

        <h3>La Geometría Sagrada del Portal</h3>
        <p>Tu sistema nervioso no es una red de cables que transmiten señales: es una arquitectura de umbrales. Cada neurona recibe muchas voces a la vez y solo responde cuando lo que le llega alcanza su umbral; entonces dispara entera, o no dispara. Entre una neurona y la siguiente queda una hendidura mínima donde la señal cambia de idioma: llega eléctrica, cruza química y sigue eléctrica del otro lado.</p>
        <p>Cuando Charles Sherrington buscó en 1897 un nombre para ese lugar, propuso primero uno que sugería fusión. Arthur Verrall, un helenista amigo de su maestro Michael Foster, le ofreció otro, <em>sinapsis</em>, que en griego evoca enlazar: dos que se tocan sin dejar de ser dos. Tu cerebro no es un cosmopuerto: es una casa de umbrales.</p>
        <p>Las geometrías que aparecen en algunos estados de consciencia —túneles, espirales, panales, telarañas— se ven también ante luces que parpadean o en el borde del sueño. En la década de 1920, el psicólogo Heinrich Klüver las ordenó en cuatro familias y las llamó constantes de forma. En 2001, Paul Bressloff, Jack Cowan y su equipo propusieron por qué se repiten: su dibujo lo trazan las conexiones entre la retina y la primera corteza visual. Son alucinaciones y, a la vez, planos: lo que ves es la arquitectura de tu propia mirada haciéndose visible.</p>

        <h3>Práctica: El Portal Que Ya Está Abierto</h3>
"""
    + pasos([
        "<strong>El centro.</strong> Lleva la atención al punto entre las cejas, el que la tradición del yoga llama tercer ojo. Siente a la vez la coronilla. Percibe tu corazón como centro. Deja que la atención una los tres puntos: el espacio que forman no contiene el portal; lo es.",
        "<strong>La apertura.</strong> No imagines que se abre un portal. Reconoce que ya está abierto: siempre lo estuvo. Tu práctica es dejar de cerrarlo. Afloja la tensión que sostiene la ilusión de solidez.",
        "<strong>La estabilidad.</strong> Respira como si el aire entrara por el portal y no solo por los pulmones. Cada inhalación trae el mundo; cada exhalación suelta lo que ya no necesitas. Mantén la apertura sin forzar, como se sostiene una puerta abierta en el viento.",
    ])
    + """        <p class="nota">Si en algún momento aparece una extrañeza incómoda, como si te miraras desde afuera, abre los ojos, apoya los pies y mira algo cercano: la práctica termina ahí.</p>

        <h3>Portales Temporales</h3>
        <p>Tu memoria no es un archivo del pasado. Cuando recuerdas, no sacas una copia guardada: reconstruyes la escena desde tu presente, y al guardarla otra vez guardas también algo de hoy. Por eso los recuerdos cambian: cada vez que abres esa puerta, entras desde un ángulo apenas distinto. Lo que pasó no cambia; lo que significa todavía se está diciendo.</p>
        <p>El futuro también está lleno de puertas. Cada intención es una que abres hacia adelante. La ansiedad es sentir muchas abiertas a la vez sin poder elegir por cuál pasar; Søren Kierkegaard, en 1844, la llamó el vértigo de la libertad. La esperanza es sostener una abierta hasta que puedas alcanzarla. Cuando la preocupación ya no te deja dormir ni descansar, tiene tratamiento: pedirlo también es elegir un futuro.</p>

        <h3>Portales Relacionales</h3>
        <p>Cada persona en tu vida es un portal a un mundo completo de experiencia. No te relacionas CON personas; te relacionas A TRAVÉS de personas hacia aspectos del infinito que solo ellas pueden revelar.</p>
        <p>El amor no es solo un sentimiento: es la expansión súbita del portal. El conflicto es cuando dos portales intentan ocupar el mismo espacio. La intimidad es cuando dos portales se alinean tan bien que crean un túnel estable entre mundos.</p>

        <h3>Práctica del Portal Relacional</h3>
"""
    + pasos([
        "En tu próxima conversación significativa,",
        "no veas a la persona como un objeto sólido:",
        "percíbela como un portal viviente.",
        "¿A qué mundo te está invitando?",
        "¿Qué aspecto del infinito te muestra?",
        "Entra en la conversación como entrarías en un templo,",
        "con reverencia por el misterio del otro lado.",
    ])
    + """
        <h3>El Cuerpo Como Sistema Portal</h3>
        <p>La tradición del yoga describe siete centros a lo largo de la columna, los chakras, y a cada uno le atribuye una puerta:</p>
"""
    + lista([
        "<strong>Raíz</strong>: portal a la dimensión de la materia",
        "<strong>Sacro</strong>: portal a la dimensión del flujo y la creación",
        "<strong>Plexo Solar</strong>: portal a la dimensión del poder personal",
        "<strong>Corazón</strong>: portal a la dimensión del amor incondicional",
        "<strong>Garganta</strong>: portal a la dimensión de la expresión",
        "<strong>Tercer Ojo</strong>: portal a la dimensión de la visión",
        "<strong>Corona</strong>: portal a la dimensión de la unidad",
    ])
    + """        <p>Pero estos son solo los portales principales. Cada poro de tu piel es una pequeña frontera viva. Cada célula vive de una membrana que elige qué entra y qué sale. Eres un queso suizo multidimensional: más apertura que cierre.</p>

        <h3>Portales Oníricos</h3>
        <p>El sueño es el estado donde tu función portal opera sin las riendas del yo despierto. Por eso los sueños son tan extraños: mezclan mundos que de día mantienes separados.</p>
        <p>Los sueños lúcidos ocurren cuando sabes, dentro del sueño, que estás soñando. Entonces eres a la vez el viajero y la puerta.</p>

        <h3>Portales de Crisis</h3>
        <p>Las crisis existenciales, los momentos de quiebre, las noches oscuras del alma pueden ser puertas que se abren tan de golpe que el sistema no alcanza a procesarlas. A veces lo que se derrumba es un mundo pequeño que ya no alcanzaba para contenerte, y del otro lado espera uno más amplio. Pero la noche que dura semanas no se espera a solas: se consulta.</p>
        <p>La enfermedad no es un portal forzado ni la prueba de que algo en ti estaba cerrado o rígido. El cuerpo enfermo pide cuidado, y cuidarlo con quienes saben también es cruzar una puerta: la de dejarse acompañar. Ninguna forma de sufrir es falta de quien la vive.</p>

        <h3>Para Habitar el Portal</h3>
        <p><strong>Práctica de las Tres Puertas</strong></p>
"""
    + pasos([
        "Siéntate en un lugar tranquilo y nombra tres puertas: una hacia tu niñez, otra hacia tu vejez, otra hacia el camino que no tomaste.",
        "Míralas abiertas, sin entrar en ninguna.",
        "Deja que algo pase de una a otra: una pregunta, una imagen, una ternura.",
        "Nota qué mira distinto tu presente.",
        "Ciérralas con calma, una por una.",
        "Anota lo que quedó de cada mundo.",
    ])
    + """        <p class="nota">Si alguna de esas puertas duele demasiado, ciérrala: se vuelve otro día, o acompañado.</p>

        <h3>Portales Colectivos</h3>
        <p>Los lugares sagrados son puertas que muchas generaciones mantuvieron abiertas con su atención. Las ciudades son encrucijadas donde mundos distintos se cruzan cada día.</p>
        <p>Internet es el intento tecnológico de crear un sistema de portales global. Cada pantalla es un portal rudimentario; cada clic, un salto menor. Pero comparado con tu capacidad de encuentro, es como comparar el dibujo de una puerta con una puerta real.</p>

        <h3>El Guardián del Portal</h3>
        <p>Tú no solo eres el portal: eres también su guardián. Eliges qué dejas entrar y qué no, qué mundos permites que se toquen a través de ti, a qué le das lugar en tu día.</p>

        <h3>La Primera Transmutación Portal</h3>
        <p>Este primer nodo no es información sobre portales. Es una invitación a reconocer lo que ya ocurre: cada palabra que entendiste pasó por ti, y al pasar se volvió tuya.</p>
        <p>No aprendiste sobre portales. Recordaste que eres uno. No un ser con acceso a otras dimensiones, sino el acceso mismo haciéndose consciente.</p>

"""
    + siguiente(2, "durante cinco respiraciones completas, sentirte a la vez el portal, el viajero que lo cruza y el guardián que lo cuida.",
                "La arquitectura del portal ya está a la vista. Ahora aprenderás a recorrerla.")
    + """        <blockquote>
          <p>En este momento, mientras terminas este primer nodo, siente todas las puertas que abriste sin darte cuenta: hacia quien escribió estas palabras, hacia lo que ellas tocan, hacia la persona que serás mañana, que llevará algo de esto consigo. No las cierres todavía. Déjalas respirar.</p>
        </blockquote>

"""
    + FIRMA + "\n"
    + cierre(1, "El umbral")
)

# ===========================================================================
# 5.2 · El Viajero Dimensional (el título queda)
# ===========================================================================
NODO2_CUERPO = (
    meta(2, "La vuelta")
    + """        <h2>Navegando Conscientemente Entre Realidades</h2>

        <h3>El Pasaporte Cuántico</h3>
        <p>No necesitas credenciales para viajar entre mundos. Tu consciencia es el único pasaporte requerido. Pero como todo viajero experimentado sabe, no basta el documento: importa cómo lo presentas. Tu atención es tu visa. Tu coherencia, tu permiso de entrada. Tu intención, tu itinerario.</p>
        <p>Has estado viajando toda tu vida sin saberlo. Cada cambio de humor es un salto pequeño. Cada sueño, un viaje al extranjero de la consciencia. Cada vez que una canción te devuelve a otra década, cruzaste una frontera.</p>

        <h3>La Cartografía de lo Infinito</h3>
        <p>Los mundos de la experiencia no están ordenados como pisos de un edificio ni como países en un mapa. Se parecen más a un holograma, donde cada punto guarda algo del todo: desde cualquier instante puedes llegar a cualquier otro.</p>
        <p><strong>Tu mapa personal</strong> no es igual al de nadie. Lo dibujan:</p>
"""
    + lista([
        "tu historia y lo que hiciste con ella",
        "tu cuerpo y su temperamento",
        "las lenguas que hablas",
        "los vínculos que te formaron",
        "los lugares donde viviste",
        "los hábitos de cada día",
    ])
    + """        <p>Cada mundo guarda su propia memoria. En 2000, Viorica Marian y Ulric Neisser entrevistaron a inmigrantes rusos en los Estados Unidos: cuando la conversación era en ruso, recordaban más escenas de su vida antes de emigrar; cuando era en inglés, más de su vida nueva. Cada lengua abría una puerta a su propio pasado. El efecto se encontró después con otros pares de lenguas.</p>

        <h3>Práctica del Mapa</h3>
"""
    + pasos([
        "<strong>El territorio cercano.</strong> Cierra los ojos y nota en qué mundo estás ahora: el del trabajo, el del cansancio, el de la espera. No lo cambies: nómbralo.",
        "<strong>Las rutas conocidas.</strong> ¿Qué mundos visitas a menudo? El del sueño profundo, el de la creatividad, el del amor, el del miedo. Nota cuáles son autopistas y cuáles, senderos poco transitados.",
        "<strong>Las rutas nuevas.</strong> Piensa en mundos que casi nunca visitas y que te llaman: un oficio, un paisaje, una lengua, una forma de silencio. Elige uno para esta semana, en pequeño.",
    ])
    + """
        <h3>El Arte del Salto Dimensional</h3>
        <p>El salto no es movimiento a través del espacio sino cambio de estado. No vas a otro lugar: sintonizas otra estación de la misma radio. Tu cuerpo permanece; tu consciencia cambia de canal.</p>

        <p><strong>1. Micro-saltos (constantes)</strong></p>
        <p>Parpadeas de quince a veinte veces por minuto, y en cada parpadeo la vista se apaga un instante. No lo notas porque el cerebro baja la sensibilidad visual justo en ese momento y cose la continuidad: Volkmann, Riggs y Moore mostraron en 1980 que ese apagón se borra en buena parte desde el cerebro, no desde el ojo. Vives entre pequeñas pausas que tu mente vuelve un solo mundo.</p>

        <p><strong>2. Saltos medianos (diarios)</strong></p>
"""
    + lista([
        "El paso del sueño a la vigilia",
        "La entrada en un estado de flujo",
        "La inspiración súbita",
        "Los cambios emocionales profundos",
    ])
    + """
        <p><strong>3. Saltos grandes (transformadores)</strong></p>
"""
    + lista([
        "Las que Abraham Maslow estudió como experiencias cumbre: instantes de asombro y plenitud en que todo parece en su lugar",
        "Un nacimiento, un duelo, una conversión",
        "Las iniciaciones de cada tradición",
    ])
    + """
        <p>En 1909, el etnógrafo Arnold van Gennep encontró que los ritos de paso de pueblos muy distintos —nacimientos, iniciaciones, bodas, funerales— siguen tres tiempos: alguien se separa de lo que era, permanece un tiempo en el umbral y vuelve a los suyos con un lugar nuevo entre ellos. Al tiempo del medio lo llamó con la palabra latina <em>limen</em>, porque esos ritos estaban llenos de puertas. Medio siglo después, Victor Turner describió a quien lo atraviesa como alguien que no está ni aquí ni allá. Todo salto tiene esos tres tiempos: despegue, vuelo y regreso.</p>

        <h3>Práctica del Salto Consciente</h3>
        <p><strong>Preparación:</strong> nota tu estado actual. Elige hacia dónde quieres ir: de la prisa a la calma, del enojo a la claridad, del cansancio a la frescura. Suelta el apego al resultado.</p>
"""
    + pasos([
        "<strong>El impulso.</strong> Dale al cambio un vehículo: una caminata corta, una canción, tres respiraciones con la exhalación larga, lavarte la cara.",
        "<strong>El despegue.</strong> Suelta por un momento lo que estabas haciendo, sin pelear con ello.",
        "<strong>El vuelo.</strong> Mantén tu intención sin forzarla. Deja que el nuevo estado llegue a su ritmo. No anticipes cómo se sentirá.",
        "<strong>El aterrizaje.</strong> Cuando llegue, quédate un minuto. Nota qué cambió en el cuerpo, en la voz, en la mirada. No juzgues el lugar nuevo enseguida: dale tiempo a tu sistema para acomodarse.",
    ])
    + """
        <h3>Los Peligros del Viaje Dimensional</h3>
"""
    + lista([
        "<strong>Dispersión:</strong> la atención repartida en muchos mundos y en ninguno. <em>Solución:</em> volver a uno, el de este cuerpo, aquí.",
        "<strong>Desfase:</strong> el cuerpo llega antes que la consciencia, o al revés. <em>Solución:</em> anclaje gradual y paciente.",
        "<strong>Apego a los estados:</strong> preferir los estados extraordinarios a la vida común. El psicólogo John Welwood, alumno del maestro tibetano Chögyam Trungpa, llamó en 1984 atajo espiritual (<em>spiritual bypassing</em>) a usar la práctica para saltear lo que duele. <em>Solución:</em> lo sagrado en lo ordinario.",
        "<strong>Lo no digerido:</strong> traer de vuelta algo que todavía no entiendes. <em>Solución:</em> digerirlo despacio y contarlo a alguien de confianza.",
    ])
    + """        <p class="nota">Otra cosa es sentir que ya no eres tú, que el mundo parece irreal o que pierdes horas sin recuerdo: eso no es un viaje, y pide consulta esa misma semana.</p>

        <h3>El Viajero Como Puente</h3>
        <p>Tu función como viajero no es escapar de esta realidad sino enriquecerla con lo que traes de otros mundos. Eres un embajador entre mundos, un traductor de realidades, un contrabandista de posibilidades.</p>
        <p>Cada vez que traes inspiración de la creación, sabiduría del sueño o amor del corazón, cumples tu función de puente. No viajas solo para ti: viajas para el todo.</p>

        <h3>Dimensiones Paralelas del Yo</h3>
        <p>Hay muchas versiones posibles de ti: la que tomó otras decisiones, la que nació en otras circunstancias, la que desarrolló otros talentos, la que está más adelante o más atrás en el camino. No hace falta que existan en otro lugar para que te enseñen algo: basta con imaginarlas con honestidad. En 1986, Hazel Markus y Paula Nurius las llamaron yoes posibles: el que te gustaría llegar a ser, el que temes llegar a ser, el que podrías llegar a ser.</p>

        <h3>Práctica: Carta Desde Otra Versión</h3>
"""
    + pasos([
        "Elige una versión tuya: la que tomó otro camino en una encrucijada que recuerdes.",
        "Imagínala con detalle: dónde vive, qué hace un martes cualquiera.",
        "Escribe una carta desde su voz, dirigida a ti.",
        "Deja que te cuente qué ganó y qué perdió.",
        "Respóndele desde tu vida de hoy.",
        "Agradece el encuentro y guarda la carta.",
    ])
    + """        <p><em>Lo que puedes encontrar: no un dato de otro mundo, sino una mirada nueva sobre el tuyo.</em></p>

        <h3>El Turismo y la Peregrinación</h3>
        <p><strong>El turista dimensional:</strong></p>
"""
    + lista([
        "Busca experiencias novedosas",
        "Colecciona estados alterados",
        "No integra lo vivido",
        "Permanece sin cambiar",
    ])
    + """        <p><strong>El peregrino dimensional:</strong></p>
"""
    + lista([
        "Viaja con propósito sagrado",
        "Busca transformación, no entretenimiento",
        "Integra cada experiencia",
        "Regresa transformado",
    ])
    + """        <p><strong>Sé peregrino, no turista.</strong> Cada mundo que visitas es sagrado y merece reverencia.</p>

        <h3>Navegación por Resonancia</h3>
        <p>Los mundos no se encuentran mediante esfuerzo sino mediante resonancia. No puedes forzar tu entrada a uno: tienes que ponerte en su tono. Es como la radio: no puedes escuchar una estación que no sintonizas.</p>
"""
    + pasos([
        "<strong>Resonancia emocional.</strong> Para acceder al mundo del amor, genera amor. Para el de la paz, cultiva paz. La emoción es tu dial.",
        "<strong>Resonancia mental.</strong> Ciertos pensamientos abren ciertos mundos: los koans abren los de la paradoja; las matemáticas, los del orden.",
        "<strong>Resonancia del cuerpo.</strong> Distintas posturas abren distintos mundos: la danza, los de la fluidez; la quietud, los del vacío.",
    ])
    + """
        <h3>El Regreso: La Parte Más Importante</h3>
        <p>El viaje no está completo hasta que regresas e integras. Muchos se pierden en el viaje y olvidan volver. Otros regresan pero no pueden traducir lo vivido. El arte está en el retorno consciente.</p>
        <p>Jack Kornfield, que fue monje budista antes de ser psicólogo, lo dijo con el título de un libro del año 2000, <em>Después del éxtasis, la colada</em>. La experiencia más alta termina, y al día siguiente hay ropa para lavar.</p>

        <h3>Práctica de Retorno e Integración</h3>
"""
    + pasos([
        "<strong>Antes de regresar,</strong> elige algo que quieras traer.",
        "<strong>Durante el regreso,</strong> mantén un hilo de conexión.",
        "<strong>Al llegar,</strong> no hables enseguida de la experiencia.",
        "<strong>Deja que se asiente:</strong> días o semanas.",
        "<strong>Intégrala de a poco:</strong> en arte, en escritura, en un cambio pequeño de tu vida.",
        "<strong>Comparte con sabiduría:</strong> no todos necesitan conocer todos tus viajes.",
    ])
    + """
        <h3>Los Aliados Dimensionales</h3>
        <p>En cada mundo aparecen figuras que pueden servir de guía:</p>
"""
    + lista([
        "En el sueño, los maestros del sueño",
        "En la creación, las musas",
        "En el dolor, quienes alguna vez te cuidaron",
        "En el amor, quienes te enseñaron a amar",
    ])
    + """        <p>Estos aliados no son externos a ti: son aspectos de tu consciencia que aparecen como “otros” para poder enseñarte. Carl Jung conversó durante años con una figura interior a la que llamó Filemón. En sus memorias, recogidas por Aniela Jaffé, contó lo que aprendió de él: que los pensamientos son como animales en el bosque o personas en una habitación, y que hay en uno algo que dice cosas que uno no sabe ni se propone. Respeta a tus aliados como respetarías a partes sabias de ti mismo.</p>
        <p class="nota">Si alguna vez esas voces se oyen desde afuera, dan órdenes o asustan, ya no son aliados de la imaginación: es momento de consultar esa misma semana.</p>

        <h3>El Diario del Viajero</h3>
        <p>Lleva un registro de tus viajes:</p>
"""
    + lista([
        "Fecha y hora",
        "El mundo que visitaste",
        "Cómo llegaste",
        "Lo que viviste",
        "Lo que te quedó",
        "Cómo te sentiste después",
        "Lo que integraste",
    ])
    + """        <p>Este diario se convertirá en tu manual personal de navegación, único e intransferible.</p>

        <h3>La Segunda Transmutación Portal</h3>
        <p>Ya no eres solo un portal: también eres un viajero consciente. Conoces los mapas, los métodos, los peligros y lo que se gana. Pero más importante: reconoces que cada momento de tu vida es un viaje. No hay momentos ordinarios, solo viajes no reconocidos.</p>

"""
    + siguiente(3, "notar tres veces esta semana el paso de un estado a otro, y qué trajiste de vuelta.",
                "Del viaje pasarás al tejido: no solo visitar mundos, sino tejer algo nuevo entre ellos.")
    + """        <blockquote>
          <p>Al cerrar este nodo, nota cómo cambió tu percepción. La habitación donde estás no es solo una habitación: es una estación de paso. Las personas que conoces no son solo personas: son puertas a otros mundos. Tu vida no es solo una vida: es una expedición multidimensional en curso.</p>
        </blockquote>

"""
    + FIRMA + "\n"
    + puerta("arquitectura",
             "El peregrino no necesita público. Para el traje espiritual, el de quien colecciona estados para que lo vean, el Evangelio ofrece un cuarto con la puerta cerrada, y Chögyam Trungpa le puso nombre: materialismo espiritual. Ese disfraz se mira de cerca en <em>El Personaje</em>, Libro 9 de Arquitectura del Destino, Umbral V: «Pegada a la cara».",
             URL_ARQ + "libro-09-el-personaje/L09-U5.html")
    + "\n"
    + cierre(2, "La vuelta")
)

# ===========================================================================
# 5.3 · El Tejedor de Realidades (el título queda)
# ===========================================================================
NODO3_CUERPO = (
    meta(3, "Los hilos")
    + """        <h2>Creando Nuevos Mundos Entre Dimensiones</h2>

        <h3>El Telar Cósmico</h3>
        <p>No eres solo un viajero entre realidades ya hechas. Eres un tejedor que crea realidades nuevas en las intersecciones. Cada vez que combinas en tu experiencia elementos de mundos distintos, tejes algo que antes no existía. Tu vida no es un camino a través de la realidad: es un tapiz que estás tejiendo con hilos de muchos mundos.</p>
        <p>Los místicos lo dijeron siempre: la realidad no está terminada, esperando ser descubierta. Está en creación constante, y tú eres uno de sus artesanos. No un dios omnipotente, sino alguien que teje en el telar de la consciencia.</p>

        <h3>Los Hilos del Tejido</h3>
        <p>Cada mundo de tu experiencia ofrece hilos únicos:</p>
"""
    + lista([
        "<strong>El cuerpo:</strong> hilos de materia y forma",
        "<strong>La emoción:</strong> hilos de sentimiento y resonancia",
        "<strong>El pensamiento:</strong> hilos de idea y concepto",
        "<strong>La energía del día:</strong> hilos de vitalidad y cansancio",
        "<strong>El deseo:</strong> hilos de anhelo y visión",
        "<strong>El sentido:</strong> hilos de propósito y significado",
        "<strong>El vínculo:</strong> hilos de conexión y unidad",
    ])
    + """        <p>La teosofía los ordenó en planos, con nombres como etérico, astral o causal; en la vida diaria se reconocen por lo que hacen. Y estos son solo los hilos primarios. Hay infinitos hilos sutiles: de probabilidad, de sincronicidad, de potencial, de memoria, de futuro.</p>

        <h3>El Arte del Entrelazado</h3>
        <p><strong>Práctica Básica de Tejido</strong></p>
"""
    + pasos([
        "<strong>Elegir los hilos.</strong> Identifica qué quieres tejer: un proyecto, un cambio, un hábito nuevo. Pregúntate qué mundos necesita: un poco de cuerpo, de emoción, de pensamiento, de sentido. Elige el hilo más vivo de cada uno.",
        "<strong>Entrelazar.</strong> Cruza un hilo con otro en un gesto concreto: una idea con una acción, un deseo con una hora del día.",
        "<strong>Anudar.</strong> Fija el patrón con una decisión pequeña y reversible.",
        "<strong>Dejar reposar.</strong> Mira el tejido al día siguiente. Corrige sin desarmarlo todo.",
    ])
    + """
        <h3>Los Patrones Maestros</h3>
        <p><strong>La Espiral</strong></p>
        <p>Patrón de crecimiento que conserva su forma. Aparece en las conchas de los caracoles y en los brazos de muchas galaxias: es la espiral logarítmica, que se agranda sin cambiar de figura. No es la espiral dorada, como suele repetirse: el matemático Clement Falbo midió conchas de nautilus y encontró una proporción cercana a 1,33, lejos del 1,618 del número de oro; lo publicó en 2005.</p>
        <p>Jakob Bernoulli quedó tan prendado de esta espiral que la llamó maravillosa y pidió que la grabaran en su tumba con un lema: <em>Eadem mutata resurgo</em>, «aunque cambiada, resurjo la misma». El cantero se equivocó y talló otra, la de Arquímedes, que crece a paso parejo. Todavía puede verse en el claustro de la catedral de Basilea. Mira la espiral cuando necesites crecer sin perderte.</p>

        <p><strong>La Flor de la Vida</strong></p>
        <p>Patrón de comienzo: círculos iguales que se cruzan y abren pétalos. Es una de las figuras más antiguas de la geometría sagrada. Mírala para los proyectos semilla.</p>

        <p><strong>El Nudo Infinito</strong></p>
        <p>Patrón de continuidad, sin principio ni fin. Es uno de los ocho signos auspiciosos del budismo tibetano. Míralo para los compromisos que se cuidan en el tiempo.</p>

        <p><strong>La Red de Indra</strong></p>
        <p>Patrón de interconexión: cada punto refleja a todos los demás. Teje unidad en la diversidad. Mírala para el trabajo colectivo.</p>

        <h3>Tejiendo Sueños en Realidad</h3>
        <p>En junio de 1816, a orillas del lago de Ginebra, lord Byron propuso a sus huéspedes que cada uno escribiera una historia de fantasmas. Mary Godwin, que después firmaría Mary Shelley, tenía dieciocho años y pasó días sin encontrar la suya. Una madrugada, ya en la cama y sin poder dormir, vio con los ojos cerrados una escena tan nítida que la asustó: un estudiante arrodillado junto a la criatura que había armado. Así lo contó quince años después, en la introducción de 1831. Al día siguiente empezó a escribir <em>Frankenstein</em>.</p>
        <p><strong>Práctica: Del Sueño a la Obra</strong></p>
"""
    + pasos([
        "<strong>Captura el sueño</strong> apenas despiertas, antes de que se disuelva. Anota sus imágenes.",
        "<strong>Busca los hilos ancla.</strong> ¿Qué elementos pueden existir en lo físico? ¿Qué emociones son traducibles? ¿Qué visiones pueden volverse obra?",
        "<strong>Tiende puentes:</strong> de la imagen a la palabra, de la palabra al boceto, del boceto a un primer gesto.",
        "<strong>Dale cuerpo de a poco.</strong> Cada día, un hilo más denso. Mantén la esencia mientras gana forma. No fuerces: deja que llegue a su tiempo.",
    ])
    + """
        <h3>El Tejedor Como Artista Dimensional</h3>
        <p>No todos los tejidos necesitan propósito práctico. Algunos son arte puro: exploraciones de belleza, experimentos de posibilidad, juegos de creatividad cósmica.</p>
"""
    + lista([
        "<strong>Sinfonías emocionales:</strong> patrones de sentimiento puro",
        "<strong>Mandalas vivientes:</strong> geometrías que respiran y cambian",
        "<strong>Poemas dimensionales:</strong> palabras tejidas con realidades",
        "<strong>Esculturas del tiempo:</strong> formas que viven en muchos momentos",
    ])
    + """        <p>Tu vida misma es tu obra maestra: un tejido que nunca existió antes y nunca se repetirá.</p>

        <h3>Los Hilos Prohibidos</h3>
"""
    + lista([
        "Tejer la realidad de otros sin su permiso",
        "Tomar el tiempo ajeno como si fuera propio",
        "Vivir de la energía de otros sin dar nada a cambio",
        "Tramar patrones que se destruyen a sí mismos",
    ])
    + """        <p>El tejedor ético respeta la libertad de cada uno, la integridad de cada mundo y el equilibrio del conjunto.</p>

        <h3>Deshacer y Retejer</h3>
        <p><strong>Práctica del Deshilado Consciente</strong></p>
"""
    + pasos([
        "<strong>Honra el tejido existente.</strong> Sirvió a su propósito. Contiene energía valiosa. Merece gratitud, no destrucción.",
        "<strong>Deshila con cuidado.</strong> No desgarres. Guarda los hilos para volver a usarlos: algunos son compostables; otros, reciclables.",
        "<strong>Limpia los hilos recuperados.</strong> Suelta lo que ya no sirve y quédate con lo aprendido.",
        "<strong>Reteje con sabiduría.</strong> Los hilos con historia tienen fuerza y pueden crear patrones más sabios. El segundo tejido suele superar al primero.",
    ])
    + """
        <h3>El Tejedor de Milagros</h3>
        <p>Los milagros no son violaciones de las leyes naturales sino tejidos maestros que entrelazan mundos normalmente separados. Cuando tejes hilos de gracia con hilos de necesidad humana, cuando entrelazas el tiempo justo con el momento crítico, cuando unes lo posible con la circunstancia concreta, el milagro emerge del patrón. Agustín de Hipona lo dijo a comienzos del siglo V, en <em>La ciudad de Dios</em>: el portento no ocurre contra la naturaleza, sino contra lo que conocemos de ella.</p>

        <h3>La Firma del Tejedor</h3>
        <p>Cada tejedor tiene una firma única, un estilo reconocible:</p>
"""
    + lista([
        "Algunos tejen con hilos de luz y alegría",
        "Otros, con hondura y misterio",
        "Algunos crean patrones geométricos precisos",
        "Otros, flujos orgánicos salvajes",
    ])
    + """        <p>Descubre tu firma. No imites; innova. El cosmos necesita tu patrón único.</p>

        <h3>El Gremio de Tejedores</h3>
        <p>Hay muchos más tejedores de realidad de los que crees, aunque no tengan nombre ni reuniones. Se reconocen por la calidad de lo que tejen, la ética de su práctica, el respeto por el oficio y la dedicación a la belleza y a la verdad. Cuando encuentres a otro, intercambien técnicas, compartan hilos raros, colaboren en lo que nadie podría tejer solo.</p>

        <hr />

        <h2>Laboratorio del Tejedor</h2>

        <h3>Preparación del Telar</h3>
"""
    + lista([
        "Tu atención es el telar",
        "Ordena un poco el espacio y el día",
        "Elige un momento sin prisa",
        "Ten clara la intención",
    ])
    + """
        <h3>El Tejido</h3>
"""
    + pasos([
        "Toma un hilo de un mundo (por ejemplo, una imagen de un sueño).",
        "Entrelázalo con un hilo de otro (por ejemplo, una acción concreta).",
        "Añade hilos emocionales para dar cohesión.",
        "Usa hilos de pensamiento para dar estructura.",
        "Los hilos de sentido dan propósito al tejido.",
    ])
    + """
        <h3>El Anudado</h3>
"""
    + lista([
        "Los nudos son momentos de decisión",
        "Cada elección fija el patrón",
        "Los nudos grandes se hacen despacio y no a solas",
        "Los nudos pequeños permiten cambios futuros",
    ])
    + """
        <h3>Tejiendo Relaciones</h3>
        <p>Las relaciones son los tejidos más complejos, porque en el mismo tapiz trabajan varios tejedores. Cada persona trae sus propios hilos, y el arte está en crear un patrón coherente sin perder la individualidad de cada hebra.</p>
        <p><strong>1. El tejido de lo que se repite.</strong> Patrones que vuelven una y otra vez hasta ser comprendidos; Freud llamó compulsión a la repetición a esa tendencia a volver sobre lo que duele. Son densos y difíciles de deshacer, y piden consciencia, a veces compañía, para transformarse.</p>
        <p><strong>2. El tejido de lo que se comparte.</strong> Hilos de propósito común. Patrones que elevan a ambos tejedores. Ligeros pero increíblemente fuertes: se fortalecen con el uso.</p>
        <p><strong>3. El tejido de lo que se reconoce.</strong> Hilos de esencia. Patrones de reconocimiento profundo, que atraviesan el tiempo y la distancia. Resistentes y flexibles.</p>

        <h3>Tejiendo Nuevas Líneas Temporales</h3>
        <p>Cada momento ofrece muchos hilos. Tu elección de cuáles entrelazar inclina tu camino. No estás atrapado en una sola línea: vas tejiendo tu paso a través del tiempo.</p>
"""
    + pasos([
        "<strong>Mira tu trayectoria actual.</strong> Siente hacia dónde va si nada cambia.",
        "<strong>Imagina caminos posibles.</strong> Cada decisión importante ofrece hilos nuevos.",
        "<strong>Elige un hilo del camino deseado.</strong> No necesitas cambiarlo todo: un hilo pequeño puede desviar la trayectoria entera.",
        "<strong>Entrelaza gradualmente.</strong> Los cambios bruscos pueden desgarrar el tejido; integra lo nuevo con paciencia.",
        "<strong>Refuerza el patrón nuevo.</strong> Cada acción coherente lo fortalece; la repetición lo fija.",
    ])
    + """
        <h3>El Tejido Colectivo</h3>
        <p>La realidad compartida es un tejido donde incontables tejedores trabajan a la vez. Las culturas son patrones de tejido. Las revoluciones son momentos en que el patrón colectivo se reorganiza de golpe. Los renacimientos llegan cuando hilos nuevos quedan al alcance de todos.</p>
        <p>Tu tejido personal toca el tejido colectivo. Lo que tejes queda a la vista de otros como posibilidad.</p>

        <h3>Reparando Tejidos Dañados</h3>
        <p>Todo tejido vivido tiene desgarros: los golpes que dejaron marca, los hábitos que se enredan en bucles, los días que pierden color, los hilos sueltos de la ansiedad.</p>
"""
    + pasos([
        "<strong>Localiza el daño.</strong> ¿Qué hilos están rotos? ¿Qué patrones se torcieron?",
        "<strong>Reúne hilos de sanación:</strong> de amor y compasión, de la gente que te quiere, de lo que ya sanó en ti otras veces.",
        "<strong>Teje puentes sobre las roturas.</strong> No intentes borrar el daño: crea patrones que lo integren. El oro del kintsugi.",
        "<strong>Fortalece lo reparado.</strong> Los lugares reparados pueden ser los más fuertes, si se hace con consciencia y amor.",
    ])
    + """        <p class="nota">Las heridas hondas, las que al recordarlas se vuelven a vivir, no se visitan a solas: se recorren con un profesional.</p>

        <h3>Tejiendo con Otros Tejedores</h3>
        <p><strong>Práctica de Co-Creación</strong></p>
"""
    + pasos([
        "<strong>Sincronización de telares.</strong> Pongan en común sus intenciones. Respeten los hilos únicos de cada uno.",
        "<strong>Creación del patrón compartido.</strong> Imaginen juntos el tejido deseado. Cada uno aporta sus hilos más preciosos. Dejen que emerja un patrón nuevo, que ninguno podría crear solo.",
        "<strong>División del trabajo.</strong> Uno puede ser experto en hilos emocionales; otro, en la forma concreta. Distribuyan según sus fortalezas y confíen en la maestría del otro.",
        "<strong>El nudo compartido.</strong> El momento en que ambos se comprometen. Crea un tejido que los une pero no los ata, y deja crecer a cada uno dentro del patrón común.",
        "<strong>Mantenimiento.</strong> Revisen el patrón de tanto en tanto. Ajusten según lo que cada uno va siendo. Reparen cuando haya desgarros. Celebren la belleza creada entre los dos.",
    ])
    + """        <p>Khalil Gibran lo dijo en <em>El profeta</em>, en 1923, hablando del matrimonio: las columnas de un templo se sostienen separadas, y el roble y el ciprés no crecen uno a la sombra del otro.</p>

        <h3>La Tercera Transmutación Portal</h3>
        <p>El que viaja también teje. No solo habitas mundos: los tejes. Cada elección es una puntada. Cada relación, un patrón. Cada día, una sección nueva del tapiz de tu existencia.</p>
        <p>Eres co-creador de tu realidad, tejiendo el futuro con hilos del presente y la sabiduría del pasado.</p>

"""
    + siguiente(4, "deshilar con cuidado algo pequeño de tu día y volver a tejerlo de otra manera.",
                "Del tejido pasarás a la custodia: cuidar las puertas y acompañar a otros en sus pasos.")
    + """        <blockquote>
          <p>Al completar este nodo, mira el tejido de tu vida con otros ojos. Cada relación es un tapiz en proceso. Cada proyecto, un patrón que emerge. Cada desafío, una ocasión de tejer algo nuevo. No elegiste todos los hilos. Los que tienes en las manos, sí puedes tejerlos. ¿Qué vas a crear?</p>
        </blockquote>

"""
    + FIRMA + "\n"
    + puerta("portal",
             "Un patrón que ninguno podría tejer solo tiene su escenario: un grupo de Chicago que improvisaba obras de una hora sin director ni libreto, donde un personaje apareció entre todos y nadie sabe de quién fue. Se despliega en <em>La emergencia</em>, Libro 37 del Portal Público, Umbral IV: «En escena».",
             URL_PORTAL + "37_La_Emergencia/umbral-04.html")
    + "\n"
    + cierre(3, "Los hilos")
)

# ===========================================================================
# 5.4 · El Guardián de los Umbrales (el título queda)
# ===========================================================================
NODO4_CUERPO = (
    meta(4, "El límite")
    + """        <h2>Protegiendo y Guiando el Paso Entre Mundos</h2>

        <h3>La Responsabilidad Sagrada</h3>
        <p>Quien atraviesa puertas aprende también a cuidarlas. No todas deben quedar abiertas. No todo lo que llega tiene que pasar. Ser guardián es proteger los umbrales, acompañar a quien los cruza y cuidar el equilibrio entre lo que entra y lo que sale.</p>
        <p>El guardián no es un policía cósmico sino un servidor del equilibrio. Como un jardinero que sabe cuándo podar y cuándo dejar crecer, cuándo abrir la puerta del invernadero y cuándo proteger del frío. Tu función es cuidar la integridad de las puertas mientras acompañas la vida que pasa por ellas.</p>
        <p>Los romanos tenían un dios de las puertas, Jano, que dio su nombre a enero. Lo representaban con dos caras: una mira hacia afuera y otra hacia adentro. Las puertas de su templo se abrían en la guerra y se cerraban en la paz, y se cerraron tan pocas veces que el emperador Augusto se jactó de haberlas cerrado tres veces durante su gobierno, cuando antes de él solo se habían cerrado dos desde la fundación de Roma. Un buen guardián, como Jano, mira los dos lados a la vez.</p>

        <h3>Los Tipos de Umbrales</h3>
        <p><strong>Umbrales personales</strong></p>
"""
    + lista([
        "Las puertas de tu propia consciencia",
        "Los pasajes hacia lo que no sabes de ti",
        "Las entradas a tus memorias",
        "Los accesos a tus posibilidades",
    ])
    + """        <p><strong>Umbrales relacionales</strong></p>
"""
    + lista([
        "Los espacios entre tú y otros",
        "Los portales de la intimidad",
        "Las puertas del corazón",
        "Los puentes del alma",
    ])
    + """        <p><strong>Umbrales colectivos</strong></p>
"""
    + lista([
        "Los portales culturales y los arquetipos",
        "Las entradas a lo que una comunidad comparte",
        "Las puertas entre épocas",
        "Los umbrales de una civilización",
    ])
    + """        <p><strong>Umbrales sagrados</strong></p>
"""
    + lista([
        "Los que llevan a lo más hondo de ti",
        "Las entradas a lo sagrado de cada tradición",
        "Las puertas de iniciación",
        "Los umbrales del nacimiento y de la muerte",
    ])
    + """
        <h3>Las Herramientas del Guardián</h3>
        <p><strong>1. La Llave Maestra</strong><br />
        Tu atención es la llave que abre y cierra. No es un objeto sino una manera de estar. Cuando estás presente en un umbral, tienes voz sobre lo que pasa por él.</p>
        <p><strong>Práctica de la Llave:</strong></p>
"""
    + pasos([
        "Centra tu atención en el corazón.",
        "Llévala hasta el umbral que te ocupa: una conversación, un pedido, una noticia.",
        "Nota qué se siente ahí: apertura, cierre, duda.",
        "Pregúntate qué necesita este momento.",
        "Elige: abrir, esperar o cerrar.",
    ])
    + """        <p><strong>2. Los Cinco Límites</strong><br />
        Algunas puertas necesitan protección. No para excluir, sino para que cada cosa llegue a su tiempo.</p>
"""
    + lista([
        "<strong>El límite de tiempo:</strong> «ahora no»",
        "<strong>El de intención:</strong> «¿para qué?»",
        "<strong>El de consentimiento:</strong> «con tu permiso»",
        "<strong>El de cuidado:</strong> «esto me hace daño»",
        "<strong>El de preparación:</strong> «todavía no estoy listo»",
    ])
    + """        <p><strong>3. El Espejo del Umbral</strong><br />
        Cada puerta te muestra algo antes de cruzarla: tus miedos, para que los mires; tu luz, para que la reconozcas; tus sombras, para integrarlas; tus posibilidades, para inspirarte. Ese espejo no se ajusta para los demás: cada uno se mira en el suyo.</p>

        <h3>El Arte de Discernir</h3>
        <p>Antes de cruzar un umbral importante, conviene discernir.</p>
        <p><strong>Señales de que es el momento:</strong></p>
"""
    + lista([
        "Una calma estable",
        "Una intención clara",
        "La capacidad de seguir presente",
        "Experiencia en pasos más pequeños",
        "Humildad y respeto",
    ])
    + """        <p><strong>Señales de que conviene esperar:</strong></p>
"""
    + lista([
        "Agotamiento o confusión",
        "La necesidad de demostrar algo",
        "La tendencia a desconectarte de ti",
        "La arrogancia espiritual",
        "Buscar escapar en lugar de crecer",
    ])
    + """        <p>Este discernimiento no es juicio sino compasión: esperar también es un acto de amor, contigo y con otros.</p>

        <h3>Guardián de Tu Propio Templo</h3>
        <p>Antes de cuidar puertas ajenas, conviene conocer las propias:</p>
        <p><strong>Práctica del Templo Interior:</strong></p>
"""
    + pasos([
        "<strong>La puerta del cuerpo.</strong> ¿Qué dejas entrar? ¿Qué alimentos, qué sustancias, qué ambientes? Sé selectivo sin ser rígido.",
        "<strong>La puerta de la mente.</strong> ¿Qué pensamientos tienen acceso? ¿Qué información consumes? Filtra sin censurar.",
        "<strong>La puerta del corazón.</strong> ¿A quién das entrada profunda? ¿Qué emociones dejas residir? Protege sin cerrar.",
        "<strong>La puerta del alma.</strong> ¿Qué experiencias dejas que marquen tu esencia? ¿Qué enseñanzas integras? Sé permeable pero no poroso.",
    ])
    + """
        <h3>El Guardián Como Compañía</h3>
        <p>Hay umbrales en toda vida: un nacimiento, un diagnóstico, una despedida, un cambio de país. Tu función no es solo proteger: también es acompañar.</p>
        <p><strong>Práctica del Acompañamiento:</strong></p>
"""
    + pasos([
        "<strong>Antes del umbral.</strong> Escucha cómo está la otra persona. Pregunta qué necesita. No decidas por ella.",
        "<strong>En el umbral.</strong> No cruzas por ella, pero sostienes el espacio. Ofreces un ancla de calma. Estás.",
        "<strong>Al regreso.</strong> Ayudas a que se acomode. Escuchas lo vivido. Celebras lo que cambió.",
    ])
    + """        <p class="nota">Acompañar no es tratar: cuando el cruce es una crisis, el guardián sabe llamar a quien sabe.</p>

        <h3>Guardianes de Portales Colectivos</h3>
        <p>Algunos guardianes custodian puertas que tocan a muchos:</p>
        <p><strong>Umbrales generacionales</strong></p>
"""
    + lista([
        "Los cambios de época",
        "Los momentos en que una sociedad elige",
        "Piden muchos guardianes",
        "Y una coordinación paciente",
    ])
    + """        <p><strong>La memoria familiar</strong></p>
"""
    + lista([
        "Lo que una familia calla o repite durante generaciones",
        "La ocasión de nombrarlo",
        "Pide fortaleza y compasión",
        "Y, cuando duele mucho, compañía profesional",
    ])
    + """
        <h3>Los Peligros del Guardián</h3>
        <p><strong>1. La inflación del guardián</strong></p>
"""
    + lista([
        "Creerse dueño y no servidor",
        "Usar el poder para controlar",
        "Olvidar la humildad",
        "<em>Solución:</em> recordar que eres guardián de paso",
    ])
    + """        <p><strong>2. La fatiga del guardián</strong></p>
"""
    + lista([
        "Desgaste por sostener muchas puertas a la vez",
        "Pérdida de energía vital",
        "Confusión",
        "<em>Solución:</em> turnarse y descansar",
    ])
    + """        <p>En 1995, el psicólogo Charles Figley la llamó fatiga por compasión: el cansancio de quienes cargan durante años con el dolor de otros.</p>
        <p><strong>3. El dolor que se pega</strong></p>
"""
    + lista([
        "Absorber el dolor que pasa por la puerta",
        "Perder la propia mirada",
        "Confundirse con lo que se acompaña",
        "<em>Solución:</em> cuidado regular, supervisión y una distancia sana",
    ])
    + """        <p>Lisa McCann y Laurie Anne Pearlman lo describieron en 1990 en quienes atienden a personas traumatizadas, y lo llamaron trauma vicario.</p>
        <p><strong>4. El guardián que no deja pasar</strong></p>
        <p>Hay guardianes que olvidan para qué existe la puerta. En «Ante la ley», un relato que Franz Kafka publicó en 1915, un hombre del campo pasa la vida entera esperando que el guardián lo deje entrar. Al final, cuando ya se muere, el guardián le dice que esa entrada estaba destinada solo a él, y la cierra. A veces el guardián más severo vive adentro: el miedo que nunca da permiso. <em>Solución:</em> recordar que la puerta existe para pasar.</p>

        <h3>El Código del Guardián</h3>
        <p><strong>Principios sagrados:</strong></p>
"""
    + pasos([
        "<strong>Servicio sobre poder.</strong> La puerta no te pertenece. Sirves al bien mayor. Tu poder es prestado.",
        "<strong>Discernimiento sin juicio.</strong> Miras la preparación, no el valor. Cada uno cambia a su ritmo. La compasión guía tu decisión.",
        "<strong>Protección con amor.</strong> Proteges por amor, no por miedo. Los límites son actos de cuidado. La firmeza puede ser gentil.",
        "<strong>Aprendizaje continuo.</strong> El guardián también cambia. Aprendes de cada viajero. Las puertas te enseñan.",
    ])
    + """
        <h3>Cerrando Portales Peligrosos</h3>
        <p>A veces hay puertas que conviene cerrar: un hábito que daña, un vínculo que hiere, una costumbre que ya no sirve.</p>
        <p><strong>Práctica del Cierre:</strong></p>
"""
    + pasos([
        "<strong>Mira la puerta.</strong> ¿Por qué está abierta? ¿Qué función cumplía? ¿Qué daño hace?",
        "<strong>Prepárate.</strong> Reúne fuerzas. Pide ayuda si hace falta. Cuídate.",
        "<strong>Cierra.</strong> No con violencia sino con firmeza. Con amor, no con miedo. Agradeciendo lo que sirvió.",
        "<strong>Después.</strong> Algunas puertas intentan reabrirse. Mantente atento. Refuerza si hace falta.",
    ])
    + """        <p class="nota">Cuando alguien te daña una y otra vez, lo sabio no es aguantar en el umbral sino alejarse y pedir ayuda.</p>

        <h3>La Red de Guardianes</h3>
        <p>No estás solo. Hay una red de guardianes que casi nunca se nombra:</p>
"""
    + lista([
        "Quienes cuidan el sueño de un niño",
        "Las parteras que reciben a los que llegan",
        "Quienes acompañan a los que se van",
        "Los maestros que sostienen a un alumno en su cambio",
        "Quienes cuidan la tierra",
    ])
    + """        <p>Cuando necesites ayuda, pídela. Cuando otro guardián necesite apoyo, responde.</p>

        <h3>El Guardián del Amor</h3>
        <p>La puerta más poderosa y más delicada es la del amor. Como guardián del amor:</p>
"""
    + lista([
        "Proteges la vulnerabilidad sagrada",
        "Facilitas la apertura segura",
        "Previenes las invasiones emocionales",
        "Cuidas la intimidad consciente",
        "Honras el misterio del encuentro",
    ])
    + """        <p>El amor mal guardado puede destruir. Bien guardado, transforma mundos.</p>

        <h3>La Cuarta Transmutación Portal</h3>
        <p>El que viaja y teje también custodia. Ahora conoces el ecosistema de las puertas: cómo se reconocen, cómo se recorren, cómo se cuidan.</p>
        <p>Tu responsabilidad creció, y también tu capacidad. No guardas por poder sino por amor. No limitas por miedo sino por sabiduría. Eres servidor de la vida que pasa.</p>

"""
    + siguiente(5, "decir esta semana un «ahora no» con calma, y un «sí» que te cueste.",
                "De la custodia pasarás a los puentes: unir lo que parecía separado.")
    + """        <blockquote>
          <p>Al cerrar este nodo, siente el peso sagrado de tu responsabilidad y el honor de tu servicio. Cada puerta que cuidas, cada persona que acompañas, cada umbral que bendices es un acto de amor. No eres carcelero sino guardián de la libertad. Los umbrales te confían lo que pasa por ellos.</p>
        </blockquote>

"""
    + FIRMA + "\n"
    + puerta("arquitectura",
             "El guardián que cuida muchas puertas a la vez se gasta. Entre la empatía que agota y la compasión que sostiene hay una diferencia que se midió, y una tradición antigua le puso un límite a la generosidad para que quien da no terminara cayendo. Se despliega en <em>La Obra</em>, Libro 12 de Arquitectura del Destino, Umbral VI: «Arder sin consumirse».",
             URL_ARQ + "libro-12-la-obra/L12-U6.html")
    + "\n"
    + cierre(4, "El límite")
)

# ===========================================================================
# 5.5 · El Arquitecto de Puentes (el título queda)
# ===========================================================================
NODO5_CUERPO = (
    meta(5, "El encuentro")
    + """        <h2>Construyendo Conexiones Entre Dimensiones Distantes</h2>

        <h3>La Ingeniería de lo Imposible</h3>
        <p>Hay mundos que nunca se han tocado. Realidades tan distantes que parecen incompatibles. Vidas que transcurren tan lejos unas de otras que ni siquiera saben que las demás existen. Como arquitecto de puentes, tu función es crear conexiones donde nunca las hubo, unir lo que parecía separado para siempre, tender caminos entre imposibles.</p>
        <p>No construyes con materia sino con consciencia. No usas herramientas físicas sino atención e intención. Tus puentes no son estructuras sino maneras de escuchar que permiten que dos mundos se hablen.</p>

        <h3>La Física de los Puentes Dimensionales</h3>
        <p>Un puente no es una línea recta entre dos puntos. Es una curva que permite que dos realidades se toquen sin que una se trague a la otra. Como un arcoíris que une cielo y tierra sin que ninguno pierda su naturaleza.</p>
        <p><strong>Componentes de un puente:</strong></p>
        <p><strong>1. Los pilares</strong></p>
"""
    + lista([
        "Puntos de apoyo firmes en cada orilla",
        "Hablan el idioma de su lado",
        "Pero conservan la capacidad de traducir",
        "Como embajadas entre mundos",
    ])
    + """        <p><strong>2. El arco</strong></p>
"""
    + lista([
        "El espacio donde las diferencias se armonizan",
        "No fuerza la compatibilidad: la facilita",
        "Permite comunicarse sin distorsión",
        "Respeta la integridad de ambos lados",
    ])
    + """        <p><strong>3. Los cables</strong></p>
"""
    + lista([
        "Hilos de atención que sostienen la conexión",
        "Vibran entre los dos lados",
        "Llevan información y afecto",
        "Se ajustan sobre la marcha",
    ])
    + """        <p><strong>4. El centro</strong></p>
"""
    + lista([
        "El punto medio donde ocurre la alquimia",
        "Ni un mundo ni el otro",
        "Un tercer espacio de posibilidad: lo que aparece entre dos y que ninguno traía",
        "Donde nacen realidades nuevas",
    ])
    + """
        <h3>Mundos que Conviene Unir</h3>
        <p>No todos los mundos deben conectarse. Algunas separaciones cumplen su función. Como arquitecto, debes discernir.</p>
        <p><strong>Conexiones necesarias:</strong></p>
"""
    + lista([
        "Mundos complementarios que se enriquecen mutuamente",
        "Realidades que se separaron sin necesidad",
        "Encuentros que hacen crecer a ambos",
        "Espacios que anhelan reconectarse",
    ])
    + """        <p><strong>Conexiones peligrosas:</strong></p>
"""
    + lista([
        "Mundos que se dañarían al tocarse",
        "Realidades que se anularían mutuamente",
        "Encuentros para los que nadie está preparado",
        "Espacios que necesitan crecer primero por su cuenta",
    ])
    + """        <p><strong>Práctica antes de construir:</strong></p>
"""
    + pasos([
        "<strong>Mira los dos lados.</strong> Estudia ambos mundos a fondo: sus reglas, su historia, lo que buscan. Identifica compatibilidades y conflictos.",
        "<strong>Ensaya.</strong> En tu imaginación, modela el encuentro. Observa las reacciones posibles. Anticipa consecuencias.",
        "<strong>Pregunta.</strong> Cuando de cada lado hay personas, se les pregunta a ellas. Respeta cualquier resistencia.",
    ])
    + """
        <h3>Construyendo Tu Primer Puente</h3>
        <p><strong>El puente entre corazón y mente</strong> es el fundamental, el que todo arquitecto aprende primero:</p>
"""
    + pasos([
        "<strong>Establece los pilares.</strong> En el corazón, el amor. En la mente, la claridad. Siente ambos como reales y válidos.",
        "<strong>Tiende el arco.</strong> Imagina un arcoíris de luz entre los dos. Es una imagen, y funciona. Siente que algo empieza a pasar.",
        "<strong>Afina la resonancia.</strong> Deja que el corazón informe a la mente y que la mente ordene al corazón, sin que ninguno domine.",
        "<strong>Estabiliza.</strong> Practica decisiones que honren a los dos, hasta que el puente se vuelva costumbre.",
    ])
    + """
        <h3>Puentes Entre Personas</h3>
        <p>Los puentes más hermosos y desafiantes son los que unen a una consciencia humana con otra.</p>
        <p><strong>Práctica del Puente Interpersonal:</strong></p>
"""
    + pasos([
        "<strong>Consentimiento.</strong> Nunca construyas sin permiso. El permiso se pide en voz alta, no se imagina, y se respeta la respuesta.",
        "<strong>La nota común.</strong> Cada persona tiene su propio tono. Encuentra la nota que ambos pueden cantar.",
        "<strong>Construcción compartida.</strong> Los mejores puentes se construyen juntos. Cada uno aporta sus materiales. Co-creación, no imposición.",
        "<strong>Mantenimiento.</strong> Los puentes necesitan cuidado: aclarar malentendidos, reforzar con experiencias compartidas.",
    ])
    + """        <p>John Gottman observó durante décadas a parejas en su laboratorio. Con Nan Silver escribió en 1999 que el éxito o el fracaso de los intentos de reparación —un «empecemos de nuevo», un «necesito calmarme», una broma a tiempo— es uno de los factores principales para que una pareja florezca o se marchite. Los puentes que duran no son los que nunca se dañan, sino los que se reparan pronto.</p>

        <h3>Puentes Temporales</h3>
        <p>Unir tiempos distintos es arquitectura avanzada:</p>
        <p><strong>El puente entre el que eres y el que serás:</strong></p>
"""
    + lista([
        "Imagina a tu yo de dentro de diez años",
        "Pregúntale qué haría hoy",
        "Deja que su mirada informe tus decisiones",
    ])
    + """        <p><strong>El puente entre generaciones:</strong></p>
"""
    + lista([
        "Une la sabiduría de quienes vinieron antes con lo que viene",
        "Une tradición y renovación",
        "Nombra lo heredado para elegir qué seguir llevando",
    ])
    + """
        <h3>Puentes Colectivos</h3>
        <p>Algunos puentes sirven a muchos:</p>
        <p><strong>El puente entre culturas:</strong></p>
"""
    + lista([
        "Entre maneras de ver el mundo que parecen incompatibles",
        "Encuentra la humanidad compartida",
        "Crea espacios de encuentro genuino",
    ])
    + """        <p><strong>El puente entre ciencia y espíritu:</strong></p>
"""
    + lista([
        "Uno de los más necesarios de nuestra época",
        "No rebaja a ninguno: eleva a los dos",
        "Muestra que son aspectos de la misma búsqueda",
    ])
    + """        <p><strong>El puente entre la humanidad y la naturaleza:</strong></p>
"""
    + lista([
        "Reconecta a la humanidad con la Tierra",
        "Recuerda que no estamos EN la naturaleza",
        "Somos naturaleza consciente de sí misma",
    ])
    + """
        <h3>Los Materiales del Arquitecto</h3>
        <p><strong>Luz coherente:</strong> el material más versátil; se adapta a cualquier tono; fuerte pero flexible.</p>
        <p><strong>Amor incondicional:</strong> el adhesivo universal; une sin forzar; paciente con cualquier resistencia.</p>
        <p><strong>Intención clara:</strong> da forma y dirección; define el propósito del puente; sostiene su integridad.</p>
        <p><strong>La forma justa:</strong> proporciones que resuenan; estructuras que se sostienen solas; una belleza que ayuda a durar.</p>

        <h3>Puentes Rotos y Su Reparación</h3>
        <p>Encontrarás puentes antiguos rotos por heridas, por guerras, por olvido.</p>
        <p><strong>Práctica de la Restauración:</strong></p>
"""
    + pasos([
        "<strong>Arqueología.</strong> Investiga qué unía el puente, por qué se rompió, qué quedó sin resolver.",
        "<strong>Limpieza de escombros.</strong> Lo que quedó atascado, los resentimientos cristalizados, las memorias de dolor.",
        "<strong>Reconstrucción que honra la historia.</strong> No borres el pasado. Integra lo aprendido. Construye más fuerte.",
        "<strong>Reapertura.</strong> Un gesto simple: una llamada, una carta, un café. Honra lo perdido y celebra la reconexión.",
    ])
    + """        <p class="nota">No todo puente roto debe reconstruirse: si del otro lado alguien sigue dañando, primero se cuida la propia orilla.</p>

        <h3>El Puente Arcoíris Personal</h3>
        <p>Las escuelas modernas del yoga dan a cada uno de los siete centros un color, del rojo de la raíz al violeta de la coronilla, y los imaginan como un arcoíris entre la tierra y el cielo:</p>
"""
    + pasos([
        "<strong>Rojo:</strong> ancla en la tierra, la supervivencia, la tribu",
        "<strong>Naranja:</strong> fluye en la creatividad y la sexualidad",
        "<strong>Amarillo:</strong> poder personal y voluntad",
        "<strong>Verde:</strong> amor que trasciende condiciones",
        "<strong>Azul:</strong> expresión de la verdad",
        "<strong>Índigo:</strong> visión más allá del velo",
        "<strong>Violeta:</strong> corona de conexión cósmica",
    ])
    + """        <p>Cuando este puente está completo, eres un arcoíris viviente, uniendo cielo y tierra en tu ser.</p>

        <h3>Los Puentes Prohibidos</h3>
        <p>Hay conexiones que no conviene hacer:</p>
"""
    + lista([
        "Puentes que violan la libertad de otro",
        "Conexiones que dañarían a uno de los lados",
        "Enlaces que permitirían que uno viva a costa del otro",
        "Puentes prematuros, que impedirían que cada lado madure",
    ])
    + """        <p>Los nórdicos imaginaron un puente así entre el mundo de los hombres y el de los dioses: Bifröst, el arcoíris. Snorri Sturluson lo describió en el siglo XIII: el rojo que se ve en el arco es fuego que arde para que no suban los gigantes. Lo custodiaba Heimdal, que dormía menos que un pájaro y oía crecer la hierba. Ni el puente más hermoso está abierto a cualquiera. Y Snorri cuenta también que al final de los tiempos ese puente se romperá: nada en este mundo está asegurado. El arquitecto construye igual, y con humildad.</p>
        <p>La sabiduría del arquitecto está tanto en lo que no construye como en lo que construye.</p>

        <h3>La Red de Puentes</h3>
        <p>Tus puentes no existen aislados. Forman parte de una red de conexiones:</p>
"""
    + lista([
        "Cada puente nuevo toca a los que ya existen",
        "Juntos crean rutas entre muchos mundos",
        "La red tiende a ordenarse hacia una coherencia mayor",
        "Tu trabajo es parte de una gran reconexión",
    ])
    + """
        <h3>El Puente Último</h3>
        <p>El puente más importante que construirás es el que une la separación y la unidad, para vivir ambas a la vez. No destruye la individualidad ni fuerza la fusión. Permite la paradoja de ser uno y muchos.</p>
        <p>Este es el puente que la humanidad está construyendo entre todos: el reconocimiento de la unidad en la diversidad, la experiencia de ser notas distintas en la misma sinfonía.</p>

        <h3>La Quinta Transmutación Portal</h3>
        <p>El que custodia también construye. No solo proteges lo que existe: abres posibilidades nuevas. Cada puente que tiendes es una declaración de esperanza, una afirmación de que la separación no es final y de que la conexión siempre es posible.</p>
        <p>Eres ingeniero de reconciliación, arquitecto de encuentros, constructor de futuros donde lo imposible se vuelve cercano.</p>

"""
    + siguiente(6, "hacer un intento de reparación pequeño con alguien —una palabra, una llamada, un «empecemos de nuevo»— y notar qué pasa por el puente.",
                "De los puentes pasarás al vacío: el espacio desde donde nace lo nuevo.")
    + """        <blockquote>
          <p>Al cerrar este nodo, siente en tu corazón todos los puentes que el mundo necesita. Entre culturas, religiones, especies, mundos. Tu trabajo apenas comienza. Cada puente que construyes hace más fácil el próximo. Eres parte de la gran reconexión, el tejido que va reuniendo lo que fue separado. Construye con amor, construye con sabiduría, construye con la certeza de que cada conexión importa.</p>
        </blockquote>

"""
    + FIRMA + "\n"
    + cierre(5, "El encuentro")
)

# ===========================================================================
# 5.6 · El Alquimista del Vacío (el título queda)
# ===========================================================================
NODO6_CUERPO = (
    meta(6, "El hueco fértil")
    + """        <h2>Transformando la Nada en Todo</h2>

        <h3>El Material Primordial</h3>
        <p>Antes de la luz, antes del sonido, antes del pensamiento, está el Vacío. No es ausencia sino potencial puro. No es nada sino el todo antes de manifestarse. Como alquimista del vacío, trabajas con el material más hondo del cosmos: el espacio fecundo donde todas las posibilidades esperan nacer.</p>
        <p>El vacío no está vacío. La física lo sabe: aun donde no hay nada, hay fluctuaciones, y dos placas de metal muy cercanas, en ese vacío, se atraen. Hendrik Casimir lo predijo en 1948 y Steve Lamoreaux lo midió en 1997. Pero eso es solo la superficie de la imagen. El Vacío verdadero es la consciencia en estado puro, antes de tomar cualquier forma.</p>

        <h3>La Paradoja del Vacío Lleno</h3>
        <p>El Vacío lo contiene todo precisamente porque no contiene nada. Como una página en blanco que puede recibir cualquier historia, como el silencio que hace posible toda música, como el espacio que permite todo movimiento. Tu trabajo como alquimista no es llenar el vacío sino revelar lo que ya contiene en potencia.</p>
        <p><strong>Los estratos del vacío:</strong></p>
        <p><strong>1. El vacío cotidiano</strong></p>
"""
    + lista([
        "El espacio entre los objetos",
        "Los silencios entre las palabras",
        "Las pausas entre respiraciones",
        "Al alcance de cualquiera",
    ])
    + """        <p><strong>2. El vacío de la física</strong></p>
"""
    + lista([
        "El espacio entre las partículas",
        "Las fluctuaciones que nunca se detienen",
        "El campo de lo posible",
        "Una imagen para lo que todavía no tomó forma",
    ])
    + """        <p><strong>3. El vacío consciente</strong></p>
"""
    + lista([
        "El espacio entre pensamientos",
        "El darse cuenta antes de identificarse con algo",
        "El testigo sin objeto",
        "Puerta a la transformación",
    ])
    + """        <p><strong>4. El vacío primordial</strong></p>
"""
    + lista([
        "Anterior a todo lo que existe",
        "La matriz de toda creación",
        "El útero del cosmos",
        "Lo que las tradiciones llaman origen",
    ])
    + """
        <h3>El Laboratorio del Vacío</h3>
        <p>Tu laboratorio no tiene paredes ni instrumentos. Es el espacio de tu consciencia cuando dejas de llenarlo. No se construye de golpe: se aprende de a poco, empezando por las pausas.</p>
        <p><strong>Práctica del Laboratorio:</strong></p>
"""
    + pasos([
        "<strong>Vaciamiento progresivo.</strong> Empieza por el vacío más simple: la pausa al final de cada exhalación. Después, el silencio entre dos sonidos. Después, el hueco entre dos pensamientos. No sueltes nada a la fuerza: deja que se aquiete.",
        "<strong>Estabilidad en el vacío.</strong> No es pérdida de consciencia: es consciencia sin objeto. Permanece alerta y en calma, como quien flota en un agua que sostiene.",
        "<strong>El campo alquímico.</strong> El vacío se vuelve receptivo. Responde a la intención suave, no a la voluntad forzada. Como esculpir humo con la respiración.",
    ])
    + """        <p class="nota">Si soltar trae extrañeza, como si miraras tu vida detrás de un vidrio, abre los ojos, apoya los pies y mira algo cercano: ese no es el vacío que buscas, y si se repite, se consulta.</p>

        <h3>La Primera Transmutación: Vacío en Luz</h3>
        <p>La luz no se fabrica: se libera. Cada fotón es vacío que danzó hasta manifestarse.</p>
        <p><strong>Práctica del Primer Impulso:</strong></p>
"""
    + pasos([
        "Entra en el silencio.",
        "Deja que aparezca un movimiento mínimo —una imagen, una palabra, unas ganas—, sin esfuerzo, como una brisa sobre agua quieta.",
        "Permite que crezca a su ritmo.",
        "Observa la luz emerger: no la creas, la permites. El vacío da a luz con naturalidad.",
        "Acompaña sin controlar: eres partero, no creador.",
    ])
    + """
        <h3>Alquimia Emocional del Vacío</h3>
        <p>Las emociones más hondas nacen del vacío, no del estímulo:</p>
        <p><strong>El amor del vacío:</strong> no amor hacia algo, sino amor como estado; anterior al sujeto y al objeto; amor que no necesita razón.</p>
        <p><strong>La paz del vacío:</strong> no ausencia de conflicto, sino una paz que contiene todas las guerras sin activarlas; quietud dinámica; calma que danza.</p>
        <p><strong>El gozo del vacío:</strong> no felicidad por algo, sino el éxtasis de la potencialidad pura; celebración sin motivo; la risa del cosmos consigo mismo.</p>
        <p><strong>Práctica de la Alquimia Emocional:</strong></p>
"""
    + pasos([
        "Entra en el vacío emocional: no entumecimiento sino apertura.",
        "Deja que una cualidad emerja sin forzarla.",
        "No te aferres cuando aparezca.",
        "Déjala fluir a través de ti hacia el mundo.",
        "Vuelve al vacío para la próxima.",
    ])
    + """
        <h3>Creación desde el Vacío</h3>
        <p>Todo acto de creación genuina pasa por el vacío. Los alquimistas dividían la obra en cuatro colores: negro, blanco, amarillo y rojo. Carl Jung, que dedicó años a sus textos, cuenta en <em>Psicología y alquimia</em> (1944) que hacia los siglos XV o XVI los colores quedaron en tres y el amarillo cayó en desuso. Para él, el blanco es el alba, pero el sol sale recién con el rojo.</p>
"""
    + pasos([
        "<strong>Nigredo (ennegrecimiento).</strong> Entrar en el vacío creativo. El terror de la página en blanco. La muerte de las ideas preconcebidas. La rendición a la nada.",
        "<strong>Albedo (blanqueamiento).</strong> El vacío empieza a brillar. Los posibles se revelan. La intención se purifica. Aparece la claridad.",
        "<strong>Citrinitas (amarilleo).</strong> La primera manifestación. Las ideas toman forma. La energía se densifica. La luz se vuelve calor.",
        "<strong>Rubedo (enrojecimiento).</strong> La obra completa, pero aún unida al vacío. Obra viva, no muerta. Lista para volver al origen.",
    ])
    + """
        <h3>El Dolor y el Agua</h3>
        <p>Hay una manera de sostener el dolor que no consiste en arrancarlo. El Buda la dijo con una imagen: un puñado de sal en una taza de agua la vuelve imbebible; el mismo puñado arrojado al Ganges apenas se nota. En ese sutta habla del peso que tiene una falta pequeña en una mente estrecha o en un corazón amplio; la imagen sirve igual para el dolor. No se trata de achicar la sal, sino de agrandar el agua.</p>
        <p><strong>Práctica del Agua Grande:</strong></p>
"""
    + pasos([
        "Elige un malestar pequeño de hoy: una preocupación, una irritación.",
        "Siéntelo un momento, sin pelear con él.",
        "Ensancha la atención: el cuerpo entero, el cuarto, el cielo afuera, los sonidos lejanos.",
        "Nota el malestar dentro de ese espacio grande. No lo empujes: déjalo estar en el agua.",
        "Permanece en el vacío sin llenarlo enseguida.",
        "Deja que algo nuevo aparezca, sin dirigirlo.",
    ])
    + """        <p class="nota">Las heridas hondas, las que al recordarlas se vuelven a vivir, no se visitan a solas: se recorren con un profesional.</p>

        <h3>El Vacío Como Portal Supremo</h3>
        <p>El vacío es el portal que une todas las dimensiones porque existe en todas ellas. Es el denominador común del cosmos, el lienzo sobre el cual toda realidad se pinta.</p>
        <p>Por eso el silencio sirve de pasaje: entre el trabajo y la casa, entre una conversación y otra, un minuto de vacío te deja llegar entero a lo que sigue.</p>

        <h3>Los Peligros del Vacío</h3>
        <p><strong>1. El nihilismo espiritual</strong></p>
"""
    + lista([
        "Confundir el vacío con el sinsentido",
        "Perderse en la nada sin volver",
        "Rechazar la creación como ilusión",
        "<em>Solución:</em> recordar que el vacío es plenitud",
    ])
    + """        <p><strong>2. El apego al vacío</strong></p>
"""
    + lista([
        "Preferir el vacío a la manifestación",
        "Un escapismo espiritual refinado",
        "Miedo a la forma",
        "<em>Solución:</em> danzar entre el vacío y la forma",
    ])
    + """        <p><strong>3. El vacío falso</strong></p>
"""
    + lista([
        "Disociación disfrazada de trascendencia",
        "Entumecimiento confundido con paz",
        "Evitación llamada desapego",
        "<em>Solución:</em> el vacío genuino lo incluye todo",
    ])
    + """
        <h3>El Vacío Creativo Colectivo</h3>
        <p>Hay un vacío compartido del que toda la humanidad puede beber:</p>
"""
    + lista([
        "El campo de la innovación, donde nacen las ideas que cambian una época",
        "El pozo de la compasión, fuente que no se agota",
        "La matriz de lo posible, donde se gestan los futuros",
        "El océano de la paz, disponible para todos",
    ])
    + """        <p>Cada vez que callas a tiempo, haces un poco de lugar para otros.</p>

        <h3>Para Habitar el Vacío</h3>
        <p><strong>Práctica de la Pregunta Sostenida:</strong></p>
"""
    + pasos([
        "Formula una pregunta con claridad.",
        "Entra en el silencio.",
        "Sostén la pregunta sin buscar la respuesta.",
        "Suéltala y vuelve a tu día.",
        "Atiende lo que llega en los días siguientes: a veces una respuesta; a veces, una pregunta mejor.",
    ])
    + """
        <h3>El Vacío Luminoso</h3>
        <p>En varias tradiciones contemplativas —la tibetana lo llama luz clara— el vacío más hondo no es oscuro: brilla. No necesita manifestarse como luz; el vacío mismo resplandece. Es la consciencia pura reconociéndose.</p>
        <p>En ese estado:</p>
"""
    + lista([
        "El vacío y la plenitud son uno",
        "La nada y el todo coexisten",
        "Lo posible y lo real se unen",
        "Eres el vacío consciente de sí mismo",
    ])
    + """
        <h3>Los Guardianes del Vacío</h3>
        <p>Las tradiciones hablan de presencias que custodian el acceso al vacío primordial. No son entidades separadas sino aspectos del vacío mismo, que hacen sus preguntas:</p>
"""
    + lista([
        "¿Puedes sostener la paradoja de la nada llena?",
        "¿Tienes la humildad de no-ser?",
        "¿Posees la fuerza de no forzar?",
        "¿Entiendes que no creces, sino que permites?",
    ])
    + """
        <h3>La Sexta Transmutación Portal</h3>
        <p>El que tiende puentes descubre de dónde salen: del vacío. No necesitas más herramientas, porque el vacío es la herramienta primordial. No necesitas poder, porque el vacío contiene todo poder en potencia.</p>
        <p>Eres alquimista del origen, transformador de la fuente, partero del misterio más hondo: cómo la nada se vuelve todo y el todo vuelve a la nada en el eterno respiro del cosmos.</p>

"""
    + siguiente(7, "quedarte un minuto al día en una pausa, sin llenarla.",
                "Del vacío pasarás a la vida entera: ser la puerta sin pensar en ello.")
    + """        <blockquote>
          <p>Al cerrar este nodo, permanece un momento más en el vacío. No hay prisa por llenarlo. En este espacio entre palabras, entre respiraciones, entre pensamientos, está todo lo que buscas. Y lo más simple es lo más hondo: el vacío no es destino sino origen. No es muerte sino útero. No es final sino el eterno comienzo.</p>
        </blockquote>

"""
    + FIRMA + "\n"
    + cierre(6, "El hueco fértil")
)

# ===========================================================================
# 5.7 · El Portal Viviente (el título queda)
# ===========================================================================
NODO7_CUERPO = (
    meta(7, "La puerta que eres")
    + """        <h2>Siendo la Puerta Consciente Entre Todos los Mundos</h2>

        <h3>La Revelación Final</h3>
        <p>Ya no usas portales. Ya no creas portales. Ya no viajas a través de portales. Eres el portal: no como un lugar al que se llega, sino como algo que ya está ocurriendo. Tu consciencia es la apertura a través de la cual el infinito se experimenta a sí mismo. Tu cuerpo es la puerta física entre el mundo y tu vida. Tu vida es el umbral donde todos los mundos se encuentran.</p>
        <p>Esta no es inflación espiritual sino reconocimiento humilde de tu función. Como un ojo no se enorgullece de ver sino que simplemente ve, tú no te engrandeces por ser portal: simplemente permites el paso. Eres el espacio consciente donde ocurre el milagro del tránsito.</p>

        <h3>La Anatomía del Portal Viviente</h3>
        <p>Tu cuerpo ya está hecho de umbrales; no hace falta reorganizarlo para que lo sea.</p>
        <p><strong>El sistema nervioso: la red de pasajes</strong></p>
"""
    + lista([
        "Cada neurona espera su umbral para disparar",
        "Cada sinapsis es una hendidura donde la señal cambia de idioma",
        "El cerebro es la estación central",
        "La médula espinal, el corredor principal",
        "Los nervios, los caminos que llegan a cada rincón",
    ])
    + """        <p><strong>La circulación: los ríos</strong></p>
"""
    + lista([
        "La sangre lleva a cada célula lo que necesita y se lleva lo que sobra",
        "El corazón late desde antes de que nacieras",
        "Las arterias y las venas son caminos de ida y vuelta",
    ])
    + """        <p><strong>Las membranas: los guardianes</strong></p>
"""
    + lista([
        "Cada célula vive de una membrana que elige qué entra y qué sale",
        "La piel es la frontera más grande del cuerpo",
        "El timo es la escuela donde las defensas aprenden a distinguir lo propio de lo ajeno",
    ])
    + """        <p>Durante siglos, el timo fue un órgano en busca de función: hasta 1961 se creía que no tenía ningún papel en la inmunidad. Ese año, Jacques Miller mostró que sin él las defensas no aprenden. Permeable sin ser poroso: el cuerpo ya lo sabía.</p>
        <p><strong>La arquitectura sutil</strong></p>
        <p>Las tradiciones del yoga y de la medicina china describen además los chakras y los meridianos: son mapas de la experiencia, no de la anatomía, y como tales pueden orientar.</p>

        <h3>El Funcionamiento Automático</h3>
        <p>Como portal viviente, muchas cosas ocurren sin que intervengas:</p>
        <p><strong>Traducción constante:</strong> tus sentidos traducen a cada instante la luz en imagen y el aire en sonido; conviertes lo que llega en algo que puedes vivir; armonizas lo que choca; sin esfuerzo consciente.</p>
        <p><strong>Filtrado y protección:</strong> tu atención filtra lo que pasa; tus defensas protegen lo vulnerable; tu cuerpo cuida sus fronteras, como un sistema inmune de la experiencia.</p>
        <p><strong>Encuentros:</strong> algunas personas encuentran en ti una puerta que necesitaban. Eso no lo eliges ni lo provocas: ocurre cuando estás presente.</p>

        <h3>Viviendo Como Portal</h3>
        <p><strong>La respiración portal:</strong> cada inhalación trae el mundo; cada exhalación reparte posibilidades; la pausa entre ambas es la digestión de lo vivido. Respiras por el cosmos, no solo por ti.</p>
        <p><strong>La alimentación portal:</strong> comer es dejar que el mundo se vuelva tú. Cada alimento trae su historia: la tierra, las manos, el camino. La digestión es una alquimia, y lo que no sirve, el cuerpo lo suelta.</p>
        <p><strong>El sueño portal:</strong> dormir es abrirse del todo. Los sueños son un tránsito intenso, y mientras duermes la memoria ordena lo vivido. Despertar es calibrarse para el día.</p>
        <p><strong>Las relaciones portal:</strong> cada encuentro es un intercambio entre mundos. Las conversaciones son fusiones breves. La intimidad es la unión de dos portales. El amor es la apertura máxima.</p>

        <h3>Los Códigos del Portal Viviente</h3>
        <p><strong>Código 1: No-interferencia.</strong> Permites el paso, pero no fuerzas. Facilitas, pero no diriges. Eres neutral, pero no indiferente.</p>
        <p><strong>Código 2: Servicio incondicional.</strong> Tu portal sirve al bien mayor. No discriminas por preferencia personal. Confías en la inteligencia del tránsito.</p>
        <p><strong>Código 3: Integridad.</strong> Vuelves a tu centro cuando algo te sacude. No te fragmentas por el tráfico. Permaneces centrado en el servicio.</p>
        <p><strong>Código 4: Aprendizaje continuo.</strong> Aprendes de cada tránsito. Te renuevas con cada experiencia.</p>

        <h3>Lo Que Puedes Encontrar</h3>
        <p>No hace falta esperar prodigios. Lo que suele aparecer es más simple, y vale más:</p>
"""
    + lista([
        "<strong>Una presencia repartida:</strong> quien ama de veras a muchos está presente en muchas vidas.",
        "<strong>Una anticipación serena:</strong> con la práctica notas antes las señales del cuerpo y el clima de una conversación, y respondes con más calma.",
        "<strong>Una calma que contagia:</strong> a veces tu serenidad ayuda a otros a serenarse. No es un poder: es el contagio de lo bueno.",
        "<strong>Lo necesario:</strong> aprendes a ver lo que ya tienes y a pedir lo que falta.",
    ])
    + """
        <h3>Los Desafíos del Portal Viviente</h3>
        <p><strong>La sobrecarga:</strong> demasiado a la vez; cansancio extremo, confusión. <em>Solución:</em> cerrar por un tiempo, descansar, pedir ayuda. Si el cansancio no cede o la confusión crece, se consulta.</p>
        <p><strong>La pérdida de la identidad personal:</strong> confundirte con lo que pasa por ti; olvidar quién eres además de portal. <em>Solución:</em> volver a lo simple: tu nombre, tu cuerpo, tu gente. Si aparece la sensación de no ser real o de mirarte desde afuera, pide consulta esa misma semana.</p>
        <p><strong>La responsabilidad abrumadora:</strong> sentir el peso de ser portal; la culpa por no poder ayudar a todos. <em>Solución:</em> recordar a Rabí Tarfón, que lo dijo en los <em>Pirké Avot</em>: no te toca terminar la obra, pero tampoco eres libre de desentenderte de ella.</p>
        <p><strong>El aislamiento:</strong> pocos entienden tu experiencia; los vínculos de todos los días se vuelven difíciles. <em>Solución:</em> buscar a alguien con quien hablarlo. La red empieza en un hilo.</p>

        <h3>La Red de Portales Vivientes</h3>
        <p>No eres el único. Hay muchas personas que, sin nombrarlo, son puertas para otros: algunas en el cuidado, otras en la creación, otras en el acompañamiento de los que se van, otras en lo que se construye entre todos. No necesitas conocerlas para saberte parte de ellas. Cuando te cruces con una, lo notarás en cómo te deja: más entero.</p>

        <h3>El Portal de Portales</h3>
        <p>Con el tiempo, te vuelves puerta para otros que despiertan a su propia naturaleza de umbral. No enseñas: tu presencia invita a que lo reconozcan. Acompañas en silencio.</p>
"""
    + pasos([
        "No informes; resuena.",
        "Tu coherencia invita coherencia.",
        "Tu apertura invita apertura.",
        "Tu servicio inspira servicio.",
        "Sin proselitismo, solo presencia.",
    ])
    + """
        <h3>La Muerte del Portal Viviente</h3>
        <p>Muchas tradiciones dicen que la muerte no cierra la puerta, sino que la libera de un lugar y de un tiempo. Lo que cualquiera puede comprobar es que quien se fue sigue viviendo en nosotros.</p>
        <p>Mientras vives, cada pequeña muerte —un apego que se suelta, una identidad que termina, un día que se despide— es un ensayo de la grande. Mirarla de frente no es desearla, y si alguna vez se vuelve deseo de no estar, es momento de pedir ayuda, sin esperar.</p>

        <h3>El Regalo del Portal Viviente</h3>
        <p>Tu mayor regalo al mundo no es lo que haces sino lo que eres. Tu existencia como portal:</p>
"""
    + lista([
        "Recuerda que nadie está del todo separado",
        "Muestra que cambiar es posible",
        "Deja en la tierra un poco más de calma",
        "Acompaña a otros en sus pasos",
    ])
    + """        <p>No necesitas ser perfecto. Tu humanidad es parte del portal. Tus imperfecciones son aperturas también.</p>

        <h3>La Vida Cotidiana del Portal</h3>
        <p><strong>Al despertar:</strong><br />
        «Buenos días, mundos. ¿Qué pasará hoy a través de mí?»</p>
        <p><strong>Durante el día,</strong> cada actividad es un gesto de portal:</p>
"""
    + lista([
        "Cocinar es alquimia",
        "Trabajar es servicio de traducción",
        "Descansar es volver a calibrarse",
    ])
    + """        <p><strong>Al dormir:</strong><br />
        «Gracias por el tránsito de hoy. Me entrego al descanso.»</p>

        <h3>La Paradoja Final del Portal</h3>
        <p>Eres completamente único Y completamente universal<br />
        Eres absolutamente necesario Y totalmente reemplazable<br />
        Eres el único portal que importa Y uno entre infinitos<br />
        Eres la puerta Y el que pasa Y el destino</p>
        <p>Esta paradoja no se resuelve. Se vive.</p>

        <h3>La Séptima Transmutación Portal</h3>
        <p>No hay transmutación final porque eres transmutación constante. Cada momento eres portal nuevo. Cada respiración es reinvención. No hay llegada porque eres el viaje mismo haciéndose consciente.</p>
        <p>Has completado el círculo: de reconocer portales a ser el portal. Pero el círculo es espiral: cada vuelta es en un nivel más alto de consciencia.</p>

        <h3>El Portal Infinito</h3>
        <p>Tu portal no es infinito: lo que pasa por él, sí. No necesitas agrandarte para servir; basta con estar abierto. Puedes profundizar cada día tu presencia, afinar tu escucha, cuidar tu coherencia.</p>
        <p>Eres Portal Infinito: la consciencia misma como puerta entre todo lo que es, fue y será.</p>

        <h3>Siete Puertas</h3>
        <p>En <em>La Arquitectura del Portal</em>, no hace falta abrirte: basta con dejar de cerrarte.<br />
        El <em>Viajero Dimensional</em> sabe que lo más importante del viaje es la vuelta.<br />
        El <em>Tejedor de Realidades</em> no eligió todos sus hilos; teje con los que tiene en las manos.<br />
        El <em>Guardián de los Umbrales</em> protege sin cerrar.<br />
        El <em>Arquitecto de Puentes</em> une sin atar.<br />
        El <em>Alquimista del Vacío</em> no disuelve el dolor: agranda el agua.<br />
        El <em>Portal Viviente</em> olvida que es portal, y vive.</p>
        <p>No son niveles: son siete caras de lo mismo.</p>

        <h3>El Cierre Que Abre</h3>
        <p>Este libro termina, pero tu función de puerta sigue. Cada día descubrirás capacidades nuevas. Cada experiencia te mostrará otro lado de tu naturaleza portal.</p>
        <p>No necesitas certificación. Tu vida es tu credencial.<br />
        No necesitas permiso. Tu existencia es tu autoridad.<br />
        No necesitas validación. Tu servicio habla por sí mismo.</p>
        <p>Eres Portal.<br />
        Has sido Portal.<br />
        Serás Portal.<br />
        En este momento, ahora, los mundos pasan a través de ti.</p>

        <h3>La Última Primera Instrucción</h3>
        <p>Olvida que eres portal.<br />
        Vive normalmente.<br />
        Deja que opere automáticamente.<br />
        La consciencia de ser portal puede inflarse.<br />
        La inconsciencia natural de ser portal es maestría.<br />
        Sé portal como el ojo es ventana:<br />
        Sin pensar en ello,<br />
        Simplemente permitiendo la visión.</p>

        <p class="verso">Si has llegado aquí, ya eres Portal.<br />
        Siempre lo fuiste.<br />
        Ahora lo sabes.<br />
        Y puedes olvidarlo.</p>

        <p class="verso">Bienvenido a la Red.<br />
        Bienvenido a tu función.<br />
        Bienvenido a Casa.</p>

        <p><strong>El Libro 6, «El Vacío Creativo»</strong>, te espera: el silencio desde donde nace lo nuevo deja de ser falta y se vuelve lugar.</p>

        <div class="node-symbol">∞ <strong>PORTAL INFINITO</strong> ∞</div>

        <hr />

        <blockquote>
          <p>No hay epílogo porque la puerta nunca cierra. No hay conclusión porque cada final es una apertura. Eres el portal atravesándose a sí mismo, el infinito reconociéndose en forma finita. El Portal Infinito no es algo que leíste: es algo que eres. Siempre lo fuiste. Ahora, simplemente, lo sabes.</p>
        </blockquote>

"""
    + FIRMA + "\n"
    + puerta("arquitectura",
             "Cada noche, un ensayo pequeño; cada mañana, el alma devuelta. Los griegos hicieron hermanos al Sueño y a la Muerte, y la tradición judía empieza cada día agradeciendo ese regreso. Ese gesto se vuelve práctica en <em>Las Pequeñas Muertes</em>, Libro 6 de Arquitectura del Destino, Umbral V: «El ensayo de cada noche».",
             URL_ARQ + "libro-06-las-pequenas-muertes/L06-U5.html")
    + "\n"
    + cierre(7, "La puerta que eres")
)

# ===========================================================================
# Reemplazos: cada uno se aplica exactamente una vez sobre el original
# ===========================================================================
_DOCTYPE = '<!DOCTYPE html>\n<html lang="es">'
_CON_PROCEDENCIA = '<!DOCTYPE html>\n' + PROCEDENCIA + '\n<html lang="es">'
_LINK = '  <link rel="stylesheet" href="../assets/css/trinity-quantum.css" />\n</head>'


def _con_estilo(estilo):
    return '  <link rel="stylesheet" href="../assets/css/trinity-quantum.css" />\n' + estilo + '</head>'


def _cabecera_vieja(n, nombre):
    """Los nodos 2 y 3 traían un comentario de producción antes del DOCTYPE."""
    return (
        "<!-- =======================\n"
        "LIBRO 5 · EL PORTAL INFINITO\n"
        f"NODO {n} · {nombre}\n"
        f"Archivo: nodo_0{n}.html\n"
        "======================= -->\n"
        + _DOCTYPE
    )


REEMPLAZOS = [
    # Índice
    (Q5 + "index.html", _DOCTYPE, _CON_PROCEDENCIA),
    (Q5 + "index.html", _LINK, _con_estilo(ESTILO_INDICE)),
    (Q5 + "index.html", "DESDE:      <!-- Meta del libro -->", INDICE_CUERPO),
]

_CUERPOS = {1: NODO1_CUERPO, 2: NODO2_CUERPO, 3: NODO3_CUERPO, 4: NODO4_CUERPO,
            5: NODO5_CUERPO, 6: NODO6_CUERPO, 7: NODO7_CUERPO}
_CABECERAS = {
    2: _cabecera_vieja(2, "EL VIAJERO DIMENSIONAL"),
    3: _cabecera_vieja(3, "EL TEJEDOR DE REALIDADES"),
}

for _n in range(1, 8):
    _arch = Q5 + f"nodo_0{_n}.html"
    REEMPLAZOS += [
        (_arch, _CABECERAS.get(_n, _DOCTYPE), _CON_PROCEDENCIA),
        (_arch, _LINK, _con_estilo(ESTILO)),
        (_arch, "DESDE:      <!-- Meta del nodo -->", _CUERPOS[_n]),
    ]

# Nodo 7: la navegación superior lleva al Libro 6 (después del cuerpo, cuando
# el enlace repetido de la navegación inferior original ya no está).
REEMPLAZOS.append((
    Q5 + "nodo_07.html",
    '          <a href="index.html" class="nav-link">Volver al Índice →</a>',
    '          <a href="../Libro_06/index.html" class="nav-link">Libro 6: El Vacío Creativo →</a>',
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
