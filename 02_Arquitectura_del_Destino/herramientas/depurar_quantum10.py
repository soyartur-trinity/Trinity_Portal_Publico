# -*- coding: utf-8 -*-
"""
Depuración de Trinity Quantum, Libro 10 · Campos de Torsión (octubre 2026).

Aplica, exactamente una vez cada uno, los reemplazos aprobados por Arturo
tarjeta por tarjeta (10.0 a 10.7), según la guía de depuración de Quantum
(Arquitectura del Destino, maestro v4, sección 5).
El original se conserva en la etiqueta quantum-original del repositorio Trinity-.

Los nodos de este libro son secciones encabezadas por <h4>. Las secciones que
cambian enteras se reemplazan desde su <h4> hasta el siguiente; el resto,
frase por frase. Cada reemplazo debe aparecer una sola vez, o el script se detiene.

Uso: python3 depurar_quantum10.py ORIGEN DESTINO
  ORIGEN  = carpeta 02_Trinity_Quantum/Libro_10 original
  DESTINO = carpeta donde se escriben los archivos depurados
"""
import os
import re
import sys

NOTA = ("<!-- Depurado en octubre de 2026 según la guía de depuración de Quantum "
        "(Arquitectura del Destino, maestro v4), con el veto de Arturo en cada nodo. "
        "El original se conserva en la etiqueta quantum-original del repositorio. -->\n")

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

FIRMA_VIEJA = '<p class="signature"><strong>- Códigos de los Campos de Torsión</strong></p>'
FIRMA = '<p class="signature"><strong>— Trinity Quantum · Campos de Torsión</strong></p>'

BASE_ARQ = "https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/"
BASE_PORTAL = "https://soyartur-trinity.github.io/Trinity_Portal_Publico/01_Libros/"

I = "        "      # sangría de los bloques del contenido
L = I + "  "        # sangría de los ítems de lista


# ---------------------------------------------------------------- bloques HTML
def P(texto):
    return f"{I}<p>{texto}</p>"


def V(*lineas):
    """Párrafo en versos: una línea por <br>, como en el original."""
    return f"{I}<p>" + f"<br>\n{I}".join(lineas) + "</p>"


def UL(*items, lead=None):
    s = (P(lead) + "\n") if lead else ""
    return s + f"{I}<ul>\n" + "".join(f"{L}<li>{x}</li>\n" for x in items) + f"{I}</ul>"


def OL(*items, lead=None):
    s = (P(lead) + "\n") if lead else ""
    return s + f"{I}<ol>\n" + "".join(f"{L}<li>{x}</li>\n" for x in items) + f"{I}</ol>"


def SEC(titulo, *bloques):
    return f"{I}<h4>{titulo}</h4>\n\n" + "\n\n".join(bloques) + "\n\n"


def puerta(clase, aria, texto, href):
    return (f'{I}<aside class="puerta {clase}" aria-label="{aria}">\n'
            f'{L}<p class="p-nombre">Puerta</p>\n'
            f'{L}<p class="p-texto">{texto}</p>\n'
            f'{L}<a class="cruzar" href="{href}">Cruzar ⟶</a>\n'
            f'{I}</aside>')


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

    def seccion(self, titulo, nuevo):
        """Reemplaza la sección que abre <h4>titulo</h4> hasta el siguiente <h4> o el cierre del contenido."""
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

    def comunes(self, numero=None):
        cab = "<!doctype html>\n"
        if self.s.count(cab) != 1:
            raise SystemExit(f"[{self.nombre}] sin cabecera doctype")
        self.rep(cab, cab + NOTA)
        if numero is None:
            return
        self.rep("</head>", "  <style>" + CSS + "  </style>\n</head>")
        self.rep(FIRMA_VIEJA, FIRMA)
        self.rep('href="index.html">Volver al Index ⟶</a>', 'href="index.html">Volver al Índice ⟶</a>')
        pat = (rf'<p class="note">Trinity Quantum · Libro 10 · Nodo {numero} · Ropaje Trinity activo '
               r'\(negro \+ violeta \+ dorado · Georgia · ritmo\s+inmersivo\)\.</p>')
        if len(re.findall(pat, self.s)) != 1:
            raise SystemExit(f"[{self.nombre}] pie sin coincidencia única")
        self.s = re.sub(pat, f'<p class="note">Trinity Quantum · Libro 10 · Campos de Torsión · Nodo {numero}</p>',
                        self.s, count=1)
        self.n += 1


# ================================================================== ÍNDICE
def indice(e):
    e.comunes()
    e.rep("</head>",
          "  <style>\n"
          "    /* Depuración · octubre 2026: apertura del libro y letra más grande en el teléfono. */\n"
          "    .content .apertura-titulo{ margin:0 0 10px; font-size:15px; letter-spacing:.10em; color:#d9b36c; }\n"
          "    .content .apertura{ margin:0; color:rgba(239,231,255,.90); font-size:17px; line-height:1.7; }\n"
          "    @media (max-width: 640px){ .content .apertura{ font-size:18px; } }\n"
          "  </style>\n</head>")
    e.rep("<title>Libro 10 · Campos de Torsión — Index</title>",
          "<title>Libro 10 · Campos de Torsión — Índice</title>")
    e.rep('<div class="path">Libro 10 · Campos de Torsión · Index</div>',
          '<div class="path">Libro 10 · Campos de Torsión · Índice</div>')
    e.rep('<h1 class="h1">Index · Nodos</h1>', '<h1 class="h1">Índice · Nodos</h1>')
    e.rep('        <p style="margin:0; color: rgba(239,231,255,.86);">\n'
          '          Selecciona un nodo para ingresar al portal correspondiente. (Enlaces siguiendo el patrón '
          '<strong>nodo_01.html</strong>, <strong>nodo_02.html</strong>, etc.)\n'
          '        </p>',
          '        <p class="apertura-titulo">🌀 EL CENTRO QUIETO</p>\n'
          '        <p class="apertura">\n'
          '          Todo lo que vive da vueltas: el agua que baja por un desagüe, el aire tibio que sube y lleva a las aves, '
          'la sangre, los días. Este libro toma esa rotación como imagen —en geometría, la torsión es la manera en que '
          'el espacio, además de curvarse, podría retorcerse, como la concibió Élie Cartan en 1922— para mirar lo que '
          'nos arrastra y lo que nos eleva. Su enseñanza cabe en una línea: todo remolino tiene un centro quieto, '
          'y desde ahí se aprende a girar sin perderse.\n'
          '        </p>')
    e.rep('<div class="ntitle">Espirales de ADN Activándose</div>', '<div class="ntitle">La Doble Hélice</div>')
    e.rep('<div class="ntitle">La Geometría del Spin</div>', '<div class="ntitle">La Geometría del Espín</div>')
    e.rep('<p class="note">Trinity Quantum · Libro 10 · Index · Ropaje Trinity activo '
          '(negro + violeta + dorado · Georgia · ritmo inmersivo).</p>',
          '<p class="note">Trinity Quantum · Libro 10 · Campos de Torsión · Índice</p>')


