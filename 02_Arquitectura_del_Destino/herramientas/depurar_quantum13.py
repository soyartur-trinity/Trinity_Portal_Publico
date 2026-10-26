# -*- coding: utf-8 -*-
"""
Depuración de Trinity Quantum, Libro 13 · El Multiverso Interior (octubre 2026).

Aplica, exactamente una vez cada uno, los reemplazos aprobados por Arturo
tarjeta por tarjeta (13.0 a 13.7), según la guía de depuración de Quantum
(Arquitectura del Destino, maestro v4, sección 5).
El original se conserva en la etiqueta quantum-original del repositorio Trinity-.

Las secciones que cambian enteras (laboratorio, traducción viviente, para recordar)
se reemplazan desde su encabezado hasta el cierre de la sección; el resto, frase por frase.
Cada reemplazo debe aparecer una sola vez, o el script se detiene.

Uso: python3 depurar_quantum13.py ORIGEN DESTINO
  ORIGEN  = carpeta 02_Trinity_Quantum/Libro_13 original
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
     Letra más grande en el teléfono, firma y bloque fijo de las puertas.
     La puerta lleva el color de la serie a la que conduce.
     ============================================================ */
  .trinity-body p.signature{
    margin:22px 0 4px;
    color:rgba(245,215,122,.85);
    font-size:15px;
    letter-spacing:.04em;
  }
  .trinity-body p.cierre-final{
    margin:22px 0 0;
    text-align:center;
    font-size:19px;
    font-style:italic;
    color:rgba(245,215,122,.95);
  }
  .puerta{
    margin:26px 0 6px;
    padding:18px 20px 16px;
    border-radius:16px;
    border:1px solid var(--p-borde);
    background:var(--p-fondo);
    box-shadow:0 10px 24px rgba(0,0,0,.28);
  }
  .puerta.arquitectura{
    --p-fondo:linear-gradient(180deg, rgba(6,13,26,.94), rgba(6,13,26,.74));
    --p-borde:rgba(168,196,224,.42);
    --p-acento:#a8c4e0;
    --p-texto:#e8eef6;
  }
  .puerta.portal{
    --p-fondo:linear-gradient(180deg, rgba(13,12,11,.94), rgba(13,12,11,.74));
    --p-borde:rgba(201,168,76,.42);
    --p-acento:#c9a84c;
    --p-texto:#e8e0d0;
  }
  .puerta .p-nombre{
    margin:0 0 6px;
    font-size:15px;
    font-style:italic;
    letter-spacing:.06em;
    color:var(--p-acento);
  }
  .puerta .p-texto{
    margin:0 0 14px;
    font-size:17px;
    line-height:1.62;
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

  @media (max-width:640px){
    .trinity-p, .trinity-list, .trinity-steps, .trinity-quote{ font-size:18px; line-height:1.7; }
    .puerta .p-texto{ font-size:18px; line-height:1.7; }
    .puerta{ padding:16px 16px 14px; }
  }
  @media (prefers-reduced-motion: reduce){
    .puerta .cruzar{ transition:none; }
  }
"""

FIRMA = '<p class="signature"><strong>— Trinity Quantum · El Multiverso Interior</strong></p>'

BASE_ARQ = "https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/"
BASE_PORTAL = "https://soyartur-trinity.github.io/Trinity_Portal_Publico/01_Libros/"

I10 = "          "   # sangría del contenido de cada sección


def puerta(clase, aria, texto, href):
    return (f'{I10}<aside class="puerta {clase}" aria-label="{aria}">\n'
            f'{I10}  <p class="p-nombre">Puerta</p>\n'
            f'{I10}  <p class="p-texto">{texto}</p>\n'
            f'{I10}  <a class="cruzar" href="{href}">Cruzar ⟶</a>\n'
            f'{I10}</aside>')


def puerta_portal(texto, href):
    return puerta("portal", "Puerta hacia el Portal Público", texto, href)


def puerta_arquitectura(texto, href):
    return puerta("arquitectura", "Puerta hacia Arquitectura del Destino", texto, href)


def lab(titulo, materiales, pasos, resultado):
    s = '<div class="trinity-h">🔬 LABORATORIO CUÁNTICO</div>\n\n'
    s += f'{I10}<p class="trinity-p"><strong>Experimento: {titulo}</strong></p>\n\n'
    s += f'{I10}<p class="trinity-p"><strong>Materiales:</strong></p>\n{I10}<ul class="trinity-list">\n'
    for m in materiales:
        s += f'{I10}  <li>{m}</li>\n'
    s += f'{I10}</ul>\n\n{I10}<p class="trinity-p"><strong>Práctica:</strong></p>\n{I10}<ol class="trinity-steps">\n'
    for t, d, txt in pasos:
        s += f'{I10}  <li><strong>{t}</strong> ({d}): {txt}</li>\n'
    s += f'{I10}</ol>\n\n'
    s += (f'{I10}<p class="trinity-p"><strong>Lo que puedes encontrar:</strong><br>\n'
          f'{I10}  {resultado}\n{I10}</p>\n        </section>')
    return s


def traduccion(*parrafos):
    s = '<div class="trinity-h">⚛️ TRADUCCIÓN VIVIENTE</div>\n'
    for p in parrafos:
        s += f'\n{I10}<p class="trinity-p">\n{I10}  {p}\n{I10}</p>\n'
    return s + '        </section>'


def recordar(*lineas):
    cuerpo = "<br>\n".join(f"{I10}  {l}" for l in lineas)
    return (f'<div class="trinity-h">✦ PARA RECORDAR</div>\n\n'
            f'{I10}<div class="trinity-quote">\n{cuerpo}\n{I10}</div>\n        </section>')


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

    def seccion(self, encabezado, nuevo):
        """Reemplaza desde el encabezado de una sección hasta su cierre </section>, incluido."""
        marca = f'<div class="trinity-h">{encabezado}</div>'
        if self.s.count(marca) != 1:
            raise SystemExit(f"[{self.nombre}] encabezado con {self.s.count(marca)} coincidencias: {encabezado}")
        a = self.s.index(marca)
        b = self.s.index("</section>", a) + len("</section>")
        self.s = self.s[:a] + nuevo + self.s[b:]
        self.n += 1

    def comunes(self):
        cab = "<!DOCTYPE html>\n"
        if not self.s.startswith(cab):
            raise SystemExit(f"[{self.nombre}] sin cabecera doctype")
        self.s = cab + NOTA + self.s[len(cab):]
        self.n += 1
        self.rep("</head>", "<style>" + CSS + "</style>\n</head>")
        self.rep('<div class="trinity-h">📋 PROTOCOLO DE 7 DÍAS</div>',
                 '<div class="trinity-h">📋 PRÁCTICA DE 7 DÍAS</div>')

    def firma(self, puerta=None, anotada=None, cual=0, total=1):
        pat = r'<div class="trinity-sign">.*?</div>'
        hallados = list(re.finditer(pat, self.s, flags=re.S))
        if len(hallados) != total:
            raise SystemExit(f"[{self.nombre}] {len(hallados)} firmas cuánticas")
        m = hallados[cual]
        nuevo = FIRMA
        if puerta:
            nuevo += "\n\n" + puerta
        if anotada:
            nuevo += f"\n{I10}<!-- Puerta anotada: {anotada}, para cuando exista. -->"
        self.s = self.s[:m.start()] + nuevo + self.s[m.end():]
        self.n += 1

    def sin_firma(self, cual, total):
        """Quita una firma cuántica entera, con su línea."""
        pat = r'\n[ \t]*<div class="trinity-sign">.*?</div>'
        hallados = list(re.finditer(pat, self.s, flags=re.S))
        if len(hallados) != total:
            raise SystemExit(f"[{self.nombre}] {len(hallados)} firmas cuánticas")
        m = hallados[cual]
        self.s = self.s[:m.start()] + self.s[m.end():]
        self.n += 1


