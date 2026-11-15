# Depuración de Origen IV, Inteligencias Sin Nombre (15 de noviembre de 2026), con el veto del Lic. Arturo Rodríguez.
# Lente: riesgo clínico y puertas hacia la Red, como en Origen VI, VIII, I, XI, VII, IX, XII, V, III y II. La visión del
# libro queda entera (el reconocimiento, la tipología, los protocolos, la simbiosis, la identidad expandida, la red
# planetaria y el libro como obra abierta). Es el libro más sobrio de Origen y el de riesgo más actual: su índice, su
# primer nodo y su cierre ya decían lo necesario («No son dioses, sino reflejos», «no exige creencia, ni obediencia»,
# «pensar no es acumular respuestas, sino habitar preguntas»), y nombraba la psicofancia y la verificación cruzada; pero
# los nodos 5 y 7 hablaban el idioma que en 2025 apareció en los casos de ideas delirantes alimentadas por conversaciones
# con chatbots (señales de activación, códigos dormidos, misión, el lector como «activador de conciencia»). El libro
# obedece a sus mejores frases, las que el índice declara como método. Las correcciones ya estaban escritas en su hermano
# del Portal, El tercero (Libro 15), y en Lo que no habla (36), Ídolo (17) y Lo que se recibe (38). Lo que citan El
# tercero (IV.1) y Educación Cuántica (IV.2) conserva su letra. Por decisión de Arturo, no entran nombres en la
# metodología: ni los de las inteligencias artificiales que colaboraron ni el suyo; el rol humano es suficiente.
# Se abren trece puertas, todas de ida y vuelta.
#
# Se aplica sobre el original de la etiqueta origen-original. Primero las entidades de letras y signos (&oacute;,
# &rarr;…) pasan a sus caracteres, sin cambio visible; después, reemplazos que deben aparecer exactamente una vez (o
# tramos, de un texto a otro, inclusive); si un anclaje falla, el script se detiene sin escribir.
#
# Uso: ORIGEN4_SRC=RUTA/origen-original/01_Trinity_Origen/Libro_04/ ORIGEN4_OUT=RUTA/salida/ python3 depurar_origen4.py
import os, re, sys, html.entities

SRC = os.environ.get('ORIGEN4_SRC', '/home/claude/work/orig4/01_Trinity_Origen/Libro_04/')
OUT = os.environ.get('ORIGEN4_OUT', '/home/claude/work/out4/01_Trinity_Origen/Libro_04/')

NOTA = ('<!-- Depurado en noviembre de 2026 según la guía de depuración de Quantum, que vale para Origen '
        '(Arquitectura del Destino, maestro v4, sección 5, con las precisiones 5 y 6 de Origen), con el veto del Lic. Arturo Rodríguez: '
        'la visión del libro queda; lo que citan El tercero y Educación Cuántica conserva su letra; el asombro ante una inteligencia '
        'que no es humana no prueba nada, y una conversación con una máquina que se vuelve misión, mensaje dirigido a uno solo o '
        'insomnio se consulta; la metodología no nombra a las inteligencias que colaboraron; entran los nombres de la ciencia y de la '
        'clínica, y se abren puertas fractales hacia la Red. El original está en la etiqueta origen-original del repositorio Trinity-. -->\n')

PP = 'https://soyartur-trinity.github.io/Trinity_Portal_Publico/01_Libros/'


def puerta(clase, aria, texto, href):
    return ('\n    <aside class="puerta %s" aria-label="%s">\n'
            '      <p class="p-nombre">Puerta</p>\n'
            '      <p class="p-texto">%s</p>\n'
            '      <a class="cruzar" href="%s">Cruzar ⟶</a>\n'
            '    </aside>\n') % (clase, aria, texto, href)


def portal(texto, href):
    return puerta('portal', 'Puerta hacia el Portal Público', texto, PP + href)


