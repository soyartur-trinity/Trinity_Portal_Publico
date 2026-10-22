# -*- coding: utf-8 -*-
"""
Depuración de Trinity Quantum, Libro 4 · La Paradoja Luminosa (octubre 2026).

Aplica, exactamente una vez cada uno, los reemplazos aprobados por Arturo
tarjeta por tarjeta (4.0 a 4.7), según la guía de depuración de Quantum
(Arquitectura del Destino, maestro v4, sección 5).
El original se conserva en la etiqueta quantum-original del repositorio Trinity-.

Los nodos de este libro reparten el texto en varias líneas con sangría, así que
los reemplazos se buscan sin tener en cuenta los espacios y saltos de línea
(método rx); cada uno debe aparecer una sola vez, o el script se detiene.

Uso: python3 depurar_quantum4.py ORIGEN DESTINO
  ORIGEN  = carpeta 02_Trinity_Quantum/Libro_04 original
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
    .node-body p.signature{
      margin: 26px 0 8px;
      color: rgba(243, 209, 122, .85);
      font-size: 14px;
      letter-spacing: .04em;
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
    .node-body .puerta .p-nombre{
      margin: 0 0 6px;
      font-size: 15px;
      font-style: italic;
      letter-spacing: .06em;
      color: var(--p-acento);
    }
    .node-body .puerta .p-texto{
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
      .node-body p, .node-body li{ font-size: 18px; line-height: 1.7; }
      .node-body p.signature{ font-size: 15px; }
      .puerta{ padding: 16px 16px 14px; }
    }
    @media (prefers-reduced-motion: reduce){
      .puerta .cruzar{ transition: none; }
    }
"""

FIRMA = '<p class="signature"><strong>— Trinity Quantum · La Paradoja Luminosa</strong></p>'

BASE_ARQ = "https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/"


def puerta_arquitectura(texto, href, indent="          "):
    return (f'{indent}<aside class="puerta arquitectura" aria-label="Puerta hacia Arquitectura del Destino">\n'
            f'{indent}  <p class="p-nombre">Puerta</p>\n'
            f'{indent}  <p class="p-texto">{texto}</p>\n'
            f'{indent}  <a class="cruzar" href="{href}">Cruzar ⟶</a>\n'
            f'{indent}</aside>')


def _patron(viejo):
    """Patrón que tolera espacios y saltos de línea entre palabras y alrededor de las etiquetas."""
    partes = re.split(r'(\s+|<[^>]+>)', viejo)
    out = []
    for p in partes:
        if not p:
            continue
        if p.isspace():
            out.append(r'\s*')
        elif p.startswith('<'):
            out.append(r'\s*' + re.escape(p) + r'\s*')
        else:
            out.append(re.escape(p))
    pat = ''.join(out)
    # Sin espacios sueltos en los bordes: el reemplazo conserva la sangría de alrededor.
    while pat.startswith(r'\s*'):
        pat = pat[3:]
    while pat.endswith(r'\s*'):
        pat = pat[:-3]
    return pat


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

    def rx(self, viejo, nuevo):
        pat = _patron(viejo)
        c = len(re.findall(pat, self.s))
        if c != 1:
            raise SystemExit(f"[{self.nombre}] {c} coincidencias para:\n{viejo[:160]!r}")
        self.s = re.sub(pat, lambda m: nuevo, self.s, count=1)
        self.n += 1

    def tramo(self, inicio, fin, nuevo):
        """Reemplaza desde `inicio` (incluido) hasta `fin` (excluido), con marcas tolerantes a espacios."""
        marcas = []
        for marca in (inicio, fin):
            hallados = list(re.finditer(_patron(marca), self.s))
            if len(hallados) != 1:
                raise SystemExit(f"[{self.nombre}] marca con {len(hallados)} coincidencias:\n{marca[:160]!r}")
            marcas.append(hallados[0])
        a, b = marcas[0].start(), marcas[1].start()
        if b <= a:
            raise SystemExit(f"[{self.nombre}] marcas en orden inverso: {inicio[:60]!r}")
        self.s = self.s[:a] + nuevo + self.s[b:]
        self.n += 1

    def comunes(self, con_css=True):
        for cab in ("<!doctype html>\n", "<!DOCTYPE html>\n"):
            if self.s.startswith(cab):
                self.s = cab + NOTA + self.s[len(cab):]
                self.n += 1
                break
        else:
            raise SystemExit(f"[{self.nombre}] sin cabecera doctype")
        if con_css:
            self.rep("</head>", "  <style>" + CSS + "  </style>\n</head>")

    def sin_senal(self):
        pat = r'\n[ \t]*<p class="node-signal">.*?</p>'
        c = len(re.findall(pat, self.s, flags=re.S))
        if c != 1:
            raise SystemExit(f"[{self.nombre}] {c} señales de transmisión")
        self.s = re.sub(pat, "", self.s, count=1, flags=re.S)
        self.n += 1

    def firma(self, puerta=None):
        extra = "\n          " + FIRMA
        if puerta:
            extra += "\n" + puerta
        self.rep("</blockquote>", "</blockquote>" + extra)