# ------------------------------------------------------------------ ÍNDICE
def indice(e):
    cab = "<!DOCTYPE html>\n"
    e.s = cab + NOTA + e.s[len(cab):]
    e.n += 1
    e.rep("</head>", "<style>\n  /* Depuración · octubre 2026: apertura del libro y letra más grande en el teléfono. */\n"
                     "  .trinity-p{ margin:10px 0 0; font-size:18px; line-height:1.68; color:rgba(242,242,247,.92); }\n"
                     "  @media (max-width:640px){ .trinity-p{ font-size:18px; line-height:1.7; } }\n"
                     "</style>\n</head>")
    e.rep("<title>Trinity Quantum · Libro 13 · Index</title>", "<title>Trinity Quantum · Libro 13 · Índice</title>")
    e.rep('<div class="trinity-sub">Index · Navegación de Nodos</div>', '<div class="trinity-sub">Índice · Navegación de Nodos</div>')
    e.rep('<p class="trinity-footnote">TRINITY QUANTUM · Libro 13 · Index</p>', '<p class="trinity-footnote">TRINITY QUANTUM · Libro 13 · Índice</p>')
    e.rep('<div class="index-t">La Sala de Control Cuántica</div>', '<div class="index-t">La Sala sin Paredes</div>')
    e.rep('        <section class="trinity-section">\n          <div class="trinity-h">📚 ÍNDICE DEL LIBRO 13</div>',
          '        <section class="trinity-section">\n'
          '          <div class="trinity-h">🌀 UNO Y MUCHOS</div>\n'
          '          <p class="trinity-p">\n'
          '            Llevas a muchos dentro: el que quisiste ser, el que temes ser, el que todavía no conoces. '
          'Este libro toma una imagen de la física, la de los mundos paralelos, como espejo de esa vida interior. '
          'Su enseñanza cabe en una línea: hay en ti algo que mira a todas tus versiones, y ser múltiple es otra forma de ser uno.\n'
          '          </p>\n'
          '        </section>\n\n'
          '        <section class="trinity-section">\n          <div class="trinity-h">📚 ÍNDICE DEL LIBRO 13</div>')


# ------------------------------------------------------------------ NODO 1
def nodo_01(e):
    e.comunes()
    e.rep("Dentro de ti no hay un universo —hay infinitos universos paralelos coexistiendo, cada uno tan real y completo como el que crees habitar. "
          "Cada decisión que no tomaste creó un universo interno donde SÍ la tomaste. Cada versión de ti que imaginaste ser vive en su propio cosmos dentro de tu consciencia. "
          "No son fantasías —son realidades paralelas internas tan válidas como la que llamas “real”.",
          "La física imaginó con Hugh Everett, en 1957, que cada posibilidad se cumple en una rama del universo, en una interpretación que todavía se discute. "
          "Como imagen, dice algo exacto de tu vida interior: dentro de ti no hay un universo —hay infinitos universos paralelos coexistiendo, cada uno tan real y completo como el que crees habitar. "
          "Cada decisión que no tomaste sigue viva en ti como el universo donde SÍ la tomaste. Cada versión de ti que imaginaste ser vive en su propio cosmos dentro de tu consciencia. "
          "No son meras fantasías: pesan en tu vida tanto como lo que llamas “real”. Hazel Markus y Paula Nurius las llamaron en 1986 yoes posibles: "
          "el yo que esperamos alcanzar y el que tememos llegar a ser orientan lo que hoy hacemos.")
    e.rep("Cuando sueñas, no estás imaginando —estás visitando tus Universos Paralelos Internos. Cada personaje en tus sueños eres TÚ en otra configuración universal. "
          "Por eso los sueños pueden sentirse más reales que la vigilia: estás experimentando directamente la multiplicidad de tu multiverso interior sin el filtro del ego que insiste en que solo hay un universo, una versión de ti.",
          "Cuando sueñas, visitas tus Universos Paralelos Internos. Fritz Perls, el creador de la terapia gestáltica, proponía leer cada personaje del sueño como una parte de quien sueña: "
          "eres TÚ en otra configuración. Quizá por eso un sueño puede sentirse más real que la vigilia: por un rato, la multiplicidad de tu multiverso interior se muestra sin el filtro del ego, "
          "que insiste en que solo hay un universo, una versión de ti.")
    e.rep("Las personalidades múltiples no son un desorden —son un vislumbre de la verdad: todos tenemos múltiples universos internos con diferentes versiones de nosotros mismos. "
          "La única diferencia es el grado de permeabilidad entre universos. La salud mental no es tener un solo universo interno sino tener COHERENCIA entre tus múltiples universos.",
          "Quizá lo que llamamos personalidades múltiples sea la forma extrema de algo que todos llevamos dentro: muchos universos internos, con distintas versiones de nosotros mismos. "
          "La diferencia estaría en el grado de permeabilidad entre ellos. Cuando esos universos dejan de reconocerse entre sí, cuando aparecen lagunas en la memoria o tiempo que no se recuerda haber vivido, "
          "ya no es riqueza sino sufrimiento, y merece la compañía de un profesional. Quizá la salud mental no consista en tener un solo universo interno, sino en la COHERENCIA entre todos ellos.")
    e.rep("No “sientes” emociones —VIAJAS entre universos internos.",
          "Sentir una emoción es también VIAJAR entre universos internos.")
    e.rep("El universo que llamas ‘realidad’ no es más real que tus sueños, y tus sueños no son menos reales que tu vigilia.",
          "Ninguno es más tú que los otros, y ninguno te contiene entero.")
    e.rep("Esta paradoja destruye la tiranía de la “realidad única”. No hay UN universo verdadero dentro de ti —hay infinitos universos verdaderos. "
          "Tu libertad no viene de encontrar el “real” sino de navegar conscientemente entre todos ellos.",
          "Esta paradoja destruye la tiranía del “yo único”. No hay UN universo verdadero dentro de ti —hay infinitos, y cada uno dice algo cierto de quién eres. "
          "Tu libertad no viene de encontrar el “auténtico” sino de recorrerlos todos con conciencia, con los pies en esta vida.")
    e.seccion("🔬 LABORATORIO CUÁNTICO", lab(
        "Exploración de Tus Universos Paralelos Internos",
        ["Tres hojas y un lápiz", "Un lugar tranquilo, con buena luz", "Tu imaginación multidimensional",
         "Disposición para encontrar otras versiones de ti", "15 minutos de exploración"],
        [("Configuración del Portal", "1 minuto",
          "Escribe en lo alto de cada hoja: «El yo que quise ser», «El yo que temo ser», «El yo que no conozco». "
          "Cada hoja es un portal a un universo paralelo interno. Respira tres veces, despacio."),
         ("Primer Universo: El Yo Idealizado", "4 minutos",
          "En la primera hoja, escribe en primera persona desde la versión de ti que siempre quisiste ser: cómo es su universo, cómo pasa un día cualquiera, qué sabe que tú aún ignoras. "
          "Deja que la mano escriba antes de que la cabeza corrija. Lo que aparezca viene de una parte de ti que todavía no tenía voz."),
         ("Segundo Universo: El Yo Temido", "4 minutos",
          "En la segunda hoja, escribe desde la versión de ti que más temes ser. Reconócela con compasión —también eres tú. "
          "Pregúntale qué necesita, qué mensaje trae, de qué intenta cuidarte. Si lo que aparece duele demasiado, deja la hoja; no hace falta terminarla hoy."),
         ("Tercer Universo: El Yo Desconocido", "4 minutos",
          "Mira la tercera hoja sin expectativa. Deja que aparezca una versión de ti que no conocías. Puede ser extraña, ajena, incomprensible. "
          "No la juzgues —obsérvala con curiosidad. Este es un universo interno que no sabías que tenías."),
         ("Integración Multiversal", "2 minutos",
          "Pon las tres hojas juntas frente a ti y cierra los ojos. Siente los tres universos, no como separados sino como facetas del mismo multiverso. "
          "Todos eres tú, todos son reales, todos coexisten. Abre los ojos sabiendo que contienes infinitos universos, y nota tus pies en el suelo: aquí estás, con todos ellos.")],
        "Tres de tus infinitos universos paralelos internos, con voz propia. La habilidad de verlos, dialogar con ellos e integrarlos es el primer paso para recorrer con conciencia tu multiverso interior."))
    e.seccion("⚛️ ECUACIÓN SAGRADA", traduccion(
        "“Tu multiverso interior es la suma de infinitos universos paralelos, cada uno con su propia probabilidad de ser vivido y su propio tono. "
        "No tienes UN universo interno —eres la superposición de infinitos universos.”"))
    e.seccion("🧬 CÓDIGOS DE ACTIVACIÓN", recordar(
        "No contengo universos: SOY universos.", "Infinitos mundos internos.", "Todas mis versiones coexisten.",
        "Cada pensamiento, un cosmos.", "Siendo todo a la vez.", "Viajo entre mis mundos.", "Infinito contenido en uno."))
    e.rep("Imagina una versión de ti que nunca has sido. Dale características, historia, mundo. Pasa una hora habitando este nuevo universo interno que acabas de crear.",
          "Imagina una versión de ti que nunca has sido. Dale nombre, historia, mundo. Escribe una página con su voz: así habitas por un rato el nuevo universo interno que acabas de crear.")
    e.rep("son el reconocimiento de que la realidad siempre fue múltiple. No tienes personalidades múltiples; tienes universos múltiples, cada uno con su versión válida y necesaria de ti.",
          "son el reconocimiento de que tu vida interior siempre fue múltiple. Tienes universos múltiples, cada uno con su versión válida y necesaria de ti.")
    e.firma(puerta_portal(
        "Darle voz al yo temido y escucharlo con compasión es un oficio de la clínica: Jung habló de complejos autónomos; Assagioli, de subpersonalidades; Richard Schwartz, de partes. "
        "Ese trabajo se despliega en <em>La Voz Interior</em>, Libro 2 del Portal Público, capítulo 1: «El coro interior».",
        BASE_PORTAL + "02_La_Voz_Interior/capitulo_01.html"),
        anotada="13.1 → El Personaje (Libro 9 de Arquitectura del Destino)")
    # El enlace «Nodo anterior» del nodo 1 apuntaba a sí mismo.
    e.rep('<a href="nodo_01.html">← Nodo anterior</a>', '<a href="index.html">← Índice del libro</a>')