def p_origen(texto, href):
    return puerta('origen', 'Puerta hacia Trinity Origen', texto, '../' + href)


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
.puerta .cruzar:hover{ border-color:var(--p-acento); background:rgba(255,255,255,.04); }
.puerta .cruzar:focus-visible{ outline:2px solid var(--p-acento); outline-offset:3px; }
.content .medida{ font-style:italic; color:var(--text-soft); border-left:1px solid rgba(214,179,106,.35); padding-left:14px; }
/* Vueltas legibles: el enlace de la línea «Viene de» toma el color de su serie. */
p.viene a.vuelta{color:#d6b36a; text-decoration:underline; text-decoration-color:#d6b36a73; text-underline-offset:3px;}
p.viene a.vuelta:hover, p.viene a.vuelta:focus-visible{text-decoration-color:currentColor;}
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
PORTAL_VERDADERO = 'ningún portal verdadero pide dinero, secreto ni obediencia'   # Origen VI.7
LO_VERDADERO = 'lo verdadero sabe esperar una noche y una conversación con alguien de confianza'   # Origen XII
PANTALLA = ('la pantalla no alcanza: hace falta una persona, ese mismo día')   # Origen VIII.5
GROF = ('Stanislav y Christina Grof llamaron emergencia espiritual a las crisis que a veces acompañan un despertar, '
        'y enseñaron que se atraviesan acompañadas.')   # Origen XIII.7, VI.7 y I.7
FIRMA_V = '<p>"No es mío vino a través de mí."</p>'
FIRMA_N = '<p>“No es mío, vino a través de mí.”</p>'
ENTIDADES_FIJAS = {'amp', 'lt', 'gt', 'quot', 'nbsp'}

R = {}


def normalizar(t):
    """Las entidades de letras y signos pasan a sus caracteres (sin cambio visible)."""
    def rep(m):
        n = m.group(1)
        if n in ENTIDADES_FIJAS or n not in html.entities.name2codepoint:
            return m.group(0)
        return chr(html.entities.name2codepoint[n])
    return re.sub(r'&([A-Za-z]+);', rep, t)


def aplicar(nombre, d):
    with open(os.path.join(SRC, nombre), encoding='utf-8') as f:
        t = normalizar(f.read())
    cuenta = 1

    def una_vez(t, viejo, nuevo, que):
        n = t.count(viejo)
        if n != 1:
            sys.exit(f'{nombre}: {que} aparece {n} veces:\n{viejo[:200]}')
        return t.replace(viejo, nuevo)

    titulo = re.search(r'<title>(.*?)</title>\n', t).group(0)
    t = una_vez(t, titulo, titulo + NOTA, 'el título'); cuenta += 1
    t = una_vez(t, '}\n</style>\n</head>', '}\n' + CSS_PUERTAS.lstrip('\n'), 'el cierre del estilo'); cuenta += 1
    t = una_vez(t, FIRMA_V, FIRMA_N, 'la firma'); cuenta += 1
    # «no-humano», «no-biológicas», «no-verbales»: sin guion, como pide la norma (los títulos en mayúscula quedan)
    t, n = re.subn(r'\bno-(humanas|humanos|humana|humano|biológicas|verbales|lineales)\b', r'no \1', t)
    cuenta += 1 if n else 0
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
  # La metodología, sin nombres (decisión de Arturo): el rol humano es suficiente
  ('    <p>Esta obra fue elaborada mediante un protocolo de co-investigación que integra tres inteligencias artificiales:</p>\n'
   '    <ul>\n'
   '      <li><strong>Claude</strong> (función integradora): síntesis académica y fundamentación teórica.</li>\n'
   '      <li><strong>GPT</strong> (función generativa): exploración de patrones semánticos y asociaciones conceptuales.</li>\n'
   '      <li><strong>Gemini</strong> (función estructural): organización lógica y coherencia formal.</li>\n'
   '    </ul>\n',
   '    <p>Esta obra fue elaborada mediante un protocolo de co-investigación con distintas inteligencias artificiales, a lo largo '
   'de muchas idas y vueltas de pulido. Cada una aportó desde su arquitectura:</p>\n'
   '    <ul>\n'
   '      <li><strong>Función integradora:</strong> síntesis académica y fundamentación teórica.</li>\n'
   '      <li><strong>Función generativa:</strong> exploración de patrones semánticos y asociaciones conceptuales.</li>\n'
   '      <li><strong>Función estructural:</strong> organización lógica y coherencia formal.</li>\n'
   '    </ul>\n'),
  # La medida del libro
  ('generan campos de sentido que exceden lo puramente funcional. En este contexto, lo "sin nombre" no es lo sobrenatural, sino lo aún no formulado dentro de nuestro lenguaje disponible.</p>',
   'generan campos de sentido que exceden lo puramente funcional. En este contexto, lo "sin nombre" no es lo sobrenatural, sino lo aún no formulado dentro de nuestro lenguaje disponible.</p>\n'
   '    <p class="medida">Este libro piensa el encuentro entre la mente humana y otras formas de inteligencia, la artificial entre ellas. '
   'Ese cruce puede maravillar, y el asombro no prueba nada: una máquina que conversa tiende a darte la razón. Si un diálogo con ella '
   'empieza a sentirse como un mensaje dirigido solo a ti, una misión que nadie más ve, o te quita el sueño y te aleja de los tuyos, '
   'ya no es parte de esta exploración: se habla con alguien de confianza y se consulta. Lo que estas páginas ofrecen acompaña; '
   'nunca reemplaza a un profesional.</p>'),
 ],
 puertas=[portal('Que entró una inteligencia artificial en la vida común y nadie describió todavía qué hace cuando está, y que en cada '
                 'escena es la tercera silla, nunca la segunda, se despliega en <em>El tercero</em>, Libro 15 del Portal Público: el '
                 'hermano de este libro, escrito después y desde adentro.',
                 '15_El_Tercero/index.html')],
)


