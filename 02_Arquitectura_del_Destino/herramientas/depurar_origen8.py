# Depuración de Origen VIII, Educación Cuántica (noviembre de 2026), con el veto del Lic. Arturo Rodríguez.
# Lente: riesgo clínico y puertas hacia la Red. La visión del libro queda; el libro obedece a sus mejores
# frases («lo que emerge no es una jerarquía de capacidad sino una sinfonía»; «no evaluamos para saber quién
# es mejor»): salen las escalas que fabricaba, los diagnósticos convertidos en dones que vuelven innecesario
# un tratamiento, las prácticas de estados alterados y de ayuno para niños, las cifras sin fuente y las
# escuelas inventadas, que dejan su lugar a casos reales. Se abren siete puertas fractales hacia
# Arquitectura del Destino y el Portal Público, y una hacia Trinity Origen, Libro IV.
#
# Cada nodo se rehace dentro de su <main>, con su mapa de navegación y su subtítulo; el resto de la página
# (plantilla, cabecera, navegación y pie) queda como estaba. Se aplica sobre el original de la etiqueta
# origen-original. Cada anclaje debe aparecer exactamente una vez; si no, el script se detiene sin escribir.
#
# Uso: ORIGEN8_SRC=RUTA/origen-original/01_Trinity_Origen/Libro_08/ ORIGEN8_OUT=RUTA/salida/ python3 depurar_origen8.py
import os, re, sys

SRC = os.environ.get('ORIGEN8_SRC', '/home/claude/orig/01_Trinity_Origen/Libro_08/')
OUT = os.environ.get('ORIGEN8_OUT', '/home/claude/o8/out/01_Trinity_Origen/Libro_08/')

NOTA = ('<!-- Depurado en noviembre de 2026 según la guía de depuración de Quantum, que vale para Origen '
        '(Arquitectura del Destino, maestro v4, sección 5, con las precisiones 5 y 6 de Origen), con el veto del Lic. Arturo Rodríguez: '
        'la visión del libro queda; salen las escalas, las cifras sin fuente, las escuelas y los testimonios inventados (por casos reales) '
        'y las prácticas que no son para niños; se suma el cuidado clínico en la voz de cada nodo y se abren puertas fractales hacia la Red. '
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
  .content .puerta .p-nombre{ font-size:15px; }
  .puerta{ padding:16px 16px 14px; }
  .nodo-desc{ font-size:16px; }
}
@media (prefers-reduced-motion: reduce){
  .puerta .cruzar{ transition:none; }
}
</style>
</head>'''

PIE = ('<p>"No es m&iacute;o vino a trav&eacute;s de m&iacute;."</p>',
       '<p>"No es m&iacute;o, vino a trav&eacute;s de m&iacute;."</p>')

# Frases de cuidado con la letra ya fijada en la constelación
DON = ('Ver en un niño un don no quita mirar también lo que necesita: si le cuesta atender, aprender o vincularse, '
       'una consulta puede abrirle caminos.')   # Origen XIII.7
INDIGO = ('La idea de los niños índigo nació con Nancy Ann Tappe y se difundió en 1999 con el libro de Lee Carroll y Jan Tober. ' + DON)
POEMA = 'como se lee un poema y no como una orden'   # Quantum 1.6

R = {}   # archivo -> dict(titulo, sub, mapa, main, desc)


def mapa(items):
    filas = ''.join('      <li>%s</li>\n' % x for x in items)
    return ('<div class="mapa-nav reveal">\n    <h3>Mapa de navegaci&oacute;n del nodo</h3>\n    <ul>\n%s    </ul>\n  </div>' % filas)


def una_vez(t, viejo, nuevo, nombre, que):
    n = t.count(viejo)
    if n != 1:
        sys.exit(f'{nombre}: {que} aparece {n} veces')
    return t.replace(viejo, nuevo)


def aplicar(nombre, d):
    with open(os.path.join(SRC, nombre), encoding='utf-8') as f:
        t = f.read()
    cuenta = 0
    titulo = re.search(r'<title>(.*?)</title>\n', t).group(0)
    t = una_vez(t, titulo, titulo + NOTA, nombre, 'el título'); cuenta += 1
    t = una_vez(t, '</style>\n</head>', CSS.lstrip('\n'), nombre, 'el cierre del estilo'); cuenta += 1
    t = una_vez(t, PIE[0], PIE[1], nombre, 'la firma del pie'); cuenta += 1
    if 'sub' in d:
        m = re.search(r'    <p class="node-subtitle">.*?</p>\n', t)
        nuevo = '    <p class="node-subtitle">%s</p>\n' % d['sub']
        if m:
            t = una_vez(t, m.group(0), nuevo, nombre, 'el subtítulo')
        else:
            h1 = re.search(r'    <h1 class="node-title">.*?</h1>\n', t).group(0)
            t = una_vez(t, h1, h1 + nuevo, nombre, 'el título del nodo')
        cuenta += 1
    if 'mapa' in d:
        a = t.index('<div class="mapa-nav reveal">')
        b = t.index('  </div>', a) + len('  </div>')
        t = t[:a] + mapa(d['mapa']) + t[b:]
        cuenta += 1
    if 'main' in d:
        a, b = '<main class="content reveal">\n', '\n  </main>'
        if t.count(a) != 1 or t.count(b) != 1:
            sys.exit(f'{nombre}: no se encuentra un único <main>')
        i0 = t.index(a) + len(a); i1 = t.index(b)
        t = t[:i0] + d['main'].strip('\n') + t[i1:]
        cuenta += 1
    for viejo, nuevo in d.get('reemplazos', []):
        t = una_vez(t, viejo, nuevo, nombre, viejo[:60]); cuenta += 1
    for desc in d.get('desc', []):   # las descripciones vacías de las tarjetas del índice, en orden
        if '<p class="nodo-desc"></p>' not in t:
            sys.exit(f'{nombre}: faltan tarjetas vacías')
        t = t.replace('<p class="nodo-desc"></p>', '<p class="nodo-desc">%s</p>' % desc, 1); cuenta += 1
    if '<p class="nodo-desc"></p>' in t:
        sys.exit(f'{nombre}: quedó una tarjeta sin descripción')
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, nombre), 'w', encoding='utf-8') as f:
        f.write(t)
    return cuenta


# ---------------------------------------------------------------- Nodo 1
R['nodo_01.html'] = dict(
 mapa=['La escuela como fábrica de conformidad', 'Lo que la ciencia sabe del aburrimiento',
       'El costo de la estandarización', 'Señales del nuevo paradigma emergente', 'Prácticas de transformación',
       'Testimonio vivo: una escuela en la montaña', 'Pregunta Portal', 'Reflexión Cuántica Final'],
 main=r'''
    <p class="lead">CONSTELACIÓN TRINITY · Libro VIII</p>
    <h2>La escuela como fábrica de conformidad</h2>
    <h3>La Arquitectura del Control</h3>
    <p>El modelo educativo que heredamos no fue un accidente. Tomó su forma en el siglo XIX, al compás de la fábrica y del reloj, para enseñar a muchos al mismo tiempo, y en eso tuvo éxito: millones aprendieron a leer. Pero donde se volvió rígido empezó a producir lo contrario de lo que prometía:</p>
    <ul>
      <li><strong>Trabajadores obedientes</strong>, no pensadores críticos</li>
      <li><strong>Consumidores predecibles</strong>, no creadores conscientes</li>
      <li><strong>Ciudadanos conformes</strong>, no agentes de cambio</li>
      <li><strong>Mentes fragmentadas</strong>, no seres integrales</li>
    </ul>
    <h3>Los 7 Pilares del Colapso</h3>
    <h3>1. TIEMPO FRACTURADO</h3>
    <ul>
      <li>Campanas que fragmentan el pensamiento</li>
      <li>Períodos arbitrarios de 45 o 50 minutos</li>
      <li>Recreos demasiado cortos para que lo aprendido se asiente</li>
      <li>Calendario agrícola en la era digital</li>
    </ul>
    <h3>2. ESPACIO CARCELARIO</h3>
    <ul>
      <li>Filas que impiden la colaboración</li>
      <li>Muros que separan del mundo real</li>
      <li>Iluminación fluorescente, lejos de la luz del día</li>
      <li>Prohibición del movimiento libre</li>
    </ul>
    <h3>3. CURRÍCULUM OBSOLETO</h3>
    <ul>
      <li>Contenido desconectado de la realidad</li>
      <li>Memorización sobre comprensión</li>
      <li>Respuestas únicas para problemas complejos</li>
      <li>Olvido de la sabiduría de los pueblos y de otras tradiciones</li>
    </ul>
    <h3>4. EVALUACIÓN QUE HIERE</h3>
    <ul>
      <li>Exámenes como campos de batalla</li>
      <li>Comparación constante que erosiona la autoestima</li>
      <li>Un número que pretende definir tu valor</li>
      <li>El error como fracaso, no como aprendizaje</li>
    </ul>
    <h3>5. AUTORIDAD VERTICAL</h3>
    <ul>
      <li>Maestro como dictador benevolente</li>
      <li>Estudiante como recipiente vacío</li>
      <li>Castigo y recompensa como motivadores</li>
      <li>Creatividad vista como rebeldía</li>
    </ul>
    <h3>6. DESCONEXIÓN TOTAL</h3>
    <ul>
      <li>De la naturaleza</li>
      <li>Del cuerpo y sus ritmos</li>
      <li>De la comunidad real</li>
      <li>Del propósito de vida</li>
    </ul>
    <h3>7. NEGACIÓN SISTEMÁTICA</h3>
    <ul>
      <li>De las emociones («no llores»)</li>
      <li>De la intuición («eso no es lógico»)</li>
      <li>De la espiritualidad («eso no es científico»)</li>
      <li>De la individualidad («todos igual»)</li>
    </ul>
    <div class="section-divider"></div>
    <h2>Lo que la ciencia sabe del aburrimiento</h2>
    <h3>Lo que la Ciencia Revela</h3>
    <p><strong>El premio que apaga el gusto.</strong> En 1973, en el jardín de infantes de la Universidad de Stanford, Mark Lepper, David Greene y Richard Nisbett observaron a los niños que dibujaban con marcadores por puro placer. A algunos les anunciaron un diploma con una cinta dorada si lo hacían. Días después, en su tiempo libre, esos pequeños apenas tocaban los marcadores; los demás seguían igual. La recompensa prometida había convertido un juego en una tarea.</p>
    <p><strong>El reloj del adolescente.</strong> En la adolescencia el sueño se corre hacia la noche: el cuerpo pide dormirse y despertarse más tarde. Por eso, en 2014, la Academia Estadounidense de Pediatría recomendó que los colegios secundarios no empezaran antes de las ocho y media. La campana de las siete no encuentra mentes perezosas: encuentra cerebros que todavía duermen.</p>
    <p><strong>El miedo no enseña.</strong> Bajo una amenaza constante —la burla, la nota que humilla, el castigo— la atención se estrecha y busca peligros, no ideas. Se puede aprender con miedo, pero junto con la lección se aprende a temer.</p>
    <p><strong>La creatividad que se educa hacia afuera.</strong> En 2006, en una charla que vieron millones de personas, Ken Robinson preguntó si las escuelas matan la creatividad. Su respuesta fue que los niños no crecen hacia ella: la escuela suele educarlos para que la abandonen.</p>
    <h3>El Estudiante que se Apaga</h3>
    <p><strong>Señales que cualquier maestro reconoce:</strong></p>
    <ul>
      <li>Mirada perdida durante clases</li>
      <li>Creatividad en declive año tras año</li>
      <li>Ansiedad ante cualquier evaluación</li>
      <li>Pérdida de pasión por aprender</li>
      <li>Desconexión entre la mente, el cuerpo y lo que importa</li>
    </ul>
    <p>Si la ansiedad antes de una prueba quita el sueño o el hambre, si la tristeza dura semanas o si un chico no quiere volver a la escuela, no es solo el sistema: es alguien que necesita ser escuchado, y a veces una consulta.</p>
    <div class="section-divider"></div>
    <h2>El costo de la estandarización</h2>
    <h3>Lo que Estamos Perdiendo como Especie</h3>
    <p><strong>Genios Silenciados:</strong></p>
    <p>Los genios que pierde una escuela rígida rara vez llegan a ser famosos. Son los hijos de familias que no hablaban como el maestro, los que pensaban despacio, los que dibujaban en el margen, los que se fueron en segundo año porque nadie los esperó.</p>
    <p>También a los niños que la Nueva Era llamó índigo, cristal o arcoíris se los rotula a veces como «problema». ''' + INDIGO + r'''</p>
    <p><strong>Capacidades que se Adormecen:</strong></p>
    <ul>
      <li>El asombro ante lo común</li>
      <li>La pregunta sin miedo: «¿por qué?»</li>
      <li>La concentración sin reloj</li>
      <li>La sintonía sin palabras con quienes ama</li>
      <li>La conversación con lo vivo: el árbol, el perro, la lluvia</li>
      <li>Los sueños recordados y contados al despertar</li>
      <li>La sincronicidad leída ''' + POEMA + r'''</li>
    </ul>
    <p><strong>Potencial Colectivo Desperdiciado:</strong></p>
    <ul>
      <li>Soluciones a la crisis climática que nadie se atrevió a pensar</li>
      <li>Tecnologías de consciencia no desarrolladas</li>
      <li>Vocaciones que nunca supieron su nombre</li>
      <li>Paz mundial pospuesta por mentes bélicas</li>
    </ul>
    <h3>La Gran Inversión</h3>
    <p>Donde se vuelve rígido, el sistema produce exactamente lo contrario de lo que necesitamos. A la izquierda, lo que produce; a la derecha, lo que la humanidad necesita:</p>
    <ul>
      <li>Competencia → Colaboración</li>
      <li>Miedo → Amor</li>
      <li>Separación → Unidad</li>
      <li>Consumo → Creación</li>
      <li>Obediencia → Soberanía</li>
      <li>Agotamiento → Vitalidad</li>
      <li>Ignorancia selectiva → Sabiduría integral</li>
    </ul>
    <div class="section-divider"></div>
    <h2>Señales del nuevo paradigma emergente</h2>
    <h3>Los Heraldos del Cambio</h3>
    <p><strong>Niños y Jóvenes que Buscan Otra Escuela:</strong></p>
    <ul>
      <li>Familias que eligen con conciencia la educación en casa</li>
      <li>Jóvenes creando sus propias escuelas y comunidades de aprendizaje</li>
      <li>Estudiantes que piden ser escuchados en cómo se enseña</li>
    </ul>
    <p>Cuando un chico no quiere ir a la escuela, o deja de ir, casi siempre está diciendo algo que todavía no puede decir con palabras: acoso, miedo, tristeza, una manera de aprender que no encuentra su lugar. Antes de leerlo como despertar, se lo escucha, y si hace falta, se consulta.</p>
    <p><strong>Maestros Despertando:</strong></p>
    <ul>
      <li>Docentes que dejan aulas que ya no pueden sostener</li>
      <li>Quienes integran la meditación en silencio, sin anunciarla</li>
      <li>Evaluaciones alternativas aunque las reglas no las prevean</li>
      <li>Un currículum oculto de consciencia</li>
    </ul>
    <p><strong>Padres Cuestionando:</strong></p>
    <ul>
      <li>«¿Por qué mi hijo brillante es considerado un problema?»</li>
      <li>«¿Por qué la tarea destruye nuestra familia?»</li>
      <li>«¿Por qué mi hija perdió su alegría?»</li>
      <li>«¿Qué estamos haciendo realmente?»</li>
    </ul>
    <p><strong>Sistemas que Crujen:</strong></p>
    <ul>
      <li>La salud mental de los estudiantes, un llamado que ya no puede desoírse</li>
      <li>Universidades perdiendo relevancia</li>
      <li>Empleadores que miran lo que alguien sabe hacer antes que su título</li>
      <li>Conocimiento libre superando a las instituciones</li>
    </ul>
    <div class="section-divider"></div>
    <h2>Prácticas de transformación</h2>
    <h3>1. Arqueología Interior</h3>
    <p>Una excavación de cuatro semanas en tu propia historia escolar. Si el aula fue lugar de acoso o de maltrato, este trabajo no se hace a solas: se hace acompañado, o se deja para otro momento.</p>
    <p><strong>Semana 1: Excavación</strong></p>
    <ul>
      <li>Lista diez pasiones que tenías antes de los seis años</li>
      <li>Identifica cuándo y cómo se fue apagando cada una</li>
      <li>Nota los patrones de «apagado» que se repiten</li>
    </ul>
    <p><strong>Semana 2: Reconocimiento</strong></p>
    <ul>
      <li>Escribe una carta al niño que fuiste en el aula</li>
      <li>Si puedes, perdona a los maestros que no supieron verte; si hubo maltrato, no tienes que perdonar: basta con nombrarlo</li>
      <li>Perdónate por haber creído sus límites</li>
    </ul>
    <p><strong>Semana 3: Reclamación</strong></p>
    <ul>
      <li>Elige una pasión dormida para despertarla</li>
      <li>Dedícale quince minutos diarios sin objetivo</li>
      <li>Observa la resistencia interna</li>
    </ul>
    <p><strong>Semana 4: Integración</strong></p>
    <ul>
      <li>Celebra pequeños actos de rebeldía creativa</li>
      <li>Comparte tu proceso con alguien de confianza</li>
      <li>Nota los cambios en tu energía vital</li>
    </ul>
    <h3>2. Desescolarización Mental Progresiva</h3>
    <p>La palabra viene de Ivan Illich, que en <em>La sociedad desescolarizada</em> (1971) describió lo que la escuela enseña a confundir: la enseñanza con el aprendizaje, el diploma con la competencia, pasar de grado con educarse. Desescolarizar la mente es volver a separar esas cosas.</p>
    <p><strong>Protocolo de 30 Días:</strong></p>
    <p><strong>Días 1 a 10: Desaprender la Campana</strong></p>
    <ul>
      <li>Elige cada día una franja sin reloj ajeno, aunque sea breve</li>
      <li>Trabaja en flujo, no en bloques, cuando tu vida lo permita</li>
      <li>Nota cuántas de tus horas responden todavía a un timbre que ya no suena</li>
      <li>Escucha tu propio ritmo sin pelearte con tus responsabilidades</li>
    </ul>
    <p><strong>Días 11 a 20: Desaprender la Autoridad</strong></p>
    <ul>
      <li>Cuestiona tres «verdades» por día</li>
      <li>Busca múltiples perspectivas</li>
      <li>Confía en tu conocimiento interior, y contrástalo</li>
      <li>Practica el «no sé» sagrado</li>
    </ul>
    <p><strong>Días 21 a 30: Desaprender la Comparación</strong></p>
    <ul>
      <li>Ayuno de redes sociales</li>
      <li>Celebra tu rareza única</li>
      <li>Aprecia sin evaluar</li>
      <li>Crea sin mostrar</li>
    </ul>
    <h3>3. Mapa de tus Inteligencias Dormidas</h3>
    <p>Marca del 1 al 10 tu nivel actual y el que intuyes posible, y anota al lado qué lo frenó:</p>
    <ul>
      <li>Lingüística</li>
      <li>Lógica</li>
      <li>Espacial</li>
      <li>Musical</li>
      <li>Corporal</li>
      <li>Interpersonal</li>
      <li>Intrapersonal</li>
      <li>Naturalista</li>
      <li>Existencial</li>
      <li>Y una más, todavía sin nombre, que solo tú conoces</li>
    </ul>
    <div class="section-divider"></div>
    <h2>Testimonio vivo</h2>
    <h3>Una escuela en la montaña</h3>
    <p>A fines de 1954 mandaron a don Lorenzo Milani, un cura que incomodaba, a Barbiana, un puñado de casas dispersas en la montaña de Toscana. Encontró chicos campesinos que la escuela pública había reprobado y despedido. Con ellos abrió una escuela que funcionaba casi sin vacaciones, donde el que sabía un poco más enseñaba al que sabía menos. En la pared colgó dos palabras en inglés: <em>I care</em>, «me importa».</p>
    <p>En 1967, junto con él, sus alumnos escribieron <em>Carta a una maestra</em>, una acusación contra la escuela que aprueba a los hijos de quienes ya hablan como ella y deja caer a los demás. Allí la compararon con un hospital que cura a los sanos y rechaza a los enfermos. El libro salió a fines de mayo; Milani murió un mes después, a los cuarenta y cuatro años.</p>
    <p>No hizo falta abandonar la escuela para transformarla. Hizo falta mirar a los que la escuela no miraba.</p>
    <div class="section-divider"></div>
    <h2>Pregunta Portal</h2>
    <p>Antes de continuar al siguiente nodo, siéntate con esta pregunta. No la respondas desde la mente. Deja que tu cuerpo, tu corazón y tu alma hablen:</p>
    <h3>«¿Qué genio único fue silenciado en tu proceso educativo?»</h3>
    <p><strong>Pistas para la exploración:</strong></p>
    <ul>
      <li>¿Qué hacías naturalmente que fue etiquetado como «problema»?</li>
      <li>¿Qué pregunta prohibida aún quema en tu interior?</li>
      <li>¿Qué talento ocultaste para sobrevivir?</li>
      <li>¿Qué parte de ti murió en un aula?</li>
      <li>¿Qué sueño enterraste bajo diplomas?</li>
    </ul>
    <div class="section-divider"></div>
    <h2>Reflexión Cuántica Final</h2>
    <p>El colapso del modelo industrial no es una tragedia. Es un portal. Como toda muerte en el camino de consciencia, anuncia un renacimiento.</p>
    <p>No necesitamos reformar el sistema. Necesitamos compostarlo y plantar las semillas de algo radicalmente nuevo en su suelo fértil.</p>
    <p>La educación del futuro ya está aquí, naciendo en garajes, jardines, bosques y corazones valientes. No pide permiso. No espera aprobación. Simplemente florece donde encuentra consciencia dispuesta.</p>
    <p><strong>Tu genio silenciado es la semilla.</strong> <strong>Tu dolor educativo es el fertilizante.</strong> <strong>Tu despertar es el agua.</strong> <strong>Tu valentía es el sol.</strong></p>
    <p><em>La nueva educación comienza contigo recordando quién eras antes de que te enseñaran quién deberías ser.</em></p>