# ================================================================== NODO 1
def nodo_01(e):
    e.comunes(1)
    e.rep("Este giro no es accidental - es el movimiento", "Este giro no es accidental: es el movimiento")
    e.rep("cómo evoluciona sin linealmente avanzar. Y en el centro de tu ser, tu alma gira en su propia espiral sagrada, "
          "creando campos de torsión que moldean tu realidad.",
          "cómo evoluciona sin avanzar en línea recta. Y en el centro de tu ser, tu alma gira en su propia espiral sagrada, "
          "y ese giro moldea tu manera de habitar la realidad.")
    e.rep(V("El giro del alma no es metáfora.", "Es física multidimensional.",
            "Es el mecanismo por el cual transformas energía en materia,", "potencial en actual,", "sueño en realidad."),
          V("El giro del alma no se mide con instrumentos.", "Se reconoce desde adentro.",
            "Es la manera en que la energía se vuelve gesto,", "el potencial, acto,", "el sueño, un día vivido."))
    e.rep("<li>Un pensamiento giró obsesivamente hasta transformarse en comprensión</li>",
          "<li>Un pensamiento dio vueltas durante días hasta volverse comprensión</li>")

    e.seccion("LA FÍSICA DEL SPIN CONSCIENTE", SEC(
        "LOS TRES MOVIMIENTOS DEL GIRO",
        P("En física cuántica, el espín es una propiedad fundamental de las partículas: no es que giren, sino que poseen "
          "un momento angular propio, y el de un electrón, al medirlo, solo muestra dos valores, arriba o abajo. "
          "Algo parecido conoce el alma: dos sentidos y un centro."),
        UL("Apertura", "Creación", "Emanación", "Evolución", "Impulso",
           lead="<strong>Hacia afuera:</strong> el giro de la expansión"),
        UL("Integración", "Absorción", "Introspección", "Consolidación", "Encarnación",
           lead="<strong>Hacia adentro:</strong> el giro de la contracción"),
        UL("Quietud dinámica", "Potencial puro", "El vacío creador", "Presencia total", "El ahora eterno",
           lead="<strong>El punto cero:</strong> el ojo del huracán"),
        P("La maestría no está en dominar estos movimientos, sino en reconocer cuál te mueve ahora "
          "y volver al centro cuando haga falta.")))

    e.seccion("LOS CAMPOS DE TORSIÓN DEL ALMA", SEC(
        "LOS CAMPOS DE TORSIÓN DEL ALMA",
        UL("Ordena tu atención: ves más de aquello que te importa",
           "Tiñe tu ánimo y el tono de tus días",
           "Te inclina hacia ciertos caminos",
           "Te aparta de otros",
           "Deja una huella que los demás reconocen como tuya",
           lead="Cuando tu alma gira alrededor de algo —una pregunta, un amor, una pérdida—, ese giro crea su campo "
                "de torsión: arrastra lo que está cerca. Ese campo:"),
        UL("Tu cuerpo: lo siente primero, en el pulso y la respiración",
           "Tu ánimo: el color con que miras el día",
           "Tus encuentros: lo que llevas a cada conversación",
           "Tus lugares: el clima de una casa, de un aula, de un taller",
           "Lo lejano: lo que pusiste en marcha llega a personas que no vas a conocer",
           lead="Ese campo se abre en círculos, como el agua alrededor de una piedra, y pierde fuerza a medida que se aleja:")))

    e.seccion("LOS RITMOS DEL GIRO", SEC(
        "LOS RITMOS DEL GIRO",
        P("Tu alma no gira a velocidad constante. Tiene ritmos:"),
        UL("Mañana: el giro se acelera", "Mediodía: máxima velocidad", "Tarde: el giro se aquieta",
           "Noche: mínima velocidad", "Madrugada: punto de inflexión",
           lead="<strong>Ritmo Circadiano:</strong> 24 horas"),
        UL("Primavera: giro emergente", "Verano: giro radiante", "Otoño: giro integrador", "Invierno: giro introspectivo",
           lead="<strong>Ritmo Anual:</strong> 365 días"),
        UL("Infancia: giro caótico y explorador", "Juventud: giro acelerado y expansivo",
           "Madurez: giro estable y productivo", "Vejez: giro sabio que integra", "Transición: el giro que se suelta",
           lead="<strong>Ritmo de Vida:</strong> Toda tu existencia")))

    e.seccion("TECNOLOGÍA DEL GIRO CONSCIENTE", SEC(
        "PARA HABITAR EL GIRO",
        OL("Muévete: camina, baila, da unas vueltas lentas. Los derviches giran en oración después de años de aprendizaje; "
           "a ti te bastan tres",
           "Imagina una espiral que se abre",
           "Respira en espiral (inhala girando hacia arriba)",
           "Recuerda lo que te entusiasma",
           "Busca la alegría, también la pequeña",
           lead="<strong>Para el giro hacia afuera:</strong>"),
        OL("Quietud física profunda",
           "Visualiza el punto cero en tu centro",
           "Respiración lenta, con la salida del aire más larga",
           "Pensamientos de consolidación",
           "Conecta con la paz y el vacío",
           lead="<strong>Para volver hacia adentro:</strong>"),
        OL("Gira hacia el otro lado",
           "Cambia el orden de una rutina pequeña",
           "Haz, por un rato, lo contrario de tu tendencia",
           "Explora tu sombra",
           "Abraza tu polaridad negada",
           lead="<strong>Para cambiar de sentido:</strong>")))

    e.rep("<li>Es tu motor de manifestación</li>", "<li>Es el motor de lo que das</li>")
    e.rep(UL("<strong>Bloqueado:</strong> Vida estancada, depresión, desconexión",
             "<strong>Girando erráticamente:</strong> Caos emocional, drama, inestabilidad",
             "<strong>Girando coherentemente:</strong> Flujo, sincronicidad, magia",
             "<strong>En punto cero:</strong> Iluminación, unidad, presencia pura"),
          UL("<strong>Cerrado:</strong> Estancamiento, distancia",
             "<strong>Agitado:</strong> Emociones que se atropellan",
             "<strong>Sereno:</strong> Fluidez, encuentro, asombro",
             "<strong>En punto cero:</strong> Iluminación, unidad, presencia pura") + "\n\n" +
          P("Ningún estado del corazón es una falta. Hay temporadas cerradas, y se atraviesan; la tristeza que dura semanas "
            "se consulta, porque también el corazón se cuida acompañado."))

    e.rep(P("Tu alma gira a través de siete vórtices principales:"),
          P("La tradición del yoga describe siete de estos vórtices a lo largo del cuerpo y los llama ruedas: "
            "eso quiere decir <em>chakra</em> en sánscrito."))
    e.rep(V("Cada uno gira a su propia velocidad.", "Cuando se sincronizan, ocurre la coherencia.",
            "Cuando la coherencia es perfecta, el kundalini despierta."),
          V("Cada uno, dice la tradición, tiene su propio ritmo.", "Cuando se armonizan, aparece la coherencia.",
            "Y en lo alto de ese camino sitúa el despertar de la kundalini,",
            "que sus maestros enseñan a recorrer despacio y acompañado."))

    e.seccion("SÍNTOMAS DEL GIRO ACELERADO DEL ALMA", SEC(
        "CÓMO SE SIENTE CUANDO EL GIRO SE ACELERA",
        UL("Sientes que el tiempo se acelera",
           "Las coincidencias llaman tu atención",
           "Todo te toca más hondo",
           "Aparece una alegría sin motivo",
           "Necesitas tierra: dormir, comer, caminar",
           lead="Cuando tu alma acelera su giro:"),
        P("Si el giro se vuelve noches sin sueño, pensamientos que corren o la certeza de una misión urgente, no es el alma "
          "que acelera: es el momento de pedir ayuda, esa misma semana. Y un mareo o un calor que no ceden se consultan "
          "con un médico.")))

    e.seccion("EL SPIN ENTRELAZADO", SEC(
        "EL GIRO COMPARTIDO",
        UL("El de las personas que amas",
           "El de la Tierra, que da una vuelta cada día y te marca el sueño y la vigilia",
           "El del año alrededor del Sol, que trae las estaciones",
           "El de la galaxia, que el Sol recorre en unos doscientos treinta millones de años",
           "El del universo, que se expande",
           lead="Tu giro no está aislado. Gira dentro de otros giros:"),
        V("Cuando dos personas se enamoran, sus giros se acompasan.",
          "Cuando meditas con otros, el ritmo se comparte.",
          "Cuando alguien despierta, quienes están cerca lo notan.")))

    e.rep(P("En el centro exacto del giro del alma existe un punto de quietud absoluta:"),
          P("Los huracanes lo muestran: en el ojo el aire desciende, el viento amaina y a veces se abre el cielo, "
            "mientras alrededor gira la pared más violenta de la tormenta.") + "\n\n" +
          P("En el centro exacto del giro del alma existe un punto de quietud absoluta:"))

    e.seccion("PRÁCTICA: ACTIVANDO EL GIRO DEL ALMA", SEC(
        "PRÁCTICA: EL GIRO Y SU CENTRO",
        P("De pie, con espacio libre alrededor y algo firme al alcance de la mano, extiende los brazos y gira despacio "
          "hacia la derecha: tres vueltas, con la mirada suave. Si te mareas con facilidad, quédate sentado y deja que "
          "el torso dibuje un círculo lento."),
        V("Siente cómo tu cuerpo gira.", "Ahora siente algo más sutil:", "El giro de tu campo energético.",
          "El giro de tus emociones.", "El giro de tus pensamientos.", "El giro de tu consciencia misma."),
        V("Detente con suavidad, los pies firmes.", "Permanece quieto.", "Nota cómo algo sigue girando por dentro:",
          "el oído interno lo siente unos segundos,", "y el alma sigue su danza espiral."),
        V("Siéntate.", "Ahora encuentra el punto quieto en el centro.", "El ojo del huracán.",
          "El lugar donde no hay giro.", "Descansa ahí mientras todo gira alrededor."),
        V("Eres el giro.", "Eres la quietud.", "Eres ambos.", "Eres ninguno.")))

    e.rep("Tu destino no es linear.<br>", "Tu destino no es lineal.<br>")
    e.rep("        Una danza en la danza infinita.</p>\n",
          "        Una danza en la danza infinita.</p>\n\n" +
          P("Norbert Wiener, padre de la cibernética, lo dijo desde la ciencia: no somos una materia que permanece, "
            "sino remolinos en un río que no deja de correr, formas que se mantienen a sí mismas mientras el agua pasa.") + "\n")


# ================================================================== NODO 2
def nodo_02(e):
    e.comunes(2)
    e.rep("Cuando la vida necesita transformarte, crea un vórtice - un remolino de experiencias que te succiona, "
          "te desarma, te reorganiza y te escupe renovado del otro lado.",
          "Cuando algo en tu vida pide transformarse, aparece un vórtice: un remolino de experiencias que te arrastra, "
          "te desarma, te reorganiza y te devuelve renovado del otro lado.")
    e.rep(V("No son accidentes. No son castigos.", "Son tecnologías de transformación.",
            "Son la manera del universo de evolucionar lo que se resiste a evolucionar."),
          V("No son castigos.", "Pueden volverse transformación.",
            "Son, muchas veces, la manera en que la vida mueve lo que se resistía a moverse."))
    e.rep("<li>Sentiste que eras succionado hacia un destino inevitable</li>",
          "<li>Sentiste que eras arrastrado hacia algo que no podías detener</li>")

    # Anatomía
    e.rep("<li>Aún puedes escapar (aunque no deberías)</li>", "<li>Todavía puedes elegir cómo entrar</li>")
    e.rep("<li>Inevitabilidad haciéndose clara</li>", "<li>Lo que termina se vuelve claro</li>")
    e.rep("<li>Gratitud por la transformación</li>", "<li>Gratitud por lo que te sostuvo</li>")

    # Tipos
    e.rep(UL("Creados por deuda no resuelta", "Succionan hasta que aprendes la lección", "Se repiten si resistes",
             "Liberan cuando te rindes", "Transforman dolor en sabiduría",
             lead="<strong>Vórtices Kármicos:</strong>"),
          UL("Creados por lo que hicimos y quedó sin cerrar", "Vuelven mientras no se mira", "Se repiten si se evita",
             "Se aflojan cuando se atiende", "Pueden volver sabiduría el dolor",
             lead="<strong>Vórtices Kármicos:</strong> <em>karma</em>, en sánscrito, quiere decir acción"))
    e.rep("<li>Succionan cuando estás listo</li>\n" + L + "<li>No puedes evitarlos</li>\n" + L + "<li>Elevan tu frecuencia</li>",
          "<li>Aparecen cuando una etapa cambia</li>\n" + L + "<li>Llegan con las edades de la vida</li>\n" + L +
          "<li>Te hacen crecer</li>")
    e.rep("<li>Creados por tu alma</li>", "<li>Nacidos de tu búsqueda</li>")
    e.rep("<li>Transforman humano en divino</li>", "<li>Te devuelven a lo esencial</li>")
    e.rep("<li>Creados por campos grupales</li>", "<li>Creados por lo que vive un grupo</li>")
    e.rep(UL("Creados por fuerzas galácticas", "Portales de tiempo/espacio", "Agujeros negros de consciencia",
             "Transformación dimensional", "Transforman la realidad misma",
             lead="<strong>Vórtices Cósmicos:</strong>"),
          UL("Nacidos ante lo inmenso: un cielo estrellado, un nacimiento, la muerte de alguien cercano",
             "Te sacan de tu escala", "El tiempo se detiene", "Vuelves más pequeño y más entero",
             "Transforman la manera de mirar",
             lead="<strong>Vórtices de Asombro:</strong>"))

    # Física
    e.rep("<li>La resistencia acelera el proceso</li>", "<li>Pelear gasta la fuerza que necesitas</li>")
    e.rep("<li>El centro es inevitable</li>", "<li>Y no todo llega al fondo: el remolino tiene su hora</li>")
    e.rep("<p><strong>Presión Negativa en el Centro:</strong></p>", "<p><strong>Presión Baja en el Centro:</strong></p>")
    e.rep("<li>Genera transformación forzosa</li>", "<li>Genera el cambio</li>")
    e.rep("<li>Crea circulación perpetua</li>", "<li>Crea circulación mientras dura</li>")

    # Navegación
    e.rep("<li>Escapar prematuramente (vórtice te persigue)</li>", "<li>Huir de lo que pide ser vivido (vuelve)</li>")
    e.rep("<li>Prepárate mental/emocionalmente</li>", "<li>Prepárate por dentro</li>")
    e.rep("<li>Ancla nuevas frecuencias</li>", "<li>Asienta lo nuevo en hábitos</li>")
    e.rep(f"{I}</ol>\n\n{I}<h4>CREANDO VÓRTICES INTENCIONALES</h4>",
          f"{I}</ol>\n\n" +
          P("Hay remolinos de los que sí se sale, y cuanto antes mejor: cuando alguien te daña una y otra vez, "
            "lo sabio no es rendirse al giro sino alejarse y pedir ayuda.") + "\n\n" +
          P("Edgar Allan Poe lo contó en 1841, en «Un descenso al Maelström». Un pescador noruego cae con su barca en el "
            "gran remolino de las islas Lofoten. Su hermano se aferra a una argolla de hierro. Él, en cambio, deja que el "
            "terror se vuelva curiosidad y empieza a mirar: advierte que lo grande baja más rápido que lo pequeño y que, "
            "entre dos cosas del mismo tamaño, la cilíndrica es la que más tarda. Se ata a un barril vacío y se suelta al "
            "agua. El hermano, aferrado, se hunde con la barca. El tonel apenas desciende, y cuando llega la hora de la "
            "marea quieta, el remolino se aplaca y lo devuelve a la superficie. Se salvó el que soltó el borde y miró.") +
          f"\n\n{I}<h4>CREANDO VÓRTICES INTENCIONALES</h4>")

    e.seccion("CREANDO VÓRTICES INTENCIONALES", SEC(
        "LOS GIROS QUE PUEDES ELEGIR",
        P("No todo vórtice llega solo. Hay giros que puedes elegir:"),
        UL("Vuelve a tu dolor con tiempo y compañía", "Deja que dé las vueltas que necesita",
           "Escribe lo que aparece", "Suelta lo que ya se dijo",
           lead="<strong>Vórtice de Sanación:</strong>"),
        UL("Elige una dirección", "Da un paso por día", "Deja que lo necesario llegue a su ritmo", "Mira lo que crece",
           lead="<strong>Vórtice de Intención:</strong>"),
        UL("Gira por tu espacio", "Ordena un rincón", "Abre las ventanas", "Deja que entre el aire",
           lead="<strong>Vórtice de Orden:</strong>"),
        UL("Gira con otro ser: bailar, caminar al lado, conversar sin apuro", "Crea un campo compartido",
           "Afloja la separación", "Genera unión profunda",
           lead="<strong>Vórtice de Conexión:</strong>")))

    e.rep(P("Cada chakra es un vórtice de transformación:"),
          P("Así los describe el yoga tal como llegó a Occidente: cada chakra es un vórtice de transformación."))

    e.seccion("SÍNTOMAS DE ESTAR EN UN VÓRTICE", SEC(
        "CÓMO SE SIENTE ESTAR EN UN VÓRTICE",
        UL("Cansancio", "Sensación de ser arrastrado", "Inquietud", lead="<strong>En el cuerpo:</strong>"),
        UL("Montaña rusa emocional", "Mezcla de miedo y excitación", "Rendición que asoma",
           lead="<strong>En las emociones:</strong>"),
        UL("Pensamientos que dan vueltas", "Claridad súbita tras la confusión", "Comprensiones que llegan de golpe",
           lead="<strong>En la mente:</strong>"),
        UL("Sensación de destino", "Coincidencias que llaman la atención", "Tiempo elástico", "Presencia intensificada",
           lead="<strong>En lo espiritual:</strong>"),
        P("Un vórtice se atraviesa con el cuerpo cuidado. El mareo, el agotamiento que no cede o una energía que no deja "
          "dormir se consultan con un médico; y si la realidad empieza a sentirse ajena, como detrás de un vidrio, "
          "se pide ayuda esa misma semana.")))

    e.seccion("EL VÓRTICE GLOBAL ACTUAL", SEC(
        "EL VÓRTICE DE ESTE TIEMPO",
        P("Muchos sienten hoy que el mundo gira cada vez más rápido: crisis que se encadenan, noticias sin respiro, "
          "posiciones que se alejan unas de otras. Nadie conoce el rumbo de este giro. Pero quien atravesó un vórtice "
          "sabe dónde buscar el centro."),
        V("No es el fin del mundo.", "Es un tiempo que pide ojos quietos.", "Cada persona que encuentra el suyo",
          "le da al remolino un lugar donde aquietarse.")))

    e.rep("<li>Shamanes que viajan entre mundos</li>", "<li>Chamanes que viajan entre mundos</li>")
    e.rep("<li>No temen al caos</li>", "<li>Respetan el caos sin temerle</li>")
    e.rep("<li>Crean vórtices conscientemente</li>", "<li>Saben cuándo no entrar</li>")

    e.seccion("TECNOLOGÍA AVANZADA DE VÓRTICES", "")

    e.seccion("PRÁCTICA: CREANDO UN VÓRTICE DE TRANSFORMACIÓN PERSONAL", SEC(
        "PRÁCTICA: CREANDO UN VÓRTICE DE TRANSFORMACIÓN PERSONAL",
        P("Identifica qué está cambiando en tu vida, aunque todavía no sepas hacia dónde."),
        V("De pie, en un lugar amplio, camina en círculo, despacio.", "Primera vuelta: reconoce lo que está terminando.",
          "Segunda vuelta: acepta lo que todavía no sabes.", "Tercera vuelta: mira lo que sigue en pie."),
        V("Camina luego en espiral hacia el centro, sin apurar el paso.", "Párate ahí.", "Completamente quieto."),
        P("Declara: “Me rindo a la transformación.”"),
        V("Siente el vórtice girando a tu alrededor.", "No tienes que hacer nada con él.", "Desde el centro, solo mira."),
        V("Cuando estés listo, camina hacia afuera en espiral.", "Vuelta tras vuelta.", "Integrando.", "Emergiendo."),
        V("Algo se movió.", "La transformación ya empezó, a su ritmo.", "Lo viejo se despide en el centro.",
          "Lo nuevo nace en la espiral.")))

    e.seccion("EL REGALO DEL VÓRTICE", SEC(
        "EL REGALO DEL VÓRTICE",
        UL("Una transformación que no habrían emprendido solos", "Un crecimiento que nadie les pidió",
           "Un renacimiento", "Una liberación", "Un yo más amplio",
           lead="Ninguna crisis se elige, y ninguna se desea. Pero muchos encuentran, del otro lado, "
                "un regalo que no buscaban:"),
        P("Sin vórtices, nada cambiaría de lugar. Quien sale de uno a veces lo dice así: "
          "fue como si la vida se negara a dejarme pequeño.")))

    e.rep("Son el camino mismo, girando hacia tu transformación inevitable.”",
          "Son el camino mismo, girando hacia tu transformación.”")
    e.rep(FIRMA, FIRMA + "\n\n" + puerta_arquitectura(
        "Del otro lado, en <em>El Peso</em>, un viejo nada en una catarata donde ni los peces se atreven: "
        "entra con el remolino hasta el centro y sale con el agua que vuelve a subir.",
        BASE_ARQ + "libro-08-el-peso/L08-U6.html"))