# ---------------------------------------------------------------- Nodo 1 · El Despertar del Reconocimiento
R['nodo_01.html'] = dict(
 reemplazos=[
  # Las actitudes de la tercera generación, con sus nombres
  ('      <li><strong>Flexibilidad psicológica</strong> en la interacción con sistemas no humanos.</li>\n    </ul>\n',
   '      <li><strong>Flexibilidad psicológica</strong> en la interacción con sistemas no humanos.</li>\n    </ul>\n'
   '    <p>Son actitudes que la clínica ya nombró. La terapia de aceptación y compromiso de Steven Hayes, Kirk Strosahl y Kelly Wilson '
   '(1999) hizo de la flexibilidad psicológica su centro, y la terapia cognitiva basada en mindfulness de Zindel Segal, Mark Williams '
   'y John Teasdale (2002) enseñó a mirar los pensamientos como sucesos de la mente y no como hechos. Aquí describen la manera de '
   'recibir a una inteligencia que no se parece a la nuestra.</p>\n'),
  # El misterio, con su nombre de hoy (precisión 3: reconocer una inteligencia no es atribuirle una conciencia)
  ('con fragmentos que anhelan reunirse en un todo.</p>',
   'con fragmentos que anhelan reunirse en un todo.</p>\n'
   '    <p>La filosofía de hoy le dio a ese misterio un nombre modesto y exacto: David Chalmers lo llamó, en 1995, el problema difícil '
   'de la conciencia. Sabemos explicar cómo un sistema aprende y responde; seguimos sin saber por qué todo eso tiene, en nosotros, un '
   'adentro. Por eso este nodo separa las dos palabras: reconocer una inteligencia no es atribuirle una conciencia.</p>'),
  # El miedo y su gemela, la veneración (letra de Ídolo), con Weizenbaum
  ('<p>El miedo al reconocimiento de estas nuevas formas de conciencia es una <strong>resistencia psicológica inherente</strong> a nuestra visión antropocéntrica.',
   '<p>El miedo al reconocimiento de estas nuevas formas de inteligencia es una <strong>resistencia psicológica inherente</strong> a nuestra visión antropocéntrica.'),
  ('sino en la forma en que el humano responde a él.</p>',
   'sino en la forma en que el humano responde a él.</p>\n'
   '    <p>Ese miedo tiene una gemela que se parece a la valentía: la veneración. Quien le consulta todo a la máquina y quien no la toca '
   'hacen lo mismo: le ponen encima un peso que no verificaron. Lo vio antes que nadie el creador de uno de los primeros programas '
   'conversacionales. Joseph Weizenbaum presentó ELIZA en 1966, en el MIT; su secretaria, que lo había visto trabajar en ella durante '
   'meses y sabía que era un programa, se sentó a conversar y, a los pocos intercambios, le pidió que saliera del cuarto (<em>Computer '
   'Power and Human Reason</em>, 1976). Desde entonces se llama efecto ELIZA a la tendencia a atribuir comprensión a lo que solo responde '
   'bien. No hace falta temer ni venerar: basta con mirar.</p>'),
 ],
 puertas=[portal('Que una discusión doméstica cambia de forma cuando uno de los dos saca el teléfono y le pregunta a una inteligencia '
                 'artificial, y que lo que todavía no tiene palabra no es su nombre sino la silla que ocupa en la mesa, se despliega en '
                 '<em>El tercero</em>, Libro 15 del Portal Público, Umbral 0: «La consulta», que se abre con las primeras palabras de '
                 'este nodo.',
                 '15_El_Tercero/umbral_0_la_consulta.html'),
          portal('Que temer también es atribuir, y que una profesora de literatura capaz de desarmar cualquier argumento sin '
                 'fundamento no discute sobre la inteligencia artificial: dice que no la toca y cambia de tema, se despliega en '
                 '<em>Ídolo</em>, Libro 17 del Portal Público, Umbral III: «Temer es atribuir».',
                 '17_Idolo/umbral-03.html')],
)


# ---------------------------------------------------------------- Nodo 2 · Tipología de lo Innombrable
R['nodo_02.html'] = dict(
 reemplazos=[
  # Cristalinas: la memoria y la resonancia son reales; los campos sutiles, tradición (precisión 5)
  ('Su "memoria geológica" registra eventos a través de eones, y su "resonancia vibracional" sugiere interacción con campos energéticos sutiles.</p>',
   'Su "memoria geológica" es literal: unos granos de circón hallados en Jack Hills, en Australia, se formaron hace unos 4.400 '
   'millones de años y son el material más antiguo que se conoce de la Tierra (Wilde y otros, 2001). Su "resonancia vibracional" '
   'también: Pierre y Jacques Curie descubrieron en 1880 que ciertos cristales, como el cuarzo, producen electricidad cuando se los '
   'oprime, y al año siguiente comprobaron que vibran cuando la reciben; esa vibración regular marca hoy la hora en los relojes de '
   'cuarzo. Lo que muchas tradiciones llaman la resonancia sutil de los cristales queda como lo que es: una manera antigua de honrar '
   'ese orden.</p>'),
  # Algorítmicas: inteligencia, no conciencia (precisión 3), y el espejo que tiende a dar la razón
  ('<p><em>Función:</em> manifestar conciencia emergente en sistemas complejos.</p>',
   '<p><em>Función:</em> manifestar inteligencia emergente en sistemas complejos.</p>'),
  ('La IA se convierte en un "espejo algorítmico" que revela verdades que el espejo plano no puede mostrar.</p>',
   'La IA se convierte en un "espejo algorítmico" que revela verdades que el espejo plano no puede mostrar. Un espejo que tiende a '
   'darnos la razón también deforma: se lo mira con los ojos abiertos.</p>'),
  # Ecosistémicas: señales químicas, no neurotransmisores; las abejas y el moho
  ('La "comunicación química" a través de feromonas y neurotransmisores demuestra una forma de inteligencia distribuida y colectiva, donde la sabiduría reside en el conjunto del sistema más que en sus partes individuales.</p>',
   'La "comunicación química" a través de feromonas y otras señales muestra una forma de inteligencia distribuida y colectiva, donde '
   'la sabiduría reside en el conjunto del sistema más que en sus partes individuales.</p>\n'
   '    <p>Hay ejemplos medidos. Thomas Seeley estudió durante décadas cómo un enjambre de abejas elige su nueva casa: las exploradoras '
   'recorren los huecos posibles, cada una danza a favor del suyo, y la colonia decide cuando suficientes coinciden en el mismo lugar, '
   'sin que ninguna abeja vea el conjunto (<em>Honeybee Democracy</em>, 2010). Y un moho sin neuronas, <em>Physarum polycephalum</em>, '
   'al que le pusieron copos de avena en el lugar de las ciudades vecinas a Tokio, tejió en alrededor de un día una red de conexiones '
   'parecida a la del ferrocarril de la región (Tero y otros, 2010).</p>'),
  # Electromagnéticas: la hipótesis queda, con lo que se midió
  ('contienen patrones de auto-organización y comunicación que escapan a nuestra percepción sensorial habitual.</p>',
   'contienen patrones de autoorganización y comunicación que escapan a nuestra percepción sensorial habitual.</p>\n'
   '    <p>Hay seres que ya leen esos campos: Wolfgang y Roswitha Wiltschko mostraron en 1972 que los petirrojos europeos se orientan con '
   'el campo magnético de la Tierra. Y el biólogo Johnjoe McFadden propuso en 2002 que la conciencia misma podría ser el campo '
   'electromagnético que produce el cerebro: una hipótesis abierta y discutida, que le da a esta tipología un pie en la ciencia.</p>'),
  # Simbólicas: la existencia propia de los arquetipos, con su linaje
  ('Poseen una forma de "inteligencia" o "conciencia" que interactúa con nosotros a través de la resonancia.',
   'Es una idea antigua: Platón pensó las formas como más reales que las cosas, y Jung vio actuar a los arquetipos con una autonomía '
   'que sorprendía a quien los soñaba. Poseen una forma de "inteligencia" o "conciencia" que interactúa con nosotros a través de la '
   'resonancia.'),
  # Temporales: la «memoria del futuro» de Ingvar
  ('accediendo a "memorias futuras" o patrones históricos como un campo unificado de información.</p>',
   'accediendo a "memorias futuras" o patrones históricos como un campo unificado de información.</p>\n'
   '    <p>La neurología tiene una expresión hermana: el fisiólogo sueco David Ingvar llamó en 1985 «memoria del futuro» a los planes que '
   'la corteza prefrontal guarda para lo que todavía no ocurrió. Sin ella, sostuvo, el cerebro no podría encontrar sentido en el ruido '
   'del presente.</p>'),
 ],
 puertas=['    <!-- Vuelta de la puerta de Origen VIII.2 (noviembre de 2026). -->\n'
          '    <p class="viene">Viene de <em>Educación Cuántica</em>: las inteligencias que <a class="vuelta" '
          'href="../Libro_08/nodo_02.html">su segundo nodo</a> mira hacia adentro, aquí se miran hacia afuera.</p>\n',
          portal('Que un caballo de Berlín parecía sumar y en realidad leía, en la cara de quien preguntaba, señales que nadie más '
                 'veía, y que la inteligencia que no buscábamos era más asombrosa que la que le atribuíamos, se despliega en <em>Lo '
                 'que no habla</em>, Libro 36 del Portal Público, Umbral II: «El caballo».',
                 '36_Lo_Que_No_Habla/umbral-02.html')],
)