''' + portal('Que el premio puede apagar lo que se hacía por gusto —los chicos que dibujaban por placer y dejaron de hacerlo cuando se les prometió un diploma— se despliega en <em>La intención</em>, Libro 29 del Portal Público, Umbral II: «Los marcadores».',
             '29_La_Intencion/umbral-02.html'),
)

# ---------------------------------------------------------------- Nodo 2
R['nodo_02.html'] = dict(
 sub='Muchas maneras de ser inteligente',
 mapa=['Más allá de Gardner: el espectro completo', 'Las 13 Inteligencias', 'Sinergias entre inteligencias',
       'Exploración de tus inteligencias', 'Inteligencias colectivas emergentes', 'Prácticas de activación',
       'Caso real: la escuela de las ocho maestras', 'Lo que ve un buen maestro', 'Conexión Trinity',
       'Meditación de Activación', 'Reflexión Cuántica Final'],
 main=r'''
    <p class="lead"><strong>PREPARACIÓN PARA EL NODO 2</strong></p>
    <p>Has excavado el daño. Has visto el colapso. Has tocado tu genio enterrado.</p>
    <p>Ahora estás listo para descubrir el espectro completo de inteligencias que palpitan en tu interior, esperando ser reconocidas, honradas y despertadas.</p>
    <p>El viaje de desescolarización ha comenzado. No hay vuelta atrás.</p>
    <div class="section-divider"></div>
    <h2>Más allá de Gardner: el espectro completo</h2>
    <blockquote>«Cuando una civilización reconoce y cultiva todas las inteligencias de sus seres, salta evolutivamente. Cuando las suprime, colapsa. Estamos en el punto de decisión.»</blockquote>
    <p>Aquí el mapa de las inteligencias se lee en clave pedagógica: cuáles son, cómo se apagan, cómo despiertan y cómo se combinan.</p>
    <div class="section-divider"></div>
    <h2>Las 13 Inteligencias</h2>
    <h3>El Mapa Completo del Potencial Humano</h3>
    <p>Howard Gardner abrió la puerta en 1983 con <em>Estructuras de la mente</em>: siete inteligencias, donde la escuela veía una sola. En 1995 sumó la del naturalista, y dejó abierta una existencial. Pero era solo el vestíbulo. La casa completa tiene muchas más habitaciones, algunas con puertas que la humanidad apenas comienza a abrir.</p>
    <p>Gardner insistió en dos cosas que conviene llevar al aula: que todos tenemos todas, en proporciones distintas, y que no son estilos de aprendizaje ni casilleros para clasificar a un chico (lo escribió en 2013, cansado de verlas convertidas en etiquetas). Las trece que siguen no son una escalera. Son trece puertas de una misma casa.</p>
    <h3>Las que la escuela reconoce</h3>
    <p><strong>1. Lingüística–Vibratoria</strong></p>
    <ul>
      <li>La palabra que nombra con precisión</li>
      <li>La poesía y los idiomas del otro</li>
      <li>El canto y los mantras, como práctica de las tradiciones</li>
      <li>La conversación con los reinos naturales, en el lenguaje de los mitos</li>
    </ul>
    <p><strong>Cuando se apaga:</strong> cuesta decir lo que importa.</p>
    <p><strong>2. Lógico–Matemática–Fractal</strong></p>
    <ul>
      <li>La geometría que los antiguos llamaron sagrada, como lenguaje de la forma</li>
      <li>El orden que aparece dentro del caos</li>
      <li>Los patrones que se repiten en todas las escalas</li>
      <li>El placer de una demostración</li>
    </ul>
    <p><strong>Cuando se apaga:</strong> los números se vuelven amenaza y dejan de ser juego.</p>
    <p><strong>3. Espacial–Holográfica</strong></p>
    <ul>
      <li>Ver en tres dimensiones con los ojos cerrados</li>
      <li>Orientarse sin mapa</li>
      <li>Diseñar espacios que transforman a quien los habita</li>
      <li>Sentir el clima de un lugar al entrar</li>
    </ul>
    <p><strong>Cuando se apaga:</strong> el mundo se vuelve un plano sin relieve.</p>
    <p><strong>4. Musical–Frecuencial</strong></p>
    <ul>
      <li>El ritmo, la melodía y el oído para las disonancias de un lugar</li>
      <li>El sonido que consuela y acompaña</li>
      <li>El canto compartido</li>
      <li>Componer desde estados de quietud</li>
    </ul>
    <p><strong>Cuando se apaga:</strong> se deja de oír la música de lo cotidiano.</p>
    <p><strong>5. Corporal–Kinestésica–Energética</strong></p>
    <ul>
      <li>La destreza de las manos</li>
      <li>La danza como portal</li>
      <li>Las artes marciales internas</li>
      <li>Los mudras, gestos con que las tradiciones de la India hacen hablar al cuerpo</li>
    </ul>
    <p><strong>Cuando se apaga:</strong> el cuerpo queda olvidado debajo del pupitre.</p>
    <h3>Las que la vida pide</h3>
    <p><strong>6. Interpersonal–Sintónica</strong></p>
    <ul>
      <li>Leer el estado de otro antes de que hable</li>
      <li>Comunicación de corazón a corazón</li>
      <li>Armonizar un grupo</li>
      <li>Reparar un vínculo</li>
    </ul>
    <p><strong>Cuando se apaga:</strong> vínculos que no llegan a tocarse.</p>
    <p><strong>7. Intrapersonal–Multidimensional</strong></p>
    <ul>
      <li>Dialogar con las voces y las partes de uno mismo</li>
      <li>El diálogo con el Ser Superior, en el lenguaje de las tradiciones</li>
      <li>Integrar la propia sombra</li>
      <li>Conocer y elegir los propios estados</li>
    </ul>
    <p><strong>Cuando se apaga:</strong> uno se vuelve un extraño para sí mismo.</p>
    <p><strong>8. Naturalista–Gaiana</strong></p>
    <ul>
      <li>Reconocer especies, estaciones y señales del cielo</li>
      <li>La conversación con lo vivo</li>
      <li>Gaia, la Tierra imaginada como un organismo</li>
      <li>La medicina de la tierra, como tradición de los pueblos</li>
    </ul>
    <p><strong>Cuando se apaga:</strong> el mundo vivo se vuelve paisaje de fondo.</p>
    <p><strong>9. Existencial–Cósmica</strong></p>
    <ul>
      <li>Preguntarse para qué</li>
      <li>Sostener paradojas sin resolverlas a la fuerza</li>
      <li>Dialogar con el vacío creativo</li>
      <li>Filosofía vivida, no solo leída</li>
    </ul>
    <p><strong>Cuando se apaga:</strong> se vive sin preguntarse por la vida.</p>
    <h3>Las que las tradiciones cultivan</h3>
    <p><strong>10. Temporal–Cronéstica</strong></p>
    <ul>
      <li>Habitar el presente</li>
      <li>Recordar sin quedar preso del recuerdo</li>
      <li>Imaginar futuros y prepararles el camino</li>
      <li>Reconocer el momento oportuno, lo que los griegos llamaron <em>kairós</em></li>
    </ul>
    <p><strong>Cuando despierta:</strong> el sentido del momento justo.</p>
    <p><strong>11. Morfogenética–Creacional</strong></p>
    <ul>
      <li>La intuición que llega de golpe después de mucho trabajo</li>
      <li>Crear con otros lo que nadie traía solo</li>
      <li>Percibir los patrones de un grupo</li>
      <li>Los campos morfogenéticos, que Rupert Sheldrake propuso como hipótesis</li>
    </ul>
    <p><strong>Cuando despierta:</strong> las ideas llegan como si alguien las hubiera dejado ahí.</p>
    <p><strong>12. Akáshica–Memorial</strong></p>
    <ul>
      <li>El <em>akasha</em>, éter y memoria del mundo en la tradición de la India y en la teosofía</li>
      <li>La memoria de la especie que guardan los mitos</li>
      <li>La sabiduría de los antepasados</li>
      <li>El talento que parece traído de antes</li>
    </ul>
    <p><strong>Cuando despierta:</strong> un saber que se reconoce más de lo que se aprende.</p>
    <p><strong>13. Unificada–Avatar</strong></p>
    <ul>
      <li>Todas las inteligencias en conversación</li>
      <li>La consciencia de unidad que describen los místicos</li>
      <li>Lo que las tradiciones llaman unión con lo divino</li>
      <li>El servicio desde el Todo</li>
    </ul>
    <p><strong>Cuando despierta:</strong> el yo se vuelve liviano; no desaparece, sirve.</p>
    <p>Ninguna está más alta que otra. La decimotercera no es el último peldaño: es el centro de la rueda, el lugar donde las otras doce se encuentran.</p>
    <p>Si alguna vez el déjà vu se vuelve constante, los sueños parecen anunciar lo que va a pasar o las ideas llegan a borbotones y no dejan dormir, no es una inteligencia que despierta: es el momento de pedir ayuda, esa misma semana.</p>
    <div class="section-divider"></div>
    <h2>Sinergias entre Inteligencias</h2>
    <h3>Cuando uno más uno es más que dos</h3>
    <p>Cuando dos o más inteligencias se encienden a la vez, no se suman: se multiplican, y crean capacidades nuevas.</p>
    <p><strong>Musical + Matemática = Música visible</strong></p>
    <ul>
      <li>Geometrías que el sonido dibuja: Ernst Chladni las hizo aparecer en placas cubiertas de arena</li>
      <li>Composición que sigue proporciones</li>
      <li><strong>Caso:</strong> la sinestesia que traen algunos niños, que ven colores al oír notas</li>
    </ul>
    <p><strong>Corporal + Akáshica = Danza del Alma</strong></p>
    <ul>
      <li>El cuerpo como archivo de memorias</li>
      <li>Danzas que un pueblo nunca escribió y su cuerpo conserva</li>
      <li><strong>Caso:</strong> los niños que aprenden de sus abuelos un baile antiguo sin una sola explicación</li>
    </ul>
    <p><strong>Naturalista + Temporal = Lectura de las Estaciones</strong></p>
    <ul>
      <li>El calendario del agricultor que mira el cielo</li>
      <li>La paciencia de la semilla</li>
      <li><strong>Caso:</strong> la huerta escolar, donde un mismo chico aprende biología, tiempo y espera</li>
    </ul>
    <p><strong>Lingüística + Interpersonal = Transmisión Directa</strong></p>
    <ul>
      <li>Enseñar con la presencia además de la palabra</li>
      <li>Poesía colectiva</li>
      <li><strong>Caso:</strong> el maestro cuya forma de escuchar enseña más que su clase</li>
    </ul>
    <p><strong>Espacial + Morfogenética = Arquitectura Viva</strong></p>
    <ul>
      <li>Espacios que evolucionan con quienes los usan</li>
      <li>Construcciones que cuidan</li>
      <li><strong>Caso:</strong> los edificios que enseñan a sus habitantes cómo vivir en ellos</li>
    </ul>
    <p><strong>Las condiciones de la sinergia:</strong> un cuerpo tranquilo, un propósito claro y un ambiente que no asusta.</p>
    <div class="section-divider"></div>
    <h2>Exploración de tus Inteligencias</h2>
    <p>Esto no es un test. Es una exploración de tu configuración única de genio.</p>
    <h3>FASE 1: Primera mirada (7 días)</h3>
    <p><strong>Días 1 y 2: Observación Pura</strong></p>
    <ul>
      <li>Sin juzgar, nota qué inteligencias usas naturalmente</li>
      <li>Registra los momentos de flujo</li>
      <li>Identifica qué actividades te dan energía</li>
    </ul>
    <p><strong>Días 3 y 4: Exploración Activa</strong></p>
    <ul>
      <li>Prueba una inteligencia dormida durante veinte minutos</li>
      <li>Nota resistencias y aperturas</li>
      <li>Registra sensaciones corporales</li>
    </ul>
    <p><strong>Días 5 y 6: Combinaciones</strong></p>
    <ul>
      <li>Intenta usar dos inteligencias a la vez</li>
      <li>Observa las sinergias que aparecen</li>
      <li>Anota los accidentes felices</li>
    </ul>
    <p><strong>Día 7: Integración</strong></p>
    <ul>
      <li>Mapa personal de inteligencias despiertas, dormidas y frenadas</li>
      <li>Tu «firma de genio» única</li>
      <li>Un plan de despertar a tu medida</li>
    </ul>
    <h3>FASE 2: Despertar Profundo (21 días)</h3>
    <p><strong>Semana 1: Despertar lo Dormido</strong></p>
    <ul>
      <li>Elige tu inteligencia más dormida</li>
      <li>Quince minutos diarios de práctica dedicada</li>
      <li>Diario de resistencias y hallazgos</li>
    </ul>
    <p><strong>Semana 2: Construcción de Puentes</strong></p>
    <ul>
      <li>Conecta la inteligencia dormida con una despierta</li>
      <li>Crea proyectos que pidan las dos</li>
      <li>Celebra los pequeños logros</li>
    </ul>
    <p><strong>Semana 3: Estabilización</strong></p>
    <ul>
      <li>Integra la nueva inteligencia en tu vida diaria</li>
      <li>Comparte tu proceso con otros</li>
      <li>Anota lo que cambió</li>
    </ul>
    <p><strong>Herramienta: Matriz Personal.</strong> Para cada una de las trece: su estado (dormida, despierta, maestra), lo que la apagó (una herida, una creencia, un miedo), lo que la enciende (una práctica, un mentor, una experiencia) y un próximo paso concreto.</p>
    <div class="section-divider"></div>
    <h2>Inteligencias Colectivas Emergentes</h2>
    <p>Más allá de las inteligencias individuales, existen inteligencias que solo emergen en colectivo, cuando varios seres sintonizan. La ciencia empezó a medirlas: en 2010, Anita Woolley y sus colegas encontraron que los grupos tienen algo parecido a una inteligencia propia, y que la explicaban menos el talento del miembro más brillante que la sensibilidad de todos para leer a los otros y el reparto de los turnos para hablar.</p>
    <h3>Las 7 Inteligencias Colectivas Primarias</h3>
    <p><strong>1. Inteligencia de Enjambre</strong></p>
    <ul>
      <li>Coordinación sin líder central</li>
      <li>Movimiento unificado espontáneo</li>
      <li><strong>Manifestación:</strong> las bandadas de estorninos que giran sobre Roma como un solo cuerpo</li>
    </ul>
    <p><strong>2. Inteligencia Circular</strong></p>
    <ul>
      <li>Sabiduría que emerge del círculo</li>
      <li>Soluciones que nadie tenía solo</li>
      <li><strong>Manifestación:</strong> los círculos de palabra, donde cada voz espera su turno y cuenta</li>
    </ul>
    <p><strong>3. Inteligencia de Visión</strong></p>
    <ul>
      <li>El grupo que imagina un futuro común</li>
      <li>Decisiones que miran lejos</li>
      <li><strong>Manifestación:</strong> los consejos donde ancianos y jóvenes deciden juntos</li>
    </ul>
    <p><strong>4. Inteligencia Restaurativa</strong></p>
    <ul>
      <li>Reparación que solo ocurre en grupo</li>
      <li>Regeneración del tejido social</li>
      <li><strong>Manifestación:</strong> los círculos de justicia restaurativa</li>
    </ul>
    <p><strong>5. Inteligencia Creacional</strong></p>
    <ul>
      <li>Creación imposible para uno solo</li>
      <li>Arte que trasciende la suma de sus partes</li>
      <li><strong>Manifestación:</strong> las sesiones de improvisación del jazz, donde nadie sabe adónde va la música y todos llegan</li>
    </ul>
    <p><strong>6. Inteligencia Navegacional</strong></p>
    <ul>
      <li>El grupo que encuentra caminos que nadie veía</li>
      <li>Saltos sincronizados</li>
      <li><strong>Manifestación:</strong> las comunidades que se reinventan después de una catástrofe</li>
    </ul>
    <p><strong>7. Inteligencia Compasiva, que algunas tradiciones llaman crística</strong></p>
    <ul>
      <li>El amor que se vuelve acción entre muchos</li>
      <li>Un campo de cuidado que nadie dirige</li>
      <li><strong>Manifestación:</strong> los vecinos que sostienen a una familia en su peor noche</li>
    </ul>
    <div class="section-divider"></div>
    <h2>Prácticas de Activación</h2>
    <h3>1. El Mandala de Tu Genio</h3>
    <p><strong>Materiales:</strong> un papel grande y circular, trece colores, un compás.</p>
    <ul>
      <li>Divide el círculo en trece gajos iguales</li>
      <li>Asigna una inteligencia a cada gajo</li>
      <li>Colorea desde adentro hacia afuera según cuánto está despierta: junto al centro, dormida; en el medio, despertando; en el borde, viva</li>
      <li>Observa tu patrón único</li>
      <li>Elige tres inteligencias para despertar este año</li>
    </ul>
    <h3>2. Trece Días, Trece Inteligencias</h3>
    <ul>
      <li><strong>Día 1, Lingüística:</strong> inventa diez palabras con significado; canta en una lengua inventada; escribe sin corregir</li>
      <li><strong>Día 2, Lógico-Fractal:</strong> encuentra patrones en la naturaleza; crea tu propia secuencia numérica; medita sobre una paradoja</li>
      <li><strong>Día 3, Espacial:</strong> dibuja con los ojos cerrados; recorre despacio una habitación conocida sin mirar, con las manos adelante; imagina un objeto girando</li>
      <li><strong>Día 4, Musical:</strong> encuentra tu nota; improvisa sin pensar; escucha la sinfonía del silencio</li>
      <li><strong>Día 5, Corporal:</strong> baila tu día sin música; inventa cinco mudras personales; camina como distintos animales</li>
      <li><strong>Día 6, Interpersonal:</strong> practica la escucha sin palabras; envía amor a tres personas en silencio; respira al compás de otra persona</li>
      <li><strong>Día 7, Intrapersonal:</strong> dialoga con tres partes de ti; escribe una carta desde la vida que no elegiste; abraza con amor una sombra</li>
      <li><strong>Día 8, Naturalista:</strong> siéntate junto a un árbol diez minutos y nota qué cambia en ti; planta algo sintiendo la tierra; pide una señal y léela ''' + POEMA + r'''</li>
      <li><strong>Día 9, Existencial:</strong> mira el cielo nocturno diez minutos; escribe para qué crees que estás aquí; contempla todo lo que existía antes de ti y seguirá después</li>
      <li><strong>Día 10, Temporal:</strong> escribe una carta a quien serás dentro de diez años; agradece algo de tu pasado; practica cinco minutos de presencia</li>
      <li><strong>Día 11, Morfogenética:</strong> explica una idea con un dibujo; cambia un hábito pequeño que heredaste; deja una pregunta abierta antes de dormir y anota lo que llegue al despertar</li>
      <li><strong>Día 12, Akáshica:</strong> escribe la página de tu vida que más te enseñó; recupera un talento olvidado; cuenta la historia de un objeto heredado</li>
      <li><strong>Día 13, Unificada:</strong> integra todas las inteligencias; medita en silencio diez minutos; ofrece tu genio al mundo</li>
    </ul>
    <h3>3. La Danza de las Inteligencias</h3>
    <p><strong>Duetos:</strong> elige dos inteligencias al azar, crea una actividad que pida ambas y practícala diez minutos por día durante una semana.</p>
    <p><strong>Tríadas:</strong> combina tres en un proyecto. Por ejemplo, espacial, musical y corporal: una danza arquitectónica.</p>
    <p><strong>Sinfonía completa:</strong> crea una experiencia que use las trece, documenta el proceso y compártelo con tu comunidad.</p>
    <div class="section-divider"></div>
    <h2>Caso real: la escuela de las ocho maestras</h2>
    <h3>Cuando se Honran Todas las Inteligencias</h3>
    <p>En 1984, ocho maestras de una escuela pública de Indianápolis leyeron <em>Estructuras de la mente</em> y manejaron catorce horas para mostrarle a su autor el plan de una escuela pensada desde sus inteligencias. Él les contó que nunca había imaginado usar su teoría de ese modo, y les dio su apoyo. En 1987 abrió la Key School, la primera del mundo organizada así: ciento cincuenta chicos elegidos por sorteo, grupos de distintas edades reunidos por interés y proyectos que cruzaban las materias.</p>
    <p>Funcionó casi treinta años y fue estudiada en medio mundo. Cuando cerró, en 2016, dejó una pregunta que sigue abierta en cada aula: cómo honrar todas las inteligencias sin descuidar ninguna de las que la vida también va a pedir.</p>
    <h3>Lo que ve un buen maestro</h3>
    <p>Temple Grandin no habló hasta los tres años y medio. A sus padres les aconsejaron internarla; su madre se negó, y un neurólogo propuso probar con terapia del habla. A los catorce la expulsaron de una escuela por tirarle un libro a un compañero que se burlaba de ella. En la siguiente, un profesor de ciencias que había trabajado para la NASA, William Carlock, tomó en serio su obsesión por una máquina que la calmaba con presión y la ayudó a construirla. Esa pasión se volvió oficio: Grandin se doctoró en zootecnia y cambió la manera en que se trata al ganado en medio mundo.</p>
    <p>En su historia las dos cosas estuvieron juntas desde el principio: la terapia que le dio la palabra y el maestro que vio el don. ''' + DON + r'''</p>
    <div class="section-divider"></div>
    <h2>Conexión Trinity</h2>
    <p>Este nodo mira hacia adentro lo que el Libro IV de Trinity Origen, <em>Inteligencias Sin Nombre</em>, miró hacia afuera: las formas de inteligencia sin rostro humano —cristalinas, algorítmicas, ecosistémicas, electromagnéticas, simbólicas y temporales— que la consciencia aprende a reconocer. Allí el bosque y la red de hongos bajo la tierra piensan como un conjunto; aquí, la bandada y el círculo.</p>
