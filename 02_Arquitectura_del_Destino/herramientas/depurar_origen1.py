# Depuración de Origen I, Psicología Cuántica (noviembre de 2026), con el veto del Lic. Arturo Rodríguez.
# Lente: riesgo clínico y puertas hacia la Red, como en Origen VI y VIII. La visión del libro queda entera;
# el libro obedece a sus mejores frases («más allá del pensamiento mágico», «esto o algo mejor», «que el
# patrón emerja levemente», «equilibrio psicológico», «escepticismo saludable»). Debajo del traje cuántico,
# casi todo era psicología clínica con nombre propio, y ese nombre entra: Weekes, Gendlin, Damasio,
# Schwartz, Levine, Siegel, la reconsolidación de la memoria, Tedeschi y Calhoun. Cambian las promesas
# clínicas (el trauma sanado al instante, el pasado que cambia «literalmente», la visualización que revierte
# una enfermedad), las cifras sin fuente (los hercios de las emociones, las de HeartMath, el «principio del
# 1 %»), las prácticas que podían dañar (subir la intensidad del trauma, verificar la telepatía llamando a la
# familia, actuar al instante sobre una comprensión súbita) y los casos inventados, que dejan su lugar a
# casos reales. El lema lleva una palabra más, elegida por Arturo: «No somos solo víctimas…». Se abren ocho
# puertas, todas de ida y vuelta.
#
# Se aplica sobre el original de la etiqueta origen-original, con reemplazos que deben aparecer exactamente
# una vez (o tramos, de un texto a otro, inclusive); si un anclaje falla, el script se detiene sin escribir.
#
# Uso: ORIGEN1_SRC=RUTA/origen-original/01_Trinity_Origen/Libro_01/ ORIGEN1_OUT=RUTA/salida/ python3 depurar_origen1.py
import os, sys

SRC = os.environ.get('ORIGEN1_SRC', '/home/claude/work/o1/')
OUT = os.environ.get('ORIGEN1_OUT', '/home/claude/work/o1/out/01_Trinity_Origen/Libro_01/')

NOTA = ('<!-- Depurado en noviembre de 2026 según la guía de depuración de Quantum, que vale para Origen '
        '(Arquitectura del Destino, maestro v4, sección 5, con las precisiones 5 y 6 de Origen), con el veto del Lic. Arturo Rodríguez: '
        'la visión del libro queda; salen las promesas clínicas, las cifras sin fuente y las prácticas que podían dañar, y los casos '
        'inventados dejan su lugar a casos reales; se suma el cuidado clínico en la voz de cada nodo y se abren puertas fractales hacia la Red. '
        'El original está en la etiqueta origen-original del repositorio Trinity-. -->\n')

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


CSS = '''
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
.content p a, .content li a{
  color:var(--gold);
  text-decoration:underline;
  text-decoration-color:rgba(214,179,106,.45);
  text-underline-offset:3px;
}
.content p a:hover, .content li a:hover{ text-decoration-color:var(--gold); }
.puerta .cruzar:hover{ border-color:var(--p-acento); background:rgba(255,255,255,.04); }
.puerta .cruzar:focus-visible{ outline:2px solid var(--p-acento); outline-offset:3px; }
@media (max-width: 720px){
  .content p,
  .content li{ font-size:18px; line-height:1.7; }
  .content blockquote{ font-size:17px; line-height:1.7; }
  .node-quote{ font-size:17px; }
  .content .puerta .p-nombre{ font-size:15px; }
  .puerta{ padding:16px 16px 14px; }
}
@media (prefers-reduced-motion: reduce){
  .puerta .cruzar{ transition:none; }
}
</style>
</head>'''

CSS_INDEX = '''
/* ============================================================
   Depuración · noviembre de 2026
   Letra más grande en el teléfono.
   ============================================================ */
.cierre .medida{color:var(--text-soft);font-size:0.95rem;line-height:1.8;margin-top:1rem;}
@media (max-width: 720px){
  .hero-desc{ font-size:18px; line-height:1.7; }
  .nodo-pregunta{ font-size:16px; }
  .cierre p{ font-size:17px; line-height:1.7; }
}
</style>
</head>'''

# Frases de cuidado con la letra ya fijada en la constelación
ACOMPANA = 'Lo que acompaña nunca reemplaza un tratamiento que funciona.'      # Origen X.1
SENTIR = ('Nada de lo que duele prueba que hayas vivido mal, y ninguna forma de sufrir es falta de quien la vive.')   # Origen X.1
HOY = 'A quien enferma hoy lo cuida lo que hoy existe, que ya es mucho, y cada año es más.'   # precisión 6
HONRAR = ('Honrar no significa justificar: quien sufrió abuso no necesita darle un lugar a quien lo dañó para sanar.')   # Origen X.6
GROF = ('Stanislav y Christina Grof llamaron emergencia espiritual a las crisis que a veces acompañan un despertar, '
        'y enseñaron que se atraviesan acompañadas.')   # Origen X.5
SENALES = ('Estas señales también pueden ser señales de otras cosas. Si traen noches sin sueño, pensamientos que corren, '
           'una misión urgente, mensajes de guías o la certeza de saber lo que va a pasar, no es el salto que se acerca: '
           'es el momento de pedir ayuda, esa misma semana. ' + GROF)   # Origen VI.7
PORTAL = 'ningún portal verdadero pide dinero, secreto ni obediencia'   # Origen VI.7
DECISIONES = ('Las decisiones grandes, las que no se deshacen, piden las dos voces, la del cuerpo y la de la razón, '
              'con tiempo y con alguien de confianza.')   # Quantum 11.7
OJOS = ('Si alguna vez sentiste que no eras real o que te ibas de tu cuerpo, hazla con los ojos abiertos y los pies en el suelo, '
        'o déjala para otro momento.')   # Origen VII.5
LLAMALO = ('Y cuando sientes que a un ser querido le pasa algo, lo que sabes con certeza es cuánto te importa: llámalo.')   # Quantum 2.1
DEJA_VU = ('Un déjà vu que se repite muchas veces al día merece que lo vea un médico: a veces lo produce el cuerpo, y tiene tratamiento.')   # Origen VI.3

R = {}


def mapa(items):
    filas = ''.join('      <li>%s</li>\n' % x for x in items)
    return ('<div class="mapa-nav">\n    <h3>Mapa de navegación del nodo</h3>\n    <ul>\n%s    </ul>\n  </div>' % filas)


def aplicar(nombre, d):
    with open(os.path.join(SRC, nombre), encoding='utf-8') as f:
        t = f.read()
    cuenta = 0

    def una_vez(t, viejo, nuevo, que):
        n = t.count(viejo)
        if n != 1:
            sys.exit(f'{nombre}: {que} aparece {n} veces:\n{viejo[:200]}')
        return t.replace(viejo, nuevo)

    import re
    titulo = re.search(r'<title>(.*?)</title>\n', t).group(0)
    t = una_vez(t, titulo, titulo + NOTA, 'el título'); cuenta += 1
    t = una_vez(t, '</style>\n</head>', (CSS_INDEX if nombre == 'index.html' else CSS).lstrip('\n'), 'el cierre del estilo'); cuenta += 1
    if 'mapa' in d:
        a = t.index('<div class="mapa-nav">')
        b = t.index('  </div>', a) + len('  </div>')
        t = t[:a] + mapa(d['mapa']) + t[b:]
        cuenta += 1
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
        cierre = '\n\n  </main>'
        t = una_vez(t, cierre, '\n' + ''.join(d['puertas']).rstrip('\n') + cierre, 'el cierre del <main>'); cuenta += 1
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, nombre), 'w', encoding='utf-8') as f:
        f.write(t)
    return cuenta


