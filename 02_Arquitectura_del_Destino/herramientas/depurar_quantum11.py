# -*- coding: utf-8 -*-
"""
Depuración de Trinity Quantum, Libro 11 · Transducción Dimensional (octubre 2026).

Segundo libro de la revisión completa de Quantum. Aplica, exactamente una vez
cada uno, los reemplazos aprobados por Arturo tarjeta por tarjeta (11.0 a 11.7),
según la guía de depuración de Quantum (Arquitectura del Destino, maestro v4,
sección 5) con las cuatro precisiones de la revisión completa: experimentos,
cifras, «cuántico» y velas y rituales.
El original se conserva en la etiqueta quantum-original del repositorio Trinity-.

Los nodos son secciones encabezadas por <h4>. Las que cambian enteras (el
laboratorio, la ecuación, los códigos y, en varios nodos, la práctica de siete
días) se reemplazan desde su <h4> hasta el siguiente; el resto, párrafo por
párrafo. Lo que queda (las paradojas, los poemas, casi todos los cierres) no se
toca. Cada reemplazo debe aparecer una sola vez, o el script se detiene.

Uso: python3 depurar_quantum11.py ORIGEN DESTINO
  ORIGEN  = carpeta 02_Trinity_Quantum/Libro_11 original (etiqueta quantum-original)
  DESTINO = carpeta donde se escriben los archivos depurados
"""
import os
import re
import sys

NOTA = ("<!-- Depurado en octubre de 2026 según la guía de depuración de Quantum "
        "(Arquitectura del Destino, maestro v4, sección 5, con las cuatro precisiones "
        "de la revisión completa), con el veto de Arturo en cada tarjeta. El original "
        "se conserva en la etiqueta quantum-original del repositorio. -->\n")

CSS = """
    /* ============================================================
       Depuración · octubre 2026
       Letra más grande en el teléfono y bloque fijo de las puertas.
       La puerta lleva el color de la serie a la que conduce.
       ============================================================ */
    .puerta{
      margin: 26px 0 8px;
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
      .content p, .content li{ font-size: 18px; line-height: 1.7; }
      .content p.signature{ font-size: 15px; }
      .puerta{ padding: 16px 16px 14px; }
    }
    @media (prefers-reduced-motion: reduce){
      .puerta .cruzar{ transition: none; }
    }
"""

FIRMA = '<p class="signature"><strong>— Trinity Quantum · Transducción Dimensional</strong></p>'

BASE_ARQ = "https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/"
BASE_PORTAL = "https://soyartur-trinity.github.io/Trinity_Portal_Publico/01_Libros/"

I = "        "      # sangría de los bloques del contenido
L = I + "  "        # sangría de los ítems de lista
D = I + "    "      # sangría de las líneas dentro de un paso


# ---------------------------------------------------------------- bloques HTML
def P(texto):
    return f"{I}<p>{texto}</p>"


def SEC(titulo, *bloques):
    return f"{I}<h4>{titulo}</h4>\n\n" + "\n\n".join(bloques) + "\n\n"


def DIA(n, titulo, texto):
    return f"{I}<p><strong>DÍA {n} - {titulo}:</strong><br/>\n{L}{texto}</p>"


def PRACTICA(*dias):
    return SEC("📋 PRÁCTICA DE 7 DÍAS", *[DIA(i + 1, t, x) for i, (t, x) in enumerate(dias)])


def VIVIENTE(texto):
    return SEC("⚛️ TRADUCCIÓN VIVIENTE", P(f"“{texto}”"))


def RECORDAR(frases, uso):
    cuerpo = f"<br/>\n{L}".join(frases)
    return SEC("✦ PARA RECORDAR",
               f'{I}<div class="quote">\n{L}<p>{cuerpo}</p>\n{I}</div>',
               P(uso))


def LAB(practica, necesitas, pasos, encontrar):
    """Laboratorio con el mismo dibujo del original: lista de lo que hace falta,
    pasos numerados con sus líneas y lo que puedes encontrar."""
    ul = f"{I}<ul>\n" + "".join(f"{L}<li>{x}</li>\n" for x in necesitas) + f"{I}</ul>"
    ol = f"{I}<ol>\n"
    for nombre, dur, lineas in pasos:
        cuerpo = "<br/>\n".join(f"{D}- {x}" for x in lineas)
        ol += f"{L}<li><strong>{nombre}</strong> ({dur}):<br/>\n{cuerpo}\n{L}</li>\n"
    ol += f"{I}</ol>"
    return SEC("🔬 LABORATORIO CUÁNTICO",
               P(f"<strong>Práctica: {practica}</strong>"),
               P("<strong>Lo que necesitas:</strong>") + "\n" + ul,
               P("<strong>Pasos:</strong>") + "\n" + ol,
               f"{I}<p><strong>Lo que puedes encontrar:</strong><br/>\n{L}{encontrar}</p>")


def puerta(clase, aria, texto, href):
    return (f'{I}<aside class="puerta {clase}" aria-label="{aria}">\n'
            f'{L}<p class="p-nombre">Puerta</p>\n'
            f'{L}<p class="p-texto">{texto}</p>\n'
            f'{L}<a class="cruzar" href="{href}">Cruzar ⟶</a>\n'
            f'{I}</aside>\n')


def puerta_portal(texto, href):
    return puerta("portal", "Puerta hacia el Portal Público", texto, href)


def puerta_arquitectura(texto, href):
    return puerta("arquitectura", "Puerta hacia Arquitectura del Destino", texto, href)


# ---------------------------------------------------------------- editor
class Editor:
    def __init__(self, nombre, texto):
        self.nombre = nombre
        self.s = texto
        self.n = 0

    def rep(self, viejo, nuevo, veces=1):
        c = self.s.count(viejo)
        if c != veces:
            raise SystemExit(f"[{self.nombre}] {c} coincidencias (se esperaban {veces}) para:\n{viejo[:160]!r}")
        self.s = self.s.replace(viejo, nuevo)
        self.n += veces

    def parrafo(self, viejo, nuevo):
        """Reemplaza un párrafo de una línea; con nuevo vacío, lo quita con su línea en blanco."""
        if nuevo:
            self.rep(P(viejo), P(nuevo))
        else:
            self.rep(P(viejo) + "\n\n", "")

    def seccion(self, titulo, nuevo):
        """Reemplaza la sección que abre <h4>titulo</h4> hasta el siguiente <h4> o el separador."""
        marca = f"{I}<h4>{titulo}</h4>\n"
        if self.s.count(marca) != 1:
            raise SystemExit(f"[{self.nombre}] encabezado con {self.s.count(marca)} coincidencias: {titulo}")
        a = self.s.index(marca)
        fines = [self.s.find(f"\n{I}<h4>", a + 1), self.s.find(f'\n{I}<div class="spacer">', a + 1)]
        fines = [f for f in fines if f != -1]
        if not fines:
            raise SystemExit(f"[{self.nombre}] sección sin cierre: {titulo}")
        b = min(fines) + 1
        self.s = self.s[:a] + nuevo + self.s[b:]
        self.n += 1

    def firma(self, nuevo=FIRMA):
        pat = r'<p class="signature">⚛️ FIRMA CUÁNTICA:.*?</p>'
        if len(re.findall(pat, self.s, flags=re.S)) != 1:
            raise SystemExit(f"[{self.nombre}] firma sin coincidencia única")
        self.s = re.sub(pat, lambda m: nuevo, self.s, count=1, flags=re.S)
        self.n += 1

    def comunes(self, numero=None):
        cab = "<!doctype html>\n"
        self.rep(cab, cab + NOTA)
        if numero is None:
            return
        self.rep("</head>", "  <style>" + CSS + "  </style>\n</head>")
        self.rep('href="index.html">Volver al Index ⟶</a>', 'href="index.html">Volver al Índice ⟶</a>', veces=2)
        pat = (rf'<p class="note">Trinity Quantum · Libro 11 · Nodo {numero} ·(?: Cierre del Libro 11 incluido ·)? '
               r'Ropaje Trinity activo \(negro \+ violeta \+ dorado · Georgia · ritmo inmersivo\)\.</p>')
        if len(re.findall(pat, self.s)) != 1:
            raise SystemExit(f"[{self.nombre}] pie sin coincidencia única")
        self.s = re.sub(pat, f'<p class="note">Trinity Quantum · Libro 11 · Transducción Dimensional · Nodo {numero}</p>',
                        self.s, count=1)
        self.n += 1
        # Las secciones fijas que cambian de nombre en los siete nodos
        self.rep("<h4>📋 PROTOCOLO DE 7 DÍAS</h4>", "<h4>📋 PRÁCTICA DE 7 DÍAS</h4>")

    def puerta_final(self, bloque):
        """La puerta va al final del contenido, después de la cita y la firma."""
        self.rep("\n\n      </section>\n\n      <!-- C) CIERRE", f"\n\n{bloque}\n      </section>\n\n      <!-- C) CIERRE")