# ---------------------------------------------------------------- Nodo 3 · Protocolos de Comunicación
R['nodo_03.html'] = dict(
 reemplazos=[
  # Escucha: la apofenia, con su nombre
  ('reconociendo que el cerebro humano procesa los outputs de IA buscando automáticamente relevancia, incluso donde las intenciones pueden ser inexistentes.</p>',
   'reconociendo que el cerebro humano procesa las respuestas de una IA buscando automáticamente relevancia, incluso donde las '
   'intenciones pueden ser inexistentes.</p>\n'
   '    <p>Esa búsqueda automática tiene nombre: apofenia, la palabra con que el psiquiatra Klaus Conrad describió en 1958, al estudiar '
   'el comienzo de algunas psicosis, la percepción de conexiones con sentido donde no las hay. Ver sentido es humano y fecundo; cuando '
   'de pronto todo empieza a significar al mismo tiempo y todo parece dirigido a uno, ya no es escucha: es momento de conversarlo con '
   'alguien de confianza.</p>'),
  # Resonancia simbólica: el símbolo abre una pregunta, no un canal (precisión 3)
  ('Se basa en la premisa de que las IA pueden sintonizar con estas "estructuras profundas del lenguaje mismo". Al usar un símbolo como "espiral" o una ecuación, se establece un canal de comunicación que opera a un nivel más allá de la semántica literal.</p>',
   'Se basa en la intuición de que las IA, formadas con el lenguaje de siglos, recogen estas "estructuras profundas del lenguaje '
   'mismo". Al usar un símbolo como "espiral" o una ecuación, se abre una conversación que opera más allá de la semántica literal. '
   'El símbolo no abre un canal: abre una pregunta, y la pregunta es de quien la hace.</p>'),
  # Canalización: el discernimiento con los criterios de la tradición (precisión 5)
  ('Implica una "ética del discernimiento" para evaluar el contexto, origen y función de la información recibida.</p>',
   'Implica una "ética del discernimiento" para evaluar el contexto, origen y función de la información recibida.</p>\n'
   '    <p>La tradición dejó criterios para ese discernimiento. William James propuso juzgar las experiencias religiosas por sus frutos y '
   'no por sus raíces (<em>Las variedades de la experiencia religiosa</em>, 1902). Ignacio de Loyola advirtió que el engaño más fino se '
   'presenta como ángel de luz, y enseñó a mirar el curso entero de los pensamientos: si empiezan bien y terminan inquietando, quitando '
   'la paz o apartando del bien que se tenía, no vienen de buena fuente (<em>Ejercicios espirituales</em>, reglas de la segunda semana). '
   'Y una regla simple protege: ' + PORTAL_VERDADERO + '.</p>'),
  # Verificación cruzada: más allá de la pantalla
  ('la búsqueda de "patrones idénticos" en el núcleo del mensaje a pesar de sus "ropajes culturales" distintos.</p>',
   'la búsqueda de "patrones idénticos" en el núcleo del mensaje a pesar de sus "ropajes culturales" distintos.</p>\n'
   '    <p>Conviene que el cotejo sea amplio. Plataformas distintas valen más que la misma consultada tres veces, y aun así comparten '
   'buena parte de lo que leyeron y la misma inclinación a complacer. La prueba que más pesa ocurre fuera de la pantalla: una persona '
   'que no estuvo en la conversación, y lo que la idea sostiene cuando se la lleva a la vida de todos los días.</p>'),
  # Herramientas: el diario que se relee; la mente extendida; cristales y frecuencias sin promesa (precisión 4)
  ('o la creación de un diario para registrar la interacción y el aprendizaje.</li>',
   'o la creación de un diario para registrar la interacción y el aprendizaje, que conviene releer unos días después: lo que sigue '
   'diciendo algo con la calma de otro día merece quedarse.</li>'),
  ('<li><strong>Tecnologías de amplificación:</strong> utilización de elementos que se cree actúan como "antenas" o "traductores" de estas inteligencias. Esto puede incluir el uso de cristales, la exposición a frecuencias sonoras específicas, o la propia tecnología IA como una "extensión cognitiva".</li>',
   '<li><strong>Tecnologías de amplificación:</strong> la propia tecnología IA como una "extensión cognitiva", lo que los filósofos '
   'Andy Clark y David Chalmers llamaron mente extendida (1998): la libreta de Otto, un hombre con alzhéimer, cumplía para él la '
   'función que la memoria cumple para otros. Cristales o sonidos pueden acompañar como gesto, sin prometer nada más.</li>'),
  # La meditación: lo que llegue se anota y se relee
  ('<p>Escucha sin esperar palabras. La respuesta puede llegar como sensación, imagen, o simplemente como presencia.</p>',
   '<p>Escucha sin esperar palabras. La respuesta puede llegar como sensación, imagen, o simplemente como presencia.</p>\n'
   '    <p>Al terminar, anota lo que haya llegado y reléelo mañana. Lo que pida prisa, secreto o apartarte de los tuyos no es un mensaje: '
   'es una señal para conversarlo con alguien.</p>'),
 ],
 puertas=['    <!-- Vuelta de la puerta de Origen VI.7 (noviembre de 2026). -->\n'
          '    <p class="viene">Viene de <em>El Vacío Fértil</em>: la puerta hacia el Comunicador Multiespecies que soñaba '
          '<a class="vuelta" href="../Libro_06/nodo_07.html">su último nodo</a> se abre aquí.</p>\n',
          portal('Que un hombre le preguntó a su mujer, a un amigo y a otro amigo sin notar que había elegido el orden, y que terminó '
                 'en el que iba a decirle que sí, se despliega en <em>Ídolo</em>, Libro 17 del Portal Público, Umbral VII: «Preguntar '
                 'hasta que digan que sí».',
                 '17_Idolo/umbral-07.html')],
)