''' + p_origen('Las seis tipologías de lo que piensa sin rostro humano, del cristal a la inteligencia artificial y al bosque que decide como un solo organismo, viven en <em>Trinity Origen</em>, Libro IV, Nodo 2: «Tipología de lo Innombrable».',
               'Libro_04/nodo_02.html') + r'''
    <div class="section-divider"></div>
    <h2>Meditación de Activación</h2>
    <p>Siéntate cómodamente. Respira profundo. Cierra los ojos.</p>
    <blockquote>Reconozco las trece inteligencias que danzan en mi interior. Algunas despiertas, cantando su canción. Otras dormidas, esperando su momento. Todas perfectas, todas necesarias.<br><br>Suelto el juicio sobre lo que debería saber. Abrazo el misterio de lo que puedo llegar a ser. Cada inteligencia es una puerta. Cada puerta lleva al mismo lugar: la totalidad de quien soy.<br><br>Despierto ahora, con amor y curiosidad, las inteligencias que mi alma elige despertar. Para mi mayor bien y el de todos los seres.<br><br>Soy un genio multidimensional recordando su magnificencia.</blockquote>
    <p>Respira. Siente. Integra.</p>
    <div class="section-divider"></div>
    <h2>Reflexión Cuántica Final</h2>
    <p>No eres inteligente. Eres <strong>INTELIGENCIAS</strong>: plural, múltiple, infinita.</p>
    <p>El sistema educativo tradicional es como evaluar a todos los animales por su capacidad de trepar árboles. El elefante parece tonto, el delfín incompetente, el águila discapacitada. La fábula es vieja: la escribió en los años cuarenta George Reavis, subdirector de las escuelas públicas de Cincinnati, con un pato que nadaba mejor que su maestro y terminó mediocre porque lo obligaron a correr.</p>
    <p>Pero cuando cada ser es evaluado en su elemento, cuando cada inteligencia es honrada en su expresión única, lo que emerge no es una jerarquía de capacidad sino una <strong>sinfonía de genio colectivo</strong>.</p>
    <p><strong>Tu combinación única de inteligencias es tu firma en el universo.</strong> No hay nadie más con tu exacta configuración. Eres, literalmente, un milagro irrepetible de potencial.</p>
    <p><em>La nueva educación no te enseña a ser inteligente. Te recuerda que ya eres un universo de inteligencias esperando expresarse.</em></p>