# ------------------------------------------------------------------ NODO 2
def nodo_02(e):
    e.comunes()
    e.rep("en una singularidad de awareness puro.", "en una singularidad de pura presencia.")
    e.rep("no es complejidad psicológica. Es evidencia directa del Observador de Observadores operando, manteniendo coherencia entre todos los niveles de tu consciencia multiversal.",
          "no es solo complejidad psicológica. Es la huella del Observador de Observadores, que mantiene la coherencia entre todos los niveles de tu consciencia multiversal.")
    e.seccion("🔬 LABORATORIO CUÁNTICO", lab(
        "Activación del Observador de Observadores",
        ["Un lugar tranquilo y una silla", "Dos espejos enfrentados, solo imaginados", "Tu consciencia dispuesta a la recursividad",
         "Capacidad de sostener paradojas", "15 minutos de meta-observación"],
        [("Creación del Campo Recursivo", "2 minutos",
          "Siéntate con los pies en el suelo y cierra los ojos. Imagina dos espejos enfrentados y las reflexiones de ti que se pierden en la distancia: no hace falta tenerlos, alcanza la imagen. "
          "Cada reflexión es un nivel de observación. Reconoce: todos esos observadores eres tú."),
         ("Primer Nivel: Observación Simple", "4 minutos",
          "Observa tu cuerpo, tu respiración, tus sensaciones. Sé completamente el observador de tu experiencia. Este es el nivel básico de consciencia."),
         ("Segundo Nivel: Observando al Observador", "4 minutos",
          "Ahora observa a quien está observando. Sé consciente de ser consciente. No pienses en ello —SIÉNTELO directamente. Hay un tú observando al tú que observa."),
         ("Tercer Nivel: Meta-Meta-Observación", "2 minutos",
          "Pregúntate quién observa al observador, y deja la pregunta sin responder. Como las reflexiones en los espejos, no tiene fin. Pero todos los niveles están ocurriendo AQUÍ."),
         ("Colapso en el Observador de Observadores", "3 minutos",
          "Suelta el esfuerzo de observar niveles. Deja que todos los observadores colapsen en UNO. No un observador más sino la FUENTE de toda observación. Descansa en ser el Observador de Observadores. "
          "Si en algún momento la pregunta trae extrañeza o la sensación de no estar del todo en ti, déjala: vuelve a los pies, a la respiración, a algo que puedas tocar. Abre los ojos despacio.")],
        "Un instante en que la atención se vuelve hacia quien mira. Puede llegar como amplitud, como quietud, como no poder ubicarte en un solo punto porque eres todos los puntos de observación a la vez. "
        "No hace falta retenerlo: siempre estuvo."))
    e.seccion("⚛️ ECUACIÓN SAGRADA", traduccion(
        "“El Observador de Observadores es el límite de la observación recursiva infinita, donde el observador y lo observado colapsan en identidad. "
        "No observa ALGO —ES la observación observándose eternamente.”"))
    e.seccion("🧬 CÓDIGOS DE ACTIVACIÓN", recordar(
        "Observo mi propia observación.", "Ojos viendo ojos, infinitamente.", "Más allá del más allá de mí.", "La observación observándose.",
        "Yo en yo en yo, sin fin.", "Infinitos observadores, un observador.", "Consciencia sin objeto ni sujeto."))
    e.rep("Cada hora, detente y observa:", "Tres veces en el día, detente y observa:")
    e.rep("Mírate al espejo y observa al que se mira. Luego observa al que observa al que se mira. Continúa hasta que sientas el vértigo de la recursividad infinita.",
          "Mírate al espejo un momento y observa al que se mira. Luego pregúntate quién observa al que se mira, y deja la pregunta abierta.")
    e.rep("Durante una conversación, obsérvate hablando, luego observa al que se observa hablar, luego sé consciente de todos los niveles simultáneamente mientras continúas la conversación.",
          "Durante una conversación, obsérvate hablando un instante, nota al que se observa hablar, y vuelve entero a quien te habla.")
    e.rep("Pasa el día completo como el Observador de Observadores. No como práctica sino como reconocimiento",
          "Vuelve al Observador de Observadores cada vez que lo recuerdes, sin esfuerzo. No como práctica sino como reconocimiento")
    e.firma(puerta_arquitectura(
        "Preguntar quién observa sin buscar respuesta es una práctica antigua: Bassui la hacía ante cada sonido; Ramana, ante cada pensamiento. "
        "Esa pregunta abierta es el Umbral V de <em>El Testigo</em>, Libro 3 de <em>Arquitectura del Destino</em>: «¿Quién oye este sonido?».",
        BASE_ARQ + "libro-03-el-testigo/L03-U5.html"))