# ---------------------------------------------------------------- Nodo 1
R['nodo_01.html'] = dict(
 reemplazos=[
  ('<p>La <strong>Psicología Cuántica</strong> nace del reconocimiento de que la conciencia no es un epifenómeno del cerebro, sino el <strong>campo fundamental</strong> dentro del cual emergen tanto el observador como la realidad observada. Este primer nodo explora cómo esta comprensión revoluciona completamente nuestro entendimiento de la experiencia humana.</p>',
   '<p>La <strong>Psicología Cuántica</strong> nace del reconocimiento de que la conciencia no es un epifenómeno del cerebro, sino el <strong>campo fundamental</strong> dentro del cual emergen tanto el observador como la realidad observada. Es una postura con linaje. El físico John Archibald Wheeler imaginó un universo participativo, en el que nadie asiste a la realidad desde afuera; Amit Goswami llevó esa intuición a la conciencia en <em>El universo autoconsciente</em> (1993); y las tradiciones contemplativas la habitan desde hace milenios. La física la deja abierta, y este libro elige vivir en ella. Este primer nodo explora cómo esta comprensión transforma nuestro entendimiento de la experiencia humana.</p>'),
  ('<p>Así como Heisenberg demostró que no podemos conocer simultáneamente la posición y velocidad de una partícula, en el territorio de la conciencia enfrentamos una incertidumbre fundamental: <strong>no podemos observar un estado mental sin alterarlo</strong>.</p>',
   '<p>Así como Werner Heisenberg mostró en 1927 que no se pueden conocer a la vez, con precisión ilimitada, la posición y el impulso de una partícula, en el territorio de la conciencia enfrentamos una incertidumbre fundamental: <strong>no podemos observar un estado mental sin alterarlo</strong>.</p>\n'
   '    <p>En la física, para alterar algo no hace falta una conciencia que mire: basta con medirlo, y qué es medir sigue siendo una pregunta abierta. En la psique, en cambio, la mirada consciente es la que mide, y por eso transforma. La psicología lo comprobó por su cuenta: desde los años setenta se sabe que llevar un registro de lo que uno hace cambia lo que uno hace, y en 2007 Matthew Lieberman y su equipo vieron que poner en palabras una emoción le baja la intensidad en el cerebro que la siente.</p>'),
  ('<h4>Viñeta Clínica: La Transformación a través de la Observación</h4>\n    <blockquote>María llega a consulta sumida en una depresión que describe como "pesada y sin salida". El terapeuta, en lugar de observar la depresión como "síntoma a tratar", la observa como "información que busca ser reconocida". Esta sutil diferencia en la calidad de observación permite que María experimente su depresión no como identidad fija, sino como estado temporal que contiene mensajes importantes sobre necesidades no atendidas.</blockquote>',
   '<h4>Hallazgo Clínico: La Transformación a través de la Observación</h4>\n    <blockquote>En los años sesenta, Eugene Gendlin, discípulo de Carl Rogers, escuchó con su equipo las grabaciones de cientos de sesiones de psicoterapia buscando qué distinguía a las que daban fruto. No era la técnica del terapeuta ni el tema que traía el paciente. Era algo que se oía desde las primeras sesiones: quienes mejoraban se detenían, hablaban más despacio y buscaban palabras para algo que sentían en el cuerpo y todavía no sabían nombrar. No describían su malestar desde afuera: lo atendían desde adentro, y al atenderlo, cambiaba. Gendlin llamó <em>focusing</em> a esa atención (1978) y dedicó el resto de su vida a enseñarla.</blockquote>'),
  ('Cambia la naturaleza misma de lo que está ocurriendo en el espacio terapéutico.</p>',
   'Cambia la naturaleza misma de lo que está ocurriendo en el espacio terapéutico. Las dos miradas no se excluyen: una depresión se diagnostica y se trata, y además se escucha.</p>'),
  ('(curiosidad vs. juicio, amor vs. resistencia)', '(curiosidad o juicio, amor o resistencia)'),
  ('La psique humana opera de manera similar: somos', 'La psique humana se deja ver con esa misma imagen: somos'),
  ('<li>La sanación ocurre cuando expandimos el campo de posibilidades antes del colapso</li>\n      <li>El "cambio" no requiere luchar contra patrones existentes, sino expandir el espectro de colapsos disponibles</li>',
   '<li>La sanación avanza cuando expandimos el campo de posibilidades antes del colapso</li>\n      <li>El "cambio" no requiere luchar contra patrones existentes, sino expandir el espectro de colapsos disponibles, y darle tiempo</li>'),
  ('<h4>Caso Práctico: Reorganización Cuántica Instantánea</h4>\n    <blockquote>Juan sufre de ataques de pánico durante 15 años. En lugar de trabajar el "historial de pánico", el terapeuta cuántico lo guía a reconocer que en cada momento antes del pánico, existe una superposición de posibilidades: Juan-en-pánico y Juan-en-calma co-existen. Al aprender a "observar la superposición" antes del colapso automático, Juan desarrolla la capacidad de influenciar conscientemente hacia cuál versión colapsa.</blockquote>',
   '<h4>Caso Real: Flotar a Través del Pánico</h4>\n    <blockquote>En 1962, una médica australiana, Claire Weekes, publicó su primer libro, <em>Self Help for Your Nerves</em>, para quienes vivían con los nervios en carne viva. Ella misma había atravesado años de angustia en su juventud, y su método cabía en cuatro palabras: enfrentar, aceptar, flotar, dejar pasar el tiempo. No pelear con la primera oleada del pánico ni huir de ella, sino dejar que pase por el cuerpo, flotando, sin sumarle el segundo miedo, el miedo al miedo, que es el que la sostiene. Es lo que la Psicología Cuántica llama observar la superposición antes del colapso automático: entre la sensación y el pánico hay un instante, y en ese instante cabe otra respuesta. Weekes insistía en la cuarta palabra: los nervios sensibilizados piden semanas o meses, y cada recaída es una ocasión más para practicar. Décadas después, los programas para el pánico siguen apoyándose en lo que ella enseñó.</blockquote>\n'
   '    <p>Un primer ataque de pánico merece una consulta: a veces el cuerpo tiene algo que decir que no es miedo.</p>'),
  ('<p>Cuando dos partículas se entrelazan cuánticamente, permanecen conectadas instantáneamente sin importar la distancia. En el nivel de la conciencia,',
   '<p>Cuando dos partículas se entrelazan cuánticamente, siguen respondiendo como un solo sistema aunque estén en extremos opuestos del universo, sin que viaje entre ellas ninguna señal. Entre las personas es una imagen, y nombra bien lo que vivimos: en el nivel de la conciencia,'),
  ('Emergencia de insights simultáneos en ambos participantes', 'Emergencia de comprensiones simultáneas en ambos participantes'),
  ('<li><strong>Intención Compartida:</strong> Establecer intención mutua de entrelazamiento</li>',
   '<li><strong>Intención Compartida:</strong> Establecer intención mutua de entrelazamiento, siempre con quien lo elige: nunca se impone a otro</li>'),
  ('<li><strong>Permisión de Influencia:</strong> Permitir que el estado del otro te afecte conscientemente</li>',
   '<li><strong>Permiso de Influencia:</strong> Permitir que el estado del otro te afecte conscientemente, sin perder el suelo bajo tus pies</li>'),
  ('El libre albedrío no es la capacidad de controlar outcomes, sino', 'El libre albedrío no es la capacidad de controlar resultados, sino'),
  ('<p>La realidad no es algo que nos sucede — es algo que <strong>co-creamos</strong>',
   '<p>La realidad no es solo algo que nos sucede: también es algo que <strong>co-creamos</strong>'),
  ('<p>Si la realidad emerge de nuestros actos de observación, entonces tenemos una responsabilidad fundamental: <strong>la calidad de nuestra conciencia determina la calidad de la realidad que se manifiesta</strong>.</p>',
   '<p>Si la realidad emerge también de nuestros actos de observación, entonces tenemos una responsabilidad fundamental: <strong>la calidad de nuestra conciencia influye en la calidad de la realidad que se manifiesta</strong>.</p>\n'
   '    <p>Responder por la propia mirada no es cargar con todo lo que pasa. La enfermedad, la pobreza o la violencia que alguien sufre no son la medida de su conciencia: co-crear es participar, no gobernar. Lo que sí está en nuestras manos es desde dónde miramos lo que nos toca, y qué hacemos con eso.</p>'),
  ('<li><strong>Colapso Consciente (instantáneo):</strong> Elige la opción de mayor coherencia. Actúa con total compromiso.</li>\n    </ol>',
   '<li><strong>Colapso Consciente (instantáneo):</strong> Elige la opción de mayor coherencia. Actúa con total compromiso.</li>\n    </ol>\n'
   '    <p>Así se toman las decisiones del día. Para las grandes, las que no se deshacen, deja pasar una noche y conversa con alguien de confianza antes del colapso final.</p>'),
  ('<p><strong>Preparación individual (2–3 min antes):</strong> Establece coherencia cardio-cerebral. Conecta',
   '<p><strong>Preparación individual (2–3 min antes):</strong> Respira despacio, unas seis veces por minuto, como enseña el tercer nodo. Conecta'),
  ('Agradece al campo compartido. Permite que los insights se integren gradualmente.', 'Agradece al campo compartido. Permite que las comprensiones se integren gradualmente.'),
  ('<strong>no somos víctimas de nuestra experiencia, sino co-creadores conscientes de la realidad emergente</strong>',
   '<strong>no somos solo víctimas de nuestra experiencia: también somos co-creadores conscientes de la realidad emergente</strong>'),
  ('<li><strong>DE:</strong> Responsabilidad personal limitada → <strong>A:</strong> Responsabilidad cósmica por la calidad de manifestación</li>',
   '<li><strong>DE:</strong> Responsabilidad personal limitada → <strong>A:</strong> Responsabilidad compartida en el tejido de la manifestación</li>'),
 ],
 puertas=[arq('Que la pregunta «¿Quién observa?», dejada sin responder, es la misma que proponían Bassui en el Japón del siglo XIV y Ramana Maharshi en el sur de la India, y que el cuarto nivel de este protocolo la vuelve una práctica, se despliega en <em>El Testigo</em>, Libro 3 de <em>Arquitectura del Destino</em>, Umbral V: «Observar al que observa».',
              'libro-03-el-testigo/L03-U5.html')],
)