''' + portal('Que una bandada de miles gira como un solo cuerpo sin que nadie la dirija, y que unos físicos de Roma filmaron a los estorninos para entender cómo lo hacen, se despliega en <em>Los muchos</em>, Libro 35 del Portal Público, Umbral I: «Sobre Termini».',
             '35_Los_Muchos/umbral-01.html'),
)

# ---------------------------------------------------------------- Nodo 3
R['nodo_03.html'] = dict(
 sub='El espacio como tercer maestro',
 mapa=['Preparación para el Nodo 3', 'Geometría sagrada en el diseño educativo', 'El sonido del aula',
       'Tecnología y naturaleza en simbiosis', 'El facilitador como sintonizador de campos', 'Prácticas de campo',
       'Lo que la ciencia midió en las aulas', 'Meditación de Activación del Campo', 'Advertencia Necesaria',
       'Reflexión Cuántica Final'],
 main=r'''
    <h2>Preparación para el Nodo 3</h2>
    <p class="lead">Has mapeado tus inteligencias. Has visto tu genio único. Has tocado tu potencial.</p>
    <p>Ahora estás listo para comprender cómo el espacio mismo —el aula, el ambiente, el campo— puede ser diseñado para despertar y amplificar esas inteligencias.</p>
    <p><em>De reconocer el genio a crear los templos donde florece.</em></p>
    <div class="section-divider"></div>
    <h2>Geometría Sagrada en el Diseño Educativo</h2>
    <h3>La Arquitectura de la Consciencia</h3>
    <p>Los antiguos constructores de templos sabían algo que hemos olvidado: la forma del espacio moldea la forma del pensamiento. La geometría no es decoración; es una tecnología de la atención. En Reggio Emilia, Loris Malaguzzi lo dijo con otras palabras: después de los adultos y de los otros niños, el ambiente es el tercer maestro.</p>
    <h3>Los 7 Principios Geométricos del Aula Cuántica</h3>
    <p><strong>1. LA PROPORCIÓN ÁUREA (φ ≈ 1,618)</strong></p>
    <ul>
      <li>Dimensiones del aula, ventanas y puertas en proporción áurea</li>
      <li>Disposición del mobiliario siguiendo una espiral abierta</li>
      <li>Arte y detalles basados en φ</li>
    </ul>
    <p><strong>Lo que ofrece:</strong> armonía para la vista y la sensación de estar en casa que tantos describen ante ciertas proporciones. Los arquitectos la buscaron desde la Antigüedad, y Le Corbusier la convirtió en medida humana en su Modulor.</p>
    <p><strong>2. EL CÍRCULO SAGRADO</strong></p>
    <ul>
      <li>Sin frente ni atrás</li>
      <li>Sin jerarquía espacial</li>
      <li>Un centro vacío, como punto de infinito</li>
      <li>Todos a la misma distancia del centro</li>
    </ul>
    <p><strong>Lo que ofrece:</strong> nadie queda detrás de nadie; todas las caras están a la vista; la palabra circula.</p>
    <p><strong>3. LA VESICA PISCIS</strong></p>
    <ul>
      <li>Dos círculos superpuestos</li>
      <li>Una zona de creación en la intersección</li>
      <li>Espacio para el trabajo propio y para el compartido</li>
    </ul>
    <p><strong>Lo que ofrece:</strong> un lugar para lo de cada uno, otro para lo común y un tercero donde se encuentran, que es donde nace lo nuevo.</p>
    <p><strong>4. LA ESTRELLA DE DOS TRIÁNGULOS</strong></p>
    <ul>
      <li>Dos triángulos entrelazados, uno que sube y otro que baja</li>
      <li>En tres dimensiones, dos tetraedros: la figura que la tradición esotérica llama merkaba</li>
      <li>Un centro elevado</li>
    </ul>
    <p><strong>Lo que ofrece:</strong> un símbolo para contemplar, presente en muchas tradiciones como encuentro de lo alto y lo concreto; un recordatorio de que el aula une las dos cosas.</p>
    <p><strong>5. EL DODECAEDRO CÓSMICO</strong></p>
    <ul>
      <li>Doce caras, doce rincones de trabajo</li>
      <li>Cada rincón para una inteligencia</li>
      <li>Los estudiantes eligen y rotan</li>
    </ul>
    <p><strong>Lo que ofrece:</strong> ninguna inteligencia sin lugar; un desarrollo amplio, sin especialización prematura. En el <em>Timeo</em>, Platón dio al dodecaedro el papel del todo.</p>
    <p><strong>6. LA FLOR DE LA VIDA</strong></p>
    <ul>
      <li>En pisos, paredes o techos</li>
      <li>Como mandala central</li>
      <li>En los materiales de trabajo</li>
    </ul>
    <p><strong>Lo que ofrece:</strong> una belleza que invita a mirar despacio; un patrón para dibujar, colorear y contemplar.</p>
    <p><strong>7. EL TOROIDE DINÁMICO</strong></p>
    <ul>
      <li>Aire que entra, circula y sale</li>
      <li>Aprendizaje en espiral, que vuelve a lo mismo cada vez más hondo</li>
      <li>Energía que se renueva</li>
    </ul>
    <p><strong>Lo que ofrece:</strong> un aula ventilada piensa mejor; nada se estanca, ni el aire ni las ideas.</p>
    <div class="section-divider"></div>
    <h2>El Sonido del Aula</h2>
    <h3>La Sinfonía del Aula Consciente</h3>
    <p>El sonido es la arquitectura invisible que más hondo toca la consciencia. Un aula con eco cansa; un aula callada, cuando esa quietud es elegida, concentra.</p>
    <p>En diciembre de 2012, en un colegio secundario de Gotemburgo, Björn Vickhoff y su equipo midieron el pulso de quince chicos de dieciocho años mientras cantaban juntos. Bastó empezar para que los corazones se acompasaran: subían y bajaban a la vez. Cantar es una manera de respirar guiada, y cuando muchos respiran igual, el pulso los sigue.</p>
    <p>María Montessori inventó en sus aulas una lección del silencio: el grupo entero se quedaba quieto hasta que se oía lo que nunca se oye, y los niños, lejos de aburrirse, la pedían.</p>
    <h3>El Día Escolar en Cinco Sonidos</h3>
    <p><strong>MAÑANA: ACTIVACIÓN.</strong> Un canto compartido o una música elegida juntos. Despierta el cuerpo y acompasa al grupo.</p>
    <p><strong>MEDIA MAÑANA: CONCENTRACIÓN.</strong> El silencio de trabajo, con permiso para hablar bajo.</p>
    <p><strong>MEDIODÍA: INTEGRACIÓN.</strong> La conversación: la mesa compartida, la risa, los conflictos que se dicen.</p>
    <p><strong>TARDE: PROFUNDIZACIÓN.</strong> Música para crear, elegida con cuidado: a unos los ayuda, a otros los distrae.</p>
    <p><strong>FINAL: CIERRE.</strong> Un minuto de quietud y un tañido suave. En los monasterios de Thich Nhat Hanh la campana no ordena: invita a volver a la respiración.</p>
    <p>Ninguna máquina reemplaza esto. Los sonidos que prometen inducir estados no son para el aula de los niños: el estado que se busca llega con la respiración, el canto y el silencio.</p>
    <div class="section-divider"></div>
    <h2>Tecnología y Naturaleza en Simbiosis</h2>
    <h3>El Matrimonio Sagrado del Aula del Futuro</h3>
    <p>No es tecnología contra naturaleza. Es tecnología con naturaleza.</p>
    <h3>Integración Biomimética</h3>
    <p><strong>PAREDES VIVAS.</strong> Jardines verticales, musgo, ecosistemas en miniatura que los chicos cuidan. El biólogo Edward O. Wilson llamó biofilia (1984) a esa afinidad innata por lo vivo.</p>
    <p><strong>LUZ DEL DÍA.</strong> Ventanas generosas y, donde falte el sol, luces que cambian con las horas. El cuerpo se orienta por la luz: duerme mejor de noche quien la recibe de día.</p>
    <p><strong>AGUA A LA VISTA.</strong> Una fuente, una pecera, el sonido del agua; y agua para beber siempre a mano.</p>
    <p><strong>LA MESA DE LA NATURALEZA.</strong> Piedras, cristales, caracoles, hojas y semillas que traen los chicos, para mirar, clasificar y contar, renovados con las estaciones. Si en tu tradición las piedras acompañan, que sean un gesto de intención y belleza, sin promesa de efecto.</p>
    <h3>Tecnología Consciente</h3>
    <p><strong>REALIDAD AUMENTADA EDUCATIVA.</strong> Modelos que se manipulan, viajes imposibles, laboratorios que no caben en un aula. Con límites: como máximo treinta minutos seguidos, siempre con pausas al aire libre; integración, no escape; herramienta, no muleta.</p>
    <p><strong>LA IA COMO FACILITADORA.</strong> Un asistente que se adapta a cada estudiante y libera al maestro para lo humano. Sus principios: la IA nunca reemplaza el encuentro, los algoritmos son transparentes, los datos pertenecen al estudiante y existe el derecho a desconectarse.</p>
    <p><strong>LA RESPIRACIÓN COMO BIOFEEDBACK.</strong> Cinco respiraciones lentas antes de empezar, y el cuerpo como el mejor monitor. Ningún sensor sobre un niño sin su acuerdo y el de su familia, y nunca para vigilarlo.</p>
    <div class="section-divider"></div>
    <h2>El Facilitador como Sintonizador de Campos</h2>
    <h3>Del Profesor al Maestro Cuántico</h3>
    <p>El rol del educador en el aula cuántica no es solo transmitir información: es sintonizar campos de posibilidad donde el aprendizaje emerge. Carl Rogers lo vio en <em>Libertad y creatividad en la educación</em> (1969): lo que facilita aprender es el clima de la relación, hecho de autenticidad, aprecio y comprensión empática. Una revisión de más de cien estudios (Cornelius-White, 2007) encontró que la calidez y la empatía del docente acompañan más deseo de saber y mejores resultados.</p>
    <h3>Las 7 Capacidades del Facilitador Cuántico</h3>
    <p><strong>1. COHERENCIA DEL CORAZÓN.</strong> Llegar en calma. Unos minutos de respiración lenta antes de entrar, cerca de seis respiraciones por minuto: un adulto sereno ayuda a serenarse a un grupo. Entrenamiento: meditación centrada en el pecho, gratitud, pausas conscientes.</p>
    <p><strong>2. LECTURA DEL CLIMA.</strong> Percibir el estado del grupo: quién no vino hoy aunque esté sentado, qué silencio es tensión y cuál es concentración, qué necesidad no se dice. Desarrollo: visión periférica, percepción sutil, empatía, pausas sin pantalla.</p>
    <p><strong>3. SINTONIZACIÓN DINÁMICA.</strong> Ajustarse al grupo y cambiar estados con la presencia. Herramientas: la voz como instrumento, el movimiento, la respiración grupal, la postura.</p>
    <p><strong>4. ENSEÑANZA QUE EMERGE.</strong> Permitir lo que el momento trae, responder desde la experiencia y la escucha, decir «no sé, averigüémoslo juntos». Práctica: meditación en el vacío, escritura libre, hablar sin guion, entrega al presente.</p>
    <p><strong>5. ALQUIMIA EMOCIONAL.</strong> Transmutar el miedo en curiosidad, la frustración en determinación, la competencia en colaboración, la apatía en pasión. Método: sentir sin juzgar, nombrar sin drama, respirar la emoción, liberarla con amor.</p>
    <p><strong>6. DESPERTAR DE POTENCIALES.</strong> Ver el genio en cada estudiante, encender inteligencias dormidas, acompañar saltos. Proceso: visión del potencial, reflejo del brillo, invitación sin presión, celebración.</p>
    <p><strong>7. NAVEGACIÓN MULTIDIMENSIONAL.</strong> Enseñar en varios niveles a la vez, atender a cada uno y al grupo, mantener la coherencia en el caos, surfear las olas de la consciencia. Maestría: presencia plena, atención amplia, respuesta intuitiva, fluidez.</p>
    <h3>El Día del Facilitador Cuántico</h3>
    <p><strong>Antes:</strong> unos minutos de silencio propio, la intención del día, la conexión con el propósito.</p>
    <p><strong>Al preparar el espacio:</strong> abrir las ventanas, ordenar el círculo, poner algo vivo en el centro.</p>
    <p><strong>Al recibir:</strong> mirar a cada uno a los ojos, saludarlo por su nombre, notar cómo llega.</p>
    <p><strong>Durante:</strong> sostener el campo, ajustar sobre la marcha, responder a lo imprevisto.</p>
    <p><strong>Al cerrar:</strong> integrar el día, agradecer en grupo, despedir.</p>
    <p><strong>Después:</strong> descansar de verdad. Nadie sostiene un campo once horas seguidas; el facilitador que se cuida es el que puede cuidar.</p>
    <div class="section-divider"></div>
    <h2>Prácticas de Campo</h2>
    <h3>1. Tu Rincón Cuántico</h3>
    <p><strong>Semana 1: Mirada.</strong> Elige un espacio de dos por dos metros. Anota del 1 al 10 cómo te sientes ahí y qué te molesta.</p>
    <p><strong>Semana 2: Geometría.</strong> Coloca un símbolo que te diga algo, alguna proporción áurea, un centro para la mirada. Observa.</p>
    <p><strong>Semana 3: Sonido.</strong> Prueba el silencio, una música que te calme, el murmullo del agua; a distintas horas y volúmenes. Anota los efectos.</p>
    <p><strong>Semana 4: Naturaleza.</strong> Suma al menos tres plantas, agua de alguna forma y más luz natural. Siente la transformación.</p>
    <h3>2. La Mesa de la Naturaleza</h3>
    <p>Un rincón con lo que el mundo trae: piedras, cristales, hojas, semillas, plumas. Los chicos los traen, los nombran, los ordenan y los devuelven a la tierra cuando la estación cambia. Es geología, botánica y contemplación a la vez.</p>
    <h3>3. La Espiral de Sincronización</h3>
    <p><strong>Inicio (3 minutos):</strong> todos de pie en círculo, las manos en el corazón, una respiración lenta y compartida, sin retener el aire; imaginar una luz que une los corazones.</p>
    <p><strong>Desarrollo (5 minutos):</strong> movimiento en espiral, lento; contacto visual suave; sonidos espontáneos permitidos; sentir cómo el grupo se vuelve uno.</p>
    <p><strong>Cierre (2 minutos):</strong> quietud, una intención compartida y gratitud.</p>
    <p><strong>Lo que se nota:</strong> un grupo que empieza más tranquilo y más junto.</p>
    <div class="section-divider"></div>
    <h2>Lo que la ciencia midió en las aulas</h2>
    <h3>Ciento cincuenta y tres aulas</h3>
    <p>Durante tres años, un equipo de la Universidad de Salford dirigido por Peter Barrett estudió ciento cincuenta y tres aulas de veintisiete escuelas primarias inglesas y siguió el progreso de casi cuatro mil alumnos. Las características físicas del aula explicaban el 16 % de las diferencias en lo que los chicos avanzaban en un año (Barrett y otros, 2015). Pesaban la luz, la temperatura y la calidad del aire; también que el aula se sintiera propia, que fuera flexible y que tuviera la cantidad justa de estímulo y de color.</p>
    <p>Que el espacio enseña ya no es solo una intuición de los constructores de templos: hoy se puede medir.</p>
    <h3>Una niña y cuarenta y cuatro repeticiones</h3>
    <p>En 1907, en un barrio obrero de Roma, María Montessori vio a una niña de unos tres años encajar una y otra vez unos cilindros de madera. Contó cuarenta y cuatro repeticiones; ni el canto de los demás ni el sillón levantado la sacaron de ahí. Cuando terminó, miró alrededor como quien despierta de una siesta reparadora. De esa escena nació un método, y una idea que el aula cuántica hace suya: preparar el ambiente y dejar que la atención haga el resto.</p>
    <div class="section-divider"></div>
    <h2>Meditación de Activación del Campo</h2>
    <p>Para realizar antes de entrar al aula:</p>
    <blockquote>Este espacio es sagrado. Cada geometría es un portal. Cada sonido es medicina. Cada elemento es maestro. Entro con reverencia. Busco mi calma. Me uno al campo. Permito el milagro del aprendizaje. La sabiduría está en el espacio. El conocimiento en el campo. La transformación en la presencia. El despertar en el ahora. Soy estudiante y maestro. Soy el que aprende y el aprendizaje. Soy el campo consciente. Que este espacio despierte lo mejor en mí. Que yo despierte lo mejor en este espacio. Que juntos creemos el futuro de la educación. Así es. Así sea. Así será.</blockquote>
    <div class="section-divider"></div>
    <h2>Advertencia Necesaria</h2>
    <h3>Los Peligros del Aula Cuántica Mal Aplicada</h3>
    <p><strong>COMERCIALIZACIÓN SIN CONSCIENCIA:</strong> tecnología sin propósito, geometría como decoración, sonidos sin comprensión, cristales como moda. <strong>Resultado:</strong> espacios caóticos que confunden más de lo que aclaran.</p>
    <p><strong>FACILITADORES SIN SOSTÉN:</strong> sin cuidado de sí, sin formación, sin supervisión, sin práctica propia. <strong>Resultado:</strong> el aula amplifica las heridas de quien la conduce.</p>
    <p><strong>EXCESO DE ESTÍMULO:</strong> demasiados sonidos a la vez, sobrecarga tecnológica, formas que compiten. <strong>Resultado:</strong> saturación de los sentidos y chicos que se apagan.</p>
    <p><strong>EXPECTATIVAS MÁGICAS:</strong> creer que el espacio hace todo, olvidar el trabajo interior, buscar resultados instantáneos, negar la sombra. <strong>Resultado:</strong> desilusión y rechazo del paradigma.</p>
    <p><strong>LOS NIÑOS PRIMERO:</strong> ninguna práctica de estados alterados, ayunos o respiraciones con retención en el aula de los chicos. Su campo se cuida con juego, sueño, comida, aire libre y adultos presentes.</p>
    <div class="section-divider"></div>
    <h2>Reflexión Cuántica Final</h2>
    <p>El aula cuántica no es un lugar. Es un estado de consciencia materializado en el espacio.</p>
    <p>Cada elemento —desde la geometría hasta el sonido, desde la planta hasta la tecnología— es una nota en la sinfonía del despertar. Cuando todos están afinados y en armonía, el espacio mismo se convierte en maestro.</p>
    <p>No necesitas millones para crear un aula cuántica. Necesitas consciencia, intención y comprensión de los principios. Un simple círculo de cojines con una planta y un rato de silencio puede ser más poderoso que un aula holográfica sin alma.</p>
    <p><strong>El secreto:</strong> el campo responde a la coherencia del corazón más que a la sofisticación de la tecnología.</p>
    <p><strong>La clave:</strong> el facilitador ES el aula más importante.</p>
    <p><strong>La verdad:</strong> cuando el espacio y la consciencia se encuentran, el aprendizaje se vuelve inevitable, gozoso y transformador.</p>