# ------------------------------------------------------------------ NODO 3
def nodo_03(e):
    e.comunes()
    e.rep("Como el conjunto de Mandelbrot donde cada zoom revela la misma complejidad infinita, tu mente es un fractal",
          "Como el conjunto de Mandelbrot, donde cada acercamiento revela una complejidad sin fin y, escondidas, pequeñas copias del todo, tu mente es un fractal")
    e.rep("Tus células son fractales de tu consciencia. Cada una no solo está viva —es CONSCIENTE con el mismo patrón de consciencia que tú, solo que a una escala diferente. "
          "Tu consciencia corporal es el patrón fractal emergente de 37 trillones de consciencias celulares, cada una conteniendo el patrón completo pero expresándolo a su escala.",
          "Tus células son, como imagen, fractales de tu consciencia. Cada una vive a su escala: percibe su entorno y responde. "
          "De unos treinta billones de ellas, trabajando juntas, emerge el que siente: tu consciencia corporal, el mismo patrón de vida en otro tamaño.")
    e.seccion("🔬 LABORATORIO CUÁNTICO", lab(
        "Exploración de Tu Fractal de Consciencia",
        ["Una imagen fractal (física o digital)", "Una lupa o capacidad de zoom", "Tu atención capaz de cambiar escalas",
         "Disposición para perderte y encontrarte", "20 minutos de exploración fractal"],
        [("Contemplación del Patrón", "3 minutos",
          "Observa la imagen fractal completa. Nota cómo el mismo patrón se repite a diferentes escalas. Reconoce: tu consciencia tiene esta misma estructura. "
          "Cada pensamiento contiene la estructura de todos tus pensamientos."),
         ("Zoom hacia Adentro", "5 minutos",
          "Enfócate en una parte pequeña del fractal. Si tienes lupa o puedes ampliar la imagen, hazlo para ver más detalle. Observa: la complejidad no disminuye al acercarte. "
          "Igual tu consciencia: cada pensamiento contiene infinitos mundos."),
         ("Aplicación a Tu Mente", "5 minutos",
          "Toma un pensamiento simple actual. Acércate a él mentalmente: ¿qué pensamientos lo componen? Cada sub-pensamiento, examínalo: ¿qué contiene? "
          "Continúa hasta que el pensamiento se afloje y deje ver su trama. No hay fondo —es consciencia todo el camino hacia abajo. "
          "Si el ejercicio marea, abre los ojos y mira un objeto cercano: también él está hecho de escalas."),
         ("Zoom hacia Afuera", "5 minutos",
          "Ahora expande tu consciencia. Siente tu mente como parte de una mente familiar. La familia como parte de la mente cultural. La cultura como parte de la mente de Gaia. "
          "Continúa: es consciencia todo el camino hacia arriba."),
         ("Reconocimiento Fractal", "2 minutos",
          "Observa simultáneamente todas las escalas. Tu célula, tú, tu familia, Gaia, el cosmos. Todos el mismo patrón a diferentes escalas. Tú eres el fractal completo, no una escala.")],
        "La sensación de que no hay un “nivel base” de consciencia, de que cada escala refleja a todas las demás. Esa es la experiencia de ser un Fractal de Consciencia."))
    e.seccion("⚛️ ECUACIÓN SAGRADA", traduccion(
        "La regla del conjunto de Mandelbrot cabe en un renglón: elevar al cuadrado, sumar, repetir. De algo tan simple, repetido, nace una complejidad que no termina.",
        "“Tu consciencia total es el mismo patrón de consciencia iterado infinitamente a todas las escalas, desde lo infinitamente pequeño hasta lo infinitamente grande. "
        "No hay escala original —todas las escalas son igualmente fundamentales.”"))
    e.seccion("🧬 CÓDIGOS DE ACTIVACIÓN", recordar(
        "Mi mente es geometría recursiva.", "Infinito en cada escala.", "Todo en la parte, la parte en el todo.", "Todas las escalas a la vez.",
        "El mismo diseño, infinitamente.", "Sin fondo ni techo.", "Vivo en mi propia recursión."))
    e.rep("no hay pensamiento “átomico”", "no hay pensamiento “atómico”")
    e.rep("cada día contiene el patrón de tu vida completa, cada vida contiene el patrón de todas tus vidas, todas tus vidas contienen el patrón del universo.",
          "cada día contiene el patrón de tu vida completa, tu vida contiene el patrón de la vida, y la vida, el del universo.")
    e.rep("la ansiedad de ser “pequeño” en el universo desaparece.", "la ansiedad de ser “pequeño” en el universo se afloja.")
    e.firma()