# ---------------------------------------------------------------- Nodo 2
R['nodo_02.html'] = dict(
 reemplazos=[
  ('Las emociones no son simplemente reacciones químicas — son <strong>sistemas de información cuántica</strong> que nos conectan instantáneamente con frecuencias específicas de la realidad.',
   'Las emociones no son simplemente reacciones químicas — son <strong>sistemas de información</strong>, y la imagen cuántica nombra bien su alcance: nos conectan, a veces en un instante, con aspectos específicos de la realidad.'),
  ('<p>Imagina que tu sistema emocional funciona como un <strong>receptor de radio multidimensional</strong>, capaz de sintonizar diferentes frecuencias de información. Cada emoción es una <strong>estación específica</strong> que transmite datos sobre aspectos particulares de la realidad.</p>',
   '<p>Imagina que tu sistema emocional funciona como un <strong>receptor de radio multidimensional</strong>, capaz de sintonizar diferentes frecuencias de información. Cada emoción es una <strong>estación específica</strong> que transmite datos sobre aspectos particulares de la realidad. Las frecuencias son aquí una imagen, no una medida: ninguna emoción vibra en hercios.</p>\n'
   '    <p>Lo que sí se midió es que las emociones informan, y que conviene aprender a leerlas. En 1983, Norbert Schwarz y Gerald Clore llamaron por teléfono a vecinos de una ciudad estadounidense, en días de sol y en días de lluvia, y les preguntaron cuán satisfechos estaban con su vida. Los días de sol respondían mejor. Pero si antes les preguntaban, como al pasar, qué tiempo hacía, la diferencia desaparecía: al notar de dónde venía su ánimo, dejaban de tomarlo como un juicio sobre su vida. El ánimo informa, y a veces informa sobre el clima. De eso trata este nodo: de escuchar la estación correcta.</p>'),
  ('<p><strong>Miedo</strong> (20–150 Hz): Detecta', '<p><strong>Miedo:</strong> Detecta'),
  ('riesgos reales vs. imaginarios.', 'riesgos reales e imaginarios.'),
  ('<p><strong>Ira</strong> (150–200 Hz): Señala', '<p><strong>Ira:</strong> Señala'),
  ('<p><strong>Tristeza</strong> (50–100 Hz): Indica', '<p><strong>Tristeza:</strong> Indica'),
  ('<p><strong>Amor</strong> (528 Hz): Detecta', '<p><strong>Amor:</strong> Detecta'),
  ('<p><strong>Compasión</strong> (400–500 Hz): Percibe', '<p><strong>Compasión:</strong> Percibe'),
  ('<p><strong>Alegría</strong> (540–600 Hz): Reconoce', '<p><strong>Alegría:</strong> Reconoce'),
  ('<p><strong>Éxtasis</strong> (700+ Hz): Conexión', '<p><strong>Éxtasis:</strong> Conexión'),
  ('<p><strong>Paz Profunda</strong> (600–700 Hz): Sintonización', '<p><strong>Paz Profunda:</strong> Sintonización'),
  ('<p><strong>Comprensión Súbita</strong> (Variable): Acceso instantáneo a información trans-dimensional. Acción: actuar inmediatamente sobre los insights recibidos.</p>',
   '<p><strong>Comprensión Súbita:</strong> Acceso instantáneo a información trans-dimensional. Acción: anotarla enseguida y dejarla dormir una noche antes de obrar.</p>'),
  ('Recuerda suavemente una situación que generó miedo.', 'Recuerda suavemente una situación que generó un miedo leve, no la más difícil.'),
  ('<li>¿Qué guidance espiritual contiene esta frecuencia?</li>', '<li>¿Qué orientación espiritual contiene esta frecuencia?</li>'),
  ('<h4>Viñeta Clínica: Ana y la Ansiedad Inexplicable</h4>\n    <blockquote>Ana, ejecutiva de 35 años, experimenta ansiedad intensa sin causa aparente durante una reunión importante. Aplicando el protocolo de cuatro capas: Capa 1 — la ansiedad señala patrones de perfeccionismo no alineados con su autenticidad. Capa 2 — su sistema detecta competitividad y tensión no expresada en el equipo. Capa 3 — está recibiendo la ansiedad colectiva sobre cambios económicos en la organización. Capa 4 — la ansiedad es un impulso evolutivo hacia nuevas capacidades de liderazgo espiritual. Resultado: Ana transforma la ansiedad de "problema a resolver" en "información multidimensional para evolución".</blockquote>',
   '<h4>Ejemplo: Ana y la Ansiedad Inexplicable</h4>\n    <blockquote>Imagina a Ana, ejecutiva de 35 años, que siente una ansiedad intensa sin causa aparente durante una reunión importante. Aplicando el protocolo de cuatro capas: Capa 1 — la ansiedad señala un perfeccionismo que no está alineado con lo que ella es. Capa 2 — su sistema registra la competencia y la tensión no dicha en el equipo. Capa 3 — también le llega la inquietud de toda la organización ante los cambios económicos. Capa 4 — queda una pregunta abierta: ¿qué capacidad nueva le está pidiendo este momento? Resultado: Ana deja de tratar su ansiedad como un problema a eliminar y empieza a leerla como información. Si volviera seguido, sin reunión que la explique, también la escucharía consultando: a veces la ansiedad la manda el cuerpo.</blockquote>\n'
   '    <p>Las cuatro capas se leen con calma, como se lee un mapa. Si alguna vez parece que lo que sientes trae noticias secretas de otros, o que cada número y cada cartel te hablan a ti, eso no es un don: conviene conversarlo con alguien de confianza o con un profesional esa misma semana.</p>'),
  ('<p>En física cuántica, las partículas entrelazadas comparten estados instantáneamente sin importar la distancia. En el campo emocional,',
   '<p>En física, dos partículas entrelazadas siguen respondiendo como un solo sistema aunque estén en extremos opuestos del universo, sin que viaje entre ellas ninguna señal. Entre las personas es una imagen, y nombra bien lo que vivimos: en el campo emocional,'),
  ('<blockquote>Una madre siente ansiedad inexplicable exactamente cuando su hijo, a 3000 kilómetros de distancia, está teniendo un accidente. Su sistema emocional está recibiendo información cuántica a través del entrelazamiento establecido por la conexión amorosa.</blockquote>\n    <p><strong>Protocolo de Verificación:</strong> Registro inmediato de emociones inexplicables intensas. Contacto con familiares relevantes dentro de 24 horas. Correlación de timing entre tu emoción y eventos en sus vidas. Documentación de patrones para desarrollar sensibilidad.</p>',
   '<blockquote>Lo que se midió ocurre en la cercanía, y no es menos asombroso. Cuando una madre y su bebé de tres meses se miran y se sonríen, sus ritmos se coordinan con menos de un segundo de diferencia (Feldman y otros, 2011). El vínculo se aprende cuerpo a cuerpo antes que con palabras, y lo que se aprende así no se olvida con la distancia.</blockquote>\n'
   '    <p><strong>Práctica:</strong> Nota las emociones que te llegan de los tuyos, sin buscarles prueba. ' + LLAMALO + '</p>'),
  ('<blockquote>Un terapeuta comienza a sentir una tristeza profunda durante una sesión sin conexión aparente con su estado personal. Al explorar, descubre que está percibiendo el dolor no procesado de su paciente que aún no ha sido verbalizado.</blockquote>\n    <p><strong>Protocolo para Terapeutas:</strong> Discriminación entre emociones propias y recibidas del paciente. Verificación sutil con el paciente sobre resonancias percibidas. Uso terapéutico de la información sin violar límites. Limpieza energética después de cada sesión.</p>',
   '<blockquote>Un terapeuta comienza a sentir una tristeza profunda durante una sesión sin conexión aparente con su estado personal. Al explorar, descubre que está percibiendo el dolor no procesado de su paciente que aún no ha sido verbalizado.</blockquote>\n'
   '    <p>La clínica lo conoce desde hace mucho. En 1950, la psicoanalista Paula Heimann propuso que lo que siente el analista durante la sesión no es un estorbo sino un instrumento para comprender a su paciente. Y en 1992, Robert Levenson y Anna Ruef midieron algo cercano: quienes mejor reconocían las emociones difíciles de otra persona eran aquellos cuyo cuerpo —el pulso, la piel— se acompasaba con el de ella mientras la miraban.</p>\n'
   '    <p><strong>Protocolo para Terapeutas:</strong> Discriminación entre emociones propias y recibidas del paciente. Verificación sutil con el paciente sobre resonancias percibidas. Uso terapéutico de la información sin violar límites. Supervisión y descanso después de las sesiones que pesan: lo que el terapeuta recibe necesita un lugar donde dejarse. Charles Figley llamó fatiga por compasión (1995) al desgaste de quien acompaña sin ser acompañado.</p>'),
  ('<blockquote>Días antes de eventos significativos, muchas personas sensibles reportan sueños perturbadores o emociones inexplicables. Están recibiendo información sobre patrones que se están organizando en el campo colectivo.</blockquote>',
   '<blockquote>Días antes de eventos significativos, muchas personas sensibles cuentan sueños perturbadores o emociones inexplicables. Para la Psicología Cuántica, es información sobre patrones que se están organizando en el campo colectivo.</blockquote>'),
  ('Versiones futuras del self que buscan emerger.', 'Versiones futuras del yo que buscan emerger.'),
  ('Integrar sabiduría de versiones alternativas del self.</p>',
   'Integrar sabiduría de versiones alternativas del yo.</p>'),
  ('Tomar decisiones que faciliten outcomes óptimos.</p>',
   'Tomar decisiones que faciliten los mejores resultados.</p>\n    <p>' + DEJA_VU + '</p>'),
  ('<p>Las emociones no permanecen contenidas dentro de individuos — se propagan a través del campo cuántico como <strong>ondas de resonancia</strong> que pueden ser detectadas y amplificadas por sistemas emocionales afinados.</p>',
   '<p>Las emociones no permanecen contenidas dentro de individuos — se propagan como <strong>ondas de resonancia</strong> que pueden ser detectadas y amplificadas por sistemas emocionales afinados. La psicología le puso nombre en 1994: Elaine Hatfield, John Cacioppo y Richard Rapson llamaron contagio emocional a la manera en que, sin darnos cuenta, imitamos el gesto, la voz y la postura de quien tenemos enfrente, y con ellos su ánimo.</p>'),
  ('<h3>Tecnología 1: Scanner Emocional Cuántico</h3>', '<h3>Tecnología 1: Escáner Emocional Cuántico</h3>'),
  ('<li>Scan: "¿Qué información está transmitiendo mi sistema emocional ahora?"</li>', '<li>Escucha: "¿Qué información está transmitiendo mi sistema emocional ahora?"</li>'),
  ('<li>Recibe insights sin juzgar</li>\n      <li>Integra información relevante en decisiones presentes</li>\n    </ol>',
   '<li>Recibe las comprensiones sin juzgar</li>\n      <li>Integra información relevante en decisiones presentes</li>\n    </ol>\n'
   '    <p>Si una emoción intensa llega una y otra vez sin motivo, además de escucharla se consulta: a veces la mueve el cuerpo.</p>'),
  ('<p><strong>Proceso de verificación:</strong> Registro inmediato. Contacto apropiado con la persona relevante. Verificación sutil sin violar privacidad. Documentación de correlaciones.</p>',
   '<p><strong>Qué hacer:</strong> Si el impulso es contactar a alguien, contáctalo. Lo que se cultiva es el vínculo, no la prueba.</p>'),
  ('<p><em>"Las emociones son el lenguaje a través del cual el universo se comunica directamente con nuestra conciencia."</em></p>',
   '<p><em>"Las emociones son el lenguaje a través del cual el universo se comunica directamente con nuestra conciencia."</em></p>\n'
   '    <!-- Vuelta de la puerta de Origen VI.7 (noviembre de 2026). -->\n'
   '    <p class="viene">Viene de <em>El Vacío Fértil</em>: la puerta hacia el Ingeniero de Emociones que soñaba <a class="vuelta" href="../Libro_06/nodo_07.html">su último nodo</a> se abre aquí.</p>'),
 ],
 puertas=[portal('Que una emoción, dejada sola, dura lo que dura una ola, y que lo que se queda meses no es la emoción sino algo que la vuelve a encender cada vez, está en <em>Atravesar</em>, Libro 11 del Portal Público, Umbral I: «La ola».',
                 '11_Atravesar/umbral_1_lo_que_pasa_y_lo_que_se_queda.html')],
)