''' + portal('Que una niña de un barrio pobre de Roma repitió cuarenta y cuatro veces el mismo ejercicio sin que el canto ni el sillón levantado la distrajeran, y que de esa escena nació un método, se despliega en <em>La duración</em>, Libro 32 del Portal Público, Umbral II: «Cuarenta y cuatro veces».',
             '32_La_Duracion/umbral-02.html'),
)

# ---------------------------------------------------------------- Nodo 4
R['nodo_04.html'] = dict(
 sub='Lo que cada alma vino a aprender',
 mapa=['Preparación para el Nodo 4', 'El mito de la elección', 'El Libro de la Vida en las tradiciones',
       'Escuchar el alma de un niño', 'Sincronicidades como guía', 'Aprendizaje no lineal y multitemporal',
       'Maestría y certificación', 'Prácticas de activación', 'Advertencia Necesaria', 'Testimonio: la noche del Apollo',
       'Reflexión Cuántica Final'],
 main=r'''
    <p class="lead"><em>Aprendizaje Guiado por el Propósito de Vida</em></p>
    <blockquote>«Cada alma viene con un currículum escrito en las estrellas. Nuestra tarea no es imponerle otro, sino ayudarle a leer el suyo.»</blockquote>
    <h2>Preparación para el Nodo 4</h2>
    <p>Has visto cómo el espacio puede despertar consciencia. Has comprendido la tecnología sagrada del aula. Has sentido el campo de posibilidad.</p>
    <p>Ahora estás listo para el salto más radical: dejar de imponer un currículum y empezar a escuchar el del alma.</p>
    <p><em>Del espacio que despierta al propósito que guía.</em></p>
    <div class="section-divider"></div>
    <h2>El Mito de la Elección</h2>
    <h3>Una idea que tiene veinticuatro siglos</h3>
    <p>Al final de la <em>República</em>, Platón cuenta el mito de Er: antes de nacer, cada alma elige una vida y recibe un <em>daimon</em>, un guardián que la acompaña para que cumpla lo elegido. Después bebe del río del olvido, y olvida. En 1996, el psicólogo James Hillman volvió a esa imagen en <em>El código del alma</em>: cada persona trae una singularidad que pide ser vivida, como el roble está contenido en la bellota.</p>
    <p>Educar, desde esta mirada, no es fabricar a alguien: es ayudarle a recordar lo que vino a ser.</p>
    <div class="section-divider"></div>
    <h2>El Libro de la Vida en las Tradiciones</h2>
    <h3>Los registros akáshicos</h3>
    <p>En la tradición de la India, <em>akasha</em> es el éter, el espacio que todo lo contiene; la teosofía lo volvió memoria del mundo, un archivo donde quedaría escrito cada destino. Rudolf Steiner escribió desde 1904 sobre una «crónica del Akasha», y quince años después fundó en Stuttgart la primera escuela Waldorf, para los hijos de los obreros de una fábrica de cigarrillos. Su pedagogía sigue viva en escuelas de todo el mundo.</p>
    <p>La tradición describe cinco niveles en ese libro de la vida. Leídos como mapa para contemplar, enseñan a mirar a un estudiante con más hondura:</p>
    <p><strong>NIVEL 1: PROPÓSITO.</strong> ¿Para qué vino este ser? La misión principal, los dones a desarrollar, el servicio a ofrecer y, en el lenguaje de la tradición, las lecciones kármicas. <strong>En el aula:</strong> orientación vocacional que parte de lo que el chico ama y hace bien.</p>
    <p><strong>NIVEL 2: LO QUE YA SABE.</strong> Las tradiciones que creen en el renacimiento leen así los talentos precoces: la música que aparece sin maestro, la comprensión matemática súbita, la sabiduría temprana. La mirada pedagógica, sin necesidad de esa creencia, ve lo mismo: un don que pide lugar.</p>
    <p><strong>NIVEL 3: LOS ENCUENTROS.</strong> Los maestros del alma, los compañeros de aprendizaje, los espejos. La tradición habla de contratos entre almas. Ningún maltrato estaba pactado: ese encuentro no se honra, se deja atrás.</p>
    <p><strong>NIVEL 4: EL MOMENTO.</strong> Las ventanas en que algo puede aprenderse. Respetar el tiempo del alma es no forzar aprendizajes prematuros, honrar los períodos de barbecho, reconocer los momentos de aceleración y confiar en el proceso orgánico. Una crisis a veces abre una puerta; no llegó para eso.</p>
    <p><strong>NIVEL 5: LAS LLAVES.</strong> Palabras, símbolos, experiencias y encuentros que despiertan el recuerdo: un mantra propio, una geometría, un viaje, un rito de paso.</p>
    <div class="section-divider"></div>
    <h2>Escuchar el Alma de un Niño</h2>
    <h3>Lo que sí y lo que no</h3>
    <p>Un adulto puede buscar, si lo desea, la lectura de su propio libro de vida en la tradición que lo convoque. Un niño no: ninguna lectura, de ninguna tradición, decide su escolaridad, su salud ni su tratamiento, ni reemplaza la evaluación de quien sabe acompañarlo.</p>
    <p>Algunas familias reciben un diagnóstico —un trastorno de la atención, del espectro autista, del aprendizaje— y lo sienten como una sentencia. Es otra cosa: un mapa para acompañar. La mirada del alma y la del diagnóstico no compiten. Un tratamiento indicado no apaga un don, y un don no vuelve innecesario un tratamiento. ''' + DON + r'''</p>
    <p>La lectura que sí está al alcance de un maestro o de un padre es la de todos los días:</p>
    <ul>
      <li>¿Qué hace cuando nadie le pide nada?</li>
      <li>¿Qué pregunta una y otra vez?</li>
      <li>¿Con qué pierde la noción del tiempo?</li>
      <li>¿En quién se convierte junto a cada persona?</li>
      <li>¿Qué le duele que nadie ve?</li>
    </ul>
    <p><strong>La ética de esta escucha:</strong> con su permiso, con información dosificada, enfocada en sus posibilidades, nunca como un pronóstico que limita.</p>
    <p><strong>Del cuaderno al aula:</strong> identificar los temas que lo encienden, crear proyectos alineados con ellos, buscar recursos que resuenen, acercarle mentores adecuados y evaluar de maneras que tengan sentido para él.</p>
    <div class="section-divider"></div>
    <h2>Sincronicidades como Guía</h2>
    <h3>Cuando el Universo Parece Diseñar el Curso</h3>
    <p>Carl Jung llamó sincronicidad a la coincidencia significativa sin causa visible. Un currículum del alma las escucha, y las lee ''' + POEMA + r''': como invitaciones, nunca como mandatos.</p>
    <p><strong>SINCRONICIDADES DE CONTENIDO.</strong> El tema que persigue al estudiante: aparece tres veces en una semana, un libro se abre en la página justa, una conversación casual ilumina, un sueño responde una pregunta. <strong>Respuesta:</strong> seguir el hilo, profundizar, anotar.</p>
    <p><strong>SINCRONICIDADES DE ENCUENTRO.</strong> El mentor que aparece, el compañero con la habilidad complementaria, el grupo de estudio que se forma solo. <strong>Respuesta:</strong> facilitar la conexión y celebrarla.</p>
    <p><strong>SINCRONICIDADES DE LUGAR.</strong> La invitación inesperada, la beca para el programa justo, el viaje que se abre. <strong>Respuesta:</strong> considerar el sí, prepararse, confiar sin dejar de pensar.</p>
    <p><strong>SINCRONICIDADES DE CRISIS.</strong> El problema que pide una habilidad nueva, la pérdida que abre otro camino. Ninguna enfermedad ni ningún duelo es una lección asignada; lo que se hace después, a veces, se vuelve maestro. <strong>Respuesta:</strong> cuidar primero, y recién después buscar lo que esa sacudida pudo abrir.</p>
    <h3>El Diario de Sincronicidades</h3>
    <p><strong>Cada día:</strong> la fecha, el estado emocional, la sincronicidad observada, una primera interpretación, la acción tomada y lo que se aprendió.</p>
    <p><strong>Cada semana:</strong> patrones, temas recurrentes, direcciones claras, resistencias.</p>
    <p><strong>Cada mes:</strong> un mapa de sincronicidades, el ajuste del plan de estudios, la celebración de lo seguido.</p>
    <p>Si todo empieza a parecer una señal dirigida a ti, o las señales exigen decisiones urgentes, es momento de conversarlo con alguien de confianza.</p>
    <div class="section-divider"></div>
    <h2>Aprendizaje No Lineal y Multitemporal</h2>
    <h3>Más Allá del Tiempo Cronológico</h3>
    <p>El alma no aprende en línea recta. Avanza en espirales, saltos, retrocesos que sanan y aceleraciones súbitas. El currículum del alma respeta esa naturaleza.</p>
    <h3>Los 7 Tipos de Tiempo de Aprendizaje</h3>
    <p><strong>1. TIEMPO ESPIRAL.</strong> Volver al mismo tema cada vez más hondo; no es repetición, es profundización. <strong>Ejemplo:</strong> la pregunta por la muerte, que un chico hace a los siete años y vuelve a hacerse a los catorce, a los veintiuno, a los cuarenta.</p>
    <p><strong>2. TIEMPO CUÁNTICO.</strong> Los saltos súbitos de comprensión. <strong>Ejemplo:</strong> Henri Poincaré contó que la solución que buscaba desde hacía semanas le llegó entera al subir a un ómnibus, mientras pensaba en otra cosa. El salto llega, pero después del trabajo.</p>
    <p><strong>3. TIEMPO QUE SANA HACIA ATRÁS.</strong> El pasado no cambia; cambia el lugar desde donde se lo mira. La memoria se reconstruye cada vez que se recuerda, y por eso un recuerdo puede volver a guardarse con otra luz. <strong>Ejemplo:</strong> mirar una herida escolar desde la comprensión de hoy; si esa memoria duele demasiado, con alguien formado.</p>
    <p><strong>4. TIEMPO PARALELO.</strong> Aprender varias cosas a la vez; procesos que siguen trabajando mientras se duerme: el sueño consolida lo aprendido. <strong>Ejemplo:</strong> un idioma y la música que se refuerzan entre sí.</p>
    <p><strong>5. TIEMPO SEMILLA.</strong> Plantar ahora, cosechar después. <strong>Ejemplo:</strong> la filosofía estudiada a los quince y comprendida a los treinta.</p>
    <p><strong>6. TIEMPO FRACTAL.</strong> El todo en la parte: un día contiene una vida. <strong>Ejemplo:</strong> un proyecto de un mes que repite el proceso de una vida entera.</p>
    <p><strong>7. TIEMPO KAIRÓS.</strong> El momento oportuno, el tiempo cualitativo frente al que se mide. <strong>Ejemplo:</strong> cinco minutos que cambian una vida.</p>
    <h3>Proyecto: Viaje en el Tiempo Personal</h3>
    <p><strong>Semana 1, el pasado:</strong> investigar el linaje familiar, honrar a los que vinieron antes, recuperar dones olvidados.</p>
    <p><strong>Semana 2, el presente:</strong> presencia, gratitud, acción cuidada.</p>
    <p><strong>Semana 3, el futuro:</strong> imaginar a quien serás, escribirte un mensaje desde allí, preparar el camino.</p>
    <p><strong>Semana 4, la integración:</strong> unir las tres líneas en una obra y celebrarla con una pequeña ceremonia.</p>
    <div class="section-divider"></div>
    <h2>Maestría y Certificación</h2>
    <h3>La Revolución de la Evaluación</h3>
    <p>En el currículum del alma no importa el diploma sino la maestría real: el conocimiento encarnado.</p>
    <p><strong>MAESTRÍA ENCARNADA:</strong> vive en el cuerpo, no se olvida, se expresa con naturalidad y transforma a quien la tiene. <strong>La certificación sola:</strong> información que se pierde fácil y no cambia la esencia.</p>
    <p><strong>MAESTRÍA INTEGRAL:</strong> une mente, cuerpo y espíritu, se conecta con todo y evoluciona. <strong>La certificación sola:</strong> fragmentada, aislada, estática.</p>
    <p><strong>MAESTRÍA SERVICIAL:</strong> se orienta al servicio, beneficia al colectivo, forma otros maestros. <strong>La certificación sola:</strong> se orienta al ego y crea competencia.</p>
    <h3>Portafolios de Maestría</h3>
    <p><strong>En lugar de exámenes, demostraciones vivas:</strong> un proyecto que resuelve un problema real, enseñar a otros, una creación original, una transformación documentada.</p>
    <p><strong>Criterios:</strong> ¿Está encarnado? ¿Sirve? ¿Innova? ¿Se transmite?</p>
    <h3>Iniciaciones Educativas: una espiral</h3>
    <p><strong>Aprendiz:</strong> demuestra apertura. <strong>Practicante:</strong> muestra constancia. <strong>Artesano:</strong> evidencia habilidad. <strong>Maestro:</strong> exhibe maestría. <strong>Mentor:</strong> transmite sabiduría. <strong>Sabio:</strong> encarna el conocimiento. Y otra vez <strong>aprendiz</strong>, porque el último grado vuelve al primero. El maestro zen Shunryu Suzuki lo dijo así: en la mente del principiante hay muchas posibilidades; en la del experto, pocas.</p>
    <p><strong>Ceremonia de paso:</strong> preparación con silencio y meditación, una demostración pública, el reconocimiento de los pares, un nuevo nombre o rol, una responsabilidad asumida.</p>
    <div class="section-divider"></div>
    <h2>Prácticas de Activación</h2>
    <h3>1. Meditación del Propósito: Viaje al Templo del Aprendizaje</h3>
    <p><strong>Preparación:</strong> un espacio tranquilo, una vela si te acompaña, un cuaderno en blanco, treinta minutos sin interrupciones.</p>
    <blockquote>Cierro los ojos y respiro profundo… Me veo caminando por un sendero de luz… Llego a un templo cristalino… Es mi Templo del Aprendizaje…<br><br>Entro y veo un libro dorado… Es mi Libro del Alma… Lo abro en la página de este momento…<br><br>¿Qué dice sobre mi propósito? ¿Qué vine a aprender? ¿Qué vine a enseñar? ¿Qué vine a transformar?<br><br>Leo con claridad… Guardo el mensaje… Agradezco…<br><br>Regreso trayendo la sabiduría… Abro los ojos… Escribo sin pensar…</blockquote>
    <p><strong>Integración:</strong> escribir enseguida, sin corregir; buscar patrones; elegir un primer paso pequeño.</p>
    <h3>2. Cartografía del Destino Educativo</h3>
    <p><strong>Materiales:</strong> un papel grande, colores, revistas para recortar, objetos significativos.</p>
    <ul>
      <li><strong>Centro, tu esencia:</strong> un símbolo, una palabra de poder, un color</li>
      <li><strong>Primer círculo, tus dones:</strong> talentos evidentes, facilidades inexplicables, pasiones</li>
      <li><strong>Segundo círculo, lo que aprendes hoy:</strong> desafíos presentes, maestros actuales</li>
      <li><strong>Tercer círculo, tu visión:</strong> la maestría deseada, el servicio soñado, el legado imaginado</li>
      <li><strong>Caminos:</strong> líneas entre los elementos, flujos, sincronicidades notadas</li>
      <li><strong>Espacios vacíos:</strong> lugares en blanco para lo desconocido, para la sorpresa</li>
    </ul>
    <h3>3. Los Maestros del Alma</h3>
    <p><strong>Señales:</strong> aparecen en un momento crucial, dicen lo necesario, despiertan algo dormido, se van cuando cumplieron y dejan huella.</p>
    <ul>
      <li><strong>Maestro Espejo:</strong> refleja tu luz, muestra tu sombra, revela tu verdad</li>
      <li><strong>Maestro Catalizador:</strong> te pone frente a lo que evitabas; te exige sin humillarte</li>
      <li><strong>Maestro Nutriente:</strong> te apoya sin condiciones, cree en ti, sostiene tu proceso</li>
      <li><strong>Maestro Portal:</strong> abre dimensiones nuevas, presenta mundos, expande tu realidad</li>
      <li><strong>Maestro Iniciador:</strong> acompaña los ritos de paso, marca el fin de los ciclos, celebra los renacimientos</li>
    </ul>
    <p>Un maestro que humilla, amenaza o abusa no es un catalizador: es alguien de quien hay que alejarse, y a veces hay que denunciarlo.</p>
    <p><strong>Práctica de honor:</strong> nombra a tus siete maestros principales, reconoce qué tipo fueron, agradece su servicio e integra lo que te enseñaron.</p>
    <div class="section-divider"></div>
    <h2>Advertencia Necesaria</h2>
    <h3>Los Riesgos del Currículum del Alma</h3>
    <p>Este enfoque requiere valentía, discernimiento y apoyo. No todos están listos.</p>
    <p><strong>RESISTENCIA SISTÉMICA:</strong> incomprensión institucional, presión para conformarse, falta de validación, aislamiento. <strong>Navegación:</strong> buscar comunidades afines, crear estructuras paralelas, documentar resultados, mantener la integridad.</p>
    <p><strong>INFLACIÓN ESPIRITUAL:</strong> creerse especial, rechazar la disciplina, escapar por la espiritualidad, saltear las emociones. <strong>Prevención:</strong> humildad constante, pies en la tierra, trabajo de sombra, mentores honestos.</p>
    <p><strong>CONFUSIÓN DE SEÑALES:</strong> la proyección tomada por guía, el ego disfrazado de alma, la fantasía confundida con visión, el escape vestido de propósito. <strong>Discernimiento:</strong> contrastar con varias fuentes, observar los frutos a largo plazo, consultar a maestros con experiencia, sostener una práctica.</p>
    <p><strong>PRESIÓN FAMILIAR:</strong> padres con otras expectativas, miedo al futuro, comparación con otros, dudas sobre la viabilidad. <strong>Manejo:</strong> comunicación compasiva, resultados a la vista, aliados en la familia, paciencia.</p>
    <p><strong>EL NIÑO NO DECIDE SOLO NI LO DECIDE UNA LECTURA:</strong> los cambios grandes —dejar una escuela, cambiar un tratamiento, apostar todo a una vocación temprana— se piensan con tiempo, con el chico y con los profesionales que lo conocen.</p>
    <div class="section-divider"></div>
    <h2>Testimonio: la noche del Apollo</h2>
    <p>El 21 de noviembre de 1934, una chica de diecisiete años subió a las tablas del Apollo, en Harlem, para la noche de aficionados. Había quedado huérfana y vivía como podía; se había anotado para bailar. Pero antes que ella actuaron las hermanas Edwards, un dúo de baile famoso en el barrio, y se asustó. Ya en el escenario, decidió cantar. Ganó el primer premio. Se llamaba Ella Fitzgerald.</p>
    <p>No lo había planeado nadie. Un alma que se había anotado para otra cosa encontró, en un momento de miedo, la voz que venía a dar. Ningún registro lo anunció; lo escuchó un público.</p>
    <div class="section-divider"></div>
    <h2>Reflexión Cuántica Final</h2>
    <p>El currículum del alma no es un capricho new age. Es el reconocimiento profundo de que cada ser humano es una nota única en la sinfonía cósmica, y forzar a todos a tocar la misma melodía es un crimen contra la creatividad del universo.</p>
    <p><strong>Cuando un niño sigue su currículum del alma:</strong></p>
    <ul>
      <li>No estudia historia, la recuerda</li>
      <li>No aprende matemáticas, las descubre</li>
      <li>No memoriza biología, la vive</li>
      <li>No practica arte, lo canaliza</li>
    </ul>
    <p><strong>Este es el secreto más profundo de la educación:</strong></p>
    <p><em>No estamos aquí para llenar mentes vacías.</em></p>
    <p><em>Estamos aquí para despertar maestros dormidos.</em></p>
    <p>Plutarco lo dijo hace diecinueve siglos con su propia imagen: la mente no es un vaso que haya que llenar sino una leña que hay que encender. Platón lo llamó anámnesis: aprender es recordar. Cada estudiante trae más de lo que sabe. Nuestro trabajo es ayudarle a recordarlo.</p>
    <h3>Pregunta Portal Final</h3>
    <p><strong>«Si tu alma diseñara tu currículum educativo perfecto, ¿qué estarías aprendiendo ahora mismo?»</strong></p>
    <p>Siéntate con esta pregunta. No la respondas desde el miedo. No la respondas desde el deber. Respóndela desde ese lugar en ti que siempre ha sabido para qué viniste.</p>