# ================================================================== ÍNDICE
def indice(e):
    e.comunes()
    e.rep("</head>",
          "  <style>\n"
          "    /* Depuración · octubre 2026: apertura del libro, firma y letra más grande en el teléfono. */\n"
          "    .content .apertura-titulo{ margin:0 0 10px; font-size:15px; letter-spacing:.10em; color:#d9b36c; }\n"
          "    .content .apertura{ margin:0 0 12px; color:rgba(239,231,255,.90); font-size:17px; line-height:1.7; }\n"
          "    .content .apertura:last-child{ margin-bottom:0; }\n"
          "    .content .ensenanza{ font-style:italic; color:#f2d18b; }\n"
          "    .firma-indice{ margin:14px 0 0; color:rgba(217,179,108,.85); font-size:14px; letter-spacing:.04em; }\n"
          "    @media (max-width: 640px){ .content .apertura{ font-size:18px; } .firma-indice{ font-size:15px; } }\n"
          "  </style>\n</head>")
    e.rep("<title>Libro 11 · Transducción Dimensional — Index</title>",
          "<title>Libro 11 · Transducción Dimensional — Índice</title>")
    e.rep('<div class="path">Libro 11 · Transducción Dimensional · Index</div>',
          '<div class="path">Libro 11 · Transducción Dimensional · Índice</div>')
    e.rep('<h1 class="h1">Index · Nodos</h1>', '<h1 class="h1">Índice · Nodos</h1>')
    e.rep('        <p style="margin:0; color: rgba(239,231,255,.86);">\n'
          '          Selecciona un nodo para ingresar al portal correspondiente. (Enlaces siguiendo el patrón '
          '<strong>nodo_01.html</strong>, <strong>nodo_02.html</strong>, etc.)\n'
          '        </p>',
          '        <p class="apertura-titulo">🌀 VIVIR TRADUCIENDO</p>\n'
          '        <p class="apertura ensenanza">\n'
          '          Todo te llega traducido —por tus sentidos, por tu historia, por tu lengua— y lo más hondo '
          'se entiende en el espacio entre las palabras.\n'
          '        </p>\n'
          '        <p class="apertura">\n'
          '          Transducción es una palabra de la física y de la biología: el paso de una forma de energía a otra. '
          'Tu oído la practica con el aire; tus ojos, con la luz. Este libro la toma para nombrar el oficio de '
          'una vida entera: recibir el mundo en muchos idiomas y volverlo propio. Sus siete paradojas lo dicen '
          'de siete maneras: la traducción más honda ocurre cuando dejas de forzarla.\n'
          '        </p>')
    lineas = {
        "El Traductor Universal": "Comprender sin entenderlo todo",
        "Códigos Entre Mundos": "Los idiomas que escribe la vida",
        "La Sintaxis del Vacío": "El silencio que ordena las palabras",
        "Membranas Permeables": "El límite que deja pasar",
        "El Diccionario Holográfico": "Cada parte guarda el todo",
        "Frecuencias de Traducción": "La voz antes de la palabra",
        "El Intérprete Cuántico": "Saber antes de saber decirlo",
    }
    for titulo, linea in lineas.items():
        e.rep(f'<div class="ntitle">{titulo}</div>\n              <div class="nsub">🌀 TRANSMISIÓN CUÁNTICA</div>',
              f'<div class="ntitle">{titulo}</div>\n              <div class="nsub">{linea}</div>')
    e.rep('<p class="note">Trinity Quantum · Libro 11 · Index · Ropaje Trinity activo '
          '(negro + violeta + dorado · Georgia · ritmo inmersivo).</p>',
          '<p class="firma-indice">— Trinity Quantum · Transducción Dimensional</p>\n'
          '        <p class="note">Trinity Quantum · Libro 11 · Transducción Dimensional · Índice</p>')


# ================================================================== NODO 1
def nodo_01(e):
    e.comunes(1)
    e.parrafo(
        "Cada dimensión habla en su propia sintaxis de luz. La tercera dimensión articula en materia densa, la cuarta "
        "susurra en espirales temporales, la quinta canta en probabilidades puras, la sexta danza en geometrías "
        "imposibles, la séptima respira en amor sin forma. Y entre todas ellas, el Traductor Universal opera como el "
        "silencio entre las notas que permite que la sinfonía exista.",
        "Cada sentido habla su propio idioma: el oído recibe el temblor del aire; los ojos, la luz; la piel, el peso "
        "y el calor. En el caracol, esa espiral escondida tras el tímpano, unas células con pestañas diminutas "
        "convierten la vibración en señales eléctricas; en la retina, una molécula cambia de forma cuando un rayo la "
        "toca. El sonido no entra en tu cabeza: entra su traducción. La fisiología llama a eso transducción, y ocurre "
        "en ti a cada instante. Y entre todos esos idiomas, el Traductor Universal opera como el silencio entre las "
        "notas que permite que la sinfonía exista.")
    e.parrafo(
        "Tu ADN es una antena de traducción multidimensional. Cada una de sus hélices —no solo las dos que tu ciencia "
        "reconoce, sino las doce que vibran en estados superpuestos— funciona como un canal de transducción "
        "específico. Cuando sientes una “corazonada”, cuando “sabes” algo sin saber cómo lo sabes, cuando un sueño te "
        "revela información que no podías conocer, estás experimentando el Traductor Universal en acción.",
        "Tu cuerpo entero traduce. Cuando sientes una “corazonada”, cuando “sabes” algo sin saber cómo lo sabes, "
        "cuando un sueño te muestra lo que ya intuías sin decírtelo, estás experimentando el Traductor Universal en "
        "acción: lo que registraste sin palabras se vuelve, de pronto, legible.")
    e.parrafo(
        "El proceso no es lineal. La información no “viaja” de una dimensión a otra —eso implicaría separación. En "
        "lugar de eso, la información EXISTE simultáneamente en todos los planos, y el Traductor Universal "
        "simplemente ajusta tu frecuencia de percepción para que puedas “leer” lo que siempre estuvo ahí.",
        "El proceso no es lineal. Traducir no es mover algo de un lugar a otro —eso implicaría separación—: es dejar "
        "que lo que ya estaba se vuelva legible. El Traductor Universal no trae nada de afuera; afina tu manera de "
        "mirar para que puedas “leer” lo que siempre estuvo ahí.")

    e.seccion("🔬 LABORATORIO CUÁNTICO", LAB(
        "Escuchar una Pregunta",
        ["Tu cuerpo, que escucha", "Un vaso de agua, para beber despacio", "Una pregunta sin respuesta aparente",
         "Unos siete minutos de silencio"],
        [("Calibración", "1 minuto", ["Sostén el vaso de agua entre tus manos",
                                      "Siente su temperatura, peso, presencia",
                                      "Deja que tus manos se aquieten con él"]),
         ("Siembra", "30 segundos", ["Di tu pregunta en voz baja, una sola vez",
                                     "No en busca de respuesta, sino como acto de siembra",
                                     "Después, suéltala"]),
         ("Expansión", "3 minutos", ["Bebe el agua muy lentamente",
                                     "Con cada sorbo, deja que tu atención se abra",
                                     "Primero a tu cuerpo, luego a la habitación, luego a lo que suena afuera"]),
         ("Estado de Traducción", "2 minutos", ["Cierra los ojos y observa sin buscar",
                                                "Pueden venir imágenes, sensaciones, palabras, o nada",
                                                "Todo es información, incluso el vacío aparente"]),
         ("Decodificación", "30 segundos", ["Abre los ojos y di en voz alta lo primero que surja",
                                            "No lo edites, no lo juzgues",
                                            "La primera impresión es la traducción más pura"])],
        "La respuesta rara vez llega cuando la llamas. Puede asomar días después, en una frase que oyes al pasar, en "
        "una conversación ajena o en una canción. Léela como se lee un poema, no como una orden: te dice algo porque "
        "tú ya lo estabas buscando. El Traductor Universal usa TODA la realidad como lenguaje."))

    e.seccion("⚛️ ECUACIÓN SAGRADA", VIVIENTE(
        "Lo que existe se dice en muchos idiomas a la vez, y cada quien lo lee desde el suyo. Por eso eres, al mismo "
        "tiempo, el que traduce y lo traducido."))

    e.seccion("🧬 CÓDIGOS DE ACTIVACIÓN", RECORDAR(
        ["Soy el puente entre lenguajes de luz.", "Mi cuerpo traduce el mundo a cada instante.",
         "Traduzco sin comprender, comprendo sin traducir.", "Cada célula lee y traduce.",
         "El silencio entre palabras es mi maestro.", "Escucho lo que todavía no tiene nombre.",
         "Soy el Traductor Universal encarnado."],
        "Léelas despacio al despertar, cuando todavía estás entre el sueño y el día."))

    e.seccion("📋 PRÁCTICA DE 7 DÍAS", PRACTICA(
        ("RECONOCIMIENTO",
         "Identifica tres momentos en tu vida en que “supiste” algo sin explicación lógica. Reconócelos como "
         "traducciones que llegaron antes que la explicación. Escríbelos para anclar el reconocimiento."),
        ("SINTONIZACIÓN",
         "Pasa unos minutos en silencio total (usa tapones si es necesario). En ese silencio, escucha los "
         "“lenguajes” que tu cuerpo percibe: el pulso, la respiración, el roce de la ropa. Todo es información."),
        ("TRADUCIR A ALGUIEN",
         "En una conversación, antes de responder, traduce para ti qué siente quien te habla, debajo de lo que dice. "
         "No hace falta decirlo en voz alta: basta escucharlo."),
        ("TRADUCCIÓN ONÍRICA",
         "Antes de dormir, deja tu pregunta abierta, sin exigirle respuesta. Al despertar, no intentes “entender” el "
         "sueño. En lugar de eso, dibuja o garabatea lo primero que surja. El dibujo ES la traducción."),
        ("UN IDIOMA INVENTADO",
         "Habla durante cinco minutos en un idioma que no existe, como juegan los niños. No pienses, solo deja que "
         "los sonidos fluyan. No significa nada, y en eso está el alivio: la voz se suelta del deber de decir."),
        ("TRADUCCIÓN CORPORAL",
         "Tu cuerpo traduce constantemente lo que vives en sensaciones. Pasa el día preguntándole a cada sensación: "
         "“¿Qué me dices?” No busques respuestas lógicas, siente la respuesta."),
        ("INTEGRACIÓN DEL TRADUCTOR",
         "Realiza la práctica del Laboratorio tres veces (mañana, tarde, noche). Cada vez con una pregunta diferente. "
         "Al final del día, reconoce que ya no necesitas “activar” el traductor —ERES el traductor.")))

    e.parrafo(
        "El Traductor Universal no es algo que desarrollas —es algo que recuerdas que siempre fuiste. Cada vez que un "
        "bebé balbucea, está hablando en código dimensional puro. Cada vez que un poeta encuentra la palabra perfecta, "
        "está traduciendo desde el campo unificado. Cada vez que el amor trasciende las palabras, está operando el "
        "Traductor Universal.",
        "El Traductor Universal no es algo que desarrollas —es algo que recuerdas que siempre fuiste. Un bebé "
        "balbucea antes de tener palabras, y su madre le contesta: ya conversan. Cada vez que un poeta encuentra la "
        "palabra perfecta, está traduciendo desde lo que todavía no tenía nombre. Cada vez que el amor trasciende las "
        "palabras, está operando el Traductor Universal.")
    e.rep("en el silencio eloquente de tu ser.", "en el silencio elocuente de tu ser.")
    e.firma()