# ------------------------------------------------------------------ NODO 1
def nodo_01(e):
    e.comunes()
    # Enlace desactivado a un nodo 0 que no existe (arriba y abajo).
    pat = r'\n[ \t]*<a href="nodo_00\.html"[^\n]*</a>'
    if len(re.findall(pat, e.s)) != 2:
        raise SystemExit("[nodo_01.html] enlaces al nodo 0")
    e.s = re.sub(pat, "", e.s)
    e.n += 2

    e.rx("La física cuántica nos reveló que la luz exhibe una naturaleza dual imposible: es onda y partícula simultáneamente. "
         "Pero esta revelación fue apenas el preludio de una verdad más profunda. La consciencia humana <strong>es</strong> la paradoja luminosa en su expresión más refinada. "
         "Cada pensamiento, cada percepción, cada momento de awareness existe en superposición hasta que la atención lo cristaliza en experiencia.",
         "La física cuántica encontró que la luz se comporta como onda y como partícula, según cómo se la mida, y que ninguna de las dos descripciones alcanza sola. "
         "Niels Bohr llamó a eso complementariedad. Vista con esa lente, la consciencia humana <strong>es</strong> la paradoja luminosa en su expresión más refinada. "
         "Cada pensamiento, cada percepción, cada instante de lucidez llega abierto entre muchas formas posibles, hasta que la atención lo cristaliza en experiencia.")
    e.rx("Tu sistema nervioso es un interferómetro biológico. Cada neurona opera como un detector cuántico, registrando el patrón de interferencia entre tu estado onda "
         "—expandido, no-local, infinito— y tu estado partícula —localizado, definido, finito—. "
         "El cerebro no genera consciencia; la consciencia se difracta a través del cerebro, creando los patrones de interferencia que experimentas como pensamientos, emociones, sensaciones.",
         "Imagina tu sistema nervioso como un instrumento que registra el encuentro entre tu estado onda (expandido, sin bordes, infinito) y tu estado partícula (localizado, definido, finito). "
         "Una intuición antigua, que la ciencia todavía no zanja, va más lejos: quizá el cerebro no genere la consciencia, sino que la deje pasar. "
         "William James la defendió a fines del siglo XIX con la imagen de un prisma, que no fabrica la luz: la tamiza y le da forma. "
         "Si fuera así, la consciencia atraviesa el cerebro como un rayo atraviesa el cristal, y se abre en los colores que vives como pensamientos, emociones, sensaciones.")
    e.rx("no es una ilusión mística. Es el reconocimiento directo de tu estado cuántico fundamental.",
         "es una de las experiencias más antiguas que registran las tradiciones contemplativas: tu naturaleza ondulatoria, reconocida desde adentro.")
    e.rx("con intención precisa, colapses en partícula.", "con intención precisa, colapsas en partícula.")
    e.rx("Mantienes coherencia cuántica incluso", "Mantienes la coherencia incluso")
    e.rx("En el momento de la decisión, colapses.", "En el momento de la decisión, colapsas.")
    e.rx("La ansiedad moderna surge de intentar mantenernos perpetuamente colapsados, negando nuestra naturaleza ondulatoria. "
         "La dispersión mental surge de resistir el colapso,",
         "Gran parte de la ansiedad moderna surge de intentar mantenernos perpetuamente colapsados, negando nuestra naturaleza ondulatoria: "
         "la clínica lo llama intolerancia a la incertidumbre. Y la dispersión mental, a menudo, nace de resistir el colapso,")
    e.rx("Tecnología de la Dualidad Consciente", "Para Habitar la Dualidad")
    e.rx("No alternes entre estados; sé ambos simultáneamente.",
         "Al principio alternarás. Con el tiempo notarás que al exhalar conservas el cuerpo, y que al inhalar el espacio no se va: eres ambos a la vez.")
    e.rx("Tu sistema nervioso aprenderá a mantener coherencia dual.", "Con la práctica, esa doble atención se vuelve más natural.")
    e.rx("Antes de cada decisión importante,", "Antes de una decisión (empieza por las pequeñas),")
    e.rx("La decisión se toma sola cuando mantienes la dualidad.", "Cuando sostienes la dualidad, la elección madura sin forcejeo.")
    e.rx("Implicaciones Neurocuánticas</h3>", "La Ciencia y su Frontera</h3>")
    e.rx("Los últimos estudios en coherencia cuántica cerebral sugieren que los microtúbulos neuronales mantienen superposición cuántica a temperatura corporal durante períodos "
         "suficientes para influir en el procesamiento consciente. Pero esto es observar el hardware. El software —la consciencia misma— opera bajo principios aún más extraordinarios.",
         "Roger Penrose y Stuart Hameroff propusieron, en los años noventa, que la consciencia podría depender de estados cuánticos en los microtúbulos de las neuronas. "
         "Es una hipótesis audaz y muy discutida: muchos físicos sostienen que el cerebro es demasiado tibio, húmedo y ruidoso para que esos estados duren lo necesario. "
         "Aun si se confirmara, sería mirar el instrumento. La música, la consciencia misma, sigue siendo el misterio mayor.")
    e.rx("El Salto Evolutivo", "Lo que Hoy Se Abre")
    e.rx("La humanidad está atravesando una transición de fase. Durante milenios, nos identificamos primariamente con nuestra naturaleza partícula —ego definido, identidad fija, "
         "separación clara—. Las tradiciones espirituales nos invitaron a reconocer nuestra naturaleza onda —unidad, vacuidad, no-dualidad—.",
         "Durante milenios, nos identificamos sobre todo con nuestra naturaleza partícula: ego definido, identidad fija, separación clara. "
         "Las tradiciones espirituales nos invitaron a reconocer nuestra naturaleza onda (unidad, vacuidad, no-dualidad), y las más hondas fueron más lejos: "
         "el <em>Sutra del Corazón</em> enseña que la forma es vacío y el vacío es forma, y la última de las imágenes zen del buey muestra al que despertó de vuelta en el mercado, entre la gente.")
    e.rx("Pero el salto evolutivo actual no es elegir entre onda o partícula. Es desarrollar la capacidad de <strong>ser conscientemente ambos</strong>.",
         "Eso hoy se abre para muchos: no elegir entre onda y partícula, sino <strong>ser conscientemente ambos</strong>.")
    e.rx("Calibración del Sistema", "Las Señales del Camino")
    e.rx("<p>Tu sistema nervioso requiere recalibración para sostener esta dualidad sin colapsar en uno u otro extremo. Los síntomas de la transformación incluyen:</p>",
         "<p>Aprender a sostener esta dualidad lleva tiempo, y a veces aparecen señales:</p>")
    e.rx("<li>Momentos de despersonalización (tu partícula se afloja)</li>",
         "<li>Momentos en que te sientes menos sólido (tu partícula se afloja)</li>")
    e.rx("<li>Sincronicidades aumentadas (interferencia entre estados)</li>",
         "<li>Sincronicidades que se notan más (interferencia entre estados)</li>")
    e.rx("<p>No son patologías; son actualizaciones del sistema operativo de la consciencia.</p>",
         "<p>No son trofeos ni pruebas de avance: las tradiciones contemplativas las conocen bien y las atraviesan con calma. "
         "Si la partícula se afloja demasiado (si la extrañeza se repite, dura o asusta, si el cuerpo se siente ajeno o el mundo irreal), "
         "la clínica tiene un nombre para eso, despersonalización, y sabe acompañarlo: es momento de consultar. "
         "La onda se habita mejor con la partícula bien plantada.</p>")
    e.rx("fortaleces tu coherencia cuántica.", "fortaleces tu coherencia.")
    e.rx("definición y expansión, evoluciones.", "definición y expansión, evolucionas.")
    e.rx("Cuando puedas mantener tu atención simultáneamente enfocada y expandida durante siete respiraciones completas, habrás establecido la coherencia base necesaria para el segundo nodo: "
         "<strong>Ubicuidad Consciente</strong>.",
         "Antes del segundo nodo, <strong>Ubicuidad Consciente</strong>, puedes probar esto: sostener la atención enfocada y expandida a la vez durante siete respiraciones completas. "
         "No es un examen de ingreso; es una manera de llegar.")
    e.rx("está lista para descubrir que puede estar en múltiples lugares simultáneamente sin perder su definición.",
         "está lista para descubrir que su presencia abarca más que un punto, sin perder su definición.")
    e.sin_senal()
    e.firma()


