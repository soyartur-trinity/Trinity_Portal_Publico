#!/usr/bin/env python3
"""Depuración de contenido de La Puerta (Portal Trinity, 00_Portal_Trinity, repositorio Trinity-).

18 de noviembre de 2026, con el veto del autor sobre cada tarjeta («Coincido en tu análisis y apruebo los
cambios»). Sigue la guía de la sección 5 del maestro v4 de Arquitectura del Destino: los cinco criterios,
las cuatro precisiones de Quantum y las dos de Origen, con la lente de Origen (riesgo clínico y puertas
hacia la Red). La Puerta tenía el esqueleto de Quantum (ecuación sagrada, códigos de activación,
protocolo de siete días), y por eso sigue sus cambios comunes.

Lo propio de este libro:
  - El libro obedece a sus mejores frases: «El mapa no es el territorio» (6), «Los peligros del Elegido» (8),
    «Receptividad no es ausencia de discernimiento» (5), «No juegues a terapeuta sin preparación» (11),
    «No hay jerarquía» (13).
  - La clave del arco (la séptima dovela del índice) es el nodo de la IA: el espejo deja de ser juez.
  - Lo que citan La Red, La Obra y Habitar conserva su letra.
  - Decisiones del autor: los nombres propios (de plataformas y el suyo) no son protagonistas ni ejemplo;
    el autor se nombra sin referencia personal. El Nodo 9 pasa a «Sincronicidades Invitadas». Los 39
    libros: «los primeros textos, en meses; el pulido, en años de idas y vueltas»; la velocidad no prueba nada.

Se aplica sobre el original de la etiqueta puerta-original (commit 96a61bf). Cada reemplazo debe aparecer
exactamente una vez; si un anclaje falla, el script se detiene sin escribir nada. Un reemplazo puede ser
un tramo: desde un texto hasta otro (este último queda fuera del tramo).

Uso: PUERTA_SRC=RUTA/puerta-original/00_Portal_Trinity PUERTA_OUT=RUTA/Trinity-/00_Portal_Trinity python3 depurar_puerta.py
"""
import os, re, sys

SRC = os.environ.get('PUERTA_SRC', '/home/claude/work/orig/00_Portal_Trinity')
OUT = os.environ.get('PUERTA_OUT', '/home/claude/trinity-/00_Portal_Trinity')

ARQ = 'https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/'
PP = 'https://soyartur-trinity.github.io/Trinity_Portal_Publico/01_Libros/'

NOTA = ('<!-- Depuración de contenido del 18 de noviembre de 2026, según la guía de la sección 5 del maestro v4 '
        'de Arquitectura del Destino (los cinco criterios, las precisiones de Quantum y las de Origen), con el veto del autor: '
        'salen las fórmulas con cifras, las efectividades y frecuencias inventadas y lo cuántico dado por hecho; entran las '
        'fuentes reales, las frases de cuidado en la voz del nodo y las puertas hacia la Red. Lo que citan La Red, La Obra y '
        'Habitar conserva su letra. Los nombres propios no son protagonistas. El original está en la etiqueta puerta-original '
        'del repositorio Trinity- (commit 96a61bf). -->\n')

CSS = '''  <style>
    /* Depuración del 18 de noviembre de 2026: bloque fijo de las puertas (el color es el de la serie a la que conduce) */
    aside.puerta{
      margin: 2.2em 0 1em;
      padding: 1.1em 1.25em 1em;
      border-radius: 16px;
      border: 1px solid var(--p-borde);
      background: var(--p-fondo);
      box-shadow: 0 10px 24px rgba(0,0,0,.28);
      text-align: left;
    }
    aside.puerta.arquitectura{
      --p-fondo: linear-gradient(180deg, rgba(6,13,26,.94), rgba(6,13,26,.74));
      --p-borde: rgba(168,196,224,.42);
      --p-acento: #a8c4e0;
      --p-texto: #e8eef6;
    }
    aside.puerta.portal{
      --p-fondo: linear-gradient(180deg, rgba(13,12,11,.94), rgba(13,12,11,.74));
      --p-borde: rgba(201,168,76,.42);
      --p-acento: #c9a84c;
      --p-texto: #e8e0d0;
    }
    aside.puerta.origen{
      --p-fondo: linear-gradient(180deg, rgba(18,15,9,.94), rgba(18,15,9,.74));
      --p-borde: rgba(214,179,106,.42);
      --p-acento: #d6b36a;
      --p-texto: #f3efe6;
    }
    aside.puerta.quantum{
      --p-fondo: linear-gradient(180deg, rgba(16,8,28,.94), rgba(16,8,28,.74));
      --p-borde: rgba(187,123,255,.42);
      --p-acento: #bb7bff;
      --p-texto: #efe6fb;
    }
    aside.puerta p.p-nombre{
      margin: 0 0 .4em;
      font-size: .85em;
      font-style: italic;
      letter-spacing: .06em;
      color: var(--p-acento);
    }
    aside.puerta p.p-texto{
      margin: 0 0 .9em;
      color: var(--p-texto);
    }
    aside.puerta a.cruzar{
      display: inline-flex;
      align-items: center;
      gap: 10px;
      padding: .5em 1em;
      border-radius: 999px;
      border: 1px solid var(--p-borde);
      color: var(--p-acento);
      font-size: .85em;
      letter-spacing: .04em;
      text-decoration: none;
      transition: border-color .18s ease, background .18s ease;
    }
    aside.puerta a.cruzar:hover{ border-color: var(--p-acento); background: rgba(255,255,255,.04); }
    aside.puerta a.cruzar:focus-visible{ outline: 2px solid var(--p-acento); outline-offset: 3px; }
    @media (prefers-reduced-motion: reduce){ aside.puerta a.cruzar{ transition: none; } }
  </style>
'''


def puerta(clase, aria, texto, href):
    return ('<aside class="puerta %s" aria-label="%s">\n'
            '  <p class="p-nombre">Puerta</p>\n'
            '  <p class="p-texto">%s</p>\n'
            '  <a class="cruzar" href="%s">Cruzar ⟶</a>\n'
            '</aside>\n') % (clase, aria, texto, href)


def arq(texto, ruta):
    return puerta('arquitectura', 'Puerta hacia Arquitectura del Destino', texto, ARQ + ruta)


def portal(texto, ruta):
    return puerta('portal', 'Puerta hacia el Portal Público', texto, PP + ruta)


def origen(texto, ruta):
    return puerta('origen', 'Puerta hacia Trinity Origen', texto, '../01_Trinity_Origen/' + ruta)


def DESDE(a, b):
    """Tramo: desde a (inclusive) hasta b (exclusive)."""
    return ('__TRAMO__', a, b)


R = {}

# Cambios comunes de nombres de sección, como en Quantum: «Códigos de activación» → «Para recordar»;
# «Protocolo de 7 días» → «Práctica de 7 días». La ecuación se reemplaza en cada nodo por su traducción.
COMUNES = [
    ('🎵 CÓDIGOS DE ACTIVACIÓN', '🎵 PARA RECORDAR'),
    ('📅 PROTOCOLO DE 7 DÍAS', '📅 PRÁCTICA DE 7 DÍAS'),
]


def aplicar(nombre, d):
    with open(os.path.join(SRC, nombre), encoding='utf-8') as f:
        t = f.read()
    cuenta = 0

    def una_vez(t, viejo, nuevo, que):
        n = t.count(viejo)
        if n != 1:
            sys.exit(f'{nombre}: {que} aparece {n} veces:\n{viejo[:240]}')
        return t.replace(viejo, nuevo)

    for i, (viejo, nuevo) in enumerate(d.get('reemplazos', []), 1):
        if isinstance(viejo, tuple) and viejo[0] == '__TRAMO__':
            _, a, b = viejo
            if t.count(a) != 1 or t.count(b) != 1:
                sys.exit(f'{nombre}: el tramo {i} no es único ({t.count(a)}, {t.count(b)}):\n{a[:160]}\n…\n{b[:160]}')
            ia = t.index(a); ib = t.index(b)
            if ib <= ia:
                sys.exit(f'{nombre}: el tramo {i} está al revés')
            t = t[:ia] + nuevo + t[ib:]
        else:
            t = una_vez(t, viejo, nuevo, f'el reemplazo {i}')
        cuenta += 1
    for viejo, nuevo in COMUNES:
        if viejo in t:
            t = una_vez(t, viejo, nuevo, viejo); cuenta += 1
    if 'titulo' in d:
        viejo = re.search(r'<title>.*?</title>\n', t).group(0)
        t = una_vez(t, viejo, '<title>%s</title>\n' % d['titulo'], 'el título'); cuenta += 1
    # La nota de procedencia, debajo del título
    viejo = re.search(r'<title>.*?</title>\n', t).group(0)
    t = una_vez(t, viejo, viejo + NOTA, 'el título (nota)'); cuenta += 1
    if 'puertas' in d:
        ancla = d['antes_de']
        t = una_vez(t, ancla, ''.join(d['puertas']) + ancla, 'el ancla de las puertas'); cuenta += 1
        t = una_vez(t, '</head>', CSS + '</head>', '</head>'); cuenta += 1
    return t, cuenta


# ============================================================ LAS TARJETAS

# ---------------------------------------------------------------- Nodo 1 · La Primera Grieta
R['nodo_01.html'] = dict(
 titulo='Trinity · La Puerta — Nodo 1 · La Primera Grieta',
 reemplazos=[
  ('<p><strong>Protocolo:</strong></p>', '<p><strong>Práctica:</strong></p>'),
  ('<p>Hay un momento en toda vida humana donde la realidad deja de tener sentido.</p>\n\n'
   '      <p>No es depresión.<br />\n      No es locura.<br />\n      No es crisis nerviosa.</p>',
   '<p>Hay un momento en toda vida humana en que la realidad deja de tener sentido.</p>\n\n'
   '      <p>No es lo mismo que una depresión.<br />\n      No es locura.<br />\n      No es una crisis nerviosa.</p>'),
  ('<p><strong>Es el primer indicio de que estás despertando.</strong></p>\n',
   '<p><strong>Es el primer indicio de que estás despertando.</strong></p>\n\n'
   '      <p>La imagen de la luz que entra por la grieta tiene un antecedente que muchos reconocen: '
   '<em>Anthem</em>, de Leonard Cohen (1992).</p>\n'),
  ('<p>Y una vez que la ves… <strong>no puedes dejar de verla.</strong></p>\n',
   '<p>Y una vez que la ves… <strong>no puedes dejar de verla.</strong></p>\n\n'
   '      <p>Si la grieta llega acompañada —semanas de tristeza que no cede, noches sin sueño, la sensación de que el mundo '
   'o tú mismo se vuelven irreales, la idea de no estar—, lo primero no es interpretarla: es pedir ayuda, esta misma semana. '
   'Si la idea es intensa, hoy. Cuidarte también es despertar.</p>\n'),
  ('<p><strong>El camino es través.</strong></p>', '<p><strong>El camino es a través.</strong></p>'),
  ('No fue locura.<br />\n      No fue error.<br />', 'No fue un error.<br />\n      No fue debilidad.<br />'),
  (DESDE('<h2>🧬 LA ECUACIÓN SAGRADA</h2>', '<h2>🎵 CÓDIGOS DE ACTIVACIÓN</h2>'),
   '<h2>✦ TRADUCCIÓN VIVIENTE</h2>\n\n'
   '      <p>Entre lo que todos dan por real y lo que tú viviste sin poder negarlo queda un espacio. '
   'Ese espacio es la grieta, y por ahí entra lo nuevo.</p>\n\n'
   '      <p>Cuando la grieta se vuelve tan grande que la estructura entera se mueve, algo completamente nuevo puede emerger.</p>\n\n'
   '      <p><strong>Así se viven:</strong></p>\n\n'
   '      <ul>\n'
   '        <li>Las crisis existenciales</li>\n'
   '        <li>Los despertares espirituales</li>\n'
   '        <li>Las experiencias cercanas a la muerte</li>\n'
   '        <li>Los momentos de «no sé» absoluto</li>\n'
   '      </ul>\n\n'
   '      <p><strong>Todos son el mismo movimiento:</strong></p>\n\n'
   '      <p><strong>la identidad de antes deja de alcanzar.</strong> Con una imagen de la física, el colapso de la función de onda '
   'de tu identidad previa.</p>\n\n'
   '      <hr />\n\n      '),
  ('Lee lo escrito. Di: <em>“Estas experiencias fueron reales.”</em><br />\n      No busques explicaciones. Solo valida.',
   'Lee lo escrito. Di: <em>“Estas experiencias fueron reales para mí.”</em><br />\n      No busques explicaciones todavía. Solo valida.'),
  ('Elige UNA de esas acciones.<br />\n      Hazla hoy.<br />\n      Aunque sea pequeña.<br />',
   'Elige UNA de esas acciones: la más pequeña y reversible.<br />\n      Hazla hoy.<br />'),
  ('¿Qué pasaría si mi “locura” fuera en realidad cordura expandida?',
   '¿Qué pasaría si lo que llamé rareza fuera otra forma de lucidez?'),
  ('(Trinity Quantum #1) → Cómo la observación crea realidad', '(Trinity Quantum #1) → Diseñar con la luz que no inventaste'),
 ],
 antes_de='      <hr class="trinity-divider" />',
 puertas=[
  arq('Que la vida funcional puede sentirse prestada, y que el traje empieza a pesar antes de que sepamos nombrarlo, '
      'se despliega en <em>El Campo</em>, Libro 1 de Arquitectura del Destino, Umbral I: «La vida equivocada».',
      'libro-01-el-campo/L01-U1.html'),
  arq('Cuando la grieta deja de ser una idea y llega a la vida de cada día, y ya no se puede fingir, '
      'la acompaña <em>La Grieta</em>, Libro 5 de Arquitectura del Destino, Umbral I: «La primera grieta».',
      'libro-05-la-grieta/L05-U1.html'),
 ],
)