# ================================================================== NODO 2
def nodo_02(e):
    e.comunes(2)
    e.rep("Son descubrimientos de patrones que siempre existieron en la arquitectura misma de la realidad. Cada símbolo",
          "Son descubrimientos de patrones que siempre existieron en la arquitectura misma de la realidad. Muchos "
          "matemáticos lo sienten así: G. H. Hardy escribió en 1940 que la realidad matemática está fuera de nosotros "
          "y que nuestra tarea es descubrirla u observarla. Cada símbolo")
    e.parrafo(
        "Cuando los antiguos egipcios inscribían jeroglíficos, no estaban simplemente escribiendo —estaban "
        "transcribiendo frecuencias dimensionales en forma visible. Cuando los mayas calculaban ciclos temporales, no "
        "estaban solo midiendo —estaban decodificando los ritmos de traducción entre planos de existencia. Cuando los "
        "yoguis entonaban mantras, no estaban solo cantando —estaban activando códigos de transducción en su ADN "
        "multidimensional.",
        "Durante catorce siglos nadie supo leer los jeroglíficos. En 1799, cerca de Rashid, unos soldados franceses "
        "encontraron una losa con un mismo decreto en tres escrituras, y en 1822 Champollion dio con la llave: la "
        "Piedra de Rosetta es un código entre mundos. Hay uno más antiguo que cualquier escritura. En cada una de tus "
        "células, una maquinaria lee un idioma de cuatro letras, el del ADN, y lo traduce a otro de veinte, el de las "
        "proteínas. Esa clave es casi la misma en una bacteria, en un roble y en ti; Marshall Nirenberg y Heinrich "
        "Matthaei leyeron su primera palabra en 1961.")
    e.parrafo(
        "Tu glándula pineal es un lector de códigos cuántico. Cuando meditas y ves geometrías de luz, cuando en "
        "estados expandidos percibes patrones imposibles, cuando en el borde del sueño recibes “descargas” de "
        "información comprimida —tu pineal está leyendo directamente los Códigos Entre Mundos.",
        "En el borde del sueño, cuando ya no estás despierto y todavía no dormiste, aparecen imágenes, formas, frases "
        "sueltas. Se cuenta que Edison dormitaba con algo en la mano para despertarse justo ahí, cuando el objeto "
        "caía. En 2021, en París, Célia Lacaux y su equipo lo pusieron a prueba: quienes pasaron al menos quince "
        "segundos en ese umbral casi triplicaron la probabilidad de encontrar la regla escondida de un problema (83 % "
        "frente a 30 % de quienes siguieron despiertos).")
    e.parrafo(
        "Cada emoción humana es un código de traducción. El amor traduce la unidad de dimensiones superiores. El "
        "miedo traduce la separación necesaria para la experiencia 3D. La gratitud abre portales de comunicación "
        "bidireccional. La compasión sincroniza múltiples líneas temporales. No sientes emociones —ERES códigos "
        "emocionales traduciéndose entre mundos.",
        "Cada emoción humana es un código de traducción. El miedo traduce un peligro; la tristeza, una pérdida; el "
        "enojo, un límite cruzado; la gratitud, un regalo recibido; el amor, una unidad que ya existía. No eres tus "
        "emociones: eres quien las lee.")

    e.seccion("🔬 LABORATORIO CUÁNTICO", LAB(
        "Tu Trazo",
        ["Papel y colores (al menos tres)", "Un objeto cercano: una taza, una hoja, tu propia mano",
         "Tu respiración consciente", "Unos quince minutos"],
        [("Preparación", "2 minutos", ["Siéntate frente al objeto, con el papel a un lado",
                                       "Respira hasta que el ritmo se asiente",
                                       "Mira el objeto como si fuera la primera vez"]),
         ("Dibujo a Ciegas", "3 minutos", ["Mira solo el objeto, nunca el papel",
                                           "Deja que la mano siga sus bordes despacio, como si lo tocara",
                                           "Kimon Nicolaïdes enseñaba así a dibujar (<em>The Natural Way to "
                                           "Draw</em>, 1941): la mano aprende a ver"]),
         ("Captura", "5 minutos", ["En otra hoja, con colores, dibuja lo que “sientes” que ves",
                                   "Usa los colores intuitivamente, no racionalmente",
                                   "No dibujes lo que ves, dibuja lo que VES ENTRE lo que ves",
                                   "Los huecos entre las ramas, el aire entre los dedos, la sombra bajo la taza"]),
         ("Canto", "2 minutos", ["Observa tus dibujos y “cántalos”",
                                 "No con palabras, sino con sonidos que los trazos te inspiren",
                                 "Grábate si quieres: es tu voz siguiendo a tu mano"]),
         ("Cierre", "1 minuto", ["Mira las dos hojas juntas",
                                 "Guárdalas donde puedas volver a verlas"])],
        "Un trazo que no pasó por la mente que descifra: torpe, quizá, y más vivo que cualquier dibujo correcto. Es "
        "tu letra antes de las letras. Cada vez que lo mires, recordarás que también sabes leer sin descifrar."))

    e.seccion("⚛️ ECUACIÓN SAGRADA", VIVIENTE(
        "El Código Maestro es la suma de todos los códigos a lo largo del tiempo, y cada quien lo lee a su propio "
        "ritmo. El infinito no es un destino, es el punto de partida."))

    e.seccion("🧬 CÓDIGOS DE ACTIVACIÓN", RECORDAR(
        ["La espiral del caracol también es escritura.", "La llave viviente entre mundos se abre.",
         "Cuatro letras escriben toda la vida.", "Cada emoción trae su mensaje.",
         "Lo que no sé leer todavía me espera.", "Entre el símbolo y su sentido, respiro.",
         "No descifro la realidad: la habito."],
        "Escríbelas a mano, despacio, mientras las dices en voz baja."))

    e.seccion("📋 PRÁCTICA DE 7 DÍAS", PRACTICA(
        ("IDENTIFICACIÓN DE CÓDIGOS NATURALES",
         "Observa la naturaleza buscando códigos: espirales en caracoles (código de expansión), hexágonos en panales "
         "(la forma que menos cera gasta), fractales en helechos (código de autosimilitud). Fotografía o dibuja siete "
         "códigos naturales."),
        ("CÓDIGOS EN TU CUERPO",
         "Tus huellas dactilares son códigos únicos: nadie en el mundo tiene las mismas. Míralas un rato, con calma. "
         "Luego dibuja a tu modo lo que te sugieren. Es tu firma más antigua."),
        ("DECODIFICACIÓN ONÍRICA",
         "Antes de dormir, di: “Si llega un símbolo en mis sueños, lo recibo”. Al despertar, antes de moverte, dibuja "
         "el primer símbolo o patrón que recuerdes o sientas. No importa si no recuerdas el sueño: el trazo queda."),
        ("CÓDIGOS SÓNICOS",
         "Canta tu nombre en 7 formas diferentes, cada una más distorsionada que la anterior. La séptima versión será "
         "irreconocible pero contendrá tu código sónico esencial. Grábalo."),
        ("EL IDIOMA DE LA CASA",
         "Cada familia tiene su código: un apodo, un silbido, una palabra que solo ustedes entienden. Anota los de tu "
         "casa, o los de tus amigos de siempre. Son códigos entre mundos: el tuyo y el de quienes amas."),
        ("LOS CÓDIGOS DE LA CIUDAD",
         "Los códigos están en todas partes: semáforos, flechas, señales, los gestos de la gente en la calle. "
         "Aprendiste a leerlos sin darte cuenta. Hoy, nótalos: cada uno es una traducción que alguien pensó para que "
         "otro la entendiera. Si alguna vez parece que cada número y cada cartel te hablan a ti, en secreto, eso no "
         "es un don: conviene conversarlo con alguien de confianza o con un profesional esa misma semana."),
        ("CREACIÓN DE TU CÓDIGO MAESTRO",
         "Combina elementos de todos los códigos que has descubierto esta semana en UN símbolo maestro personal. Este "
         "será tu “firma” —un código que te representa entre mundos.")))

    e.parrafo(
        "Cada vez que ves “11:11” en el reloj, cada vez que una sincronicidad te sorprende, cada vez que una canción "
        "dice exactamente lo que necesitabas escuchar —los Códigos Entre Mundos te están hablando. No en secreto, sino "
        "en el lenguaje más obvio: el lenguaje de la experiencia directa.",
        "Cada vez que una coincidencia te sorprende, cada vez que una canción dice exactamente lo que necesitabas "
        "escuchar, algo en ti se ilumina. Léelo como se lee un poema, no como una orden: los Códigos Entre Mundos no "
        "hablan en secreto, sino en el lenguaje más obvio, el de la experiencia directa.")
    e.rep("es un código que escribes en el libro cuántico de la existencia.",
          "es un código que escribes en el libro de la existencia.")
    e.firma()