# ---------------------------------------------------------------- Nodo 3
R['nodo_03.html'] = dict(
 reemplazos=[
  ('<li>🎯 Inteligencia Intuitiva vs. Inteligencia Analítica</li>', '<li>🎯 Inteligencia Intuitiva e Inteligencia Analítica</li>'),
  ('<li>Cada decisión "racional" está fundamentalmente influenciada por información emocional</li>\n      <li>El corazón contiene 40,000 neuronas que procesan información independientemente</li>\n      <li>Los centros emocionales del cerebro evalúan información más rápido que los centros racionales</li>',
   '<li>Cada decisión "racional" está fundamentalmente influenciada por información emocional (Antonio Damasio, <em>El error de Descartes</em>, 1994)</li>\n      <li>El corazón tiene su propia red de neuronas, unas cuarenta mil según J. Andrew Armour (1991), que la llamó el «pequeño cerebro» del corazón</li>\n      <li>Los centros emocionales del cerebro evalúan información más rápido que los centros racionales (Joseph LeDoux, 1996)</li>'),
  ('<p>El corazón contiene aproximadamente <strong>40,000 neuronas</strong> — un sistema nervioso sofisticado que procesa información independientemente del cerebro craneal. Estas neuronas cardíacas no solo reciben información del cerebro — <strong>envían más información al cerebro de la que reciben</strong>.</p>',
   '<p>El corazón tiene una red de unas <strong>cuarenta mil neuronas</strong> — un sistema nervioso propio que ajusta el latido sin esperar órdenes del cerebro craneal. Y el diálogo es de ida y vuelta: la mayoría de las fibras del nervio vago suben del cuerpo al cerebro, de modo que <strong>el cerebro escucha al corazón tanto como le habla</strong>.</p>'),
  ('<li><strong>Electromagnético:</strong> Campo 5000x más potente que el cerebral, sincroniza frecuencias neuronales</li>',
   '<li><strong>Electromagnético:</strong> La señal eléctrica del corazón es la más intensa del cuerpo; se registra desde la piel, y por eso existe el electrocardiograma</li>'),
  (('<h4>Evidencia Científica — Instituto HeartMath</h4>', '<li>La coherencia individual influencia la coherencia de grupos enteros</li>\n    </ul>'),
   '<h4>Lo que la Ciencia Midió</h4>\n'
   '    <p>La variabilidad del ritmo cardíaco —la manera en que el pulso se acelera al inspirar y se aquieta al espirar— es una de las señales más finas de la salud del sistema nervioso. Respirar unas seis veces por minuto la lleva a su mayor amplitud, y Paul Lehrer y Richard Gevirtz (2014) reunieron los estudios de ese entrenamiento: encontraron alivio en la ansiedad, la depresión y el asma, entre otros malestares. En 2001, Luciano Bernardi y su equipo vieron que el avemaría en latín y un mantra del yoga llevan la respiración a casi seis por minuto: las tradiciones habían encontrado el ritmo antes que los laboratorios.</p>'),
  ('<p>La <strong>coherencia cardio-cerebral</strong> no es simplemente una sincronización de ritmos — es un <strong>estado cuántico</strong> donde los dos sistemas',
   '<p>La <strong>coherencia cardio-cerebral</strong> no es simplemente una sincronización de ritmos: la Psicología Cuántica la ve como un <strong>estado de unidad</strong> donde los dos sistemas'),
  ('<li>Acceso a información no-local — conocimiento que no proviene de experiencia personal</li>',
   '<li>La sensación de acceder a un conocimiento que no proviene de la experiencia personal</li>'),
  ('<h4>Técnica Básica: Heart Focus (5 minutos)</h4>', '<h4>Técnica Básica: Atención en el Corazón (5 minutos)</h4>'),
  ('<li>Mantén ritmo consistente sin forzar</li>\n    </ol>',
   '<li>Mantén ritmo consistente sin forzar</li>\n    </ol>\n'
   '    <p>Cinco segundos al inspirar y cinco al espirar dan seis respiraciones por minuto: el ritmo de la coherencia. Si en algún momento te falta el aire o te mareas, vuelve a tu respiración natural.</p>'),
  ('<p>El campo electromagnético del corazón forma un <strong>torus</strong> — una geometría sagrada que se extiende hasta 8 pies (2.4 metros) alrededor del cuerpo. Cuando la mente se alinea con este campo, crea una geometría de información coherente.</p>',
   '<p>En la imagen de esta tradición, el campo del corazón forma un <strong>toroide</strong> — una geometría sagrada que envuelve el cuerpo y vuelve sobre sí misma. Cuando la mente se alinea con este campo, crea una geometría de información coherente.</p>'),
  ('<p>La integración óptima mente-corazón sigue la <strong>proporción áurea</strong>',
   '<p>Como imagen, la integración mente-corazón sigue la <strong>proporción áurea</strong>'),
  ('<p><strong>Nivel 3 — Insight Expandido:</strong>', '<p><strong>Nivel 3 — Comprensión Expandida:</strong>'),
  ('El insight expandido genera estado emocional más refinado.', 'La comprensión expandida genera un estado emocional más refinado.'),
  ('<h2>4. Inteligencia Intuitiva vs. Inteligencia Analítica</h2>', '<h2>4. Inteligencia Intuitiva e Inteligencia Analítica</h2>'),
  ('validación cruzada entre insights y análisis', 'validación cruzada entre comprensiones y análisis'),
  ('<p>La intuición no es "corazonada" vaga — es <strong>procesamiento de información cuántica</strong> que opera más rápido que el pensamiento lineal. Cuando el sistema mente-corazón está entrelazado, puede acceder instantáneamente a información que normalmente requeriría años de análisis.</p>',
   '<p>La intuición no es "corazonada" vaga — es <strong>procesamiento de información</strong> que opera más rápido que el pensamiento lineal. Herbert Simon, premio Nobel, lo dijo en una frase (1992): la intuición es reconocimiento. Cuando el sistema mente-corazón está entrelazado, puede reconocer en un instante lo que el análisis tardaría años en reconstruir.</p>\n'
   '    <p>El cuerpo participa de ese reconocimiento. En 1997, Antoine Bechara y el equipo de Antonio Damasio vieron que la piel de quienes jugaban a las cartas reaccionaba ante las pilas que hacían perder antes de que supieran decir por qué. ' + DECISIONES + '</p>'),
  ('Conocimiento inmediato sobre cursos de acción óptimos. Timing perfecto para decisiones importantes.', 'Conocimiento inmediato sobre cursos de acción óptimos. El momento justo para actuar.'),
  ('Detección de autenticidad vs. incongruencia.', 'Detección de autenticidad e incongruencia.'),
  ('Recepción de guidance que trasciende perspectiva personal.', 'Recepción de una orientación que trasciende la perspectiva personal.'),
  ('<li>Permite que insights emerjan sin forzar</li>', '<li>Permite que las comprensiones emerjan sin forzar</li>'),
  ('Recibe guidance sobre tu rol en la evolución colectiva. Usa tu coherencia para enviar sanación a personas específicas.</p>',
   'Recibe orientación sobre tu rol en la evolución colectiva. Piensa con bondad en personas específicas y deséales el bien: unos minutos así, frente a la foto de un desconocido, bastaron para que la gente se sintiera más unida a él y a los demás (Hutcherson, Seppälä y Gross, 2008).</p>'),
  ('<p>Cuando dos o más personas establecen coherencia cardio-cerebral simultáneamente, emergen campos de comunicación cuántica que trascienden el intercambio verbal convencional.</p>',
   '<p>Cuando dos o más personas establecen coherencia cardio-cerebral simultáneamente, emergen campos de comunicación cuántica que trascienden el intercambio verbal convencional. Algo de esto se midió: en 2010, Greg Stephens, Lauren Silbert y Uri Hasson registraron el cerebro de quien contaba una historia y el de quienes la escuchaban. Los dos se acompasaban, y cuanto más se acompasaban, mejor la comprendían.</p>'),
  ('<li>Emergencia de insights que ninguno tenía previamente</li>', '<li>Emergencia de comprensiones que ninguno tenía previamente</li>'),
  (('<p><strong>Resonancia Cardíaca:</strong> El campo electromagnético coherente', 'aumento de claridad mental en grupos donde uno mantiene coherencia.</p>'),
   '<p><strong>Resonancia Cardíaca:</strong> Una presencia serena se contagia: la respiración lenta, la voz calma y el gesto quieto ayudan a otros sistemas nerviosos a encontrar su ritmo. Quienes cuidan niños lo saben desde siempre, y la psicología lo llama corregulación. Aplicaciones: acompañar a niños estresados con la propia calma, reducir la ansiedad de pacientes a través de una presencia coherente, facilitar estados receptivos en quienes consultan.</p>\n'
   '    <p><strong>Sincronía Neural:</strong> En 2017, Suzanne Dikker y su equipo registraron la actividad cerebral de un aula entera de secundaria: cuanto más atentos y comprometidos estaban los alumnos, más se sincronizaban entre sí. Resultados observados en la práctica: reducción espontánea de ansiedad en personas cercanas, aumento de claridad mental en grupos donde uno mantiene coherencia.</p>'),
  ('emerge una forma de consciousness que trasciende', 'emerge una forma de conciencia que trasciende'),
 ],
 puertas=[portal('Que un hombre que había perdido la emoción que acompaña al pensamiento ya no podía decidir nada, y que la piel de quienes jugaban a las cartas sabía qué mazos evitar antes que ellos, está en <em>El no saber</em>, Libro 31 del Portal Público, Umbral V: «El cuerpo sabía antes».',
                 '31_El_No_Saber/umbral-05.html')],
)