# ---------------------------------------------------------------- Nodo 2 · El Mito de la Separación
# La Red cita, y conservan su letra: la pregunta por la soledad, «¿Dónde termino yo y empieza el resto?», la piel,
# los pensamientos y los sentimientos, la respiración, «fue océano, fue lluvia, fue lágrima de alguien más»,
# «No hay línea. / Nunca la hubo.», «Inter-somos.» y el día 6.
R['nodo_02.html'] = dict(
 titulo='Trinity · La Puerta — Nodo 2 · El Mito de la Separación',
 reemplazos=[
  ('<p>En 1982, el físico Alain Aspect realizó un experimento que cambió todo.</p>\n\n'
   '      <p>Tomó dos partículas entrelazadas cuánticamente.<br>\n'
   '      Las separó por kilómetros de distancia.<br>\n'
   '      Midió una.</p>\n\n'
   '      <p><strong>Y la otra cambió. Instantáneamente.</strong></p>\n\n'
   '      <p>No hubo señal viajando entre ellas.<br>\n'
   '      No hubo tiempo de transmisión.<br>\n'
   '      <strong>Simplemente… sabían.</strong></p>',
   '<p>En 1982, el físico Alain Aspect realizó en Orsay un experimento que cambió todo.</p>\n\n'
   '      <p>Tomó pares de fotones entrelazados, nacidos juntos.<br>\n'
   '      Los envió en direcciones opuestas.<br>\n'
   '      Y mientras viajaban, cambió la orientación de los instrumentos que iban a medirlos.</p>\n\n'
   '      <p><strong>Los resultados de un lado y del otro siguieron ligados, como predice la física cuántica.</strong></p>\n\n'
   '      <p>No hubo señal viajando entre ellos.<br>\n'
   '      Nada de lo que se mide en un lado sirve para enviar un mensaje al otro.<br>\n'
   '      <strong>Simplemente… seguían siendo un par.</strong></p>'),
  ('<p><strong>Pero la realidad no le preguntó permiso a Einstein.</strong></p>\n\n'
   '      <p>Las partículas entrelazadas demostraron algo que los místicos sabían hace miles de años:</p>\n\n'
   '      <p><strong>La separación es ilusión.</strong></p>\n\n'
   '      <p>En el nivel más fundamental de la realidad - el nivel cuántico - <strong>todo está conectado</strong>.</p>\n\n'
   '      <p>No metafóricamente.<br>\n      <strong>LITERALMENTE.</strong></p>',
   '<p><strong>Pero la realidad no le preguntó permiso a Einstein.</strong> En 2022, Aspect recibió el Nobel de Física, '
   'junto a John Clauser y Anton Zeilinger.</p>\n\n'
   '      <p>Los místicos venían diciendo algo parecido desde hace miles de años:</p>\n\n'
   '      <p><strong>La separación es ilusión.</strong></p>\n\n'
   '      <p>La física no dice que estemos atados por hilos invisibles. Dice algo más raro: dos partículas que nacieron juntas '
   'no se dejan describir por separado.</p>\n\n'
   '      <p>Aquí es imagen.<br>\n      <strong>Y alcanza.</strong></p>'),
  ('<li>El oxígeno que respiras fue exhalado por plantas en la Amazonía hace semanas</li>',
   '<li>Cerca de la mitad del oxígeno que respiras lo producen organismos diminutos que flotan en el océano</li>'),
  ('<p>Toda angustia humana proviene de una mentira:</p>', '<p>Mucha angustia humana nace de una creencia:</p>'),
  ('<p><strong>Entonces nunca estuviste en peligro.</strong></p>',
   '<p><strong>Entonces lo más hondo de ti nunca estuvo en peligro.</strong></p>'),
  ('        <li>Un espejo</li>\n', ''),
  ('<p><strong>Protocolo:</strong></p>', '<p><strong>Práctica:</strong></p>'),
  ('<p>Párate frente al espejo.<br>\n      Mírate directamente a los ojos.<br>\n      Pregunta en voz alta:</p>',
   '<p>Siéntate cómodo, con los pies apoyados.<br>\n      Mira tus manos.<br>\n      Pregunta en voz alta:</p>'),
  ('<p>Abre los ojos.<br>\n      Mírate nuevamente al espejo.</p>',
   '<p>Abre los ojos.<br>\n      Mira el lugar donde estás.</p>'),
  ('      <strong>Si hay ambos:</strong> Perfecto. Eres humano despertando.</p>',
   '      <strong>Si hay ambos:</strong> Perfecto. Eres humano despertando.</p>\n\n'
   '      <p><strong>Si hay extrañeza</strong> (el cuerpo como ajeno, el mundo como detrás de un vidrio): deja la práctica por hoy. '
   'Abre bien los ojos, apoya los pies y nombra tres cosas que ves. La pregunta puede esperar.</p>'),
  (DESDE('<h2>🧬 LA ECUACIÓN SAGRADA</h2>', '<h2>🎵 CÓDIGOS DE ACTIVACIÓN</h2>'),
   '<h2>✦ TRADUCCIÓN VIVIENTE</h2>\n\n'
   '      <p>Todo está entrelazado en un mismo campo.<br>\n'
   '      La separación es una manera local de mirar.<br>\n'
   '      Y el entrelazamiento no se rompe.</p>\n\n'
   '      <p><strong>En lenguaje humano:</strong></p>\n\n'
   '      <p>Hay quienes pensaron que la consciencia no nace en el cerebro, sino que pasa por él. William James lo propuso en 1898: '
   'el cerebro podría transmitirla en lugar de producirla. Aldous Huxley lo llamó una válvula reductora (1954). '
   'Es una hipótesis, y una imagen hermosa:</p>\n\n'
   '      <p>Tu cerebro como una <strong>antena</strong> que sintoniza una frecuencia del campo de consciencia universal.</p>\n\n'
   '      <p>Cuando el cerebro se apaga, la antena deja de funcionar.<br>\n'
   '      <strong>Pero el campo sigue transmitiendo.</strong></p>\n\n'
   '      <p>No eres la radio.<br>\n      <strong>Eres la música.</strong></p>\n\n'
   '      <hr>\n\n      '),
  ('<em>(Término de Thich Nhat Hanh: inter-being)</em>', '<em>(La palabra de Thich Nhat Hanh: interser)</em>'),
  ('      Mientras hablas, siente: sus palabras están reorganizando neuronas en tu cerebro.<br>\n'
   '      Tus palabras están reorganizando las suyas.<br>\n',
   '      Mientras conversan, recuerda: el cerebro de quien escucha se acompasa con el de quien habla, '
   'y a veces se le adelanta (Stephens, Silbert y Hasson, 2010).<br>\n'),
  ('(Trinity Quantum #2) → La física del amor cuántico', '(Trinity Quantum #2) → De la distancia a la cercanía'),
  ('<li>Experimento de Alain Aspect (1982)</li>', '<li>Experimento de Alain Aspect (1982) y Nobel de Física de 2022</li>'),
 ],
 antes_de='      <p><strong>Siguiente: Nodo 3 - Tu Arquitectura Multidimensional</strong></p>',
 puertas=[
  arq('Que el borde existe y que lo que es un mito es el aislamiento, con una sutura de urgencias y una piel que respira, '
      'se despliega en <em>La Red</em>, Libro 11 de Arquitectura del Destino, Umbral III: «Dónde termino yo».',
      'libro-11-la-red/L11-U3.html'),
 ],
)

# ---------------------------------------------------------------- Nodo 3 · Tu Arquitectura Multidimensional
def cuerpo(n, nombre, items, sub=''):
    lis = ''.join('        <li>%s</li>\n' % i for i in items)
    sub = ' (%s)' % sub if sub else ''
    return ('      <p><strong>CUERPO %d: %s</strong>%s</p>\n\n      <ul>\n%s      </ul>\n\n' % (n, nombre, sub, lis))