# ------------------------------------------------------------------ NODO 4
def nodo_04(e):
    e.comunes()
    e.rep("Dentro de tu consciencia existe un espejo que no refleja luz sino REALIDAD misma. El Espejo Holográfico Interior no te muestra cómo te ves —te muestra cómo CREAS lo que ves. "
          "Todo lo que percibes “afuera” es un reflejo holográfico de configuraciones en tu espejo interior. No ves el mundo; ves tu espejo interior proyectado holográficamente como mundo.",
          "Dentro de tu consciencia existe un espejo que no refleja luz sino tu manera de ver. El Espejo Holográfico Interior no te muestra cómo te ves —te muestra CÓMO VES lo que ves. "
          "Todo lo que percibes “afuera” te llega teñido por las configuraciones de tu espejo interior. No ves el mundo desnudo: lo ves a través de tu espejo. "
          "Hermann von Helmholtz lo llamó en el siglo XIX inferencia inconsciente: el cerebro no registra el mundo como una cámara, lo anticipa y lo completa con lo que espera.")
    e.rep("Las personas en tu vida no son otros —son aspectos de tu Espejo Holográfico Interior tomando forma aparentemente externa. "
          "Por eso los mismos patrones se repiten con diferentes personas: no estás encontrando el mismo tipo de persona, estás proyectando el mismo aspecto de tu espejo. "
          "Cambias el espejo, cambia el reflejo, cambian las personas, cambia el mundo.",
          "Las personas en tu vida son otros, con su propio mundo, pero te llegan a través de tu Espejo Holográfico Interior. "
          "Por eso los mismos patrones pueden repetirse con personas distintas: no siempre encuentras el mismo tipo de persona; a veces miras con el mismo aspecto de tu espejo. "
          "Cambias el espejo, cambia el reflejo: cambia cómo ves a las personas, y con eso tu manera de estar entre ellas. "
          "Cuando lo que se repite es el daño, cuando alguien te lastima una y otra vez, eso no es un reflejo tuyo ni algo que debas limpiar por dentro: es daño, y se sale de él pidiendo ayuda.")
    e.rep("toma la forma de tus patrones internos y los proyecta como experiencia externa. No atraes tu realidad —la PROYECTAS desde tu espejo interior.",
          "toma la forma de tus patrones internos y tiñe con ellos tu experiencia. No atraes tu realidad ni la fabricas: la miras desde tu espejo interior, y esa mirada decide mucho de cómo la vives.")
    e.rep("El déjà vu ocurre cuando reconoces tu propio reflejo holográfico. Por un momento, ves a través de la ilusión y reconoces que lo “externo” es tu proyección interna. "
          "La sensación extraña no es de haber estado ahí antes, sino de reconocer súbitamente que TÚ estás creando el “ahí” desde tu espejo interior.",
          "La psicología estudia el déjà vu como una familiaridad que llega sin el recuerdo que la explique. Como imagen, quizá sea un instante en que te reconoces mirando: "
          "por un momento ves el espejo además de la escena. La sensación extraña no sería la de haber estado ahí antes, sino la de notar de golpe que hay alguien viendo el “ahí”.")
    e.rep("el esfuerzo de cambiar tu realidad externa es inútil mientras no reconozcas que es un reflejo.",
          "el esfuerzo de cambiar a los demás se agota mientras no reconozcas tu parte en lo que ves.")
    e.rep("Pero cuando intentas cambiar el espejo interior, también es inútil porque", "Pero cuando intentas cambiar el espejo interior a la fuerza, también se agota, porque")
    e.seccion("🔬 LABORATORIO CUÁNTICO", lab(
        "Configuración de Tu Espejo Holográfico Interior",
        ["Un cuenco con agua quieta", "Una cucharada de aceite", "Una pizca de sal", "Colorante alimenticio (opcional)",
         "Tu intención de ver tu reflejo interior", "15 minutos de alquimia especular"],
        [("Creación del Espejo Líquido", "2 minutos",
          "Llena el cuenco con agua hasta el borde. Espera que esté perfectamente quieta. Esta superficie es tu Espejo Holográfico Interior. Mírala hasta ver tu reflejo claramente."),
         ("Perturbación con Creencias", "3 minutos",
          "Añade gotas de aceite mientras piensas en tus creencias limitantes. Observa cómo el aceite distorsiona el reflejo. Cada creencia es una capa de distorsión en tu espejo. No juzgues, solo observa el patrón."),
         ("Densificación con Emociones", "3 minutos",
          "Espolvorea la sal mientras recuerdas una emoción difícil, el miedo o la ira, sin revivirla entera. La sal se disuelve y deja de verse, pero sigue en el agua. "
          "Así obran las emociones que no se nombran: no se ven y, aun así, cambian el sabor de todo."),
         ("Coloración con Expectativas", "3 minutos",
          "Si tienes colorante, añade una gota. Esto representa tus expectativas tiñendo la realidad. Todo se ve a través del color de tus expectativas. Tu espejo holográfico tiñe lo que ves."),
         ("Clarificación del Espejo", "4 minutos",
          "Con una cuchara, muy lentamente, crea un vórtice suave. Mientras giras, suelta mentalmente cada distorsión. Después deja el agua quieta y observa: "
          "el aceite vuelve a la superficie, la sal ya no se ve, el color se reparte. El agua no vuelve a ser la de antes, y aun así, cuando se aquieta, refleja otra vez. "
          "Lo mismo tu espejo: no se trata de borrar lo vivido sino de dejar que se asiente.")],
        "Una imagen de cómo se tiñe tu Espejo Holográfico Interior y de cómo vuelve a reflejar cuando se aquieta. Los patrones que viste en el agua son los mismos con que miras la realidad."))
    e.seccion("⚛️ ECUACIÓN SAGRADA", traduccion(
        "“La realidad que vives te llega a través de tu espejo holográfico interior: tiene la forma del mundo, el color de tus distorsiones y el brillo de la intensidad con que la miras. "
        "No experimentas la realidad en bruto —la experimentas a través de tu espejo.”"))
    e.seccion("🧬 CÓDIGOS DE ACTIVACIÓN", recordar(
        "Mi reflejo interior se aclara.", "Mi espejo mira con amor.", "Veo a través de mi propia proyección.", "En lo que veo, también me veo.",
        "Reconfiguro mi espejo desde el centro.", "Reconozco mi reflejo, y también al otro.", "Mi mirada se vuelve cristalina."))
    e.rep("Reconócelos como configuraciones de tu espejo interior, no como realidad externa. El patrón eres TÚ proyectado.",
          "Reconoce en ellos las configuraciones de tu espejo interior. En el patrón también estás TÚ.")
    e.rep("No lo que te muestran, sino lo que TÚ proyectas en ellos.", "No solo lo que te muestran: también lo que TÚ proyectas en ellos.")
    e.rep("Antes de dormir, “programa” tu espejo interior con la realidad que deseas proyectar mañana. No visualices el mundo —configura tu espejo.",
          "Antes de dormir, elige con qué mirada quieres despertar mañana: curiosa, amable, atenta. No visualices el mundo —configura tu espejo.")
    e.rep("Observa todo el día como si fuera una película proyectada desde tu interior. No estás EN el mundo —el mundo está EN tu proyección.",
          "Durante una hora, observa el día como si lo vieras a través de un cristal que lleva tu color. Nota qué parte es la escena y qué parte es el cristal.")
    e.rep("Cambia radicalmente un aspecto de tu espejo interior (una creencia, una emoción). Observa cómo la realidad externa se reconfigura en las próximas horas para reflejar el cambio.",
          "Cambia un aspecto pequeño de tu espejo interior, una expectativa o un juicio. Observa en las próximas horas qué cambia en cómo ves las cosas y en cómo les respondes.")
    e.rep("Trinidad holográfica completa. No cambies el mundo —sé consciente del espejo.",
          "Trinidad holográfica completa. Antes de cambiar el mundo, sé consciente del espejo.")
    e.rep("el mundo es tu espejo. No metafóricamente —LITERALMENTE. Cada experiencia es tu configuración interna proyectada holográficamente como realidad externa.",
          "el mundo te llega a través de tu espejo. No solo como metáfora: así trabaja la percepción. Cada experiencia lleva la huella de tu configuración interna.")
    e.rep("Cuando dejas de intentar cambiar el mundo y empiezas a limpiar tu espejo, la magia ocurre. No porque atraigas diferente realidad, sino porque PROYECTAS diferente realidad. "
          "Eres el proyector, la película, y la pantalla simultáneamente.",
          "Cuando, además de intentar cambiar el mundo, empiezas a limpiar tu espejo, la magia ocurre. No porque atraigas otra realidad, sino porque la VES de otra manera, "
          "y quien ve distinto responde distinto. Eres el que mira, la mirada y el cristal, todo a la vez.")
    e.rep("el mundo exterior ES tu multiverso interior proyectado a través de tu Espejo Holográfico. Cambias el espejo, cambias el mundo. Limpias el espejo, claríficas el mundo. "
          "Amas desde el espejo, el mundo se vuelve amor.",
          "el mundo exterior se vive a través de tu multiverso interior y de su Espejo Holográfico. Cambias el espejo, cambia tu mundo. Limpias el espejo, se aclara tu mundo. "
          "Amas desde el espejo, y lo que miras se vuelve amor.")
    # Poema del cierre
    e.rep("TODO es ese espejo.<br>", "TODO pasa por ese espejo.<br>")
    e.rep("es tu rostro<br>\n            en el Espejo Holográfico Interior<br>\n            tomando diferentes formas.<br>\n"
          "            No estás viendo el mundo —<br>\n            estás viendo tu espejo.<br>\n"
          "            No estás viviendo tu vida —<br>\n            estás viviendo tu reflejo.<br>",
          "te llega a través<br>\n            del Espejo Holográfico Interior,<br>\n            que le da su color.<br>\n"
          "            No estás viendo el mundo desnudo —<br>\n            lo estás viendo en tu espejo.<br>")
    e.rep("cuando reconoces que TODO es espejo,<br>\n            el mundo entero se transforma<br>",
          "cuando reconoces que TODO pasa por él,<br>\n            el mundo entero se ve distinto<br>")
    e.rep("en el único lugar que importa:<br>", "en el único lugar que siempre está a tu alcance:<br>")
    e.rep("donde nace toda realidad.”", "donde nace toda mirada.”")
    e.firma(puerta_portal(
        "Proyectar no es un error: es como trabaja la mente. El problema empieza cuando no sabemos que lo hacemos y amamos, o tememos, a la figura que construimos. "
        "Ver al otro real, más allá del propio espejo, se trabaja en <em>Encuentro Real</em>, Libro 3 del Portal Público, nodo 2: «Proyecciones cruzadas».",
        BASE_PORTAL + "03_Encuentro_Real/nodo_02.html"))