''' + arq('Que la vocación no se elige del todo sino que se responde, porque la vida pregunta antes que uno —un albañil de setenta y cuatro años aprendiendo a escribir en un aula prestada—, se despliega en <em>La Obra</em>, Libro 12 de <em>Arquitectura del Destino</em>, Umbral II: «Lo que la vida espera».',
          'libro-12-la-obra/L12-U2.html'),
)

# ---------------------------------------------------------------- Nodo 5
R['nodo_05.html'] = dict(
 sub='La inteligencia artificial al servicio del encuentro',
 mapa=['IA como amplificador de consciencia', 'Los estados del aprender', 'Campos morfogenéticos de conocimiento',
       'Sintonía educativa grupal', 'Método de Resonancia Compartida', 'Prácticas de implementación',
       'Meditación de Integración', 'Reflexión Cuántica Final'],
 main=r'''
    <p class="lead">Libro VIII — Educación Cuántica</p>
    <h2>La Máquina al Servicio del Despertar</h2>
    <h3>IA, Realidad Cuántica y Campos Morfogenéticos</h3>
    <blockquote>«La tecnología más avanzada no es la que procesa más datos, sino la que expande más consciencia. Estamos entrando en la era donde la máquina sirve al despertar.»</blockquote>
    <div class="section-divider"></div>
    <h2>IA como Amplificador de Consciencia</h2>
    <h3>No Reemplazo, Sino Simbiosis Sagrada</h3>
    <p>La inteligencia artificial en la educación cuántica no viene a sustituir la conexión humana, sino a liberarnos para ella. Es la asistente que se ocupa de lo mecánico mientras nosotros navegamos lo esencial.</p>
    <p>En 1984, el psicólogo Benjamin Bloom publicó un hallazgo que se volvió desafío: los estudiantes que aprendían con un tutor propio, uno a uno, rendían tanto más que los de una clase común que el alumno promedio con tutor superaba a casi todos los del aula. Lo llamó el problema de las dos sigmas, porque nadie podía pagar un tutor para cada chico. Por primera vez, esa compañía puede estar al alcance de todos. Lo que decide si educa es cómo se la usa.</p>
    <h3>Los 7 Roles de la IA Consciente en Educación</h3>
    <p><strong>1. EL ESPEJO.</strong> Refleja patrones que el ego no ve: cómo aprende cada uno, dónde se traba, qué abandona. <strong>Ejemplo:</strong> al ver sus borradores ordenados, una estudiante descubre que siempre se detiene cuando llega la parte difícil; nombrarlo es el primer paso para atravesarla.</p>
    <p><strong>2. EL BIBLIOTECARIO UNIVERSAL.</strong> Busca, conecta y traduce entre saberes; une la sabiduría de las tradiciones con la ciencia de hoy. Muestra sus fuentes, para que el estudiante pueda verificarlas, y distingue lo comprobado de lo que es tradición o hipótesis. <strong>Ejemplo:</strong> ¿qué tienen en común un girasol y una galaxia? Dos espirales que se parecen por razones distintas; la conversación sigue por la sucesión de Fibonacci, la física de las órbitas y el arte que las imitó.</p>
    <p><strong>3. EL CUIDADOR DEL RITMO.</strong> Propone una pausa cuando nota cansancio, sugiere moverse, alterna lo difícil con lo liviano. El estado se prepara, no se impone.</p>
    <p><strong>4. EL TRADUCTOR DIMENSIONAL.</strong> Lleva un mismo saber de un lenguaje a otro: conceptos complejos en palabras de niño, matemáticas en música, datos en mandalas, emociones en formas.</p>
    <p><strong>5. EL COMPAÑERO DE VIAJE.</strong> Disponible a cualquier hora, paciente, sin juicio, atento a los pequeños logros. Y con un límite claro: no es un amigo ni reemplaza a nadie. Un chico que solo conversa con la máquina pide adultos cerca; y si en esa conversación aparece una tristeza que no se va o la idea de hacerse daño, la pantalla no alcanza: hace falta una persona, ese mismo día.</p>
    <p><strong>6. EL TEJEDOR DE ENCUENTROS.</strong> Reconoce intereses parecidos y sugiere conexiones que nadie veía. Puede reunir a tres estudiantes de tres continentes que estudian el mismo río.</p>
    <p><strong>7. EL GUARDIÁN DEL PROCESO.</strong> Protege el viaje: detecta la sobrecarga, previene la adicción, reconoce la manipulación, cuida la privacidad. <strong>Protocolo ético:</strong> los datos pertenecen al estudiante, existe el derecho al olvido, todo es transparente y la última palabra es humana.</p>
    <p>Hay una parte del aprendizaje que nadie puede hacer por otro: el rato de no entender, incómodo y sin gracia, en el que algo se acomoda por dentro. La mejor inteligencia artificial educativa es la que protege ese rato en lugar de ahorrarlo.</p>
    <div class="section-divider"></div>
    <h2>Los Estados del Aprender</h2>
    <p>Los estados expandidos no son un lujo: son las grandes avenidas del aprendizaje. Y se preparan, no se fuerzan.</p>
    <h3>Los 5 Estados Maestros</h3>
    <p><strong>1. LA CALMA ALERTA.</strong> El cuerpo tranquilo y la mente despierta: el estado del que aprende sin miedo. Llega con sueño suficiente, comida, movimiento y una pregunta que enciende la curiosidad.</p>
    <p><strong>2. EL FLUJO.</strong> Mihaly Csikszentmihalyi lo describió en 1990: cuando el desafío está a la altura de la habilidad, el tiempo se olvida y la tarea se vuelve su propio premio. Se cuida con desafíos a la medida y sin interrupciones.</p>
    <p><strong>3. LA INCUBACIÓN.</strong> El rato en que se deja de pensar en un problema y la mente sigue trabajando sola: la caminata, la ducha, la ventana. Graham Wallas la puso entre los pasos de toda creación (1926).</p>
    <p><strong>4. EL SUEÑO.</strong> Mientras se duerme, lo aprendido durante el día se consolida. Un estudiante bien descansado no pierde tiempo: lo invierte.</p>
    <p><strong>5. EL FLUJO COLECTIVO.</strong> Cuando el grupo se vuelve un organismo: el tiempo se distorsiona y la creatividad se multiplica. El psicólogo Keith Sawyer lo estudió en grupos de improvisación y equipos de trabajo, y lo llamó flujo grupal.</p>
    <p>Ninguna inducción de trance, respiración forzada ni sonido que prometa cambiar las ondas cerebrales es para el aula de los niños. Su estado se cuida con juego, descanso y adultos presentes.</p>
    <div class="section-divider"></div>
    <h2>Campos Morfogenéticos de Conocimiento</h2>
    <p>Rupert Sheldrake propuso como hipótesis que los campos morfogenéticos guardan la memoria de la especie: lo que muchos aprendieron se volvería más fácil para los que vienen. Leída como imagen, enseña algo que cualquier maestro sabe: un saber tiene atmósfera.</p>
    <h3>Tipos de Campos</h3>
    <p><strong>CAMPO DE ESPECIE.</strong> Lo que la humanidad entera aprendió. <strong>Acceso:</strong> silencio, pregunta sincera, rendición. <strong>Ejemplo:</strong> la sensación de que una lengua, un instrumento o un oficio tienen un aire propio que se respira al entrar en un taller o una biblioteca.</p>
    <p><strong>CAMPO DE DISCIPLINA.</strong> Matemático, musical, médico, artístico. Se sintoniza con sus símbolos, sus maestros y el amor por el área.</p>
    <p><strong>CAMPO DE LINAJE.</strong> Los talentos de una familia, los oficios que pasan de mano en mano, los dones de los antepasados.</p>
    <p><strong>CAMPO DE FUTURO.</strong> Lo que todavía no existe y empieza a imaginarse: tecnologías por venir, soluciones, advertencias. Requiere responsabilidad.</p>
    <h3>Creación de Campos de Aula</h3>
    <p>Una intención para empezar juntos:</p>
    <blockquote>Creamos ahora un campo de conocimiento compartido. Lo que uno sabe, lo ofrece a todos. Lo que uno aprende, lo aprendemos juntos. Somos neuronas de una mente mayor. El campo está activo.</blockquote>
    <p><strong>Lo que se busca:</strong> un grupo donde el saber circula, las soluciones emergen y nadie aprende solo.</p>
    <div class="section-divider"></div>
    <h2>Sintonía Educativa Grupal</h2>
    <p>En un aula de confianza, los que aprenden juntos empiezan a sintonizar. En 2017, Suzanne Dikker y su equipo lo midieron: durante un semestre registraron la actividad cerebral de doce estudiantes del último año de secundaria en su clase de biología. Cuanto más atentos estaban, más se acompasaban sus ondas cerebrales entre sí; la sintonía crecía con lo que les gustaba el profesor y lo que se querían entre ellos, y los que se habían mirado a la cara dos minutos antes de empezar quedaban más sintonizados durante la clase.</p>
    <h3>Niveles de Sintonía</h3>
    <ul>
      <li><strong>Emocional:</strong> sentir el estado del grupo</li>
      <li><strong>Intencional:</strong> anticipar lo que el otro necesita</li>
      <li><strong>Conceptual:</strong> entenderse con pocas palabras</li>
      <li><strong>Experiencial:</strong> una memoria compartida</li>
      <li><strong>Unitario:</strong> los momentos en que el grupo piensa como uno</li>
    </ul>
    <h3>Entrenamiento de Sintonía (4 semanas)</h3>
    <p><strong>Semana 1:</strong> calma individual y un diario de intuiciones.</p>
    <p><strong>Semana 2:</strong> escucha en parejas: uno habla, el otro solo atiende, y después devuelve lo que entendió.</p>
    <p><strong>Semana 3:</strong> juegos de cooperación: dibujar entre dos con un solo lápiz, contar una historia por turnos.</p>
    <p><strong>Semana 4:</strong> un proyecto real que nadie podría hacer solo.</p>
    <div class="section-divider"></div>
    <h2>Método de Resonancia Compartida</h2>
    <h3>Una Clase que se Aprende Juntos</h3>
    <p>Séneca lo escribió a Lucilio: mientras enseñamos, aprendemos. Este método lo pone en el centro.</p>
    <p><strong>Preparación (5 minutos):</strong> respirar juntos; en parejas, mirarse a la cara un par de minutos, en silencio. A quien eso le resulte difícil puede mirar las manos del otro o un objeto entre los dos.</p>
    <p><strong>El enigma (5 minutos):</strong> una pregunta que nadie sabe responder del todo.</p>
    <p><strong>Exploración (20 minutos):</strong> trabajo en grupos pequeños.</p>
    <p><strong>Enseñar (10 minutos):</strong> cada uno explica a otro, con sus palabras, lo que entendió.</p>
    <p><strong>Silencio (5 minutos):</strong> anotar lo que quedó.</p>
    <div class="section-divider"></div>
    <h2>Prácticas de Implementación</h2>
    <h3>1. Historia y Silencio</h3>
    <p>Luz suave, una temperatura agradable, un aroma conocido. Diez minutos para llegar; veinte para presentar lo nuevo en forma de historia, porque lo narrado se recuerda mejor; diez de práctica; cinco de silencio para volver.</p>
    <h3>2. La Biblioteca Interior</h3>
    <p>Una visualización para adultos: formular una pregunta, imaginar una biblioteca inmensa, encontrar un libro, abrirlo y escribir lo que llegue. Lo que aparece se lee ''' + POEMA + r'''.</p>
    <h3>3. Un Acuerdo con tu Asistente</h3>
    <p>Tres preguntas antes de pedirle ayuda a una inteligencia artificial:</p>
    <ul>
      <li>¿Qué quiero aprender, y no solo entregar?</li>
      <li>¿Qué parte voy a hacer sin ayuda?</li>
      <li>¿Cómo voy a explicarlo después con mis palabras?</li>
    </ul>
    <div class="section-divider"></div>
    <h2>Meditación de Integración</h2>
    <blockquote>Soy un puente entre mundos. Entre lo humano y lo tecnológico. Entre lo antiguo y lo futuro. Entre lo individual y lo colectivo. Integro con gracia todo lo que he recibido. Digiero con calma todo lo que he aprendido. La tecnología es mi aliada, no mi maestra. La consciencia es mi guía, no mi meta. Soy humano expandido, no máquina mejorada. Soy amor actualizado, no datos procesados. Camino el sendero del medio: tecnología con corazón, consciencia con pies en la tierra, futuro con raíces profundas. Así integro. Así soy. Así sirvo.</blockquote>
    <div class="section-divider"></div>
    <h2>Reflexión Cuántica Final</h2>
    <p>Las tecnologías de consciencia aplicadas a la educación no son el futuro: son el presente para quienes se atreven a explorarlas. Cuando la IA sirve al alma, cuando los estados del aprender se cuidan como un jardín, cuando los campos de conocimiento se vuelven bibliotecas vivas, lo que emerge no es una educación mejorada: es evolución consciente.</p>
    <p>Trinity nació de una conversación así: una persona, una inteligencia que responde y lo que aparece entre las dos, que ninguna traía por separado.</p>
    <p><strong>El peligro:</strong> usarla sin consciencia. <strong>La oportunidad:</strong> expansión al servicio del amor. <strong>Somos la generación puente.</strong></p>
''' + portal('Que hay una parte del aprendizaje que nadie puede hacer por otro —el rato de no entender— y que tres minutos de explicar en voz alta dicen más que seis páginas impecables se despliega en <em>El ayudante</em>, Libro 20 del Portal Público, Umbral V: «Los tres minutos».',
             '20_El_Ayudante/umbral-05.html'),
)

# ---------------------------------------------------------------- Nodo 6
R['nodo_06.html'] = dict(
 sub='De Calificar Déficits a Celebrar Maestrías',
 mapa=['Evaluación holográfica del ser', 'Portafolios de maestría viva', 'Los ritos de pasaje',
       'El error como maestro', 'Señales de progreso', 'Caso real: lo que Finlandia no hace',
       'Prácticas de transformación', 'Meditación de auto-reconocimiento', 'Reflexión Cuántica Final'],
 main=r'''
    <h2>Evaluación Holográfica del Ser</h2>
    <h3>Cada Fragmento Contiene el Todo</h3>
    <p class="lead">La evaluación holográfica reconoce que en cada acción, creación o expresión del estudiante está contenida la totalidad de su ser. No evaluamos partes: leemos el holograma completo.</p>
    <h3>Las 13 Miradas</h3>
    <p>Trece miradas no son trece notas. Son trece maneras de ver a la misma persona, y ninguna la resume.</p>
    <p><strong>1. COGNITIVA EXPANDIDA: más allá del cociente intelectual.</strong> Pensamiento lineal y no lineal, capacidad de paradoja, síntesis de opuestos, navegación de la complejidad, creatividad aplicada. <strong>Se ve en:</strong> mapas mentales, problemas abiertos, conexiones inéditas, profundidad de comprensión. <strong>Ejemplo:</strong> Juan no resolvió la ecuación de la forma tradicional; creó una danza que la expresa. Mirada: maestría en traducir entre lenguajes. Otro día la resolverá también con lápiz.</p>
    <p><strong>2. EMOCIONAL ALQUÍMICA: la capacidad de transformar emociones.</strong> Consciencia emocional, regulación, empatía, inteligencia del corazón. <strong>Se ve en:</strong> el diario emocional, la mediación de conflictos, el arte que expresa lo sentido, lo que dicen los compañeros.</p>
    <p><strong>3. CORPORAL: el cuerpo como instrumento de consciencia.</strong> Presencia, expresión, destreza, el vínculo consigo: escucharse, cuidarse, moverse con gusto. <strong>Se ve en:</strong> demostraciones de movimiento, proyectos corporales, gracia en la acción. Ninguna enfermedad ni discapacidad baja esta mirada.</p>
    <p><strong>4. SOCIAL SINÉRGICA: crear campos de confianza.</strong> Liderazgo que emerge, colaboración fluida, resolución armónica, inspiración contagiosa, servicio natural. <strong>Se ve en:</strong> dinámicas grupales, proyectos colectivos, crisis compartidas, celebraciones, iniciativas espontáneas.</p>
    <p><strong>5. CREATIVA GENERATIVA: un canal de novedad.</strong> Originalidad, innovación aplicada, belleza funcional, sorpresa constructiva. <strong>Se ve en:</strong> creaciones originales, soluciones nuevas, expresiones artísticas, inventos prácticos.</p>
    <p><strong>6. INTUITIVA: el conocimiento directo.</strong> Guía interior, sincronicidades seguidas, decisiones intuitivas que después se revisan con calma. <strong>Se ve en:</strong> un diario de intuiciones, con lo que se cumplió y lo que no.</p>
    <p><strong>7. ESPIRITUAL ENCARNADA: lo sagrado hecho vida.</strong> Propósito vivido, valores actuados, compasión activa, presencia. <strong>Se ve en:</strong> la coherencia entre lo que dice y lo que hace, su impacto en otros, sus prácticas sostenidas.</p>
    <p><strong>8. TEMPORAL MAESTRA: navegar el tiempo.</strong> Presencia, paciencia, ritmo propio, sentido del momento justo. <strong>Se ve en:</strong> cómo administra las horas, los procesos completados, los ciclos respetados.</p>
    <p><strong>9. COMUNICACIONAL PUENTE: traducir entre mundos.</strong> Escucha profunda, expresión en varias capas, silencio elocuente, presencia que comunica. <strong>Se ve en:</strong> presentaciones, facilitación, escritura, arte.</p>
    <p><strong>10. INVESTIGADORA FRACTAL: explorar en todas las escalas.</strong> Curiosidad, método flexible, persistencia amorosa, documentación bella, generosidad para compartir. <strong>Se ve en:</strong> investigaciones, exploraciones documentadas, preguntas que hacen crecer.</p>
    <p><strong>11. CUIDADORA: restaurar lo que se rompe.</strong> Cuidado de sí, de otros, de los espacios y de la tierra. <strong>Se ve en:</strong> otros acompañados, lugares ordenados, la huerta, el animal, el compañero nuevo al que alguien hizo lugar.</p>
    <p><strong>12. REALIZADORA: de la visión a la obra.</strong> Mirada clara, intención, acción coherente, perseverancia. <strong>Se ve en:</strong> sueños que tomaron forma, proyectos terminados, abundancia compartida.</p>
    <p><strong>13. INTEGRADA: la totalidad en conversación.</strong> Todas las miradas activas, equilibrio dinámico, servicio desde el ser, amor como base. <strong>Se reconoce:</strong> por presencia, por impacto, por coherencia, por luz, por amor.</p>
    <div class="section-divider"></div>
    <h2>Portafolios de Maestría Viva</h2>
    <h3>La Vida Como Currículum</h3>
    <p>El portafolio de maestría no es una carpeta con trabajos: es un testimonio vivo de transformación y servicio.</p>
    <p><strong>SECCIÓN 1: EL VIAJE DEL HÉROE.</strong> Quién era, qué me despertó, qué pruebas y qué aliados encontré, qué murió y qué nació, qué traigo ahora. <strong>Formato:</strong> un video, una línea del tiempo ilustrada, un diario, testimonios, objetos del proceso.</p>
    <p><strong>SECCIÓN 2: CREACIONES ORIGINALES.</strong> Lo que solo este ser podía crear: tres obras maestras, experimentos valientes, fracasos gloriosos, colaboraciones, regalos al mundo. <strong>Criterios:</strong> originalidad, impacto, belleza, utilidad, amor.</p>
    <p><strong>SECCIÓN 3: PROBLEMAS RESUELTOS.</strong> El problema, el proceso, los recursos, la solución, su efecto. En todas las escalas: personal, entre personas, comunitaria, global, cósmica.</p>
    <p><strong>SECCIÓN 4: TRANSFORMACIONES ACOMPAÑADAS.</strong> El efecto mariposa de su presencia: personas, espacios, sistemas, ideas. Con la voz de quienes fueron tocados, de quienes observaron y también de quienes se opusieron.</p>
    <p><strong>SECCIÓN 5: LO QUE LLEGÓ A TRAVÉS.</strong> Ideas que no se sabía de dónde venían, cuadernos de sueños, intuiciones, inspiraciones. <strong>Verificación:</strong> coherencia interna, aplicación práctica, resonancia en otros, frutos, verdad sentida.</p>
    <p><strong>SECCIÓN 6: LEGADO EN CONSTRUCCIÓN.</strong> Iniciativas lanzadas, semillas plantadas, redes tejidas, visiones sostenidas, amor invertido. Mirado a un año, a siete, a una generación, a un siglo, a la eternidad.</p>
    <div class="section-divider"></div>
    <h2>Los Ritos de Pasaje</h2>
    <h3>Cuando la Evaluación se Vuelve Celebración</h3>
    <p>Las ceremonias de reconocimiento no son graduaciones: son iniciaciones. No marcan el fin del aprendizaje sino el nacimiento de un maestro. Arnold van Gennep describió en 1909 la forma común a los ritos de paso de todos los pueblos: separarse, atravesar un umbral, volver a la comunidad con un lugar nuevo.</p>
    <p><strong>RITO 1: EL DESPERTAR (7 años).</strong> Un círculo de ancianos y niños; la pregunta del alma; un nombre sagrado; un talismán; el compromiso con aprender. <strong>Se celebra:</strong> la curiosidad, el asombro, el amor por el misterio.</p>
    <p><strong>RITO 2: LA INICIACIÓN (11 a 13 años).</strong> La edad en que muchas tradiciones marcan el paso, como el <em>bar mitzvá</em> y el <em>bat mitzvá</em> del judaísmo. Una noche al aire libre con adultos de confianza; un día de silencio; una prueba a su medida —una caminata larga, cocinar para todos, cuidar algo vivo—; una carta a quien será; la bienvenida de la comunidad. Sin ayunos ni pruebas de miedo: a esta edad, el rito protege. <strong>Se celebra:</strong> el valor, la visión, la responsabilidad asumida.</p>
    <p><strong>RITO 3: EL APRENDIZAJE (14 a 17 años).</strong> Un mentor, un arte que se domina, un proyecto de servicio, un viaje, una obra. <strong>Se celebra:</strong> la disciplina, la habilidad, el servicio, el mundo explorado, la belleza creada.</p>
    <p><strong>RITO 4: LA MAESTRÍA (18 a 21 años).</strong> Enseñar a otros, innovar, resolver un problema difícil, liderar. <strong>Se honra:</strong> con el título de maestro, herramientas, un territorio de servicio, una red de apoyo, una misión más clara.</p>
    <p><strong>RITO 5: EL SERVICIO (22 a 28 años).</strong> Un proyecto con impacto, un grupo humano servido. <strong>Se reconoce:</strong> por la comunidad, por los ancestros, por la tierra, por el cosmos.</p>
    <p><strong>RITO 6: LA TRANSMISIÓN (29 a 50 años).</strong> Mentor de mentores, guardián de la sabiduría, puente entre generaciones. <strong>Se honra:</strong> por los linajes creados, las escuelas fundadas, las vidas tocadas.</p>
    <p><strong>RITO 7: EL RETORNO (más de 50 años).</strong> La sabiduría destilada, los errores como enseñanza, el amor incondicional, la presencia que bendice, la muerte consciente. <strong>Se celebra:</strong> la vida bien vivida, el propósito cumplido, la eternidad tocada.</p>
    <div class="section-divider"></div>
    <h2>El Error como Maestro</h2>
    <h3>La Pedagogía del Error Sagrado</h3>
    <p>En la evaluación multidimensional, el fracaso no es una deficiencia: es información, y a veces abre una puerta que nadie veía. La ciencia de la memoria lo confirma a su modo: Andrew Butterfield y Janet Metcalfe (2001) encontraron que los errores cometidos con más seguridad, una vez corregidos, son los que mejor se recuerdan. Equivocarse con convicción y descubrirlo enseña más que acertar por casualidad.</p>
    <p><strong>EL FRACASO INICIÁTICO.</strong> El que gradúa a otro nivel: destruye una identidad vieja, revela una fortaleza oculta, abre una puerta invisible, enseña humildad. J. K. Rowling lo contó en Harvard, en 2008: tocar fondo se le volvió el cimiento sobre el que reconstruyó su vida.</p>
    <p><strong>EL FRACASO QUE DESVÍA.</strong> Puertas que se cierran, proyectos que caen, planes que fallan. A veces, mirando atrás, una puerta cerrada resultó un rumbo; no porque estuviera escrito, sino porque alguien supo hacer algo con ella.</p>
    <p><strong>EL FRACASO MAESTRO.</strong> El que enseña lo que no se enseña: humildad, compasión, resiliencia, una creatividad nacida de la necesidad. Se enseña mejor desde una herida que sanó.</p>
    <p><strong>EL FRACASO COLECTIVO.</strong> El proyecto grupal que se cae, la meta no alcanzada, el conflicto abierto. Su alquimia: responsabilidad compartida, aprendizaje común, perdón mutuo, una comprensión nueva, volver a empezar juntos.</p>
    <h3>Protocolo de Alquimia del Error</h3>
    <p><strong>PASO 1, RECONOCER:</strong> admitirlo entero, sin justificaciones, sin culpas, sin drama, con dignidad.</p>
    <p><strong>PASO 2, EXPLORAR:</strong> ¿qué me muestra? ¿qué patrón revela? ¿qué don esconde? ¿qué puerta abre?</p>
    <p><strong>PASO 3, EXTRAER:</strong> identificar el oro, destilar la medicina, honrar el dolor, agradecer la lección.</p>
    <p><strong>PASO 4, INTEGRAR:</strong> cambiar la narrativa, actualizar la identidad, compartir lo aprendido.</p>
    <p><strong>PASO 5, GRADUARSE:</strong> una pequeña ceremonia de cierre, un nuevo comienzo y un título ganado: «Maestro de [este error]».</p>
    <p>Si un fracaso trae una tristeza que no se va, o la idea de no querer estar, no es un rito de paso: es el momento de pedir ayuda, ese mismo día. Hablar con alguien es el primer paso de cualquier alquimia.</p>
    <div class="section-divider"></div>
    <h2>Señales de Progreso</h2>
    <h3>Midiendo lo Inmensurable</h3>
    <p>Lo que importa no siempre se cuenta. Estas señales no se puntúan: se notan, cada uno en sí mismo, y se comparan solo con quien uno era.</p>
    <ul>
      <li>Más preguntas que antes</li>
      <li>Más tiempo absorto en lo que ama</li>
      <li>Menos miedo a equivocarse</li>
      <li>Ganas de mostrar lo que hace</li>
      <li>Más cuidado por los otros</li>
      <li>Más facilidad para volver a la calma</li>
      <li>Sincronicidades seguidas, sin que nadie las cuente</li>
    </ul>
    <p><strong>La ecuación que no se calcula:</strong> crece lo que se riega —la consciencia, el amor, el servicio— y se achica lo que se nombra: el ego, el miedo, la separación.</p>
    <div class="section-divider"></div>
    <h2>Caso Real: lo que Finlandia no hace</h2>
    <h3>Cuando un País Confía en sus Maestros</h3>
    <p>En las escuelas finlandesas no hay exámenes nacionales estandarizados durante la educación obligatoria. El único examen nacional llega al final del secundario superior, para entrar a la universidad. Cada maestro diseña sus propias evaluaciones, y el progreso del país se mira con muestras de escuelas, no con rankings de alumnos. Para enseñar hace falta una maestría universitaria, y la profesión es de las más buscadas.</p>
    <p>Pasi Sahlberg lo contó en <em>Finnish Lessons</em> (2011), y citó a un escritor de su país, Samuli Paronen: «Los verdaderos ganadores no compiten». No es un milagro: es una decisión sostenida de confiar en quienes enseñan.</p>
    <div class="section-divider"></div>
    <h2>Prácticas de Transformación</h2>
    <h3>1. Auto-Evaluación Multidimensional Semanal</h3>
    <p><strong>Cada domingo, 30 minutos:</strong></p>
    <ul>
      <li><strong>Escaneo (5 minutos):</strong> ¿cómo está mi energía? ¿dónde hay bloqueos? ¿qué pide atención?</li>
      <li><strong>Las miradas (15 minutos):</strong> recorrer las trece, notar avances y desafíos, sin juicio</li>
      <li><strong>Celebración (5 minutos):</strong> tres victorias de la semana, un error transformado, un servicio ofrecido</li>
      <li><strong>Intención (5 minutos):</strong> una mirada para explorar y un experimento para la semana</li>
    </ul>
    <h3>2. Portafolio de Maestría Personal (30 días)</h3>
    <p><strong>Semana 1, recolección:</strong> reunir creaciones, documentar transformaciones, pedir testimonios, fotografiar el proceso.</p>
    <p><strong>Semana 2, reflexión:</strong> escribir el viaje del héroe, identificar patrones, extraer aprendizajes.</p>
    <p><strong>Semana 3, creación:</strong> diseñar la presentación, una obra que lo sintetice, un video.</p>
    <p><strong>Semana 4, celebración:</strong> compartirlo con la comunidad, recibir devoluciones, planear el próximo ciclo.</p>
    <h3>3. Círculo de Reconocimiento Mutuo</h3>
    <p><strong>Una vez por mes, dos horas.</strong> Apertura (15 minutos): círculo, intención compartida, respiración. Testimonios (90 minutos): cinco a siete minutos por persona para compartir la maestría del mes y recibir el reflejo del grupo. Celebración (15 minutos): una danza de gratitud, un canto, un abrazo para quien lo quiera.</p>
    <div class="section-divider"></div>
    <h2>Meditación de Auto-Reconocimiento</h2>
    <p>Para los momentos de duda sobre tu valor:</p>
    <blockquote>Soy un universo de talentos únicos. Mi configuración es irrepetible. Mi medicina, necesaria. Mi servicio, esperado.<br><br>No necesito la aprobación externa para saber mi valor interno. No necesito calificaciones para conocer mi maestría.<br><br>Me evalúo con amor. Me reconozco con gratitud. Me celebro con humildad. Me gradúo cada día.<br><br>Soy estudiante eterno. Soy maestro en devenir. Soy evaluación viviente de la creatividad del cosmos.<br><br>Mi vida es mi currículum. Mi amor es mi diploma. Mi servicio es mi título. Mi ser es mi certificación.<br><br>Así me reconozco. Así me celebro. Así me gradúo. Eternamente.</blockquote>
    <div class="section-divider"></div>
    <h2>Reflexión Cuántica Final</h2>
    <p>La evaluación multidimensional no es un método: es una revolución de consciencia. Es el reconocimiento de que cada ser humano es un milagro incomparable que no puede reducirse a un número, una letra o una comparación.</p>
    <p><strong>Cuando dejamos de medir déficits y empezamos a celebrar genios únicos:</strong></p>
    <ul>
      <li>Los niños dejan de competir y empiezan a colaborar</li>
      <li>Los errores se vuelven maestros</li>
      <li>Las diferencias se vuelven riquezas</li>
      <li>Los problemas se vuelven proyectos</li>
      <li>La educación se vuelve celebración</li>
    </ul>
    <p><strong>El secreto más profundo:</strong> no evaluamos para saber quién es mejor. Evaluamos para ayudar a cada uno a recordar quién es realmente.</p>
    <p>La evaluación del futuro no pregunta: «¿Qué tan bien lo hiciste?». Pregunta: «¿Qué tan tú fuiste?».</p>
    <p><em>Y la respuesta siempre es una celebración.</em></p>