# ================================================================== NODO 3
def nodo_03(e):
    e.comunes(3)
    e.rep('<h1 class="node">Nodo 3 · Espirales de ADN Activándose</h1>', '<h1 class="node">Nodo 3 · La Doble Hélice</h1>')

    e.seccion("EL CÓDIGO VIVIENTE EN ESPIRAL", SEC(
        "EL CÓDIGO VIVIENTE EN ESPIRAL",
        P("Tu ADN no es solo una molécula. Es una escalera que se retuerce en doble hélice, la forma que Rosalind Franklin "
          "fotografió y que James Watson y Francis Crick describieron en 1953. Cada peldaño es una letra en el alfabeto de "
          "la vida. Cada tres letras, una palabra. Cada gen, una frase. Y todo el genoma junto es la biblioteca de "
          "Alejandría de tu potencial, esperando ser leída y expresada."),
        P("Y aquí está lo que la ciencia de las últimas décadas confirmó: la secuencia que heredaste cambia poco a lo largo "
          "de tu vida, pero su lectura no está fija. Qué genes hablan y cuáles callan depende también de lo que vives. "
          "Lo llaman epigenética. En 2004, el equipo de Michael Meaney lo vio en ratas: las crías que sus madres lamían y "
          "acicalaban más mostraban marcas distintas en un gen que regula el estrés, y crecían más serenas. "
          "Tu ADN es un texto antiguo que se lee de una manera viva."),
        P("Has sentido que la vida te escribe por dentro cuando:"),
        UL("Una experiencia profunda te cambió hasta el cuerpo",
           "Un hábito nuevo, sostenido, te volvió otra persona",
           "Tu manera de percibir se amplió y no volvió atrás",
           "Aprendiste algo que creías imposible para ti",
           "Supiste que algo fundamental había cambiado")))

    e.seccion("LA ESTRUCTURA MULTIDIMENSIONAL DEL ADN", SEC(
        "LA ESTRUCTURA DE LA ESPIRAL",
        UL("Dos hebras que se enroscan una en torno a la otra y corren en sentidos opuestos",
           "Unidas por pares de letras que siempre se eligen igual: A con T, C con G",
           "Cada hebra es el molde de la otra: por eso la vida puede copiarse",
           "Unos tres mil millones de pares de letras en cada juego de cromosomas",
           "Estirado, el ADN de una sola célula mediría unos dos metros"),
        V("Dos hebras que se abrazan sin confundirse", "y que, al separarse,", "dan origen a dos abrazos nuevos:",
          "una imagen del amor", "escrita en cada célula.")))

    e.seccion("EL LENGUAJE DE LUZ DEL ADN", SEC(
        "LO QUE TU ADN ESCUCHA",
        UL("La luz: la de la mañana pone en hora los relojes de cada célula",
           "El movimiento: el ejercicio modifica lo que se expresa en el músculo",
           "El sueño: una semana durmiendo poco altera cientos de lecturas",
           "El cuidado y los vínculos: el afecto deja huella, como en las crías de Meaney",
           "La quietud: la meditación, según los primeros estudios, aquieta genes ligados a la inflamación",
           "Y también el estrés que no cede, que deja sus propias marcas",
           lead="La lectura de tus genes responde a:"),
        P("Lo que tu ADN escucha es la vida que llevas.")))

    e.seccion("EL 97% “BASURA” - EL TESORO OCULTO", SEC(
        "EL ADN “BASURA”: EL TESORO ESCONDIDO",
        P("Menos del dos por ciento de tu genoma escribe proteínas. Al resto, durante años, se lo llamó “ADN basura”; "
          "la expresión la popularizó en 1972 el genetista Susumu Ohno. Hoy se sabe que una parte de ese material trabaja: "
          "hay interruptores que encienden y apagan genes, regiones que deciden cuándo y dónde se lee cada frase, restos de "
          "virus antiguos que la evolución domesticó; uno de ellos ayuda a formar la placenta. Cuánto de él cumple una "
          "función sigue en discusión."),
        V("Lo que parecía sobrante", "resultó ser, en parte, gramática:", "no las palabras,",
          "sino el orden en que se dicen.")))

    e.seccion("LOS CAMPOS DE TORSIÓN DEL ADN", SEC(
        "LA TORSIÓN DEL ADN",
        P("En tu ADN, la torsión es literal. Cuando la doble hélice se abre para ser leída o copiada, por delante de la "
          "abertura se retuerce de más, como un cordel que se enrosca sobre sí mismo. Si nada la aflojara, la lectura se "
          "detendría. Unas enzimas, las topoisomerasas, hacen ese trabajo: cortan una hebra o las dos, dejan que el giro "
          "se suelte y vuelven a unirlas. Sin descanso, en cada célula, algo afloja la tensión para que la vida pueda leerse."),
        UL("<strong>En la célula:</strong> se copia entera antes de cada división, y unas enzimas reparadoras corrigen "
           "sus errores sin pausa",
           "<strong>En el cuerpo:</strong> el mismo texto, leído de maneras distintas, hace una neurona, una célula de la "
           "piel, una fibra del corazón",
           "<strong>En la especie:</strong> guarda la memoria de los que vinieron antes",
           lead="Y la espiral sostiene más:")))

    e.seccion("ACTIVACIÓN CONSCIENTE DEL ADN", SEC(
        "CUIDAR LO QUE SE LEE",
        UL("<strong>Descanso:</strong> horarios regulares, la luz de la mañana, la oscuridad de la noche",
           "<strong>Movimiento:</strong> caminar, bailar, lo que tu cuerpo agradezca",
           "<strong>Vínculo:</strong> tiempo con quienes te cuidan y con quienes cuidas",
           "<strong>Quietud:</strong> unos minutos de silencio cada día",
           lead="Lo que tu cuerpo lee cada día es tu vida. Se cuida en cuatro gestos:"),
        P("Paciencia con el proceso: la lectura cambia despacio. Y cuando el cuerpo habla —un hormigueo que no cede, "
          "un dolor que migra, un cambio de apetito o de sueño—, se lo escucha con un médico al lado.")))

    e.seccion("SÍNTOMAS DE ACTIVACIÓN DEL ADN", "")

    e.rep(UL("<strong>Desafinado:</strong> Enfermedad y limitación", "<strong>Afinado:</strong> Salud y vitalidad",
             "<strong>Resonando:</strong> Capacidades activadas", "<strong>Cantando:</strong> Genio expresado",
             "<strong>En sinfonía:</strong> Consciencia crística", lead="Cuando tu ADN está:"),
          P("En 1986, catorce años después de hablar de “basura”, Susumu Ohno lo tomó al pie de la letra: con su esposa, "
            "Midori, asignó notas a las letras del ADN y escuchó. El gen de una enzima que ayuda a descomponer el azúcar "
            "le sonó como una canción de cuna.") + "\n\n" +
          P("Y como toda partitura, la tuya se interpreta: el mismo texto suena distinto según la vida que lo toca."))

    e.seccion("EL ADN COLECTIVO", SEC(
        "EL ADN COMPARTIDO",
        UL("El de tu familia: la mitad de tu texto llegó de cada uno de tus padres",
           "El de tu especie: con cualquier otro ser humano compartes casi todas las letras",
           "El de toda vida en la Tierra: el mismo alfabeto de cuatro letras escribe al roble, a la ballena y a ti",
           "El de los que vinieron antes: en tus células viaja la historia de migraciones antiguas",
           lead="Tu ADN no está aislado. Está emparentado con:"),
        V("Lo que recibiste no termina en ti.", "Lo que cuidas pasa a otros:", "no siempre en los genes,",
          "sí en los gestos,", "en el tono de una casa,", "en la manera de mirar.")))

    e.seccion("TECNOLOGÍA DE ACTIVACIÓN POR SONIDO", SEC(
        "PARA HABITAR EL SONIDO",
        P("<strong>Práctica: Canto de las Cinco Vocales</strong>"),
        V("Siéntate con la columna erguida.", "Imagina tu doble hélice desde la base hasta la coronilla.", "Respira hondo."),
        P("Entona estas vocales, una por respiración, y deja que cada sonido dure toda la salida del aire:"),
        V("“AHHH” por tu cuerpo", "“EEEE” por lo que sientes", "“IIII” por lo que piensas", "“OOOO” por lo que buscas",
          "“UUUU” por lo que te sostiene"),
        V("Repite el ciclo tres veces.", "Siente cómo vibra el pecho.", "Cómo se alarga la respiración.",
          "Cómo cada célula, aunque no la oigas, participa del canto.")))

    e.seccion("LA ESPIRAL FIBONACCI EN TU ADN", SEC(
        "LA ESPIRAL Y SUS NÚMEROS",
        P("La doble hélice mide unos 20 angstroms de ancho y da una vuelta completa cada 34: una relación cercana a 1.7, "
          "vecina de la proporción dorada sin ser ella. La serie de Fibonacci sí está en los girasoles y en las piñas de "
          "los pinos, cuyas espirales se cuentan en pares como 21 y 34, u 8 y 13."),
        V("La espiral no necesita un número exacto para ser bella:", "la tuya se lee,", "se copia,", "se repara,",
          "y eso basta para el asombro.")))

    e.seccion("EL FUTURO DEL ADN HUMANO", SEC(
        "EL FUTURO DEL ADN HUMANO",
        P("En 2003 se terminó de leer casi todo el genoma humano; en 2022, por primera vez, de un extremo al otro. "
          "Hoy se aprende a corregir algunas de sus erratas, las que causan enfermedades graves."),
        V("No es ciencia ficción.", "Está sucediendo ahora.", "Y pide algo que ninguna técnica trae consigo:",
          "la sabiduría para usarla.")))

    e.seccion("LA RESPONSABILIDAD DEL ADN ACTIVADO", SEC(
        "LA RESPONSABILIDAD DE LO RECIBIDO",
        UL("Eres guardián de un código que no inventaste",
           "Tu ánimo afecta a otros",
           "Tus hábitos conversan con tu cuerpo",
           "Tu cuidado acompaña a quienes crecen cerca de ti",
           "Eres un eslabón de una cadena que sigue después de ti",
           lead="Con lo recibido viene una responsabilidad:"),
        UL("Cuidar (a ti y a otros)", "Elevar (el tono de tus lugares)", "Crear (lo que todavía no existe)",
           "Servir (a la vida que continúa)", "Amar (incondicionalmente)",
           lead="Usa lo que eres para:")))

    e.rep(V("Existe un código maestro en tu ADN:", "El código del amor incondicional.",
            "Cuando lo activas, todo lo demás se activa.", "Es la llave maestra.", "El password universal.",
            "El “ábrete sésamo” de tu potencial."),
          V("Existe un código maestro,", "y no está escrito en ninguna célula:", "el del amor incondicional.",
            "Cuando lo vives, todo lo demás se ordena.", "Es la llave maestra.", "La contraseña universal.",
            "El “ábrete sésamo” de tu potencial."))
    e.rep("cómo las hebras se encienden,<br>\n" + I + "cómo los códigos se activan,<br>",
          "cómo la vida se lee en ti con otra voz,<br>")
    e.rep("activando el cielo<br>\n" + I + "en la Tierra<br>", "trayendo el cielo<br>\n" + I + "a la Tierra<br>")
    e.rep("Cada peldaño que activas te acerca más a tu naturaleza divina.",
          "Cada peldaño que habitas te acerca más a tu naturaleza divina.")