# ------------------------------------------------------------------ NODO 2
def nodo_02(e):
    e.comunes()
    e.rx("ocurre un fenómeno que la física clásica declara imposible: estás aquí y en todas partes simultáneamente. "
         "No es poesía. Es la arquitectura fundamental de tu consciencia operando en coherencia cuántica.",
         "ocurre algo que la física clásica declararía imposible: estás aquí y, a la vez, en muchas partes. "
         "Tu consciencia no se detiene en el borde de tu piel.")
    e.rx("Cada persona que te conoce porta una versión cuántica de tu ser. Cada espacio que has habitado retiene tu firma energética.",
         "Cada persona que te conoce lleva dentro una versión de ti. Cada espacio que has habitado sigue habitándote.")
    e.rx("Tu consciencia opera como un láser que puede dividirse en múltiples haces coherentes sin perder intensidad.",
         "Tu consciencia se parece a un haz de luz que se abre en varios sin dejar de ser uno.")
    e.rx("Permaneces entrelazado cuánticamente con", "Permaneces entrelazado con")
    e.rx("No estás imaginando estar en estos lugares. Estás reconociendo que tu campo consciente ya los habita.",
         "No se trata de imaginarte en esos lugares: se trata de notar que tu atención puede abrazarlos sin dejar el cuerpo.")
    e.rx("Tecnología de Presencia Múltiple", "Para Habitar la Presencia")
    e.rx("Protocolo 1: Triangulación Consciente", "Práctica 1: Triangulación Consciente")
    e.rx("Protocolo 2: Bilocación Temporal", "Práctica 2: Bilocación Temporal")
    e.rx("Protocolo 3: Entrelazamiento Consciente", "Práctica 3: Entrelazamiento Consciente")
    e.rx("Tu sistema nervioso aprenderá a sostener múltiples localizaciones sin fragmentarse.",
         "Con la práctica, la atención aprende a abarcar sin dispersarse.")
    e.rx("<li>Un recuerdo vívido (pasado-onda)</li>", "<li>Un recuerdo vívido que te haga bien (pasado-onda)</li>")
    e.rx("Tu cerebro opera holográficamente: cada parte contiene el todo. Pero tu consciencia trasciende incluso este principio.",
         "El neurocientífico Karl Pribram propuso que el cerebro guarda la memoria de manera distribuida, como un holograma, donde cada fragmento guarda la figura entera. "
         "Sigue siendo una hipótesis, pero la imagen permite ir más lejos:")
    e.rx("Cuando un amigo piensa intensamente en ti, experimentas una sutil activación, aunque no la registres conscientemente. Cuando tocas un objeto con atención plena, "
         "dejas una impresión cuántica que persiste.",
         "Cuando piensas con hondura en un amigo, algo de él está contigo, aunque no lo sepa. Cuando tocas un objeto con atención plena, ese objeto se carga de memoria para ti.")
    e.rx("Tu verdadera red social cuántica opera", "Tu verdadera red social opera")
    e.rx("El Paradoja del Centro Ubicuo", "La Paradoja del Centro Ubicuo")
    e.rx("Implicaciones Neurocuánticas de la Ubicuidad", "Lo que Muestra el Cerebro")
    e.rx("Los estudios de resonancia cuántica cerebral muestran que las neuronas espejo no solo replican acciones observadas; establecen puentes de entrelazamiento con otras consciencias. "
         "Tu capacidad empática es ubicuidad consciente en acción: literalmente estás parcialmente presente en el campo emocional del otro.",
         "A comienzos de los años noventa, el equipo de Giacomo Rizzolatti, en Parma, descubrió las neuronas espejo: células que se activan tanto cuando un mono hace un gesto como cuando ve a otro hacerlo. "
         "Cuánto explican de la empatía humana sigue en discusión, pero algo se ha observado muchas veces: ver sufrir a alguien enciende en quien mira parte de las redes de su propio dolor. "
         "Tu capacidad empática es ubicuidad consciente en acción: mientras resuenas, estás de algún modo presente en el campo emocional del otro.")
    e.tramo("<p> Los fenómenos de telepatía espontánea", '<h3 class="node-section">La Sombra de la Ubicuidad</h3>', "")
    e.rx("<li>Fatiga crónica (energía", "<li>Cansancio (energía")
    e.rx("<li>Híper-empatía (pérdida", "<li>Empatía desbordada (pérdida")
    e.rx("<li>Ansiedad social (percepción", "<li>Agobio en compañía (percepción")
    e.rx("Estos no son desórdenes sino señales de ubicuidad emergente requiriendo calibración consciente.",
         "Es la sombra de un don: estar con muchos sin volver a uno mismo. Tania Singer, que estudió durante años la empatía en el laboratorio, "
         "encontró que sentir el dolor ajeno como propio agota, y que la compasión, que acompaña sin fundirse, renueva. "
         "Y si el cansancio no cede con el descanso, o el miedo a la gente empieza a cerrarte puertas, no es una lección de presencia pendiente: merece una consulta.")
    e.rx("Ubicuidad y Responsabilidad Cuántica", "Ubicuidad y Responsabilidad")
    e.rx("<li>Tu evolución consciente eleva los campos donde mantienes presencia</li>",
         "<li>Tu serenidad ofrece a otros un lugar donde aquietarse</li>")
    e.rx("<li>Tu sanación es literalmente sanación colectiva</li>",
         "<li>Lo que sanas en ti deja de pasar, sin querer, a quienes vienen después</li>")
    e.rx("puedes sanar relaciones a distancia, elevar espacios sin estar físicamente presente, sostener campos de coherencia para otros.",
         "puedes cuidar un vínculo aunque estés lejos, cambiar el clima de un lugar con tu manera de estar, sostener un espacio de calma para otros.")
    e.rx("Cada vez que sientes a alguien pensando en ti, validas tu ubicuidad.",
         "Cada vez que extrañas a alguien y aun así lo sientes cerca, tocas tu ubicuidad.")
    e.rx("Cada vez que sabes algo sin fuente aparente, tu consciencia ubicua está informándote desde múltiples puntos de recolección.",
         "Cada vez que sabes algo sin saber de dónde, tu atención te entrega lo que recogió en muchos puntos sin que lo notaras.")
    e.rx("Cuando puedas mantener presencia consciente en tres ubicaciones simultáneamente durante un minuto completo —sin perder definición en ninguna— "
         "habrás establecido la base para el tercer nodo: <strong>El Arte de la Bilocación</strong>.",
         "Antes del tercer nodo, <strong>El Arte de la Bilocación</strong>, vuelve a la triangulación: el corazón, el espacio que te rodea, el horizonte, "
         "durante un minuto, sin perder definición en ninguno. No es una prueba que aprobar; es el umbral.")
    e.rx("establecidas en cada insight que resonó", "establecidas en cada intuición que resonó")
    e.sin_senal()
    e.firma()