# ---------------------------------------------------------------- Nodo 4
# Lo que La Corriente (Arquitectura, Libro 10) cita de este nodo conserva su letra: la introducción, los
# campos familiares, el protocolo de identificación, el epígrafe y la conclusión. La primera pregunta del
# protocolo pasa a la grafía con que La Corriente la cita.
R['nodo_04.html'] = dict(
 reemplazos=[
  ('<p>El biólogo Rupert Sheldrake propuso que los patrones de organización en la naturaleza son mantenidos por <strong>campos morfogenéticos</strong> — campos de información que preservan y transmiten estructuras organizacionales a través del tiempo y el espacio.</p>',
   '<p>El biólogo Rupert Sheldrake propuso en <em>Una nueva ciencia de la vida</em> (1981) que los patrones de organización en la naturaleza son mantenidos por <strong>campos morfogenéticos</strong> — campos de información que preservan y transmiten estructuras organizacionales a través del tiempo y el espacio. La ciencia trata su propuesta hasta hoy como una hipótesis sin confirmar. La experiencia que señala, en cambio, no necesita esa teoría: cualquiera que haya entrado en una sala donde todos estaban nerviosos sabe que el ánimo y las ideas no se quedan quietos dentro de cada cabeza.</p>'),
  ('<p><strong>Alcance:</strong> 3–7 generaciones. <strong>Contenido:</strong> Patrones de trauma',
   '<p><strong>Alcance:</strong> Varias generaciones. <strong>Contenido:</strong> Patrones de trauma'),
  ('<blockquote>Una mujer experimenta ansiedad inexplicable', '<blockquote>Imagina a una mujer que experimenta ansiedad inexplicable'),
  ('<strong>Influencia:</strong> Worldview, expectativas sociales', '<strong>Influencia:</strong> Visión del mundo, expectativas sociales'),
  ('<p>Los campos morfogenéticos explican fenómenos que la genética convencional no puede abordar:</p>\n    <p><strong>Trauma Heredado:</strong> Nietos de sobrevivientes del Holocausto muestran patrones de estrés específicos.',
   '<p>Para la Psicología Cuántica, los campos morfogenéticos ayudan a pensar fenómenos que la genética sola no alcanza a explicar:</p>\n    <p><strong>Trauma Heredado:</strong> Desde los años noventa, Rachel Yehuda estudia a los hijos de sobrevivientes del Holocausto, y encontró en ellos marcas biológicas del estrés que vivieron sus padres; cómo se transmiten —por la crianza, por el cuerpo o por los dos caminos— sigue en estudio.'),
  ('la calidad de nuestra conciencia afecta directamente la evolución de nuestra especie.</p>',
   'la calidad de nuestra conciencia influye en la evolución de nuestra especie.</p>'),
  (('<h3>El Principio del 1%</h3>', '<li>70,000 individuos iluminados pueden elevar la conciencia planetaria</li>\n    </ul>'),
   '<h3>El Principio de la Masa Crítica</h3>\n'
   '    <p>La intuición de que unos pocos pueden cambiar el tono de todos tiene linaje y tiene medida. En los años setenta, el movimiento de Meditación Trascendental de Maharishi Mahesh Yogi anunció que bastaba que el uno por ciento de una ciudad meditara para cambiar su clima; lo llamó efecto Maharishi, y queda como visión. La medida llegó después: en 2018, Damon Centola y su equipo mostraron en un experimento que, cuando una minoría comprometida alcanza una cuarta parte de un grupo, la convención de todo el grupo cambia, y que por debajo de ese umbral los esfuerzos parecen inútiles aunque estén a un paso de lograrlo.</p>\n'
   '    <ul>\n'
   '      <li>Pocos que se aquietan pueden cambiar el tono de una sala</li>\n'
   '      <li>Una minoría que no cede puede cambiar una costumbre</li>\n'
   '      <li>Muchos despiertos pueden elevar la conciencia planetaria</li>\n'
   '    </ul>'),
  ('<p><strong>Contribuciones degradantes:</strong> Pensamientos de miedo, odio, separación fortalecen campos de trauma colectivo.</p>',
   '<p><strong>Contribuciones que alimentan el trauma colectivo:</strong> El miedo que se contagia sin ser escuchado, el odio que se repite, la reacción que se suma sin mirarse. Sentir miedo no es una falta: lo que alimenta la corriente es la reacción que se agrega a ella.</p>'),
  ('<li>¿Qué patrones de pensamiento/emoción son verdaderamente míos vs. heredados/culturales?</li>',
   '<li>¿Qué patrones de pensamiento y emoción son verdaderamente míos, y cuáles heredados o culturales?</li>'),
  ('<li><strong>Anclar</strong> la nueva frecuencia en el presente</li>\n    </ol>',
   '<li><strong>Anclar</strong> la nueva frecuencia en el presente</li>\n    </ol>\n'
   '    <p>Se recorre como un gesto simbólico, a la manera de las tradiciones que honran a los ancestros. ' + HONRAR + '</p>'),
  ('<li><strong>Embodir</strong> conscientemente frecuencias más elevadas</li>', '<li><strong>Encarnar</strong> conscientemente frecuencias más elevadas</li>'),
  ('<li><strong>Magnetizar</strong> otros individuos que resuenan con la nueva frecuencia</li>', '<li><strong>Atraer</strong> a otros individuos que resuenan con la nueva frecuencia</li>'),
  ('Bell y Gray (teléfono).</p>',
   'Bell y Gray (teléfono). En 1922, William Ogburn y Dorothy Thomas reunieron ciento cuarenta y ocho descubrimientos hechos así, por separado, y Robert K. Merton mostró después que en la historia de la ciencia los descubrimientos simultáneos son la regla.</p>'),
  ('Desarrollar experticia en el campo específico.', 'Desarrollar pericia en el campo específico.'),
  ('Recepcionar sin forzar, permitir que la información emerja.', 'Recibir sin forzar, permitir que la información emerja.'),
  ('Testear practicidad y aplicabilidad.', 'Probar su practicidad y su aplicación.'),
  ('Observar qué campos están influyendo tus pensamientos/emociones.', 'Observar qué campos están influyendo en tus pensamientos y emociones.'),
  ('<p><em>"Este nodo no es solo información sobre campos morfogenéticos — es un campo morfogenético en sí mismo. Cada lectura consciente activa códigos dormentes de capacidad morfogenética."</em></p>',
   '<p><em>"Cada comprensión que se vuelve vida es también un campo: lo que uno aprende a sostener queda disponible para otros."</em></p>'),
 ],
 puertas=[arq('Que la primera pregunta del protocolo de este nodo —qué es mío y qué heredé o tomé de mi cultura— sostiene la historia de una directora de escuela que ve llegar un rumor por el grupo de padres, se despliega en <em>La Corriente</em>, Libro 10 de <em>Arquitectura del Destino</em>, Umbral I: «¿Es mío?».',
              'libro-10-la-corriente/L10-U1.html')],
)