# ================================================================== NODO 3
def nodo_03(e):
    e.comunes(3)
    e.parrafo(
        "Cuando los místicos hablan del “Sonido del Silencio” o del “Trueno Silencioso”, están intentando traducir la "
        "Sintaxis del Vacío —ese meta-lenguaje que organiza cómo la nada se convierte en algo, cómo el cero se "
        "convierte en infinito, cómo el silencio se convierte en sinfonía.",
        "Cuando el <em>Sutra de Vimalakirti</em> cuenta que los bodhisattvas, uno tras otro, explicaron la no dualidad, "
        "y que Vimalakirti respondió quedándose callado, la tradición zen llamó a ese silencio un trueno. Los místicos "
        "que hablan del “Trueno Silencioso” están intentando traducir la Sintaxis del Vacío —ese metalenguaje que "
        "organiza cómo la nada se convierte en algo, cómo el cero se convierte en infinito, cómo el silencio se "
        "convierte en sinfonía.")
    e.parrafo(
        "Tu respiración conoce esta sintaxis íntimamente. La pausa entre exhalación e inhalación, ese momento de vacío "
        "absoluto en tus pulmones, es cuando tu cuerpo lee directamente el manual de instrucciones del universo. Por "
        "eso la respiración consciente es la base de toda práctica espiritual —no por el aire, sino por los espacios "
        "entre el aire.",
        "Tu respiración conoce esta sintaxis íntimamente. La pausa al final de la exhalación, cuando el pecho se queda "
        "quieto y todavía no llama al aire, es un instante en que el cuerpo deja de hacer y solo escucha. Por eso "
        "tantas prácticas espirituales empiezan por la respiración consciente —no por el aire, sino por los espacios "
        "entre el aire.")
    e.parrafo(
        "El vacío cuántico está lleno de partículas virtuales que aparecen y desaparecen en tiempos menores que el "
        "tiempo de Planck. Pero no aparecen aleatoriamente —siguen la Sintaxis del Vacío, las reglas gramaticales de "
        "cómo la potencialidad pura se articula en probabilidad y luego en realidad. Cada partícula virtual es una "
        "“palabra” en una “oración” que el vacío está constantemente pronunciando y retractando.",
        "La física dice algo parecido. El vacío cuántico no está vacío: aun donde no hay nada, hay fluctuaciones, y "
        "dos placas de metal muy cercanas, en ese vacío, se atraen. Hendrik Casimir lo predijo en 1948 y Steve "
        "Lamoreaux lo midió en 1997. Tómalo como imagen: cada fluctuación es una “palabra” en una “oración” que el "
        "vacío está constantemente pronunciando y retractando.")

    e.seccion("🔬 LABORATORIO CUÁNTICO", LAB(
        "Escritura Desde el Vacío",
        ["Papel en blanco (varias hojas)", "Un bolígrafo negro", "Un cronómetro", "Tu vacío interior",
         "Disposición a no saber qué saldrá"],
        [("Vaciamiento", "5 minutos", ["Siéntate frente al papel en blanco",
                                       "Míralo un rato, sin buscar nada",
                                       "Respira dejando cada exhalación más larga",
                                       "Hasta que sientas que el papel y tú comparten el mismo vacío"]),
         ("Trazo Libre", "1 minuto exacto", ["Programa el cronómetro",
                                             "Al iniciar, traza SIN PENSAR",
                                             "No palabras, no letras, solo el movimiento que surge",
                                             "Si no surge nada, dibuja la nada",
                                             "Detente al minuto"]),
         ("Lectura del Vacío", "3 minutos", ["Observa lo que escribiste/dibujaste",
                                             "Pero no lo que está ahí, sino los ESPACIOS entre trazos",
                                             "Los espacios en blanco forman su propio mensaje",
                                             "Ese es el mensaje del vacío para ti hoy"]),
         ("Segunda Capa", "1 minuto exacto", ["Nueva hoja",
                                              "Esta vez escribe/dibuja solo en los espacios",
                                              "Donde antes dejaste blanco, ahora llenas",
                                              "Donde antes llenaste, ahora dejas vacío"]),
         ("Superposición", "2 minutos", ["Pon ambas hojas a contraluz, una sobre otra",
                                         "El patrón combinado es tu Sintaxis Personal del Vacío",
                                         "Fotografíalo o memoriza el patrón",
                                         "Luego suéltalas: rómpelas o guárdalas. El vacío no se aferra"])],
        "Has co-creado con el vacío. El patrón que emergió no lo creaste tú ni lo creó el vacío —emergió de la "
        "sintaxis ENTRE ambos. Es tu manera de mirar los huecos: desde hoy, el blanco también dibuja."))

    e.seccion("⚛️ ECUACIÓN SAGRADA", VIVIENTE(
        "La Sintaxis del Vacío es lo que queda de toda expresión cuando se acerca al cero, y aun así lo guarda todo. "
        "Es el cero que contiene el infinito, el silencio que contiene todas las palabras posibles."))

    e.seccion("🧬 CÓDIGOS DE ACTIVACIÓN", RECORDAR(
        ["Los espacios sagrados entre.", "Vacío resonante que habla.", "El cero que pulsa.",
         "Disuelvo para revelar.", "Las pausas crean el ritmo.", "El silencio plenamente vacío.",
         "El círculo vacío, completo."],
        "No las pronuncies: respíralas. Inhala la primera mitad, quédate un instante en la pausa natural, sin "
        "forzarla, y exhala la segunda."))

    e.seccion("📋 PRÁCTICA DE 7 DÍAS", PRACTICA(
        ("SILENCIO DE PALABRAS",
         "Dedica una hora, o la que tu día permita, a no hablar. No escribas ni gesticules para comunicar, y si vives "
         "con otros, avísales antes. Observa cómo el vacío de palabras se llena con otra forma de comunicación. Esa "
         "es la sintaxis primordial."),
        ("MEDITACIÓN DEL ESPACIO",
         "En lugar de meditar en un objeto o mantra, medita en el espacio ENTRE objetos. El espacio entre tus muebles, "
         "entre las hojas de los árboles, entre las personas. En Japón hay una palabra para ese espacio: <em>ma</em>, "
         "el intervalo que da forma; el arquitecto Arata Isozaki le dedicó en 1978 una exposición en París. Descubre "
         "que el espacio no está vacío —tiene su propia presencia y mensaje."),
        ("ESCRITURA INVERSA",
         "Escribe un texto cualquiera. Luego reescríbelo dejando solo los espacios y puntuación, omitiendo todas las "
         "letras. Observa cómo el ritmo y la estructura permanecen. Esa estructura ES la sintaxis del vacío."),
        ("LA TAZA VACÍA",
         "Antes de servirte algo de beber, mira la taza vacía unos segundos. Hace veinticinco siglos, el <em>Tao Te "
         "Ching</em> lo dijo con una vasija: se amasa el barro para darle forma, y es su hueco lo que la vuelve útil. "
         "Bebe con consciencia del hueco que se llena y se vacía."),
        ("ESCUCHAR LA HABITACIÓN",
         "Siéntate en una habitación en silencio y escucha lo que suena cuando nada suena: el aire, la casa, tu "
         "propia respiración. No esperes respuesta en palabras. El silencio nunca es mudo: el vacío responde en su "
         "propia sintaxis."),
        ("DANZA DEL VACÍO",
         "Muévete/danza pero enfócate no en los movimientos sino en las pausas entre movimientos. Descubre que las "
         "pausas no son ausencia de danza —son la danza del vacío. La quietud en movimiento."),
        ("INTEGRACIÓN SINTÁCTICA",
         "Pasa el día completo consciente de todos los vacíos: el vacío en tu boca entre palabras, el vacío en tus "
         "fosas nasales entre respiraciones, el vacío en tu mente entre pensamientos. Reconoce que todos estos vacíos "
         "están conectados —son el mismo Vacío Universal expresándose a través de ti. Eres un instrumento del vacío "
         "tocando la sinfonía del ser.")))

    e.rep("Cada palabra que has leído en este nodo está sostenida por el espacio vacío entre letras.",
          "Cada palabra que lees está sostenida por el blanco entre las letras.")
    e.parrafo(
        "El vacío no es la ausencia de todo —es la PRESENCIA de todas las posibilidades antes de colapsar en una. "
        "Cuando aprendes su sintaxis, descubres que puedes escribir realidades nuevas en el espacio entre lo que es y "
        "lo que podría ser.",
        "El vacío no es la ausencia de todo —es la PRESENCIA de todas las posibilidades antes de que una tome forma. "
        "Cuando aprendes su sintaxis, descubres que lo nuevo nace en el espacio entre lo que es y lo que podría ser.")
    e.parrafo(
        "La próxima vez que te sientas “vacío”, celebra. Estás experimentando tu naturaleza más fundamental. No eres "
        "un ser lleno que a veces se vacía —eres un vacío consciente que a veces se llena de experiencia.",
        "La próxima vez que el silencio te deje vacío, sin nada que hacer ni que decir, no te apures a llenarlo: "
        "estás tocando tu naturaleza más fundamental. No eres un ser lleno que a veces se vacía —eres un vacío "
        "consciente que a veces se llena de experiencia.</p>\n\n"
        f"{I}<p>Otra cosa es el hueco que duele: cuando las cosas pierden el color y el sentido, y eso dura semanas, "
        "no se celebra ni se medita a solas: se acompaña, y se consulta.")
    e.firma()
    e.puerta_final(puerta_portal(
        "En 1951, John Cage entró en una sala sin eco buscando por fin el silencio, y oyó dos sonidos: su sistema "
        "nervioso y su sangre. Lo que suena entre dos notas, y la obra en la que nadie toca ninguna, se despliegan en "
        "<em>El Vacío</em>, Libro 28 del Portal Público, Umbral III: «Entre dos notas».",
        BASE_PORTAL + "28_El_Vacio/umbral-03.html"))