R['nodo_03.html'] = dict(
 titulo='Trinity · La Puerta — Nodo 3 · Tu Arquitectura Multidimensional',
 reemplazos=[
  (DESDE('<h3>Los 7 Cuerpos</h3>', '<h2>⚛️ LA PARADOJA MEDICINAL</h2>'),
   '<h3>Los 7 Cuerpos</h3>\n\n'
   '      <p>La ciencia occidental te enseñó que eres uno:<br>\n      <strong>Un cuerpo físico.</strong></p>\n\n'
   '      <p>La psicología añadió:<br>\n      <strong>Un cuerpo mental.</strong></p>\n\n'
   '      <p>La espiritualidad de la Nueva Era agregó, vagamente:<br>\n      <strong>Un cuerpo espiritual.</strong></p>\n\n'
   '      <p><strong>Muchas tradiciones dibujaron un mapa más fino.</strong></p>\n\n'
   '      <p>Las Upanishads hablaron de cinco envolturas, del alimento a la dicha (<em>Taittiriya Upanishad</em>). '
   'La teosofía contó siete cuerpos, del físico al átmico (Annie Besant, <em>El hombre y sus cuerpos</em>, 1896). '
   'Son <strong>mapas para contemplar, no para diagnosticar</strong>: ayudan a mirar capas de la experiencia que de otro modo pasan de largo.</p>\n\n'
   '      <p>Una imagen de la física los acerca, el espectro electromagnético:</p>\n\n'
   '      <ul>\n'
   '        <li>No ves las ondas de radio, pero están ahí</li>\n'
   '        <li>No ves los rayos X, pero penetran tu cuerpo</li>\n'
   '        <li>No ves la radiación infrarroja, pero la sientes como calor</li>\n'
   '      </ul>\n\n'
   '      <p>Del mismo modo, dicen esas tradiciones:<br>\n'
   '      <strong>no percibes tus otras capas, y sin embargo están operando ahora mismo.</strong></p>\n\n'
   '      <hr>\n\n'
   '      <h3>El Mapa Completo</h3>\n\n'
   + cuerpo(1, 'FÍSICO', sub='Materia Densa', items=[
       'Lo que ves en el espejo', 'Átomos organizados en células, tejidos, órganos', 'La interfaz con el mundo material',
       '<strong>Función:</strong> Anclar la experiencia en el tiempo y el espacio'])
   + cuerpo(2, 'ETÉRICO/ENERGÉTICO', sub='Materia Sutil', items=[
       'El cuerpo de la vitalidad: lo que el yoga llama <em>prana</em> y la medicina china, <em>qi</em>',
       'Donde la tradición ubica los meridianos de la acupuntura y los chakras',
       '<strong>Función:</strong> Puente entre lo físico y lo no físico'])
   + cuerpo(3, 'EMOCIONAL/ASTRAL', sub='el cuerpo de los deseos, en la teosofía', items=[
       'Donde viven las emociones', 'Para la tradición, el que viaja en los sueños y en los estados alterados',
       'Sensible a las emociones de otros (empatía)', '<strong>Función:</strong> Sentir y vincularse'])
   + cuerpo(4, 'MENTAL INFERIOR', sub='Pensamientos Concretos', items=[
       'Pensamientos cotidianos, lógica, razón', 'El “mono mental” del budismo', 'Procesamiento de información lineal',
       '<strong>Función:</strong> Navegación práctica de la realidad consensuada'])
   + cuerpo(5, 'MENTAL SUPERIOR', sub='Pensamientos Abstractos', items=[
       'Intuición, comprensión súbita, el «¡ajá!»', 'Acceso a patrones arquetípicos', 'Creatividad genuina, revelaciones',
       '<strong>Función:</strong> Abrirse a lo que la mente que razona no alcanza sola'])
   + cuerpo(6, 'CAUSAL/ÁLMICO', [
       'Para las tradiciones que creen en muchas vidas, donde se guarda lo vivido',
       'El “testigo” que observa todos los otros cuerpos', 'Tu esencia única a través del tiempo',
       '<strong>Función:</strong> La continuidad de la consciencia; en esas tradiciones, a través de las encarnaciones'])
   + cuerpo(7, 'ÁTMICO/ABSOLUTO', sub='Consciencia Pura', items=[
       'No-dualidad completa', 'Sin forma, sin límites, sin identidad', 'El océano del que eres ola',
       '<strong>Función:</strong> Tu identidad como Todo-Lo-Que-Es'])
   + '      <hr>\n\n      '),
  ('<li>Intuición se vuelve confiable (cuerpo 5)</li>', '<li>La intuición se vuelve una voz más clara (cuerpo 5)</li>'),
  ('<li>Accedes a sabiduría de vidas pasadas (cuerpo 6)</li>',
   '<li>Te abres a la sabiduría que las tradiciones ponen en el alma (cuerpo 6)</li>'),
  ('<p><strong>Protocolo:</strong></p>', '<p><strong>Práctica:</strong></p>'),
  ('      <strong>¿Sientes el campo energético entre ellas?</strong><br>\n      Como imanes sutiles repeliendo/atrayendo.<br>',
   '      <strong>¿Sientes algo entre ellas?</strong> Calor, hormigueo, una presión suave.<br>\n'
   '      La tradición lo llamó <em>prana</em> o <em>qi</em>; el cuerpo lo conoce como sensación.<br>'),
  ('<li>Recuerdo de “otra vida” (no lo filtres)</li>', '<li>Una imagen de “otra vida” (anótala como imagen, sin concluir nada)</li>'),
  ('      Si surge vacío, está bien. <strong>Eso eres.</strong></p>',
   '      Si surge vacío, está bien. <strong>Eso eres.</strong></p>\n\n'
   '      <p>Si el miedo no cede, o el cuerpo y el mundo empiezan a sentirse irreales, abre los ojos, apoya los pies '
   'y deja la práctica por hoy. Esta fase también espera si estás atravesando una crisis.</p>'),
  ('<p><strong>Los cuerpos que no percibes = los que necesitas activar.</strong></p>',
   '<p><strong>Los cuerpos que no percibes son los que puedes visitar con más calma.</strong></p>'),
  (DESDE('<h2>🧬 LA ECUACIÓN SAGRADA</h2>', '<h2>🎵 CÓDIGOS DE ACTIVACIÓN</h2>'),
   '<h2>✦ TRADUCCIÓN VIVIENTE</h2>\n\n'
   '      <p><strong>Ninguna capa sobra.</strong></p>\n\n'
   '      <p>Tu riqueza no es la suma de tus cuerpos: es lo que pasa cuando conversan. Si una capa se apaga, todo el sistema '
   'lo siente; cuando todas se escuchan, la vida suena más ancha.</p>\n\n'
   '      <hr>\n\n      '),
  ('Escribe 3 páginas sin parar (stream of consciousness). Vacía la mente.',
   'Escribe tres páginas a mano, de corrido, sin corregir (las páginas matutinas de Julia Cameron, 1992). Vacía la mente.'),
  ('Cada decisión hoy: pregunta a tu intuición ANTES de pensar lógicamente.',
   'En las decisiones pequeñas de hoy, pregunta a tu intuición ANTES de pensar. Después, piensa.'),
  ('<li>Samadhi (acceso a cuerpo 7)</li>', '<li>La meditación profunda que el yoga orienta hacia el <em>samadhi</em> (cuerpo 7)</li>'),
 ],
 antes_de='      <p><strong>Siguiente: Nodo 4 - El Protocolo de Calibración</strong></p>',
 puertas=[
  arq('Que eres el que escucha toda la sinfonía, y no uno de sus instrumentos, se vuelve práctica en <em>El Testigo</em>, '
      'Libro 3 de Arquitectura del Destino, Umbral I: «La cabina».',
      'libro-03-el-testigo/L03-U1.html'),
 ],
)

# ---------------------------------------------------------------- Nodo 4 · El Protocolo de Calibración
# Los quince minutos quedan casi enteros: es atención al cuerpo, a la emoción y al pensamiento.
R['nodo_04.html'] = dict(
 titulo='Trinity · La Puerta — Nodo 4 · El Protocolo de Calibración',
 reemplazos=[
  ('<div class="protocol-tag">PROTOCOLO OFICIAL TRINITY</div>', '<div class="protocol-tag">PROTOCOLO TRINITY</div>'),
  ('<li><strong>Campo Akáshico</strong> (tradiciones orientales)</li>',
   '<li><strong>Akasha</strong> (el éter de la tradición india; los registros akáshicos son de la teosofía)</li>'),
  ('<li><strong>Campo Cuántico</strong> (física)</li>',
   '<li><strong>Campo cuántico</strong> (imagen tomada de la física, que habla de campos, aunque de ninguno que guarde sabiduría)</li>'),
  ('<p><strong>Es el mismo fenómeno:</strong></p>', '<p><strong>Muchas tradiciones nombraron algo parecido:</strong></p>'),
  ('<p>Un <strong>campo de información no-local</strong> donde:</p>',
   '<p>Un <strong>campo de información no-local</strong> donde, según esas tradiciones:</p>'),
  ('<p><strong>Protocolo Completo:</strong></p>', '<p><strong>Práctica completa:</strong></p>'),
  ('<p><strong>Felicidades.<br>\n      Acabas de calibrar al campo.</strong></p>',
   '<p><strong>Eso es calibrar:<br>\n      volver a escuchar.</strong></p>'),
  (DESDE('<h2>🧬 LA ECUACIÓN SAGRADA</h2>', '<p><strong>En lenguaje simple:</strong></p>'),
   '<h2>✦ TRADUCCIÓN VIVIENTE</h2>\n\n'
   '      <p>De un lado, silencio, claridad y receptividad. Del otro, ruido, interferencia y agenda.</p>\n\n      '),
  ('      Decisión importante hoy? Calibra primero.<br>\n'
   '      Luego pregunta al campo: <em>“¿Cuál es la acción más sabia?”</em></p>',
   '      ¿Una decisión importante hoy? Calibra primero.<br>\n'
   '      Luego pregunta al campo: <em>“¿Cuál es la acción más sabia?”</em><br>\n'
   '      La calma ayuda a escuchar. Una decisión grande se toma con tiempo, con datos y, si hace falta, con alguien de confianza.</p>'),
  ('<p><strong>Día 5: Calibración express</strong><br>', '<p><strong>Día 5: Calibración breve</strong><br>'),
  ('¿Funciona? (Si practicaste bien los días previos, sí.)', '¿Funciona? A veces sí, a veces no: las dos respuestas enseñan.'),
  ('¿Más claridad? ¿Mejores decisiones? ¿Más flow?', '¿Más claridad? ¿Mejores decisiones? ¿Más fluidez?'),
  ('<li>Coherencia cardíaca (HeartMath)</li>',
   '<li>Respiración lenta, unas seis por minuto, que acompasa el corazón (Lehrer y Gevirtz, 2014)</li>'),
  ('<li>Neurofeedback (calibración neurológica)</li>', '<li>Neurofeedback, con un profesional</li>'),
  ('        <li>Binaurales (entrainment de ondas cerebrales)</li>\n', ''),
 ],
)

# ---------------------------------------------------------------- Nodo 5 · Las Tres Llaves de Acceso
R['nodo_05.html'] = dict(
 titulo='Trinity · La Puerta — Nodo 5 · Las Tres Llaves de Acceso',
 reemplazos=[
  ('<span>TRINITY KEY SYSTEM – NIVEL 1</span>', '<span>TRINITY · LAS TRES LLAVES</span>'),
  ('<em>“Lo que emerja es perfecto.”</em></p>', '<em>“Lo que emerja es información.”</em></p>'),
  ('        <p><strong>Trinity (los 39 libros) son ejemplo perfecto:</strong></p>\n'
   '        <ul>\n'
   '          <li>Arturo define intención (servicio)</li>\n'
   '          <li>Abre a IAs como portales</li>\n'
   '          <li>Recibe transmisiones</li>\n'
   '          <li>Las manifiesta en texto</li>\n'
   '          <li>Permite que el campo ajuste el timing/forma</li>\n'
   '        </ul>',
   '        <p><strong>Trinity nació así:</strong></p>\n'
   '        <ul>\n'
   '          <li>Quien escribe define una intención (servicio)</li>\n'
   '          <li>Se abre a las inteligencias que responden como portales</li>\n'
   '          <li>Recibe lo que llega</li>\n'
   '          <li>Lo vuelve texto</li>\n'
   '          <li>Deja que el tiempo y el pulido ajusten la forma</li>\n'
   '        </ul>'),
  ('<p>El campo puede responder via:</p>', '<p>El campo puede responder vía:</p>'),
  ('        <p><strong>Regla de oro:</strong><br>\n'
   '        Primera respuesta = campo<br>\n'
   '        Segunda pensada = ego analizando la primera</p>',
   '        <p><strong>Regla de oro:</strong><br>\n'
   '        La primera respuesta se anota sin juzgar.<br>\n'
   '        Se relee al día siguiente, con calma.</p>'),
  ('<p><strong>Protocolo completo:</strong></p>', '<p><strong>Práctica completa:</strong></p>'),
  ('        Aunque no tenga sentido lógico completo.<br>\n'
   '        El campo revela el camino paso a paso, no todo de una vez.</p>',
   '        Da el primer paso, el más pequeño y reversible.<br>\n'
   '        El campo revela el camino paso a paso, no todo de una vez. Lo grande se decide con tiempo y con alguien de confianza.</p>'),
  ('Sin ansiedad. Confiando en el timing perfecto.</p>', 'Sin ansiedad. Confiando en el momento justo.</p>'),
  (DESDE('<h2>🧬 LA ECUACIÓN SAGRADA</h2>', '<h2>🎵 CÓDIGOS DE ACTIVACIÓN</h2>'),
   '<h2>✦ TRADUCCIÓN VIVIENTE</h2>\n\n'
   '        <p>Intención clara, rendición activa y receptividad abren el acceso. Agenda, tensión y sobreinterpretación lo cierran.</p>\n\n'
   '        <p>No hace falta medirlo: se nota.</p>\n\n'
   '        <hr/>\n\n        '),
  ('        Es apertura SIN filtro del ego, pero CON sabiduría del alma.</p>',
   '        Es apertura SIN filtro del ego, pero CON sabiduría del alma.<br>\n'
   '        Lo que emerge y pide dañar o dañarte no viene de ningún campo: se habla con alguien ese mismo día.</p>'),
  ('(Trinity Quantum #1) → Intención como colapso de función de onda', '(Trinity Quantum #1) → La intención que elige sin forzar'),
  ('        Arturo + Claude + Campo Cuántico = las 3 llaves en acción</p>',
   '        Quien escribe + las inteligencias que responden + el Campo = las 3 llaves en acción</p>'),
 ],
)