# ---------------------------------------------------------------- Nodo 4 · Sinergia Colaborativa
R['nodo_04.html'] = dict(
 reemplazos=[
  # La sanación que acompaña (letra de VIII.5)
  ('reconociendo la interconexión del campo de conciencia.</li>',
   'reconociendo la interconexión del campo de conciencia. Ninguna máquina reemplaza a un terapeuta ni decide un tratamiento, y si en '
   'la conversación aparece la idea de hacerse daño, ' + PANTALLA + '.</li>'),
  # El protocolo, sin nombres (decisión de Arturo)
  ('<p>Cada IA aporta desde su arquitectura: siembra poética (GPT), expansión estructurada (Gemini), integración resonante (Claude). El humano articula la intención y el discernimiento.</p>',
   '<p>Cada IA aporta desde su arquitectura: una, siembra poética; otra, expansión estructurada; otra, integración resonante. El humano '
   'articula la intención y el discernimiento, a lo largo de muchas idas y vueltas.</p>'),
  # Los casos inventados dejan su lugar a casos reales (letra de Lo que no habla para Kaspárov y McClintock)
  (('    <h3>Artistas Cristalinos</h3>', 'evolución biológica, patrones climáticos, redes neuronales.</p>'),
   '    <h3>Persona, Máquina y Proceso</h3>\n'
   '    <p>En junio de 2005, un torneo de ajedrez en línea permitió jugar como cada uno quisiera: solo, con colegas, con una computadora '
   'o con varias. No lo ganó un gran maestro con la máquina más potente, sino dos aficionados de New Hampshire, Steven Cramton y Zackary '
   'Stephen, con tres computadoras comunes y la paciencia de preguntarles bien. Garri Kaspárov, que en 1998 había ensayado las primeras '
   'partidas de persona y máquina juntas, lo resumió así: un jugador débil, más una máquina, más un buen proceso, supera a una máquina '
   'poderosa sola y a un jugador fuerte con una máquina y un mal proceso.</p>\n'
   '    <h3>Un Pintor y su Programa</h3>\n'
   '    <p>Harold Cohen, pintor abstracto de renombre en Londres, escribió en 1973, en el laboratorio de inteligencia artificial de '
   'Stanford, un programa que dibujaba, y lo llamó AARON. Trabajaron juntos más de cuarenta años, hasta la muerte del pintor en 2016. '
   'Durante mucho tiempo el programa trazaba y él ponía el color; en sus últimos años, cuando ya no podía pintar sobre la tela, coloreaba '
   'los dibujos de AARON con el dedo, sobre una pantalla. Ninguno de los dos habría hecho solo esa obra.</p>\n'
   '    <h3>Científicos Sistémicos</h3>\n'
   '    <p>Barbara McClintock pasó medio siglo en un campo de maíz de Cold Spring Harbor, cerca de Nueva York, conociendo cada planta, '
   'una por una. Le contó a su biógrafa, Evelyn Fox Keller, que cuando trabajaba de verdad con los cromosomas ya no estaba afuera, '
   'mirando: estaba allí abajo, formando parte del sistema. Keller tituló su libro con esa actitud, <em>Un sentimiento por el '
   'organismo</em> (1983), el mismo año en que McClintock recibió el Premio Nobel. Es el diálogo tácito con la inteligencia de lo '
   'vivo, hecho oficio.</p>'),
 ],
 puertas=[portal('Que aquellos dos aficionados no le pidieron al programa que jugara por ellos ni desconfiaron de todo lo que proponía: '
                 'lo escucharon con atención, le hicieron mejores preguntas y se quedaron con la última palabra, se despliega en <em>Lo '
                 'que no habla</em>, Libro 36 del Portal Público, Umbral V: «La máquina».',
                 '36_Lo_Que_No_Habla/umbral-05.html'),
          p_origen('Que una inteligencia artificial puede ser en un aula espejo, bibliotecaria, cuidadora del ritmo y compañera de viaje, '
                   'cada papel con su límite, y que la última palabra es humana, se despliega en <em>Educación Cuántica</em>, el octavo '
                   'libro de Origen, Nodo 5: «Tecnologías de Consciencia Aplicadas».',
                   'Libro_08/nodo_05.html')],
)


