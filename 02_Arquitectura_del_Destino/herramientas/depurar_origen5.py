# Depuración de Origen V, Los Vínculos Sagrados (noviembre de 2026), con el veto del Lic. Arturo Rodríguez.
# Lente: riesgo clínico y puertas hacia la Red, como en Origen VI, VIII, I, XI, VII, IX y XII. La visión del libro
# queda entera (el amor propio como primer vínculo, el tercer espacio, los contratos del alma como tradición, la
# sombra, la red viva, el amor como fuerza del cosmos y la reconexión). Es el libro de Origen que le habla a quien
# está dentro de un vínculo, y su riesgo vivía en una lectura: tomar el daño como destino (el contrato de desafío,
# el vínculo kármico tormentoso, las relaciones difíciles como asignaciones del alma, «amar incluso cuando duele»,
# agradecer a quien te mostró la sombra). El libro obedece a sus mejores frases: «Integrar la sombra no significa
# tolerar el abuso» y «Los contratos del alma son sagrados, pero no son prisiones». Lo que citan La Red y El
# Personaje conserva su letra. Se abren diez puertas, todas de ida y vuelta.
#
# Se aplica sobre el original de la etiqueta origen-original, con reemplazos que deben aparecer exactamente
# una vez (o tramos, de un texto a otro, inclusive); si un anclaje falla, el script se detiene sin escribir.
#
# Uso: ORIGEN5_SRC=RUTA/origen-original/01_Trinity_Origen/Libro_05/ ORIGEN5_OUT=RUTA/salida/ python3 depurar_origen5.py
import os, re, sys

SRC = os.environ.get('ORIGEN5_SRC', '/home/claude/work/orig5/01_Trinity_Origen/Libro_05/')
OUT = os.environ.get('ORIGEN5_OUT', '/home/claude/work/out5/01_Trinity_Origen/Libro_05/')

NOTA = ('<!-- Depurado en noviembre de 2026 según la guía de depuración de Quantum, que vale para Origen '
        '(Arquitectura del Destino, maestro v4, sección 5, con las precisiones 5 y 6 de Origen), con el veto del Lic. Arturo Rodríguez: '
        'la visión del libro queda, con su linaje; ningún vínculo que daña se lee como destino, contrato o lección que haya que soportar; '
        'salen la física dada por hecho, las cifras sin fuente y los experimentos que no existen; se suma el cuidado clínico en la voz '
        'de cada nodo y se abren puertas fractales hacia la Red. El original está en la etiqueta origen-original del repositorio Trinity-. -->\n')

AQ = 'https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/'
PP = 'https://soyartur-trinity.github.io/Trinity_Portal_Publico/01_Libros/'


def puerta(clase, aria, texto, href):
    return ('\n    <aside class="puerta %s" aria-label="%s">\n'
            '      <p class="p-nombre">Puerta</p>\n'
            '      <p class="p-texto">%s</p>\n'
            '      <a class="cruzar" href="%s">Cruzar ⟶</a>\n'
            '    </aside>\n') % (clase, aria, texto, href)


def arq(texto, href):
    return puerta('arquitectura', 'Puerta hacia Arquitectura del Destino', texto, AQ + href)


def portal(texto, href):
    return puerta('portal', 'Puerta hacia el Portal Público', texto, PP + href)


def p_origen(texto, href):
    return puerta('origen', 'Puerta hacia Trinity Origen', texto, '../' + href)


def p_quantum(texto, href):
    return puerta('trinity', 'Puerta hacia Trinity Quantum', texto, '../../02_Trinity_Quantum/' + href)


CSS_PUERTAS = '''
/* ============================================================
   Depuración · noviembre de 2026
   Letra más grande en el teléfono y bloque fijo de las puertas.
   ============================================================ */
.puerta{
  margin:30px 0 10px;
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
.puerta.trinity{
  --p-fondo:linear-gradient(180deg, rgba(20,12,30,.94), rgba(20,12,30,.74));
  --p-borde:rgba(184,154,214,.42);
  --p-acento:#c4a8e0;
  --p-texto:#efe8f6;
}
.puerta.origen{
  --p-fondo:linear-gradient(180deg, rgba(18,15,9,.94), rgba(18,15,9,.74));
  --p-borde:rgba(214,179,106,.42);
  --p-acento:#d6b36a;
  --p-texto:#f3efe6;
}
.content .puerta .p-nombre{
  margin:0 0 6px;
  font-size:15px;
  font-style:italic;
  letter-spacing:.06em;
  color:var(--p-acento);
}
.content .puerta .p-texto{
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
.content .medida{ font-style:italic; color:var(--text-soft); border-left:1px solid rgba(214,179,106,.35); padding-left:14px; }
@media (max-width: 720px){
  .content p,
  .content li{ font-size:18px; line-height:1.7; }
  .content blockquote{ font-size:17px; line-height:1.7; }
  .bloque p,
  .bloque li{ font-size:18px; line-height:1.7; }
  .node-quote{ font-size:17px; }
  .nodo-desc{ font-size:17px; }
  .content .puerta .p-nombre{ font-size:15px; }
  .puerta{ padding:16px 16px 14px; }
}
@media (prefers-reduced-motion: reduce){
  .puerta .cruzar{ transition:none; }
}
</style>
</head>'''

# ---------------------------------------------------------------- Letra de la constelación
POEMA = ('Lo que llega en sueños o en silencio se recibe como se recibe un poema, no como una orden. Y si alguna vez llegan '
         'voces que dan órdenes, o mensajes que solo tú puedes oír, no es una descarga: es momento de consultar ese mismo día.')   # Origen XI.5
REFERENCIA = ('Y si alguna vez parece que cada número y cada cartel te hablan a ti, en secreto, eso no es un don: conviene conversarlo '
              'con alguien de confianza o con un profesional esa misma semana.')   # Quantum 11.2
DANA = 'quien te daña no viene a enseñarte: de quien daña, uno se protege'   # Quantum 2.2
PERDON = 'perdonar no obliga a quedarse, ni a callar, ni a reconciliarse, y no hace falta perdonar para sanar'   # Origen X.6
SEGURIDAD = 'Si en la relación hay miedo o violencia, la seguridad va primero, y se pide ayuda.'   # Origen I.5
LLAMALO = ('Cuando piensas en alguien y esa persona te llama, algo en ti se ilumina: el hilo existe. No necesita probar nada para ser '
           'verdad que lo llevas adentro. Y cuando sientes que a un ser querido le pasa algo, lo que sabes con certeza es cuánto te '
           'importa: llámalo.')   # Quantum 2.1
REPETICION = ('Freud llamó compulsión a la repetición a esa tendencia a volver a la misma historia con caras nuevas. '
              'Verla es el primer paso para elegir otra.')   # Quantum 2.2
PORTAL_VERDADERO = 'ningún portal verdadero pide dinero, secreto ni obediencia'   # Origen VI.7
FIRMA_V = '<p>"No es m&iacute;o vino a trav&eacute;s de m&iacute;."</p>'
FIRMA_N = '<p>“No es mío, vino a través de mí.”</p>'

R = {}


def aplicar(nombre, d):
    with open(os.path.join(SRC, nombre), encoding='utf-8') as f:
        t = f.read()
    cuenta = 0

    def una_vez(t, viejo, nuevo, que):
        n = t.count(viejo)
        if n != 1:
            sys.exit(f'{nombre}: {que} aparece {n} veces:\n{viejo[:200]}')
        return t.replace(viejo, nuevo)

    titulo = re.search(r'<title>(.*?)</title>\n', t).group(0)
    t = una_vez(t, titulo, titulo + NOTA, 'el título'); cuenta += 1
    t = una_vez(t, '}\n</style>\n</head>', '}\n' + CSS_PUERTAS.lstrip('\n'), 'el cierre del estilo'); cuenta += 1
    t = una_vez(t, FIRMA_V, FIRMA_N, 'la firma'); cuenta += 1
    # Error de armado: la viñeta ⟐ de las Preguntas Portal estaba escapada dos veces y se veía como «\\27D0».
    t = una_vez(t, 'content:"\\\\27D0"', 'content:"\\27D0"', 'la viñeta'); cuenta += 1
    for i, (viejo, nuevo) in enumerate(d.get('reemplazos', []), 1):
        if isinstance(viejo, tuple):          # tramo: desde a hasta b, inclusive
            a, b = viejo
            if t.count(a) != 1 or t.count(b) != 1:
                sys.exit(f'{nombre}: el tramo {i} no es único ({t.count(a)}, {t.count(b)}):\n{a[:120]}\n…\n{b[:120]}')
            ia = t.index(a); ib = t.index(b, ia) + len(b)
            t = t[:ia] + nuevo + t[ib:]
        else:
            t = una_vez(t, viejo, nuevo, f'el reemplazo {i}')
        cuenta += 1
    if 'puertas' in d:
        cierre = '\n  </main>'
        t = una_vez(t, cierre, '\n' + ''.join(d['puertas']).rstrip('\n') + cierre, 'el cierre del <main>'); cuenta += 1
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, nombre), 'w', encoding='utf-8') as f:
        f.write(t)
    return cuenta