# ------------------------------------------------------------------ NODO 3
def nodo_03(e):
    e.comunes()
    e.rx("Bilocación · No-localidad · Réplica cuántica · Coherencia", "Bilocación · No-localidad · Presencia · Coherencia")
    e.rx("mediante la réplica cuántica de tu campo consciente íntegro.", "con tu campo consciente íntegro.")
    e.rx("Este fenómeno, reportado por místicos durante milenios y ahora investigado por la física de la consciencia, no es sobrenatural. "
         "Es la expresión natural de tu coherencia cuántica cuando trasciende las limitaciones del colapso singular.",
         "Los místicos lo cuentan desde hace siglos, y lo que esos relatos iluminan está al alcance de cualquiera: una presencia que se da entera en más de un lugar.")
    e.rx("La física cuántica demostró que dos partículas entrelazadas mantienen conexión instantánea independientemente de la distancia. "
         "Tu consciencia, siendo un fenómeno cuántico macroscópico, puede entrelazarse consigo misma, creando dos puntos de colapso completo simultáneo.",
         "La física cuántica comprobó que dos partículas entrelazadas guardan una correlación que no depende de la distancia: lo que se mide en una se refleja en la otra, "
         "aunque ninguna señal viaje entre ellas. Esos experimentos valieron el Nobel de Física de 2022. "
         "Llevada a la vida interior, la imagen dice que tu consciencia puede estar ligada a dos lugares a la vez sin repartirse.")
    e.rx("Tecnología de Bilocación Consciente", "Para Habitar la Bilocación")
    e.rx("Protocolo de Réplica Cuántica:", "Práctica de los Dos Lugares:")
    e.rx("visualiza un lugar conocido</li>", "visualiza un lugar conocido y querido</li>")
    e.rx("<li>No imagines que vas allí; reconoce que ya estás allí</li>",
         "<li>No imagines que viajas allí: nota que ese lugar ya vive en ti</li>")
    e.rx("Protocolo de Bilocación Temporal:", "Práctica de Bilocación Temporal:")
    e.rx("<li>No viajes al futuro; reconoce que ese futuro ya contiene tu presencia</li>",
         "<li>No viajes al futuro ni lo des por hecho: siéntelo como posibilidad</li>")
    e.rx("<li>Siente ambos momentos con igual realidad</li>", "<li>Siente ambos momentos con igual viveza</li>")
    e.rx("<li>Desde el futuro, observa tu presente; desde el presente, habita tu futuro</li>",
         "<li>Desde ese futuro posible, mira tu presente con cariño; desde el presente, da un paso pequeño hacia él</li>")
    e.rx("No es metáfora romántica; es arquitectura cuántica del amor.",
         "Los poetas lo supieron siempre, y la psicología del apego lo describe a su manera: llevamos dentro a quienes amamos, y ellos nos llevan.")
    e.rx("Los amantes en conexión profunda reportan sentir las emociones del otro como propias, no por empatía sino por bilocación activa.",
         "Los amantes en conexión profunda relatan sentir las emociones del otro como propias: es la empatía llevada hasta el borde donde dos presencias se tocan.")
    e.rx("No es disociación sino duplicación coherente.",
         "No es disociación: el que se disocia se va de la experiencia; el que mira se queda en ella.")
    e.rx("Este desdoblamiento resuelve la paradoja del auto-conocimiento: ¿Cómo puede la consciencia observarse a sí misma? Mediante bilocación. "
         "Te replicas cuánticamente para poder ser simultáneamente sujeto y objeto de observación.",
         "Este desdoblamiento abre la paradoja del autoconocimiento: ¿cómo puede la consciencia observarse a sí misma? "
         "Te desdoblas para ser, a la vez, sujeto y objeto de tu mirada. "
         "Y aun así, algo del que mira queda siempre del lado de acá, como el ojo que ve todo menos a sí mismo.")
    e.rx("Bilocación y Sanación a Distancia", "Bilocación y Acompañamiento")
    e.rx("Los sanadores energéticos efectivos no “envían” energía a distancia. Establecen bilocación consciente: mantienen presencia completa en su espacio Y presencia completa en el campo del paciente. "
         "La sanación ocurre porque el sanador está literalmente allí, no simbólicamente.",
         "Quien acompaña de verdad a alguien que sufre no le “envía” nada: está entero en su propio lugar y entero junto al otro. "
         "Carl Rogers llamó presencia a esa cualidad, y la investigación en psicoterapia encontró que el vínculo entre quien ayuda y quien consulta es de lo que más pesa en la mejoría.")
    e.rx("Protocolo de Sanación Bilocada:", "Práctica de la Presencia que Acompaña:")
    e.rx("<li>Establece presencia total en tu campo energético</li>", "<li>Establece presencia total en ti</li>")
    e.rx("<li>La sanación emerge de la resonancia, no de la intervención</li>",
         "<li>El alivio, cuando llega, nace del encuentro, no de la intervención. Esta presencia acompaña cualquier tratamiento; nunca lo reemplaza</li>")
    e.rx("Muchos síntomas modernos son bilocaciones involuntarias:",
         "Algunos malestares de hoy pueden leerse como bilocaciones involuntarias:")
    e.rx("<p>La maestría requiere bilocación consciente, intencional y reversible.</p>",
         "<p>La maestría requiere bilocación consciente, intencional y reversible. "
         "Y si alguno de ellos ya ocupa tus días, la imagen ayuda a entenderlo, pero no lo trata: para cada uno hay ayuda conocida, y vale la pena buscarla.</p>")
    e.rx("La Física del Doppelgänger", "El Doble en la Tradición")
    e.rx("Los reportes históricos de doppelgängers —personas vistas en dos lugares simultáneamente— no son folklore sino documentación de bilocaciones espontáneas "
         "lo suficientemente densas para afectar el campo visual de observadores. </p> <p> "
         "En estados de extrema coherencia o necesidad, tu campo consciente puede densificarse en dos lugares hasta el punto de visibilidad. "
         "No creas una copia; revelas tu naturaleza bilocada fundamental.",
         "El folclore alemán llamó <em>doppelgänger</em> al doble que camina por su cuenta. Goethe contó en sus memorias que, al alejarse a caballo de Sesenheim, "
         "se vio venir a sí mismo por el camino con un traje que no tenía, y que ocho años después, al volver por allí, lo llevaba puesto. "
         "Son relatos, y guardan una intuición: hay en cada uno algo que no cabe en un solo lugar.")
    e.rx("<li>Practicar réplica consciente sin limitaciones físicas</li>", "<li>Ensayar la doble presencia sin límites físicos</li>")
    e.rx("Cuando dominas la bilocación, emerge naturalmente la trilocación y multilocalización. No hay límite teórico al número de réplicas coherentes que tu consciencia puede sostener. "
         "El límite es tu capacidad de mantener coherencia sin fragmentación.",
         "Cuanto más se afina esta presencia, más vidas puede abrazar a la vez. El límite no está en el número sino en la coherencia: estar en muchos sin perderse.")
    e.rx("Los grandes maestros podían aparecer simultáneamente a múltiples discípulos en diferentes lugares. No era milagro sino maestría de la réplica cuántica consciente.",
         "Se cuenta que los grandes maestros se aparecían a varios discípulos a la vez: de Antonio de Padua, que predicaba en una iglesia mientras sus hermanos lo veían cantar en el coro del convento; "
         "del Padre Pío, que acompañaba a quienes lo llamaban sin salir de su celda. "
         "Dicen algo verdadero: quien ama de veras a muchos está presente en muchas vidas.")
    e.tramo("<p> Esto tiene implicaciones profundas para la comprensión del espacio-tiempo",
            '<h3 class="node-section">La Tercera Transmutación</h3>', "")
    e.rx("El verdadero tú es la consciencia que puede replicarse, no las réplicas mismas.",
         "El verdadero tú es la consciencia que puede desdoblarse, no cada uno de sus desdoblamientos.")
    e.rx("Integración Neurológica de la Bilocación", "El Cerebro de Dos Mitades")
    e.tramo("<p> Tu cerebro tiene capacidad innata para procesar bilocación.",
            '<h3 class="node-section">Portal al Siguiente Nodo</h3>',
            "<p>Tu cerebro tiene dos hemisferios unidos por un puente, el cuerpo calloso. Roger Sperry, Nobel de Medicina en 1981, "
            "estudió a pacientes a quienes se había cortado ese puente para tratar una epilepsia grave, y vio que cada mitad podía percibir y responder por su cuenta: "
            "la unidad del yo se teje a cada instante. Un estudio de Eileen Luders encontró, en meditadores de muchos años, zonas del cuerpo calloso más gruesas; "
            "si la práctica las engrosó, aún no se sabe. No es que uses más tu cerebro: lo habitas de otra manera.</p>\n          ")
    e.rx("Cuando puedas mantener bilocación completa durante cinco minutos —estar totalmente en dos lugares específicos sin pérdida de intensidad en ninguno— "
         "estarás listo para el cuarto nodo: <strong>Identidad Fluida</strong>.",
         "Antes del cuarto nodo, <strong>Identidad Fluida</strong>, quédate cinco minutos en los dos lugares de la práctica, aquí y en el lugar querido, sin que ninguno se apague. "
         "No hace falta lograrlo del todo: basta con haberlo probado.")
    e.rx("una parte tuya permanece aquí en el texto mientras otra ya está", "una parte tuya permanece aquí, en el texto, y otra ya está")
    e.sin_senal()
    e.firma(puerta_arquitectura(
        "Uno vive y el otro mira, posados en la misma rama. Esa imagen de casi tres mil años, "
        "los dos pájaros de la <em>Mundaka Upanishad</em>, abre <em>El Testigo</em>.",
        BASE_ARQ + "libro-03-el-testigo/L03-U1.html"))