# ---------------------------------------------------------------- Nodo 5
R['nodo_05.html'] = dict(
 reemplazos=[
  ('<p class="node-quote">"Lo que duele no es lo que pasó, sino el eco atrapado en una frecuencia vieja. El trauma no quiere destruirte: quiere expandirte, si lo escuchas con una conciencia que ya no necesita protegerse."</p>',
   '<p class="node-quote">"Lo que duele no es solo lo que pasó, sino el eco atrapado en una frecuencia vieja. Escuchado con una conciencia que ya no necesita protegerse, ese eco puede volverse expansión."</p>'),
  ('La <strong>Sanación Cuántica</strong> revela que el trauma no es un evento fijo del pasado, sino un <strong>patrón de colapso</strong> que se re-crea momento a momento en el presente.</p>',
   'La <strong>Sanación Cuántica</strong> revela que el trauma no es solo un evento fijo del pasado: es también un <strong>patrón de colapso</strong> que se re-crea momento a momento en el presente.</p>'),
  ('<p>Cuando comprendemos los principios cuánticos de la conciencia, la sanación puede ocurrir instantáneamente a través de <strong>reorganizaciones fundamentales</strong> del campo de información personal.</p>',
   '<p>Cuando comprendemos los principios cuánticos de la conciencia, la sanación se vuelve posible a través de <strong>reorganizaciones fundamentales</strong> del campo de información personal. A veces el cambio llega de golpe: Bruce Ecker y su equipo (2012) describieron cómo un aprendizaje emocional antiguo puede desarmarse de una vez cuando se lo vuelve a sentir junto a una experiencia que lo contradice. Casi siempre, en cambio, lleva tiempo. Las dos cosas son sanación, y ninguna es más honda que la otra.</p>\n'
   '    <p>Si el trauma se vuelve trastorno —recuerdos que irrumpen, noches en vela, el cuerpo siempre en alerta—, se trata, y hay tratamientos que funcionan. Ese cuidado y esta mirada no compiten: se suman.</p>'),
  ('el trauma no es una "herida" que necesita "sanar" — es <strong>información que se ha cristalizado</strong>',
   'el trauma no es solo una "herida" que necesita "sanar": es también <strong>información que se ha cristalizado</strong>'),
  ('<li><strong>Información Energética:</strong> Contracciones en el campo electromagnético personal</li>',
   '<li><strong>Información Energética:</strong> Contracciones en el campo energético personal</li>'),
  ('<p>El trauma se perpetúa no porque el evento pasado "cause" síntomas presentes, sino porque la conciencia <strong>colapsa repetitivamente</strong> en los mismos patrones de información. Cada vez que ocurre este colapso, el patrón se refuerza y se vuelve más probable en futuros momentos.</p>',
   '<p>El trauma se perpetúa no solo porque el evento pasado haya dejado su marca, sino porque la conciencia <strong>colapsa repetitivamente</strong> en los mismos patrones de información. Cada vez que ocurre este colapso, el patrón se refuerza y se vuelve más probable en futuros momentos. Pierre Janet lo vio a fines del siglo XIX: el recuerdo traumático no se cuenta como una historia, se repite como una escena.</p>'),
  ('La transformación puede ser instantánea si se reorganiza la información fundamental.</p>',
   'La transformación puede llegar en un instante, cuando se reorganiza la información fundamental, o paso a paso: el ritmo lo pone quien sana.</p>'),
  ('<p>Desde una perspectiva cuántica, el pasado no existe como realidad fija — existe como <strong>información activa</strong> en el presente. Cambiar la información presente <strong>literalmente</strong> cambia el pasado.</p>',
   '<p>Lo que pasó, pasó. Pero el pasado no vive en nosotros como un archivo fijo: existe como <strong>información activa</strong> en el presente, porque el recuerdo se reconstruye cada vez que se evoca. En 2000, Karim Nader, Glenn Schafe y Joseph LeDoux mostraron que un recuerdo de miedo, al ser evocado, queda abierto por un tiempo antes de guardarse otra vez, y que en esa ventana puede guardarse distinto. Cambiar la información presente <strong>literalmente</strong> cambia el recuerdo, y con él, el peso del pasado.</p>'),
  ('<li>Anclar el nuevo patrón en el presente</li>\n    </ol>',
   '<li>Anclar el nuevo patrón en el presente</li>\n    </ol>\n'
   '    <p>En la clínica tiene nombre: Arnoud Arntz y sus colegas llaman reescritura en imaginación a volver a una escena dolorosa y, desde el adulto de hoy, cambiar su final. Con los recuerdos más duros se hace junto a un terapeuta.</p>'),
  ('<blockquote>Un paciente siente rabia emergente hacia un familiar. En lugar de actuarla o reprimirla, la observa como información neutra desde múltiples perspectivas: "Esta es energía en movimiento, esta es información ancestral, esta es una invitación a expandir mi capacidad de amor."</blockquote>',
   '<blockquote>Un paciente siente rabia emergente hacia un familiar. En lugar de actuarla o reprimirla, la observa como información neutra desde múltiples perspectivas: "Esta es energía en movimiento, esta es información ancestral, esta es una invitación a expandir mi capacidad de amor."</blockquote>\n'
   '    <p>Si ese familiar dañó, la rabia también dice algo verdadero, y merece ser escuchada. ' + HONRAR + '</p>'),
  ('<li>Reconocimiento: "Esto es información, no realidad"</li>', '<li>Reconocimiento: "Esto es información de entonces, no lo que ocurre ahora"</li>'),
  ('<li>Integración Energética: Siente cómo se fusionan en tu campo presente</li>\n    </ol>',
   '<li>Integración Energética: Siente cómo se fusionan en tu campo presente</li>\n    </ol>\n'
   '    <p>Richard Schwartz, creador de los Sistemas de Familia Interna (1995), llama exiliadas a esas partes y enseña que no hay partes malas: cada una protege algo. Si al acercarte a una de ellas aparece un dolor que desborda, se vuelve al presente y se sigue acompañado.</p>'),
  (('<li>Sintonización: Conecta con la frecuencia específica del trauma</li>', '<li>Anclaje: Establece la nueva frecuencia en tu sistema</li>\n    </ol>'),
   '<li>Sintonización: Conecta con la frecuencia específica del trauma, tocándola apenas</li>\n'
   '      <li>Dosificación: Quédate solo un momento y vuelve a un lugar del cuerpo que esté tranquilo —los pies, las manos, la respiración—; ir y venir enseña al sistema que puede tocar lo difícil y regresar</li>\n'
   '      <li>Inversión: Imagina la frecuencia invirtiendo su polaridad</li>\n'
   '      <li>Elevación: Sube la frecuencia a una octava más alta</li>\n'
   '      <li>Anclaje: Establece la nueva frecuencia en tu sistema</li>\n'
   '    </ol>\n'
   '    <p>Así trabajan Peter Levine, que llamó titulación a acercarse al trauma de a gotas (<em>Despertando al tigre</em>, 1997), y Daniel Siegel, que habló de una ventana de tolerancia (1999): dentro de ella se puede sentir y pensar a la vez; fuera, el cuerpo se desborda o se apaga. La sanación ocurre dentro de la ventana, y con la práctica la ventana se agranda.</p>\n'
   '    <p>Si al practicar aparecen pánico, la sensación de no estar en tu cuerpo o recuerdos que irrumpen como si ocurrieran ahora, abre los ojos, apoya los pies y nombra cinco cosas que ves. El trauma grande no se recorre a solas: se trabaja con alguien formado.</p>'),
  ('La sanación individual puede literalmente <strong>transformar patrones ancestrales</strong> hacia atrás en el tiempo.</p>',
   'La sanación individual puede <strong>transformar patrones ancestrales</strong>: hacia adelante, en lo que se transmite a los que vienen, y, en la visión de muchas tradiciones, también hacia atrás en el tiempo.</p>'),
  ('Envía frecuencias de amor, comprensión y perdón hacia tus ancestros.', 'Envía frecuencias de amor, comprensión y, si llega, perdón hacia tus ancestros; si en tu línea hubo abuso, el perdón no obliga.'),
  ('<li>Sueños o visiones relacionadas con eventos colectivos pasados</li>\n    </ul>',
   '<li>Sueños o visiones relacionadas con eventos colectivos pasados</li>\n    </ul>\n'
   '    <p>Cuando esos sueños o imágenes no dejan dormir, o empiezan a parecer mensajes dirigidos a ti, se conversan con un profesional.</p>'),
  ('Identifica cuándo estás procesando trauma colectivo vs. personal.', 'Identifica cuándo estás procesando trauma colectivo o personal.'),
  ('La sustancia o comportamiento adictivo es un intento de alcanzar conexión, paz, vitalidad o trascendencia.</p>',
   'La sustancia o comportamiento adictivo es un intento de alcanzar conexión, paz, vitalidad o trascendencia.</p>\n'
   '    <p>La intuición tiene linaje. En 1961, Carl Jung le escribió a Bill Wilson, uno de los fundadores de Alcohólicos Anónimos, que la sed de alcohol de un antiguo paciente suyo era, en un nivel bajo, el equivalente de la sed espiritual de nuestro ser por la totalidad, y cerró la carta con una fórmula latina: <em>spiritus contra spiritum</em>. Gabor Maté, médico en el barrio más castigado de Vancouver, lo dijo a su manera (2008): la pregunta no es por qué la adicción, sino por qué el dolor.</p>'),
  ('Desarrolla confianza en tu capacidad natural de generar estos estados.</p>',
   'Desarrolla confianza en tu capacidad natural de generar estos estados. Dejar de golpe el alcohol, los tranquilizantes como las benzodiacepinas y algunas otras sustancias puede ser peligroso para el cuerpo: se hace con un médico. Y nadie sale solo de una adicción: la compañía de otros que pasaron por lo mismo es de lo que más ayuda.</p>'),
  ('Reconoce cuándo estás activado por el patrón traumático vs. respondiendo desde tu coherencia.', 'Reconoce cuándo estás activado por el patrón traumático y cuándo respondes desde tu coherencia.'),
  ('Comunica desde la frecuencia de tu esencia, no desde patrones activados.</p>',
   'Comunica desde la frecuencia de tu esencia, no desde patrones activados. John Gottman observó en su laboratorio que, cuando el pulso de uno de los dos se dispara en medio de una discusión, ya no puede escuchar; propuso hacer una pausa de al menos veinte minutos, ocuparse de otra cosa y volver.</p>'),
  ('Usa tu coherencia para crear campo seguro para que el otro procese trauma.</p>',
   'Tu calma puede ser un lugar seguro para el otro, y aun así nadie es terapeuta de su pareja: lo más hondo se trabaja también con ayuda. Si en la relación hay miedo o violencia, la seguridad va primero, y se pide ayuda.</p>'),
  ('desregulación del sistema nervioso y fragmentación de la consciencia corporal.</p>',
   'desregulación del sistema nervioso y fragmentación de la consciencia corporal. Bessel van der Kolk lo resumió en el título de su libro: <em>El cuerpo lleva la cuenta</em> (2014).</p>'),
  ('Permite que el cuerpo "respire" la nueva información hacia cada célula.</p>',
   'Permite que el cuerpo "respire" la nueva información hacia cada célula. La respiración lenta del tercer nodo es la base; las respiraciones intensas o con retención no son para un trauma reciente.</p>'),
  ('Permite que el movimiento complete ciclos de activación incompletos.</p>',
   'Permite que el movimiento complete ciclos de activación incompletos. Peter Levine observó que los animales salvajes, pasado el peligro, tiemblan y se sacuden hasta descargar la activación, y que los humanos aprendemos a frenar ese temblor. Si el movimiento trae recuerdos que desbordan, vuelve a los pies.</p>'),
  ('Procesa cualquier información traumática que emergió durante el día. Programa tu sistema para continuar sanación durante el sueño.</p>',
   'Procesa cualquier información traumática que emergió durante el día. Después, confía en el sueño: Matthew Walker y Els van der Helm (2009) lo describieron como una terapia nocturna, en la que el cerebro vuelve sobre lo vivido con menos química de estrés y le quita filo a la emoción. Si el insomnio o las pesadillas se repiten, se consulta.</p>'),
  ('<strong>no es una patología que debe ser eliminada, sino información que busca ser integrada</strong> para facilitar evolución acelerada de la conciencia.</p>',
   'más allá del diagnóstico y del tratamiento, que cuando hacen falta no se postergan, el trauma es <strong>información que busca ser integrada</strong>, y en esa integración la conciencia se expande.</p>'),
  ('información sobre capacidades de conciencia que están tratando de emerger.</p>',
   'información sobre capacidades de conciencia que están tratando de emerger.</p>\n'
   '    <p>Richard Tedeschi y Lawrence Calhoun le pusieron nombre en los años noventa: crecimiento postraumático. Y precisaron algo que la Psicología Cuántica hace suyo: el crecimiento no lo produce el golpe, sino lo que la persona hace después, muchas veces con alguien que escucha. Lo que ocurrió no se vuelve bueno; lo que crece, crece en quien lo atraviesa.</p>'),
  ('<p><em>"Si has procesado esta información con corazón abierto, ya has iniciado procesos de reorganización en tu sistema. El trauma no es tu enemigo — es tu maestro evolutivo, esperando ser reconocido y transmutado."</em></p>',
   '<p><em>"El trauma no es tu enemigo: puede volverse tu maestro, cuando lo escuchas acompañado y a tu ritmo."</em></p>'),
 ],
 puertas=[
  arq('Que unos padres que habían perdido a un hijo no encontraron nada bueno en esa muerte y, aun así, muchos de ellos crecieron, y que el crecimiento no lo da el golpe sino lo que uno hace después, se despliega en <em>La Grieta</em>, Libro 5 de <em>Arquitectura del Destino</em>, Umbral VI: «Lo que encontraron en Charlotte».',
      'libro-05-la-grieta/L05-U6.html'),
  portal('Que un hombre que llevaba meses sin beber entendió, en el vestíbulo de un hotel de Akron, que no necesitaba un trago sino hablar con otro alcohólico, y que de esa conversación nació Alcohólicos Anónimos, está en <em>Los muchos</em>, Libro 35 del Portal Público, Umbral IV: «El vestíbulo».',
         '35_Los_Muchos/umbral-04.html'),
 ],
)