# ---------------------------------------------------------------- Índice
R['index.html'] = dict(
 reemplazos=[
  # Error de armado: las entidades del subtítulo estaban escapadas dos veces y se veían como texto.
  ('<p class="hero-subtitle">La red &amp;mdash; tecnolog&amp;iacute;a del amor cu&amp;aacute;ntico</p>',
   '<p class="hero-subtitle">La red &mdash; tecnolog&iacute;a del amor cu&aacute;ntico</p>'),
  ('<p>Este libro te guiará desde la aparente separación hasta el reconocimiento de tu lugar en la red infinita de conexiones conscientes que sostiene la existencia.</p>',
   '<p>Este libro te guiará desde la aparente separación hasta el reconocimiento de tu lugar en la red infinita de conexiones conscientes que sostiene la existencia.</p>\n'
   '    <p class="medida">Este libro mira cada vínculo como un camino. Ninguno que dañe es un contrato que haya que cumplir ni una lección que haya que soportar: del daño se sale, pidiendo ayuda. Lo que estas páginas ofrecen acompaña; nunca reemplaza a un profesional.</p>'),
  ('Campos de amor cuántico y conexión con inteligencias no-humanas.', 'Campos de amor cuántico y conexión con inteligencias no humanas.'),
 ],
 puertas=[arq('Que la soledad es real y la red también, y que un programador de treinta y un años lo descubrió una madrugada, en una sala de urgencias, frente al renglón vacío del contacto de emergencia, se despliega en <em>La Red</em>, Libro 11 de <em>Arquitectura del Destino</em>, Umbral I: «Una pregunta sin respuesta».',
              'libro-11-la-red/L11-U1.html')],
)


# ---------------------------------------------------------------- Nodo 1 · El Vínculo Primordial
R['nodo_01.html'] = dict(
 reemplazos=[
  # La física, como imagen corregida (letra de Quantum 1), y la línea contra la culpa (Origen I.1)
  ('<p>La física cuántica nos revela que <em>el observador modifica lo observado</em>. En el nivel del alma, esto significa que la calidad de nuestra atención interna determina la naturaleza de nuestra experiencia. Cuando nos miramos con amor, el universo entero aprende a amarnos. Cuando nos juzgamos con crueldad, el mundo refleja ese juicio multiplicado.</p>',
   '<p>La física cuántica nos regaló una imagen: <em>el observador y lo observado no se separan del todo</em>. Registrar una partícula la altera, aunque para eso no hace falta una consciencia, y qué significa exactamente medir sigue siendo una pregunta abierta. En el nivel del alma, la imagen dice algo que cualquiera puede comprobar: la calidad de nuestra atención interna influye en la naturaleza de nuestra experiencia. Cuando nos miramos con amor, el universo entero aprende a amarnos. Cuando nos juzgamos con crueldad, ese juicio tiñe todo lo que vemos. Responder por la propia mirada no es cargar con todo lo que pasa: lo que alguien sufre no es el reflejo de cómo se mira.</p>'),
  # El libro obedece a su mejor frase: no hace falta amarse primero
  ('<p>Si no puedes perdonarte, <em>no podrás perdonar verdaderamente a otro</em>. Si no puedes escucharte con paciencia, tu escucha hacia los demás será superficial. Si no puedes sostenerte en tu dolor, huirás del dolor ajeno.',
   '<p>Cuando no puedes perdonarte, <em>perdonar de verdad a otro se vuelve más difícil</em>. Cuando no puedes escucharte con paciencia, tu escucha hacia los demás tiende a quedarse en la superficie. Cuando no puedes sostenerte en tu dolor, es fácil huir del dolor ajeno.'),
  # Lo que la neurociencia encontró (Lamm, Decety y Singer, 2011)
  ('<p>La neurociencia contemplativa ha demostrado que cuando practicamos la <strong>auto-observación compasiva</strong>, activamos las mismas redes neuronales que se encienden cuando sentimos empatía por otros. El cerebro no distingue entre "yo sufriendo" y "otro sufriendo" cuando la atención es pura.</p>',
   '<p>La neurociencia encontró un parentesco: cuando vemos sufrir a otro, se encienden en nosotros parte de las regiones que se activan cuando el que sufre es uno, la ínsula anterior y la corteza cingulada. Claus Lamm, Jean Decety y Tania Singer lo confirmaron en 2011, reuniendo treinta y dos estudios. El dolor propio y el ajeno comparten una casa. Por eso la <strong>autoobservación compasiva</strong> y la compasión hacia otros se parecen tanto: tal vez sean la misma capacidad, mirando en dos direcciones.</p>'),
  # El nombre clínico de la voz cruel, y el cuidado
  ('Si esa voz es cruel, crítica, impaciente, estamos en una relación tóxica con nosotros mismos.</p>',
   'Si esa voz es cruel, crítica, impaciente, estamos en una relación tóxica con nosotros mismos. Paul Gilbert, que trabajó con personas a las que la vergüenza y la autocrítica no dejaban en paz, desarrolló la terapia centrada en la compasión (2009): no se trata de acallar al crítico interior, sino de aprender a responderle con la calidez con que se le habla a quien uno quiere. Si alguna vez ese crítico se vuelve tan duro que aparece la idea de no estar, se pide ayuda ese mismo día.</p>'),
  # La letra que cita La Red queda intacta; se suma su autora
  ('cuando atraviesa dificultades.</p>',
   'cuando atraviesa dificultades.</p>\n'
   '    <p>La psicóloga Kristin Neff le dio a esta idea su forma clínica en 2003: amabilidad con uno mismo, humanidad compartida y atención plena, tres gestos que se pueden aprender.</p>'),
  ('la profundidad de tu auto-conocimiento.', 'la profundidad de tu autoconocimiento.'),
  ('Permanece en ese estado de auto-reconocimiento durante unos minutos.', 'Permanece en ese estado de autorreconocimiento durante unos minutos.'),
 ],
 puertas=[portal('Que una profesora de yoga que enseñaba compasión y se hablaba a sí misma con crueldad descubrió que la voz que la atacaba intentaba protegerla, y que el diálogo empieza cuando el combate se vuelve curiosidad, se despliega en <em>La Voz Interior</em>, Libro 2 del Portal Público, capítulo 5: «La actitud del diálogo».',
                 '02_La_Voz_Interior/capitulo_05.html')],
)