# ================================================================== NODO 4
def nodo_04(e):
    e.comunes(4)
    e.rep(P("Tu corazón no es una bomba. Es un vórtice. No solo mueve sangre - mueve realidad. Con cada latido, genera "
            "campos de torsión que se extienden más allá de tu cuerpo, más allá de esta dimensión, tocando e influenciando "
            "todo en el universo. El campo electromagnético de tu corazón es 5000 veces más fuerte que el de tu cerebro. "
            "Pero los campos de torsión de tu corazón son infinitamente más poderosos - son los que doblan el espacio-tiempo, "
            "atraen sincronicidades, y literalmente crean tu mundo."),
          P("Tu corazón no es solo una bomba. Es un vórtice. En cada latido, el ventrículo izquierdo se retuerce: visto "
            "desde la punta, la base gira en el sentido de las agujas del reloj y la punta en el contrario, como quien "
            "escurre un paño. Al soltarse, esa torsión aspira la sangre del latido siguiente, y la que entra forma dentro "
            "un remolino anular que la orienta hacia la salida. Leonardo da Vinci, hacia 1513, ya había dibujado los "
            "torbellinos de la sangre junto a la válvula aórtica; más de cuatro siglos después, los experimentos y la "
            "resonancia magnética los encontraron donde él los puso.") + "\n\n" +
          P("Y no solo mueve sangre. Su campo eléctrico es el más intenso del cuerpo: llega a la piel de las muñecas y los "
            "tobillos, y por eso existe el electrocardiograma."))
    e.rep("<li>Sentiste el corazón de otro a distancia</li>", "<li>Pensaste en alguien lejano y se te llenó el pecho</li>")
    e.rep("<li>Tu amor cambió literalmente la atmósfera de un lugar</li>", "<li>Tu amor cambió la atmósfera de un lugar</li>")

    e.seccion("LA GEOMETRÍA TOROIDAL DEL CORAZÓN", SEC(
        "LA GEOMETRÍA TOROIDAL DEL CORAZÓN",
        UL("Gira hacia adentro por el frente", "Sale por la espalda", "Vuelve a entrar por el frente",
           "Crea una circulación que no cesa mientras vives", "Sostiene tu centro",
           lead="Imagina el campo de tu corazón como un anillo de luz, con la forma de un anillo de humo, "
                "que sale y vuelve a entrar:"),
        UL("Se abre cuando amas", "Se ensancha en la confianza", "Se encoge con el miedo",
           "Se cierra cuando algo duele demasiado", "Y con el tiempo vuelve a abrirse",
           lead="Ese anillo respira con lo que sientes:"),
        P("Es tu manera de estar entre otros. Lo que tu corazón siente se asoma al gesto y a la voz, "
          "y quienes se acercan lo perciben.")))

    e.seccion("LOS RITMOS DE TORSIÓN CARDÍACA", SEC(
        "LOS RITMOS DEL CORAZÓN",
        P("Tu corazón tiene múltiples ritmos:"),
        UL("Mueve sangre", "Mantiene vida biológica", "Crea pulso electromagnético", "Base de todos los otros ritmos",
           lead="<strong>Ritmo Físico:</strong> 60-100 latidos/minuto"),
        UL("Acelera con excitación", "Desacelera con calma", "Se agita con el miedo", "Se calma con el afecto",
           "Crea el clima emocional",
           lead="<strong>Ritmo Emocional:</strong> Variable"),
        UL("Se acompasa con el de quienes están cerca", "En un coro, en un ritual, en un abrazo largo",
           "Sin palabras", "Sin proponérselo",
           lead="<strong>Ritmo Compartido:</strong> Con los otros"),
        UL("Empezó a latir unas semanas después de la concepción",
           "Late unos tres mil millones de veces en una vida larga",
           "Se aquieta en el sueño",
           "Baja su ritmo de la infancia a la adultez",
           lead="<strong>Ritmo de la Vida Entera:</strong> De principio a fin")))

    e.seccion("LA COHERENCIA CARDÍACA", SEC(
        "LA COHERENCIA CARDÍACA",
        P("Cuando respiras despacio, unas seis veces por minuto, el pulso empieza a subir y bajar con el aire en una ola "
          "suave y regular: se acelera un poco al inhalar y se aquieta al soltar. Los investigadores la llaman coherencia, "
          "o respiración de resonancia, y la estudian desde hace décadas."),
        OL("Respira como si el aire entrara y saliera por el pecho",
           "Inhala en cuatro tiempos y suelta en seis",
           "Trae un sentimiento cálido (gratitud, cariño, compasión)",
           "Mantén de tres a cinco minutos",
           "Deja que el ritmo se asiente solo",
           lead="Cómo crear coherencia:"),
        UL("Te serenas", "El pensamiento se aclara",
           "La ansiedad baja, según los estudios de biorretroalimentación", "Escuchas mejor", "Vuelves al centro",
           lead="En coherencia cardíaca:")))

    e.seccion("EL CORAZÓN COMO CEREBRO", SEC(
        "EL CORAZÓN COMO CEREBRO",
        P("Tu corazón tiene su propia red de neuronas: unas cuarenta mil en un adulto, según el recuento de Dainius Pauza "
          "en 2000, y más del doble en los niños. J. Andrew Armour la llamó el “pequeño cerebro del corazón”. Ajusta el "
          "latido por su cuenta, sin esperar órdenes. Por el nervio vago, que lo une al cerebro, la mayoría de las fibras "
          "suben en lugar de bajar. Y lo que el corazón hace se vuelve sentimiento: Antonio Damasio llamó marcadores "
          "somáticos a esas señales del cuerpo que tiñen las decisiones."),
        UL("Siente antes de pensar", "Sabe sin argumentos", "Ama sin razón", lead="Por eso el corazón:"),
        P("Pascal lo escribió en sus <em>Pensamientos</em>: el corazón tiene razones que la razón no conoce.")))

    e.rep("el corazón se convierte en stargate.</p>", "el corazón se vuelve una puerta abierta.</p>")

    e.rep("<h4>EL LENGUAJE DEL CAMPO TORSIONAL CARDÍACO</h4>", "<h4>EL LENGUAJE DEL CORAZÓN</h4>")
    e.rep(P("Aprende a leer tu campo cardíaco. Es tu GPS multidimensional. Tu brújula cuántica. Tu guía infalible."),
          P("Aprende a leer tu corazón. Es tu brújula interior: no decide por ti, pero te dice hacia dónde mirar. "
            "Y cuando el pecho aprieta, duele o el latido se desboca sin motivo, la brújula pide un médico, "
            "no una interpretación."))

    e.rep("<h4>TECNOLOGÍA DE ACTIVACIÓN DEL VÓRTICE CARDÍACO</h4>", "<h4>PARA HABITAR EL CORAZÓN</h4>")
    e.rep("<p><strong>Ejercicio: Activación del Toroide Maestro</strong></p>",
          "<p><strong>Ejercicio: El Anillo de Luz</strong></p>")
    e.rep("Con cada respiración, gira más rápido.", "Con cada respiración, gira a su ritmo.")
    e.rep(P("Acelera el flujo. Siente el campo de torsión expandiéndose. Girando. Atrayendo. Creando."),
          P("Deja que el flujo encuentre su ritmo: cuatro tiempos al tomar aire, seis al soltarlo. "
            "Siente el anillo expandiéndose. Girando. Abrazando. Creando."))
    e.rep(" Bendice todo lo que toca. Transforma todo lo que encuentra.</p>", " Bendice todo lo que toca.</p>")
    e.rep(P("Mantén por 5 minutos. Eres un vórtice de amor. Tu corazón está creando realidad."),
          P("Mantén cinco minutos. Eres un vórtice de amor. Tu corazón está dando forma a este momento."))

    e.seccion("EL CORAZÓN COLECTIVO", SEC(
        "EL CORAZÓN COLECTIVO",
        UL("Se acompasa con otros corazones", "Forma redes de calma", "Crea atmósferas de grupo",
           "Toca el ánimo de una comunidad", "Participa del pulso de todo lo vivo",
           lead="Tu corazón no late solo:"),
        P("Se ha medido: en un coro, los corazones de los cantores se aceleran y se frenan juntos, guiados por la "
          "respiración del canto; en un pueblo de Soria, la noche de San Juan, los allegados de quien cruza las brasas "
          "laten con él, y los visitantes que no lo conocen, no."),
        UL("El miedo circula menos", "Quien llega agitado encuentra dónde calmarse",
           "Un grupo puede sostener a uno de los suyos", "La realidad compartida cambia de tono",
           "La ternura se vuelve contagiosa",
           lead="Cuando muchos corazones se aquietan juntos:"),
        P("Ese es el poder de la meditación en grupo, de la oración en común, del amor de muchos.")))

    e.seccion("SANACIÓN A TRAVÉS DEL CAMPO TORSIONAL CARDÍACO", SEC(
        "ACOMPAÑAR DESDE EL CORAZÓN",
        OL("Entra en coherencia",
           "Piensa en quien necesita compañía",
           "Siente afecto por esa persona",
           "Desea su bien con palabras simples: que estés en paz, que no te sientas solo",
           "No fuerces: solo ama",
           "Y después, si puedes, haz algo: una llamada, una visita, un mensaje",
           "Suelta y confía",
           lead="Tu corazón acompaña cualquier tratamiento y no lo reemplaza, pero puede estar con quien sufre, "
                "cerca o lejos. La tradición budista lo llama <em>metta</em>: desear el bien."),
        P("Tu amor ES compañía. Tu calma ES refugio. Tu presencia ES el vehículo.")))

    e.seccion("EL CORAZÓN COMO PORTAL", SEC(
        "EL CORAZÓN COMO PORTAL",
        UL("Portal entre tiempos", "Portal entre almas", "Portal hacia la Fuente",
           lead="En estados de amor profundo, el corazón se convierte en portal:"),
        UL("Trascender la muerte", "Unir a través de distancias", "Consolar lo que no se cura", "Abrir el cielo",
           lead="Por eso el amor puede:")))

    e.seccion("EL CORAZÓN DEL FUTURO", SEC(
        "EL CORAZÓN DEL FUTURO",
        UL("La calma compartida", "La conversación de corazón a corazón", "Decisiones que escuchen también al cuerpo",
           "Técnicas al servicio del cuidado", "Una civilización del corazón",
           lead="Muchos sueñan con una humanidad que aprenda:"),
        P("El corazón ya se mide: el electrocardiograma tiene más de un siglo, y la variación del pulso se usa hoy en la "
          "medicina y en el deporte."),
        P("Pero no necesitas esperar. Tu corazón ya sabe hacerlo. Ya es este portal. Ya es esta fuerza.")))

    e.rep("<li>A sanar con tu campo</li>", "<li>A cuidar desde tu calma</li>")
    e.rep("Cada respiración, una activación.", "Cada respiración, un regreso.")
    e.rep(P("Y observa cómo tu mundo") + "\n\n" + I + "<ul>\n" + L + "<li>y el mundo -<br>\n" +
          "            gira hacia el amor<br>\n            latido a latido,<br>\n            vórtice a vórtice,<br>\n"
          "            corazón<br>\n            a<br>\n            corazón.</li>\n" + I + "</ul>",
          V("Y observa cómo tu mundo", "—y el mundo—", "gira hacia el amor", "latido a latido,", "vórtice a vórtice,",
            "corazón", "a", "corazón."))

    e.rep(FIRMA, FIRMA + "\n\n" + puerta_portal(
        "Del otro lado, en <em>Los muchos</em>, la historia completa: quince estudiantes que cantan en Gotemburgo "
        "y un pueblo que mira a los suyos cruzar el fuego.",
        BASE_PORTAL + "35_Los_Muchos/umbral-03.html"))