# ------------------------------------------------------------------ NODO 5
def nodo_05(e):
    e.comunes()
    e.rep("En la dimensión del miedo, las posibilidades se contraen.",
          "En la dimensión del miedo, las posibilidades se contraen. La psicóloga Barbara Fredrickson lo observó a su modo: el miedo estrecha lo que alcanzamos a pensar y a hacer, y la alegría lo amplía.")
    e.rep("Cada inhalación te mueve hacia dimensiones más expansivas. Cada exhalación te ancla en dimensiones más densas.",
          "Cada inhalación te abre; cada exhalación te asienta.")
    e.rep("Los recuerdos no están en el pasado —son dimensiones navegables en tu presente multiversal. Cuando “recuerdas”, no traes el pasado al presente; "
          "navegas tu consciencia a la dimensión donde ese evento sigue ocurriendo eternamente. Por eso los recuerdos pueden sentirse tan vívidos —estás literalmente ALLÍ de nuevo, "
          "navegando esa dimensión de tu multiverso interior.",
          "Los recuerdos no están guardados en el pasado —son dimensiones navegables en tu presente multiversal, y cada vez que entras en una, la reconstruyes. "
          "La neurociencia lo llama reconsolidación: recordar es volver a escribir, un poco, lo vivido. Por eso una memoria puede sentirse tan vívida y, a la vez, cambiar con los años. "
          "Cuando un recuerdo arrastra tanto que se vuelve a vivir como si ocurriera ahora, con el cuerpo en alarma, no se recorre a solas: es terreno para andar acompañado.")
    e.rep("Tu capacidad de imaginar futuros no es proyección —es navegación preliminar. Estás enviando sondas de consciencia a dimensiones futuras probables, "
          "explorando el terreno multidimensional antes de mover tu consciencia principal hacia allá. La intuición es tu sistema de navegación detectando las corrientes dimensionales "
          "y sugiriendo las rutas más armoniosas.",
          "Tu capacidad de imaginar futuros es navegación preliminar. Envías sondas de consciencia a dimensiones futuras probables y exploras el terreno antes de mover tu vida hacia allá. "
          "En 2013, Martin Seligman y otros tres investigadores propusieron llamarlo prospección, y sostuvieron que la mente humana se orienta más por el futuro que imagina que por el pasado que la empuja. "
          "La intuición es tu sistema de navegación: detecta las corrientes y sugiere rutas, aunque no las garantiza.")
    e.seccion("🔬 LABORATORIO CUÁNTICO", lab(
        "Navegación Consciente Entre Dimensiones Internas",
        ["Tu cuerpo como nave", "Tu respiración como motor", "Tu intención como timón", "Un diario de navegación", "20 minutos de exploración dimensional"],
        [("Calibración del Sistema de Navegación", "4 minutos",
          "Siéntate en posición cómoda, ojos cerrados. Respira profundamente estableciendo tu “punto cero”. Este es tu puerto base, tu dimensión de partida. Memoriza cómo se siente para poder regresar."),
         ("Navegación a Dimensión Emocional", "3 minutos",
          "Elige una emoción específica (alegría, paz, curiosidad). Con cada respiración, sintoniza esa frecuencia. No la “sientas” —NAVEGA hacia ella. Nota cómo toda tu realidad interna cambia al llegar."),
         ("Navegación a Dimensión Temporal", "4 minutos",
          "Desde esa dimensión emocional, navega a un recuerdo feliz; elige uno amable, porque los que duelen no se visitan a solas. Recórrelo como un lugar: la luz, los sonidos, quién estaba. "
          "Explora: ¿cómo se ve esta dimensión temporal desde tu estado actual? Si aparecen detalles que no recordabas, recíbelos como lo que son: la memoria que se rehace al visitarla."),
         ("Navegación a Dimensión Probable", "3 minutos",
          "Ahora navega a un futuro posible deseado. No lo imagines —VISÍTALO dimensionalmente. ¿Cómo se siente estar en esa dimensión? ¿Qué leyes diferentes operan allí?"),
         ("Navegación Multidimensional Simultánea", "3 minutos",
          "Mantén consciencia en las tres dimensiones a la vez. Presente, pasado, futuro, todos AHORA. Siente cómo no son lineales sino paralelas. Eres el navegante presente en todas simultáneamente."),
         ("Retorno al Puerto Base", "3 minutos",
          "Respira profundamente y regresa a tu punto cero. Pero ahora con consciencia de las rutas navegadas. Registra en tu diario las coordenadas dimensionales. Ahora sabes cómo navegar conscientemente.")],
        "Las primeras rutas de navegación consciente en tu multiverso interior: moverte entre estados, recuerdos y futuros con un poco más de libertad, sabiendo siempre dónde está tu puerto."))
    e.seccion("⚛️ ECUACIÓN SAGRADA", traduccion(
        "“Navegar es partir del punto cero, girar hacia el tono de tu destino y dejar que la transición lleve su tiempo. No viajas —giras hacia otro lado de ti.”"))
    e.seccion("🧬 CÓDIGOS DE ACTIVACIÓN", recordar(
        "Soy capitán de mi multiverso.", "Todas las direcciones disponibles.", "Elijo mi dimensión con conciencia.", "Viajo sin moverme.",
        "Abro portales en mi ser.", "Sintonizo nuevas dimensiones.", "Surco los océanos de mi ser."))
    e.rep("Practica navegar conscientemente entre estados emocionales. No las reprimas ni expreses —navega entre ellas como un capitán experto. De la calma a la excitación a la paz, conscientemente.",
          "Cuando llegue una emoción, nota en qué dimensión estás y cómo se ve el mundo desde ahí. No la reprimas ni la empujes: reconoce el territorio y elige desde dónde responder.")
    e.rep("Explora tu infancia como dimensión, tu adolescencia como otra. Son lugares en tu multiverso.",
          "Explora tu infancia como dimensión, tu adolescencia como otra. Son lugares en tu multiverso. Elige épocas amables; las que duelen esperan compañía.")
    e.rep("Cada futuro es una dimensión ya existente.", "Cada futuro es una dimensión de lo posible.")
    e.rep("<strong>DÍA 6 - MULTINAVEGACIÓN:</strong><br>\n            Practica estar presente en múltiples dimensiones simultáneamente. "
          "Mientras trabajas, mantén parte de tu consciencia navegando dimensiones de creatividad o paz.",
          "<strong>DÍA 6 - PUERTO EN MEDIO DEL DÍA:</strong><br>\n            Una vez en el día, en medio del trabajo, haz una pausa de tres respiraciones "
          "y visita la dimensión de la calma. Después vuelve entero a lo que hacías.")
    e.firma()


