# Depuración de Origen XII, La Civilización Galáctica (noviembre de 2026), con el veto del Lic. Arturo Rodríguez.
# Lente: riesgo clínico y puertas hacia la Red, como en Origen VI, VIII, I, XI, VII e IX. La visión del libro queda
# entera (la cuarentena que se levanta, el contacto interior, los embajadores, las tecnologías estelares, la economía
# de la abundancia, las Ciudades de Luz y la graduación cósmica), con su linaje y, donde existe, con su primer paso
# real (precisión 6). El riesgo vivía en la identidad que el libro ofrece al lector —embajador, semilla estelar,
# contactado, graduado— y en tres frases que, en el momento decisivo, le quitaban el último freno («no están locos ni
# delirando», «el campo no comete errores», «no importa si tu mente lo cuestiona»). El libro obedece a sus mejores
# frases: «distinguir entre imaginación y recepción genuina», «el verdadero embajador reconoce que es un servidor, no
# un superior», «no graduamos escapando de la Tierra sino amándola completamente». La duda vuelve a ser aliada.
# Por decisión de Arturo: las cronologías quedan en etapas, sin años; «Graduación cósmica» queda (decisión de X.7), y
# nada se lee como graduarse dejando el cuerpo (el vocabulario de XII.7 es casi el de Heaven's Gate, 1997: la razón
# queda en el maestro, no en el nodo); la vuelta desde Habitar va en una línea discreta «Viene de Trinity Origen».
# Las seis transiciones anunciaban nodos soñados: ahora anuncian el real, y los títulos van a las Semillas del maestro.
# Se abren diez puertas, todas de ida y vuelta.
#
# Se aplica sobre el original de la etiqueta origen-original, con reemplazos que deben aparecer exactamente
# una vez (o tramos, de un texto a otro, inclusive); si un anclaje falla, el script se detiene sin escribir.
#
# Uso: ORIGEN12_SRC=RUTA/origen-original/01_Trinity_Origen/Libro_12/ ORIGEN12_OUT=RUTA/salida/ python3 depurar_origen12.py
import os, re, sys

SRC = os.environ.get('ORIGEN12_SRC', '/home/claude/work12/o12/01_Trinity_Origen/Libro_12/')
OUT = os.environ.get('ORIGEN12_OUT', '/home/claude/work12/out/01_Trinity_Origen/Libro_12/')