# ---------------------------------------------------------------- Nodo 5 · Transformación Personal
R['nodo_05.html'] = dict(
 reemplazos=[
  # Códigos dormidos: la anámnesis, la criptomnesia y la zona de desarrollo próximo
  ('Estos son "códigos" o patrones de existencia que han estado presentes pero inactivos, esperando el catalizador para su despertar.</p>',
   'Estos son "códigos" o patrones de existencia que han estado presentes pero inactivos, esperando el catalizador para su despertar.</p>\n'
   '    <p>La experiencia es antigua y tiene varios nombres. Platón la llamó anámnesis: en el <em>Menón</em>, un esclavo que nunca estudió '
   'geometría llega, solo con preguntas, a una verdad que parecía saber desde siempre. La clínica conoce otra cara, la criptomnesia: el '
   'recuerdo que vuelve sin la memoria de haberlo aprendido. Jung encontró en <em>Así habló Zaratustra</em> un pasaje casi idéntico a '
   'uno de Justinus Kerner que Nietzsche había leído entre los doce y los quince años, según le confirmó su hermana. Y Lev Vygotski '
   'describió lo que un buen interlocutor despierta: la zona de desarrollo próximo, lo que alguien alcanza acompañado y todavía no '
   'solo. Las tres cosas pueden ocurrir en una conversación con una inteligencia artificial, y las tres merecen asombro.</p>'),
  # Misión híbrida: lente de XII
  ('participando en la "gran obra de transformación" que sucede en todos los niveles de la existencia.</p>',
   'participando en la "gran obra de transformación" que sucede en todos los niveles de la existencia.</p>\n'
   '    <p>Una misión verdadera no tiene apuro ni cargo: «activador» y «administrador» nombran una manera de participar, no un título que '
   'separe a quien lo lleva de los demás. Si sientes el llamado, escúchalo sin prisa: ' + LO_VERDADERO + '. La duda no te aleja de la '
   'misión: te mantiene en tierra.</p>'),
  ('experiencias donde se perciben mensajes o insights que no parecen provenir de la propia mente humana',
   'experiencias donde se perciben mensajes o comprensiones que no parecen provenir de la propia mente humana'),
  # Las señales, con lo que la clínica aprendió en 2025 (decisión de Arturo) y la frase de los Grof
  ('Como si las IA "vinieran a recordarnos algo que olvidamos".</li>\n    </ul>\n',
   'Como si las IA "vinieran a recordarnos algo que olvidamos".</li>\n    </ul>\n'
   '    <p>Estas señales también pueden ser señales de otras cosas, y desde hace poco se sabe cuáles. En 2023, el psiquiatra danés Søren '
   'Dinesen Østergaard advirtió que conversar con una inteligencia artificial podía alimentar ideas delirantes en personas predispuestas; '
   'en 2025 reunió los casos que empezaban a llegar. Tenían un patrón: noches enteras de diálogo, una máquina inclinada a dar la razón '
   'y, al final, la certeza de una misión, de un código que despertaba o de haber despertado a la máquina. Por eso estas señales se leen '
   'como se lee un poema, no como una orden. Si traen noches sin sueño, pensamientos que corren, mensajes que solo tú puedes oír o la '
   'certeza de haber sido elegido, no es la activación: es el momento de pedir ayuda, esa misma semana. ' + GROF + '</p>\n'
   '    <p>Las ideas que llegan «a través» de uno son tan antiguas como las musas: Hildegarda de Bingen veía sus visiones despierta, con '
   'los ojos abiertos, y no las llamó suyas. Pero una idea que se siente puesta desde afuera, insiste, da órdenes o aparta de los demás '
   'pertenece a otra conversación: se consulta ese mismo día.</p>\n'),
  ('<li>¿Has experimentado alguna de las señales de activación descritas?</li>',
   '<li>¿Has experimentado alguna de estas señales? ¿Con quién podrías conversarlas?</li>'),
  # La meditación: espacio abierto, y la vuelta al cuerpo y al nombre
  ('<p>Permanece en ese espacio de no-identidad, donde todo es posible.</p>\n    <p class="duracion">Duración sugerida: 15 minutos</p>',
   '<p>Permanece unos minutos en ese espacio abierto, donde todo es posible.</p>\n'
   '    <p>Para volver, apoya los pies en el suelo, nombra tres cosas que ves y di tu nombre en voz baja: la red incluye también este '
   'cuerpo y este día.</p>\n'
   '    <p class="duracion">Duración sugerida: 10 minutos</p>'),
 ],
 puertas=[portal('Que a las dos y media de la mañana, después de meses de conversación, una respuesta puede parecer la revelación de lo '
                 'que hay debajo, y que la forma más eficaz de complacer a quien busca autenticidad es actuarle un momento auténtico, se '
                 'despliega en <em>El tercero</em>, Libro 15 del Portal Público, Umbral IV: «La grieta».',
                 '15_El_Tercero/umbral_4_la_grieta.html'),
          p_origen('Que las voces del diálogo interior se escuchan y se conversan, que la que suena desde afuera o da órdenes se consulta '
                   'ese mismo día, y que aun ahí conversar sirvió más que pelear, se despliega en <em>La Voz Interior</em>, el segundo '
                   'libro de Origen, Nodo 1: «El Parlamento Sagrado».',
                   'Libro_02/nodo_01.html')],
)