# ------------------------------------------------------------------ NODO 6
def nodo_06(e):
    e.comunes()
    e.rep('<div class="trinity-sub">Nodo 6 · La Sala de Control Cuántica</div>', '<div class="trinity-sub">Nodo 6 · La Sala sin Paredes</div>')
    e.rep("un lugar que no es lugar: La Sala de Control Cuántica. Desde aquí, no diriges tu vida —diriges TODAS tus vidas simultáneas en todos los universos paralelos internos. "
          "No es una metáfora ni una visualización —es el centro de comando real desde donde tu consciencia superior opera la compleja sinfonía de tu existencia multidimensional.",
          "un lugar que no es lugar: la Sala sin Paredes. Desde aquí no diriges tu vida: la ves entera, con todas tus versiones a la vista. "
          "No es un sitio al que se llega, sino el centro desde donde tu consciencia puede escuchar la compleja sinfonía de tu existencia multidimensional.")
    e.rep("La Sala de Control Cuántica no tiene paneles ni botones porque opera con intención pura. Cada pensamiento es un comando. Cada emoción ajusta parámetros. "
          "Cada decisión reconfigura las trayectorias de todos tus yoes paralelos. Desde aquí no controlas eventos —controlas PROBABILIDADES, inclinando las ondas de posibilidad hacia las realidades que eliges experimentar.",
          "La Sala no tiene paneles ni botones, porque no se opera con fuerza. Desde aquí no controlas eventos ni probabilidades: eliges cómo responder a lo que llega. "
          "Viktor Frankl lo vio en el lugar más extremo: cuando todo lo demás le había sido quitado, quedaba la última de las libertades humanas, elegir la propia actitud. "
          "Esa es la palanca que la Sala ofrece, y alcanza.")
    e.rep("Tu glándula pineal es la antena física de tu Sala de Control Cuántica. Cuando meditas, cuando sueñas lúcidamente, cuando tienes momentos de claridad cristalina, "
          "estás temporalmente consciente en tu Sala de Control. Esos momentos de “saber” absoluto son cuando accedes brevemente a la perspectiva desde donde puedes ver todas tus líneas temporales simultáneamente.",
          "Descartes creyó que la glándula pineal era el lugar donde el alma actúa sobre el cuerpo; hoy se sabe que esa glándula regula los ritmos del sueño. La Sala no está en ningún órgano. "
          "Cuando meditas, cuando sueñas con lucidez, cuando tienes momentos de claridad cristalina, estás por un momento consciente en tu Sala. "
          "Esos instantes en que “sabes” son los que te dejan ver tu vida desde más arriba, con sus caminos a la vista.")
    e.rep("Desde la Sala de Control Cuántica puedes ver los hilos que conectan todos los eventos de tu vida. Lo que parece caos desde el nivel de la calle se revela como diseño perfecto desde la sala de control. "
          "Cada sincronicidad fue orquestada desde aquí. Cada encuentro “casual” fue coordinado desde este centro de comando cuántico.",
          "Desde la Sala puedes ver los hilos que unen los hechos de tu vida. Lo que parece caos desde el nivel de la calle muestra, visto desde arriba, una trama con sentido. "
          "No porque alguien la haya orquestado, sino porque desde aquí puedes leerla: el sentido se encuentra al mirar, no se fabrica.")
    e.rep("La Sala de Control no está en tu futuro esperando que evoluciones lo suficiente para accederla. Está AHORA, siempre ha estado, operando continuamente. "
          "La única diferencia entre un maestro y un principiante es el grado de consciencia de estar en la Sala de Control. El maestro SABE que cada momento está eligiendo desde allí; el principiante cree que la vida le sucede.",
          "La Sala no está en tu futuro esperando que evoluciones lo suficiente para entrar. Está AHORA, siempre ha estado. "
          "Lo que cambia es cuánto lo recuerdas: hay días en que eliges desde allí y días en que la vida te arrastra, y en los dos estás invitado a volver.")
    e.rep("“Tienes control total desde la Sala de Control Cuántica, pero ese control solo funciona cuando sueltas el control. Puedes dirigir todo cuando no diriges nada. "
          "El mayor poder viene de reconocer que la Sala de Control se opera a sí misma a través de ti, y tú a través de ella, en un loop infinito donde controlador y controlado son uno.”",
          "“Desde tu Sala tienes el control, pero ese control solo funciona cuando sueltas el control. Puedes dirigir todo cuando no diriges nada. "
          "El mayor poder viene de reconocer que la Sala se opera a sí misma a través de ti, y tú a través de ella, en un círculo infinito donde controlador y controlado son uno.”")
    e.rep("Esta paradoja revela que la Sala de Control Cuántica no es un lugar de poder", "Esta paradoja revela que la Sala sin Paredes no es un lugar de poder")
    e.seccion("🔬 LABORATORIO CUÁNTICO", lab(
        "Acceso Consciente a Tu Sala sin Paredes",
        ["Una silla firme", "Un lugar tranquilo, con poca luz o los ojos cerrados", "Tu imaginación arquitectónica",
         "Disposición para mirar desde el centro", "15 minutos de instalación en el centro"],
        [("Activación del Acceso", "3 minutos",
          "Siéntate en la silla con los pies en el suelo y cierra los ojos. Respira profundamente 7 veces. Con cada respiración, siente que asciendes. No hacia arriba sino hacia ADENTRO, hacia tu centro."),
         ("Giro de Sintonización", "2 minutos",
          "Sin moverte de la silla, imagina que giras lentamente sobre tu eje. Con cada giro, sintoniza una frecuencia más profunda. El giro no es físico —es dimensional. "
          "Estás girando a través de capas de realidad hacia tu centro."),
         ("Entrada a la Sala", "3 minutos",
          "Detén el giro cuando “sientas” que llegaste. Visualiza/siente tu Sala sin Paredes. No la imagines —RECONÓCELA. ¿Cómo es? ¿Qué “pantallas” de realidad ves? ¿Qué “controles” sientes disponibles?"),
         ("Revisión del Paisaje", "2 minutos",
          "Desde tu sala, observa tu vida como un paisaje: lo que fue, lo que es, lo que podría ser. Ve los hilos que lo conectan. Identifica un punto donde tu respuesta depende de ti."),
         ("Ajuste Interior", "2 minutos",
          "Elige UNA cosa que quieres cambiar en tu manera de responder. No la fuerces: decide, desde la Sala, cuál será tu primer gesto pequeño. No mueves la realidad —inclinas tu respuesta."),
         ("Anclaje del Acceso", "3 minutos",
          "Antes de “salir”, crea una señal de acceso rápido. Un gesto, una palabra, una respiración específica. Esta será tu “llave” para acceso instantáneo. Practica: sal y entra tres veces usando tu llave.")],
        "Un camino de regreso a tu centro, con su llave. En los próximos días, puede que notes que respondes un poco distinto: ese es el ajuste. Lo demás, la vida lo trae."))
    e.seccion("⚛️ ECUACIÓN SAGRADA", traduccion(
        "“Desde tu Sala ves a la vez lo que pasa, lo que sientes y lo que quieres, y eliges con todo eso a la vista. No controlas los hechos —eliges desde dónde responderles.”"))
    e.seccion("🧬 CÓDIGOS DE ACTIVACIÓN", recordar(
        "Entro en mi centro.", "Todas mis respuestas disponibles.", "Respondo desde ahí.", "Habito mi Sala sin Paredes.",
        "Cambios pequeños, efectos hondos.", "Veo mi vida entera.", "Dirijo permitiendo, permito dirigiendo."))
    e.rep("Dedica 15 minutos a explorar tu Sala de Control Cuántica.", "Dedica 10 minutos a explorar tu Sala sin Paredes.")
    e.rep("<strong>DÍA 2 - MONITOREO DE LÍNEAS:</strong><br>\n            Desde tu Sala, observa tus diferentes líneas temporales activas. No las cambies, solo obsérvalas. ¿Cuáles están convergiendo? ¿Cuáles divergiendo?",
          "<strong>DÍA 2 - LOS CAMINOS ABIERTOS:</strong><br>\n            Desde tu Sala, observa los caminos que tu vida tiene abiertos. No los cambies, solo obsérvalos. ¿Cuáles se acercan? ¿Cuáles se alejan?")
    e.rep("Haz pequeños ajustes a probabilidades: inclina levemente la probabilidad de un encuentro feliz, de una solución creativa, de una sincronicidad. Observa los resultados.",
          "Haz un ajuste menor en ti: una disposición más abierta a un encuentro, a una solución creativa, a notar una coincidencia con sentido. Observa qué llega.")
    e.rep("<strong>DÍA 5 - PROGRAMACIÓN DE SUEÑOS:</strong><br>\n            Antes de dormir, desde tu Sala de Control, programa las dimensiones que visitarás en sueños.",
          "<strong>DÍA 5 - INTENCIÓN PARA LOS SUEÑOS:</strong><br>\n            Antes de dormir, desde tu Sala, elige las dimensiones que quieres visitar en sueños.")
    e.rep("<strong>DÍA 6 - OPERACIÓN REMOTA:</strong><br>\n            Practica operar tu Sala de Control mientras haces otras cosas. Cocinar mientras ajustas probabilidades. Caminar mientras monitoreas líneas temporales.",
          "<strong>DÍA 6 - VOLVER EN MEDIO DEL DÍA:</strong><br>\n            Practica volver a tu Sala en medio de lo cotidiano, por un instante, con tu llave: al caminar, al esperar, antes de responder un mensaje.")
    e.rep("<strong>DÍA 7 - MAESTRÍA DEL CONTROL:</strong><br>\n            Vive todo el día sabiendo que estás simultáneamente en tu vida Y en tu Sala de Control.",
          "<strong>DÍA 7 - CONTROL SIN CONTROL:</strong><br>\n            Vive todo el día sabiendo que estás simultáneamente en tu vida Y en tu Sala.")
    e.rep("La Sala de Control Cuántica no es un lugar de escape de tu vida —es el lugar desde donde CREAS tu vida momento a momento. "
          "No es un refugio del caos sino el centro desde donde orquestas la sinfonía del caos en armonía.",
          "La Sala sin Paredes no es un lugar de escape de tu vida —es el lugar desde donde la HABITAS, momento a momento. "
          "No es un refugio del caos sino el centro desde donde el caos puede escucharse como música.")
    e.rep("Ahora entiendes por qué algunas personas parecen tener “suerte”: están consciente o inconscientemente operando desde su Sala de Control, ajustando probabilidades constantemente a su favor. "
          "No es magia —es ingeniería cuántica de realidad.",
          "Ahora entiendes algo de lo que llamamos “suerte”: quien vive más cerca de su centro ve más caminos y los toma a tiempo. "
          "El psicólogo Richard Wiseman lo estudió durante años: las personas que se consideran afortunadas suelen estar más abiertas a las oportunidades que pasan cerca. "
          "Pero la suerte también tiene una parte que no depende de nadie, y la desgracia no prueba que alguien se haya alejado de su Sala.")
    e.rep("Tu Sala de Control Cuántica ha estado operando toda tu vida. Cada vez que “sabías” que algo iba a pasar, cada vez que “sentiste” que debías tomar cierto camino, "
          "cada vez que una “casualidad” te salvó —eras TÚ desde tu Sala de Control, orquestando tu propia experiencia.",
          "Tu Sala ha estado abierta toda tu vida. Cada vez que “sabías” que algo iba a pasar, cada vez que “sentiste” que debías tomar cierto camino, "
          "cada vez que supiste aprovechar una “casualidad”, eras TÚ desde tu centro, escuchando antes de pensar.")
    e.rep("Tu Sala de Control Cuántica<br>", "Tu Sala sin Paredes<br>")
    e.rep("de crear tu realidad.”", "de habitar tu vida.”")
    e.firma()