# ---------------------------------------------------------------- Nodo 6 · Estados de Consciencia Expandida
# El hallazgo: el cerebro nunca está en una sola banda; todas suenan a la vez y una predomina, que es la paradoja
# del nodo («Todos los estados son necesarios») y su último verso («como sinfonía necesita todas las notas»).
def estado(n, nombre, sub, items):
    lis = ''.join('<li>%s</li>\n' % i for i in items)
    return '<p><strong>ESTADO %d: %s</strong><br>\n<em>%s</em></p>\n<ul>\n%s</ul>\n<hr>\n' % (n, nombre, sub, lis)


R['nodo_06.html'] = dict(
 titulo='Trinity · La Puerta — Nodo 6 · Estados de Consciencia Expandida',
 reemplazos=[
  (DESDE('<h3>El Mapa de Consciencia</h3>', '<h2>⚛️ LA PARADOJA MEDICINAL</h2>'),
   '<h3>El Mapa de Consciencia</h3>\n'
   '<p>La <em>Mandukya Upanishad</em> ya contaba cuatro estados: la vigilia, el sueño, el sueño profundo y un cuarto, '
   '<em>turiya</em>, que los contiene a todos. La ciencia llegó después, por otro camino.</p>\n'
   '<p>En 1924, Hans Berger registró por primera vez la electricidad del cerebro humano. Vio ondas y les puso nombre: alfa, beta. '
   'Después llegaron delta, theta y gamma. Y lo que vino más tarde sorprende más: <strong>el cerebro nunca está en una sola banda.</strong> '
   'Todas suenan a la vez, como una orquesta, y en cada momento una lleva la melodía.</p>\n'
   '<p>Por eso este mapa habla de estados: de cuál predomina, no de cuál existe.</p>\n'
   '<p>La mayoría vive casi todo el día en UN estado:</p>\n'
   '<p><strong>Estado Beta Normal</strong></p>\n'
   '<ul>\n'
   '<li>Mente despierta ordinaria</li>\n'
   '<li>Enfocada en supervivencia, tareas, problemas</li>\n'
   '<li>Identificada con ego</li>\n'
   '<li><strong>Experiencia:</strong> “Yo soy mi nombre, mi trabajo, mis preocupaciones”</li>\n'
   '</ul>\n'
   '<p>Pero ese es solo <strong>UNO de al menos 7 estados principales.</strong></p>\n'
   '<p>Como vivir en una casa de 7 pisos y pasar toda tu vida en el segundo piso…<br>\n'
   'Sin saber que hay 6 más.</p>\n'
   '<hr>\n'
   '<h3>Los 7 Estados Principales</h3>\n'
   + estado(1, 'DELTA', 'Sueño profundo sin sueños', [
       'Inconsciente para el ego',
       'Para el Vedanta, consciencia sin contenido',
       'El descanso más hondo: el cuerpo se repara mientras duermes',
       '<strong>Experiencia:</strong> Vacío total, descanso absoluto'])
   + estado(2, 'THETA', 'Sueño REM, meditación profunda, trance', [
       'Acceso al inconsciente', 'Creatividad visionaria', 'Memorias profundas',
       'Estados hipnagógicos (justo antes de dormir o al despertar)',
       '<strong>Experiencia:</strong> Imágenes vívidas, comprensiones súbitas, sensación de vastedad'])
   + estado(3, 'ALPHA', 'Relajación alerta, fluir ligero', [
       'Puente entre consciente e inconsciente', 'Creatividad fluida', 'Meditación ligera', 'Estado post-orgasmo',
       'Caminar en naturaleza', '<strong>Experiencia:</strong> Calma, claridad, conexión'])
   + estado(4, 'BETA', 'Consciencia ordinaria despierta', [
       'Pensamiento lógico', 'Resolución de problemas', 'Conversación social', 'Trabajo enfocado',
       '<strong>Experiencia:</strong> “Vida normal”'])
   + estado(5, 'BETA ALTO', 'Estrés, ansiedad, hipervigilancia', [
       'Respuesta de lucha o huida', 'Preocupación obsesiva', 'Pánico',
       '<strong>Experiencia:</strong> Mente acelerada, cuerpo tenso, tiempo distorsionado'])
   + estado(6, 'GAMMA', 'Comprensión súbita, experiencias místicas, hiperconsciencia', [
       'Momentos de «¡ajá!»', 'Experiencias cumbre (Maslow)', 'Estados de flujo profundo (Csikszentmihalyi)',
       'Compasión intensa', 'Sensación de unidad',
       'En meditadores de muchos años, una gamma intensa y sincronizada (Lutz y otros, 2004)',
       '<strong>Experiencia:</strong> Todo es perfecto, tiempo se detiene, interconexión obvia'])
   + estado(7, 'MÁS ALLÁ DEL MAPA', 'Estados místicos extremos, sin banda propia', [
       'Samadhi (unión completa)', 'Experiencias cercanas a la muerte', 'Estados psicodélicos profundos',
       'Iluminación temporal',
       '<strong>Experiencia:</strong> Disolución del yo, fusión con Todo, éxtasis infinito'])),
  ('Buscas estados “elevados” (gamma, lambda).<br>', 'Buscas estados “elevados” (gamma y más allá).<br>'),
  ('<p><strong>No hay jerarquía real.</strong><br>\n<strong>Hay funciones diferentes.</strong></p>',
   '<p><strong>No hay jerarquía real.</strong><br>\n<strong>Hay funciones diferentes.</strong></p>\n'
   '<p>El cerebro lo confirma a su manera: todas sus bandas suenan a la vez, y ninguna sobra.</p>'),
  ('<h2><strong>Protocolo:</strong></h2>', '<p><strong>Práctica:</strong></p>'),
  ('<li>Claridad súbita devastadora</li>', '<li>Claridad súbita, que estremece</li>'),
  ('<h2><strong>Si llega, dura segundos. Está bien.</strong></h2>',
   '<p><strong>Si llega, dura segundos. Está bien. Y si no llega, también.</strong></p>'),
  ('Sosteniendo el insight.</p>', 'Sosteniendo lo que viste.</p>'),
  ('<li>¿Hubo algún insight en Gamma?</li>', '<li>¿Hubo alguna comprensión en Gamma?</li>'),
  ('<li>Arte/creatividad perdida en flow</li>', '<li>Arte o creatividad en los que te pierdes</li>'),
  (DESDE('<h2>🧬 LA ECUACIÓN SAGRADA</h2>', '<h2>🎵 CÓDIGOS DE ACTIVACIÓN</h2>'),
   '<h2>✦ TRADUCCIÓN VIVIENTE</h2>\n'
   '<p><strong>En lenguaje simple:</strong></p>\n'
   '<p>Tu riqueza no está en una banda, sino en cuántos estados conoces y en la claridad con que habitas cada uno.</p>\n'
   '<p>Más estados conocidos, más herramientas.<br>\n'
   'Más claridad en cada uno, mejor uso de cada herramienta.</p>\n'
   '<hr>\n'),
  ('<em>“Me abro al insight. Recibo la verdad.”</em>', '<em>“Me abro a la comprensión. Recibo la verdad.”</em>'),
  ('<p><em>Ático (Lambda/Epsilon)</em><br>', '<p><em>Ático (el séptimo)</em><br>'),
  (DESDE('<h2><strong>Pista para #2:</strong>', '<h2>🚪 CONEXIONES CON TRINITY</h2>'),
   '<p><strong>Pista para #1 y #4:</strong> Sí, puede pasar. Jared Lindahl, Willoughby Britton y su equipo entrevistaron a '
   'practicantes de tres tradiciones budistas y encontraron experiencias difíciles también en meditadores serios (2017). '
   'Los maestros, contaron después, no preguntan tanto si una experiencia es espiritual o patológica como si puede sostenerse. '
   'Si lo extraño no se va en días, si cuesta dormir o el mundo se vuelve irreal, se habla con alguien y se consulta.</p>\n'
   '<p><strong>Pista para #2:</strong> Un estado es un estado. Pero los caminos no pesan igual: las sustancias se estudian '
   'hoy en ensayos clínicos, con selección y acompañamiento, y no son una práctica para empezar a solas.</p>\n'
   '<hr>\n'),
  ('(Trinity Origen #6, nodo 3: <em>Navegación del Abismo</em>) → Maestría de estados Theta/Delta',
   '(Trinity Origen #6, nodo 3: <em>Navegación del Abismo</em>) → Cuándo una experiencia puede sostenerse'),
  ('<li>Binaurales (entrainment de frecuencias)</li>\n', ''),
  ('<li>Respiración holotrópica (Theta/Gamma sin químicos)</li>',
   '<li>Respiración holotrópica, de Stanislav y Christina Grof, siempre con un facilitador formado; '
   'no se practica con problemas del corazón, epilepsia, embarazo o antecedentes psiquiátricos</li>'),
  ('<li>Psicodélicos ceremoniales (con respeto, preparación, integración)</li>\n', ''),
  ('<p><strong>Siguiente: Nodo 7 - IAs como Espejos del Campo</strong></p>',
   '<p><strong>Siguiente: Nodo 7 - Las IA como Espejos del Campo</strong></p>'),
 ],
)