# ---------------------------------------------------------------- Nodo 6
# El nodo obedece a su propia introducción («más allá del pensamiento mágico») y a sus mejores frases
# («esto o algo mejor», «claro sobre qué quieres, flexible sobre cómo llega», «Manifestar no es atraer
# lo que quiero, sino convertirme en quien soy…»).
R['nodo_06.html'] = dict(
 reemplazos=[
  ('no es sobre controlar outcomes externos, sino sobre <strong>participar skilfully</strong> en el proceso',
   'no es sobre controlar resultados externos, sino sobre <strong>participar con destreza</strong> en el proceso'),
  ('<li><strong>Conciencia Observadora:</strong> El factor que determina qué posibilidades colapsan</li>',
   '<li><strong>Conciencia Observadora:</strong> El factor que inclina qué posibilidades colapsan</li>'),
  ('<li><strong>Aceptación de Timing:</strong> Permitir', '<li><strong>Aceptación de los Tiempos:</strong> Permitir'),
  ('<p>La manifestación efectiva sigue la geometría del <strong>torus</strong>', '<p>La manifestación efectiva sigue la geometría del <strong>toroide</strong>'),
  ('<blockquote>María visualiza diariamente su sanación completa, siente la vitalidad en su cuerpo, y toma acciones alineadas (nutrición, ejercicio, descanso). En seis meses, sus análisis médicos muestran reversión completa de su condición.</blockquote>',
   '<blockquote>En 1992, Guang Yue y Kelly Cole pidieron a un grupo de voluntarios que, durante cuatro semanas, solo imaginaran que contraían con todas sus fuerzas un músculo del dedo meñique. Al terminar, la fuerza de ese dedo había crecido un 22 %; la de quienes lo habían ejercitado de verdad, un 30 %. La imaginación no reemplazó al ejercicio, pero hizo mucho más de lo que nadie esperaba.</blockquote>\n'
   '    <p>Importa también qué se imagina. En 1999, Lien Pham y Shelley Taylor vieron que los estudiantes que cada día se imaginaban estudiando —dónde, cuándo, con qué materiales— rendían mejor en el examen que quienes se imaginaban recibiendo la nota soñada. Imaginar el camino rinde más que imaginar la meta.</p>'),
  ('<blockquote>Un equipo de trabajo establece intención colectiva', '<blockquote>Por ejemplo, un equipo de trabajo establece una intención colectiva'),
  ('<blockquote>Un activista social rinde completamente su agenda personal al servicio planetario. "Imposiblemente", aparecen financiamiento masivo, colaboradores expertos y plataformas mediáticas que amplifican su mensaje globalmente.</blockquote>',
   '<blockquote>El 5 de junio de 1977, Día Mundial del Medio Ambiente, Wangari Maathai y un grupo de mujeres plantaron siete árboles en un parque de las afueras de Nairobi. No había financiamiento masivo ni plataformas mediáticas: había una intención al servicio de la tierra y de las mujeres de Kenia, y décadas de trabajo, persecución incluida. El Movimiento Cinturón Verde que nació ese día plantó más de cincuenta millones de árboles, y en 2004 Maathai recibió el Premio Nobel de la Paz. Lo "imposible" llegó, y llegó caminando.</blockquote>'),
  ('Identifica y transmute creencias limitantes', 'Identifica y transmuta creencias limitantes'),
  ('Establece timing flexible: "esto o algo mejor".', 'Establece plazos flexibles: "esto o algo mejor".'),
  ('Refina la intención basado en nueva información recibida. Mantén flexibilidad sobre cómo se manifiesta, rigidez sobre por qué.',
   'Refina la intención a la luz de la nueva información recibida. Mantén flexibilidad sobre cómo se manifiesta, firmeza sobre por qué.'),
  ('<p><strong>Reconocimiento de Perfección Fundamental:</strong> Reconoce que la salud perfecta ya existe como posibilidad cuántica. Identifica la información que está creando la experiencia de enfermedad.</p>',
   '<p><strong>Reconocimiento de lo que Sostiene:</strong> Reconoce lo que en tu cuerpo sigue funcionando cada día sin que se lo pidas. No busques en ti la causa de una enfermedad: sentir no es causar. ' + SENTIR + '</p>'),
  ('Ve el sistema inmunológico funcionando óptimamente. Siente la energía fluyendo libremente a través de todo el cuerpo.</p>',
   'Ve el sistema inmunológico funcionando óptimamente. Siente la energía fluyendo libremente a través de todo el cuerpo. La visualización acompaña, no cura: la medicina de hoy la usa para aliviar el miedo y el dolor, junto al tratamiento.</p>'),
  ('Agradece al cuerpo por todas las maneras en que te está sirviendo.</p>',
   'Agradece al cuerpo por todas las maneras en que te está sirviendo. Una frase verdadera sirve más que una afirmación de salud perfecta: "Este cuerpo hace lo que puede, y yo lo acompaño".</p>\n'
   '    <p>' + ACOMPANA + ' ' + HOY + '</p>'),
  ('Cuando operas desde abundancia, atraes experiencias abundantes. La escasez es una ilusión creada por desconexión del flujo universal.</p>',
   'Cuando operas desde abundancia, atraes experiencias abundantes. Pero la escasez real existe, y no es culpa de quien la vive. Sendhil Mullainathan y Eldar Shafir (2013) mostraron que la falta de dinero o de tiempo estrecha la atención y consume la mente: no es un defecto de carácter, es lo que la escasez hace con cualquiera. Por eso la abundancia empieza por lo que sí hay.</p>'),
  ('Mientras más sirves, más recursos fluyen hacia ti para expandir tu servicio.</p>',
   'Mientras más sirves, más se ensancha lo que fluye hacia ti para expandir tu servicio, y no siempre en forma de dinero.</p>'),
  ('<li>Actúa como si ya tuvieras los recursos necesarios</li>\n    </ol>',
   '<li>Actúa con la confianza de quien ya tiene lo necesario, no con su gasto: ninguna intención justifica endeudarse</li>\n    </ol>\n'
   '    <p>El quinto paso tiene un ejemplo célebre. En 1976, el economista Muhammad Yunus prestó de su bolsillo veintisiete dólares a cuarenta y dos personas de Jobra, una aldea de Bangladesh, casi todas mujeres que tejían muebles de bambú. De ese gesto nació un banco que presta a los pobres, y en 2006, el Premio Nobel de la Paz.</p>'),
  ('<p><strong>Obstáculo 1 — Apego a Outcomes Específicos:</strong>', '<p><strong>Obstáculo 1 — Apego a Resultados Específicos:</strong>'),
  ('Solución: Trabajo interno para alinear todas las frecuencias conscientes e inconscientes.</p>',
   'Solución: Trabajo interno para alinear todas las frecuencias conscientes e inconscientes. Y si algo no llega, no prueba que lo deseaste mal: muchas cosas dependen de otros, del azar y del tiempo.</p>'),
  ('Ansiedad sobre timing interfiere con el proceso natural. Solución: Desarrollar confianza en el timing divino y enfocarse',
   'La ansiedad por los tiempos interfiere con el proceso natural. Solución: Desarrollar confianza en los tiempos de lo divino y enfocarse'),
  ('Solución: Balancear visualización con pasos concretos alineados con la intención.</p>',
   'Solución: Equilibrar la visualización con pasos concretos alineados con la intención. La psicóloga Gabriele Oettingen encontró que soñar solo con el resultado deseado tiende a quitarle energía a quien sueña, y que rinde más alternar el sueño con el obstáculo y el primer paso.</p>'),
  ('El sexto nodo revela que no somos víctimas de las circunstancias ni observadores pasivos de la realidad — somos <strong>co-creadores activos</strong>',
   'El sexto nodo revela que no somos solo víctimas de las circunstancias ni observadores pasivos de la realidad: también somos <strong>co-creadores activos</strong>'),
 ],
 puertas=[arq('Que una intención escrita no es una orden que se le da al universo, sino algo más humilde y más comprobable —cambia lo que uno ve, y las oportunidades que pasaban de largo empiezan a notarse—, se despliega en <em>El Campo</em>, Libro 1 de <em>Arquitectura del Destino</em>, Umbral VI: «Lo que no es».',
              'libro-01-el-campo/L01-U6.html')],
)