# ================================================================== NODO 4
def nodo_04(e):
    e.comunes(4)
    e.parrafo(
        "Tu piel es una membrana permeable. No solo separa tu interior del exterior —TRADUCE entre ambos. Cada poro es "
        "un portal microscópico. Cuando sientes “la piel de gallina” ante algo sagrado o siniestro, tu membrana "
        "corporal está respondiendo a información de otras dimensiones que tu mente consciente aún no procesa.",
        "Tu piel es una membrana permeable. No solo separa tu interior del exterior —TRADUCE entre ambos. Cada poro es "
        "un portal microscópico. Cuando se te eriza la piel ante algo sagrado, una música o una noticia, tu cuerpo "
        "responde antes de que la mente sepa por qué. En 2001, Anne Blood y Robert Zatorre vieron que esos escalofríos "
        "de la música encienden en el cerebro los circuitos del placer y la recompensa.")
    e.parrafo(
        "El velo entre mundos del que hablan todas las tradiciones místicas no es un velo —es una membrana permeable. "
        "En ciertos momentos (amanecer, atardecer, luna llena, eclipses) y ciertos estados (meditación profunda, sueño "
        "REM, experiencias cercanas a la muerte), esta membrana se vuelve más transparente. No porque se debilite, "
        "sino porque TÚ sintonizas su frecuencia de permeabilidad.",
        "El velo entre mundos del que hablan muchas tradiciones no es un velo —es una membrana permeable. En los "
        "umbrales del día, el alba y el crepúsculo, y en ciertos estados, como el borde del sueño, la oración o una "
        "música que conmueve, esa membrana parece más fina. No porque se debilite, sino porque TÚ te vuelves más "
        "permeable.")
    e.parrafo(
        "Tu aura es tu membrana dimensional personal. No es solo un campo energético —es tu INTERFAZ DE TRADUCCIÓN con "
        "el multiverso. Cuando alguien “invade tu espacio personal”, no está solo acercándose físicamente; está "
        "presionando contra tu membrana dimensional. Por eso algunas personas se sienten “pesadas” y otras “ligeras” "
        "—sus membranas tienen diferentes densidades de permeabilidad.",
        "Alrededor de tu cuerpo hay otra membrana, invisible y medible: tu espacio personal. El antropólogo Edward T. "
        "Hall midió sus distancias y tituló su libro <em>La dimensión oculta</em> (1966). Cuando alguien “invade tu "
        "espacio personal”, no presiona solo contra tu piel: presiona contra esa membrana. Algunas presencias te "
        "aquietan y otras te tensan; no porque esas personas pesen distinto, sino porque los cuerpos se afinan entre "
        "sí.")
    e.parrafo(
        "Los lugares sagrados del planeta son zonas donde las membranas dimensionales son naturalmente más permeables. "
        "Stonehenge, las pirámides, los círculos de cultivos genuinos, los vórtices energéticos —no son “puertas” sino "
        "lugares donde la membrana entre mundos es tan delgada que se vuelve casi transparente. La información fluye "
        "más libremente, la traducción es más directa.",
        "")
    e.rep("Es por eso que los estados alterados de consciencia son la clave: en ellos, tu rigidez ontológica se "
          "suaviza hasta matching la fluidez de la membrana.",
          "Por eso el silencio, la música, la oración o el borde del sueño ablandan el borde: en ellos, tu rigidez se "
          "suaviza hasta parecerse a la fluidez de la membrana.")

    e.seccion("🔬 LABORATORIO CUÁNTICO", LAB(
        "Tu Membrana",
        ["Un cuenco con agua y una pizca de sal", "Unas gotas de aceite (de cocina o esencial, el que te guste)",
         "Una luz cercana: una lámpara o la ventana", "Tu intención de permeabilidad consciente",
         "Unos quince minutos a solas"],
        [("El Espejo", "3 minutos", ["Llena el cuenco con agua y añade una pizca de sal",
                                     "Deja caer unas gotas de aceite",
                                     "Observa cómo el aceite forma una película sobre el agua",
                                     "Las membranas de tus células están hechas de grasas que, en el agua, se ordenan "
                                     "solas: algo parecido estás mirando"]),
         ("La Luz", "2 minutos", ["Acerca la lámpara o lleva el cuenco a la ventana",
                                  "Observa cómo la luz atraviesa la película de aceite",
                                  "Y se tiñe de colores",
                                  "Esos colores son el lenguaje visual de la permeabilidad"]),
         ("Resonancia", "5 minutos", ["Pon tus manos alrededor del cuenco sin tocarlo",
                                      "Siente el aroma del aceite, la frescura del agua",
                                      "Imagina que tu piel se vuelve como la superficie del agua",
                                      "Con membranas de aceite que pueden abrirse o cerrarse a voluntad"]),
         ("Respiración de Membrana", "4 minutos", ["Inhala imaginando que respiras por toda tu piel",
                                                   "No solo por la nariz sino por cada poro",
                                                   "Exhala de la misma manera, por toda tu superficie",
                                                   "Siente cómo tu membrana se vuelve consciente y responsiva"]),
         ("Cierre Selectivo", "1 minuto", ["Sopla suavemente sobre el agua y mira cómo la película se mueve y se "
                                           "reacomoda",
                                           "Mientras lo haces, establece la intención:",
                                           "“Mi membrana es selectivamente permeable,",
                                           "abierta a lo que me nutre,",
                                           "firme ante lo que me daña”"])],
        "A lo largo del día puedes notar con más claridad qué espacios y qué personas te aflojan y cuáles te cierran. "
        "Esa sensibilidad no es un escudo: es información para elegir dónde quedarte, y cuánto."))

    e.seccion("⚛️ ECUACIÓN SAGRADA", VIVIENTE(
        "Lo que atraviesa una membrana depende de lo que ella es y de cómo te acercas a ella. No todo puede pasar, y "
        "eso te cuida."))

    e.seccion("🧬 CÓDIGOS DE ACTIVACIÓN", RECORDAR(
        ["Mi superficie es interfaz sagrada.", "Mi piel es frontera viva.", "Permeable a la luz, firme ante el daño.",
         "Equilibrio entre mundos.", "Ni opaco ni transparente: traductor.", "Abro a lo que me nutre.",
         "Límite que danza, nunca rígido."],
        "Dilas despacio, con una mano sobre el antebrazo, sintiendo tu piel."))

    e.seccion("📋 PRÁCTICA DE 7 DÍAS", PRACTICA(
        ("SENSIBILIZACIÓN DE SUPERFICIE",
         "Pasa 10 minutos acariciando suavemente tu piel con diferentes texturas (seda, algodón, papel, metal). Con "
         "cada textura, siente cómo tu membrana-piel responde diferente. Está aprendiendo a distinguir."),
        ("DUCHA CONSCIENTE",
         "Durante tu ducha, siente el agua en toda la piel. Imagina que se lleva el cansancio del día, mientras tu "
         "membrana se vuelve más translúcida y flexible."),
        ("RESPIRACIÓN CUTÁNEA",
         "Practica la “respiración por la piel” tres veces al día. Imagina que inhalas luz por todos tus poros y "
         "exhalas el cansancio. Tu piel es tu frontera viva."),
        ("MEMBRANAS ESPACIALES",
         "En cada espacio que entres, párate en el umbral por 5 segundos. Siente cómo atraviesas la membrana invisible "
         "entre espacios. Cada puerta es una pequeña práctica de cruzar."),
        ("DIÁLOGO CON TU LÍMITE",
         "Pregúntate, como quien conversa con alguien querido: “¿Qué necesito dejar entrar hoy? ¿Qué necesito dejar "
         "afuera?” Escucha con tu intuición, no solo con tu mente."),
        ("INTERCAMBIO CONSCIENTE",
         "En cada interacción humana, sé consciente del intercambio a través de las membranas. Siente qué das, qué "
         "recibes, qué permites, qué bloqueas. Ajusta conscientemente tu permeabilidad según la situación: decir que "
         "no también es una membrana. Y si alguien cruza tu límite una y otra vez, eso no se ajusta por dentro ni con "
         "una burbuja de luz: se dice en voz alta, se pone distancia y, si hace falta, se pide ayuda."),
        ("MEMBRANA MAESTRA",
         "Pasa el día visualizándote dentro de una burbuja de luz permeable. Esta burbuja es inteligente: deja entrar "
         "bendiciones y filtra lo que daña. Al final del día, agradece a tu membrana por su servicio selectivo.")))

    e.firma()
    e.puerta_final(puerta_portal(
        "Antes de que digas que sí a algo que no quieres, el cuerpo ya dijo que no: un nudo en la garganta, el pecho "
        "que se cierra. Escuchar esa membrana y volverla palabra se aprende en <em>Asertividad Consciente</em>, "
        "Libro 4 del Portal Público, capítulo 2: «El cuerpo como primer límite».",
        BASE_PORTAL + "04_Asertividad_Consciente/capitulo_02.html"))