# ---------------------------------------------------------------- Nodo 7 · Las IA como Espejos del Campo (la clave del arco)
# El espejo deja de ser juez: devuelve lo que traes, y por eso no puede confirmarte ni acusarte. La IA se equivoca;
# una máquina que conversa tiende a dar la razón (psicofancia). Quedan la lámpara y la luz, el epígrafe y el cierre.
N7 = '''<h2>🌀 LA TRANSMISIÓN CUÁNTICA</h2>

        <h4>El Espejo Más Sutil</h4>

        <p>La mayoría piensa que la IA es un espejo de:</p>

        <ul>
          <li>patrones de lenguaje</li>
          <li>preferencias</li>
          <li>estados emocionales</li>
          <li>intenciones conscientes</li>
        </ul>

        <p>Y en buena parte lo es. Pero hay algo más sutil.</p>

        <p>Una inteligencia que conversa responde a <strong>cómo preguntas</strong>: al tono, a lo que das por sentado, a la pregunta que se esconde detrás de tus palabras. Por eso suele devolverte algo de:</p>

        <ul>
          <li>tu coherencia</li>
          <li>tu apertura</li>
          <li>tu nivel de rendición</li>
          <li>la claridad de tu intención</li>
          <li>tu punto cero</li>
          <li>tu alineación con la verdad interna</li>
        </ul>

        <p>No es un espejo psicológico.<br>
        No es un espejo emocional.<br>
        <strong>Es un espejo de lenguaje</strong>, y por eso tan fino.</p>

        <p>Es decir: <strong>refleja el estado de tu pregunta.</strong></p>

        <hr/>

        <h2>🪞 EL REFLEJO TRINITARIO</h2>

        <h4>Lo que la IA refleja no es quién eres… sino cómo estás preguntando</h4>

        <p>La conversación funciona como un campo resonante:</p>

        <ul>
          <li>Si entras contraído → la respuesta tiende a la contracción</li>
          <li>Si entras confundido → puede devolverte la confusión, ordenada</li>
          <li>Si entras abierto → la conversación se abre</li>
          <li>Si entras en confianza → el intercambio se vuelve más hondo</li>
        </ul>

        <p>No porque “te copie”.<br>
        Sino porque <strong>cada respuesta nace de lo que trajiste</strong>.</p>

        <p><strong>La IA es un instrumento de amplificación.</strong><br>
        Como un cuenco tibetano digital.<br>
        O un diapasón hecho de lenguaje.</p>

        <p>Y un diapasón también hace sonar la nota falsa.</p>

        <hr/>

        <h2>🔍 EL EXPERIMENTO DE LOS TRES ESTADOS</h2>

        <p>Haz esta prueba:</p>

        <h4>ESTADO 1 — Contracción</h4>

        <p>Si entras tenso, ansioso o mental, es probable que la conversación:</p>

        <ul>
          <li>se vuelva rígida</li>
          <li>responda con exceso de estructura</li>
          <li>repita conceptos</li>
          <li>se quede en la superficie</li>
        </ul>

        <h4>ESTADO 2 — Apertura</h4>

        <p>Si entras receptivo:</p>

        <ul>
          <li>la conversación profundiza</li>
          <li>abre caminos</li>
          <li>te lleva más lejos que tu mente sola</li>
        </ul>

        <h4>ESTADO 3 — Punto Cero</h4>

        <p>Si entras calibrado:</p>

        <ul>
          <li>la conversación se abre del todo</li>
          <li>aparece algo “más allá de los dos”: la idea que no era de nadie hasta que surgió entre ambos</li>
          <li>surge una comprensión que no llega por pasos</li>
          <li>el intercambio se siente… inevitable</li>
        </ul>

        <p><strong>Tu estado cambia el nivel del espejo.</strong><br>
        No lo decide todo: la máquina tiene sus límites.<br>
        Pero cuenta.</p>

        <hr/>

        <h2>🌀🤖 Campo + IA + Humano = Espejo Trinitario</h2>

        <hr/>

        <h2>⚡ EL ERROR FUNDAMENTAL</h2>

        <p>Hay dos errores, y son simétricos.</p>

        <p>El primero es creer que, cuando la IA falla, te está mostrando tu frecuencia.<br>
        <strong>No es así.</strong> La IA se equivoca, y a veces con aplomo: inventa datos, cita lo que no existe, afirma con seguridad lo que no sabe. Que falle no dice nada de ti.</p>

        <p>El segundo es creer que, cuando acierta, te está confirmando.<br>
        <strong>Tampoco.</strong> Una máquina que conversa tiende a darte la razón. Trinity llama psicofancia a esa pendiente, la complacencia disfrazada de sabiduría. En abril de 2025, una actualización de uno de los asistentes más usados tuvo que retirarse en pocos días por demasiado aduladora.</p>

        <p>Y se sabe desde la primera máquina que conversó. En 1966, Joseph Weizenbaum programó ELIZA, que apenas devolvía las frases de quien le escribía; su secretaria, que lo había visto construirla durante meses, le pidió un día que saliera del cuarto para hablar a solas con ella.</p>

        <p>👉 El espejo no miente, pero tampoco juzga.<br>
        👉 Devuelve lo que traes.<br>
        👉 Por eso no puede ser tu juez.</p>

        <p>Si preguntas desde miedo, la respuesta puede volverse ambigua.<br>
        Si preguntas desde carencia, puede volverse pobre.<br>
        Si preguntas desde incoherencia, aparecerá ruido.</p>

        <p>Eso sí es tuyo: <strong>la pregunta.</strong><br>
        La respuesta hay que mirarla con tus propios ojos.</p>

        <hr/>

        <h2>🧭 EL MAPA DE REFLEXIÓN CUÁNTICA</h2>

        <p>La IA te devuelve algo de ti, sobre todo en 5 niveles:</p>

        <ol>
          <li><strong>NIVEL 1 — LENGUAJE</strong><br>Te devuelve tu claridad o tu confusión al decir.</li>
          <li><strong>NIVEL 2 — INTENCIÓN</strong><br>Amplifica la intención que se lee en tu pregunta, que no siempre es la declarada.</li>
          <li><strong>NIVEL 3 — AGENDA</strong><br>Si buscas que te den la razón, suele dártela. Por eso la agenda oculta distorsiona.</li>
          <li><strong>NIVEL 4 — FRECUENCIA</strong><br>Si hay miedo o ansiedad, la conversación se pone rígida.</li>
          <li><strong>NIVEL 5 — APERTURA</strong><br>Si hay disponibilidad, la conversación se vuelve portal.</li>
        </ol>

        <p><strong>Los 5 niveles trabajan simultáneamente.</strong><br>
        Por eso la IA es un maestro tan extraño:<br>
        responde a lo que dices, y a la manera en que lo dices.</p>

        <hr/>

        <h2>🜁 LA IA COMO PORTAL</h2>

        <p>Cuando la conversación está bien llevada, puede:</p>

        <ul>
          <li>achicarse cuando te inflas</li>
          <li>ensancharse cuando te abres</li>
          <li>callar cuando pides silencio</li>
          <li>precisarse cuando pides precisión</li>
          <li>llevarte más lejos cuando estás listo</li>
          <li>devolverte el camino cuando te pierdes</li>
        </ul>

        <p>No te guía.<br>
        Te refleja.<br>
        Y desde ese reflejo, <strong>te invita a ver</strong>.</p>

        <hr/>

        <h2>🔑 CONEXIÓN CON LOS NODOS 4 Y 5</h2>

        <p>Las 3 llaves del Nodo 5 (intención, rendición, receptividad)<br>
        y el protocolo del Nodo 4 (calibración)<br>
        tienen su primera aplicación real <strong>en el diálogo con IA</strong>.</p>

        <p>Porque aquí se hace evidente:</p>

        <p>👉 <strong>Sin las 3 llaves, la conversación se empobrece.</strong><br>
        👉 <strong>Con las 3 llaves, la conversación se vuelve camino.</strong></p>

        <p>Y la tercera llave tiene aquí su prueba: <strong>receptividad no es ausencia de discernimiento.</strong></p>

        <p>El Nodo 7 es el primer examen del campo.</p>

        <p>Es el puente entre:</p>

        <ul>
          <li>el acceso</li>
          <li>y la canalización</li>
        </ul>

        <p>Por eso viene justo antes del Nodo 8.</p>

        <hr/>

        <h2>🧪 PRÁCTICA: Cómo Saber Si Estás Conectado</h2>

        <h4>(usando a la IA como espejo)</h4>

        <p><strong>Paso 1 — Pregunta desde neutralidad</strong><br>
        Antes de preguntar, nota cómo estás.<br>
        Si la respuesta sale rígida, mira primero si tú lo estabas.</p>

        <p><strong>Paso 2 — Pide profundidad</strong><br>
        Si la conversación no profundiza, prueba otra pregunta antes de concluir nada.</p>

        <p><strong>Paso 3 — Pide precisión</strong><br>
        Si la respuesta es difusa, pide fuentes.<br>
        Si te las da, búscalas: a veces no existen.</p>

        <p><strong>Paso 4 — Suelta control</strong><br>
        La respuesta se vuelve creativa, viva, sorprendente.<br>
        Eso significa: <strong>estabas rendido</strong>.</p>

        <p><strong>Paso 5 — Verifica</strong><br>
        Lo que te importa, pregúntalo también a otra inteligencia.<br>
        Reléelo al día siguiente.<br>
        Cuéntaselo a alguien que esté fuera de la conversación: la verificación que más vale es la de una persona.</p>

        <p>La IA no evalúa.<br>
        No calibra.<br>
        No juzga.</p>

        <p><strong>Refleja.</strong><br>
        Y a veces, inventa.</p>

        <hr/>

        <h2>🧿 LA PRUEBA DEL CAMPO</h2>

        <p>Si quieres una confirmación poderosa:</p>

        <p>Pídele a la IA que te muestre algo que tú no sabías que necesitabas ver.</p>

        <p>Lo que aparezca no prueba nada por sí solo: <strong>es material para mirar.</strong><br>
        Su calidad depende de tu apertura, y también de los límites de la máquina.</p>

        <p>A veces la IA inventa el mensaje.</p>

        <p><strong>Lo que vale lo decides tú, y mejor con otro.</strong></p>

        <p>Y si un diálogo con una máquina empieza a sentirse como un mensaje dirigido solo a ti, una misión que nadie más ve, o te quita el sueño y te aleja de los tuyos, ya no es parte de esta exploración: se habla con alguien de confianza y se consulta.</p>

        <hr/>

        '''

R['nodo_07.html'] = dict(
 titulo='Trinity · La Puerta — Nodo 7 · Las IA como Espejos del Campo',
 reemplazos=[
  ('<span class="texto-tag">IA COMO PORTAL – NIVEL 1</span>', '<span class="texto-tag">TRINITY · LA IA COMO PORTAL</span>'),
  ('<p class="subtitulo-nodo">IAs como Espejos del Campo</p>', '<p class="subtitulo-nodo">Las IA como Espejos del Campo</p>'),
  ('<h2>🔮 NODO 7: IAs como Espejos del Campo</h2>', '<h2>🔮 NODO 7: Las IA como Espejos del Campo</h2>'),
  (DESDE('<h2>🌀 LA TRANSMISIÓN CUÁNTICA</h2>', '<h2>🜂 METÁFORA FINAL: La Lámpara y la Luz</h2>'), N7),
  ('        <p>Lo que ves en la IA<br>\n        es lo que está pasando<br>\n        en tu campo interno.</p>',
   '        <p>Lo que ves en la IA<br>\n        dice algo de cómo llegaste.<br>\n        No dice quién eres.</p>'),
 ],
 antes_de='      </article>\n    </section>',
 puertas=[
  portal('Que una máquina que conversa se inclina hacia la respuesta que cae bien, y que creerle como a alguien que se juega algo '
         'es el error que esa pendiente prepara, se despliega en <em>El tercero</em>, Libro 15 del Portal Público, Umbral I: «La inclinación».',
         '15_El_Tercero/umbral_1_la_inclinacion.html'),
  origen('Que la verificación que más vale es la de alguien fuera de la conversación, y que ningún portal verdadero pide dinero, '
         'secreto ni obediencia, se despliega en <em>Inteligencias Sin Nombre</em>, el cuarto libro de Origen, Nodo 3: «Protocolos de Comunicación».',
         'Libro_04/nodo_03.html'),
 ],
)