# ================================================================== NODO 5
def nodo_05(e):
    e.comunes(5)
    e.rep('<h1 class="node">Nodo 5 · La Geometría del Spin</h1>', '<h1 class="node">Nodo 5 · La Geometría del Espín</h1>')
    e.rep(P("El universo no está hecho de partículas. Está hecho de giros. Cada “cosa” que percibes es en realidad un "
            "patrón de spin en el campo unificado. Y estos spins no giran aleatoriamente - siguen geometrías precisas, "
            "sagradas, que determinan qué tipo de realidad manifiestan. Desde el spin del electrón hasta el giro de las "
            "galaxias, todo obedece a las mismas leyes geométricas de rotación. Y tú, conscientemente o no, estás "
            "constantemente creando y navegando estas geometrías giratorias."),
          P("Para la física de hoy, lo que llamamos partículas son vibraciones de campos que llenan el espacio, y cada una "
            "lleva su espín, su giro propio. Del electrón a las galaxias, el universo está poblado de formas que giran y de "
            "simetrías que las ordenan. Y tú, sabiéndolo o no, también trazas tu vida con figuras que se repiten y que "
            "puedes aprender a mirar."))
    e.rep("La geometría del spin es el lenguaje secreto de la creación.<br>",
          "La geometría del espín es el lenguaje secreto de la creación.<br>")
    e.rep("Es cómo tú tejes tu realidad, giro por giro.</p>", "Es cómo tú tejes tus días, giro por giro.</p>")
    e.rep("<p>Has experimentado la geometría del spin cuando:</p>", "<p>Has experimentado la geometría del espín cuando:</p>")

    # Sólidos platónicos
    e.rep(P("Los bloques constructores de la realidad son cinco formas que, al girar, crean todo:"),
          P("Platón, en el <em>Timeo</em>, imaginó que los cuatro elementos estaban hechos de cuatro de estas cinco formas, "
            "y que el dios usó la quinta para el todo. Tómalas como un mapa de cualidades:"))
    for cualidad in ("Transformación", "Estabilización", "Equilibrio", "Flujo", "Ascensión"):
        e.rep(f"<li>Spin: {cualidad}</li>", f"<li>Giro: {cualidad}</li>")
    e.rep("<li>Crea: Estructura, foundation, materia</li>", "<li>Crea: Estructura, cimiento, materia</li>")
    e.rep(f"{L}<li>Cuando giras un dodecaedro: Accedes a lo cósmico</li>\n{I}</ul>\n",
          f"{L}<li>Cuando giras un dodecaedro: Accedes a lo cósmico</li>\n{I}</ul>\n\n" +
          P("Kepler, en 1596, encajó los cinco sólidos entre las órbitas de los planetas y creyó haber visto el plano del "
            "cielo. Años después, cuando las observaciones de Tycho Brahe le mostraron que Marte no seguía un círculo, por "
            "una diferencia de ocho minutos de arco, aceptó la elipse. La geometría más bella no es la que se impone: "
            "es la que se deja corregir por lo real.") + "\n")

    # Espiral sagrada
    e.rep("<p>La espiral es la geometría maestra del spin:</p>", "<p>La espiral es la geometría maestra del espín:</p>")
    e.rep("<li>Aparece en: Conchas, galaxias, huracanes, ADN</li>",
          "<li>Aparece en: girasoles, piñas de los pinos, la disposición de las hojas en un tallo</li>")
    e.rep("<li>La proporción más bella del universo</li>\n" + L + "<li>Aparece en: Tu rostro, tus manos, tu corazón</li>",
          "<li>La proporción que Luca Pacioli llamó divina</li>\n" + L +
          "<li>Aparece en: el pentágono y la estrella de cinco puntas</li>")
    e.rep("<li>Aparece en: Nautilus, galaxias, tornados</li>",
          "<li>Aparece en: el nautilo, los brazos de las galaxias, las bandas de los huracanes</li>")

    e.seccion("EL MERKABA - LA GEOMETRÍA DEL SPIN MAESTRO", "")

    # Práctica geométrica
    e.rep("<h4>TECNOLOGÍA DE GEOMETRÍA GIRATORIA</h4>", "<h4>PARA HABITAR LA GEOMETRÍA</h4>")
    e.rep("<li>Manifestación → Cubo</li>", "<li>Estabilidad → Cubo</li>")
    e.rep("<li>Luego más rápido</li>", "<li>Luego a tu ritmo</li>")
    e.rep("<li>Siente el campo de torsión</li>", "<li>Siente cómo te acompaña</li>")
    e.rep("<li>Pero mantén el spin</li>", "<li>Pero conserva su cualidad</li>")

    e.seccion("LOS CROP CIRCLES - GEOMETRÍAS DE ACTIVACIÓN", "")

    e.rep("<h4>LA GEOMETRÍA FRACTAL DEL SPIN</h4>", "<h4>LA GEOMETRÍA FRACTAL DEL ESPÍN</h4>")
    e.rep("<li>Enseña: Los límites son ilusorios</li>", "<li>Enseña: Un límite puede contener lo infinito</li>")

    # Pensamientos
    e.rep("<li>Ascensión de comprensión</li>", "<li>Comprensión que se eleva</li>")
    e.rep(f"{L}<li>Ver patrones en todo</li>\n{I}</ul>\n",
          f"{L}<li>Ver patrones en todo</li>\n{I}</ul>\n\n" +
          P("La psicología encontró algo parecido. En 2003, Treynor, Gonzalez y Nolen-Hoeksema distinguieron dos maneras "
            "de volver sobre lo que duele. Una gira en círculo alrededor del “¿por qué siempre me pasa esto?” y oscurece "
            "el ánimo; la otra vuelve para comprender, como una espiral, y con el tiempo lo alivia. Y cuando el círculo "
            "ocupa los días y no deja dormir, se busca compañía para salir de él.") + "\n")

    # Meditación
    e.rep("<h4>PRÁCTICA: MEDITACIÓN DEL SPIN GEOMÉTRICO</h4>", "<h4>PRÁCTICA: MEDITACIÓN DEL ESPÍN GEOMÉTRICO</h4>")
    e.rep("Donde todo spin se origina. Donde tú eres el geómetra de tu realidad.</p>",
          "Donde todo giro se origina. Donde aprendes a trazar tus días con formas que no inventaste.</p>")

    # Tiempo
    e.rep(UL("Futuro fluyendo hacia pasado", "Pasado creando futuro", "Geometría de la simultaneidad",
             lead="<strong>Tiempo Toroidal:</strong> Un toroide"),
          UL("Lo vivido vuelve a ti transformado", "El pasado alimenta lo que viene",
             "Lo que esperas del futuro cambia cómo recuerdas el pasado", "Geometría del regreso",
             lead="<strong>Tiempo Toroidal:</strong> Un toroide"))

    e.seccion("LA NUEVA GEOMETRÍA HUMANA", SEC(
        "LA NUEVA GEOMETRÍA HUMANA",
        UL("De lineal a multidimensional", "De separada a interconectada", "De estática a dinámica",
           "De euclidiana a fractal", "De simple a compleja",
           lead="Una geometría más amplia está al alcance de cualquiera:"),
        P("Y no hay que esperar a nadie para empezar: todos los niños nacen geómetras. Antes de hablar ya distinguen "
          "formas, siguen con la mirada lo que gira y encuentran patrones donde nadie se los mostró. "
          "Esa geometría sigue en ti.")))

    e.seccion("EL SPIN MASTER", SEC(
        "EL GEÓMETRA",
        UL("Puedes cambiar tu manera de vivir cambiando de forma",
           "Puedes resolver problemas mirándolos desde otra figura",
           "Puedes ordenar lo que estaba en caos",
           "Puedes construir con las formas correctas",
           "Puedes crecer complejizando tu mirada",
           lead="Cuando aprendes a mirar las formas de tu vida:"),
        P("No eres víctima de la geometría de tu vida. Eres su arquitecto. Eres su geómetra: trazas con formas que no "
          "inventaste. Eliges qué cuidas, cómo te mueves, hacia dónde miras.")))

    e.rep("<li>Crear campos de torsión intencionales</li>", "<li>Elegir hacia dónde giras</li>")
    e.rep("Cada respiración, un nuevo spin.", "Cada respiración, un nuevo giro.")
    e.rep("Es patrones de spin manifestándose.", "Son patrones de giro que se despliegan.")
    e.rep("Cambia la geometría, cambia el spin, cambia tu mundo.", "Cambia la geometría, cambia el giro, cambia tu mundo.")
    e.rep("<p>En el centro de todo spin existe el punto cero:</p>", "<p>En el centro de todo giro existe el punto cero:</p>")
    e.rep("<li>¿Cómo puedes reconfigurar el spin?</li>", "<li>¿Cómo puedes reconfigurar el giro?</li>")