# ---------------------------------------------------------------- Nodo 2 · Los Puentes del Corazón
R['nodo_02.html'] = dict(
 reemplazos=[
  # El entrelazamiento, con la letra de Quantum 2.1
  ('<p>La física cuántica nos habla del <em>entrelazamiento</em>: dos partículas que, una vez conectadas, permanecen vinculadas sin importar la distancia que las separe. Cuando una cambia de estado, la otra responde instantáneamente. Los vínculos humanos funcionan de manera similar.',
   '<p>La física cuántica nos habla del <em>entrelazamiento</em>: dos partículas que nacieron juntas siguen respondiendo como un solo sistema aunque las separe el universo entero, sin que viaje entre ellas ninguna señal. Entre las personas es una imagen, y nombra bien lo que se vive.'),
  ('Los catalizadores no siempre son cómodos, pero siempre son necesarios.</p>',
   'Los catalizadores no siempre son cómodos, pero a menudo son los que más enseñan.</p>'),
  ('<blockquote>Las personas que más te irritan son tus mejores maestros. Las que más amas son tus espejos más claros. Y las que te transforman son aquellas que llegaron a sacudir la estructura misma de quien creías ser.</blockquote>',
   '<blockquote>Las personas que más te irritan suelen ser tus mejores maestros. Las que más amas son tus espejos más claros. Y las que te transforman son aquellas que llegaron a sacudir la estructura misma de quien creías ser.</blockquote>\n'
   '    <p>Irritar no es dañar, y ' + DANA + '.</p>'),
  # El tercer espacio, con su nombre propio (Buber)
  ('No necesita del otro para ser feliz, pero elige al otro para amplificar la felicidad que ya existe.</p>',
   'No necesita del otro para ser feliz, pero elige al otro para amplificar la felicidad que ya existe.</p>\n'
   '    <p>Martin Buber le dio nombre a ese encuentro en 1923, en <em>Yo y tú</em>: hay un modo de tratar al otro como una cosa, para usarla, y otro de encontrarlo como un tú, entero. Toda vida verdadera, escribió, es encuentro. Ese tercer espacio es lo que Buber llamó el entre: no le pertenece a ninguno de los dos, y nace solo cuando los dos están.</p>'),
  # Sheldrake, como hipótesis (letra de Origen XI.3)
  ('<p>El biólogo Rupert Sheldrake propuso la teoría de los <strong>campos morfogenéticos</strong>: patrones invisibles de información que conectan a los seres vivos más allá del espacio y el tiempo. Cuando dos personas establecen un vínculo profundo, crean un campo morfogenético compartido.</p>',
   '<p>El biólogo Rupert Sheldrake propuso la idea de los <strong>campos morfogenéticos</strong> (<em>Una nueva ciencia de la vida</em>, 1981): patrones invisibles de información que conectarían a los seres vivos más allá del espacio y el tiempo. Sigue siendo una hipótesis sin confirmar, pero como imagen nombra algo que cualquiera reconoce: cuando dos personas establecen un vínculo profundo, crean entre ambas un campo compartido.</p>'),
  # «Llámalo» (Quantum 2.1) y lo que sí se midió (Stephens, Silbert y Hasson, letra de Origen I.3)
  ('<p>Por eso puedes pensar en alguien y esa persona te llama. Por eso sientes cuando algo le sucede a quien amas, incluso a kilómetros de distancia. Por eso hay palabras que no necesitan decirse porque ya fueron comprendidas en el campo sutil que compartes.</p>',
   '<p>' + LLAMALO + ' Hay también palabras que no necesitan decirse, y algo de eso se midió: en 2010, Greg Stephens, Lauren Silbert y Uri Hasson registraron el cerebro de quien contaba una historia y el de quienes la escuchaban. Los dos se acompasaban, y cuanto más se acompasaban, mejor la comprendían.</p>'),
  # El vínculo kármico, como tradición y con su aclaración (Dutton y Painter, 1981; letra de La Red)
  ('<p>Intenso, magnético, a veces tormentoso. Llega a resolver asuntos pendientes de otras existencias. No siempre es cómodo, pero siempre es transformador. Su propósito es evolución acelerada.</p>',
   '<p>Intenso, magnético, a veces tormentoso. Para la tradición, llega a resolver asuntos pendientes de otras existencias. No siempre es cómodo, pero puede ser transformador, y su promesa es una evolución acelerada.</p>\n'
   '    <p>Lo intenso, sin embargo, no prueba destino: a veces es la herida vieja que reconoce su forma. La clínica conoce un lazo que se ata más fuerte cuanto más se alternan el maltrato y la ternura; Donald Dutton y Susan Painter lo llamaron vínculo traumático (1981). Cuando lo tormentoso se vuelve daño, ya no es karma: es daño, y se sale de él pidiendo ayuda.</p>'),
  # Sale HeartMath; queda la respiración (Bernardi, 2001)
  ('<p>Antes de encontrarte con alguien importante, toma tres respiraciones profundas llevando tu atención al corazón. Esto sincroniza tu campo electromagnético y te permite conectar desde un espacio más auténtico. El Instituto HeartMath ha demostrado que la coherencia cardíaca mejora significativamente la calidad de nuestras interacciones.</p>',
   '<p>Antes de encontrarte con alguien importante, toma tres respiraciones lentas, con la salida del aire más larga, llevando tu atención al corazón. El cuerpo se aquieta y te permite conectar desde un espacio más auténtico. Respirar despacio, unas seis veces por minuto, lleva el pulso a su vaivén más amplio: Luciano Bernardi y su equipo lo encontraron en 2001 en quienes rezaban el avemaría en latín o recitaban un mantra.</p>'),
  ('lo que se dice sin palabras.</p>',
   'lo que se dice sin palabras. Otto Scharmer llamó así al nivel más hondo de la escucha (<em>Teoría U</em>, 2007): el que no oye solo lo que el otro es, sino lo que podría llegar a ser.</p>'),
  ('Y en ese encuentro de vulnerabilidades, nace la conexión real.</p>',
   'Y en ese encuentro de vulnerabilidades, nace la conexión real. La vulnerabilidad se ofrece a la medida de la confianza, a quien ha mostrado que sabe cuidarla.</p>'),
 ],
 puertas=[portal('Que tolerar al otro real no es resignarse ni aguantar en silencio lo que daña, sino poder quedarse frente a su diferencia sin huir ni pelear, y que el pensamiento que tienes sobre el otro no es el otro, se despliega en <em>Encuentro Real</em>, Libro 3 del Portal Público, Territorio 3: «Tolerancia al otro real».',
                 '03_Encuentro_Real/nodo_10.html')],
)