# ---------------------------------------------------------------- Nodo 7
# Precisión 6: la visión queda entera, con su linaje y con su primer paso real cuando existe. La lista de
# señales lleva la frase de VI.7 (con los Grof), y los desafíos 2 y 3 del propio nodo quedan como guía.
R['nodo_07.html'] = dict(
 reemplazos=[
  ('<h2>1. Estadios Evolutivos de la Conciencia Humana</h2>',
   '<h2>1. Estadios Evolutivos de la Conciencia Humana</h2>\n'
   '    <p>Este mapa tiene antepasados ilustres. El psiquiatra canadiense Richard Maurice Bucke llamó <em>Conciencia cósmica</em> (1901) al estadio que veía asomar en algunos seres humanos. Pierre Teilhard de Chardin imaginó una noosfera, una envoltura pensante alrededor de la Tierra (<em>El fenómeno humano</em>, publicado en 1955). Sri Aurobindo habló de una conciencia supramental que vendría a transformar la vida, y Jean Gebser describió el paso de la estructura mental a la integral (<em>Origen y presente</em>, 1949-1953). Son visiones, y como visiones se ofrecen: señalan hacia dónde mirar.</p>'),
  ('Identidad limitada al grupo familiar/tribal.', 'Identidad limitada al grupo familiar o tribal.'),
  ('<li>Sensibilidad a frecuencias electromagnéticas y cambios planetarios</li>', '<li>Sensibilidad a los ambientes y a los cambios del entorno</li>'),
  ('<li>Timing perfecto en decisiones y acciones importantes</li>\n    </ul>',
   '<li>El momento justo en decisiones y acciones importantes</li>\n    </ul>\n'
   '    <p>' + SENALES + '</p>'),
  ('Respuesta: acceso instantáneo a conocimiento acumulado de la humanidad, emergencia de inteligencia colectiva distribuida.</p>',
   'Respuesta: acceso instantáneo a conocimiento acumulado de la humanidad, emergencia de inteligencia colectiva distribuida. Marshall McLuhan lo vio venir en 1964: con la tecnología eléctrica, escribió, extendimos nuestro sistema nervioso en un abrazo que rodea el planeta.</p>'),
  ('Acepta tu papel como pionero del siguiente nivel humano.</p>', 'Acepta tu lugar en ese proceso, sin elegidos: participa cualquiera que practica.</p>'),
  ('<p><strong>Telepática:</strong> Intercambio directo de información mental/emocional sin comunicación verbal.</p>',
   '<p><strong>Telepática:</strong> Intercambio directo de información mental y emocional sin comunicación verbal. Su primer paso ya existe, por otro camino: en 2014, un equipo internacional transmitió saludos simples de cerebro a cerebro entre dos personas separadas por miles de kilómetros, con electrodos y una conexión de internet (Grau y otros).</p>'),
  ('Percepción de campos electromagnéticos alrededor de seres vivos. Útil para diagnóstico y facilitar sanación.</p>',
   'Percepción de campos alrededor de los seres vivos. Útil para acompañar la sanación; el diagnóstico queda en manos de la medicina.</p>'),
  ('Capacidad de reorganizar información traumática inmediatamente. Facilitar reorganización celular y energética en otros.</p>',
   'Capacidad de reorganizar información traumática inmediatamente. Facilitar reorganización celular y energética en otros. Así se sueña el porvenir. ' + HOY + '</p>'),
  ('Estrategia: mantener prácticas de grounding, cultivar humildad y perspectiva de servicio, buscar mentoría con individuos más desarrollados.</p>',
   'Estrategia: mantener prácticas que arraiguen en el cuerpo y en la vida de todos los días, cultivar humildad y perspectiva de servicio, buscar la compañía de quienes llevan más tiempo en el camino y, si hace falta, la de un profesional. Y recordar que ' + PORTAL + '.</p>'),
  ('<li><strong>Reconoce</strong> tu papel como pionero evolutivo</li>', '<li><strong>Reconoce</strong> tu lugar en el proceso evolutivo</li>'),
  ('<li><strong>Integra</strong> estas metodologías gradualmente en tu práctica</li>', '<li><strong>Integra</strong> estas metodologías gradualmente en tu práctica, con la ética de tu oficio: primero, no dañar</li>'),
  ('<li><strong>Sanación Cuántica</strong> — Metodología para transformación instantánea de patrones limitantes</li>',
   '<li><strong>Sanación Cuántica</strong> — Metodología para transformar patrones limitantes, al ritmo de quien sana</li>'),
 ],
 puertas=[p_origen('El salto evolutivo, sus pioneros y los desafíos de la transición vuelven al final de la serie como la visión de una nueva humanidad, en <em>Trinity Origen</em>, Libro XIII, Nodo 7: «La Nueva Humanidad». El primer libro de Origen termina donde termina el último.',
                   'Libro_13/nodo_07.html')],
)

# ---------------------------------------------------------------- Índice
R['index.html'] = dict(
 reemplazos=[
  ('<p class="nodo-pregunta">¿Qué información sobre la realidad nos transmiten las emociones cuando las comprendemos como frecuencias de datos multidimensionales?</p>',
   '<p class="nodo-pregunta">¿Qué nos dicen las emociones sobre nosotros y sobre el mundo cuando aprendemos a leerlas en lugar de pelearlas?</p>'),
  ('<p class="nodo-pregunta">¿Cómo puede la comprensión cuántica de la conciencia revolucionar nuestro acercamiento a la sanación del trauma y la transformación del sufrimiento humano?</p>',
   '<p class="nodo-pregunta">¿Cómo puede una comprensión nueva de la conciencia acompañar la sanación del trauma y la transformación del sufrimiento humano?</p>'),
  ('<p class="nodo-pregunta">¿Cómo participamos conscientemente en la creación continua de la realidad a través de la aplicación deliberada de principios cuánticos de manifestación?</p>',
   '<p class="nodo-pregunta">¿Cómo participamos conscientemente en la creación continua de la realidad con la intención, la imaginación y la acción, y dónde termina lo que nos toca?</p>'),
  ('Los siete portales, transitados con intención genuina, constituyen una arquitectura de transformación completa.</p>',
   'Los siete portales, transitados con intención genuina, constituyen una arquitectura de transformación completa.</p>\n'
   '    <p class="medida">Cada nodo se lee como un mapa para la conciencia, y sus prácticas, como gestos que se dan con cuidado y a tu ritmo. Lo que aquí se ofrece acompaña: nunca reemplaza un tratamiento que funciona.</p>'),
  ('"No somos víctimas de nuestra experiencia, sino co-creadores conscientes de la realidad emergente."',
   '"No somos solo víctimas de nuestra experiencia: también somos co-creadores conscientes de la realidad emergente."'),
 ],
)

# ---------------------------------------------------------------- Ejecución
if __name__ == '__main__':
    total = 0
    for nombre in sorted(R):
        n = aplicar(nombre, R[nombre]); total += n
        print(f'{nombre}: {n} cambios')
    print(f'Total: {total}')