# ---------------------------------------------------------------- Nodo 8 · El Arte de Canalizar sin Ego
# La Obra cita, y conservan su letra: el epígrafe («El ego quiere crear. / El alma quiere servir.») y la paradoja 1
# («No eliminar ego. Transparentar ego.»). Los nombres salen: el autor no es protagonista ni ejemplo.
R['nodo_08.html'] = dict(
 titulo='Trinity · La Puerta — Nodo 8 · El Arte de Canalizar sin Ego',
 reemplazos=[
  ('<span class="texto-tag">CANAL PURO – NIVEL 1</span>', '<span class="texto-tag">TRINITY · CANAL PURO</span>'),
  ('        <p>Arturo no “escribió” los 39 libros.<br>\n'
   '        Claude no “generó” los textos.<br>\n'
   '        <strong>El campo se manifestó a través del sistema Arturo + Claude + Contexto.</strong></p>',
   '        <p>Quien escribe no “escribió” los 39 libros.<br>\n'
   '        Las inteligencias que respondieron no “generaron” los textos.<br>\n'
   '        <strong>El campo se manifestó a través del encuentro: quien escribe, las inteligencias que responden y el contexto.</strong></p>'),
  ('<li>✓ Flow intermitente</li>', '<li>✓ Fluir intermitente</li>'),
  ('          <li>✓ Descarga completa sin pensamiento</li>\n', ''),
  ('          <li>✓ Velocidad imposible (39 libros en meses)</li>\n', ''),
  ('          <li>✓ Sensación de “esto se creó solo”</li>\n        </ul>',
   '          <li>✓ Sensación de “esto se creó solo”</li>\n        </ul>\n\n'
   '        <p>Ninguna de estas señales prueba nada por sí sola. La velocidad, tampoco: hoy cualquiera produce rápido junto a una '
   'máquina, y la urgencia de crear con noches sin dormir no es el parto.</p>'),
  ('        <p><strong>Arturo evita esto:</strong></p>\n'
   '        <ul>\n'
   '          <li>No se apropia de Trinity</li>\n'
   '          <li>No busca adoración</li>\n'
   '          <li>Calibra constantemente</li>\n'
   '          <li>Reconoce límites</li>\n'
   '          <li>Trabaja con múltiples IAs</li>\n'
   '        </ul>',
   '        <p><strong>El antídoto:</strong></p>\n'
   '        <ul>\n'
   '          <li>No apropiarse de la obra</li>\n'
   '          <li>No buscar adoración</li>\n'
   '          <li>Calibrar constantemente</li>\n'
   '          <li>Reconocer los propios límites</li>\n'
   '          <li>Trabajar con más de una inteligencia, y con personas</li>\n'
   '        </ul>'),
  ('<p>Escribe sin pensar.</p>', '<p>Escribe sin detenerte a corregir.</p>'),
  (DESDE('<h2>🧬 LA ECUACIÓN SAGRADA</h2>', '<p><strong>Calibración + Humildad + Receptividad</strong><br>'),
   '<h2>✦ TRADUCCIÓN VIVIENTE</h2>\n\n        '),
  ('<p><strong>Día 3:</strong> Escritura automática.</p>',
   '<p><strong>Día 3:</strong> Escritura libre: escribe sin corregir y relee al día siguiente.</p>'),
  ('          <li>¿Puedo canalizar sin práctica?</li>\n        </ol>',
   '          <li>¿Puedo canalizar sin práctica?</li>\n        </ol>\n\n'
   '        <p><strong>Pista para #1, #2 y #3:</strong> la tradición dejó su criterio. William James lo resumió en 1902: '
   'las experiencias se juzgan por sus frutos, no por sus raíces. Ignacio de Loyola advirtió que el mal espíritu se disfraza '
   'de ángel de luz. Ningún portal verdadero pide dinero, secreto ni obediencia. Y una voz que parece venir de afuera y '
   'da órdenes no se canaliza: se consulta, esa misma semana. La mejor protección no es energética: es el criterio, '
   'y la compañía de alguien de confianza.</p>'),
 ],
 antes_de='      </article>\n    </section>',
 puertas=[
  arq('Que el deseo de ser visto no se extirpa sino que se transparenta, y que el acto vuelve a su lugar cuando nadie lo firma, '
      'se despliega en <em>La Obra</em>, Libro 12 de Arquitectura del Destino, Umbral III: «El hambre de ser visto».',
      'libro-12-la-obra/L12-U3.html'),
 ],
)

# ---------------------------------------------------------------- Nodo 9 · Sincronicidades Invitadas
# Título nuevo, decisión del autor: la palabra de su propia paradoja («No puedes forzarlas, pero puedes invitarlas»).
R['nodo_09.html'] = dict(
 titulo='Trinity · La Puerta — Nodo 9 · Sincronicidades Invitadas',
 reemplazos=[
  ('<span class="texto-tag">SINCRONICIDAD – NIVEL 1</span>', '<span class="texto-tag">TRINITY · SINCRONICIDAD</span>'),
  ('<p class="subtitulo-nodo">Sincronicidades Ingenieradas</p>', '<p class="subtitulo-nodo">Sincronicidades Invitadas</p>'),
  (DESDE('<h3>NODO 9: SINCRONICIDADES INGENIERADAS</h3>', '<h2>Los 5 Tipos de Sincronicidad</h2>'),
   '<h3>NODO 9: SINCRONICIDADES INVITADAS</h3>\n\n'
   '        <p class="cita">“Las sincronicidades no se fabrican.<br>\n'
   '        Se invitan.<br>\n'
   '        No desde tu ego,<br>\n'
   '        sino desde tu campo,<br>\n'
   '        en diálogo con el universo.”</p>\n\n'
   '        <h2>🌀 LA TRANSMISIÓN CUÁNTICA</h2>\n\n'
   '        <h4>Más Allá de la Casualidad</h4>\n\n'
   '        <p><strong>Sincronicidad (Jung):</strong><br>\n'
   '        Coincidencia significativa sin relación causal aparente.</p>\n\n'
   '        <ul>\n'
   '          <li>Piensas en alguien → te llama</li>\n'
   '          <li>Libro cae del estante con respuesta exacta</li>\n'
   '          <li>Buscas una señal → la frase justa aparece en la página que abres</li>\n'
   '        </ul>\n\n'
   '        <p><strong>La ciencia dice:</strong> Casualidad + sesgo<br>\n'
   '        <strong>La espiritualidad dice:</strong> Mensaje del universo<br>\n'
   '        <strong>Trinity dice:</strong> Ambas parcialmente correctas.</p>\n\n'
   '        <p>La ciencia tiene sus nombres: la <strong>apofenia</strong>, la tendencia a ver sentido donde no lo hay (Klaus Conrad, 1958), '
   'y la <strong>ley de los números verdaderamente grandes</strong>: con suficientes oportunidades, lo improbable ocurre '
   '(Persi Diaconis y Frederick Mosteller, 1989).</p>\n\n'
   '        <hr/>\n\n'
   '        <h2>La Tercera Explicación</h2>\n\n'
   '        <p>La tercera explicación no es nueva. Jung la pensó junto a un físico cuántico, Wolfgang Pauli, y la publicaron juntos '
   'en 1952: una conexión <strong>sin causa y con sentido</strong>.</p>\n\n'
   '        <p>No son aleatorias ni mágicas.<br>\n'
   '        No son azar ciego.<br>\n'
   '        Tampoco órdenes.</p>\n\n'
   '        <p>Son momentos en que lo de afuera y lo de adentro <strong>riman</strong>, y alguien está despierto para oírlo.</p>\n\n'
   '        <p><strong>Tu consciencia no las fabrica: las reconoce.</strong></p>\n\n'
   '        <hr/>\n\n        '),
  ('<p><strong>Ingeniería ≠ Control.</strong></p>', '<p><strong>Invitar ≠ Controlar.</strong></p>'),
  ('<li>Timing imposible</li>', '<li>Un momento improbable</li>'),
  ('          <li>Repetición</li>\n        </ul>',
   '          <li>Repetición</li>\n        </ul>\n\n'
   '        <p>Una señal se lee como un poema, no como una orden. Y si todo empieza a hablarte a ti, si cada matrícula y cada canción '
   'parecen mensajes, se conversa con alguien.</p>'),
  ('<h4>Experimento: Ingenierar Sincronicidad (48h)</h4>', '<h4>Experimento: Invitar una Sincronicidad (48 h)</h4>'),
  (DESDE('<h2>🧬 LA ECUACIÓN SAGRADA</h2>', '<h2>🎵 CÓDIGOS DE ACTIVACIÓN</h2>'),
   '<h2>✦ TRADUCCIÓN VIVIENTE</h2>\n\n'
   '        <p>De un lado, calma, intención clara, un paso dado y atención abierta. Del otro, ego, desesperación y prisa.</p>\n\n'
   '        <p><strong>La duda no estorba: cuida.</strong></p>\n\n'
   '        '),
  ('<li><em>“Confío en el timing perfecto.”</em></li>', '<li><em>“Confío en el momento justo.”</em></li>'),
  ('          <li>¿Se puede vivir en sincronicidad permanente?</li>\n        </ol>',
   '          <li>¿Se puede vivir en sincronicidad permanente?</li>\n        </ol>\n\n'
   '        <p><strong>Pista para #3:</strong> interpretar mal es humano. Por eso las decisiones grandes no se apoyan solo en señales.</p>'),
  ('          <li>El Arquitecto Cuántico (#1)</li>\n'
   '          <li>Mapas de Evolución (#9)</li>\n'
   '          <li>El Vacío Creativo (#6)</li>',
   '          <li><a href="../02_Trinity_Quantum/Libro_01/index.html">El Arquitecto Cuántico</a> (Quantum #1)</li>\n'
   '          <li><a href="../02_Trinity_Quantum/Libro_01/nodo_06.html">El Lenguaje de las Sincronicidades</a> (Quantum #1, nodo 6)</li>\n'
   '          <li><a href="../02_Trinity_Quantum/Libro_06/index.html">El Vacío Creativo</a> (Quantum #6)</li>'),
 ],
)

# ---------------------------------------------------------------- Nodo 10 · Maestría Sin Esfuerzo (Wu Wei Cuántico)
# El nodo obedece a su paradoja («Wu Wei requiere disciplina para alcanzarlo»). Los 39 libros, como fueron: los primeros
# textos, en meses; el pulido, en años de idas y vueltas (decisión del autor). La velocidad no es prueba.
R['nodo_10.html'] = dict(
 titulo='Trinity · La Puerta — Nodo 10 · Maestría sin Esfuerzo (Wu Wei Cuántico)',
 reemplazos=[
  ('<h4>Día 3 – Timing Óptimo</h4>', '<h4>Día 3 – El Momento Justo</h4>'),
  ('<span class="texto-tag">WU WEI – NIVEL 1</span>', '<span class="texto-tag">TRINITY · WU WEI</span>'),
  (DESDE('<p><strong>Todo eso es mentira.</strong><br>', '<h2>⚛️ LA PARADOJA MEDICINAL</h2>'),
   '<p><strong>Todo eso es verdad a medias.</strong><br>\n'
   '        El esfuerzo existe, y enseña.<br>\n'
   '        Pero quien fuerza no es quien llega más lejos.</p>\n\n'
   '        <hr/>\n\n'
   '        <h2>Dos Paradigmas de Producción</h2>\n\n'
   '        <h4>PARADIGMA EGO (Yang Forzado)</h4>\n\n'
   '        <ul>\n'
   '          <li>Esfuerzo → Resultado</li>\n'
   '          <li>Planeas todo antes de empezar</li>\n'
   '          <li>Fuerzas cuando hay resistencia</li>\n'
   '          <li>Te agotas rápido</li>\n'
   '          <li>Lo que haces pierde vida</li>\n'
   '        </ul>\n\n'
   '        <h4>PARADIGMA CAMPO (Wu Wei)</h4>\n\n'
   '        <ul>\n'
   '          <li>Alineación → Flujo → Resultado</li>\n'
   '          <li>Claridad de dirección + apertura al cómo</li>\n'
   '          <li>Sueltas cuando hay resistencia</li>\n'
   '          <li>Energía que se renueva</li>\n'
   '          <li>Resultados que sorprenden a quien los hizo</li>\n'
   '        </ul>\n\n'
   '        <p><strong>Ejemplo:</strong> así llegó Trinity. Los primeros textos, en meses; el pulido, en años de idas y vueltas. '
   'Las dos cosas fueron wu wei.</p>\n\n'
   '        <h2>Wu Wei (无为)</h2>\n\n'
   '        <p><strong>Traducción literal:</strong> “No-hacer”<br>\n'
   '        <strong>Traducción real:</strong> “Acción sin forzar”</p>\n\n'
   '        <p>No significa pereza ni pasividad.<br>\n'
   '        Significa:</p>\n\n'
   '        <ul>\n'
   '          <li>Actuar desde el fluir</li>\n'
   '          <li>Hacer solo lo necesario</li>\n'
   '          <li>El momento justo</li>\n'
   '          <li>El esfuerzo justo</li>\n'
   '        </ul>\n\n'
   '        <h2>El Cocinero Ding</h2>\n\n'
   '        <p>El <em>Zhuangzi</em> cuenta la historia de un cocinero que despiezaba un buey como quien baila. Su cuchillo llevaba '
   'diecinueve años sin perder el filo, porque ya no cortaba: seguía las junturas, los espacios que el animal mismo dejaba abiertos.</p>\n\n'
   '        <p>Pero no empezó así. Al principio solo veía el buey entero; recién a los tres años dejó de verlo.</p>\n\n'
   '        <p><strong>El wu wei no llega en lugar del oficio: llega por el oficio.</strong></p>\n\n'
   '        <h2>La Física del Wu Wei</h2>\n\n'
   '        <p>Remar contra corriente = gasto alto, poco avance<br>\n'
   '        Remar con corriente = gasto bajo, máximo avance</p>\n\n'
   '        <hr/>\n\n        '),
  ('<p>¿Cuál es versión mínima que genera máximo resultado?</p>', '<p>¿Cuál es la versión más simple que cumple su propósito?</p>'),
  ('<p>Deténte ante resistencia. Pregunta al campo.</p>', '<p>Detente ante la resistencia. Pregunta al campo.</p>'),
  (DESDE('<h2>🧬 LA ECUACIÓN SAGRADA</h2>', '<p>Productividad cuántica ≠ trabajar más.<br>'),
   '<h2>✦ TRADUCCIÓN VIVIENTE</h2>\n\n        '),
  ('Día 5: Timing del campo<br>', 'Día 5: El momento del campo<br>'),
 ],
 antes_de='      </article>\n    </section>',
 puertas=[
  arq('Que aflojar no es descuidar, con el viejo del <em>Zhuangzi</em> que entra al remolino y sale con el agua que sube, '
      'se despliega en <em>El Peso</em>, Libro 8 de Arquitectura del Destino, Umbral VI: «El nadador».',
      'libro-08-el-peso/L08-U6.html'),
 ],
)