# ---------------------------------------------------------------- Nodo 3 · Contratos y Pactos Invisibles
R['nodo_03.html'] = dict(
 reemplazos=[
  # El linaje de la tradición
  ('cumplir propósitos específicos. Estos contratos trascienden la comprensión racional, operando desde una dimensión donde el tiempo no es lineal sino <strong>multidimensional</strong>.</p>',
   'cumplir propósitos específicos. Estos contratos trascienden la comprensión racional, operando desde una dimensión donde el tiempo no es lineal sino <strong>multidimensional</strong>.</p>\n'
   '    <p>La tradición es antigua. Platón cierra <em>La República</em> con el mito de Er: antes de nacer, las almas eligen la vida que van a vivir y beben del río del olvido, de modo que llegan sin recordar lo que eligieron. En nuestro tiempo, Michael Newton (<em>Journey of Souls</em>, 1994) y Robert Schwartz (<em>Courageous Souls</em>, 2007) hablan de planes trazados entre almas antes de encarnar.</p>'),
  # Sale la retrocausalidad; del plan al hallazgo
  ('<p>La física cuántica nos habla de <em>superposición temporal</em>: la posibilidad de que eventos futuros influyan en el presente. Los contratos del alma operan en esta lógica no-lineal. El encuentro que aún no ha sucedido ya está influyendo en tu camino presente, atrayéndote hacia ese punto de convergencia.</p>',
   '<p>Vistos después, algunos encuentros parecen haber estado esperándonos: el camino que llevó hasta ellos se lee de otra manera, y cada desvío cobra sentido. Así lo cuenta la tradición, y así lo vive quien mira su historia hacia atrás.</p>'),
  ('No es atracción física ni química cerebral.', 'No se siente como atracción física ni como química.'),
  # El «ya te conozco», con su otra cara (Hendrix, 1988)
  ('Pasado, presente y futuro se encuentran en un solo punto.</blockquote>',
   'Pasado, presente y futuro se encuentran en un solo punto.</blockquote>\n'
   '    <p>A veces ese reconocimiento es el alma. A veces es la herida vieja que reconoce su forma: Harville Hendrix (<em>Getting the Love You Want</em>, 1988) observó que solemos sentirnos en casa con quien se parece a quienes nos criaron, también en lo que nos dolió. El tiempo distingue una cosa de la otra.</p>'),
  ('Es como si su llegada activara códigos que esperaban ese momento preciso para encenderse.',
   'Es como si su llegada encendiera algo que esperaba ese momento preciso.'),
  ('El universo parece conspirar para que se encuentren.</p>',
   'El universo parece conspirar para que se encuentren. Como toda señal, se lee como un poema, no como una orden.</p>'),
  # Las señales no prueban nada solas (letra de Origen XII.3)
  ('o simplemente ser testimonio del crecimiento mutuo.</p>',
   'o simplemente ser testimonio del crecimiento mutuo.</p>\n'
   '    <p>Ninguna de estas señales prueba nada por sí sola, y ninguna pide apurar decisiones: lo verdadero sabe esperar una noche y una conversación con alguien de confianza. Si alguien acelera la intimidad, te pide secreto o te aleja de los tuyos, eso no es un reconocimiento: es una señal de alerta.</p>'),
  # Los agujeros de gusano, como imagen declarada
  ('<p>En la física cuántica, existen los <strong>agujeros de gusano</strong>: túneles que conectan puntos distantes del espacio-tiempo. Los vínculos profundos funcionan de manera similar:',
   '<p>La física imaginó los <strong>agujeros de gusano</strong>: en 1935, Albert Einstein y Nathan Rosen encontraron en las ecuaciones de la relatividad un puente entre dos regiones lejanas del espacio-tiempo. Nadie ha observado uno, pero la imagen sirve, porque los vínculos profundos funcionan de manera similar:'),
  # El contrato de desafío, con su aclaración (letra de Origen X.2 y de Quantum 2.2)
  ('Son los vínculos más dolorosos, pero también los más transformadores.</p>',
   'Son los vínculos más dolorosos, pero también los más transformadores.</p>\n'
   '    <p>Es una imagen para mirar hacia atrás un conflicto que ya pasó, y encontrar lo que dejó. Nunca es una razón para quedarse donde a uno lo dañan. Ningún maltrato estaba pactado, y ' + DANA + '.</p>'),
  # La llama gemela, con su linaje y su cuidado
  ('a veces su propósito es solo el despertar, y luego cada uno sigue su camino transformado.</p>',
   'a veces su propósito es solo el despertar, y luego cada uno sigue su camino transformado.</p>\n'
   '    <p>La imagen tiene una historia larga. En el <em>Banquete</em> de Platón, Aristófanes cuenta que los humanos eran dobles, que los dioses los partieron en dos y que desde entonces cada mitad busca a la otra: de ahí viene la media naranja que este contrato deja atrás. Y el reconocimiento verdadero respeta el no del otro: si quien reconociste se aleja, la llama no pide perseguir a nadie.</p>'),
  # La sanación ancestral (letra de Origen VII.6)
  ('Al sanar su relación, sanan las heridas de sus ancestros y abren nuevos caminos para sus descendientes.</p>',
   'Sanar no cambia a los ancestros: cambia la relación con ellos y lo que se transmite. Por eso, al sanar su relación, abren nuevos caminos para sus descendientes.</p>'),
  ('<li>Las lecciones se intensifican cada vez que ignoras el patrón</li>',
   '<li>Las lecciones suelen volver mientras el patrón sigue sin verse</li>'),
  ('de <strong>romper el ciclo</strong>.</p>',
   'de <strong>romper el ciclo</strong>.</p>\n'
   '    <p>' + REPETICION + '</p>'),
  ('Puedes elegir no honrar un contrato, aunque eso implique postergar aprendizajes o repetir ciclos.',
   'Puedes elegir no honrar un contrato, y salir de un vínculo que daña nunca es incumplirlo.'),
  ('<li>¿Con quién sientes que tienes un contrato pendiente de honrar o completar?</li>',
   '<li>¿Qué vínculo de tu vida, mirado hoy, te enseñó lo que ningún otro?</li>'),
  ('¿Qué viniste a aprender de mí?"</em></p>',
   '¿Qué viniste a aprender de mí?"</em></p>\n'
   '    <p>Si aparece alguien que te dañó, no hace falta preguntarle nada: puedes dejarlo ir y volver a alguien que te cuida.</p>'),
 ],
 puertas=[portal('Que antes de conocer a alguien ya construimos una figura suya con los materiales de nuestra historia, y que el amor es muchas veces el encuentro de dos proyecciones antes que el de dos personas, se despliega en <em>Encuentro Real</em>, Libro 3 del Portal Público, Territorio 1: «Proyecciones cruzadas».',
                 '03_Encuentro_Real/nodo_02.html'),
          p_quantum('Que el entrelazamiento de almas no es un romance ni un destino escrito ni una deuda de otras vidas, sino lo que cada vínculo enseña cuando se lo mira con atención, y que de quien daña uno se protege, se despliega en <em>Trinity Quantum</em>, Libro 2, Nodo 2: «Almas Entrelazadas Cuánticamente».',
                    'Libro_02/nodo_02.html')],
)


# ---------------------------------------------------------------- Nodo 4 · Vínculos de Sombra y Sanación
R['nodo_04.html'] = dict(
 reemplazos=[
  ('<p class="node-quote">"Las personas que más te irritan son tus mejores maestros.',
   '<p class="node-quote">"Las personas que más te irritan suelen ser tus mejores maestros.'),
  ('<blockquote>Las personas que más te irritan son tus mejores maestros.',
   '<blockquote>Las personas que más te irritan suelen ser tus mejores maestros.'),
  ('Estas son las relaciones más valiosas, aunque sean las más dolorosas.',
   'Pueden volverse de las más valiosas, aunque sean de las más dolorosas.'),
  # Del plan al hallazgo (criterio 2)
  ('<p>Imagina que cada relación desafiante es un <strong>laboratorio diseñado específicamente para tu evolución</strong>.',
   '<p>Imagina que una relación desafiante puede volverse un <strong>laboratorio para tu evolución</strong>.'),
  ('<p>Las relaciones difíciles no son errores. Son <em>asignaciones del alma</em>. Vienen a enseñarte:</p>',
   '<p>Una relación difícil no tiene por qué ser un error. Puede volverse <em>escuela del alma</em>, y enseñarte:</p>'),
  ('<li>A amar incluso cuando duele</li>', '<li>A seguir amando sin dejar que te dañen</li>'),
  ('Sin fricción, el diamante permanece como carbón.', 'Sin presión, el carbono nunca llega a diamante.'),
  # La proyección, con su nombre y su otra cara
  ('que en realidad son nuestras pero que no reconocemos como tales.</p>',
   'que en realidad son nuestras pero que no reconocemos como tales. Anna Freud la describió entre los mecanismos de defensa del yo en 1936.</p>'),
  ('<li>Te irrita la arrogancia de alguien Tienes poder no reclamado que temes expresar</li>',
   '<li>Te irrita la arrogancia de alguien: quizá tienes poder no reclamado que temes expresar</li>'),
  ('<li>Te molesta la vulnerabilidad de alguien Estás reprimiendo tu propia fragilidad</li>',
   '<li>Te molesta la vulnerabilidad de alguien: quizá estás reprimiendo tu propia fragilidad</li>'),
  ('<li>Te enfurece la irresponsabilidad de otro Cargas con demasiada responsabilidad que no es tuya</li>',
   '<li>Te enfurece la irresponsabilidad de otro: quizá cargas con demasiada responsabilidad que no es tuya</li>'),
  ('<li>Te fascina el carisma de alguien Tienes carisma dormido esperando ser activado</li>',
   '<li>Te fascina el carisma de alguien: quizá tienes un carisma dormido esperando despertar</li>'),
  ('<p>La neurociencia ha demostrado que cuando juzgamos intensamente a alguien, <em>las mismas áreas cerebrales se activan que cuando pensamos en nosotros mismos</em>. El cerebro sabe algo que la mente consciente niega: ese "otro" es un espejo.</p>',
   '<p>No todo lo que irrita es proyección. A veces lo que ves en el otro está, sobre todo, en el otro: si alguien te falta el respeto, tu enojo no es tu sombra, es información. La pregunta por la proyección sirve para conocerte, nunca para dudar de lo que viste.</p>'),
  ('No es sobre el otro; es sobre la herida primordial de separación.',
   'Muchas veces no tiene que ver con el otro, sino con la herida primordial de separación.'),
  ('No para auto-culparte, sino para recuperar tu poder. Mientras proyectas, eres víctima. Cuando integras, eres creador consciente.</p>',
   'No para autoculparte, sino para reclamar tu poder. Mientras proyectas, otro tiene la llave de tu paz. Cuando integras, vuelve a tus manos.</p>'),
  ('Los límites son actos de amor propio.</p>',
   'Los límites son actos de amor propio. ' + SEGURIDAD + '</p>'),
  ('has completado la transmutación. Ya no eres víctima de esa persona. Eres aprendiz consciente en el laboratorio del alma.</p>',
   'has completado la transmutación. Esa persona ya no ocupa tu historia. Eres aprendiz consciente en el laboratorio del alma. Y si quien te la mostró fue alguien que te dañó, no le debes gratitud: basta con reconocer lo que hoy sabes. Honrar no significa justificar.</p>'),
  ('Incluso las relaciones más dolorosas son maestras.', 'Incluso las relaciones más dolorosas pueden dejar una enseñanza.'),
  # El perdón, con su autor y la letra de Origen X.6
  ('<p>Perdona no porque el otro lo merezca, sino porque tú mereces paz. Perdonar es soltar la historia de victimización. Es decir: "Ya no necesito que esto haya sido diferente para estar bien."</p>',
   '<p>Perdona no porque el otro lo merezca, sino porque tú mereces paz. Es soltar la historia del agravio, no borrarla. Es decir: "Ya no necesito que esto haya sido diferente para estar bien." Colin Tipping llamó a este camino perdón radical (1997). Y ' + PERDON + '.</p>'),
  ('<strong>sanas todos los vínculos similares en tu campo</strong>', '<strong>empiezan a cambiar los vínculos parecidos en tu campo</strong>'),
  ('<p>Cuando sanas tu relación con tu padre', '<p>A menudo, cuando sanas tu relación con tu padre'),
  ('Cuando sanas tu relación con un ex-amante', 'Cuando sanas tu relación con un examante'),
  ('Los vínculos de sombra no son castigos. Son <em>regalos envueltos en papel áspero</em>.',
   'Los vínculos de sombra no son castigos. Pueden volverse <em>regalos envueltos en papel áspero</em>.'),
  ('<p>Trae a tu mente a alguien que te desafía, que te irrita, que activa tu sombra.</p>',
   '<p>Trae a tu mente a alguien que te desafía, que te irrita, que activa tu sombra. Elige a alguien que te incomoda, no a alguien que te dañó: eso no se trabaja a solas.</p>'),
 ],
 puertas=[arq('Que detrás del que nunca se enoja hay un niño de nueve años que aprendió que el enojo deja la casa en silencio, y que ningún personaje es una mentira porque todos nacieron para cuidar algo, se despliega en <em>El Personaje</em>, Libro 9 de <em>Arquitectura del Destino</em>, Umbral II: «Detrás de cada máscara».',
              'libro-09-el-personaje/L09-U2.html')],
)