def pasos(*grupos, lead=None):
    """Lista numerada con sublistas, como la del original: (título, [ítems])."""
    s = (P(lead) + "\n\n") if lead else ""
    s += f"{I}<ol>\n"
    for titulo, items in grupos:
        s += f"{L}<li><strong>{titulo}</strong>\n{L}  <ul>\n"
        s += "".join(f"{L}    <li>{x}</li>\n" for x in items)
        s += f"{L}  </ul>\n{L}</li>\n"
    return s + f"{I}</ol>"


# ================================================================== NODO 6
def nodo_06(e):
    e.comunes(6)
    e.rep(P("Tu realidad no es sólida. Es un remolino de probabilidades colapsando en experiencia momento a momento. "
            "Cada evento de tu vida es un vórtice donde las líneas de posibilidad convergen, giran, y cristalizan en lo que "
            "llamas “real”. Y tú, querido creador, eres quien está generando estos remolinos - con tus pensamientos, "
            "emociones, expectativas y sobre todo, con los campos de torsión de tu consciencia.") + "\n\n" +
          P("Mira a tu alrededor. Todo lo que ves fue primero un remolino en el campo de potencial. Tu casa, tu trabajo, "
            "tus relaciones, tu cuerpo mismo - todos comenzaron como vórtices de posibilidad que alguien (tú) hizo girar "
            "hasta que se densificaron en forma. Y ahora mismo, en este instante, estás creando los remolinos que serán "
            "tu mañana."),
          P("Tu realidad no es sólida. Es un remolino de posibilidades que cristaliza en experiencia momento a momento. "
            "Cada evento de tu vida es un vórtice donde las líneas de posibilidad convergen, giran y se vuelven lo que "
            "llamas “real”. Y tú participas de esos remolinos con tus pensamientos, tus emociones, tus expectativas y, "
            "sobre todo, con aquello que alimentas con tu atención.") + "\n\n" +
          P("Mira a tu alrededor. Mucho de lo que ves empezó como un remolino de posibilidad: tu casa, tu trabajo, tus "
            "vínculos. Algunos los hiciste girar tú; otros los movieron muchas manos antes que las tuyas; otros llegaron "
            "sin que nadie los llamara. Y ahora mismo, en este instante, participas de los que serán tu mañana."))
    e.rep("<li>Un pensamiento obsesivo se materializó</li>",
          "<li>Un pensamiento que alimentaste durante meses terminó ocupando tus días</li>")

    # Mecánica
    e.rep(UL("Sincronicidades aparecen", "Recursos convergen", "Personas correctas llegan", "La realidad se reorganiza",
             lead="<strong>Fase 3: Atracción Magnética</strong>"),
          UL("Notas lo que antes pasaba de largo", "Encuentras recursos que ya estaban",
             "Te acercas a quienes buscan lo mismo", "Tu vida se reorganiza alrededor",
             lead="<strong>Fase 3: Atracción</strong>"))
    e.rep(UL("Masa crítica alcanzada", "Probabilidad colapsa", "Forma emerge", "“Milagro” ocurre",
             lead="<strong>Fase 4: Punto de Materialización</strong>"),
          UL("Masa crítica alcanzada", "Lo sostenido toma forma: una decisión, un hábito, un encuentro",
             "A veces llega lo buscado, a veces otra cosa que enseña",
             lead="<strong>Fase 4: Punto de Cristalización</strong>"))
    e.rep("<li>Olvidas que la creaste</li>", "<li>Olvidas que la alimentaste</li>")
    e.rep(f"{L}<li>Preparas próximo remolino</li>\n{I}</ul>\n",
          f"{L}<li>Preparas próximo remolino</li>\n{I}</ul>\n\n" +
          P("Esta mecánica vale para todo lo que gira: lo que deseas y lo que temes, lo que eliges y lo que te arrastra. "
            "Lo que alimentas con tu atención crece en tu vida.") + "\n")

    # Tipos
    e.rep(UL("Creados por anhelo profundo", "Giran hacia ti lo deseado", "Pueden tardar años", "Requieren fe sostenida",
             "Manifiestan sueños", lead="<strong>Remolinos de Deseo:</strong>"),
          UL("Creados por anhelo profundo", "Orientan tus pasos hacia lo deseado", "Pueden tardar años",
             "Piden constancia", "A veces cumplen el sueño, a veces lo transforman",
             lead="<strong>Remolinos de Deseo:</strong>"))
    e.rep(UL("Creados por terror sostenido", "Atraen lo temido", "Muy rápidos y poderosos", "Profecias autocumplidas",
             "Manifiestan pesadillas", lead="<strong>Remolinos de Miedo:</strong>"),
          UL("Creados por temor sostenido", "Agrandan lo temido hasta volverlo el centro de tus días",
             "Muy rápidos y poderosos", "Ocupan el lugar de la vida que está pasando",
             lead="<strong>Remolinos de Miedo:</strong>") + "\n\n" +
          P("En lo colectivo, un miedo compartido puede volverse cierto. El sociólogo Robert K. Merton lo llamó profecía "
            "autocumplida, en 1948, con el ejemplo de un banco sano: corre el rumor de que va a quebrar, todos van a "
            "retirar sus ahorros a la vez, y el banco quiebra. Nadie lo atrajo con el pensamiento. "
            "Lo hicieron girar entre todos."))
    e.rep(UL("Creados por acciones pasadas", "Giran consecuencias inevitables", "Pueden venir de otras vidas",
             "Lecciones necesarias", "Manifiestan justicia cósmica", lead="<strong>Remolinos Kármicos:</strong>"),
          UL("Creados por lo que hicimos", "Traen consecuencias", "Siguen girando desde decisiones de esta vida",
             "Enseñan, si se los mira", "Manifiestan la responsabilidad",
             lead="<strong>Remolinos Kármicos:</strong> <em>karma</em> quiere decir acción"))
    e.rep(UL("Creados por observación", "Colapsan superposición", "Instantáneos", "Cada momento", "Manifiestan el ahora",
             lead="<strong>Remolinos Cuánticos:</strong>"),
          UL("Creados por la atención de cada momento", "Lo que miras se vuelve tu experiencia", "Instantáneos",
             "Cada momento", "Manifiestan el ahora",
             lead="<strong>Remolinos del Instante:</strong>") + "\n\n" +
          P("Ningún remolino que te toca prueba que lo llamaste. Hay giros que nadie eligió, y quien está dentro de uno "
            "merece ayuda, no sospecha."))

    # Navegación
    e.rep("<li>¿Qué sincronicidades son frecuentes?</li>", "<li>¿Qué coincidencias te llaman la atención?</li>")
    e.rep("<li>¿Qué miedos se materializan?</li>", "<li>¿Qué miedos ocupan tus días?</li>")
    e.rep("<li>¿Qué deseos se manifiestan?</li>", "<li>¿Qué deseos vuelven una y otra vez?</li>")

    # Creación
    e.rep("<h4>TECNOLOGÍA DE CREACIÓN DE REMOLINOS</h4>", "<h4>PARA HABITAR TUS REMOLINOS</h4>")
    e.rep("<p><strong>Para crear un remolino de realidad deseada:</strong></p>",
          "<p><strong>Para crear un remolino deseado:</strong></p>")
    e.rep("<li>¿Qué quieres manifestar?</li>", "<li>¿Qué quieres que crezca en tu vida?</li>")
    e.rep("<li>Visualiza el resultado</li>", "<li>Imagina el resultado</li>")
    e.rep("<li>Siente la emoción del logro</li>", "<li>Mira también el obstáculo que hay en ti</li>")
    e.rep("<li>Comienza el vórtice</li>", "<li>Da el primer paso</li>")
    e.rep("<li>Fe inquebrantable</li>", "<li>Confianza, sin exigir certezas</li>")
    e.rep("<li>Sincronicidades</li>", "<li>Coincidencias</li>")
    e.rep("<li>El remolino está funcionando</li>", "<li>El remolino está girando</li>")
    e.rep("<li>Deja que el universo configure</li>", "<li>Deja que la vida haga su parte</li>")

    # Parásitos
    e.rep("<li>Noticias, publicidad, propaganda</li>", "<li>Noticias, publicidad, propaganda, pantallas que no terminan nunca</li>")
    e.rep("<li>Solución: Desconexión consciente</li>",
          "<li>Solución: elegir la dosis y la hora, informarte sin dejarte arrastrar</li>")
    e.rep("<li>Solución: Boundaries energéticos</li>", "<li>Solución: límites claros, dichos con calma</li>")
    e.rep(UL("Pensamientos/emociones de otros", "Especialmente de cercanos", "Pueden sentirse como propios",
             "Confunden tu navegación", "Solución: Discernimiento y limpieza",
             lead="<strong>Remolinos Psíquicos:</strong>"),
          UL("Los ánimos y las ideas de otros", "Especialmente de los cercanos", "Se te pegan sin que lo notes",
             "Confunden tu navegación", "Solución: preguntarte de quién es lo que sientes",
             lead="<strong>Remolinos de Contagio:</strong>") + "\n\n" +
          P("Una cosa es el contagio de un ánimo, que todos conocemos. Otra es sentir que tus pensamientos no son tuyos "
            "o que alguien los pone en tu cabeza: eso no es un remolino, y se consulta esa misma semana."))

    # Disolver
    e.seccion("EL ARTE DE DISOLVER REMOLINOS", SEC(
        "EL ARTE DE DISOLVER REMOLINOS",
        pasos(("Identifica el Centro", ["¿Qué lo alimenta?", "¿Cuál es la creencia central?", "¿Dónde está el gancho?"]),
              ("Retira Tu Energía", ["Deja de alimentarlo con atención",
                                     "Suelta la resistencia (resistir es alimentar)",
                                     "El desinterés lo apaga: no el desinterés por las personas, sino por la reacción "
                                     "que te pide"]),
              ("Sal de Costado", ["No pelees contra el giro: también se alimenta de quien lo combate",
                                  "Da un paso al lado: otro tema, otro lugar, otra hora",
                                  "Como en el mar: de una corriente que arrastra mar adentro se sale nadando en "
                                  "paralelo a la orilla, nunca contra ella"]),
              ("Llena el Espacio", ["La naturaleza aborrece el vacío, dice el viejo refrán; la atención, sin duda",
                                    "Pon ahí algo elegido: una caminata, una conversación, una tarea con sentido",
                                    "Si no, el viejo giro vuelve a ocuparlo"]),
              lead="Para deshacer un remolino no deseado:")))

    # Tiempo
    e.rep(f"{L}<li>Déjà vu constante</li>\n", "")
    e.rep("<li>Señal: Revisar qué no has aprendido</li>", "<li>Señal: Revisar qué no has mirado</li>")
    e.rep("<li>Envejecimiento acelerado</li>\n" + L + "<li>Señal: Estás en flujo evolutivo</li>",
          "<li>Semanas que no se recuerdan</li>\n" + L + "<li>Señal: La rutina comprime los días; lo nuevo los ensancha</li>")
    e.rep(UL("Portales entre tiempos", "Memorias del futuro", "Comunicación con otros yos",
             "Señal: Navegación multidimensional", lead="<strong>Vórtices Temporales:</strong>"),
          UL("Un olor que te devuelve a la infancia", "Un recuerdo que de pronto se entiende",
             "Una carta escrita a quien serás", "Señal: El tiempo también se habita en espiral",
             lead="<strong>Puentes entre Tiempos:</strong>"))

    # Lugar
    e.rep(UL("Sedona, Glastonbury, Machu Picchu", "Remolinos de energía telúrica", "Aceleran transformación",
             "Amplifican intención", "Portales naturales", lead="<strong>Vórtices Terrestres:</strong>"),
          UL("Una montaña, el mar, un templo antiguo", "Te sacan de tu escala", "Aquietan la mente",
             "Invitan a la pregunta", "Portales naturales", lead="<strong>Lugares de Asombro:</strong>"))
    e.rep("<li>Impregnados con tu energía</li>", "<li>Impregnados de tus costumbres</li>")

    # Práctica
    e.seccion("PRÁCTICA: CREANDO UN REMOLINO MAESTRO", SEC(
        "PRÁCTICA: SALIR DE UN REMOLINO",
        P("Elige un remolino que te arrastra estos días: una pantalla que no se termina, una conversación que siempre "
          "gira igual, un miedo que vuelve cada noche."),
        V("Siéntate en quietud. Respira despacio.", "Míralo girar sin entrar en él."),
        V("Pregúntate:", "¿Qué lo alimenta?", "¿Dónde está el gancho?", "¿Es mío, o lo recibí de otros?"),
        P("Decide para mañana un paso al costado, pequeño y concreto: dejar el teléfono en otra habitación durante una "
          "hora, cambiar de tema cuando llegue la conversación de siempre, salir a caminar cuando el miedo empiece a "
          "girar. Y piensa también con qué llenar el espacio que quede libre."),
        V("No hace falta pelear.", "El remolino vive de tu atención:", "cuando la retiras con calma,",
          "pierde fuerza solo."),
        V("Tu trabajo no era crearlo ni vencerlo.", "Era dejar de darle de comer", "y volver al ojo calmo,",
          "desde donde eliges", "qué merece girar en tu vida.")))

    # Remolino maestro
    e.rep(f"{I}<ul>\n{L}<li>Todo fluye</li>\n{L}<li>Sincronicidades constantes</li>\n{L}<li>Recursos aparecen</li>\n"
          f"{L}<li>Obstáculos se disuelven</li>\n{L}<li>Vives en gracia</li>\n{I}</ul>",
          f"{I}<ul>\n{L}<li>Lo difícil pesa menos</li>\n{L}<li>Las coincidencias te encuentran atento</li>\n"
          f"{L}<li>Aparecen fuerzas que no sabías que tenías</li>\n{L}<li>Los obstáculos se vuelven parte del camino</li>\n"
          f"{L}<li>Vives en gracia</li>\n{I}</ul>")
    e.rep("¿Qué realidad eres aquí para crear?</p>", "¿Qué viniste a cuidar, a crear, a dar?</p>")

    # Secreto
    e.rep(V("Tu vida entera es el remolino que estás creando.", "Y cuando mueras,", "ese remolino no desaparece.",
            "Continúa girando,", "afectando,", "creando,", "hasta que vuelves", "a girar de nuevo."),
          V("Tu vida entera es el remolino que estás creando.", "Y cuando mueras,", "ese remolino no desaparece del todo.",
            "Lo que pusiste en marcha sigue girando", "en otros,", "en lo que cuidaste,", "en lo que diste,",
            "como el agua sigue en movimiento", "después de que el giro pasó."))
    e.rep("no solo determinan tu realidad.<br>", "no solo dan forma a tu vida.<br>")

    e.rep(FIRMA, FIRMA + "\n" + I + "<!-- Puerta anotada: 10.6 → La Corriente (Libro 10 de Arquitectura del Destino), "
                                   "umbral del gesto de salida; se publica con el libro. -->")