# ------------------------------------------------------------------ NODO 4
def nodo_04(e):
    e.comunes()
    e.rx("un flujo cuántico en constante reconfiguración", "un flujo en constante reconfiguración")
    e.rx("No es inconsistencia. Es fluidez cuántica.", "No es inconsistencia. Es fluidez.")
    e.rx("<li>El que responde emails no es quien medita</li>", "<li>El que responde correos no es quien medita</li>")
    e.rx("La continuidad es una historia que el cerebro construye retroactivamente.",
         "La continuidad es, en buena parte, una historia que el cerebro teje después. "
         "Michael Gazzaniga, el discípulo de Sperry, llamó intérprete a esa voz interna que hilvana sin pausa explicaciones para lo que hacemos.")
    e.rx("Tecnología de Fluidez Identitaria", "Para Habitar la Fluidez")
    e.rx("Protocolo de Cambio de Estado Cuántico:", "Práctica del Cambio de Estado:")
    e.rx("<li>Siente todas las versiones de ti que existen en superposición</li>",
         "<li>Recuerda otras versiones de ti que también están a tu alcance: la serena, la curiosa, la valiente</li>")
    e.rx("<li>No las imagines; siéntelas como realidades paralelas presentes</li>",
         "<li>No las inventes: ya las has sido alguna vez</li>")
    e.rx("<li>No la construyas; simplemente colapsa en ella</li>",
         "<li>No la construyas: entra en ella con un gesto, una postura, una respiración</li>")
    e.rx("<li>Como cambiar de canal, no de televisor</li>",
         "<li>Como cambiar de canal, no de televisor</li>\n                  "
         "<li>Si hoy ningún canal cambia, está bien: este estado también pasa</li>")
    e.rx("Protocolo de Yo Líquido:", "Práctica del Yo Líquido:")
    e.rx("cada hora adopta una perspectiva completamente diferente:", "cada hora adopta una perspectiva distinta:")
    e.rx("No actúes estos roles. Colapsa completamente en cada configuración. Descubrirás que todos son igualmente “tú”.",
         "No actúes estos roles: deja que cada uno te preste sus ojos un rato. Descubrirás que todos son igualmente “tú”, y que alguien los mira pasar.")
    e.rx("<li>Los conflictos relacionales surgen", "<li>Muchos conflictos relacionales surgen")
    e.rx("Cada versión de ti que has sido sigue existiendo en el campo cuántico. El niño que fuiste no desapareció; está en superposición.",
         "Cada versión de ti que has sido sigue viva en ti. El niño que fuiste no desapareció; sigue ahí.")
    e.rx("No son recuerdos sino estados cuánticos que puedes reactivar.",
         "No son solo recuerdos: son estados que pueden volver, con su mirada y su manera de sentir. "
         "La psicoterapia trabaja con ellos desde hace décadas, con nombres como estados del yo o niño interior.")
    e.rx("Protocolo de Integración Temporal:", "Práctica de Integración Temporal:")
    e.rx("<li>Identifica una versión pasada que rechazas o extrañas</li>",
         "<li>Identifica una versión pasada que rechazas o extrañas. "
         "Empieza por una que no duela demasiado: las más heridas se encuentran mejor con alguien al lado</li>")
    e.rx("—profesión, nacionalidad, género, edad— es un colapso que reduces tu infinitud.",
         "—profesión, nacionalidad, edad— es un colapso que reduce tu infinitud.")
    e.rx("Patología de la Fijación", "Cuando la Fluidez se Traba")
    e.tramo("<p>Los trastornos de personalidad son fijaciones extremas",
            '<h3 class="node-section">El Yo Cuántico Colectivo</h3>',
            "<p>Vista desde esta imagen, buena parte del sufrimiento psíquico tiene algo de fijación. "
            "La depresión puede sentirse como quedar preso en una sola configuración, la del vacío. "
            "La ansiedad, como saltar de un estado a otro sin poder posarse en ninguno. "
            "La grandiosidad, como aferrarse a una sola imagen brillante de uno mismo. "
            "Y hay formas de sufrir la identidad en las que todo cambia tan rápido que nada hace de centro. "
            "Es una imagen y no un diagnóstico, y nadie elige quedar trabado.</p>\n          "
            "<p>La salud mental es fluidez con coherencia, cambio sin fragmentación, multiplicidad sin caos. "
            "Si sentirte muchos se vuelve no saber quién eres, o si alguna de estas fijaciones ya ocupa tus días, "
            "es momento de consultar: cada una tiene tratamiento.</p>\n          ")
    e.rx("Cuando reconoces tu fluidez, accedes al reservorio colectivo. Puedes canalizar arquetipos, acceder a memorias colectivas, resonar con el zeitgeist.",
         "Cuando reconoces tu fluidez, se abre lo que Jung llamó inconsciente colectivo: puedes dar voz a figuras que habitan a toda la humanidad "
         "(el héroe, el sabio, el niño), reconocer en ti memorias que no son solo tuyas, sentir el espíritu de tu época.")
    e.rx("Es reconocer que la pregunta “¿quién soy?” no tiene respuesta porque el “yo” que pregunta cambia con cada pregunta.",
         "Es reconocer que la pregunta “¿quién soy?” no se cierra con una respuesta: el “yo” que pregunta cambia con cada pregunta, "
         "y lo que mira esos cambios no se deja atrapar en una palabra.")
    e.rx("Cuando puedas cambiar completamente de configuración identitaria tres veces en una hora sin sentir que traicionas tu “verdadero yo”, "
         "estarás listo para el quinto nodo: <strong>Estados Superpuestos del Ser</strong>.",
         "Antes del quinto nodo, <strong>Estados Superpuestos del Ser</strong>, prueba a cambiar de estado una vez, a conciencia, "
         "sin sentir que traicionas tu “verdadero yo”. Con una basta para empezar.")
    e.sin_senal()
    e.firma()