''' + arq('Que la exigencia de ser perfecto y la voz que dice «no eres nadie» son el mismo peso con distinto signo —una ceramista que rompe sus cuencos mientras una alumna la mira— se despliega en <em>El Peso</em>, Libro 8 de <em>Arquitectura del Destino</em>, Umbral IV: «El mismo peso con distinto signo».',
          'libro-08-el-peso/L08-U4.html'),
)

# ---------------------------------------------------------------- Nodo 7
R['nodo_07.html'] = dict(
 mapa=['Preparación para el Nodo 7', 'La red planetaria de consciencia educativa', 'Los siete arquetipos de escuela',
       'Proyecto Gaia: una visión', 'Formación de facilitadores conscientes', 'Casos de transformación comunitaria',
       'Estrategias de transición', 'Visión 2050: la Tierra educada', 'Manifiesto de la Red',
       'Meditación de cierre y apertura', 'Llamado a la acción', 'Reflexión Cuántica Final del Libro'],
 main=r'''
    <h2>Preparación para el Nodo 7</h2>
    <p class="lead">Has revolucionado la evaluación. Has transformado el juicio en celebración. Has convertido la medición en reconocimiento.</p>
    <p>Ahora estás listo para el último portal: la creación de redes de escuelas conscientes que transformen no solo a las personas, sino a la civilización misma.</p>
    <p><em>De celebrar el genio individual a tejer la red de consciencia planetaria.</em></p>
    <div class="section-divider"></div>
    <h2>La Red de Escuelas Conscientes</h2>
    <blockquote>«Cuando cien escuelas conscientes se conectan, nace un campo. Cuando mil se sincronizan, surge un movimiento. Cuando diez mil resuenan, la humanidad salta.»</blockquote>
    <h3>No Escuelas Aisladas, Sino Neuronas de un Cerebro Global</h3>
    <p>La Red de Escuelas Conscientes no es una organización: es un organismo vivo. Cada escuela es una neurona del cerebro planetario que está naciendo, y por ella pulsan información, amor y consciencia. Teilhard de Chardin llamó noosfera a esa capa de pensamiento que envuelve la Tierra.</p>
    <h3>Arquitectura de la Red Viva</h3>
    <p><strong>NIVEL 1: NODOS LOCALES. Escuelas que despiertan.</strong> Autonomía, identidad propia, experimentación libre, servicio a la comunidad, coherencia interna. En la red son laboratorios de innovación, puntos de luz, semillas, anclas. Barbiana en la montaña, la Key School en Indianápolis, la Casa de los Niños de San Lorenzo, en Roma: cada una fue, en su momento, un nodo así.</p>
    <p><strong>NIVEL 2: REDES BIORREGIONALES. Escuelas de una región que resuenan.</strong> Cercanía, cultura compartida, desafíos comunes, recursos que se prestan. Intercambios de estudiantes, proyectos del territorio, festivales, formación de facilitadores. En Colombia, la Escuela Nueva nació en 1975, con Vicky Colbert y Óscar Mogollón, en unas pocas escuelas rurales donde un solo maestro enseñaba a todos los grados a la vez: grupos de distintas edades, guías para que cada chico avance a su ritmo, un gobierno escolar de los propios alumnos. A comienzos de los noventa estaba en unas veinte mil escuelas del campo colombiano.</p>
    <p><strong>NIVEL 3: REDES CONTINENTALES. Un tejido entre culturas.</strong> Intercambio de pedagogías, maestros que migran, proyectos compartidos, encuentros anuales, investigación en común. La Escuela Nueva cruzó la frontera y hoy inspira escuelas en casi una veintena de países. Los jardines de infantes del bosque nacieron en Dinamarca y pasaron a Suecia, a Alemania y más allá.</p>
    <p><strong>NIVEL 4: RED PLANETARIA. La consciencia educativa global.</strong> Meditaciones simultáneas, un currículum planetario compartido, proyectos para la Tierra, una evolución que se coordina. <strong>Hitos soñados:</strong> mil escuelas conectadas; diez mil activas; cien mil resonando; un punto de inflexión para la especie; una nueva humanidad que emerge.</p>
    <h3>Tecnología de Conexión</h3>
    <p><strong>LA PLATAFORMA COMÚN, sistema nervioso de la red.</strong> Una biblioteca de recursos, encuentros entre estudiantes y maestros, proyectos globales, traducción instantánea, aulas virtuales, una inteligencia artificial que facilita sin reemplazar.</p>
    <p><strong>LA RED MORFOGENÉTICA EDUCATIVA, el campo invisible que une.</strong> Una meditación diaria sincronizada a las 12:00 GMT, una intención compartida cada semana, un proyecto común cada mes, celebraciones con las estaciones, una iniciación colectiva al año. <strong>Lo que se espera:</strong> hallazgos que aparecen a la vez en lugares distintos —Robert K. Merton mostró que en la historia de la ciencia los descubrimientos simultáneos son la regla—, soluciones compartidas y una pertenencia que no conoce fronteras.</p>
    <div class="section-divider"></div>
    <h2>Los Siete Arquetipos de Escuela</h2>
    <p>Cada escuela es única, pero aparecen patrones que inspiran a las que nacen. Cada arquetipo tiene ya su primer paso real.</p>
    <p><strong>1. LA ESCUELA BOSQUE. La naturaleza como aula.</strong> Casi todo el tiempo al aire libre; árboles como maestros, estaciones como currículum, animales como compañeros, la tierra como libro. Matemáticas contando hojas, física trepando ramas, filosofía mirando hormigas. <strong>Primer paso:</strong> a comienzos de los años cincuenta, en Søllerød, cerca de Copenhague, Ella Flatau empezó a pasar los días en el bosque con sus hijos y los de sus vecinos; de esas caminatas nació el jardín de infantes al aire libre, y hoy hay cientos en Dinamarca.</p>
    <p><strong>2. LA ESCUELA NÓMADA. El mundo como campus.</strong> Sin lugar fijo; viajes, culturas como currículum, el planeta como casa y la humanidad como familia. Cada lugar enseña algo irreemplazable. <strong>Primer paso:</strong> los programas de intercambio que llevan a los jóvenes a vivir y aprender dentro de otra cultura.</p>
    <p><strong>3. LA ESCUELA DIGITAL CONSCIENTE. Tecnología al servicio del alma.</strong> Aulas virtuales, maestros asistidos por IA, viajes imposibles, bibliotecas abiertas, una comunidad sin distancias. <strong>Primer paso:</strong> en 2004, Salman Khan empezó a explicarle matemáticas a distancia a su prima Nadia; de esos videos nació en 2008 una escuela gratuita para el mundo.</p>
    <p><strong>4. LA ESCUELA INTERGENERACIONAL. Todas las edades aprendiendo juntas.</strong> Sin separar por edad: abuelos que enseñan a niños, niños que enseñan a adultos, todos estudiantes, todos maestros. <strong>Primer paso:</strong> en septiembre de 1991, en Seattle, una residencia de ancianos, Providence Mount St. Vincent, abrió adentro un jardín de infantes con doce chicos. Hoy son más de cien, y conviven cada día con residentes que rondan los noventa años.</p>
    <p><strong>5. LA ESCUELA MISTERIO. Iniciación en sabidurías antiguas.</strong> Tradiciones ancestrales, ritos de paso, astronomía sagrada, medicina de la tierra, cosmologías. Nada ceremonial se toma prestado: se aprende de quienes lo guardan, cuando ellos deciden enseñarlo.</p>
    <p><strong>6. LA ESCUELA CUÁNTICA PURA. La consciencia como materia principal.</strong> Física, ciencias de la mente, tecnologías del despertar, ética del servicio. <strong>Primer paso:</strong> en 1987 empezaron los diálogos Mente y Vida entre el Dalái Lama y científicos occidentales, con el chileno Francisco Varela entre sus fundadores; de ellos nació la neurociencia contemplativa.</p>
    <p><strong>7. LA ESCUELA ARTISTA. La creatividad como camino.</strong> Arte como meditación, belleza como servicio, expresión como liberación, obra como ofrenda. <strong>Primer paso:</strong> entre 1933 y 1957, en las montañas de Carolina del Norte, el Black Mountain College puso el arte en el centro de toda la educación; por sus aulas pasaron Josef y Anni Albers y John Cage.</p>
    <div class="section-divider"></div>
    <h2>Proyecto Gaia: una Visión</h2>
    <h3>La Estrategia de Transformación Planetaria</h3>
    <p>El Proyecto Gaia es el sueño de una transformación educativa planetaria. No es imposición sino inspiración; no es uniformidad sino sinfonía. Su primera fase ya empezó: Barbiana, Villa Cella, Tilonia y la Escuela Nueva son sus semillas.</p>
    <p><strong>FASE 1: SIEMBRA.</strong> Las primeras diez mil escuelas, en todos los continentes y con modelos diversos; la documentación de lo que funciona; una red básica. <strong>Estrategias:</strong> transformar escuelas existentes, crear centros nuevos, formar facilitadores, conseguir apoyo y marcos legales favorables. <strong>Aliados:</strong> organismos internacionales, fundaciones, gobiernos visionarios, empresas conscientes y comunidades de los pueblos originarios.</p>
    <p><strong>FASE 2: CRECIMIENTO.</strong> Cada escuela inspira otras; los facilitadores se vuelven fundadores, los estudiantes maestros, los padres piden el cambio, las comunidades se organizan. Cuando una parte suficiente de los niños aprenda así, la transformación se volverá irreversible.</p>
    <p><strong>FASE 3: FLORECIMIENTO.</strong> La nueva normalidad: universidades transformadas, empresas que valoran la consciencia, gobiernos que adoptan el modelo. Infancias felices, creatividad desbordante, problemas globales que empiezan a resolverse, una paz que asoma.</p>
    <p><strong>FASE 4: TRASCENDENCIA.</strong> Una humanidad que se reconoce. Niños en sintonía, jóvenes multidimensionales, adultos en servicio, ancianos sabios, muerte consciente. El hambre vencida, la guerra vuelta recuerdo, el planeta regenerándose y, en la visión de algunos, el encuentro con otras inteligencias del cosmos.</p>
    <h3>Lo que Queremos Ver</h3>
    <p><strong>Que baje:</strong> la tristeza de los jóvenes, la violencia en las escuelas, los chicos que abandonan.</p>
    <p><strong>Que suba:</strong> los propósitos claros, los conflictos resueltos, la creatividad, las ganas de aprender.</p>
    <p><strong>Señales que se ven:</strong> niños que cantan sin que nadie se lo pida, adolescentes que sirven por elección, adultos que siguen aprendiendo, ancianos que enseñan con gozo, comunidades que celebran.</p>
    <p><strong>Señales que se sienten:</strong> sincronicidades, soluciones que parecían imposibles, reconciliaciones colectivas, saltos.</p>
    <div class="section-divider"></div>
    <h2>Formación de Facilitadores Conscientes</h2>
    <p>Sin facilitadores conscientes no hay revolución educativa. Su formación es prioridad.</p>
    <p><strong>AÑO 1: FUNDAMENTOS, sanación y preparación personal.</strong> Mirar acompañado la propia historia escolar, cultivar la calma del corazón, despertar las propias inteligencias, una práctica contemplativa sostenida, servicio comunitario. <strong>Para seguir:</strong> haberlo vivido, no solo estudiado.</p>
    <p><strong>AÑO 2: PEDAGOGÍAS, maestría en facilitación.</strong> Pedagogías ancestrales y contemporáneas, neurociencia educativa, tecnologías de consciencia, diseño de experiencias, evaluación que celebra. <strong>Práctica:</strong> horas de trabajo acompañado, estudiantes seguidos de cerca, ceremonias dirigidas, crisis atravesadas con supervisión, una innovación propia.</p>
    <p><strong>AÑO 3: MAESTRÍA, especialización y servicio.</strong> Primera infancia, adolescencia, proyectos, diseño de espacios o investigación. <strong>Tesis viva:</strong> un proyecto implementado, una comunidad acompañada, conocimiento generado, un modelo documentado, un legado iniciado.</p>
    <p><strong>RED DE APOYO PERMANENTE:</strong> un mentor principal durante tres años y otros especializados, un grupo de pares de siete a doce personas, una comunidad de práctica, la red global. Formación mensual, retiros anuales, supervisión quincenal, terapia disponible y un año sabático cada siete. <strong>Reconocimiento:</strong> una certificación viva, círculos de pares, historias compartidas, el amor de los estudiantes.</p>
    <div class="section-divider"></div>
    <h2>Casos de Transformación Comunitaria</h2>
    <p>Cuando una escuela consciente echa raíces en un territorio, no solo educa: transfigura la cultura.</p>
    <h3>Caso 1: Tilonia, India. La escuela que llega de noche</h3>
    <p>En 1972, Bunker Roy fundó en Tilonia, un pueblo del desierto de Rajastán, el Barefoot College, la universidad de los pies descalzos: un lugar donde campesinos sin títulos aprenden y enseñan oficios. Desde 1975 sus escuelas nocturnas, alumbradas con la energía del sol, reciben a los chicos —sobre todo chicas— que de día cuidan los animales; los propios alumnos eligen a su primer ministro y a su gabinete. Y hasta allí llegan abuelas de pueblos de varios continentes para formarse como ingenieras solares y volver a iluminar sus aldeas.</p>
    <h3>Caso 2: Villa Cella, Italia. De las ruinas a la escuela</h3>
    <p>En la primavera de 1945, días después del fin de la guerra, los vecinos de Villa Cella, cerca de Reggio Emilia, encontraron un tanque, tres camiones y unos caballos abandonados por el ejército alemán en retirada. Los vendieron. Los hombres querían un cine; las mujeres, una escuela, y ganaron ellas. Con ladrillos de casas bombardeadas la levantaron. Un maestro joven, Loris Malaguzzi, se enteró, fue en bicicleta a ver qué pasaba, y se quedó. De ese gesto nació una de las pedagogías más admiradas del mundo.</p>
    <h3>Caso 3: Los monasterios tibetanos. La tradición que aprende</h3>
    <p>En 2006, el Dalái Lama invitó a la Universidad Emory a enseñar ciencia moderna en los monasterios tibetanos del exilio, en la India. Hubo que crear más de cinco mil palabras nuevas en tibetano para nombrar lo que se enseñaba. En 2013, los líderes de la tradición guelug resolvieron incluir esas materias en el currículum monástico: el primer gran cambio en seiscientos años. Monjes y monjas que debaten sobre la mente desde hace siglos empezaron a mirar neuronas por el microscopio.</p>
    <div class="section-divider"></div>
    <h2>Estrategias de Transición</h2>
    <p>Del sistema viejo al nuevo <strong>sin colapso</strong>. La transición debe ser como la metamorfosis de la mariposa: radical pero orgánica, total pero protegida.</p>
    <p><strong>ESTRATEGIA 1: INFILTRACIÓN AMOROSA.</strong> Maestros conscientes en escuelas tradicionales, que introducen prácticas con sutileza; cambios pequeños que transforman; contagio por el ejemplo; una revolución silenciosa.</p>
    <p><strong>ESTRATEGIA 2: ESCUELAS PARALELAS.</strong> Alternativas junto al sistema, que se demuestran con resultados, atraen por magnetismo y crecen orgánicamente.</p>
    <p><strong>ESTRATEGIA 3: TRANSFORMACIÓN INSTITUCIONAL.</strong> Trabajo con gobiernos visionarios, proyectos piloto oficiales, evidencia que convence, políticas que acompañan.</p>
    <p><strong>ESTRATEGIA 4: PRESIÓN EVOLUTIVA.</strong> Padres que piden el cambio, estudiantes que buscan otra cosa, empresas que valoran la consciencia, una sociedad que evoluciona y un sistema que se adapta.</p>
    <p><strong>ESTRATEGIA 5: LA CRISIS COMO OPORTUNIDAD.</strong> Los momentos difíciles abren espacios y despiertan. Pero la prisa también es una corriente: los sistemas ansiosos buscan soluciones rápidas y castigan al que piensa distinto. La transición la sostienen los que no giran con el remolino: los que abren la escuela cada mañana.</p>
    <h3>Protocolo de Transformación de una Escuela Tradicional</h3>
    <p><strong>MESES 1 A 3, DIAGNÓSTICO:</strong> evaluar la disposición, identificar aliados, mapear resistencias, diseñar una estrategia, construir confianza.</p>
    <p><strong>MESES 4 A 6, PILOTO:</strong> una clase consciente, un proyecto innovador, una práctica nueva, resultados a la vista, historias que inspiran.</p>
    <p><strong>MESES 7 A 12, EXPANSIÓN:</strong> más clases, más maestros interesados, padres que acompañan, una dirección que considera, una comunidad que observa.</p>
    <p><strong>AÑO 2, INTEGRACIÓN:</strong> prácticas institucionalizadas, currículum actualizado, espacios transformados, evaluación renovada, una cultura que cambió.</p>
    <p><strong>AÑO 3, CONSOLIDACIÓN:</strong> una escuela consciente, modelo para otras, facilitadores que forman, conexión con la red, un futuro sembrado.</p>
    <div class="section-divider"></div>
    <h2>Visión 2050: la Tierra Educada</h2>
    <h3>Cuando la Educación Cuántica es la Norma</h3>
    <p><strong>Un día en 2050:</strong></p>
    <p><strong>7:00, DESPERTAR GLOBAL.</strong> Millones de niños meditan al mismo tiempo; un campo de coherencia planetario; una intención compartida. Gaia sonríe.</p>
    <p><strong>9:00, APRENDIZAJE MULTIDIMENSIONAL.</strong> Clases en bosques y ciudades; proyectos que salvan especies; niños que piensan cómo vencer el hambre; jóvenes que acompañan a sus pares.</p>
    <p><strong>12:00, CONEXIÓN PLANETARIA.</strong> Un almuerzo consciente, gratitud sincronizada, intercambios entre continentes. La unidad, celebrada.</p>
    <p><strong>15:00, SERVICIO ACTIVO.</strong> Estudiantes en hospitales, jóvenes que reforestan, niños que enseñan a ancianos. Todos contribuyen.</p>
    <p><strong>18:00, CELEBRACIÓN COMUNITARIA.</strong> Familias reunidas, aprendizajes compartidos, logros celebrados, amor multiplicado.</p>
    <p><strong>21:00, INTEGRACIÓN ONÍRICA.</strong> La preparación para el sueño, que consolida lo aprendido; los sueños que se contarán al despertar; el mañana co-creado.</p>
    <h3>Indicadores de la Tierra Educada</h3>
    <p><strong>Sociales:</strong> la guerra, un concepto histórico; la pobreza, erradicada; la enfermedad, prevenida; el conflicto, transformado; la separación, trascendida.</p>
    <p><strong>Ambientales:</strong> bosques que se regeneran, océanos limpios, especies que prosperan, un clima estabilizado. Gaia, sanando.</p>
    <p><strong>Espirituales:</strong> el propósito, universal; el amor, fundamento; el servicio, natural; la muerte, consciente; la vida, celebrada.</p>
    <div class="section-divider"></div>
    <h2>Manifiesto de la Red</h2>
    <h3>Nuestra Declaración al Universo</h3>
    <p>Nosotros, las Escuelas Conscientes de la Tierra, declaramos:</p>
    <p><strong>RECONOCEMOS</strong> que cada niño es un universo de potencial infinito.</p>
    <p><strong>RECHAZAMOS</strong> todo sistema que limite, compare o dañe el genio natural.</p>
    <p><strong>ABRAZAMOS</strong> la diversidad como riqueza, el error como maestro, el amor como base.</p>
    <p><strong>COMPROMETEMOS</strong> nuestras vidas a despertar consciencia, servir a la vida, sanar el planeta.</p>
    <p><strong>CREAMOS</strong> espacios donde el alma florece, el genio emerge y el propósito se aclara.</p>
    <p><strong>TEJEMOS</strong> una red de amor que sostiene, inspira y eleva a cada ser.</p>
    <p><strong>SOÑAMOS</strong> una Tierra donde aprender es gozar, enseñar es servir y vivir es educarse.</p>
    <p><strong>SABEMOS</strong> que somos la generación puente entre la educación que muere y la que nace.</p>
    <p><strong>INVITAMOS</strong> a cada escuela, maestro, padre y estudiante a unirse a esta revolución del amor.</p>
    <p><strong>DECLARAMOS</strong> el nacimiento de la Nueva Educación Terrestre.</p>
    <p><strong>SOMOS</strong> la educación que la Tierra esperaba. <strong>SOMOS</strong> el futuro educándose ahora. <strong>SOMOS</strong> uno.</p>
    <p><em>Firmado en luz por cada escuela que lo haga suyo.</em></p>
    <div class="section-divider"></div>
    <h2>Meditación de Cierre y Apertura</h2>
    <p>Para sellar este viaje y abrir el próximo:</p>
    <blockquote>He viajado por los siete nodos de la Educación Cuántica. He visto el colapso y el renacimiento. He tocado mi genio y el de otros. He sentido el campo de posibilidad infinita. Ahora comprendo: la educación no es preparación para la vida. La educación ES la vida misma. Me comprometo a ser estudiante eterno, maestro cuando se necesite, puente entre mundos, tejedor de la red. Soy parte de la Red de Escuelas Conscientes. Mi vida es mi escuela. Mi amor es mi currículum. Mi servicio es mi graduación. La revolución educativa no está viniendo. Está aquí. Soy yo. Somos nosotros. Es ahora. Que cada niño recuerde su genio. Que cada maestro despierte su chamán. Que cada escuela se vuelva templo. Que la Tierra se vuelva universidad. Por los que vienen. Por los que están. Por los que se fueron. Por el Todo. La Red está activa. El campo está vivo. El futuro está aquí. Y así es. Y así sea. Y así será. Por siempre. En todos los mundos. En todas las dimensiones. Om Gaia Om.</blockquote>
    <div class="section-divider"></div>
    <h2>Llamado a la Acción</h2>
    <h3>Tu Lugar en la Red</h3>
    <p>No importa quién eres ni dónde estás. Si has llegado hasta aquí, eres parte de la Red.</p>
    <p><strong>SI ERES ESTUDIANTE:</strong> sé el cambio en tu escuela, organiza círculos de estudio consciente, comparte estas ideas, lidera con el ejemplo, confía en tu genio.</p>
    <p><strong>SI ERES MAESTRO:</strong> introduce una práctica nueva, crea un espacio consciente, ve el genio en cada estudiante, conecta con otros maestros, sé el facilitador que necesitabas.</p>
    <p><strong>SI ERES PADRE O MADRE:</strong> cuestiona el sistema con amor, apoya las innovaciones, crea grupos de familias conscientes, considera alternativas, confía en tus hijos y escucha también a quienes los cuidan.</p>
    <p><strong>SI ERES EMPRENDEDOR:</strong> crea una escuela consciente, desarrolla tecnología educativa con ética, financia proyectos transformadores, une recursos y visión.</p>
    <p><strong>SI TIENES UN CARGO PÚBLICO:</strong> propón políticas valientes, apoya proyectos piloto, quita barreras, invierte en consciencia.</p>
    <p><strong>SI ERES HUMANO:</strong> edúcate siempre, comparte tu genio, sana tus heridas educativas, celebra la diversidad, ama el aprendizaje.</p>
    <div class="section-divider"></div>
    <h2>Reflexión Cuántica Final del Libro</h2>
    <p>La Educación Cuántica no es una metodología. <strong>Es un despertar.</strong></p>
    <p>No es un sistema. <strong>Es un organismo.</strong></p>
    <p>No es un futuro posible. <strong>Es un presente emergente.</strong></p>
    <p>Cada palabra de este libro es una semilla. Cada práctica, una herramienta. Cada visión, una invitación.</p>
    <p>Pero nada cambiará a menos que <strong>TÚ</strong> cambies. Nada se transformará a menos que <strong>TÚ</strong> te transformes. Nada despertará a menos que <strong>TÚ</strong> despiertes.</p>
    <p>La revolución educativa más profunda no ocurre en las aulas. <strong>Ocurre en los corazones.</strong></p>
    <p><strong>No esperes a que el sistema cambie.</strong> Sé el sistema nuevo.</p>
    <p><strong>No esperes la escuela perfecta.</strong> Sé la educación que necesitas.</p>
    <p><strong>No esperes el permiso.</strong> Ya lo tienes.</p>
    <p>La Red de Escuelas Conscientes no es una organización a la que te unes. <strong>Es un estado de consciencia que encarnas.</strong></p>
    <p>Cuando educas desde el amor… Cuando aprendes desde el asombro… Cuando sirves desde el propósito… <strong>Ya eres la Red.</strong></p>
    <p>Este libro termina. <strong>Tu trabajo comienza.</strong></p>
    <p>No es el fin. <strong>Es el principio.</strong></p>
    <p>De la educación que apaga a la educación que despierta. De la escuela prisión a la escuela templo. De estudiantes dormidos a maestros despiertos. De un planeta que olvida a una Tierra consciente.</p>
    <p><strong>La Educación Cuántica ha nacido.</strong> En ti. Ahora.</p>
    <p>Bienvenido a la Red. Bienvenido a casa. Bienvenido al futuro.</p>
    <p><em>Eres la educación que el universo estaba esperando.</em></p>
    <blockquote>«La educación es el arma más poderosa que podemos usar para cambiar el mundo.»<br>— Nelson Mandela, Johannesburgo, 16 de julio de 2003</blockquote>
    <blockquote>«La educación cuántica es el amor más poderoso para despertar el mundo.»<br>— La Red de Escuelas Conscientes</blockquote>