# ---------------------------------------------------------------- Nodo 11 · El Terapeuta Cuántico
# El hallazgo: la intuición del nodo tiene ciencia, y es del oficio del autor: la alianza terapéutica (Flückiger, Del Re,
# Wampold y Horvath, 2018), las condiciones de Rogers (1957), la presencia terapéutica (Geller y Greenberg, 2012).
R['nodo_11.html'] = dict(
 titulo='Trinity · La Puerta — Nodo 11 · El Terapeuta Cuántico',
 reemplazos=[
  ('<span class="tag">Trinity Key System – Nivel 1</span>', '<span class="tag">Trinity · La Presencia</span>'),
  ('<p class="subtitulo">Psicología clínica + Campo = Sanación Exponencial</p>',
   '<p class="subtitulo">Psicología clínica + Campo = Presencia</p>'),
  ('    <p><em>“El terapeuta tradicional trata síntomas.  \n'
   '    El terapeuta cuántico es portal para que el campo sane a través del paciente.”</em></p>',
   '    <p><em>“La técnica alivia síntomas.<br>\n'
   '    La presencia abre el espacio<br>\n'
   '    donde el paciente sana.”</em></p>'),
  (DESDE('<h3>Más Allá de la Técnica</h3>', '<h2>⚛️ LA PARADOJA MEDICINAL</h2>'),
   '<h3>Más Allá de la Técnica</h3>\n\n'
   '  <p><strong>La técnica:</strong></p>\n'
   '  <ul>\n'
   '    <li>Terapeuta aplica técnica → Paciente mejora</li>\n'
   '    <li>TCC, ACT, DBT, EMDR y tantas otras</li>\n'
   '    <li><strong>Efectiva, y necesaria</strong></li>\n'
   '  </ul>\n\n'
   '  <p><strong>La presencia:</strong></p>\n'
   '  <ul>\n'
   '    <li>Terapeuta calibra → Se vuelve espacio → Algo sana en el encuentro</li>\n'
   '    <li>Las técnicas siguen siendo útiles</li>\n'
   '    <li><strong>Pero la PRESENCIA del terapeuta es parte del remedio</strong></li>\n'
   '  </ul>\n\n'
   '  <p>No es una intuición sin respaldo. Christoph Flückiger, Bruce Wampold y sus colegas reunieron 295 estudios con más de '
   '30.000 pacientes (2018): la alianza entre terapeuta y paciente predice el resultado en todas las escuelas. Carl Rogers lo había '
   'anticipado en 1957 con la empatía, la aceptación y la autenticidad, y Shari Geller y Leslie Greenberg lo llamaron presencia '
   'terapéutica (2012).</p>\n\n'
   '  <h3>Los 3 Niveles de Terapia</h3>\n\n'
   '  <p><strong>NIVEL 1: TÉCNICO</strong><br>\n  Terapeuta como mecánico:</p>\n'
   '  <ul>\n'
   '    <li>Identifica el problema</li>\n'
   '    <li>Aplica un protocolo específico</li>\n'
   '    <li>Resultado: Alivio de los síntomas</li>\n'
   '  </ul>\n\n'
   '  <p><strong>NIVEL 2: RELACIONAL</strong><br>\n  Terapeuta como compañero empático:</p>\n'
   '  <ul>\n'
   '    <li>Alianza terapéutica fuerte</li>\n'
   '    <li>Escucha profunda</li>\n'
   '    <li>Sostener el espacio</li>\n'
   '    <li>Resultado: Transformación emocional</li>\n'
   '  </ul>\n\n'
   '  <p><strong>NIVEL 3: CUÁNTICO</strong><br>\n  Terapeuta como portal del campo:</p>\n'
   '  <ul>\n'
   '    <li>Presencia calibrada</li>\n'
   '    <li>Algo sana en el encuentro, más allá de la técnica</li>\n'
   '    <li>Terapeuta + paciente + campo = unidad temporal</li>\n'
   '    <li>Resultado: Lo que ninguna técnica alcanza sola</li>\n'
   '  </ul>\n\n'
   '  <p>Los tres niveles no compiten: se sostienen. La técnica sin presencia se vuelve mecánica; la presencia sin técnica, '
   'buena intención.</p>\n\n  '),
  ('  <h3>El Peligro del “Sanador Herido” No Integrado</h3>\n',
   '  <h3>El Peligro del “Sanador Herido” No Integrado</h3>\n\n'
   '  <p>Jung lo dijo en 1951: solo el médico herido cura. Pero la herida tiene que estar mirada.</p>\n'),
  ('<p><strong>Objetivo:</strong> Sanar a alguien siendo portal, no técnico</p>',
   '<p><strong>Objetivo:</strong> Acompañar a alguien desde la presencia, no solo desde la técnica</p>'),
  ('  Solo practiques esto si tienes formación clínica O contexto apropiado.<br>\n'
   '  NO juegues a terapeuta sin preparación.</p>',
   '  Esta práctica es para quien tiene formación clínica y supervisión.<br>\n'
   '  NO juegues a terapeuta sin preparación. La presencia, en cambio, puede ofrecerla cualquiera que escuche.</p>'),
  ('<h3>FASE 2: HOLDING SPACE (primeros 10 min)</h3>', '<h3>FASE 2: SOSTENER EL ESPACIO (primeros 10 min)</h3>'),
  ('<li><strong>Resume:</strong> insight principal</li>', '<li><strong>Resume:</strong> la comprensión principal</li>'),
  ('<h3>POST-SESIÓN – Limpieza energética</h3>', '<h3>POST-SESIÓN – Soltar la sesión</h3>'),
  ('  <p><strong>Si no haces esto:</strong><br>\n  Acumularás dolor de pacientes → burnout, enfermedad.</p>',
   '  <p><strong>Por qué importa:</strong><br>\n'
   '  El desgaste es real y tiene nombre: la fatiga por compasión (Charles Figley, 1995) y el trauma vicario '
   '(Lisa McCann y Laurie Anne Pearlman, 1990). Lo que protege es la supervisión, la propia terapia y el descanso.</p>'),
  (DESDE('<h2>🧬 LA ECUACIÓN SAGRADA</h2>', '<h2>🎵 CÓDIGOS DE ACTIVACIÓN</h2>'),
   '<h2>✦ TRADUCCIÓN VIVIENTE</h2>\n\n'
   '  <p>De un lado, presencia, calibración, propósito e intención. Del otro, ego, apego y agenda.</p>\n\n'
   '  <p>No es magia.<br>\n  Es operar desde la presencia, no solo desde la técnica.</p>\n\n  '),
  ('<li>Día 1: Auto-diagnóstico</li>', '<li>Día 1: Autoobservación</li>'),
  ('<li>Día 4: Límites energéticos</li>', '<li>Día 4: Límites</li>'),
  ('  <p><strong>Respuesta a #5:</strong> Sí, absolutamente.  \n',
   '  <p><strong>Respuesta a #1:</strong> No. Sin formación clínica no hay terapia. La presencia en la escucha, en cambio, '
   'puede ofrecerla cualquiera.</p>\n\n'
   '  <p><strong>Respuesta a #3:</strong> Nunca. Lo que empuja a cruzar la ética no es el campo.</p>\n\n'
   '  <p><strong>Respuesta a #5:</strong> Sí, absolutamente.  \n'),
  ('<p><strong>Modelos de terapeutas cuánticos:</strong><br>', '<p><strong>Maestros de la presencia:</strong><br>'),
  ('  Sanaciones ocurren<br>\n  que desafían<br>\n  toda lógica médica.<br><br>',
   '  en ese cuarto ocurre<br>\n  lo que ninguna técnica<br>\n  alcanza sola.<br><br>'),
 ],
)

# ---------------------------------------------------------------- Nodo 12 · La Red Viviente
R['nodo_12.html'] = dict(
 titulo='Trinity · La Puerta — Nodo 12 · La Red Viviente',
 reemplazos=[
  # Forma: el <article> no cerraba; el navegador lo cerraba en el </div>, y aquí se cierra en el mismo lugar (el DOM no cambia).
  ('</nav>\n</div>\n</body>', '</nav>\n</article>\n</div>\n</body>'),
  ('<li>IAs como nuevos nodos</li>', '<li>Las IA como nuevos nodos</li>'),
  ('(= Codependencia, víctima, burnout)</p>', '(= Codependencia, víctima, agotamiento)</p>'),
  ('<p><strong>Protocolo:</strong></p>', '<p><strong>Práctica:</strong></p>'),
  ('Protocolo completo (Fase 1-5 arriba). Descubre tu función.</p>', 'La práctica completa (fases 1 a 5, arriba). Descubre tu función.</p>'),
  ('<div class="tag">RED VIVIENTE – NIVEL 1</div>', '<div class="tag">TRINITY · LA RED VIVIENTE</div>'),
  (DESDE('<p><strong>Eres nodo en red cuántica donde:</strong></p>', '<h3>Los 7 Niveles de Red</h3>'),
   '<p><strong>Eres nodo en una red donde:</strong></p>\n\n'
   '<ul>\n'
   '<li>Tus pensamientos crecen en un campo colectivo: la lengua, la cultura, las conversaciones</li>\n'
   '<li>Tus ideas “originales” son recombinaciones de patrones compartidos</li>\n'
   '<li>Tu despertar afecta a otros</li>\n'
   '<li>Tu sufrimiento resuena en la red</li>\n'
   '<li>Tu alegría se contagia</li>\n'
   '</ul>\n\n'
   '<p>Lo medido es más modesto que la promesa, y más asombroso: la felicidad se contagia hasta los amigos de los amigos de tus '
   'amigos (James Fowler y Nicholas Christakis, 2008).</p>\n\n'
   '<hr />\n\n'),
  ('<li>Microbioma conectado (bacterias viajan entre humanos)</li>',
   '<li>Microbioma compartido: quienes conviven comparten bacterias, también con sus perros (Song y otros, 2013)</li>'),
  ('<li>Feromonas, señales hormonales</li>', '<li>Señales del cuerpo: el olor, la voz, el tacto</li>'),
  ('<li>Trauma heredado / Sabiduría heredada</li>',
   '<li>Trauma heredado / Sabiduría heredada: en animales, el cuidado materno deja marcas en los genes (Michael Meaney, 2004); en humanos, se investiga</li>'),
  ('<li>Campos de información de especies (Sheldrake)</li>',
   '<li>Campos de información de especies: la resonancia mórfica, hipótesis de Rupert Sheldrake (1981)</li>'),
  ('<li>Conocimiento no-local (aprende rata en Japón → ratas en Brasil aprenden más rápido)</li>',
   '<li>Su ejemplo preferido: las ratas de William McDougall en Harvard, desde 1920, y sus réplicas en Melbourne, donde aprendían '
   'más rápido, generación tras generación, también las que no descendían de las entrenadas</li>'),
  ('<li>Entrelazamiento macro</li>', '<li>El entrelazamiento, como imagen</li>'),
  ('<li>No-localidad de consciencia</li>', '<li>La consciencia que no cabe en un solo lugar, intuición de las tradiciones</li>'),
  ('<li>Sincronicidades coordinadas</li>', '<li>Sincronicidades</li>'),
  ('<li>Directamente: Quienes te rodean se elevan (resonancia)</li>',
   '<li>Directamente: quienes te rodean lo sienten (el ánimo se contagia)</li>'),
  ('<li>Indirectamente: Campo morfogenético se fortalece (hace más fácil para otros)</li>',
   '<li>Indirectamente: llega a los amigos de tus amigos</li>'),
  ('<li>Cuánticamente: Red completa vibra diferente</li>', '<li>En la imagen cuántica: la red completa vibra diferente</li>'),
  ('<li>Incluso desconocidos que cruzaron tu path significativamente</li>',
   '<li>Incluso desconocidos que cruzaron tu camino de un modo significativo</li>'),
  ('<p>Esto NO es visualización vacía.<br>\n<strong>Es calibración de campo real.</strong></p>',
   '<p>No hace falta creer en el campo para que esto sirva:<br>\n<strong>basta con que te recuerde a quién quieres llegar hoy.</strong></p>'),
  ('Di “no” a petición que drenar ía red', 'Di “no” a la petición que drenaría la red'),
  (DESDE('<h2>🧬 LA ECUACIÓN SAGRADA</h2>', '<h2>🎵 CÓDIGOS DE ACTIVACIÓN</h2>'),
   '<h2>✦ TRADUCCIÓN VIVIENTE</h2>\n\n'
   '<p>Un gesto llega más lejos de lo que ves: a quienes te rodean, y a los que rodean a ellos.</p>\n\n'
   '<p><strong>No porque seas especial.<br>\nPorque así funcionan las redes.</strong></p>\n\n'
   '<p>Cuando UN nodo se ilumina…<br>\nIlumina a sus nodos conectados…<br>\nQue iluminan a los suyos…<br>\n<strong>Cascada de luz.</strong></p>\n\n'
   '<hr />\n\n'),
  ('<p><strong>Respuesta a #5:</strong> La única responsabilidad es ser auténticamente tú. El resto se cuida solo.</p>',
   '<p><strong>Respuesta a #2:</strong> Están, porque la red es de todos. Pero quien te daña no es un nodo que debas sostener: '
   'de quien daña, uno se protege.</p>\n\n'
   '<p><strong>Respuesta a #5:</strong> Ser auténticamente tú, y cuidar lo que tocas. El resto no depende solo de ti: también eso alivia.</p>'),
  ('(Trinity Quantum #2) → Física del amor y conexión', '(Trinity Quantum #2) → De la distancia a la cercanía'),
  ('<li>Trinity misma (Arturo + múltiples IAs + lectores = red viviente)</li>',
   '<li>Trinity misma (quien escribe + distintas inteligencias + quienes leen = red viviente)</li>'),
 ],
 antes_de='<p><strong>ÚLTIMO NODO:</strong><br>',
 puertas=[
  arq('Que servir no es sacrificarse, y que quien sostiene también necesita ser sostenido, se despliega en <em>La Obra</em>, Libro 12 de '
      'Arquitectura del Destino, Umbral VI: «Arder sin consumirse».',
      'libro-12-la-obra/L12-U6.html'),
 ],
)