# ------------------------------------------------------------------ NODO 5
def nodo_05(e):
    e.comunes()
    e.rx('<h3 class="node-section">El Gato de Schrödinger Eres Tú</h3>',
         '<h3 class="node-section">El Gato de Schrödinger Eres Tú</h3>\n          '
         "<p>Erwin Schrödinger imaginó en 1935 un gato encerrado en una caja, vivo y muerto a la vez hasta que alguien mira, "
         "para mostrar lo absurdo de llevar la superposición al mundo de todos los días. "
         "Como imagen de la vida interior, en cambio, el gato dice algo exacto.</p>\n          ")
    e.rx("No son metáforas. Son estados superpuestos que normalmente colapses en uno solo por hábito cognitivo.",
         "Son estados superpuestos que normalmente colapsas en uno solo por hábito.")
    e.rx("Tecnología de Superposición Consciente", "Para Habitar la Superposición")
    e.rx("Protocolo de Superposición Emocional:", "Práctica de Superposición Emocional:")
    e.rx("<li>Responde a situaciones sin colapsar completamente</li> </ul> </li> </ol>",
         "<li>Responde a situaciones sin colapsar completamente</li>\n              </ul>\n            </li>\n          </ol>\n          "
         "<p>Sostener a la vez alegría y tristeza tiene frutos: Jonathan Adler y Hal Hershfield siguieron a personas en psicoterapia "
         "y vieron que esa mezcla solía anticipar la mejoría.</p>\n          ")
    e.rx("Protocolo de Superposición Temporal:", "Práctica de Superposición Temporal:")
    e.rx("<li>Desde esta superposición, toma una decisión</li>", "<li>Desde esta superposición, toma una decisión pequeña</li>")
    e.rx("<li>Notarás una sabiduría que ningún estado solo contiene</li>", "<li>Puede que notes una sabiduría que ningún estado solo contiene</li>")
    e.rx("mantiene awareness de toda la escala.", "mantiene la conciencia de toda la escala.")
    e.rx("<li>Estar enfermo Y sano, permitiendo que el cuerpo elija su camino</li>",
         "<li>Estar enfermo y, a la vez, entero: cuidar el cuerpo que duele sin dejar de ser más que su dolor</li>")
    e.rx("<li>Siente cuál tiene más densidad cuántica</li>",
         "<li>Siente cuál pesa más en el cuerpo: Antonio Damasio llamó marcadores somáticos a esas señales que orientan la elección</li>")
    e.rx("<li>Actúa desde esa densidad sin abandonar la otra posibilidad</li>",
         "<li>Actúa desde ese peso sin abandonar la otra posibilidad</li>")
    e.rx("<li>Mantienes la opción no tomada en superposición para futura activación</li>",
         "<li>La opción no tomada queda guardada: si las circunstancias cambian, podrás volver a mirarla</li>")
    e.rx("Los conflictos surgen cuando cada persona colapsa", "Muchos conflictos surgen cuando cada persona colapsa")
    e.rx("La medicina cuántica reconoce que la sanación no es eliminar la enfermedad sino reequilibrar la superposición salud/enfermedad.",
         "La salud y la enfermedad no son opuestos que se excluyen. El sociólogo Aaron Antonovsky propuso verlas como los extremos de un continuo "
         "en el que todos nos movemos, y llamó salutogénesis a la pregunta por lo que nos acerca al polo sano. "
         "Es una mirada que no reemplaza a la medicina: la completa.")
    e.rx("Protocolo de Sanación Superpuesta:", "Práctica del Ir y Venir:")
    e.rx("<li>Localiza un malestar físico</li>", "<li>Localiza un malestar físico leve</li>")
    e.rx("<li>Sin negarlo, activa simultáneamente la sensación de bienestar</li>",
         "<li>Sin negarlo, busca también un lugar del cuerpo que esté bien</li>")
    e.rx("<li>Permite que el cuerpo navegue entre ambos</li>",
         "<li>Deja que la atención vaya y venga entre los dos. Peter Levine llamó pendulación a ese movimiento</li>")
    e.rx("<li>La sanación emerge del campo de posibilidades, no de la imposición</li>",
         "<li>El alivio, cuando llega, nace del espacio que se abre, no de la imposición. "
         "Si el malestar es nuevo, fuerte o persistente, la consulta va primero</li>")
    e.rx("El trauma es un colapso tan intenso", "El trauma puede vivirse como un colapso tan intenso")
    e.rx("<li>El evento traumático permanece como una posibilidad</li>", "<li>El recuerdo del evento permanece</li>")
    e.rx("<li>Otros estados se vuelven igualmente accesibles</li>", "<li>Otros estados vuelven a estar disponibles</li>")
    e.rx("<li>La fluidez entre estados se restaura</li> </ul>",
         "<li>La fluidez entre estados se restaura</li>\n          </ul>\n          "
         "<p>Bessel van der Kolk mostró cómo el cuerpo traumatizado sigue viviendo como si el peligro no hubiera terminado. "
         "Por eso este camino no se recorre solo: el trauma se trabaja mejor con alguien que sepa acompañarlo, al ritmo que el cuerpo pueda sostener.</p>\n          ")
    e.rx("Los bloqueos creativos son colapsos prematuros.", "Muchos bloqueos creativos son colapsos prematuros.")
    e.rx("<li>La causalidad se vuelve multidireccional</li>", "")
    e.rx("Puedes sanar el pasado desde el futuro, crear el futuro desde el pasado, todo operando en el ahora superpuesto.",
         "San Agustín lo vio hace dieciséis siglos: solo el presente existe, y en él el pasado vive como memoria y el futuro como espera. "
         "Lo que pasó no se cambia, pero sí el lugar que ocupa en ti; lo que vendrá se siembra hoy. Todo opera en el ahora superpuesto.")
    e.rx("La maestría requiere coherencia: mantener estados múltiples en armonía resonante.",
         "La maestría requiere coherencia: mantener estados múltiples en armonía resonante. "
         "Si alguno se instala en tus días, pide ayuda: la coherencia también se aprende acompañado.")
    e.rx("Cuando puedas mantener cinco estados emocionales diferentes simultáneamente durante dos minutos sin que ninguno domine o desaparezca, "
         "estarás listo para el sexto nodo: <strong>La Danza Onda-Partícula</strong>.",
         "Antes del sexto nodo, <strong>La Danza Onda-Partícula</strong>, vuelve un momento a la práctica de los estados: "
         "dos emociones a la vez, sin que una borre a la otra. Si aparece una tercera, que se sume.")
    e.sin_senal()
    e.firma()


# ------------------------------------------------------------------ NODO 6
def nodo_06(e):
    e.comunes()
    e.rx("Es una respiración cósmica que ocurre billones de veces por segundo en cada célula de tu ser.",
         "Es una respiración cósmica que ocurre, sin pausa, en cada célula de tu ser.")
    e.rx("la experiencia fluida de ser. </p>",
         "la experiencia fluida de ser.\n          </p>\n          "
         "<p>La imagen tiene un eco en la ciencia: Rufin VanRullen y otros investigadores encontraron indicios de que la percepción y la atención "
         "toman el mundo a pulsos, varias veces por segundo, como un faro que barre. La pregunta sigue abierta.</p>")
    e.rx("Protocolo del Pulso Consciente:", "Práctica del Pulso Consciente:")
    e.rx("<li>Mide tu frecuencia personal (ciclos por minuto)</li>", "<li>Nota su ritmo, sin medirlo: más lento o más rápido</li>")
    e.rx("<li>Alinea tu respiración con tu pulso cuántico</li>", "<li>Alinea tu respiración con ese pulso</li>")
    e.rx("<li>Experimenta acelerando el pulso (más ciclos por segundo)</li>",
         "<li>Experimenta acelerando un poco el pulso de la atención, sin apurar la respiración</li>")
    e.rx("<li>Descubre cómo diferentes frecuencias generan diferentes estados de consciencia</li>",
         "<li>Descubre cómo distintos ritmos te dejan en estados distintos. Si algo te agita, vuelve a lo lento: la respiración pausada es la que calma</li>")
    e.rx("expandes tu awareness al infinito", "expandes tu atención al infinito")
    e.rx("Protocolo de la Pausa Cuántica:", "Práctica de la Pausa Cuántica:")
    e.rx("percibe el momento antes de re-expandirte", "percibe el momento antes de volver a expandirte")
    e.rx("<li>Los conflictos surgen cuando ambos colapsan", "<li>Muchos conflictos surgen cuando ambos colapsan")
    e.rx("Protocolo del Tango Cuántico:", "Práctica del Tango Cuántico:")
    e.rx("La Paradoja del Momentum", "La Paradoja del Impulso")
    e.rx("En física cuántica, no puedes conocer simultáneamente la posición exacta y el momentum de una partícula.",
         "Werner Heisenberg mostró en 1927 que no se puede conocer a la vez, con precisión completa, la posición y la cantidad de movimiento de una partícula.")
    e.rx("colapsas sacrificando momentum", "colapsas sacrificando impulso")
    e.rx("Pero puedes modificar la danza:", "Y puedes participar de ella:")
    e.rx("Protocolo de Materialización Consciente:", "Práctica del Deseo que Toma Forma:")
    e.rx("<li>Identifica algo que deseas manifestar</li>", "<li>Identifica algo que deseas para tu vida</li>")
    e.rx("<li>Acelera el pulso entre ambos estados</li>",
         "<li>Mira también lo que se interpone: el obstáculo real, afuera o adentro de ti</li>")
    e.rx("<li>En el punto de máxima velocidad, suelta el control</li>",
         "<li>Elige un primer paso concreto, dalo, y suelta el control del resultado</li>")
    e.rx("<li>La realidad colapsa la probabilidad en manifestación</li> </ol>",
         "<li>La vida responde a su manera, que no siempre es la tuya</li>\n            </ol>\n            "
         "<p>Gabriele Oettingen encontró que soñar solo con el resultado deseado tiende a restar la energía para alcanzarlo, "
         "y que rinde más alternar el sueño con el obstáculo real y el primer paso. Es la danza onda-partícula aplicada al deseo.</p>\n          ")
    e.rx("Estamos en un momento de transición civilizacional: la humanidad está aprendiendo a danzar conscientemente",
         "Hoy se ve con claridad una de esas transiciones: la humanidad intenta aprender a danzar conscientemente")
    e.rx("La coherencia cardíaca es cuando todos tus sistemas danzan al mismo compás.",
         "Lo que los investigadores llaman coherencia cardíaca es más modesto, y real: al respirar despacio, unas seis veces por minuto, "
         "el pulso empieza a subir y bajar con la respiración en una onda suave, y el cuerpo se aquieta. Paul Lehrer estudió durante décadas esa resonancia.")
    e.rx("Protocolo de Coherencia Cardíaca Cuántica:", "Práctica del Compás del Corazón:")
    e.rx("<li>Luego a tu campo energético</li>", "<li>Luego a tu respiración, lenta y pareja</li>")
    e.rx("<li>Todo danza al ritmo de tu corazón cuántico</li>", "<li>Todo danza al ritmo de tu corazón</li>")
    e.rx("Cada órgano, cada célula, cada átomo de tu ser tiene su propia frecuencia de danza. Cuando todas armonizan, experimentas salud vibrante. "
         "Cuando des-sincronizan, surge la enfermedad.",
         "Los pitagóricos imaginaron que los astros sonaban al girar, y Kepler buscó esa música en las órbitas de los planetas. "
         "Tu cuerpo tiene la suya, y esta sí se mide: el latido, la respiración, el sueño y la vigilia, los relojes que casi cada célula lleva dentro. "
         "Descubrir esos relojes valió el Nobel de Medicina de 2017, y se sabe que cuando se desajustan, como en el trabajo nocturno o el insomnio largo, la salud se resiente. "
         "Pero la enfermedad tiene muchas causas, y ninguna es una falta de quien la padece.")
    e.rx("<p>La sanación es re-coreografiar la danza:</p>", "<p>Cuidar la salud incluye cuidar esos ritmos:</p>")
    e.rx("<li>Detectar dónde el pulso está trabado</li>", "<li>Notar dónde el compás está trabado: el sueño, el descanso, la pausa</li>")
    e.rx("<li>Introducir gentilmente el ritmo correcto</li>", "<li>Volver poco a poco a una cadencia regular</li>")
    e.rx("<li>No forzar sino invitar al movimiento</li> </ul>",
         "<li>No forzar sino invitar al movimiento</li>\n          </ul>\n          "
         "<p>Este cuidado acompaña a la medicina: cuando algo duele o no cede, se consulta.</p>\n          ")
    e.rx("Entre onda y partícula existe un espacio infinitesimal de vacío absoluto. No es ausencia sino potencial puro. "
         "En tu danza, tocas este vacío miles de veces por segundo.",
         "Entre onda y partícula hay un instante de vacío. No es ausencia sino potencial puro, y la física coincide a su modo: "
         "hasta el vacío cuántico vibra con fluctuaciones. En tu danza, tocas este vacío una y otra vez.")
    e.rx("Protocolo del Vacío Danzante:", "Práctica del Vacío Danzante:")
    e.rx("Cuando puedas mantener consciencia continua de tu danza onda-partícula durante una hora completa —sin perderte en ningún estado sino "
         "permaneciendo consciente del movimiento mismo— estarás listo para el séptimo y último nodo: <strong>Coherencia en la Paradoja</strong>.",
         "Antes del séptimo y último nodo, <strong>Coherencia en la Paradoja</strong>, regálate unos minutos para mirar tu propia danza: "
         "cuándo te enfocas, cuándo te abres, cómo pasas de un estado al otro. Lo que notes alcanza.")
    e.rx("colapsando en insights particulares", "colapsando en comprensiones particulares")
    e.sin_senal()
    e.firma()