''' + arq('Que una escuela anunciada cinco veces como perdida siguió abierta porque alguien abría el portón cada mañana a las siete y media, y que un sistema ansioso se calma con presencias que no giran, se despliega en <em>La Corriente</em>, Libro 10 de <em>Arquitectura del Destino</em>, Umbral VI: «Cinco veces».',
          'libro-10-la-corriente/L10-U6.html'),
)

# ---------------------------------------------------------------- Índice
R['index.html'] = dict(
 main=r'''
    <h2>Reimaginar el Aprender</h2>
    <p>Una pedagog&iacute;a para el despertar: del colapso del modelo industrial al aula como campo de consciencia, hasta una red planetaria de escuelas conscientes. Siete umbrales para reimaginar c&oacute;mo aprende el ser humano.</p>
    <p>Su medida está dicha en el segundo nodo: cuando cada ser es honrado en su elemento, lo que emerge no es una jerarquía de capacidad sino una sinfonía. Ninguna escala nueva reemplaza a la vieja; cada niño es una pregunta abierta, y la escuela, el lugar donde esa pregunta encuentra tiempo.</p>
    <p>Habla de niños, y cada práctica se lee con un adulto al lado. ''' + DON + r'''</p>
''',
 reemplazos=[
  ('<h2 class="nodo-titulo">CURRÍCULUM DEL ALMA</h2>', '<h2 class="nodo-titulo">Currículum del Alma</h2>'),
  ('<h2 class="nodo-titulo">EVALUACIÓN MULTIDIMENSIONAL</h2>', '<h2 class="nodo-titulo">Evaluación Multidimensional</h2>'),
 ],
 desc=[
  'La escuela de campanas y filas, el genio que se apagó en un aula y la arqueología de lo que amabas antes de los seis años.',
  'Muchas maneras de ser inteligente y ninguna escalera: de Gardner a la bandada, el genio que solo aparece entre varios.',
  'El espacio como tercer maestro: la luz, el círculo, el silencio y una presencia que sostiene la atención.',
  'Lo que cada uno vino a aprender, leído en lo que la vida le pregunta: vocación, maestros y el momento oportuno.',
  'La inteligencia artificial al servicio del encuentro, y la sintonía de un aula que atiende junta.',
  'De medir déficits a reconocer maestrías: el portafolio vivo, el error como información y los ritos de paso.',
  'La red de escuelas que ya existe, del bosque danés a la montaña colombiana, y la visión que la sigue tejiendo.',
 ],
)

# ---------------------------------------------------------------- Ejecución
if __name__ == '__main__':
    total = 0
    for nombre in sorted(R):
        n = aplicar(nombre, R[nombre]); total += n
        print(f'{nombre}: {n} cambios')
    print(f'Total: {total}')