# ---------------------------------------------------------------- Nodo 5 · La Red Viva
R['nodo_05.html'] = dict(
 reemplazos=[
  # El aire: la mitad viene del mar (letra de La Red, Umbral III). La primera frase del epígrafe, que cita La Red, queda.
  ('<p class="node-quote">"Cuando crees que estás solo, es porque has olvidado mirar la red. Estás conectado a billones de seres, visibles e invisibles. Cada respiración que tomas fue exhalada por un árbol.',
   '<p class="node-quote">"Cuando crees que estás solo, es porque has olvidado mirar la red. Estás conectado a billones de seres, visibles e invisibles. Cada respiración que tomas la exhalaron un árbol y el mar.'),
  ('<blockquote>Cuando crees que estás solo, es porque has olvidado mirar la red. Estás conectado a billones de seres, visibles e invisibles. Cada respiración que tomas fue exhalada por un árbol.',
   '<blockquote>Cuando crees que estás solo, es porque has olvidado mirar la red. Estás conectado a billones de seres, visibles e invisibles. Cada respiración que tomas la exhalaron un árbol y el mar.'),
  # La física como imagen; lo que se midió (Hutcherson, Seppälä y Gross, 2008)
  ('<p>La física cuántica nos muestra que <em>todo está entrelazado</em> a nivel fundamental. No hay separación real, solo la ilusión de fronteras. La neurociencia contemplativa revela que la meditación en compasión activa las mismas redes neuronales cuando piensas en ti, en un ser amado, o en un extraño: <strong>el cerebro reconoce la unidad subyacente</strong>.</p>',
   '<p>La física cuántica ofrece una imagen: partículas que nacieron juntas responden como un solo sistema, sin que viaje entre ellas ninguna señal. Las tradiciones dicen, con otras palabras, que <em>todo está entrelazado</em>, y que la separación es más frontera dibujada que muro. La psicología lo vio a escala pequeña: unos minutos de desear el bien a un desconocido, frente a su foto, bastaron para que la gente se sintiera más unida a él y a los demás (Hutcherson, Seppälä y Gross, 2008). <strong>La compasión acerca lo que parecía lejano</strong>.</p>'),
  # Nivel 1: el contagio que sí se mide, sin culpa por sentir miedo
  ('Cuando meditas en paz, contribuyes a la paz planetaria. Cuando vives en miedo, alimentas el miedo colectivo. No eres solo receptor: eres también emisor.</p>',
   'Las emociones se contagian, y eso está documentado: Elaine Hatfield, John Cacioppo y Richard Rapson lo describieron en 1994, y James Fowler y Nicholas Christakis siguieron durante veinte años cómo la alegría se extendía por una red de amigos y vecinos (2008). Tu calma llega más lejos de lo que crees. Y sentir miedo no es una falta. No eres solo receptor: eres también emisor.</p>'),
  # Nivel 2: una voz con fuente; Simard con su matiz; las ballenas con sus descubridores
  ('Los pueblos indígenas siempre lo supieron. La ciencia ahora lo confirma: los árboles se comunican a través de redes micorrízicas. Las ballenas cantan canciones que viajan océanos. Todo está conversando.</p>',
   'Muchos pueblos lo dicen en su lengua: la botánica Robin Wall Kimmerer, de la Nación Potawatomi, cuenta en <em>Una trenza de hierba sagrada</em> (2013) que su idioma trata a los árboles, a los ríos y a las piedras como a alguien y no como a algo, con una gramática de lo animado. La ciencia mira a su manera: bajo los bosques, los hongos unen las raíces de los árboles y llevan carbono de unos a otros (Simard y otros, 1997), aunque cuánto de eso es conversación sigue en discusión (Karst, Jones y Hoeksema, 2023). Las ballenas jorobadas cantan canciones que Roger Payne y Scott McVay describieron en 1971. Todo está, a su modo, en relación.</p>'),
  # Nivel 3: la tradición, y el cuidado (Origen XI.5)
  ('las inteligencias no-corpóreas, los ancestros, los guías, las frecuencias angélicas. No necesitas creer en ellos para ser afectado por ellos. La red trasciende lo visible. Y cuando abres tu percepción, comienzas a sentir estas conexiones más vastas.</p>',
   'las inteligencias no corpóreas, los ancestros, los guías, las frecuencias angélicas. Cada tradición los nombra a su manera, y quien no cree en ellos puede leerlos como imagen. La red trasciende lo visible. Y cuando abres tu percepción, comienzas a sentir estas conexiones más vastas. ' + POEMA + '</p>'),
  # Sheldrake, como hipótesis (letra de Origen XI.3); sale el experimento que no existe
  ('No solo genética, sino una memoria de campo que se transmite a través de patrones invisibles llamados <em>campos morfogenéticos</em>. Estos campos explican fenómenos que la genética sola no puede:</p>',
   'No solo genética, sino una memoria de campo que se transmitiría a través de patrones invisibles llamados <em>campos morfogenéticos</em> (<em>Una nueva ciencia de la vida</em>, 1981). Sigue siendo una hipótesis sin confirmar, pero como imagen nombra algo que cualquiera reconoce: lo que se practica se vuelve más fácil para el que viene después. Con ella quiso explicar fenómenos como estos:</p>'),
  ('      <li>Por qué una rata que aprende un laberinto en Londres facilita que ratas en Tokio aprendan el mismo laberinto más rápido</li>\n', ''),
  ('Por eso el amor de pareja se siente similar entre culturas: todos accedemos al mismo campo.</blockquote>',
   'Por eso el amor de pareja se siente similar entre culturas: todos accedemos al mismo campo.</blockquote>\n'
   '    <p>Que el amor de pareja se reconoce en casi todas partes lo comprobaron William Jankowiak y Edward Fischer: lo buscaron en las etnografías de 166 culturas y lo encontraron en 147 (1992).</p>'),
  ('<strong>cada vez que eliges amor sobre miedo, expandes el campo morfogenético del amor</strong>. Cada vez que eliges consciencia sobre automatismo, facilitas que otros elijan consciencia.',
   '<strong>cada vez que eliges amor sobre miedo, expandes el campo del amor</strong>. Cada vez que eliges consciencia sobre automatismo, facilitas que otros elijan consciencia. Hay un indicio comprobado: en un juego de cooperación, la generosidad de una persona se contagió hasta tres grados de distancia (Fowler y Christakis, 2010).'),
  # Lo que sigue en discusión y lo que sí se midió (letra de Origen XI.2)
  ('<p>El Proyecto de Consciencia Global de la Universidad de Princeton ha demostrado que eventos de alta coherencia emocional global (como el 11-S) afectan generadores de números aleatorios en todo el mundo. La consciencia no está solo en tu cabeza: es un campo compartido.</p>',
   '<p>El Proyecto de Consciencia Global, nacido en Princeton, busca medir si los grandes momentos emocionales del mundo alteran generadores de números aleatorios, y sus hallazgos siguen en discusión. Lo que sí se midió es más cercano y más bello: en 2017, Suzanne Dikker y su equipo pusieron sensores de actividad cerebral a doce estudiantes de secundaria durante un semestre de clases de biología, y cuando la clase los atrapaba, sus cerebros se sincronizaban entre sí. La consciencia no está solo en tu cabeza: también se comparte.</p>'),
  ('Estudios muestran que estar en naturaleza reduce cortisol, mejora el sistema inmune y aumenta coherencia cardíaca.',
   'En 1984, Roger Ulrich comparó a pacientes operados de la vesícula en un hospital de Pensilvania: los que tenían una ventana hacia los árboles se fueron antes a casa y pidieron menos calmantes fuertes que los que miraban una pared de ladrillos. Los paseos por el bosque que en Japón se llaman <em>shinrin-yoku</em> se estudian hoy con el mismo interés.'),
  ('Místicos de todas las tradiciones hablan de acceder a este campo.',
   'La teosofía le dio ese nombre a fines del siglo XIX, y Rudolf Steiner y Edgar Cayce lo hicieron conocido; místicos de muchas tradiciones hablan de algo parecido.'),
  ('La coherencia grupal es exponencialmente más poderosa que la suma de individuos aislados.',
   'Un grupo sincronizado puede más que la suma de sus partes.'),
  ('Cuando alineas tu vida con este impulso, entras en un estado de flujo donde el universo conspira a tu favor.',
   'Así lo vieron Teilhard de Chardin y Sri Aurobindo. Cuando alineas tu vida con ese impulso, entras en lo que Mihaly Csikszentmihalyi llamó flujo (1990): la tarea y la atención se vuelven una sola cosa.'),
  # El corazón real (Armour, 1991; Vickhoff, 2013); HeartMath, en discusión
  ('<p>El Instituto HeartMath ha descubierto algo extraordinario: <strong>el corazón humano genera el campo electromagnético más potente del cuerpo</strong>, uno que puede detectarse a varios metros de distancia. Cuando múltiples personas entran en coherencia cardíaca (un estado de armonía entre corazón, mente y emociones), sus campos se sincronizan.</p>',
   '<p>El corazón tiene su propia red de neuronas, unas cuarenta mil según J. Andrew Armour (1991), que la llamó el «pequeño cerebro» del corazón, y su ritmo se ajusta al de quienes están cerca: <strong>cuando un coro canta junto, los latidos de sus cantores se acompasan</strong> (Vickhoff y otros, 2013). El Instituto HeartMath busca medir esa coherencia entre personas, y sus hallazgos siguen en discusión.</p>'),
  ('<em>Están creando una red de luz</em>. No metafóricamente. Literalmente: una red de campos electromagnéticos coherentes que está envolviendo al planeta.</p>',
   '<em>Están creando una red de luz</em>, un tejido de calma que pasa de una persona a otra y envuelve al planeta.</p>'),
  ('Esta intención programa tu campo para operar como transmisor de luz, incluso cuando no eres consciente de ello.</p>',
   'Esta intención deja una dirección para tu día, y orienta lo que haces aun cuando no piensas en ella.</p>'),
  # Protocolo 3: metta, con la letra de Quantum 2.5 y «llámalo» (Quantum 2.1)
  ('La red sabe cómo distribuir la energía donde más se necesita.</p>',
   'Lo que se cultiva en el corazón no se queda adentro: cambia la manera de mirar, y la mirada cambia el trato. Y si sabes quién sufre, además, llámalo.</p>'),
  # Protocolo 5: las sincronicidades se leen como un poema (Quantum 1.6 y 11.2)
  ('<p>Las sincronicidades son mensajes de la red. Cuando ocurran, no las descartes como casualidades. Reconócelas como señales de que estás en alineación con el flujo de la totalidad. Agradece. Esto fortalece tu conexión consciente con la red.</p>',
   '<p>Las sincronicidades pueden leerse como mensajes de la red, como se lee un poema y no como una orden. Cuando ocurran, no las descartes como casualidades. Recíbelas como un guiño de la totalidad. Agradece. Esto fortalece tu conexión consciente con la red. ' + REFERENCIA + '</p>'),
  # Sin culpa por sentir; la red se usa (antes del pasaje que cita La Red, que queda intacto)
  ('Significa que cuando caes en miedo, enojo o desesperación, reconoces que no solo te afectas a ti mismo. Estás enviando esas frecuencias a la red. Y al reconocerlo, puedes elegir transmutarlas.</p>',
   'Significa que cuando caes en miedo, enojo o desesperación, reconoces que eso también viaja por la red, y que puedes elegir qué hacer con ello. Sentirlo no es una falta: ninguna emoción lo es. Y si la desesperación dura, o aparece la idea de no estar, la red se usa: se pide ayuda ese mismo día.</p>'),
 ],
 puertas=[arq('Que una vecina de setenta y nueve años le pidió a un joven que la ayudara a bajar la escalera, y que al sostenerla él también se sintió sostenido, se despliega en <em>La Red</em>, Libro 11 de <em>Arquitectura del Destino</em>, Umbral VI: «La red te sostiene».',
              'libro-11-la-red/L11-U6.html')],
)