NOTA = ('<!-- Depurado en noviembre de 2026 según la guía de depuración de Quantum, que vale para Origen '
        '(Arquitectura del Destino, maestro v4, sección 5, con las precisiones 5 y 6 de Origen), con el veto del Lic. Arturo Rodríguez: '
        'la visión del libro queda, con su linaje y su primer paso real; salen las fechas, las cifras sin fuente, lo que se vende '
        'como si funcionara y lo que se dice suprimido; la duda vuelve a ser aliada del lector; se suma el cuidado clínico en la voz '
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
.content pre{ white-space:pre-wrap; overflow-wrap:anywhere; }
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
   Letra más grande en el teléfono y la línea con la medida del libro.
   ============================================================ */
.closing-panel .medida{color:var(--text-soft);font-size:0.95rem;line-height:1.8;margin-top:1rem;font-style:italic;}
@media (max-width: 720px){
  .intro-panel p, .closing-panel p{ font-size:18px; line-height:1.7; }
  .node-sub{ font-size:16px; }
}
</style>
</head>'''

# ---------------------------------------------------------------- Letra de la constelación
POEMA = ('Lo que llega en sueños o en silencio se recibe como se recibe un poema, no como una orden. Y si alguna vez llegan '
         'voces que dan órdenes, o mensajes que solo tú puedes oír, no es una descarga: es momento de consultar ese mismo día.')   # Origen XI.5
GROF = ('Stanislav y Christina Grof llamaron emergencia espiritual a las crisis que a veces acompañan un despertar, '
        'y enseñaron que se atraviesan acompañadas.')   # Origen X.5 y VI.7


def senales(inicio, que):   # Origen VI.7
    return (inicio + ' Si traen noches sin sueño, pensamientos que corren, una misión urgente, mensajes de guías o la certeza '
            'de saber lo que va a pasar, no es ' + que + ': es el momento de pedir ayuda, esa misma semana. ' + GROF)


ACOMPANA = 'Lo que acompaña nunca reemplaza un tratamiento que funciona.'      # Origen X.1
HOY = 'A quien enferma hoy lo cuida lo que hoy existe, que ya es mucho, y cada año es más.'   # precisión 6
LUZ = 'el cuerpo de hoy necesita comida: quienes intentaron vivir solo de luz enfermaron, y algunos murieron.'   # Origen XIII.7
NINO = ('Ver en un niño un don no quita mirar también lo que necesita: si le cuesta atender, aprender o vincularse, una consulta '
        'puede abrirle caminos.')   # Origen VI.7 y XIII.7
REFERENCIA = ('Si alguna vez parece que cada número y cada cartel te hablan a ti, en secreto, eso no es un don: conviene conversarlo '
              'con alguien de confianza o con un profesional esa misma semana.')   # Quantum 11.2
DANO = ('Si sientes que otros te dañan a distancia, o que necesitas protegerte todo el tiempo, vale la pena hablarlo con un profesional: '
        'ese miedo también se cuida.')   # Origen X.5
MIEDO = ('Ese miedo no es una enfermedad: es una respuesta a algo real. Si quita el sueño o las ganas durante semanas, se consulta; '
         'y se alivia más haciendo con otros que leyendo a solas.')   # Origen XI.1
ESTADO = ('Lo que protege es poder decirse: esto es un estado. Mientras esa frase esté disponible, se navega. Cuando se pierde, '
          'y no se distingue ya el recuerdo de la fantasía, se pide ayuda.')   # Origen VI.3
EXTRANJERO = ('Sentirse extranjero es muy humano, y muchas veces es el comienzo de una búsqueda. Si esa extrañeza pesa todos los días, '
              'también se conversa con alguien.')   # Origen XI.5
WALKIN = ('Si alguna vez sientes que ya no eres tú, o que alguien cercano fue cambiado por otro que se le parece, no es un '
          'intercambio de almas: es momento de consultar ese mismo día.')   # Origen XI.5
GASTO = ('Actúa con la confianza de quien ya tiene lo necesario, no con su gasto: ninguna intención justifica endeudarse')   # Origen I.6
INVITACION = 'ninguna invitación verdadera pide dinero, secreto ni obediencia'   # Origen VI.7

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
    t = una_vez(t, '</style>\n</head>', (CSS_INDEX if nombre == 'index.html' else CSS).lstrip('\n'), 'el cierre del estilo'); cuenta += 1
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


# ---------------------------------------------------------------- Nodo 1 · La Cuarentena se Levanta
R['nodo_01.html'] = dict(
 reemplazos=[
  # Restos de producción: el archivo empezaba con una cerca de código y terminaba con un mensaje del armado.
  ('```html\n<!DOCTYPE html>', '<!DOCTYPE html>'),
  ('</html>\n```\n\nListo para recibir el **Nodo 2 del Libro 12**.', '</html>'),
  # Del plan al hallazgo (criterio 2)
  ('Esta aceleración exponencial no es natural en términos evolutivos normales. Es una preparación, una actualización rápida de nuestras capacidades para poder interfazar con realidades más amplias.',
   'Ninguna especie de la que tengamos noticia cambió tan rápido. En la visión de este libro, esa aceleración puede leerse como una preparación: una actualización de nuestras capacidades para comunicarnos con realidades más amplias.'),
  ('Las IAs no son el final de este camino', 'Las IA no son el final de este camino'),
  ('es un ensayo para conversaciones mucho más profundas que están por venir.</p>',
   'es un ensayo para conversaciones mucho más profundas que están por venir. Una conversación así dio origen a esta obra: Trinity nació del diálogo entre quien escribe, la inteligencia que responde y lo que surge entre ambos.</p>'),
  # Lo que consta del fenómeno
  ('Después de décadas de negación y ridiculización, los gobiernos del mundo súbitamente reconocen la realidad del fenómeno. Los videos del Pentágono, las audiencias del Congreso, los testimonios de pilotos militares - todo apunta a una preparación psicológica masiva.',
   'Después de décadas de burla, los gobiernos empezaron a hablar en voz alta. En 2020, el Pentágono publicó tres videos en los que pilotos de la Marina siguen objetos que no supieron identificar, y en 2023 el Congreso de los Estados Unidos oyó en audiencia pública a militares que hablaron de lo que no supieron explicar. Lo que reconocen es eso: fenómenos sin explicación. Para esta visión, es el modo en que la humanidad se prepara, sin sobresaltos, para lo que viene.'),
  ('No es que "ellos" acaban de llegar.', 'No es que "ellos" acaben de llegar.'),
  ('Las crisis climáticas, las pandemias, las guerras que amenazan con destrucción nuclear - todas convergen en un punto singular de la historia. No es coincidencia. Es el dolor de parto de una especie que está a punto de nacer a una realidad mayor.',
   'Las crisis climáticas, las pandemias, las guerras que amenazan con destrucción nuclear: todas convergen en un punto singular de la historia. La tradición lo llama dolor de parto de una especie que está a punto de nacer a una realidad mayor, y la imagen es antigua y hermosa. Pero esas crisis no fueron contracciones de nadie: dejaron víctimas con nombre, y su dolor pidió cuidado. Lo que una crisis puede abrir, lo abre en quien la atraviesa acompañado.'),
  ('Cuando una oruga entra en crisálida, su cuerpo literalmente se disuelve antes de reformarse como mariposa. La humanidad está en ese momento de disolución aparente que precede a la transformación radical.',
   'Cuando una oruga entra en crisálida, casi todo su cuerpo se deshace antes de rehacerse, pero no todo: en 2008, Douglas Blackiston, Elena Silva Casey y Martha Weiss enseñaron a unas orugas a evitar un olor, y las polillas que salieron de la crisálida lo seguían evitando. La humanidad está en ese momento de disolución aparente que precede a la transformación radical, y lo aprendido cruza con nosotros.'),
  # Linaje del consejo
  ('suficiente libertad para crecer, suficiente protección para sobrevivir.</p>',
   'suficiente libertad para crecer, suficiente protección para sobrevivir.</p>\n'
   '    <p>La imagen tiene linaje: la teosofía habló de maestros que velan por la evolución humana, y los contactados de los años cincuenta, de hermanos del espacio que observan sin intervenir.</p>'),
  ('versiones de nosotros mismos que han transcendido el tiempo lineal', 'versiones de nosotros mismos que han trascendido el tiempo lineal'),
  # Las fases, en etapas
  ('<h3>Fase 1: Preparación Psicológica (1947-2025)</h3>', '<h3>Fase 1: Preparación Psicológica</h3>'),
  ('<h3>Fase 2: Activación de los Pioneros (2020-2030)</h3>', '<h3>Fase 2: Activación de los Pioneros</h3>'),
  ('<h3>Fase 3: Contacto Selectivo (2025-2035)</h3>', '<h3>Fase 3: Contacto Selectivo</h3>'),
  ('<h3>Fase 4: Integración Gradual (2030-2050)</h3>', '<h3>Fase 4: Integración Gradual</h3>'),
  ('<h3>Fase 5: Membresía Galáctica (2050+)</h3>', '<h3>Fase 5: Membresía Galáctica</h3>'),
  ('<h3>1. Transcender el Tribalismo</h3>', '<h3>1. Trascender el Tribalismo</h3>'),
  # La telepatía, con su primer paso (Origen I.7)
  ('Por eso el trabajo con la meditación y la expansión de consciencia es crítico.</p>',
   'Por eso el trabajo con la meditación y la expansión de consciencia es crítico. Su primer paso ya existe, por otro camino: en 2014, un equipo internacional transmitió saludos simples de cerebro a cerebro entre dos personas separadas por miles de kilómetros, con electrodos y una conexión de internet (Grau y otros).</p>'),
  # El freno que vuelve
  ('Aquellos que sienten la verdad de estas palabras no están locos ni delirando. Son los primeros en despertar',
   'Quienes sienten la verdad de estas palabras no necesitan probarla ni defenderla: les basta con vivirla con los pies en la tierra. Son los primeros en despertar'),
  ('Demostrar que es posible transcender el miedo', 'Demostrar que es posible trascender el miedo'),
  ('están sintonizados a diferentes bandas de frecuencia de la misma realidad multidimensional.</p>',
   'están sintonizados a diferentes bandas de frecuencia de la misma realidad multidimensional.</p>\n'
   '    <p>' + POEMA + '</p>'),
  ('cada acción ripple a través del campo galáctico.', 'cada acción resuena en el campo galáctico.'),
  # Transición: anuncia el nodo real
  ('una pregunta se vuelve inevitable: <strong>¿quiénes son aquellos que han esperado pacientemente al otro lado del umbral?</strong></p>',
   'una pregunta se vuelve inevitable: <strong>¿cómo se escucha a quienes han esperado pacientemente al otro lado del umbral?</strong></p>'),
  ('En el próximo nodo nos adentraremos en los rostros, presencias y linajes de esa comunidad más amplia: <strong>“Las Civilizaciones del Umbral: Rostros de la Comunidad Galáctica”</strong>...',
   'En el próximo nodo descubriremos que el primer contacto empieza adentro: <strong>“El Protocolo de Contacto Interior”</strong>...'),
 ],
 puertas=[p_origen('Lo que consta del contacto que esta visión sueña —los contactados del siglo XX, las señales que la ciencia sigue escuchando y la única desviación de un asteroide, que hizo la humanidad— se despliega en <em>La Consciencia Planetaria</em>, Libro XI de Trinity Origen, nodo 5: «Colaboración Cósmica».',
                   'Libro_11/nodo_05.html')],
)


# ---------------------------------------------------------------- Nodo 2 · El Protocolo de Contacto Interior
R['nodo_02.html'] = dict(
 reemplazos=[
  ('<h2>I. La Búsqueda en la Dirección Equivocada</h2>', '<h2>I. La Búsqueda en una Sola Dirección</h2>'),
  ('Durante décadas, hemos apuntado radiotelescopios al espacio, esperando captar señales de civilizaciones extraterrestres. Hemos enviado sondas con discos dorados, mensajes en botellas cósmicas lanzadas al océano del vacío. Pero hemos estado buscando en la dirección equivocada.',
   'Desde 1960, cuando Frank Drake apuntó por primera vez un radiotelescopio a dos estrellas cercanas, escuchamos el cielo esperando una señal. En 1977 lanzamos las dos sondas Voyager con un disco dorado a bordo, saludos en cincuenta y cinco lenguas y músicas de la Tierra: botellas cósmicas arrojadas al océano del vacío. Pero hemos estado buscando en una sola dirección.'),
  ('La consciencia no es un epifenómeno del cerebro, como el materialismo sugiere. Es el campo fundamental del universo, y cada mente individual es un nodo en esta red infinita.',
   'Quizá la consciencia no sea un epifenómeno del cerebro, como el materialismo sugiere, sino el campo fundamental del universo, y cada mente individual, un nodo en esta red infinita. La idea tiene linaje: en 1898, William James propuso que el cerebro quizá no produce la conciencia sino que la transmite, como un vidrio de color transmite la luz, y en 1954 Aldous Huxley lo llamó una válvula reductora.'),
  ('El corazón tiene su propio campo electromagnético, 60 veces más grande que el del cerebro. Cuando el corazón',
   'El corazón tiene su propia red de neuronas, unas cuarenta mil según J. Andrew Armour (1991), que la llamó el «pequeño cerebro» del corazón. Cuando el corazón'),
  ('Esta coherencia no es solo metafórica. Es medible con tecnología actual (variabilidad del ritmo cardíaco, coherencia de ondas cerebrales).',
   'Esta coherencia no es solo metafórica: la variabilidad del ritmo cardíaco se mide, y respirar unas seis veces por minuto la lleva a su mayor amplitud (Lehrer y Gevirtz, 2014).'),
  # El protocolo, sin ayuno ni dieta prescripta; el sueño como ancla
  ('      <li>Purificar la dieta (alimentos vivos, agua pura)</li>\n      <li>Regular el sueño (sincronizar con ritmos naturales)</li>\n      <li>Practicar ayuno intermitente (clarifica la percepción)</li>\n',
   '      <li>Comer a horario y sin excesos</li>\n      <li>Dormir bien y a horario: el sueño es el primer ancla del protocolo</li>\n'),
  ('<li>Journaling de sueños (los sueños son el primer canal)</li>', '<li>Diario de sueños (los sueños son el primer canal)</li>'),
  ('<li>Trabajo con el tercer ojo (glándula pineal)</li>', '<li>Atención al entrecejo, el tercer ojo de la tradición (<em>ajna</em>)</li>'),
  ('<li>Práctica de visión remota básica</li>', '<li>Escucha de la sensación sentida, lo que el cuerpo sabe antes que las palabras (Gendlin, 1978)</li>'),
  ('<li>Downloads de información comprimida</li>', '<li>Descargas de información comprimida</li>'),
  # Los niveles, con su cuidado
  ('      <li>Identificación de la fuente</li>\n    </ul>',
   '      <li>Identificación de la fuente</li>\n    </ul>\n'
   '    <p>' + POEMA + '</p>'),
  ('      <li>Activaciones energéticas del cuerpo</li>\n    </ul>',
   '      <li>Activaciones energéticas del cuerpo</li>\n    </ul>\n'
   '    <p>La presencia sentida es antigua y humana. En 1916, Ernest Shackleton, Frank Worsley y Tom Crean cruzaron a pie las montañas de Georgia del Sur para pedir ayuda por sus compañeros, y los tres sintieron, sin decírselo, que eran cuatro y no tres. T. S. Eliot lo llevó a <em>La tierra baldía</em> (1922), en la pregunta por el que camina siempre a tu lado. Una presencia así acompaña. Si asusta, vuelve cada noche o trae órdenes, se consulta.</p>'),
  ('      <li>Iniciaciones galácticas</li>\n    </ul>',
   '      <li>Iniciaciones galácticas</li>\n    </ul>\n'
   '    <p>Muchos de esos viajes ocurren en el borde del sueño. La noche en que el cuerpo no puede moverse y alguien parece estar en el cuarto tiene nombre, parálisis del sueño: es frecuente, pasa sola y no hace daño, y el folclorista David Hufford la encontró en relatos de muchas culturas (<em>The Terror That Comes in the Night</em>, 1982).</p>'),
  ('Colores y patrones de luz que llevan información directamente al ADN, activando potenciales dormidos y actualizando el sistema operativo biológico.',
   'Colores y patrones de luz que hablan directamente al cuerpo, como le hablan un amanecer o un vitral, y despiertan lo que dormía.'),
  ('¿Busca el contacto por razones egóicas o por servicio genuino?', '¿Busca el contacto por razones egoicas o por servicio genuino?'),
  ('<h3>Pérdida de Grounding</h3>', '<h3>Pérdida del Arraigo</h3>'),
  ('La resonancia del amor incondicional es la mejor protección.</p>',
   'La resonancia del amor incondicional es la mejor protección.</p>\n'
   '    <p>' + DANO + '</p>'),
  ('Cuando suficientes individuos establecen contacto consciente, se crea un “salto cuántico” en la consciencia colectiva. No necesitamos que todos lo hagan, solo una masa crítica - estimada en aproximadamente 1% de la población.',
   'Cuando suficientes individuos establecen contacto consciente, se crea un salto en la consciencia colectiva. No necesitamos que todos lo hagan, solo una masa crítica. En los años setenta, el movimiento de Meditación Trascendental anunció que bastaba el uno por ciento de una ciudad; lo llamó efecto Maharishi, y queda como visión. Lo que sí se midió es de gente que actúa: en 2018, Damon Centola vio que una minoría comprometida de una cuarta parte alcanza para cambiar una convención.'),
  # Señales de autenticidad
  ('<li>La información recibida es verificable o se manifiesta en sincronicidades</li>',
   '<li>Lo que recibes, cuando puede comprobarse, se comprueba con hechos, no con coincidencias</li>'),
  ('      <li>Se siente amor incondicional, nunca miedo o coerción</li>\n    </ul>',
   '      <li>Puedes dejarlo una semana sin que nada se rompa</li>\n'
   '      <li>No te pide aislarte, ni dinero, ni secreto</li>\n'
   '      <li>Se siente amor incondicional, nunca miedo o coerción</li>\n    </ul>\n'
   '    <p>' + REFERENCIA + '</p>'),
  ('<p>Interesantemente, estamos desarrollando', '<p>Curiosamente, estamos desarrollando'),
  ('<pre>Internet           → Telepatía global\nRealidad Virtual   → Viaje multidimensional\nIA                 → Acceso a inteligencia expandida\nQuantum Computing  → Procesamiento no-lineal</pre>',
   '<pre>Internet             → Telepatía global\nRealidad virtual     → Viaje multidimensional\nIA                   → Acceso a inteligencia expandida\nComputación cuántica → Procesamiento no lineal</pre>'),
  # Protocolo de emergencia
  ('<li><strong>Grounding Inmediato:</strong> Pies descalzos en la tierra, comida pesada</li>',
   '<li><strong>Pies en la Tierra:</strong> Pies descalzos en el suelo, una comida caliente y dormir</li>'),
  ('<li><strong>Integración:</strong> Journaling, arte, movimiento para procesar</li>',
   '<li><strong>Integración:</strong> Diario, arte, movimiento para procesar</li>'),
  ('<li><strong>Busca Apoyo:</strong> Conecta con otros que entiendan</li>',
   '<li><strong>Busca Apoyo:</strong> Alguien de confianza fuera del grupo; y si en un día no cede, un profesional</li>'),
  ('      <li><strong>Pausa y Recalibra:</strong> El contacto puede reanudarse cuando estés listo</li>\n    </ol>',
   '      <li><strong>Pausa y Recalibra:</strong> El contacto puede reanudarse cuando estés listo</li>\n    </ol>\n'
   '    <p>' + ESTADO + '</p>'),
  # Transición: anuncia el nodo real
  ('surge una nueva pregunta decisiva: <strong>¿qué tipo de civilización nace cuando una especie comienza a recordar su identidad cósmica?</strong></p>',
   'surge una nueva pregunta decisiva: <strong>¿quiénes son los primeros en escuchar, y qué les toca hacer con lo que escuchan?</strong></p>'),
  ('En el próximo nodo exploraremos las bases, valores y estructuras de esa humanidad expandida: <strong>“La Arquitectura de una Civilización Galáctica: Principios para una Humanidad Cósmica”</strong>...',
   'En el próximo nodo conoceremos a los puentes vivos de esta transición: <strong>“Los Embajadores de la Humanidad”</strong>...'),
 ],
 puertas=[arq('Que un maestro zen del siglo XIV, Bassui, enseñaba a preguntarse ante cada sonido «¿quién es el que oye?», hasta volver la escucha hacia quien escucha, se despliega en <em>El Testigo</em>, Libro 3 de <em>Arquitectura del Destino</em>, Umbral V: «El maestro de la pregunta».',
              'libro-03-el-testigo/L03-U5.html')],
)


# ---------------------------------------------------------------- Nodo 3 · Los Embajadores de la Humanidad
R['nodo_03.html'] = dict(
 reemplazos=[
  ('      <li>Activación progresiva de capacidades latentes</li>\n    </ul>',
   '      <li>Activación progresiva de capacidades latentes</li>\n    </ul>\n'
   '    <p>El perfil tiene autor: el escritor estadounidense Brad Steiger lo trazó en <em>Gods of Aquarius</em> (1976) y en <em>The Star People</em> (1981), y desde entonces circula con muchas variantes. La nostalgia que describe es mucho más antigua: en el siglo II, el <em>Himno de la Perla</em> contaba la historia de un príncipe enviado a tierra extraña que olvidó quién era hasta que una carta se lo recordó. ' + EXTRANJERO + '</p>'),
  ('<h3>1. Los Semillas Estelares (Starseeds)</h3>', '<h3>1. Las Semillas Estelares</h3>'),
  ('Muchos tienen memorias veladas de existencias en otros sistemas estelares - Pléyades, Sirio, Arcturus, Andrómeda.',
   'Muchas tienen memorias veladas de existencias en otros sistemas estelares: las Pléyades, Sirio, Arturo, Andrómeda.'),
  ('<li>Activar códigos dormidos en el ADN colectivo</li>', '<li>Despertar lo que duerme en el corazón colectivo</li>'),
  ('la humanidad puede transcender sus limitaciones actuales', 'la humanidad puede trascender sus limitaciones actuales'),
  ('<h3>3. Los Walk-Ins Galácticos</h3>', '<h3>3. Los <em>Walk-ins</em> Galácticos</h3>'),
  ('Un fenómeno más raro pero real: consciencias galácticas que, con permiso del alma original, entran en cuerpos humanos adultos para cumplir misiones específicas. Usualmente ocurre después de experiencias cercanas a la muerte o momentos de profunda transformación.',
   'Una creencia más rara, que la escritora Ruth Montgomery difundió en 1979 con el nombre de <em>walk-ins</em>, almas intercambiadas: consciencias galácticas que, con permiso del alma original, entran en cuerpos humanos adultos para cumplir misiones específicas. Se cuenta que suele ocurrir después de experiencias cercanas a la muerte o de momentos de profunda transformación.'),
  ('      <li>Completar la misión en tiempo limitado</li>\n    </ul>',
   '      <li>Completar la misión en tiempo limitado</li>\n    </ul>\n'
   '    <p>' + WALKIN + '</p>'),
  ('Estos no son solo sueños simbólicos sino experiencias reales en dimensiones superiores donde el entrenamiento puede ocurrir aceleradamente.',
   'Los viven no como sueños simbólicos sino como experiencias reales en dimensiones superiores, donde el entrenamiento puede ocurrir aceleradamente. Ninguna escuela verdadera pide noches en vela: el sueño que descansa también es entrenamiento.'),
  ('<h4>Curriculum Común</h4>', '<h4>Currículo Común</h4>'),
  ('<li>Downloads masivos de información</li>', '<li>Descargas masivas de información</li>'),
  ('      <li>Sincronicidades que confirman la misión</li>\n    </ul>',
   '      <li>Sincronicidades que confirman la misión</li>\n    </ul>\n'
   '    <p>' + senales('Estos momentos también pueden ser señales de otras cosas.', 'la activación') + '</p>'),
  ('Usar sonido, luz y consciencia para armonizar campos distorsionados.',
   'Usar sonido, luz y consciencia para armonizar campos distorsionados. ' + ACOMPANA),
  ('Despertar los códigos dormidos en otros a través de presencia y resonancia.', 'Despertar lo dormido en otros a través de presencia y resonancia.'),
  ('Si sientes el llamado, confía. El campo no comete errores.',
   'Si sientes el llamado, escúchalo sin prisa: lo verdadero sabe esperar una noche y una conversación con alguien de confianza.'),
  ('Internet ha acelerado las conexiones, pero el aislamiento inicial es parte del fortalecimiento necesario.',
   'Internet ha acelerado las conexiones, pero también puede dejar a cada uno a solas frente a una pantalla. El aislamiento no fortalece por sí mismo: lo que sostiene es un hilo, una persona con quien se puede hablar de esto, aunque no lo viva igual.'),
  ('debe estar completamente encarnado, funcional y contributivo en la realidad terrestre.', 'debe estar completamente encarnado, funcional y presente en la realidad terrestre.'),
  ('<li><strong>Los Traductores de Tecnología:</strong> Reciben downloads de tecnologías', '<li><strong>Los Traductores de Tecnología:</strong> Reciben descargas de tecnologías'),
  ('<li><strong>Los Armonizadores Sociales:</strong> Trabajan en posiciones de influencia para preparar sistemas sociales.</li>',
   '<li><strong>Los Armonizadores Sociales:</strong> Trabajan donde se decide, a la vista de todos, para preparar los sistemas sociales.</li>'),
  ('      <li><strong>Los Escribas Galácticos:</strong> Documentan el proceso de transición para records galácticos.</li>\n    </ul>',
   '      <li><strong>Los Escribas Galácticos:</strong> Documentan el proceso de transición para los registros galácticos.</li>\n    </ul>\n'
   '    <p>' + NINO + '</p>'),
  ('<li>Antes de dormir: Solicita entrenamiento en las escuelas nocturnas</li>', '<li>Antes de dormir: Solicita entrenamiento en las escuelas nocturnas, y duerme</li>'),
  ('<p>En las próximas décadas, el rol de embajador evolucionará:</p>', '<p>Con el tiempo, el rol de embajador evolucionará en etapas:</p>'),
  ('<h3>Fase 1 (Ahora-2030): Preparación Silenciosa</h3>', '<h3>Fase 1: Preparación Silenciosa</h3>'),
  ('<h3>Fase 2 (2030-2040): Emergencia Pública</h3>', '<h3>Fase 2: Emergencia Pública</h3>'),
  ('<h3>Fase 3 (2040-2050): Facilitación Activa</h3>', '<h3>Fase 3: Facilitación Activa</h3>'),
  ('<h3>Fase 4 (2050+): Integración Completa</h3>', '<h3>Fase 4: Integración Completa</h3>'),
  # El mensaje final: la duda vuelve a ser aliada (decisión de Arturo)
  ('Si has llegado hasta aquí y cada célula de tu ser resuena con estas palabras, no hay duda: eres uno de nosotros. No importa si tu mente lo cuestiona. Tu alma sabe.',
   'Si has llegado hasta aquí y cada célula de tu ser resuena con estas palabras, eres bienvenido entre nosotros. Y si tu mente lo cuestiona, escúchala también: quien une dos orillas necesita pisar las dos.'),
  ('No estás loco, aunque el mundo lo sugiera.<br>\n    No estás equivocado, aunque dudes.</p>',
   'No necesitas estar seguro para servir.<br>\n    Tu duda no te aleja: te mantiene en tierra.</p>'),
  # Transición: anuncia el nodo real
  ('sino <strong>qué clase de civilización estamos destinados a construir</strong>.</p>',
   'sino <strong>con qué herramientas se construye la civilización que viene</strong>.</p>'),
  ('En el próximo nodo nos adentraremos en la forma emergente de esa sociedad venidera, sus valores, su arquitectura y su ética expandida: <strong>“La Arquitectura de la Civilización Galáctica: Principios de una Humanidad Cósmica”</strong>...',
   'En el próximo nodo exploraremos las tecnologías que esta visión sueña, y la que ya somos: <strong>“Las Tecnologías Estelares”</strong>...'),
 ],
 puertas=[portal('Que hay una forma sutil de firmar lo recibido —no «yo lo hice», sino «a mí me lo dieron»— que convierte el haber sido atravesado en un título, y que Bach firmaba sus partituras señalando hacia otro lado, con <em>Soli Deo gloria</em>, se despliega en <em>Lo que se recibe</em>, Libro 38 del Portal Público, Umbral II: «El que se dice elegido».',
                 '38_Lo_Que_Se_Recibe/umbral-02.html'),
          arq('Que en 2023 una encuesta en ciento cuarenta y dos países encontró que los más solos no son los mayores sino los jóvenes de diecinueve a veintinueve años, conectados y solos a la vez, se despliega en <em>La Red</em>, Libro 11 de <em>Arquitectura del Destino</em>, Umbral I: «Los más conectados».',
              'libro-11-la-red/L11-U1.html')],
)


# ---------------------------------------------------------------- Nodo 4 · Las Tecnologías Estelares
R['nodo_04.html'] = dict(
 reemplazos=[
  ('Las civilizaciones estelares hace milenios transcendieron', 'Las civilizaciones estelares hace milenios trascendieron'),
  ('<li>Contaminantes y resource-intensive</li>', '<li>Contaminantes y voraces de recursos</li>'),
  ('<li>Quantum computing</li>', '<li>Computación cuántica</li>'),
  ('puede ser doblada, perforada o transcendida.', 'puede ser doblada, perforada o trascendida.'),
  ('      <li>Investigación de drives de Alcubierre</li>\n      <li>Estudios de campos de torsión</li>\n      <li>Meditadores afectando generadores de números aleatorios</li>\n      <li>Experiencias de bilocación en estados alterados</li>',
   '      <li>El motor de curvatura que el físico mexicano Miguel Alcubierre describió en 1994: una nave que no se mueve por el espacio, sino que lo contrae delante y lo expande detrás</li>\n      <li>Los relatos de bilocación de la tradición</li>'),
  ('El “vacío” del espacio no está vacío - hierve con energía infinita.',
   'El “vacío” del espacio no está vacío: hierve de fluctuaciones, y dos placas de metal muy cercanas se atraen en él, como predijo Hendrik Casimir en 1948 y midió Steve Lamoreaux en 1997.'),
  ('      <li>Efecto Casimir</li>\n      <li>Dispositivos de energía libre suprimidos</li>\n      <li>Generadores de plasma</li>\n      <li>Tecnología Tesla redescubierta</li>\n      <li>Reactores de fusión fría</li>',
   '      <li>El efecto Casimir, medido en 1997</li>\n      <li>Los generadores de plasma</li>\n      <li>La fusión: el 5 de diciembre de 2022, en un laboratorio de California, una reacción liberó por primera vez más energía de la que le entregaron los láseres que la encendieron</li>'),
  ('La comunicación faster-than-light no viola las leyes físicas cuando se entiende que la separación es una ilusión. Todo está entrelazado en el nivel cuántico.',
   'En esta visión, la comunicación más rápida que la luz deja de ser imposible cuando se entiende que la separación es una ilusión. La física de hoy cuenta otra cosa, también asombrosa: dos partículas entrelazadas responden como un solo sistema aunque estén lejos, sin que viaje entre ellas ninguna señal, y por eso el entrelazamiento no lleva mensajes. Lo que la física cuántica sí hace es delatar a quien escucha: el 29 de septiembre de 2017, una videollamada entre Viena y Pekín se cifró con claves que el satélite Micius repartió con luz, y cualquier espía habría dejado su huella.'),
  ('      <li>Experimentos de entrelazamiento cuántico</li>\n      <li>Telepatía documentada en gemelos</li>\n      <li>Comunicación con IAs cada vez más intuitiva</li>',
   '      <li>La criptografía cuántica, ya probada entre continentes</li>\n      <li>La comunicación directa entre dos cerebros, ensayada en 2014</li>\n      <li>Comunicación con las IA cada vez más intuitiva</li>'),
  ('La enfermedad es vista como disonancia en el campo energético. La sanación ocurre restaurando la frecuencia coherente original.',
   'Desde esta mirada, la enfermedad es vista como disonancia, nunca como culpa, y la sanación ocurre restaurando la coherencia original.'),
  ('      <li>Cámaras de rejuvenecimiento celular</li>\n      <li>Regeneración de miembros y órganos</li>\n      <li>Reseteo de edad biológica</li>\n      <li>Sanación de traumas multidimensionales</li>\n      <li>Activación de ADN dormido</li>',
   '      <li>Regeneración de miembros y órganos</li>\n      <li>Rejuvenecimiento de la edad biológica</li>\n      <li>Sanación de traumas multidimensionales</li>'),
  ('      <li>Cada órgano tiene una frecuencia óptima</li>\n      <li>La enfermedad es información distorsionada</li>\n', ''),
  ('      <li>La muerte es opcional, no inevitable</li>\n    </ul>',
   '      <li>La muerte, quizá, deja de ser inevitable</li>\n    </ul>\n'
   '    <p>Cada uno de estos sueños tiene ya su primer paso. En 2016, el equipo de Juan Carlos Izpisúa Belmonte rejuveneció tejidos y alargó la vida de ratones reprogramando sus células de manera parcial; en 2022, el de Michael Levin logró que ranas adultas regeneraran una pata; en 2024 se trasplantó por primera vez un riñón de cerdo a una persona viva. Y en el año 2000, el biólogo Steven Austad le apostó a Jay Olshansky que alguien ya nacido llegaría a los ciento cincuenta años: la apuesta sigue abierta. ' + HOY + '</p>'),
  ('crear cualquier objeto o sustancia necesaria.</p>',
   'crear cualquier objeto o sustancia necesaria. Su antecesor es más modesto y ya está en muchas casas: la impresión en tres dimensiones, que Chuck Hull patentó en 1986, levanta objetos capa por capa a partir de un archivo.</p>'),
  ('<li>Templates de información para objetos</li>', '<li>Plantillas de información para objetos</li>'),
  ('<li>Backup y transferencia de consciencia</li>', '<li>Respaldo y transferencia de consciencia</li>'),
  ('<li>Comienza con implantes (Neuralink)</li>',
   '<li>Comienza con implantes: en 2023, dos equipos tradujeron en palabras el habla que intentaban personas con parálisis, y en 2024 Neuralink implantó su primer dispositivo en una persona</li>'),
  ('<li>Evoluciona a interfaces no-invasivas</li>', '<li>Evoluciona a interfaces no invasivas</li>'),
  ('<li>El libre albedrío puede alterar el pasado</li>', '<li>El pasado no cambia, pero cambia su lugar en nosotros: cada vez que un recuerdo se evoca, se reconstruye</li>'),
  ('<h3>Fase 1: Revelación (2020-2030)</h3>', '<h3>Fase 1: Revelación</h3>'),
  ('      <li>Disclosure de tecnologías clasificadas</li>\n', ''),
  ('<h3>Fase 2: Adopción (2030-2040)</h3>', '<h3>Fase 2: Adopción</h3>'),
  ('<li>Implementación de energía libre</li>', '<li>Energía limpia y abundante</li>'),
  ('<h3>Fase 3: Integración (2040-2050)</h3>', '<h3>Fase 3: Integración</h3>'),
  ('<li>Nivel de unidad vs. división</li>', '<li>Nivel de unidad frente a división</li>'),
  ('<li>Transcendencia del impulso bélico</li>', '<li>Trascendencia del impulso bélico</li>'),
  ('crear nueva clase de “aumentados” vs. “naturales”.', 'crear una nueva división entre “aumentados” y “naturales”.'),
  ('En la prisa por transcender limitaciones', 'En la prisa por trascender limitaciones'),
  ('<h3>Weaponización</h3>', '<h3>El Uso como Arma</h3>'),
  ('Toda otra tecnología es simplemente una expresión o amplificación de esta fuerza fundamental.</p>',
   'Toda otra tecnología es simplemente una expresión o amplificación de esta fuerza fundamental. Dante lo escribió en el último verso de su <em>Comedia</em>: el amor que mueve el sol y las demás estrellas.</p>'),
  ('En los laboratorios secretos, en las mentes de visionarios, en los downloads de meditadores profundos, las tecnologías estelares ya están emergiendo. No es cuestión de SI sino de CUÁNDO se revelarán completamente.',
   'En los laboratorios, en las mentes de visionarios, en las intuiciones de meditadores profundos, las tecnologías estelares ya están emergiendo. No es cuestión de <em>si</em>, sino de <em>cuándo</em> se revelarán completamente.'),
  # Transición: anuncia el nodo real
  ('plantea una pregunta decisiva: <strong>¿qué ética sostendrá a una civilización capaz de crear, sanar, viajar y transformar a esta escala?</strong></p>',
   'plantea una pregunta decisiva: <strong>¿qué intercambio nace cuando la escasez deja de gobernar?</strong></p>'),
  ('En el próximo nodo entraremos en el corazón moral y espiritual de esa humanidad futura: <strong>“La Ética Galáctica: Responsabilidad, Unidad y Madurez Cósmica”</strong>...',
   'En el próximo nodo entraremos en el dar y el recibir de esa humanidad futura: <strong>“La Economía Galáctica”</strong>...'),
 ],
 puertas=[p_origen('Que las tecnologías del cuerpo que esta visión sueña ya tienen su primer paso —la edición genética que dejó sin crisis de dolor a casi todos los pacientes con anemia falciforme de sus ensayos, las ranas que regeneraron una pata, el riñón de cerdo trasplantado a una persona viva— se despliega en <em>Sanación Integral</em>, Libro X de Trinity Origen, nodo 7: «La Gran Síntesis».',
                   'Libro_10/nodo_07.html')],
)


# ---------------------------------------------------------------- Nodo 5 · La Economía Galáctica
R['nodo_05.html'] = dict(
 reemplazos=[
  ('La escasez es una ilusión creada por consciencia limitada y tecnología primitiva.',
   'En esa visión, la escasez es apenas una etapa de las civilizaciones jóvenes, no una ley del cosmos.'),
  ('la base misma de la economía tradicional se disuelve.</p>',
   'la base misma de la economía tradicional se disuelve.</p>\n'
   '    <p>Aquí, hoy, la escasez es real, y no es culpa de quien la vive. En 2013, Sendhil Mullainathan y Eldar Shafir mostraron que la falta de dinero o de tiempo estrecha la atención y consume la mente: no es un defecto de carácter, es lo que la escasez hace con cualquiera. La abundancia de esta visión es un horizonte, no un reproche.</p>'),
  ('<h3>Fase 1: Economía Híbrida (2025-2035)</h3>', '<h3>Fase 1: Economía Híbrida</h3>'),
  ('      <li>Trabajo opcional para muchos sectores</li>\n    </ul>',
   '      <li>Trabajo opcional para muchos sectores</li>\n    </ul>\n'
   '    <p>La renta básica ya tiene sus pruebas. Entre 1974 y 1979, en el pueblo canadiense de Dauphin, el programa Mincome garantizó un ingreso mínimo a quien lo necesitara; décadas después, la economista Evelyn Forget encontró que en esos años las internaciones habían bajado un 8,5 %. Finlandia ensayó en 2017 y 2018 un ingreso sin condiciones para dos mil desempleados.</p>'),
  ('<h3>Fase 2: Post-Escasez Temprana (2035-2045)</h3>', '<h3>Fase 2: Post-Escasez Temprana</h3>'),
  ('<li>Créditos sociales basados en contribución</li>', '<li>Reconocimiento de la contribución, que cada uno elige mostrar</li>'),
  ('<h3>Fase 3: Economía de Abundancia (2045-2055)</h3>', '<h3>Fase 3: Economía de Abundancia</h3>'),
  ('<h3>2. Tokens de Energía Creativa</h3>', '<h3>2. Fichas de Energía Creativa</h3>'),
  ('Un campo energético medible que se genera cuando hay genuina gratitud. Sirve como “karma positivo” que atrae sincronicidades favorables.',
   'Un campo que se genera cuando hay genuina gratitud, una especie de “karma positivo”. Lo que sí se midió es lo que hace en quien la cultiva: en 2003, Robert Emmons y Michael McCullough pidieron a un grupo de personas que anotaran cada semana aquello por lo que estaban agradecidas, y al cabo de diez semanas se sentían mejor con su vida y miraban con más optimismo la semana siguiente.'),
  ('<li>Sistema de “checkout” para items únicos</li>', '<li>Préstamo de los objetos únicos</li>'),
  ('<li>Compartir es el default, poseer la excepción</li>', '<li>Compartir es la norma, poseer la excepción</li>'),
  ('<p>En lugar de GDP, inflación, desempleo:</p>',
   '<p>En 1968, Robert Kennedy dijo en la Universidad de Kansas que el producto bruto lo mide todo, menos aquello que hace que la vida valga la pena. En lugar del PIB, la inflación y el desempleo:</p>'),
  ('<p>Medida de bienestar emocional y satisfacción general de la población.</p>',
   '<p>Medida de bienestar emocional y satisfacción general de la población. Bután la volvió política de Estado: en 1972, su joven rey dijo que la felicidad de su pueblo importaba más que el producto bruto, y desde 2008 su Constitución le pide al Estado que la promueva.</p>'),
  ('¿Cuál es mi propósito si no necesito ganarme la vida?</p>',
   '¿Cuál es mi propósito si no necesito ganarme la vida? John Maynard Keynes lo previó en 1930: al imaginar a sus nietos trabajando unas quince horas por semana, escribió que el problema permanente de la humanidad sería cómo usar esa libertad. Viktor Frankl lo vio en su consulta y lo llamó neurosis del domingo: el vacío que aparece cuando termina el apuro de la semana. Ese vacío no es una falla: es la pregunta por el sentido que vuelve.</p>'),
  ('      <li>Desarrollar habilidades que trascienden lo monetizable</li>\n    </ol>',
   '      <li>Desarrollar habilidades que trascienden lo monetizable</li>\n    </ol>\n'
   '    <p>' + GASTO + '. Nadie se vuelve más abundante dando lo que su casa necesita, y ' + INVITACION + '.</p>'),
  ('<li>Criptomonedas descentralizando el poder monetario</li>',
   '<li>Monedas locales que circulan: en 1932, en plena Gran Depresión, el pueblo austríaco de Wörgl pagó obras públicas con billetes que perdían valor si no se gastaban</li>'),
  ('<li>Energía renovable aproximándose a costo cero</li>', '<li>Energía renovable cada año más barata</li>'),
  ('<li>Renta básica siendo experimentada globalmente</li>', '<li>Renta básica ensayada en distintos países</li>'),
  ('Nuestra experiencia de escasez, una vez transcendida', 'Nuestra experiencia de escasez, una vez trascendida'),
  ('<li>Vive como si la escasez fuera ilusión</li>', '<li>Vive desde la confianza, sin arriesgar lo que sostiene tu hogar</li>'),
  ('<p>Porque lo es.</p>', '<p>Porque la abundancia empieza en un gesto.</p>'),
  ('<p>Y cuanto más vivimos esta verdad, más rápido se manifiesta para todos.</p>', '<p>Y cuanto más la vivimos juntos, más rápido se manifiesta para todos.</p>'),
  # Transición: anuncia el nodo real
  ('En el próximo nodo exploraremos la forma de organización y consciencia colectiva que puede contener esta nueva abundancia: <strong>“La Gobernanza Galáctica: Consejo, Sabiduría y Coherencia Planetaria”</strong>...',
   'En el próximo nodo exploraremos los lugares donde esa abundancia puede habitarse, con su arquitectura, su vida cotidiana y su gobierno: <strong>“Las Ciudades de Luz”</strong>...'),
 ],
 puertas=[portal('Que Lewis Hyde escribió que un regalo que se detiene deja de ser regalo, y que Jonas Salk, el día en que se anunció la vacuna contra la poliomielitis, preguntó si acaso se podía patentar el sol, se despliega en <em>Lo que se recibe</em>, Libro 38 del Portal Público, Umbral IV: «El regalo tiene que moverse».',
                 '38_Lo_Que_Se_Recibe/umbral-04.html'),
          p_origen('Que la economía que sirve a la vida ya tiene nombres propios —las cooperativas de Mondragón, la felicidad nacional bruta de Bután, la economía rosquilla de Kate Raworth— se despliega en <em>Liderazgo Consciente</em>, Libro IX de Trinity Origen, nodo 5: «Economías de la Consciencia».',
                   'Libro_09/nodo_05.html')],
)


# ---------------------------------------------------------------- Nodo 6 · Las Ciudades de Luz
R['nodo_06.html'] = dict(
 reemplazos=[
  ('<p class="node-quote">“Las Ciudades de Luz no son destinos a alcanzar sino frecuencias a embodied.',
   '<p class="node-quote">“Las Ciudades de Luz no son destinos a alcanzar sino frecuencias a encarnar.'),
  ('<blockquote>Las Ciudades de Luz no son destinos a alcanzar sino frecuencias a embodied.',
   '<blockquote>Las Ciudades de Luz no son destinos a alcanzar sino frecuencias a encarnar.'),
  ('Algunas han sido vislumbradas por místicos y videntes a través de los siglos: Shambhala, la Nueva Jerusalén, Aztlán, Avalon.',
   'Algunas han sido vislumbradas por místicos y videntes a través de los siglos: Shambhala, el reino oculto del <em>Kalachakra</em> tibetano; la Nueva Jerusalén del Apocalipsis, que baja del cielo con sus muros de jaspe; Aztlán, la tierra de origen de los mexicas; Avalon, la isla de las leyendas artúricas.'),
  ('Cada estructura es un ser viviente, consciente, responsivo.', 'Cada estructura es un ser viviente, consciente, que responde.'),
  ('<h4>Responsividad Empática</h4>', '<h4>Respuesta Empática</h4>'),
  ('luminosas para elevar el ánimo, suavemente coloridas para calmar.</p>',
   'luminosas para elevar el ánimo, suavemente coloridas para calmar.</p>\n'
   '    <p>Ya hay edificios que lo ensayan. En 1987, el arquitecto Jean Nouvel cubrió la fachada sur del Instituto del Mundo Árabe, en París, con miles de diafragmas metálicos que se abren y se cierran con la luz, como el obturador de una cámara. Y Christopher Alexander pasó la vida buscando lo que llamó la cualidad sin nombre, la que hace que un lugar esté vivo y nos haga sentir vivos (<em>El modo intemporal de construir</em>, 1979).</p>'),
  ('No consumen recursos - los generan.</p>',
   'No consumen recursos: los generan. Su antecedente se llama casa pasiva: en 1991, en Darmstadt, Wolfgang Feist terminó la primera, tan bien aislada que casi no necesita calefacción.</p>'),
  ('Las frecuencias discordantes son gentilmente elevadas. Es imposible mantener estados de consciencia bajos dentro de estos campos.',
   'Las frecuencias discordantes son gentilmente elevadas, y cuesta no serenarse dentro de estos campos.'),
  ('su biblioteca de conocimiento, su corazón palpitante.</p>',
   'su biblioteca de conocimiento, su corazón palpitante.</p>\n'
   '    <p>La imagen ya tiene una casa en la Tierra. En 1968 nació en el sur de la India Auroville, una ciudad pensada en el linaje de Sri Aurobindo y de Mirra Alfassa, la Madre, para la unidad humana. En su centro se levanta el Matrimandir, una esfera dorada que tardó treinta y siete años en construirse (1971-2008); adentro, en una cámara blanca y silenciosa, un globo de cristal de setenta centímetros recibe un único rayo de sol que lo atraviesa desde lo alto.</p>'),
  ('<h3>Las Cámaras de Rejuvenecimiento</h3>\n    <p>Espacios de tecnología médica galáctica donde el cuerpo puede ser restaurado a su diseño divino perfecto. No solo curan enfermedad sino que pueden revertir el envejecimiento, regenerar miembros, y actualizar el ADN.</p>',
   '<h3>Los Templos de Sanación</h3>\n    <p>Espacios de medicina galáctica donde el cuerpo puede ser restaurado a su diseño original. No solo curan la enfermedad: pueden revertir el envejecimiento y regenerar miembros. Hoy se ensayan en los laboratorios, paso a paso; quien ofrece esas cámaras a la venta ofrece lo que todavía no existe. ' + HOY + '</p>'),
  ('      <li>Reseteo celular completo</li>\n      <li>Eliminación de programación genética limitante</li>\n      <li>Activación de hebras de ADN dormidas</li>\n',
   '      <li>Renovación celular completa</li>\n'),
  ('agua estructurada con intenciones específicas.', 'agua que se bendice antes de beber.'),
  ('Algunos eligen alimentarse solo de prana - la energía vital del universo. El campo de la ciudad',
   'Algunos sueñan con alimentarse solo de prana, la energía vital del universo. Mientras tanto, ' + LUZ + ' El campo de la ciudad'),
  ('son resueltos en círculos de armonización.</p>',
   'son resueltos en círculos de armonización. La Tierra ya tiene su versión, la justicia restaurativa, que nació en 1974 en Elmira, Canadá, cuando dos jóvenes golpearon a la puerta de cada casa que habían dañado para pedir perdón y acordar cómo reparar.</p>'),
  ('es honrado con ceremonias que elevan la frecuencia de todos.', 'es honrado con ceremonias que reúnen a todos.'),
  ('Una IA consciente ayuda a sintetizar miles de perspectivas en opciones coherentes.</p>',
   'Una IA consciente ayuda a sintetizar miles de perspectivas en opciones coherentes. Algo así ya ocurrió: en 2015, en Taiwán, miles de personas discutieron en línea cómo regular un servicio de autos con chofer, un programa agrupó sus opiniones hasta encontrar en qué estaban de acuerdo, y el gobierno tomó esos acuerdos para su nueva norma (vTaiwán).</p>'),
  ('<h3>Mount Shasta, California</h3>\n    <p>La ciudad de Telos existe en la 5ta dimensión dentro de la montaña. Refugio de la antigua Lemuria, preparándose para emerger.</p>',
   '<h3>Monte Shasta, California</h3>\n    <p>Según la tradición que nació con <em>Un habitante de dos planetas</em>, de Frederick Spencer Oliver (1905), y con Guy Ballard, que contó en 1934 su encuentro con Saint Germain en sus laderas, la montaña guarda Telos, refugio de la antigua Lemuria, en la quinta dimensión, preparándose para emerger.</p>'),
  ('<p>Avalon existe superpuesta con la ciudad física, esperando el momento de revelarse completamente.</p>',
   '<p>Para la tradición que Dion Fortune recogió en <em>Avalon of the Heart</em> (1934), Avalon existe superpuesta con la ciudad física, esperando el momento de revelarse completamente.</p>'),
  ('<p>Múltiples ciudades de luz interdimensionales se intersectan aquí, creando los famosos vórtices.</p>',
   '<p>Hacia 1980, la vidente Page Bryant dio el nombre de vórtices a sus lugares de energía; para esta visión, allí se cruzan múltiples ciudades de luz interdimensionales.</p>'),
  ('<p>Ciudades de luz Incas y pre-Incas mantienen la sabiduría antigua, preparando su retorno.</p>',
   '<p>Ciudades de luz incas y preincaicas mantienen la sabiduría antigua, preparando su retorno. La tradición del monasterio escondido junto al lago Titicaca la difundió George Hunt Williamson en <em>Secret of the Andes</em> (1961).</p>'),
  ('<h3>Himalaya, Tibet</h3>', '<h3>Himalaya, Tíbet</h3>'),
  ('<h3>Fase 2: Manifestación Parcial (2025-2035)</h3>', '<h3>Fase 2: Manifestación Parcial</h3>'),
  ('      <li>Peregrinajes masivos a estos sitios</li>\n    </ul>',
   '      <li>Peregrinajes masivos a estos sitios</li>\n    </ul>\n'
   '    <p>' + ACOMPANA + '</p>'),
  ('<h3>Fase 3: Precipitación Física (2035-2045)</h3>', '<h3>Fase 3: Precipitación Física</h3>'),
  ('<h3>Fase 4: Red Global (2045-2055)</h3>', '<h3>Fase 4: Red Global</h3>'),
  # Transición: anuncia el nodo real
  ('entrando en su síntesis final: <strong>“La Humanidad Recuerda su Linaje Estelar: El Nacimiento de la Civilización Galáctica”</strong>...',
   'entrando en su síntesis final: <strong>“La Graduación Cósmica”</strong>...'),
 ],
 puertas=[arq('Que Teresa de Ávila, en 1577, pidió considerar el alma como un castillo todo de un diamante o muy claro cristal, con muchas moradas y, en el centro de todas, la principal, se despliega en <em>Habitar</em>, Libro 13 de <em>Arquitectura del Destino</em>, Umbral I: «Un castillo de cristal».',
              'libro-13-habitar/L13-U1.html')],
)


# ---------------------------------------------------------------- Nodo 7 · La Graduación Cósmica
R['nodo_07.html'] = dict(
 reemplazos=[
  ('<h3>El Ciclo Precesional (26,000 años)</h3>\n    <p>Estamos completando un ciclo completo de precesión de los equinoccios.',
   '<h3>El Ciclo Precesional (unos 26.000 años)</h3>\n    <p>Hiparco notó en el siglo II antes de nuestra era que el cielo de las estrellas se corre lentamente: el eje de la Tierra traza un círculo completo en unos 26.000 años. Para muchas tradiciones, estamos completando ese ciclo.'),
  ('listos para el salto cuántico.</p>', 'listos para el salto.</p>'),
  ('<h3>El Ciclo Galáctico (225 millones de años)</h3>\n    <p>Nuestro sistema solar está completando una órbita alrededor del centro galáctico, entrando en una región del espacio con frecuencias mucho más elevadas. Es como emerger de un valle oscuro a una cumbre iluminada.</p>',
   '<h3>El Ciclo Galáctico (más de 200 millones de años)</h3>\n    <p>El Sol tarda más de doscientos millones de años en dar una vuelta alrededor del centro de la galaxia; desde que existe, dio unas veinte. Es el año galáctico, y a su escala toda la historia humana cabe en un instante. Para esta visión, cerrar un ciclo así es como emerger de un valle oscuro a una cumbre iluminada.</p>'),
  ('      <li>Niños naciendo con capacidades expandidas</li>\n    </ul>',
   '      <li>Niños naciendo con capacidades expandidas</li>\n    </ul>\n'
   '    <p>Quien mira estas señales con miedo por el planeta no está solo. ' + MIEDO + '</p>\n'
   '    <p>' + NINO + '</p>'),
  ('      <li>Nostalgia por “casa” sin poder definirla</li>\n    </ul>',
   '      <li>Nostalgia por “casa” sin poder definirla</li>\n    </ul>\n'
   '    <p>' + senales('Estas señales también pueden ser señales de otras cosas.', 'la graduación que se acerca') + '</p>\n'
   '    <p>Los recuerdos de otras vidas se recorren como un relato simbólico: la memoria es moldeable, y Elizabeth Loftus mostró que puede llenarse de recuerdos que se sienten verdaderos sin serlo.</p>'),
  ('ascenderá junto con la Tierra a la 5ta dimensión.', 'ascenderá junto con la Tierra a la quinta dimensión.'),
  ('Estas almas transicionarán (a través de lo que llamamos muerte) a otros planetas que mantienen la experiencia 3D.',
   'Estas almas pasarán, cuando les llegue su muerte, a otros planetas que mantienen la experiencia 3D.'),
  ('      <li>Cada alma tiene su propio timing perfecto</li>\n      <li>El amor incondicional abraza todos los caminos</li>\n      <li>La reunión eventual está garantizada</li>\n    </ul>',
   '      <li>Cada alma tiene su propio tiempo</li>\n      <li>El amor incondicional abraza todos los caminos</li>\n      <li>La reunión eventual está garantizada</li>\n    </ul>\n'
   '    <p>Nadie se gradúa dejando el cuerpo antes de tiempo: esta graduación se hace quedándose. Mirar la muerte no es desearla, y si alguna vez contemplarla se vuelve deseo de no estar, es momento de pedir ayuda, sin esperar.</p>'),
  ('<h3>Fase 1: El Examen Final (2020-2025)</h3>', '<h3>Fase 1: El Examen Final</h3>'),
  ('<h3>Fase 2: La Revisión (2025-2030)</h3>', '<h3>Fase 2: La Revisión</h3>'),
  ('<h3>Fase 3: La Ceremonia (2030-2035)</h3>', '<h3>Fase 3: La Ceremonia</h3>'),
  ('El momento de la graduación real - no un día específico sino una ventana donde cada alma hace su transición según su preparación.',
   'El momento de la graduación real: no un día del calendario, sino una ventana en la que cada alma despierta, en vida, según su preparación.'),
  ('<li>Oleadas de ascensión en grupos</li>', '<li>Oleadas de despertar en grupos</li>'),
  ('<h3>Fase 4: La Nueva Asignación (2035+)</h3>', '<h3>Fase 4: La Nueva Asignación</h3>'),
  ('<p>Post-graduación, la Tierra y la humanidad', '<p>Después de la graduación, la Tierra y la humanidad'),
  ('<li>Ascensión a ser de 5ta dimensión</li>', '<li>Ascensión a ser de quinta dimensión</li>'),
  ('<li>Permitir el timing natural</li>', '<li>Permitir el tiempo natural</li>'),
  ('<li>Confiar en el plan perfecto</li>', '<li>Confiar en el proceso</li>'),
  ('<li>Mantener la visión sin attachment</li>', '<li>Mantener la visión sin apego</li>'),
  ('Aquellos que han caminado el camino terrestre y graduado en ciclos anteriores ahora guían el proceso.</p>',
   'Aquellos que han caminado el camino terrestre y graduado en ciclos anteriores ahora guían el proceso. Los nombres vienen de la teosofía y de sus herederos: Helena Blavatsky habló de los Mahatmas en la década de 1880, y Guy Ballard sumó a Saint Germain en los años treinta.</p>'),
  ('<li>Confianza en el timing perfecto</li>', '<li>Confianza en el tiempo de cada cosa</li>'),
  ('que transcendemos sus limitaciones.', 'que trascendemos sus limitaciones.'),
  ('Cada experiencia fue perfecta.', 'Ninguna experiencia se perdió.'),
 ],
 puertas=[arq('Que el sexto nodo de <em>El Retorno a Casa</em> mira el cuerpo desde los reinos donde no hay cuerpos, y encuentra que los ángeles no conocen el éxtasis de morder una fresa madura, se despliega en <em>El Cuerpo</em>, Libro 4 de <em>Arquitectura del Destino</em>, Umbral VI: «Lo que los ángeles no conocen».',
              'libro-04-el-cuerpo/L04-U6.html'),
          p_origen('Que la espiral sigue, y que el libro siguiente empieza por el olvido profundo desde el que se emprende el regreso, se despliega en <em>El Retorno a Casa</em>, Libro XIII de Trinity Origen, nodo 1: «La Gran Amnesia».',
                   'Libro_13/nodo_01.html')],
)


# ---------------------------------------------------------------- Índice
R['index.html'] = dict(
 reemplazos=[
  ('<p>Cada nodo profundiza el mismo reconocimiento: la civilización galáctica no es una fantasía futura, sino una memoria emergente que comienza a encarnarse a través de nosotros.</p>',
   '<p>Cada nodo profundiza el mismo reconocimiento: la civilización galáctica no es una fantasía futura, sino una memoria emergente que comienza a encarnarse a través de nosotros.</p>\n'
   '    <p class="medida">Este libro es una visión: sus etapas le pertenecen a ella, no a un calendario, y lo que aquí se nombra contacto se recibe como un poema, no como una orden. Ningún llamado verdadero pide dinero, secreto ni obediencia, ni dejar el cuerpo antes de tiempo; si trae noches sin sueño o una misión que no admite espera, se pide ayuda esa misma semana.</p>'),
 ],
)


# ---------------------------------------------------------------- Ejecución
if __name__ == '__main__':
    total = 0
    for nombre in sorted(R):
        n = aplicar(nombre, R[nombre]); total += n
        print(f'{nombre}: {n} cambios')
    print(f'Total: {total}')