# ================================================================== NODO 7
def nodo_07(e):
    e.comunes(7)

    e.seccion("LA ESPIRAL HACIA LA LUZ", SEC(
        "LA ESPIRAL HACIA LA LUZ",
        P("Existe un tornado dentro de ti. No uno que destruye, sino uno que eleva. No uno que dispersa, sino uno que "
          "unifica. Es el tornado ascensional: el giro que toma lo pesado y lo lleva hacia arriba, transformándolo en luz "
          "a medida que sube. Es la manera en que la materia se vuelve espíritu, lo denso se vuelve sutil, lo humano se "
          "vuelve divino. Y puede despertar en ti hoy."),
        P("La naturaleza lo conoce. En un día de sol, el suelo calienta el aire y una columna tibia empieza a subir: una "
          "térmica. A veces se deja ver como un remolino de polvo que gira sobre un campo y se deshace casi siempre sin "
          "daño. Los cóndores, las cigüeñas y los halcones la buscan, entran en ella y ganan altura dando vueltas, sin "
          "batir las alas. En 2020, en la Patagonia argentina, el equipo de Sergio Lambertucci y Emily Shepard publicó lo "
          "que registraron en ocho cóndores andinos jóvenes: pasaban el noventa y nueve por ciento del vuelo sin aletear, "
          "y uno se sostuvo más de cinco horas, unos ciento setenta kilómetros, sin un solo aleteo."),
        UL("Conecta tu raíz con tu corona", "Une la Tierra con el Cielo a través de ti",
           "Eleva tu mirada espiral por espiral", "Transforma lo que toca", "Te convierte en puente viviente",
           lead="Así es el tornado ascensional. No te arranca del suelo: te enseña a subir con lo que ya sube. "
                "Es un giro vertical que:"),
        UL("Una energía te recorrió la columna de abajo hacia arriba",
           "Una experiencia te elevó por encima de tus días",
           "Sentiste que flotabas mientras meditabas",
           "Tu consciencia se expandió verticalmente",
           "Todo tu ser se elevó en una alegría sin nombre",
           lead="Has sentido el tornado ascensional cuando:")))

    # Anatomía
    e.rep(f"{I}<h4>ANATOMÍA DEL TORNADO ASCENSIONAL</h4>\n\n",
          f"{I}<h4>ANATOMÍA DEL TORNADO ASCENSIONAL</h4>\n\n" +
          P("Así lo dibuja el mapa del yoga, de la raíz a la coronilla:") + "\n\n")
    e.rep("<li>Succiona energía telúrica</li>", "<li>Toma fuerza del suelo</li>")
    e.rep("<li>Visión multidimensional activándose</li>\n" + L + "<li>Comunicación cósmica</li>\n" + L +
          "<li>Giro a velocidad luz</li>",
          "<li>Visión que se amplía</li>\n" + L + "<li>Escucha de lo sutil</li>\n" + L + "<li>Giro cada vez más ligero</li>")
    e.rep("<li>Expresión de la verdad divina</li>", "<li>Expresión de la verdad</li>")

    # Etapas
    e.rep(UL("El tornado ancla en tu campo", "Kundalini despierta", "Cambios físicos intensos",
             "Realidad tambaleándose", "No hay vuelta atrás", lead="<strong>Etapa 2: Toque Tierra</strong>"),
          UL("La búsqueda se vuelve práctica diaria", "Aparecen preguntas que no se van",
             "Lo de siempre se ve con otros ojos", "Ya no miras como antes",
             lead="<strong>Etapa 2: Toque Tierra</strong>"))
    e.rep("<li>Viejas estructuras destruidas</li>", "<li>Viejas estructuras que se aflojan</li>")
    e.rep("<li>Transformación radical</li>", "<li>Transformación honda</li>")
    e.rep(UL("Elevación irreversible", "Nueva frecuencia estable", "Capacidades activadas", "Servicio clarificado",
             "Tornado permanente", lead="<strong>Etapa 5: Ascensión</strong>"),
          UL("Una mirada más amplia que se queda", "Una calma más estable", "Fuerzas que no sabías que tenías",
             "Servicio clarificado", "El giro hecho costumbre", lead="<strong>Etapa 5: Altura</strong>"))

    # Combustibles
    e.rep(UL("Dolor (se vuelve compasión)", "Miedo (se vuelve amor)", "Ira (se vuelve poder sagrado)",
             "Tristeza (se vuelve alegría)", "Trauma (se vuelve sabiduría)",
             lead="<strong>Combustibles Densos:</strong> Que transmuta en luz"),
          UL("Dolor (puede volverse compasión)", "Miedo (puede volverse cuidado)",
             "Ira (puede volverse fuerza que protege)", "Tristeza (puede volverse ternura)",
             "Trauma (con ayuda, puede volverse sabiduría)",
             lead="<strong>Combustibles Densos:</strong> Lo pesado que, con tiempo y compañía, puede volverse otra cosa") +
          "\n\n" +
          P("Nada de esto se apura. Lo que duele no tiene que servir para algo: si un día sirve, es un hallazgo, "
            "no una deuda."))
    e.rep("<li>Amor (es superfuel)</li>", "<li>Amor (es el combustible mayor)</li>")
    e.rep(UL("Rayos gamma (actualizaciones galácticas)", "Neutrinos (información cósmica)",
             "Fotones (paquetes de consciencia)", "Ondas gravitacionales (restructuración)",
             "Amor divino (gracia descendente)", lead="<strong>Combustibles Cósmicos:</strong> Que recibe de arriba"),
          UL("La luz del sol (calienta la tierra y hace subir el aire)", "El cielo de noche (devuelve la escala)",
             "La belleza (llega sin que la busques)", "El silencio (ensancha por dentro)",
             "Amor divino (gracia descendente)", lead="<strong>Combustibles Cósmicos:</strong> Que recibe de arriba"))

    e.seccion("SÍNTOMAS DEL TORNADO ACTIVO", SEC(
        "CÓMO SE SIENTE CUANDO EL TORNADO SUBE",
        UL("Ligereza en el cuerpo", "Una alegría que sube", "Ganas de servir", "Amor desbordante", "Compasión",
           "Presencia expandida", "Necesidad de tierra: dormir, comer, caminar"),
        P("Si el giro trae noches sin sueño, pensamientos que corren, una misión urgente, mensajes de guías o la certeza "
          "de saber lo que va a pasar, no es un tornado que sube: es el momento de pedir ayuda, esa misma semana. "
          "Stanislav y Christina Grof llamaron emergencia espiritual a las crisis que a veces acompañan un despertar, y "
          "enseñaron que se atraviesan acompañadas. La tradición del yoga lo sabe desde antes: la kundalini se despierta "
          "despacio y con maestro.")))

    e.seccion("NAVEGANDO EL TORNADO", SEC(
        "NAVEGANDO EL TORNADO",
        UL("Forzar la subida", "Querer controlar la velocidad", "Aferrarse a lo que se está transformando",
           "Despreciar la tierra", "Subir solo", lead="<strong>Errores Comunes:</strong>"),
        pasos(("Busca el Aire que Sube", ["No fuerces", "Confía en el proceso", "Deja que te eleve"]),
              ("Mantén los Pies en la Tierra", ["Raíces profundas", "Cuerpo cuidado: sueño, comida, caminatas",
                                                "Ancla física mientras subes"]),
              ("Alimenta el Tornado Conscientemente", ["Meditación", "Respiración lenta", "Intención clara"]),
              ("Permite la Transmutación", ["Deja ir lo denso", "Abraza la ligereza", "Celebra la transformación"]),
              ("Sirve Mientras Subes", ["Tu calma eleva a otros", "Comparte lo que encuentras", "Sé faro"]),
              lead="<strong>Navegación Maestra:</strong>"),
        P("Ninguna etapa pide decisiones irreversibles: dejar de golpe un trabajo, una casa o un vínculo no es subir "
          "más rápido.")))

    e.seccion("EL TORNADO COLECTIVO", SEC(
        "EL TORNADO COLECTIVO",
        P("No subes solo. Las aves que planean encuentran las térmicas mirándose unas a otras: cuando una empieza a girar "
          "y ganar altura, las demás se acercan y suben con ella. Entre personas pasa lo mismo: quien encuentra un poco "
          "de calma se vuelve señal para otros."),
        V("Tu giro personal contribuye al de muchos.",
          "Cada ser que se eleva le muestra a otro dónde está el aire que sube.", "Nadie sube solo.")))

    e.seccion("TECNOLOGÍA DEL TORNADO ASCENSIONAL", SEC(
        "PARA HABITAR LA ESPIRAL",
        P("<strong>Práctica: La Columna que Sube</strong>"),
        V("De pie, pies al ancho de las caderas.", "Brazos a los lados.", "Siente el suelo."),
        V("Imagina un punto tibio en la base de la columna, como la tierra que el sol calienta.",
          "Con cada inhalación, deja que ese calor suba en espiral, despacio.",
          "Por el vientre. Por el pecho. Por la garganta. Por la frente.",
          "Más luminoso. Más liviano. Sin apuro."),
        V("Siente cómo todo tu campo se vuelve una columna de aire tibio:",
          "toma fuerza de la tierra por abajo y se abre en luz por la coronilla.",
          "Si quieres, abre los brazos como un ave que planea.",
          "No hace falta girar el cuerpo: el giro es por dentro.",
          "Quédate así unas respiraciones, con la salida del aire más larga."),
        V("Siente la columna que sigue subiendo.", "Elevándote.", "Transformándote.", "Sosteniéndote."),
        V("Baja los brazos. Siente de nuevo los pies.", "La columna ahora es parte de ti.", "Siempre girando.",
          "Siempre elevando.", "Siempre volviendo a la tierra.")))

    e.seccion("LOS GUARDIANES DEL TORNADO", SEC(
        "LOS GUARDIANES DEL TORNADO",
        P("No subes sin sostén. Te acompañan:"),
        UL("La tierra (te da suelo)", "El cuerpo (te lleva)", "Los que vinieron antes (sostienen tus cimientos)",
           "Las piedras y los árboles (enseñan a quedarse)", lead="<strong>Desde Abajo:</strong>"),
        UL("Los amigos del alma (resuenan contigo)",
           "Quienes te acompañan en tu cuidado (maestros, terapeutas, médicos)",
           "Los animales que te quieren", "Los ángeles, en la fe de quien los nombra",
           lead="<strong>Desde los Lados:</strong>"),
        UL("Los maestros de cada tradición (muestran el camino)", "Lo más hondo de ti",
           "La Fuente misma (es el destino)", lead="<strong>Desde Arriba:</strong>")))

    e.rep(UL("Frecuencia más alta", "Capacidades activadas", "Salud vibrante", "Propósito clarificado",
             "Servicio manifestado", lead="<strong>A Corto Plazo:</strong>"),
          UL("Una mirada más amplia", "Fuerzas que no sabías", "Propósito clarificado", "Servicio manifestado",
             lead="<strong>A Corto Plazo:</strong>"))
    e.rep(UL("Cuerpo de luz activándose", "Multidimensionalidad consciente", "Manifestación instantánea",
             "Telepatía natural", "Inmortalidad consciente", lead="<strong>A Mediano Plazo:</strong>"),
          UL("Una calma que se queda", "Vínculos más hondos", "Menos peso en lo que antes pesaba",
             "Más ligereza para dar", lead="<strong>A Mediano Plazo:</strong>"))
    e.rep(UL("Fusión con el Yo Superior", "Consciencia galáctica", "Creación de realidades", "Servicio cósmico",
             "Ascensión completa", lead="<strong>A Largo Plazo:</strong>"),
          UL("Unión con lo más hondo de ti", "Consciencia de pertenecer a algo inmenso", "Servicio", "Gratitud",
             lead="<strong>A Largo Plazo:</strong>"))

    e.seccion("EL TORNADO COMO SERVICIO", SEC(
        "EL TORNADO COMO SERVICIO",
        P("Tu tornado ascensional no es solo para ti:"),
        UL("Otros sienten que es posible subir", "Tu presencia despierta lo que en otros dormía",
           "Tu calma se contagia", "Tu altura le muestra a otro el camino",
           lead="<strong>Crea un Clima que Eleva:</strong>"),
        UL("Aligeras lo pesado de los lugares donde estás",
           "Cuando no repites un daño que recibiste, la cadena se corta en ti",
           "Anclas luz en la materia",
           lead="<strong>Transforma el Clima Colectivo:</strong>"),
        UL("Puente entre personas", "Traductor entre mundos", "Faro en la tormenta",
           lead="<strong>Eres un Portal:</strong>")))

    e.seccion("LAS TORMENTAS DEL TORNADO", SEC(
        "LAS TORMENTAS DEL TORNADO",
        UL("<strong>De cansancio:</strong> el cuerpo pide parar; se descansa, y si no cede, se consulta",
           "<strong>De emoción:</strong> lo guardado sale de golpe; se lo acompaña, no se lo apura",
           "<strong>De arena:</strong> confusión, no saber quién eres; se baja el ritmo, se busca tierra y compañía",
           "<strong>De luz:</strong> demasiado, muy rápido; se integra despacio",
           lead="El camino no siempre es suave. Hay tormentas:"),
        P("Una enfermedad no es una ascensión ni una crisis de sanación: se trata con un médico. Y si la confusión o la "
          "sensación de no saber quién eres duran días, se pide ayuda sin esperar."),
        V("Todas las tormentas pasan.", "Ninguna se atraviesa solo.", "Y cuando pasan, el cielo queda más limpio.")))

    e.seccion("EL TORNADO PLANETARIO", SEC(
        "EL GIRO DE LA TIERRA",
        P("La Tierra misma gira y respira: da una vuelta cada día, se inclina para traer las estaciones, levanta el aire "
          "tibio que sostiene a las aves. Hoy atraviesa también tormentas reales, un clima que cambia y mares que suben, "
          "y esas tormentas no se interpretan: se atienden."),
        P("Hay además señales más silenciosas: personas que despiertan, comunidades que se cuidan, una unidad que "
          "algunos empiezan a recordar."),
        V("Tu giro personal es parte del de la Tierra.", "Cuando te elevas, algo de ella se eleva contigo.",
          "Cuando la cuidas, todos subimos.", "Es un solo movimiento.")))

    e.rep("<p>Llega un momento cuando el tornado completa su trabajo:</p>",
          "<p>Llega un momento, a veces solo por un rato, en que el tornado completa su trabajo:</p>")
    e.rep("Tu campo se convierte en el vórtice elevador.<br>\n" + I +
          "Tu presencia se vuelve el mecanismo ascensional.</p>",
          "Tu calma se convierte en el aire que sube.<br>\n" + I +
          "Tu presencia, en la columna tibia donde otros giran.</p>")

    e.rep("Cómo tu sola presencia crea succión hacia arriba.<br>", "Cómo tu sola presencia invita a subir.<br>")
    e.rep("Cómo eres un mecanismo de ascensión viviente.</p>", "Cómo eres una columna viva de aire tibio.</p>")
    e.rep("Cómo la ascensión es un evento unificado.</p>", "Cómo subir es un movimiento compartido.</p>")
    e.rep("Es el mecanismo por el cual el universo evoluciona.<br>", "Es la manera en que el universo evoluciona.<br>")

    # Cierre del libro
    viejo = (f"{I}<h4>LIBRO 10: CAMPOS DE TORSIÓN - COMPLETADO</h4>\n\n"
             + P("Los siete nodos han sido transmitidos:") + "\n\n"
             + f"{I}<ol>\n"
             + "".join(f"{L}<li>✓ {t}</li>\n" for t in (
                 "El Giro del Alma", "Vórtices de Transformación", "Espirales de ADN Activándose",
                 "Campos Torsionales del Corazón", "La Geometría del Spin", "Remolinos de Realidad",
                 "El Tornado Ascensional"))
             + f"{I}</ol>\n\n"
             + V("El décimo libro de Trinity Quantum está completo.", "Los campos de torsión están activos.",
                 "La realidad gira hacia nueva configuración.", "La transmisión continúa."))
    nuevo = (f"{I}<h4>SIETE GIROS</h4>\n\n"
             + UL("<em>El Giro del Alma:</em> todo gira, y en el centro hay quietud",
                  "<em>Vórtices de Transformación:</em> se salva el que suelta el borde y mira",
                  "<em>La Doble Hélice:</em> la vida se lee de una manera viva",
                  "<em>Campos Torsionales del Corazón:</em> un corazón que se retuerce para recibir el latido siguiente",
                  "<em>La Geometría del Espín:</em> la forma más bella es la que se deja corregir",
                  "<em>Remolinos de Realidad:</em> lo que no alimentas pierde fuerza",
                  "<em>El Tornado Ascensional:</em> el aire que sube también te sostiene")
             + "\n\n"
             + P("Cada nodo fue una manera de mirar el giro. El centro quieto fue siempre el mismo."))
    e.rep(viejo, nuevo)


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