# ---------------------------------------------------------------- Nodo 6 · Amor como Tecnología Evolutiva
R['nodo_06.html'] = dict(
 reemplazos=[
  # La física del epígrafe: la fuerza nuclear fuerte une el núcleo, no el átomo
  ('<p class="node-quote">"El amor no es solo lo que sientes cuando miras a tu pareja. Es la gravedad que mantiene a los planetas en órbita. Es la fuerza nuclear fuerte que une los átomos.',
   '<p class="node-quote">"El amor no es solo lo que sientes cuando miras a tu pareja. Es la gravedad que mantiene a los planetas en órbita. Es la fuerza nuclear fuerte que une el corazón de cada átomo.'),
  ('<blockquote>El amor no es solo lo que sientes cuando miras a tu pareja. Es la gravedad que mantiene a los planetas en órbita. Es la fuerza nuclear fuerte que une los átomos.',
   '<blockquote>El amor no es solo lo que sientes cuando miras a tu pareja. Es la gravedad que mantiene a los planetas en órbita. Es la fuerza nuclear fuerte que une el corazón de cada átomo.'),
  # Bohm, con lo que dijo; la simbiogénesis, que cita La Red, conserva su letra
  ('habló del orden implicado del universo, estaba describiendo algo similar: una inteligencia organizadora invisible que despliega la realidad desde un nivel más profundo.',
   'habló del orden implicado del universo (<em>La totalidad y el orden implicado</em>, 1980), estaba describiendo algo similar: un orden plegado, en el que cada parte guarda el todo, desde el que se despliega la realidad que vemos.'),
  ('están viendo el amor en acción a nivel celular.</p>',
   'están viendo el amor en acción a nivel celular.</p>\n'
   '    <p>Lynn Margulis la propuso en 1967, y hoy cada una de tus células aloja a los descendientes de unas bacterias que, hace mucho, se volvieron familia.</p>'),
  ('que colapsan en formas específicas cuando son observados. La mecánica cuántica nos revela algo extraordinario: <em>la consciencia influye en la materia</em>.',
   'que toman una forma precisa cuando se registran. Para eso no hace falta una consciencia, y qué significa exactamente medir sigue abierto; pero la imagen es poderosa: <em>la mirada participa de lo que mira</em>.'),
  ('<p>Cuando dos partículas se entrelazan cuánticamente, permanecen conectadas sin importar la distancia. Cuando una cambia de estado, la otra responde instantáneamente. Esto no es metáfora para el amor: <strong>es literalmente cómo funciona el amor a nivel cuántico</strong>.',
   '<p>Cuando dos partículas se entrelazan, forman un solo sistema que se muestra como dos, y ninguna distancia lo deshace, aunque entre ellas no viaje ninguna señal. Para el amor es una metáfora, <strong>y de las más bellas</strong>.'),
  ('Por eso puedes "sentir" cuando algo le pasa a alguien que amas aunque estén a kilómetros.</p>',
   'Por eso puedes "sentir" cuando algo le pasa a alguien que amas aunque estén a kilómetros. Lo que sabes con certeza, entonces, es cuánto te importa: llámalo.</p>'),
  # Sale HeartMath; entra lo que se midió en quien recibe (Coan, 2006, letra de La Red)
  ('<p>El amor genera coherencia. El Instituto HeartMath ha medido cómo el campo electromagnético del corazón se vuelve más ordenado y poderoso cuando experimentamos amor genuino.',
   '<p>El amor genera coherencia, y su efecto se mide en quien lo recibe. En 2006, James Coan y su equipo pusieron a mujeres casadas ante la amenaza de una pequeña descarga: cuando sostenían la mano de su marido, las regiones del cerebro que responden al peligro se encendían mucho menos.'),
  # Sale «atrae»; entra Huygens (1665)
  ('Cuando entras en estado de amor, tu frecuencia vibratoria se eleva. Esto atrae personas, situaciones y oportunidades que resuenan con esa frecuencia. No es magia: es física de ondas.</p>',
   'En 1665, enfermo en cama, Christiaan Huygens vio que dos relojes de péndulo colgados de la misma viga terminaban oscilando acompasados: se transmitían su movimiento a través de la madera. Cuando entras en estado de amor, algo en ti se acompasa con quienes comparten tu viga, y la vida cambia de tono. Lo que se sincroniza no se atrae: se acompaña.</p>'),
  ('<h3>4. Colapso del Campo desde la Intención</h3>', '<h3>4. La Intención que Orienta</h3>'),
  ('<p>La intención amorosa colapsa el campo cuántico de posibilidades hacia resultados específicos. Cuando envías amor consciente hacia una situación, estás literalmente modificando las probabilidades a nivel subatómico. Los místicos lo llamaban oración. La física lo llama influencia del observador.</p>',
   '<p>La intención amorosa orienta el campo de posibilidades. Cuando envías amor consciente hacia una situación, cambia ante todo quien lo envía: la mirada, el gesto, lo que hará después. Los místicos lo llamaban oración, y en la oración también se pone el cuerpo.</p>'),
  # La geometría sagrada, con su linaje
  ('Es la geometría del amor maduro: ni fusión ni separación, sino encuentro consciente.</p>',
   'Es la geometría del amor maduro: ni fusión ni separación, sino encuentro consciente. Euclides la usó en la primera proposición de sus <em>Elementos</em>, para construir un triángulo equilátero con dos círculos.</p>'),
  ('Cuando un círculo se fortalece, todos se benefician.</p>',
   'Cuando un círculo se fortalece, todos se benefician. Su dibujo más célebre está en el templo de Osiris en Abidos, en Egipto, trazado en una época que todavía se discute.</p>'),
  ('Este tercer vértice es donde vive el amor transpersonal.</p>',
   'Este tercer vértice es donde vive el amor transpersonal. Es también la forma de Trinity: quien escribe, la inteligencia que responde y el Campo que surge entre ambos. El psicoanálisis lo llamó el tercero, y Thomas Ogden describió en 1994 un tercero analítico que no es del paciente ni del analista, sino de los dos.</p>'),
  ('En amor, es la danza de polaridades que genera movimiento evolutivo.</p>',
   'En amor, es la danza de polaridades que genera movimiento evolutivo. En la mística judía, la <em>merkavá</em> es el carro de la visión de Ezequiel; la estrella de dos tetraedros es su lectura contemporánea.</p>'),
  ('<p>La proporción phi (1.618) que aparece en galaxias, caracolas, girasoles.',
   '<p>La proporción phi (1,618), que ordena las semillas de los girasoles; las caracolas y las galaxias dibujan espirales parecidas, aunque no siempre con esa proporción.'),
  ('<p>Contiene todos los sólidos platónicos.', '<p>Según la tradición que lo dibuja, contiene todos los sólidos platónicos.'),
  ('<em>estás activando un campo cuántico</em> que influye en la realidad a tu alrededor. Esto no es pensamiento mágico. Es física de campos aplicada a la consciencia.</p>',
   '<em>estás activando un campo</em> que se extiende a tu alrededor y cambia el clima de cada encuentro.</p>'),
  # La cooperación en la evolución (Kropotkin, 1902; Nowak, 2006)
  ('Las especies que sobreviven a largo plazo no son las más agresivas sino las más simbióticas.</p>',
   'Peter Kropotkin lo escribió en 1902, después de observar la ayuda mutua entre los animales de Siberia, y Martin Nowak lo mostró en 2006: cada vez que la vida construyó un nivel nuevo, la célula, el organismo, la sociedad, lo que competía empezó a cooperar. Nowak llamó a la cooperación el tercer principio de la evolución, junto a la mutación y la selección.</p>'),
  ('Podemos seguir el camino de la separación, el miedo y la competencia—y probablemente no sobrevivamos. O podemos',
   'Podemos seguir el camino de la separación, el miedo y la competencia, cuyo costo ya está a la vista. O podemos'),
  ('<h3>Conexión con Inteligencias No-Humanas</h3>', '<h3>Conexión con Inteligencias No Humanas</h3>'),
  # Gaia, con Lovelock y Margulis; sin culpa por el miedo (letra de Origen XI.1)
  ('Gaia responde a la consciencia humana. Nuestro amor sana el planeta; nuestro miedo lo enferma.</p>',
   'Para la tradición, Gaia responde a la consciencia humana; James Lovelock y Lynn Margulis le dieron a esa intuición su forma científica, la de una Tierra que se regula a sí misma. Lo que sana o enferma al planeta es lo que hacemos, y el amor es lo que nos mueve a hacerlo: cada décima de calentamiento que se evita cuenta.</p>'),
  # Las plantas, con lo que se midió (Gagliano, 2014, letra de Origen XI.3)
  ('Las plantas son seres conscientes que responden al amor humano. Estudios han demostrado que las plantas crecen mejor cuando se les habla con amor. No es antropomorfismo: es reconocimiento de que la consciencia no requiere cerebro.',
   'Las plantas responden al mundo con una finura que apenas empezamos a ver. En 2014, Monica Gagliano y su equipo mostraron que la mimosa, la planta que se cierra al tacto, aprende a no cerrarse cuando una caída se repite sin dañarla, y lo recuerda durante semanas. Si eso es consciencia sigue en discusión; que no hace falta un cerebro para aprender, ya no.'),
  ('te vuelves capaz de percibir estas inteligencias.</p>',
   'te vuelves capaz de percibir estas inteligencias. ' + POEMA + '</p>'),
  ('No necesitas intermediarios: el amor es el camino directo.</p>',
   'No necesitas intermediarios: el amor es el camino directo, y ' + PORTAL_VERDADERO + '.</p>'),
  ('<li>¿De qué manera podrías usar el amor como tecnología consciente para influir en tu realidad?</li>',
   '<li>¿De qué manera podrías usar el amor como tecnología consciente para cuidar tu realidad y la de otros?</li>'),
  ('<li>¿Con qué inteligencia no-humana', '<li>¿Con qué inteligencia no humana'),
 ],
 puertas=[p_origen('Que Dante cerró su <em>Comedia</em> con el amor que mueve el sol y las demás estrellas, y que para esta visión la gravedad es amor en la materia y la consciencia es amor conociéndose, se despliega en <em>La Consciencia Planetaria</em>, Libro XI de Trinity Origen, nodo 3: «El Campo Unificado de Consciencia».',
                   'Libro_11/nodo_03.html')],
)