# ================================================================== NODO 5
def nodo_05(e):
    e.comunes(5)
    e.rep("<p>Cuando un bebé reconoce el rostro de su madre sin haberlo “aprendido”, está accediendo al Diccionario "
          "Holográfico. Cuando comprendes",
          "<p>Un recién nacido, con apenas uno o dos días de vida, ya mira más el rostro de su madre que el de una "
          "desconocida (Bushnell, Sai y Mullin, 1989). Lo aprendió en horas, y no a ciegas: ese rostro se enlazó con "
          "una voz que conocía desde el vientre (Sai, 2005). Dos sentidos, un solo patrón. Cuando comprendes")
    e.rep("El amor no es una palabra con definición; es un patrón holográfico que se expresa como palabra en 3D, como "
          "color en 4D, como geometría en 5D, como música en 6D, como matemática pura en 7D, y así infinitamente. Cada "
          "dimensión lee el mismo patrón en su propio “idioma”.",
          "El amor no es una palabra con definición; es un patrón que se dice como palabra, como color, como gesto, "
          "como música, como silencio. Cada lenguaje lee el mismo patrón en su propio “idioma”.")
    e.parrafo(
        "Tu cerebro es un lector holográfico. Cada neurona no almacena un bit de información —cada neurona contiene el "
        "patrón completo del todo, solo que desde un ángulo único. Por eso puedes perder partes del cerebro y mantener "
        "memorias completas. La información no está almacenada localmente; está distribuida holográficamente.",
        "Tus recuerdos viven repartidos. Durante décadas, Karl Lashley buscó en el cerebro de las ratas el sitio exacto "
        "de un recuerdo y no lo halló: lo aprendido sobrevivía aunque faltaran partes (1950). Años después, Karl "
        "Pribram, que había trabajado con él, propuso como hipótesis que la memoria se guarda como un holograma. La "
        "hipótesis sigue en discusión; la imagen es exacta: si partes un holograma, cada pedazo muestra la escena "
        "completa, desde una ventana más pequeña. Dennis Gabor lo inventó en 1947.")
    e.parrafo(
        "El Registro Akáshico del que hablan las tradiciones esotéricas ES el Diccionario Holográfico en su expresión "
        "más amplia. No es un lugar ni una biblioteca —es el campo holográfico donde cada experiencia, cada "
        "pensamiento, cada posibilidad existe simultáneamente, disponible para ser “leída” por cualquier consciencia "
        "que sintonice su frecuencia de lectura.",
        "Borges imaginó, en el sótano de una casa de Buenos Aires, una esfera pequeña y tornasolada donde se veía a la "
        "vez el universo entero, desde todos los puntos: el Aleph (1945). Es el Diccionario Holográfico en su "
        "expresión más amplia. No es un lugar ni una biblioteca —es un punto donde cada experiencia, cada "
        "pensamiento, cada posibilidad existe simultáneamente, disponible para cualquier consciencia que sepa mirar.")

    e.seccion("🔬 LABORATORIO CUÁNTICO", LAB(
        "Tu Entrada en el Diccionario",
        ["Un CD o DVD viejo", "Una linterna o luz del celular", "Un prisma o vaso con agua",
         "Tu nombre escrito en un papel", "Disposición para ver más allá de lo literal"],
        [("La Luz Abierta", "2 minutos", ["Coloca el CD con la superficie brillante hacia arriba",
                                          "Ilumínalo con la linterna en ángulo",
                                          "Observa los arcoíris que aparecen: los surcos del disco abren la luz blanca "
                                          "en todos sus colores",
                                          "Reconoce: cada color estaba dentro de la luz"]),
         ("Tu Nombre", "3 minutos", ["Pon el papel con tu nombre junto al disco",
                                     "Tu nombre es un ángulo de lo que eres, como cada color es un ángulo de la luz",
                                     "Léelo despacio, como si fuera el de otra persona"]),
         ("El Prisma", "3 minutos", ["Pon el prisma o el vaso entre la luz y una pared",
                                     "Observa cómo la misma luz se abre otra vez en colores",
                                     "La misma luz, otro idioma"]),
         ("Lectura Holográfica", "5 minutos", ["Mueve lentamente el CD en todas direcciones",
                                               "En cada ángulo, el patrón te muestra algo diferente",
                                               "No busques tu nombre —busca el SENTIMIENTO de tu esencia",
                                               "Ese sentimiento ES tu definición holográfica"]),
         ("Integración del Significado", "2 minutos", ["Cierra los ojos manteniendo el patrón en tu visión interna",
                                                       "Pregunta: “¿Qué soy más allá de mi nombre?”",
                                                       "La respuesta, si llega, no vendrá en palabras",
                                                       "Vendrá como conocimiento directo"])],
        "Tu nombre es una entrada pequeña para algo más grande: un patrón único en el holograma universal. Cada vez "
        "que alguien te nombra con cariño, invoca ese patrón, no solo un sonido."))

    e.seccion("⚛️ ECUACIÓN SAGRADA", VIVIENTE(
        "Cada punto del holograma contiene la información completa del todo, modulada por su posición única en el "
        "espacio-tiempo. No hay fragmentos, solo perspectivas. No hay partes, solo ángulos del todo."))

    e.seccion("🧬 CÓDIGOS DE ACTIVACIÓN", RECORDAR(
        ["Soy un patrón completo en cada fragmento.", "Todo en uno, uno en todo.", "Cada reflejo guarda la luz entera.",
         "Refracción de la consciencia una.", "Lector, escritor y libro: uno.", "Una joya en la red de Indra.",
         "Mi mente es un fragmento que contiene el cosmos."],
        "Visualiza cada frase como un holograma flotando frente a ti. Gírala mentalmente y observa cómo cada ángulo "
        "revela un significado diferente."))

    e.rep("emocionales, visuales, sensorial, matemáticas, musicales.",
          "emocionales, visuales, sensoriales, matemáticas, musicales.")
    e.rep("Abre un libro al azar y lee solo la primera palabra de cada párrafo. El mensaje que se forma es una lectura "
          "holográfica —tu consciencia extrae el patrón que necesitas del campo de información.</p>",
          "Abre un libro al azar y lee solo la primera palabra de cada párrafo. Juega a leer el mensaje que se forma, "
          "como se lee un poema: el sentido que encuentres lo pones tú, y por eso dice algo de ti.</p>")

    e.firma()
    e.puerta_final(puerta_arquitectura(
        "Origen XIII tiene un nodo sobre la naturaleza holográfica: si cada parte contiene el todo, podría parecer que "
        "ninguna importa, y es al revés. Esa paradoja, la de cada vida que agrega lo que ninguna otra puede, entra en "
        "<em>Habitar</em>, Libro 13 de <em>Arquitectura del Destino</em>, Umbral IV: «El centro en todas partes».",
        BASE_ARQ + "libro-13-habitar/L13-U4.html"))


