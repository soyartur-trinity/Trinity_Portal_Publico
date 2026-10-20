# Depuración breve de Origen VII (octubre de 2026), aprobada por Arturo: aplica cada reemplazo exactamente una vez.
import os
SRC='/home/claude/Trinity-/01_Trinity_Origen/Libro_07/'
OUT='/home/claude/origen7/out/01_Trinity_Origen/Libro_07/'
NOTA=('<!-- Depuración breve por riesgo clínico (octubre de 2026), con el veto del Lic. Arturo Rodríguez: '
      'las sustancias quedan como tradición o investigación, nunca como indicación; ningún trastorno se presenta como iniciación; '
      'los datos de salud se corrigen con su fuente; las atribuciones rotas se reparan. '
      'El original está en la etiqueta origen-original del repositorio Trinity-. -->\n')
R={}
R['nodo_01.html']=[
 ('    <p>— Mahatma Gandhi</p>\n    <p>Gandhi entendía: la paradoja se resuelve en la acción consciente.</p>',
  '    <p>La paradoja se resuelve en la acción consciente.</p>'),
]
R['nodo_02.html']=[
 ('Como dijo Sócrates antes de beber la cicuta: "La vida no examinada no vale la pena vivirla."',
  'Como dijo Sócrates ante sus jueces: "Una vida sin examen no merece vivirse."'),
]
R['nodo_04.html']=[
 ('Desde el tambor chamánico hasta la neurotecnología, la humanidad ha desarrollado tecnologías precisas para navegar el gran tránsito.',
  'Desde el tambor chamánico hasta los cuidados paliativos, la humanidad ha desarrollado tecnologías precisas para acompañar el gran tránsito.'),
 ('Pero fue escrito para monjes tibetanos del siglo VIII.','Pero fue pensado para practicantes tibetanos de hace siglos.'),
 ('<li>Recordar: la consciencia sigue presente</li>','<li>Recordar lo que enseña la tradición: la consciencia sigue presente</li>'),
 ('<li>Neurotecnología: Hackeando el Cerebro Moribundo</li>','<li>Neurociencia: Lo que se Observa en el Umbral</li>'),
 ('<li>Plantas Maestras: Aliadas en el Umbral</li>','<li>Plantas Maestras: Tradición e Investigación</li>'),
 ('<li>Tecnologías Sonoras: Frecuencias de Transición</li>','<li>Tecnologías Sonoras: La Música del Tránsito</li>'),
 ('''    <h2>Neurotecnología: Hackeando el Cerebro Moribundo</h2>
    <p>La ciencia está confirmando lo que los místicos siempre supieron: la muerte es un estado alterado de consciencia que puede ser navegado. Las nuevas tecnologías nos permiten facilitar este proceso.</p>
    <h3>Estimulación Gamma para Lucidez Terminal</h3>
    <p>Estudios recientes muestran picos de ondas gamma en el momento de la muerte - más altos que en cualquier estado de vida. Es la consciencia consolidándose para el gran salto.</p>
    <h3>Tecnología Aplicada</h3>
    <ul>
      <li>Dispositivos de luz/sonido calibrados a 40Hz</li>
      <li>Estimulación transcraneal suave</li>
      <li>Biofeedback para mantener coherencia</li>
      <li>Realidad virtual con paisajes de transición</li>
    </ul>''',
  '''    <h2>Neurociencia: Lo que se Observa en el Umbral</h2>
    <p>Los místicos siempre dijeron que la muerte es un estado de consciencia que puede ser navegado. La ciencia empieza a mirar ese umbral con sus propios instrumentos, y todavía sabe poco.</p>
    <h3>Ondas Gamma en el Umbral</h3>
    <p>Algunos estudios registraron, en animales y en unos pocos pacientes, un aumento breve de la actividad gamma, la que acompaña la atención y la conciencia, en los minutos que rodean la muerte. Qué significa sigue abierto: hay quien ve ahí una última lucidez, y la investigación todavía no puede decirlo.</p>
    <h3>Lo que Acompaña</h3>
    <ul>
      <li>Luz tenue y sonidos conocidos</li>
      <li>Una mano que sostiene</li>
      <li>Hablarle, aunque parezca no oír: el oído parece ser de lo último en apagarse</li>
      <li>Respirar al ritmo de quien se va</li>
    </ul>'''),
 ('''    <p>La glándula pineal libera DMT endógeno en dos momentos: nacimiento y muerte. Es nuestro psicodélico interno para las grandes transiciones.</p>
    <h3>Investigaciones Actuales</h3>
    <ul>
      <li>DMT exógeno para "ensayar" la muerte</li>
      <li>Protocolos de preparación psicodélica</li>
      <li>Integración de experiencias cercanas a la muerte</li>
      <li>Mapeo de territorios post-mortem</li>
    </ul>
    <p>Protocolo de Preparación con DMT (donde es legal):</p>
    <ul>
      <li>Screening médico/psicológico completo</li>
      <li>Preparación meditativa de 3 meses</li>
      <li>Sesión guiada con facilitador experto</li>
      <li>Dosis progresivas para familiarización</li>
      <li>Integración profunda de cada experiencia</li>
      <li>Aplicación de insights a la vida diaria</li>
    </ul>
    <blockquote>Mi experiencia con DMT me mostró que la muerte es solo un cambio de canal. El miedo se evaporó. Ahora trabajo preparando a otros para sus transiciones." — Dr. Marcus, investigador</blockquote>
''',
  '''    <p>El psiquiatra Rick Strassman propuso, a fines de los años noventa, que la glándula pineal podría liberar DMT en el nacimiento y en la muerte, como un psicodélico interno para las grandes transiciones. Es una hipótesis hermosa que nadie ha comprobado en seres humanos.</p>
'''),
 ('''    <h2>Plantas Maestras: Aliadas en el Umbral</h2>
    <p>Las plantas sagradas han sido utilizadas por milenios para preparar y facilitar el tránsito. No como escape, sino como maestras.</p>''',
  '''    <h2>Plantas Maestras: Tradición e Investigación</h2>
    <p>Muchas tradiciones usaron plantas sagradas como maestras para mirar la muerte. Aquí se nombran como parte de esa historia, no como indicación: ninguna se toma por cuenta propia.</p>'''),
 ('<p>En la Amazonía, la ayahuasca es conocida como la "pequeña muerte". Enseña a morir antes de morir.</p>',
  '<p>En quechua, su nombre quiere decir "liana de los espíritus", o "de los muertos", y en las tradiciones amazónicas se dice que enseña a morir antes de morir.</p>'),
 ('<h3>Enseñanzas de la Medicina</h3>','<h3>Lo que la Tradición Dice que Enseña</h3>'),
 ('<p>Los cactus sagrados enseñan que la muerte es un acto del corazón, no de la mente.</p>',
  '<p>Para las tradiciones que los usan, los cactus sagrados enseñan que la muerte es un acto del corazón, no de la mente.</p>'),
 ('<p>Johns Hopkins está usando psilocibina para ansiedad terminal con resultados revolucionarios.</p>',
  '<p>En 2016, equipos de la Universidad Johns Hopkins y de la Universidad de Nueva York publicaron ensayos con pacientes de cáncer: una sola dosis de psilocibina, con preparación y acompañamiento, redujo la ansiedad y la depresión, y en la mayoría el alivio seguía seis meses después.</p>'),
 ('<h3>Protocolo Hospitalario Emergente</h3>','<h3>Cómo se Hace en los Ensayos</h3>'),
 ('''      <li><strong>Resultado:</strong> 80% reportan pérdida del miedo a la muerte</li>
    </ul>
    <h3>Cannabis Sagrado: El Consolador</h3>
    <p>Usado ritualmente, no recreativamente, el cannabis puede:</p>
    <ul>
      <li>Aliviar ansiedad terminal</li>
      <li>Facilitar conversaciones profundas</li>
      <li>Aumentar apreciación sensorial final</li>
      <li>Suavizar la rigidez del ego</li>
    </ul>''',
  '''    </ul>
    <p>Fuera de estos ensayos, con su selección médica y su acompañamiento, no es una práctica para hacer por cuenta propia.</p>'''),
 ('<h2>Tecnologías Sonoras: Frecuencias de Transición</h2>','<h2>Tecnologías Sonoras: La Música del Tránsito</h2>'),
 ('''    <h3>Frecuencias Específicas</h3>
    <h3>111 Hz - La Frecuencia de los Templos</h3>
    <ul>
      <li>Encontrada en cámaras mortuorias antiguas</li>
      <li>Induce estados de trance</li>
      <li>Facilita experiencias fuera del cuerpo</li>
    </ul>
    <h3>528 Hz - Frecuencia del Amor</h3>
    <ul>
      <li>Resonancia con el corazón</li>
      <li>Reduce ansiedad terminal</li>
      <li>Abre campos de conexión</li>
    </ul>
    <h3>Frecuencia Schumann (7.83 Hz)</h3>
    <ul>
      <li>Resonancia terrestre</li>
      <li>Ayuda en el "despegue" del cuerpo</li>
      <li>Mantiene conexión con Gaia</li>
    </ul>''',
  '''    <h3>La Música en el Umbral</h3>
    <p>Desde los años setenta, la tanatología musical acompaña a quienes mueren con arpa y voz, al ritmo de su respiración, y la musicoterapia forma parte de muchos equipos de cuidados paliativos.</p>'''),
 ('<li><strong>Tambor Chamánico:</strong> 4–7 Hz induce viaje</li>','<li><strong>Tambor Chamánico:</strong> El ritmo que acompaña el viaje</li>'),
 ('''    <p>La VR está emergiendo como herramienta poderosa para preparar la transición.</p>
    <h3>Aplicaciones Actuales</h3>
    <ul>
      <li><strong>"Death Simulator":</strong> Experimentar tu funeral</li>
      <li><strong>"Bardo VR":</strong> Navegación visual del después</li>
      <li><strong>"Peaceful Passing":</strong> Paisajes de transición</li>
      <li><strong>"Ancestor Realms":</strong> Encuentro con fallecidos</li>
    </ul>''',
  '''    <p>La realidad virtual empieza a usarse en cuidados paliativos para llevar paisajes a quien ya no puede salir de su cama.</p>'''),
 ('''      <li><strong>Post-mortem:</strong> Instrucciones inmediatas</li>
    </ul>''',
  '''      <li><strong>Post-mortem:</strong> Instrucciones inmediatas</li>
    </ul>
    <p>En muchos países, una parte de este plan tiene forma legal, las voluntades anticipadas, y se conversa con el equipo de salud.</p>'''),
 ('''    <p>Estudiando consciencia durante paro cardíaco. <strong>Resultados:</strong> consciencia continúa 3–5 minutos post "muerte clínica".</p>
    <h3>Comunicación Post-Mortem Verificada</h3>
    <p>Médiums en laboratorio con resultados estadísticamente significativos.</p>
    <h3>Fotografía de Biofotones</h3>
    <p>Luz emitida por el cuerpo hasta 48 horas post-mortem.</p>
    <h3>Peso del Alma</h3>
    <p>Replicación moderna del experimento de 21 gramos con resultados intrigantes.</p>''',
  '''    <p>Estudia la consciencia durante el paro cardíaco. En su primera etapa, publicada en 2014, algunos sobrevivientes recordaron percepciones durante la reanimación; en un caso, los detalles pudieron verificarse hasta unos tres minutos después de detenido el corazón. Los investigadores lo plantean como una pregunta abierta.</p>'''),
 ('"El protocolo de psilocibina cambió todo.','"El ensayo de psilocibina en el que participé cambió todo.'),
 ('''    <blockquote><strong>David, 67 años - Ingeniero Escéptico</strong> "No creía en nada espiritual. Pero la neurotecnología me mostró estados que… no hay palabras. Ahora sé que soy más que este hardware biológico.</blockquote>
    <blockquote><strong>Carmen, 55 años - Madre en Duelo</strong> "Después de perder a mi hijo, quería morir. La ayahuasca me mostró que él seguía existiendo, solo cambió de forma. Ahora ayudo a otros padres en duelo a conectar.</blockquote>''',
  '''    <p>Si después de una pérdida aparece el deseo de morir, eso necesita ayuda ese mismo día. Ninguna planta ni técnica reemplaza esa compañía.</p>'''),
 ('<li><strong>Para el Intelectual:</strong> Neurotecnología + Bardo study</li>','<li><strong>Para el Intelectual:</strong> Estudio del Bardo + neurociencia</li>'),
 ('<li><strong>Para el Devoto:</strong> Mantras + Plantas sagradas</li>','<li><strong>Para el Devoto:</strong> Mantras + oración</li>'),
 ('tecnologías sonoras, visuales y de estimulación cerebral para facilitar','tecnologías sonoras y visuales para facilitar'),
 ('<li><strong>Guías Certificados:</strong> Profesionales del acompañamiento tecnológico</li>',
  '<li><strong>Acompañantes Formados:</strong> Las doulas del final de la vida y los equipos de cuidados paliativos</li>'),
]
R['nodo_05.html']=[
 ('''      <li>Todo lo conocido se desmorona</li>
    </ul>''',
  '''      <li>Todo lo conocido se desmorona</li>
    </ul>
    <p>La noche oscura no es lo mismo que una depresión. Si durante semanas se apagan el sueño, el apetito y el interés, eso se trata, y tratarlo no interrumpe ningún camino.</p>'''),
 ('''    <h3>Crisis Psicoespiritual</h3>
    <ul>
      <li>Lo que llaman "psicosis" puede ser apertura</li>
      <li>Los límites del yo se disuelven caóticamente</li>
      <li>Sin guía, es terrorífico</li>
      <li>Con comprensión, es liberación</li>
    </ul>
    <h3>Testimonio: La Ejecutiva que Murió en Vida</h3>
    <blockquote><strong>Andrea, 45 años, CEO de multinacional</strong> \"Un día, en medio de una presentación millonaria, me 'salí'. Vi mi cuerpo hablando, pero YO no estaba ahí. O mejor dicho, el YO que conocía se evaporó. Terror puro. Terminé en psiquiátrico. Los médicos lo llamaron 'despersonalización'. Los medicamentos no funcionaron porque no era enfermedad - era iniciación. Encontré un guía que entendía. Me dijo: 'No estás perdiendo la cabeza. Estás perdiendo tu identificación con ella.' Seis meses de infierno. Cada identidad muriendo: no soy ejecutiva, no soy madre, no soy mujer, no soy… ¿qué queda? Un día, en meditación profunda, lo vi: Consciencia pura. Sin forma. Sin límites. Sin miedo. Volví al mundo, pero transformada. Sigo siendo CEO, madre, mujer - pero ahora son roles que juego, no quien SOY. La diferencia es la libertad.</blockquote>
''','''    <h3>Emergencia Espiritual</h3>
    <p>Stanislav y Christina Grof llamaron así a ciertas crisis en las que una apertura espiritual se vive como desborde. Distinguirla de una psicosis no se hace a solas: lo hace un profesional. Si los límites del yo se disuelven y aparece el terror, lo primero es pedir ayuda médica. La comprensión espiritual puede acompañar ese cuidado, nunca reemplazarlo.</p>
'''),
 ('''      <li>El "yo" se revela como <strong>proceso, no cosa</strong></li>
    </ul>''',
  '''      <li>El "yo" se revela como <strong>proceso, no cosa</strong></li>
    </ul>
    <p>Un retiro así se hace en un centro que tenga a quién recurrir. Con antecedentes de psicosis, trauma o crisis de pánico, conviene consultarlo antes.</p>'''),
 ('''    <h3>Trabajo con Enteógenos: Química de la Disolución</h3>
    <p>[Nota: Solo donde es legal y con guía experto]</p>
    <h3>5-MeO-DMT: "La Molécula de Dios"</h3>
    <ul>
      <li>Disolución completa en 15 minutos</li>
      <li>No hay "tú" para tener la experiencia</li>
      <li>Solo consciencia experimentándose</li>
      <li>Integración crucial post-experiencia</li>
    </ul>
    <h3>Ayahuasca: Muerte y Renacimiento</h3>
    <ul>
      <li>El ego vomitado literal y metafóricamente</li>
      <li>Enfrentar cada miedo hasta disolución</li>
      <li>Rendición como única opción</li>
      <li>Renacimiento desde el vacío</li>
    </ul>
    <h3>LSD/Psilocibina: Derretir Fronteras</h3>
    <ul>
      <li>Dosis heroicas supervisadas</li>
      <li>Límites yo/mundo se disuelven</li>
      <li>Unidad directamente experimentada</li>
      <li>El ego como constructo arbitrario</li>
    </ul>''',
  '''    <h3>Las Sustancias: Una Advertencia</h3>
    <p>Algunas tradiciones y algunas investigaciones exploran sustancias que disuelven por un tiempo la sensación de ser un yo separado. No son un método de este camino: pueden desencadenar crisis graves en personas vulnerables, y fuera de un ensayo clínico o de un contexto ceremonial legal y cuidado no hay manera segura de usarlas. La disolución que este nodo busca no llega en una dosis: se cultiva.</p>'''),
 ('<li>Muerte física irrelevante</li>','<li>La muerte física, sin el miedo de antes</li>'),
 ('''    <p><strong>Muerte del ego:</strong> Paz última, integración, función mejorada</p>''',
  '''    <p><strong>Muerte del ego:</strong> Paz última, integración, función mejorada</p>
    <p>Ante la duda, la consulta con un profesional va primero.</p>'''),
 ('    <p>— Sócrates</p>','    <p>Sócrates, ante sus jueces, dijo que una vida sin examen no merece vivirse.</p>'),
 ('Más aún: solo muriendo completamente puedes vivir realmente.','Más aún: solo soltando por completo a quien creías ser puedes vivir realmente.'),
 ('aria-label="Meditación: Morir Ahora"','aria-label="Meditación: Morir Antes de Morir"'),
 ('''    <h3>Meditación: Morir Ahora</h3>
    <p>Siéntate inmóvil. Cierra los ojos. Respira natural.</p>''',
  '''    <h3>Meditación: Morir Antes de Morir</h3>
    <p>Si alguna vez sentiste que no eras real o que te ibas de tu cuerpo, hazla con los ojos abiertos y los pies en el suelo, o déjala para otro momento.</p>
    <p>Siéntate inmóvil. Cierra los ojos. Respira natural.</p>'''),
]
total=0
for f,reps in R.items():
    s=open(SRC+f,encoding='utf-8').read()
    for a,b in reps:
        n=s.count(a)
        assert n==1, (f, n, a[:70])
        s=s.replace(a,b); total+=1
    i=s.index('</title>')+len('</title>\n')
    s=s[:i]+NOTA+s[i:]
    open(OUT+f,'w',encoding='utf-8').write(s)
    print(f, len(reps),'reemplazos')
print('total',total)