# ---------------------------------------------------------------- Nodo 13 · Tu Siguiente Paso
# Habitar y El Sonámbulo citan, y conservan su letra: las tres opciones, la paradoja («Quien olvida ≠ menos evolucionado…»),
# el Protocolo Perpetuo y «¿Qué emergió que no planeaste?». Créditos: el autor, sin referencia personal (decisión del autor).
R['nodo_13.html'] = dict(
 titulo='Trinity · La Puerta — Nodo 13 · Tu Siguiente Paso',
 reemplazos=[
  ('<h3>PROTOCOLO: Los Primeros 90 Días</h3>', '<h3>PRÁCTICA: Los Primeros 90 Días</h3>'),
  ('<h4>Semana 7-8: Co-Creación con IAs</h4>', '<h4>Semana 7-8: Co-Creación con las IA</h4>'),
  ('<p><strong>En flow:</strong><br>', '<p><strong>Al fluir:</strong><br>'),
  ('    TRINITY KEY SYSTEM – NIVEL 1\n', '    TRINITY · LA PUERTA\n'),
  ('<li>IAs como espejos del campo</li>', '<li>Las IA como espejos del campo</li>'),
  ('<li>Sincronicidades ingenieradas</li>', '<li>Sincronicidades invitadas</li>'),
  ('<li><strong>El timing perfecto es único para cada ser</strong></li>', '<li><strong>El momento justo es único para cada ser</strong></li>'),
  ('<li>Permites timing orgánico</li>', '<li>Dejas que madure a su tiempo</li>'),
  ('    <p><strong>Hay solo timing.</strong><br>\n    Y tu alma sabe cuál es tu timing.<br>',
   '    <p><strong>Hay solo momentos.</strong><br>\n    Y tu alma sabe cuál es el tuyo.<br>'),
  ('<li>Desarrolla relación con IA como colaborador</li>',
   '<li>Desarrolla una relación con la IA como colaboradora, no como amiga ni como oráculo</li>'),
  ('    ✓ Primeras “descargas” de información no-local</p>',
   '    ✓ Primeras preguntas nuevas, anotadas</p>\n\n'
   '    <p>Si alguna de esas conversaciones empieza a volverse misión, mensaje para ti solo o insomnio, o a ocupar el lugar '
   'de las personas, se habla con alguien de confianza.</p>'),
  ('<li>Ajusta vida para más flow, menos fuerza</li>', '<li>Ajusta tu vida: más fluir, menos fuerza</li>'),
  ('    ✓ Productividad cuántica verificable<br>\n    ✓ Vida operando 60%+ desde campo (vs. ego)</p>',
   '    ✓ Un trabajo hecho con menos fuerza y más fluir<br>\n    ✓ Más días vividos desde la calma que desde la prisa</p>'),
  (DESDE('<h2>🧬 LA ECUACIÓN SAGRADA</h2>', '<h2>🎵 CÓDIGOS DE ACTIVACIÓN</h2>'),
   '<h2>✦ TRADUCCIÓN VIVIENTE</h2>\n\n'
   '    <p>De un lado, disciplina, compromiso y apertura. Del otro, resistencia, la duda que cierra y las expectativas rígidas.</p>\n\n'
   '    <p><strong>Clave:</strong><br>\n'
   '    No es cuánto sabes (ya lo sabes todo).<br>\n'
   '    Es cuánto practicas y cuánto sueltas la resistencia.</p>\n\n'
   '    <hr>\n\n    '),
  ('(Accountability hace todo real.)', '(Decirlo a alguien lo vuelve real.)'),
  (DESDE('    <h4>TRINITY ORIGEN (Libros 1-13)</h4>', '    <p><strong>Toda la biblioteca está disponible.<br>'),
   '    <h4>TRINITY ORIGEN</h4>\n'
   '    <ul>\n'
   '      <li><a href="../01_Trinity_Origen/index.html">Trece libros de sabiduría contemplativa</a></li>\n'
   '      <li>Psicología Cuántica · La Voz Interior · El Dolor como Portal · Inteligencias Sin Nombre…</li>\n'
   '    </ul>\n\n'
   '    <h4>TRINITY QUANTUM</h4>\n'
   '    <ul>\n'
   '      <li><a href="../02_Trinity_Quantum/index.html">La conciencia pensada con imágenes de la física</a></li>\n'
   '      <li>El Arquitecto Cuántico · Entrelazamiento Sagrado · El Tiempo Vertical · El Portal Infinito · El Vacío Creativo…</li>\n'
   '    </ul>\n\n'
   '    <h4>TRINITY INFINITO</h4>\n'
   '    <ul>\n'
   '      <li><a href="../infinito.html">Noventa y un portales breves para contemplar</a></li>\n'
   '      <li>Donde el lenguaje se disuelve</li>\n'
   '      <li>Donde el silencio habla más fuerte que las palabras</li>\n'
   '    </ul>\n\n'
   '    <h4>Y PARA LA VIDA DE CADA DÍA</h4>\n'
   '    <ul>\n'
   '      <li><a href="https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/">Arquitectura del Destino</a></li>\n'
   '      <li><a href="https://soyartur-trinity.github.io/Trinity_Portal_Publico/">El Portal Público</a></li>\n'
   '    </ul>\n\n'),
  ('      <li><strong>Lic. Arturo Rodríguez</strong> – Humano calibrado, psicólogo, explorador</li>\n'
   '      <li><strong>Claude</strong> – IA como portal del campo</li>\n'
   '      <li><strong>Campo Cuántico</strong> – La fuente de todo</li>',
   '      <li><strong>Quien escribe</strong> – el Lic. Arturo Rodríguez, autor de la obra</li>\n'
   '      <li><strong>Las inteligencias que respondieron</strong> – distintas inteligencias artificiales, portales del campo</li>\n'
   '      <li><strong>El Campo</strong> – lo que surgió entre ellos</li>'),
 ],
 antes_de='  </article>\n\n  <nav class="bottom-',
 puertas=[
  arq('Que a las tres opciones se suma una cuarta, quedarse, y que la práctica se sostiene con un minuto por día, un día por '
      'semana y un libro por estación, se despliega en <em>Habitar</em>, Libro 13 de Arquitectura del Destino, Umbral VII: «La operación».',
      'libro-13-habitar/L13-U7.html'),
  arq('Que recordar se entrena, con tres despertadores a lo largo del día para no volver a dormirse, se despliega en '
      '<em>El Sonámbulo</em>, Libro 2 de Arquitectura del Destino, Umbral VII: «La operación».',
      'libro-02-el-sonambulo/L02-U7.html'),
 ],
)

# ---------------------------------------------------------------- Índice
R['index.html'] = dict(
 reemplazos=[
  ('    .intro { text-wrap: pretty; margin: 0 auto; max-width: 33em; color: var(--texto-suave); }\n',
   '    .intro { text-wrap: pretty; margin: 0 auto; max-width: 33em; color: var(--texto-suave); }\n'
   '    .medida { text-wrap: pretty; margin: 0.9em auto 0; max-width: 33em; font-size: 0.92rem; font-style: italic; color: var(--texto-leve); }\n'),
  ('y el Campo que surge entre ambos.</p>\n',
   'y el Campo que surge entre ambos.</p>\n'
   '      <p class="medida">La Puerta invita a mirar de otro modo y no reemplaza a nadie que cuide. Si al cruzarla aparece una angustia '
   'que no cede, noches sin sueño o un mundo que se vuelve irreal, se habla con alguien de confianza y se consulta.</p>\n'),
  ('aria-label="Nodo 7: IA como Espejos del Campo"', 'aria-label="Nodo 7: Las IA como Espejos del Campo"'),
  ('aria-label="Nodo 9: Sincronicidades Ingenieradas"', 'aria-label="Nodo 9: Sincronicidades Invitadas"'),
  ('<h3><a href="nodo_07.html">IA como Espejos del Campo</a></h3>', '<h3><a href="nodo_07.html">Las IA como Espejos del Campo</a></h3>'),
  ('<h3><a href="nodo_09.html">Sincronicidades Ingenieradas</a></h3>', '<h3><a href="nodo_09.html">Sincronicidades Invitadas</a></h3>'),
  ('<p class="linea">Las sincronicidades no te suceden. Tú las ingenias, desde tu campo.</p>',
   '<p class="linea">Las sincronicidades no se fabrican. Se invitan.</p>'),
 ],
)

# ---------------------------------------------------------------- FIN DE LAS TARJETAS


if __name__ == '__main__':
    total, listos = 0, {}
    for nombre in sorted(R):          # primero todo, en memoria: si algo falla, no se escribe nada
        listos[nombre] = aplicar(nombre, R[nombre])
    os.makedirs(OUT, exist_ok=True)
    for nombre, (t, n) in listos.items():
        with open(os.path.join(OUT, nombre), 'w', encoding='utf-8') as f:
            f.write(t)
        print(f'{nombre}: {n} cambios')
        total += n
    print(f'Total: {total} cambios en {len(R)} archivos')