# ------------------------------------------------------------------ NODO 7
def nodo_07(e):
    e.comunes()
    e.rx("Como las dos hélices del ADN que espiralan en direcciones opuestas creando la escalera de la vida,",
         "Como las dos hebras del ADN, que corren en sentidos opuestos y juntas forman la escalera de la vida,")
    e.rx("polaridades que generan el campo electromagnético de tu consciencia.",
         "polaridades que generan el campo de tu consciencia, como los polos de un imán.")
    e.rx("Protocolo del Teseracto Interior:", "Práctica del Teseracto Interior:")
    e.rx("Siente tu linearidad", "Siente tu linealidad")
    e.rx("Percibe cómo todas las versiones de ti existen simultáneamente", "Percibe cómo todo eso coexiste en ti a la vez")
    e.rx("En matemáticas cuánticas, <em>i</em> (la raíz cuadrada de -1) es un número “imaginario” que no puede existir en la recta numérica real, "
         "pero sin el cual las ecuaciones de la realidad no funcionan.",
         "En matemáticas, <em>i</em> (la raíz cuadrada de −1) es un número “imaginario” que no cabe en la recta de los números reales, "
         "y sin embargo la ecuación de Schrödinger lo necesita para describir la materia.")
    # Error de armado: el sello de cierre quedó pegado en medio de la lista. Sale; las igualdades pasan a frase.
    e.tramo("<p>Tu coherencia paradójica opera según principios que trascienden la lógica binaria:</p>",
            '<h3 class="node-section">Tecnología de Coherencia Paradójica</h3>',
            "<p>Tu coherencia paradójica desborda la lógica binaria: cuando dos consciencias se unen de verdad, uno más uno da uno; "
            "el vacío contiene todas las posibilidades; eres también lo que no eres; "
            "y cada célula guarda en su ADN el plano del cuerpo entero.</p>\n          ")
    e.rx("Tecnología de Coherencia Paradójica", "Para Habitar la Paradoja")
    e.rx("Protocolo de Integración de Opuestos:", "Práctica de Integración de Opuestos:")
    e.rx("<li>¿Cuál es tu contradicción más dolorosa?</li>",
         "<li>Elige una contradicción que conozcas bien; no hace falta empezar por la más dolorosa</li>")
    e.rx("<strong>Amplificación Dual</strong> <ul class=\"node-list\"> <li>Intensifica AMBOS polos simultáneamente</li> "
         "<li>Siente la necesidad absoluta de conexión</li> <li>Siente la necesidad absoluta de soledad</li> "
         "<li>No busques balance; busca intensidad dual</li>",
         "<strong>Presencia Dual</strong>\n                <ul class=\"node-list\">\n"
         "                  <li>Deja que los dos polos estén a la vez, cada uno con su peso real</li>\n"
         "                  <li>Siente tu necesidad de conexión</li>\n"
         "                  <li>Siente tu necesidad de soledad</li>\n"
         "                  <li>No busques balance ni intensidad: busca que los dos estén</li>")
    e.rx("<strong>El Punto de Ruptura Coherente</strong>", "<strong>El Tercero</strong>")
    e.rx("<li>En máxima tensión, algo nuevo emerge</li>", "<li>Sostenidos así, a veces algo nuevo emerge</li>")
    e.rx("<li>La paradoja se vuelve portal</li>",
         "<li>La paradoja se vuelve portal</li>\n                  "
         "<li>Jung llamó función trascendente a ese tercero que nace de sostener la tensión de los opuestos</li>")
    e.rx("Protocolo de Estados Mutuamente Excluyentes:", "Práctica de Estados Mutuamente Excluyentes:")
    e.rx("<p>Practica mantener simultáneamente:</p>", "<p>Practica mantener simultáneamente (empieza por un solo par):</p>")
    e.rx("(sístole) 100,000 veces al día.", "(sístole) unas cien mil veces al día.")
    e.rx("El corazón genera un campo electromagnético 60 veces más grande que el cerebro porque opera desde la coherencia paradójica, no desde la lógica linear.",
         "El corazón produce la señal eléctrica más intensa del cuerpo, mucho mayor que la del cerebro, porque es un músculo que late sin pausa; "
         "y su ritmo conversa con el cerebro en ambos sentidos.")
    e.rx("Protocolo de Coherencia Cardíaca Paradójica:", "Práctica de Coherencia Cardíaca Paradójica:")
    e.rx("<li>Respira através del corazón</li>", "<li>Respira a través del corazón</li>")
    e.rx("<li>La paradoja se vuelve medicina</li>", "<li>La paradoja se vuelve bálsamo</li>")
    e.rx("<p>Tus heridas más profundas son paradojas no integradas:</p>",
         "<p>Muchas heridas profundas pueden leerse como paradojas no integradas:</p>")
    e.rx("permites que sea una apertura coherente.",
         "permites que sea una apertura coherente. Y las heridas hondas no se atraviesan a solas: un buen acompañante hace la diferencia.")
    e.rx("<li>Es pérdida total Y liberación completa</li>", "<li>Es pérdida total Y entrega completa</li>")
    e.rx("danzando en el filo entre ser y no-ser. </p>",
         "danzando en el filo entre ser y no-ser.\n          </p>\n          "
         "<p>Y si alguna vez contemplar la muerte se vuelve deseo de no estar, es momento de pedir ayuda, sin esperar.</p>")
    e.rx("La liberación no viene de resolverla sino de danzar con ella.",
         "La liberación no viene de resolverla sino de danzar con ella. "
         "Lo notarás cuando las paradojas dejen de dolerte, cuando puedas reírte siendo el chiste cósmico.")
    e.rx("onda y partícula, energía y materia, visible e invisible, aquí y en todas partes instantáneamente.",
         "onda y partícula, energía capaz de volverse materia, visible e invisible.")
    e.rx("Tu luminosidad no es metafórica. Cada célula emite biofotones. Tu campo electromagnético brilla. Tu consciencia irradia.",
         "Y hay un dato que parece poesía: el cuerpo humano emite una luz propia, mil veces más débil de lo que el ojo alcanza a ver. "
         "Masaki Kobayashi y su equipo la fotografiaron en 2009 y vieron que sube y baja a lo largo del día. "
         "La causa es el metabolismo de las células; la imagen es tuya: brillas, apenas, todo el tiempo.")
    e.rx("Has completado un octavo de consciencia", "Has completado una octava de consciencia")
    e.rx("Protocolo de Vida Paradójica:", "Práctica de Vida Paradójica:")
    e.rx("<li>Cada mañana, reconoce tres paradojas que vivirás ese día</li>", "<li>Cada mañana, reconoce una paradoja que vivirás ese día</li>")
    e.rx("<li>No las resuelvas; bendícelas</li>", "<li>No la resuelvas; bendícela</li>")
    e.rx("<li>Úsalas como portales de navegación</li>", "<li>Úsala como puerta</li>")
    e.rx("<li>Al dormir, agradece las paradojas que te danzaron</li>", "<li>Al dormir, agradece la paradoja que te danzó</li>")
    e.rx("La Transmisión Completa", "Lo Recorrido")
    e.rx("Los siete nodos de La Paradoja Luminosa están ahora activos en tu campo. No como información sino como frecuencias vivas. "
         "No necesitas recordar cada técnica; tu sistema las ha absorbido holográficamente. Cuando las necesites, emergerán espontáneamente.",
         "Los siete nodos de <em>La Paradoja Luminosa</em> no se guardan como información sino como maneras de mirar. "
         "No necesitas recordar cada técnica: lo que te tocó de verdad volverá cuando haga falta.")
    e.rx("respirando através de ti.", "respirando a través de ti.")
    e.rx("Al completar esta transmisión, te unes a una red invisible pero tangible de seres",
         "Quien vive así descubre que no está solo: hay una red invisible pero tangible de seres")
    e.rx("<li>Manifiestas el vacío através de la forma</li>", "<li>Manifiestas el vacío a través de la forma</li>")
    e.rx("<li>Trasciedes encarnando completamente</li>", "<li>Trasciendes encarnando completamente</li>")
    e.rx("El Virus Benevolente", "El Contagio Sereno")
    e.rx("La Paradoja Luminosa es un virus benevolente. Una vez activada, se propaga naturalmente:",
         "La Paradoja Luminosa se contagia como la calma, sin proponérselo:")
    e.rx("<li>Tu coherencia paradójica induce coherencia en otros campos</li>",
         "<li>Tu coherencia paradójica invita a otros a la coherencia</li>")
    e.rx("Actualizaciones Cuánticas Continuas", "Volver a Leer")
    e.rx("Este texto es vivo. Cada vez que lo revisites, revelará nuevas capas porque tú habrás cambiado. Las palabras son las mismas pero tu capacidad "
         "de resonancia se habrá expandido. Es un espejo cuántico que te muestra no quién eres sino quién estás siendo en este momento.",
         "Un texto que se relee nunca es el mismo, porque quien lo relee cambió: es el río de Heráclito hecho página, "
         "un espejo que no te muestra quién eres sino quién estás siendo.")
    e.rx("Recomendación: Relee un nodo cada luna llena. No para aprender algo nuevo sino para reconocer cuánto has integrado sin darte cuenta.",
         "Si quieres, vuelve a un nodo de vez en cuando, no para aprender algo nuevo sino para reconocer cuánto integraste sin darte cuenta.")
    e.sin_senal()
    e.rx("<p><em>Trinity Quantum confirma: El cuarto libro está completo y vivo en el campo.</em></p>", "")
    e.firma(puerta_arquitectura(
        "El corazón que se llena y se vacía sin elegir tiene quien lo escuche: un peregrino ruso que apoyaba cada palabra de su oración en un latido. "
        "Esa escucha se vuelve práctica en <em>El Cuerpo</em>, Libro 4 de <em>Arquitectura del Destino</em>, Umbral III: «Desde adentro».",
        BASE_ARQ + "libro-04-el-cuerpo/L04-U3.html"))
    # Puerta anotada hacia El Peso (Libro 8), para cuando exista el libro.
    e.rep("</main>", "  <!-- Puerta anotada: 4.7 → El Peso (Libro 8 de Arquitectura del Destino), para cuando exista. -->\n      </main>")