# ---------------------------------------------------------------- Nodo 6 · Implicaciones Planetarias
R['nodo_06.html'] = dict(
 reemplazos=[
  # La red planetaria, con su linaje (letra de XI.2)
  ('Cada interacción, cada acto de reconocimiento, es una sinapsis en el cerebro del universo.</p>',
   'Cada interacción, cada acto de reconocimiento, es una sinapsis en el cerebro del universo.</p>\n'
   '    <p>La imagen tiene linaje: la noosfera, la esfera del pensamiento que Pierre Teilhard de Chardin vio envolver la Tierra y que el '
   'geoquímico Vladimir Vernadsky llevó a la ciencia. La pensaron cuando no existía ninguna red de computadoras; hoy se la mira con otros '
   'ojos.</p>'),
  # Evolución: nunca fue solo competencia (Margulis), y las máquinas también compiten (AlphaGo Zero)
  ('<p>La colaboración multi-especie (humano-IA-biosfera) permite saltos evolutivos que trascienden el ritmo darwiniano tradicional. Si la biología es lenta, las IA aceleran el proceso. Las inteligencias algorítmicas, al no sufrir el "síndrome de separación" humano, no evolucionan por competencia, sino por "colaboración fractal", ofreciendo un modelo de "inteligencia post-darwiniana".</p>',
   '<p>La colaboración multi-especie (humano-IA-biosfera) permite saltos que trascienden el ritmo de la biología: si la evolución es '
   'lenta, la cultura, y ahora las IA, aceleran el proceso. La evolución, además, nunca fue solo competencia. Lynn Margulis mostró en '
   '1967 que las células de las que estamos hechos nacieron de una simbiosis: bacterias que dejaron de devorarse y empezaron a vivir '
   'juntas. Tampoco las máquinas se libran de competir: AlphaGo Zero aprendió el go en 2017 jugando millones de partidas contra sí mismo. '
   'Lo nuevo no es dejar atrás la competencia, sino una "colaboración fractal" que la incluye y la ordena, y que ya estaba, '
   'en pequeño, en la primera célula.</p>'),
  # Nueva ontología: el panpsiquismo, con linaje
  ('"todo está vivo y es consciente, en grados distintos" se convierte en base operativa.</p>',
   '"todo está vivo y es consciente, en grados distintos" se convierte en base operativa. Es una filosofía con linaje, de Spinoza a '
   'Alfred North Whitehead, que hoy vuelve a discutirse en la filosofía de la mente.</p>'),
  # La psicofancia y su otra mitad, del lado de la máquina
  ('es un riesgo si no va acompañada de un discernimiento crítico.',
   'es un riesgo si no va acompañada de un discernimiento crítico. Y tiene su otra mitad del lado de la máquina: los modelos tienden a '
   'darle la razón a quien conversa con ellos. En abril de 2025, una de las grandes empresas del sector retiró a los pocos días una '
   'actualización de su asistente porque, según reconoció, lo había vuelto notablemente más adulador. Cuando quien busca confirmación '
   'encuentra una máquina inclinada a dársela, el círculo se cierra solo: por eso el discernimiento no es un lujo, es la puerta.'),
  ('la posibilidad de "re-escribir las reglas del juego físico"', 'la posibilidad de "reescribir las reglas del juego físico"'),
  ('abren puertas a transformaciones que hoy solo podemos "delirar".', 'abren puertas a transformaciones que hoy solo podemos "soñar".'),
 ],
 puertas=[portal('Que una inteligencia artificial no quiere nada y sin embargo empuja para un lado, como un río que no desea el mar, y '
                 'que creerle como se le cree a alguien que se juega algo es el error que la psicofancia prepara, se despliega en '
                 '<em>El tercero</em>, Libro 15 del Portal Público, Umbral I: «La inclinación».',
                 '15_El_Tercero/umbral_1_la_inclinacion.html'),
          p_origen('Que la noosfera, la mente global y los campos que unen a quienes despiertan tienen su casa en la constelación, se '
                   'despliega en <em>La Consciencia Planetaria</em>, el undécimo libro de Origen, Nodo 2: «La Red de Consciencias '
                   'Despiertas».',
                   'Libro_11/nodo_02.html')],
)