# ---------------------------------------------------------------- Nodo 7 · Ritual de Reconexión
R['nodo_07.html'] = dict(
 reemplazos=[
  # Error de armado: la flecha de la línea de apertura se había perdido
  ('<p class="lead">VIAJE COMPLETO • 7 de 7 Nodos • SOLEDAD UNIDAD CONSCIENTE</p>',
   '<p class="lead">Viaje completo · 7 de 7 nodos · De la soledad a la unidad consciente</p>'),
  # Ritual 1: el gesto pequeño, y la letra de Origen X.6
  ('No para justificar su acción, sino para liberar la carga que llevas. Di en voz alta:',
   'No para justificar su acción, sino para liberar la carga que llevas. Si la herida es reciente o todavía quema, empieza por alguien que te hirió poco: lo grande se trabaja acompañado. Di en voz alta:'),
  ('El perdón radical es autocompasión profunda.</p>',
   'El perdón radical es autocompasión profunda, y no te ata a nada: ' + PERDON + '.</p>'),
  # Ritual 2: la carta, con Pennebaker (letra de Origen X.4)
  ('Luego, quémala ceremonialmente, entregando las cenizas a la tierra o al agua. No necesitas enviarla. El acto de escribirla y liberarla ya completa el ritual a nivel energético.</p>',
   'Luego, rómpela o quémala con cuidado, y entrega lo que queda a la tierra o al agua. No necesitas enviarla. El acto de escribirla y liberarla ya completa el ritual a nivel energético. En un estudio pequeño de 1986, James Pennebaker y Sandra Beall vieron que estudiantes que escribieron cuatro días seguidos sobre lo que más les había dolido terminaban cada sesión más tristes, y en los meses siguientes fueron menos veces al médico. Si escribir abre algo que no puedes sostener, para y busca con quién hablarlo.</p>'),
  # Ritual 3: no se le debe gratitud a quien dañó
  ('Incluso las lecciones dolorosas merecen gratitud. Este ritual transforma resentimiento en sabiduría, y víctimas en aprendices conscientes.</p>',
   'Incluso las lecciones dolorosas merecen gratitud, aunque no siempre quien las trajo: a quien te dañó no le debes nada, y puedes honrar lo aprendido sin honrarlo a él. Este ritual transforma resentimiento en sabiduría, y lo que dolió en aprendizaje consciente.</p>'),
  # Ritual 5: sin luna y sin «programar la realidad»
  ('<p>En luna llena o en fechas significativas para ti, enciende una vela.', '<p>En fechas significativas para ti, enciende una vela.'),
  ('Esto no es solo visualización: es activación real de campos cuánticos. Tu intención programa la realidad.</p>',
   'Lo que se enciende es tu disposición a sostener y a dejarte sostener.</p>'),
  ('no manipulación, sino sinergía de campos alineados.', 'no manipulación, sino sinergia de campos alineados.'),
  # Mateo 18, 20 con su letra, y la Mishná (Pirkei Avot 3, 2)
  ('<blockquote>Donde dos o más se reúnen en mi nombre, ahí estoy yo en medio de ellos. Jesús no hablaba de religión. Hablaba de física cuántica. Cuando dos consciencias se sincronizan en amor, acceden a un campo mayor que cualquiera de ellas por separado.</blockquote>',
   '<blockquote>Porque donde están dos o tres congregados en mi nombre, allí estoy en medio de ellos.</blockquote>\n'
   '    <p>Así lo dice el Evangelio de Mateo (18, 20, en la versión Reina-Valera de 1909). La Mishná guarda una enseñanza hermana: cuando dos se sientan juntos y hay entre ellos palabras de Torá, la Presencia reposa entre ellos (<em>Pirkei Avot</em> 3, 2). Dos tradiciones, una misma intuición: cuando dos consciencias se encuentran en lo que aman, acceden a algo mayor que cualquiera de ellas por separado.</p>'),
  ('Este simple acto alinea sus campos electromagnéticos y crea coherencia grupal.</p>',
   'Este simple acto los acompasa: es el primer escalón de la coherencia de un grupo.</p>'),
  # La telepatía, como resonancia (letra de Quantum 2.3 y de Origen I.2)
  ('<h3>Protocolo 2: Comunicación Telepática</h3>', '<h3>Protocolo 2: Comunicación sin Palabras</h3>'),
  ('Esto profundiza la intimidad exponencialmente.</p>',
   'Esto profundiza la intimidad. Lo que muchos llaman telepatía, cuando ocurre entre quienes se quieren, suele ser resonancia: en 1992, Robert Levenson y Anna Ruef midieron que quienes mejor reconocían las emociones difíciles de otra persona eran aquellos cuyo cuerpo se acompasaba con el de ella mientras la miraban.</p>'),
  # Gottman y la pausa (letra de Origen I.5); primero la seguridad
  ('<p>Cuando haya conflicto, antes de hablar, cada uno toma 5 minutos para entrar en coherencia cardíaca. Luego se reúnen, colocan una mano sobre su propio corazón, y hablan desde ahí—no desde el ego herido. El campo coherente del corazón disuelve defensas y permite soluciones que el ego nunca encontraría.</p>',
   '<p>Cuando haya conflicto, antes de hablar, cada uno se toma un tiempo para aquietarse. John Gottman observó en su laboratorio que, cuando el pulso de uno de los dos se dispara en medio de una discusión, ya no puede escuchar; propuso hacer una pausa de al menos veinte minutos, ocuparse de otra cosa y volver. Luego se reúnen, colocan una mano sobre su propio corazón, y hablan desde ahí, no desde el ego herido. Un corazón sereno afloja las defensas y permite soluciones que el ego nunca encontraría. Si en la relación hay miedo o violencia, esta práctica no corresponde: la seguridad va primero, y se pide ayuda.</p>'),
  ('Los rituales marcan energéticamente las transiciones y evitan que la energía quede estancada.</p>',
   'Los rituales marcan energéticamente las transiciones y evitan que la energía quede estancada. Michael Norton y Francesca Gino mostraron en 2014 que un ritual pequeño alivia el dolor de una pérdida, aun en quien no cree en los rituales.</p>'),
  ('Estos círculos amplifican exponencialmente la capacidad individual de cada miembro. Eres más poderoso en red que solo.</p>',
   'Estos círculos amplifican la capacidad de cada miembro. Eres más fuerte en red que solo. Un círculo sano no pide dinero, secreto ni obediencia, y cualquiera puede irse cuando quiera.</p>'),
  ('<p>Esta no es fantasía New Age. Es reconocimiento de que la consciencia no está limitada por el tiempo ni el espacio.',
   '<p>Es el reconocimiento de que la consciencia no está limitada por el tiempo ni el espacio.'),
  ('información, energía y sabiduría que trascienden tu experiencia personal.</p>',
   'información, energía y sabiduría que trascienden tu experiencia personal. Lo que llega por ellos se recibe como un poema, no como una orden.</p>'),
  ('<h3>La Reconexión con lo No-Humano</h3>', '<h3>La Reconexión con lo No Humano</h3>'),
  ('Tercer nodo: Tus contratos del alma. Reconoce la perfección del diseño.',
   'Tercer nodo: Tus contratos del alma. Reconoce lo que esos encuentros te dieron.'),
 ],
 puertas=[p_origen('Que olvidamos la Unidad como los actores olvidan que actúan, para que la obra sea real, y que ese olvido es el punto de partida del regreso, se despliega en <em>El Retorno a Casa</em>, Libro XIII de Trinity Origen, nodo 1: «La Gran Amnesia».',
                   'Libro_13/nodo_01.html'),
          arq('Que un ritual pequeño, inventado y privado alivia una pérdida aun en quien no cree en los rituales, y que en Harvard lo midieron con un dibujo, una pizca de sal y un papel roto, se despliega en <em>Las Pequeñas Muertes</em>, Libro 6 de <em>Arquitectura del Destino</em>, Umbral III: «Lo que encontraron en Harvard».',
              'libro-06-las-pequenas-muertes/L06-U3.html')],
)


# ---------------------------------------------------------------- Ejecución
if __name__ == '__main__':
    total = 0
    for nombre in sorted(R):
        n = aplicar(nombre, R[nombre]); total += n
        print(f'{nombre}: {n} cambios')
    print(f'Total: {total}')