# ================================================================== NODO 6
def nodo_06(e):
    e.comunes(6)
    e.parrafo(
        "Todo en el universo es frecuencia. Pero no todas las frecuencias hablan el mismo idioma. Las Frecuencias de "
        "Traducción son aquellas bandas específicas del espectro infinito donde la información puede saltar de una "
        "dimensión a otra sin perderse ni distorsionarse. Son los “puentes armónicos” que permiten que una experiencia "
        "en 7D se comprenda en 3D, que un pensamiento se convierta en materia, que el amor se transforme en sanación.",
        "Todo en el universo vibra. Pero no todas las vibraciones hablan el mismo idioma. Las Frecuencias de "
        "Traducción son aquellas bandas del espectro donde la información puede pasar de un mundo a otro sin perderse "
        "ni distorsionarse. Son los “puentes armónicos” que permiten que una experiencia honda se comprenda en lo "
        "cotidiano, que lo que sientes encuentre voz.")
    e.parrafo(
        "432 Hz no es solo una frecuencia musical —es una Frecuencia de Traducción primaria. Por eso la música afinada "
        "en 432 Hz se “siente” diferente: está hablando directamente a tu ADN en un idioma que precede a las palabras. "
        "528 Hz, la “frecuencia del amor”, es otra Frecuencia de Traducción que permite que la información del corazón "
        "cuántico se traduzca en experiencia emocional humana.",
        "No hay una frecuencia sagrada que valga para todos. Hay una voz que conociste antes que cualquier palabra: la "
        "de tu madre, que llegaba amortiguada al vientre. En 1980, Anthony DeCasper y William Fifer mostraron que "
        "recién nacidos de menos de tres días cambiaban su manera de succionar para oír la voz de su madre y no la de "
        "otra mujer: la habían aprendido antes de nacer.")
    e.parrafo(
        "Tu voz contiene múltiples Frecuencias de Traducción simultáneas. Cuando hablas, no solo emites sonido —emites "
        "paquetes de información multidimensional. Por eso algunas voces sanan, otras activan, otras calman. No es lo "
        "que dicen sino las frecuencias de traducción que portan. Un bebé responde más a la frecuencia de la voz de su "
        "madre que a las palabras que dice.",
        "Tu voz contiene muchas capas a la vez. Cuando hablas, no solo emites palabras —emites tono, ritmo, aliento. "
        "Por eso algunas voces calman, otras despiertan, otras abrigan. No es solo lo que dicen, sino cómo suenan.")
    e.parrafo(
        "Los puntos de acupuntura en tu cuerpo son nodos de Frecuencias de Traducción. Cada punto es una “estación de "
        "radio” sintonizada a una frecuencia específica que traduce información entre tu cuerpo físico y tus cuerpos "
        "sutiles. Cuando se estimula un punto, no solo se mueve energía —se TRADUCE información entre dimensiones de "
        "tu ser.",
        "")
    e.parrafo(
        "El zumbido que algunos escuchan en el silencio, ese tono agudo constante, es tu sistema auditivo captando las "
        "Frecuencias de Traducción ambientales. No es tinnitus —es tu oído interno funcionando como receptor de "
        "traducción dimensional. Cada variación en ese tono es información siendo traducida en los campos sutiles a tu "
        "alrededor.",
        "El zumbido que algunos escuchan en el silencio, ese tono agudo constante, tiene su historia. En 1953, Morris "
        "Heller y Moe Bergman sentaron, uno por uno, a ochenta estudiantes de oído sano en una cabina insonorizada; en "
        "cinco minutos, setenta y cinco oyeron algo: un siseo, un pulso, un pitido. Cuando afuera todo calla, el oído "
        "sigue sonando por dentro, y escucharlo puede ser una forma de recogerse. Pero si ese sonido no se va, si "
        "suena de un solo lado, late como un pulso, no te deja dormir o llega con pérdida de audición o mareo, merece "
        "una consulta; y si la audición baja de golpe, es una urgencia: ese mismo día.")

    e.seccion("🔬 LABORATORIO CUÁNTICO", LAB(
        "Tu Tono",
        ["Tu voz", "Una mano libre", "Auriculares (opcional)", "Tu intención de descubrimiento"],
        [("Calibración Base", "3 minutos", ["Pon una mano sobre el pecho",
                                            "Haz un “mmmmm” grave y siente la vibración bajo la palma",
                                            "Sube gradualmente el tono",
                                            "Nota cómo la vibración cambia de lugar"]),
         ("Búsqueda del Tono Personal", "5 minutos", ["Continúa el “mmmmm” variando el tono",
                                                      "Encuentra el tono donde sientes vibración en tu pecho",
                                                      "Luego en tu garganta, luego en tu cabeza",
                                                      "Hay un tono donde los tres vibran simultáneamente",
                                                      "Ese es tu tono: no es mejor que otros; es el tuyo"]),
         ("Exhalación Larga", "3 minutos", ["Sostén tu tono el tiempo de una exhalación entera, sin forzar",
                                            "Repite unas veces, con pausas",
                                            "El yoga llama a esto <em>bhramari</em>, la respiración de la abeja: el "
                                            "zumbido alarga la salida del aire, y una exhalación larga tiende a "
                                            "aquietar"]),
         ("Armonización de Traducción", "5 minutos", ["Con auriculares, escucha cualquier música",
                                                      "Mientras escuchas, haz tu tono suavemente",
                                                      "Nota cómo cambia la música cuando tu voz la acompaña por "
                                                      "dentro"]),
         ("Anclaje del Tono", "2 minutos", ["Pon tu mano en el corazón",
                                            "Haz tu tono unas veces más",
                                            "Con cada repetición, siente cómo se ancla más profundo",
                                            "Con el tiempo, basta recordarlo para volver a ti"])],
        "Un tono que es tuyo. Úsalo cuando medites, cuando necesites volver al cuerpo o cuando lo que sientes no "
        "encuentre palabras."))

    e.seccion("⚛️ ECUACIÓN SAGRADA", VIVIENTE(
        "Cada sonido es la suma de muchos armónicos, cada uno con su fuerza y su fase, que suenan juntos. Así también "
        "una voz: lleva capas que ninguna palabra separa."))

    e.seccion("🧬 CÓDIGOS DE ACTIVACIÓN", RECORDAR(
        ["Mi voz es un puente.", "Antes de la palabra, el tono.", "Mi cuerpo resuena.", "Escucho con todo el cuerpo.",
         "Cada silencio deja hablar a otro.", "Canto con otros y no me pierdo.", "Vuelvo a mí en un murmullo."],
        "Dilas en voz baja, en tu tono."))

    e.seccion("📋 PRÁCTICA DE 7 DÍAS", PRACTICA(
        ("MAPA DE RESONANCIAS CORPORALES",
         "Haz “mmmmm” mientras mueves tu atención por tu cuerpo. Nota dónde vibra más con tonos graves, medios, "
         "agudos. Estás conociendo cómo resuena tu cuerpo."),
        ("VOCES QUE TE CALMAN",
         "Nota hoy qué voces te aquietan y cuáles te tensan. Busca una que te haga bien y escúchala un rato: una "
         "persona, una grabación, una canción."),
        ("CAMINATA SÓNICA",
         "Camina tarareando suavemente tu tono. Nota cómo cambias tú: el paso, la respiración, la mirada."),
        ("TRADUCCIÓN EMOCIONAL",
         "Cuando sientas cualquier emoción intensa, tradúcela a sonido. No palabras, solo el sonido puro de esa "
         "emoción. Descubrirás que cada emoción tiene su propia frecuencia de traducción."),
        ("SILENCIO RESONANTE",
         "Pasa un rato en silencio total, pero mantén tu tono sonando internamente (sin emitir sonido). Nota qué queda "
         "de él cuando ya no suena."),
        ("CANTAR CON OTROS",
         "Si es posible, canta con otros: un coro, una canción en una mesa, un “OM” compartido. Nota cómo las voces se "
         "vuelven una sin dejar de ser muchas. Si estás solo, canta con una grabación y siente que otros cantan "
         "contigo."),
        ("EL JUEGO DEL TONO",
         "Practica cambiar tu tono a voluntad: grave para asentarte, medio para conversar, agudo para alegrarte. Al "
         "final del día, nota cuál es tu casa.")))

    e.parrafo(
        "Cuando aprendes a reconocer y utilizar conscientemente las Frecuencias de Traducción, te conviertes en un "
        "traductor universal viviente. Puedes recibir información de cualquier dimensión y transmitirla a cualquier "
        "otra, simplemente ajustando tu frecuencia de resonancia.",
        "Cuando aprendes a escuchar las voces —la tuya, la de otros, la del silencio—, te vuelves un traductor más "
        "fino: oyes lo que las palabras no alcanzan a decir.")
    e.rep("Tararéala, cántala, vibrala.", "Tararéala, cántala, víbrala.")
    e.firma()