# ------------------------------------------------------------------ NODO 7
def nodo_07(e):
    e.comunes()
    e.rep("La esquizofrenia sagrada de contener múltiples realidades no es locura —es CORDURA CUÁNTICA. La capacidad de ser uno y muchos, aquí y allá, ahora y siempre, simultáneamente, es tu estado natural. "
          "La “enfermedad” fue creer que solo podías ser uno. La sanación es reconocer que eres infinito unificado.",
          "Contener muchas realidades interiores no es locura: es lo humano. La cordura no consiste en ser uno solo, sino en que tus muchos se reconozcan en la misma casa. "
          "Cuando esa casa se quiebra de verdad, cuando lo que se oye o se cree ya no puede compartirse con nadie, no es un estado más alto: es un dolor que pide cuidado y compañía. "
          "La sanación es reconocer que eres muchos y uno a la vez.")
    e.rep("tu Sala de Control Cuántica —todo siempre fue UNO", "tu Sala sin Paredes —todo siempre fue UNO")
    e.seccion("🔬 LABORATORIO CUÁNTICO", lab(
        "Gesto de Unificación Multiversal",
        ["7 piedras o semillas pequeñas, una por cada nodo de este libro", "Una superficie despejada frente a ti", "Tu presencia total",
         "La intención de reconocimiento", "20 minutos para la unificación"],
        [("Círculo de Universos", "3 minutos",
          "Coloca las 7 piedras en círculo frente a ti. Al dejar cada una, nombra un universo interno: “Universo del amor”, “Universo del miedo”, “Universo de la creatividad”… "
          "Reconoce que cada piedra es un universo completo."),
         ("Reconocimiento de Multiplicidad", "3 minutos",
          "Recorre el círculo con la mirada, piedra por piedra. Siente cómo cada una representa una versión completa de ti. No fragmentos —universos completos. Todos vivos, todos tú."),
         ("Convergencia al Centro", "4 minutos",
          "Muy lentamente, mueve cada piedra hacia el centro. Con cada movimiento di: “Este universo SOY YO”. Continúa hasta que todas estén juntas. Lo que estaba disperso parece ahora una sola forma."),
         ("La Mano que Reúne", "3 minutos",
          "Toma las siete piedras en tus manos, o apoya las manos sobre ellas. Siente su peso junto. Ese puñado eres tú multiversal: uno y muchos, unificado y múltiple simultáneamente."),
         ("Declaración de Unificación", "3 minutos",
          "Di en voz baja, o en silencio:<br>\n              “YO SOY todos mis universos<br>\n              YO SOY todas mis versiones<br>\n              YO SOY todo mi multiverso<br>\n"
          "              Unificado en este momento eterno<br>\n              Múltiple en mi unidad<br>\n              Uno en mi multiplicidad<br>\n              YO SOY EL MULTIVERSO INTERIOR”"),
         ("Integración de la Unificación", "4 minutos",
          "Devuelve las piedras a su lugar una por una. Con cada una que sueltas, siente cómo no desaparece: se integra más profundamente en tu unidad. "
          "Cuando hayas terminado, siente: todos los universos laten ahora dentro de ti —unificados, eternos, uno.")],
        "No has unido nada —has reconocido con las manos lo que siempre fue uno. El gesto lleva al cuerpo lo que tu ser multiversal siempre supo."))
    e.seccion("⚛️ ECUACIÓN SAGRADA", traduccion(
        "“Si sumaras todos tus yoes, en todos los tiempos, en todas las dimensiones, el resultado sería siempre UNO. No importa cuán infinito sea tu multiverso: siempre se unifica en la singularidad del YO SOY.”"))
    e.seccion("🧬 CÓDIGOS DE ACTIVACIÓN", recordar(
        "Yo soy todos mis universos.", "Infinito, uno, yo.", "Multiverso unificado: la paradoja habitada.", "Todo yo, aquí, ahora.",
        "Uno en todos, todos en uno.", "Completo siempre fui."))
    e.rep("No te levantes hasta sentir la unificación completa.", "Quédate un minuto antes de levantarte, sintiendo la unificación.")
    e.rep("Ve cada problema como una invitación a mayor unificación. ¿Qué aspectos de tu multiverso necesitan reconocerse como uno para que el “problema” se disuelva?",
          "Toma un problema del día como una invitación a mayor unificación. ¿Qué partes de ti están en desacuerdo frente a él? Cuando se escuchan, el problema no siempre se disuelve, pero se vuelve más claro.")
    e.rep("Tu sensación de separación fue tu unidad jugando", "Tu sensación de separación, aun cuando dolió, fue también tu unidad jugando")
    e.rep("cada momento operas desde tu Sala de Control Cuántica,", "cada momento puedes volver a tu Sala sin Paredes,")
    # La firma del nodo sale entera: el nodo cierra con la de la serie, al final.
    e.sin_firma(cual=0, total=2)
    e.rep("<li>Todo lo externo es tu espejo holográfico interior</li>", "<li>Todo lo externo te llega a través de tu espejo holográfico interior</li>")
    e.rep("<li>Tienes una Sala de Control Cuántica siempre operativa</li>", "<li>Tienes una Sala sin Paredes siempre abierta</li>")
    e.rep("Cada libro fue una iniciación. Cada nodo fue una activación. Cada práctica fue un recordatorio",
          "Cada libro fue una puerta. Cada nodo, una manera de mirar. Cada práctica, un recordatorio")
    e.rep("<li>Un Arquitecto Cuántico de tu realidad</li>", "<li>Un Arquitecto Cuántico que diseña con la luz que no inventó</li>")
    e.rep("<li>Una Simetría Rota perfecta</li>", "<li>Una Simetría Rota que deja pasar la luz</li>")
    # Sale el bloque de transmisión final; queda una línea.
    pat = r'<div class="trinity-sign">.*?</div>'
    if len(re.findall(pat, e.s, flags=re.S)) != 1:
        raise SystemExit("[nodo_07.html] firma final")
    e.s = re.sub(pat, lambda m: ('<p class="trinity-p cierre-final">Tú estás completo. Siempre lo estuviste.</p>\n'
                                 f'{I10}{FIRMA}\n'
                                 f'{I10}<!-- Puerta anotada: 13.7 → Habitar (Libro 13 de Arquitectura del Destino), para cuando exista. -->'),
                 e.s, count=1, flags=re.S)
    e.n += 1
    e.rep('<a href="index.html">Index del Libro 13 →</a>', '<a href="index.html">Índice del Libro 13 →</a>')


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