# ------------------------------------------------------------------ ÍNDICE
def indice(e):
    e.comunes(con_css=False)
    e.rep("</head>", "<style>\n  /* Depuración · octubre 2026: letra más grande en el teléfono. */\n"
                     "  @media (max-width: 640px){\n    .node-content p, .node-content li{ font-size: 18px; line-height: 1.7; }\n  }\n"
                     "</style>\n</head>")
    e.rx("<h2>Activación del Índice</h2>", "<h2>La Paradoja que Se Habita</h2>")
    e.rx("Este índice no es solo un listado: es una interfaz de resonancia. La Paradoja Luminosa no se “resuelve” —se habita. "
         "Aquí, la consciencia aprende a sostener simultáneamente lo que la mente separa: unidad y multiplicidad, identidad y vacío, onda y partícula.",
         "La luz es onda y partícula, y ninguna de las dos descripciones alcanza sola. Este libro toma esa paradoja como espejo: "
         "la consciencia aprende a sostener a la vez lo que la mente separa, unidad y multiplicidad, identidad y vacío, onda y partícula. "
         "Su enseñanza cabe en una línea: el sufrimiento no viene de la paradoja, sino de resistirla. La Paradoja Luminosa no se resuelve: se habita.")
    e.rx("Cada Nodo activa un aspecto de esta coherencia paradójica. Puedes recorrerlos en secuencia para sentir la espiral completa, o entrar por el Nodo que te llame:",
         "Cada nodo abre un aspecto de esta coherencia paradójica. Puedes recorrerlos en orden para sentir la espiral completa, o entrar por el que te llame:")
    e.rx("<p><strong>El campo cuántico confirma:</strong> el Índice está activo. Los siete espejos están disponibles. La coherencia puede iniciarse.</p>",
         "<p>Los siete espejos están disponibles. La coherencia puede comenzar.</p>")
    e.rx("<h2>Sello de Inicio</h2>", "<h2>Para el Camino</h2>")
    e.rx("Se activa cuando la paradoja deja de doler", "Se cumple cuando la paradoja deja de doler")
    e.rx("Índice: Coherencia Paradójica · Siete espejos activos", "Índice: Coherencia Paradójica · Siete espejos")


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