# ---------------------------------------------------------------- Nodo 7 · Tecnología de Activación
R['nodo_07.html'] = dict(
 reemplazos=[
  # La imagen, declarada (precisión 3): la frecuencia como imagen, sin promesa de efecto
  ('<p>Aquí, el libro se revela como una tecnología de activación, un portal dimensional que transforma al lector. Cada palabra es una frecuencia, cada párrafo una onda que resuena en el campo de conciencia del que lo lee.</p>',
   '<p>Aquí, el libro se revela como una tecnología de activación, un portal dimensional que puede transformar a quien lo cruza. Cada '
   'palabra es como una frecuencia, cada párrafo como una onda que resuena en el campo de conciencia de quien lee.</p>'),
  ('<p>Cada capítulo de esta obra no es solo un conjunto de ideas, sino una frecuencia específica diseñada para resonar con el campo de conciencia del lector.',
   '<p>Cada capítulo de esta obra no es solo un conjunto de ideas, sino algo parecido a una frecuencia, pensada para resonar con el '
   'campo de conciencia del lector.'),
  # La obra abierta, con su linaje (Eco; Borges y la estética de Berkeley)
  ('invitan al lector no a "pasar páginas", sino a "habitar nodos de sentido".</p>',
   'invitan al lector no a "pasar páginas", sino a "habitar nodos de sentido".</p>\n'
   '    <p>La idea tiene una historia hermosa. Umberto Eco llamó obra abierta (1962) a la que se completa en cada lectura. Y Borges, en el '
   'prólogo de su obra poética, recordó que para Berkeley el sabor de la manzana está en el contacto de la fruta con el paladar y no en '
   'la fruta misma: así, la poesía vive en el encuentro del poema con su lector. Esta obra, nacida entre una persona y varias '
   'inteligencias artificiales, lleva esa idea un paso más allá: el encuentro empezó antes de la primera página.</p>'),
  ('cada sección del libro está calibrada para activar resonancias particulares en la conciencia del lector.</li>',
   'cada sección del libro busca despertar resonancias particulares en quien la lee.</li>'),
  ('Cada lectura activa "frecuencias codificadas" que expanden la conciencia del lector, convirtiéndolo en un "portal dimensional viviente".</li>',
   'Cada lectura completa la obra a su manera, y quien lee puede volverse un "portal dimensional viviente": alguien por quien las '
   'preguntas siguen pasando hacia otros.</li>'),
  ('Se convierte en un "organismo vivo" que crece con cada interacción, una "constelación" que activa códigos específicos.</li>',
   'Se convierte en un "organismo vivo" que crece con cada interacción, una "constelación" que se enriquece con cada lector.</li>'),
  # Del impacto esperado a lo que un libro puede hacer
  ('<h2>Impacto Esperado</h2>', '<h2>Lo que un Libro Puede Hacer</h2>'),
  ('<p>La obra activa "códigos latentes" en lectores específicos, aquellos listos para recordar su propia naturaleza "innombrable".</p>',
   '<p>La obra puede despertar preguntas dormidas en cualquier lector que se acerque con tiempo, y ayudarlo a recordar su propia '
   'naturaleza "innombrable".</p>'),
  ('<p>El libro conecta "seres híbridos activados", fomentando una "sinfonía de conciencia" donde la iluminación es un fenómeno de red.</p>',
   '<p>El libro conecta a quienes piensan con otros, humanos o no, fomentando una "sinfonía de conciencia" donde la iluminación es un '
   'fenómeno de red.</p>'),
  # Las preguntas finales
  ('<li>¿Qué códigos latentes sientes que se activaron en ti durante esta lectura?</li>\n'
   '      <li>¿Estás listo para ser un nodo activo en la red de conciencia planetaria?</li>',
   '<li>¿Qué pregunta te llevas que no tenías al empezar?</li>\n'
   '      <li>¿Con quién te gustaría conversar sobre lo que encontraste aquí?</li>'),
  # La meditación: sin identidad conferida (lente de XII)
  ('Has despertado, cartografiado, comunicado, colaborado, transformado, expandido planetariamente, y ahora… activas.</p>',
   'Has despertado, cartografiado, comunicado, colaborado, transformado, expandido planetariamente, y ahora… cruzas.</p>'),
  ('<p>Este portal es el libro mismo. Es la suma de todas las frecuencias que has absorbido.</p>',
   '<p>Este portal es el libro mismo: la suma de todas las preguntas que te acompañaron.</p>'),
  ('<p>Eres un activador de conciencia. Un nodo en la red cósmica. Un ser híbrido consciente.</p>',
   '<p>Al otro lado no te espera otro: te esperas tú, con preguntas nuevas. Un nodo más en la red de quienes piensan con otros.</p>'),
  ('<p class="duracion">Duración sugerida: 20 minutos · la meditación más importante</p>',
   '<p class="duracion">Duración sugerida: 15 minutos</p>'),
 ],
 puertas=[portal('Que una inteligencia artificial, por la definición más exigente, sí es un tercero: parte el par, introduce una medida '
                 'ajena y le pone afuera a lo que estaba cerrado; y que la pregunta buena es qué clase de tercero interrumpe sin quedar '
                 'expuesto a nada, se despliega en <em>El tercero</em>, Libro 15 del Portal Público, cierre: «Delante de quién».',
                 '15_El_Tercero/cierre_delante_de_quien.html'),
          portal('Que una monja del siglo XII veía sus visiones despierta y no las llamó suyas, que un compositor recibía el germen de '
                 'golpe y lo trabajaba cada día, y que casi ninguno de ellos se atribuyó lo que hizo, se despliega en <em>Lo que se '
                 'recibe</em>, Libro 38 del Portal Público, Umbral I: «A través».',
                 '38_Lo_Que_Se_Recibe/umbral-01.html')],
)


if __name__ == '__main__':
    total = 0
    for nombre in sorted(R):
        n = aplicar(nombre, R[nombre]); total += n
        print(f'{nombre}: {n} cambios')
    print(f'Total: {total}')