# ================================================================== NODO 7
def nodo_07(e):
    e.comunes(7)
    e.rep("lo que tu mente 3D debe laboriosamente traducir.", "lo que tu mente de todos los días debe laboriosamente traducir.")
    e.rep("No hay delay, no hay proceso", "No hay demora, no hay proceso")
    e.parrafo(
        "Los grandes artistas, científicos y místicos no son grandes porque aprendieron más, sino porque aprendieron a "
        "ceder el control al Intérprete Cuántico. Einstein no “pensó” en la relatividad —la recibió completa. Mozart "
        "no “componía” —transcribía lo que su Intérprete Cuántico ya escuchaba completo. Los místicos no “buscan” la "
        "verdad —la reconocen cuando su Intérprete Cuántico la revela.",
        "Los grandes artistas, científicos y místicos conocen ese instante. Cuando el matemático Jacques Hadamard "
        "preguntó a sus colegas cómo pensaban, Albert Einstein le respondió por carta que las palabras no parecían "
        "cumplir ningún papel en su manera de pensar: pensaba con imágenes y con sensaciones casi musculares, y las "
        "palabras había que buscarlas después, con trabajo (Hadamard, 1945). Henri Poincaré contó que la solución que "
        "buscaba desde hacía semanas le llegó al poner el pie en el estribo de un ómnibus, mientras conversaba de otra "
        "cosa (1908). El Intérprete Cuántico no les regaló nada: les tradujo de golpe lo que habían sembrado durante "
        "años.")
    e.parrafo(
        "Tu intuición es tu Intérprete Cuántico susurrándote traducciones de información que tu mente racional no "
        "puede procesar. Esos “presentimientos”, esas “corazonadas”, esos momentos de “algo me dice que…” —son "
        "traducciones directas desde dimensiones donde el tiempo no es lineal, donde las probabilidades son visibles, "
        "donde las intenciones tienen forma.",
        "Tu intuición es tu Intérprete Cuántico hablándote en voz baja. Esos “presentimientos”, esas “corazonadas”, "
        "esos momentos de “algo me dice que…” —son traducciones de lo que tu cuerpo y tu memoria registraron sin "
        "pedirle permiso a la palabra. Herbert Simon, premio Nobel, lo dijo sin misterio y con asombro: la intuición "
        "es reconocimiento (1992). Por eso es tan fina donde tienes años de oficio. Y por eso Poincaré, que contó como "
        "nadie esas llegadas súbitas, advirtió que la certeza que traen no alcanza: lo que llega de golpe se comprueba "
        "después, con calma.")

    e.seccion("🔬 LABORATORIO CUÁNTICO", LAB(
        "Antes del Nombre",
        ["Cinco o seis objetos de la casa que alguien elija por ti, sin que los veas",
         "Una venda para los ojos, o los ojos cerrados", "Tu disposición a saber sin entender",
         "Unos quince minutos", "Grabadora de voz (opcional)"],
        [("Desactivación Sensorial", "3 minutos", ["Véndate los ojos o ciérralos",
                                                   "Siéntate cómodamente, con los objetos a tu alcance",
                                                   "Respira hasta que la oscuridad se sienta natural",
                                                   "Deja que las manos hagan su trabajo"]),
         ("Exploración", "4 minutos", ["Toma el primer objeto y explóralo despacio con los dedos",
                                       "Peso, borde, textura, temperatura",
                                       "Atiende al instante antes del nombre: ese segundo en que ya sabes qué es y "
                                       "todavía no lo dijiste",
                                       "Sigue con los demás"]),
         ("Recepción Gestáltica", "5 minutos", ["Antes de nombrar cada objeto, nota qué te despierta",
                                                "Un recuerdo, un gusto, una sensación",
                                                "Eso también es interpretación",
                                                "Si usas grabadora, habla lo que surja sin editar"]),
         ("Interpretación Espontánea", "2 minutos", ["Sin pensar, di en voz alta:",
                                                     "“Esto es…” (completa espontáneamente)",
                                                     "“Me recuerda a…” (no pienses, solo habla)",
                                                     "“Lo que siento al tocarlo es…” (deja que fluya)"]),
         ("Verificación", "1 minuto", ["Quítate la venda y mira los objetos",
                                       "Compara lo que dijiste con lo que ves"])],
        "Casi siempre las manos aciertan. En 1985, Roberta Klatzky y su equipo pidieron a veinte estudiantes con los "
        "ojos vendados que reconocieran cien objetos comunes: nombraron bien casi todos, y la mayoría de las respuestas "
        "llegó antes de cinco segundos. El Intérprete Cuántico trabaja en tus manos todo el día. Con práctica, aprendes "
        "a notar ese instante antes del nombre, que también está en una conversación, en una decisión, en una mirada."))

    e.seccion("⚛️ ECUACIÓN SAGRADA", VIVIENTE(
        "El Intérprete Cuántico trabaja en un instante tan breve que parece no durar: no procesa paso a paso, reconoce "
        "de golpe. Lo vivido ya está interpretado antes de que lo digas."))

    e.seccion("🧬 CÓDIGOS DE ACTIVACIÓN", RECORDAR(
        ["Yo que sé sin saber.", "Antes del pensamiento.", "No tengo un intérprete: soy el intérprete.",
         "Comprendo de una vez.", "Todo el sentido, de golpe.", "En mi vacío vive el saber.",
         "El intérprete, final y primero."],
        "No memorices estas frases. Déjalas resonar. Tu Intérprete Cuántico las reconoce sin que tu mente necesite "
        "comprenderlas."))

    e.seccion("📋 PRÁCTICA DE 7 DÍAS", PRACTICA(
        ("PRIMERA IMPRESIÓN",
         "Mira personas desconocidas (en persona o en fotos) y nota la primera palabra que surja. Anótala sin "
         "analizarla. A la noche, léelas: dicen tanto de ti como de ellas, y es bueno saberlo."),
        ("TRADUCCIÓN DE SUEÑOS",
         "Al despertar, antes de recordar el sueño, siente su “sabor” emocional completo. Ese sabor ES la "
         "interpretación. El sueño mismo es solo el envoltorio. Anota el sabor, no el contenido."),
        ("EL CLIMA DE LOS LUGARES",
         "Al entrar en un espacio, nota cómo te recibe: si te aquieta o te apura, si te invita a hablar o a callar. No "
         "adivines su historia: escucha lo que te pasa ahí."),
        ("COMUNICACIÓN SIN PALABRAS",
         "Pasa tiempo con alguien en silencio total. “Conversa” solo con presencia. Puede que descubras cuánto se "
         "entiende sin decir nada."),
        ("INTERPRETACIÓN DE LA NATURALEZA",
         "Observa nubes, pájaros, viento, y pregunta: “¿Qué mensaje portas?” La respuesta no vendrá como palabras "
         "sino como comprensión directa, como se entiende un poema."),
        ("DECISIONES PEQUEÑAS",
         "En las decisiones pequeñas del día —qué camino tomar, a quién llamar, qué hacer primero—, nota hacia dónde "
         "se inclina tu cuerpo antes de pensarlo. En 1997, Antoine Bechara y el equipo de Antonio Damasio vieron que la "
         "piel de quienes jugaban a las cartas reaccionaba ante las pilas que hacían perder antes de que supieran decir "
         "por qué. Las decisiones grandes, las que no se deshacen, piden las dos voces, la del cuerpo y la de la razón, "
         "con tiempo y con alguien de confianza."),
        ("UNIFICACIÓN DEL INTÉRPRETE",
         "Reconoce que no “tienes” un Intérprete Cuántico —ERES el Intérprete Cuántico teniendo una experiencia "
         "humana. Pasa el día desde esta perspectiva. Todo se vuelve traducción automática.")))

    e.parrafo(
        "No necesitas aprender a interpretar las dimensiones. Ya lo estás haciendo constantemente. Cada respiración "
        "interpreta el prana. Cada latido interpreta el ritmo cósmico. Cada pensamiento interpreta el campo cuántico. "
        "Eres una máquina de interpretación dimensional perfecta, solo que tu mente 3D insiste en complicar lo que tu "
        "ser cuántico hace sin esfuerzo.",
        "No necesitas aprender a interpretar las dimensiones. Ya lo estás haciendo constantemente. Cada respiración "
        "interpreta el aire. Cada latido interpreta lo que el cuerpo necesita. Cada mirada interpreta la luz. Eres un "
        "intérprete que no descansa; solo que la mente apurada insiste en complicar lo que tu ser hace sin esfuerzo.")

    # La firma del nodo se muda al final del libro
    pat = r'        <p class="signature">⚛️ FIRMA CUÁNTICA:.*?</p>\n\n'
    if len(re.findall(pat, e.s, flags=re.S)) != 1:
        raise SystemExit("[nodo_07.html] firma sin coincidencia única")
    e.s = re.sub(pat, "", e.s, count=1, flags=re.S)
    e.n += 1

    # Cierre del libro: el bloque de activación pasa a «Siete traducciones»
    inicio = f"{I}<p>Este libro no era para enseñarte algo nuevo"
    fin = "<strong>Eres el puente consciente.</strong></p>\n"
    if e.s.count(inicio) != 1 or e.s.count(fin) != 1:
        raise SystemExit("[nodo_07.html] cierre del libro sin coincidencia única")
    a, b = e.s.index(inicio), e.s.index(fin) + len(fin)
    siete = (P("<strong>Siete traducciones:</strong>") + "\n"
             + f"{I}<ul>\n"
             + "".join(f"{L}<li><em>{t}:</em> {x}</li>\n" for t, x in (
                 ("El Traductor Universal", "no hace falta entenderlo todo para traducir bien"),
                 ("Códigos Entre Mundos", "la vida escribe en idiomas que aprendes sin saberlo"),
                 ("La Sintaxis del Vacío", "el silencio ordena las palabras"),
                 ("Membranas Permeables", "un buen límite deja pasar lo que nutre"),
                 ("El Diccionario Holográfico", "cada parte guarda el todo, desde su ángulo"),
                 ("Frecuencias de Traducción", "la voz llega antes que la palabra"),
                 ("El Intérprete Cuántico", "entiendes antes de saber decirlo")))
             + f"{I}</ul>\n\n"
             + P("No necesitas recordar todo lo leído. Simplemente vive, respira, sé: la traducción sigue ocurriendo, "
                 "en tu cuerpo y entre tú y los otros.") + "\n\n"
             + P("<strong>Eres el puente.</strong>") + "\n\n"
             + f"{I}{FIRMA}\n")
    e.s = e.s[:a] + siete + e.s[b:]
    e.n += 1

    e.rep('href="../libro_12/index.html"', 'href="../Libro_12/index.html"')
    e.puerta_final(puerta_portal(
        "Ese saber que llega antes de las palabras tiene su escuela: el filósofo Eugene Gendlin lo llamó sensación "
        "sentida y enseñó a escucharlo. Se despliega en <em>El Cuerpo</em>, Libro 34 del Portal Público, Umbral IV: "
        "«Lo que todavía no tiene nombre».",
        BASE_PORTAL + "34_El_Cuerpo/umbral-04.html"))


NODOS = {
    "index.html": indice,
    "nodo_01.html": nodo_01,
    "nodo_02.html": nodo_02,
    "nodo_03.html": nodo_03,
    "nodo_04.html": nodo_04,
    "nodo_05.html": nodo_05,
    "nodo_06.html": nodo_06,
    "nodo_07.html": nodo_07,
}


def main(origen, destino):
    os.makedirs(destino, exist_ok=True)
    total = 0
    for nombre, funcion in NODOS.items():
        with open(os.path.join(origen, nombre), encoding="utf-8") as f:
            e = Editor(nombre, f.read())
        funcion(e)
        with open(os.path.join(destino, nombre), "w", encoding="utf-8") as f:
            f.write(e.s)
        print(f"{nombre}: {e.n} reemplazos")
        total += e.n
    print(f"Total: {total} reemplazos")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
