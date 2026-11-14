# Depuración de Origen XI, La Consciencia Planetaria (noviembre de 2026), con el veto del Lic. Arturo Rodríguez.
# Lente: riesgo clínico y puertas hacia la Red, como en Origen VI, VIII e I. La visión del libro queda entera
# (Gaia que vive y despierta, la noosfera, el Campo del que somos olas, la gran transición, los aliados,
# la Nueva Tierra, el servicio), con su linaje y, donde existe, con su primer paso real (precisión 6).
# El riesgo vivía en tres cosas que se le mezclaban: un calendario del fin, una guerra de la luz contra
# enemigos ocultos y listas de síntomas leídos como «ascensión». Quien hoy busca este libro suele llegar con
# miedo por el planeta, y el libro obedece a sus mejores frases: «"No sé" es la puerta a la sabiduría»,
# «Desesperación → Esperanza activa», «La Nueva Tierra no es un lugar». Por decisión de Arturo, las
# cronologías quedan en etapas, sin años. Su columna escondida es la casa: abre diciendo que Gaia no es
# nuestra casa y cierra con «Bienvenidos a casa». Se abren diez puertas, todas de ida y vuelta.
#
# Se aplica sobre el original de la etiqueta origen-original, con reemplazos que deben aparecer exactamente
# una vez (o tramos, de un texto a otro, inclusive); si un anclaje falla, el script se detiene sin escribir.
#
# Uso: ORIGEN11_SRC=RUTA/origen-original/01_Trinity_Origen/Libro_11/ ORIGEN11_OUT=RUTA/salida/ python3 depurar_origen11.py
import os, re, sys

SRC = os.environ.get('ORIGEN11_SRC', '/home/claude/work11/o11/01_Trinity_Origen/Libro_11/')
OUT = os.environ.get('ORIGEN11_OUT', '/home/claude/work11/out/01_Trinity_Origen/Libro_11/')

NOTA = ('<!-- Depurado en noviembre de 2026 según la guía de depuración de Quantum, que vale para Origen '
        '(Arquitectura del Destino, maestro v4, sección 5, con las precisiones 5 y 6 de Origen), con el veto del Lic. Arturo Rodríguez: '
        'la visión del libro queda, con su linaje; salen las fechas del fin, las cifras sin fuente, las teorías conspirativas y lo que se vende '
        'como si funcionara; los síntomas dejan de leerse como ascensión; se suma el cuidado clínico en la voz de cada nodo y se abren puertas '
        'fractales hacia la Red. El original está en la etiqueta origen-original del repositorio Trinity-. -->\n')

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
        cierre = '\n  </main>'
        t = una_vez(t, cierre, '\n' + ''.join(d['puertas']).rstrip('\n') + cierre, 'el cierre del <main>'); cuenta += 1
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, nombre), 'w', encoding='utf-8') as f:
        f.write(t)
    return cuenta



# Frases de cuidado propias de este libro
MIEDO = ('Ese miedo no es una enfermedad: es una respuesta a algo real. Si quita el sueño o las ganas durante semanas, se consulta; '
         'y se alivia más haciendo con otros que leyendo a solas.')
DANO = ('Si sientes que otros te dañan a distancia, o que necesitas protegerte todo el tiempo, vale la pena hablarlo con un profesional: '
        'ese miedo también se cuida.')   # Origen X.5
REFERENCIA = ('Si alguna vez parece que cada número y cada cartel te hablan a ti, en secreto, eso no es un don: conviene conversarlo '
              'con alguien de confianza o con un profesional esa misma semana.')   # Quantum 11.2
LUZ = 'El cuerpo de hoy necesita comida: quienes intentaron vivir solo de luz enfermaron, y algunos murieron.'   # Origen X.5 y VI.7
MIRARLA = ('Mirarla no es desearla: es aprender a no vivir de espaldas a ella. Y si alguna vez contemplar la muerte se vuelve deseo '
           'de no estar, es momento de pedir ayuda, sin esperar.')   # Origen X.7
NINO = ('Ver en un niño un don no quita mirar también lo que necesita: si le cuesta atender, aprender o vincularse, una consulta '
        'puede abrirle caminos.')   # Origen VI.7 y XIII.7
DOLOR = 'Un dolor que persiste, un síntoma nuevo o un cansancio sin causa merecen que alguien los revise.'   # Origen X.1


# ---------------------------------------------------------------- Nodo 1
# Gaia queda viva en la voz de la tradición; la ciencia entra con lo que dijo (Lovelock y Margulis, Daisyworld).
# Schumann queda como latido y pierde la aceleración; el miedo por el planeta encuentra su nombre y su cuidado.
R['nodo_01.html'] = dict(
 reemplazos=[
  ('<p class="lead">James Lovelock propuso la Hipótesis Gaia: la Tierra como sistema autorregulado. Pero era tímido. No se atrevió a decir lo que intuía: <strong>la Tierra no solo se autorregula, está VIVA, es CONSCIENTE, está EVOLUCIONANDO</strong>.</p>',
   '<p class="lead">En los años setenta, James Lovelock y Lynn Margulis propusieron la Hipótesis Gaia: la vida regula las condiciones del planeta que la sostiene. El nombre se lo sugirió a Lovelock un vecino, el novelista William Golding. La ciencia llegó hasta ahí, y Lovelock fue claro: ni él ni Margulis le atribuyeron a Gaia un propósito. Las tradiciones dieron el paso siguiente mucho antes, y lo siguen dando: <strong>la Tierra no solo se autorregula, está VIVA, es CONSCIENTE, está EVOLUCIONANDO</strong>. La Pachamama de los Andes, la Gea de Hesíodo, el alma del mundo que Platón describe en el <em>Timeo</em>: muchas voces para una misma intuición.</p>'),
  ('<p>La evidencia es abrumadora:</p>', '<p>Lo que se observa es asombroso:</p>'),
  ('<li><strong>Evolución dirigida:</strong> La vida aumenta en complejidad y consciencia</li>',
   '<li><strong>Evolución creciente:</strong> La vida ha ido ganando complejidad y consciencia</li>'),
  (('<pre>EDAD: 4,500 millones de años', 'TEMPERATURA PROMEDIO: 15°C (perfecta para la vida)</pre>'),
   '<pre>EDAD: 4.500 millones de años\n'
   'DIÁMETRO: 12.742 km\n'
   'VELOCIDAD DE ROTACIÓN: 1.670 km/h en el ecuador\n'
   'ÓRBITA ALREDEDOR DEL SOL: 940 millones de km por año\n'
   'CAMPO MAGNÉTICO: 25-65 microteslas\n'
   'RESONANCIA SCHUMANN: 7,83 Hz (el "latido")\n'
   'BIODIVERSIDAD: unos 8,7 millones de especies\n'
   '  (estimadas; descritas, algo más de 1,2 millones)\n'
   'AGUA: 1.386 millones de km³\n'
   'TEMPERATURA PROMEDIO: 15 °C (templada para la vida)</pre>'),
  ('<p>Cada número es <strong>precisamente calibrado</strong> para sostener la vida. No es casualidad. Es inteligencia.</p>',
   '<p>Ninguno de estos números lo <strong>calibró</strong> alguien, y en eso está el asombro. A quienes objetaron que una Tierra que se regula necesitaría un plan, Lovelock y Andrew Watson respondieron en 1983 con un planeta imaginario, Daisyworld, poblado solo de margaritas: las negras absorben el calor, las blancas lo reflejan, y entre las dos, sin que ninguna lo busque, la temperatura se mantiene templada mientras su sol se vuelve más brillante. No es casualidad: es la inteligencia de la vida entera, que no necesita que nadie la planee.</p>'),
  ('<p class="lead">7.83 Hz - la frecuencia fundamental de la Tierra, descubierta por Winfried Schumann. Pero es más que una frecuencia:</p>',
   '<p class="lead">7,83 Hz: la nota fundamental de la cavidad que forman la Tierra y la ionosfera, predicha por el físico alemán Winfried Otto Schumann en 1952 y medida por primera vez en 1960. La encienden los rayos: decenas de descargas por segundo, en todo el planeta, la mantienen sonando, con sus armónicos cerca de 14, 20, 26 y 33 Hz. Como imagen, es más que una frecuencia:</p>'),
  (('      <li>Sincroniza todos los sistemas vivos</li>', '      <li>Conecta toda vida</li>'),
   '      <li>Envuelve a todos los seres vivos</li>\n'
   '      <li>Late en la misma franja que las ondas lentas del cerebro, una coincidencia que muchos leen como parentesco</li>\n'
   '      <li>Acompaña cada día y cada noche del planeta</li>\n'
   '      <li>Conecta toda vida</li>'),
  (('<p><strong>Cambios Recientes Alarmantes:</strong></p>', 'GAIA ESTÁ ACELERANDO</pre>'),
   '<p><strong>Lo que de verdad se mueve:</strong> la frecuencia sube y baja unas décimas a lo largo del día, siguiendo a las tormentas del mundo y al Sol. Los «picos» de 15 a 90 Hz que circulan en imágenes no son la Tierra que se acelera: son los armónicos de siempre, o tormentas y ruidos cercanos que tiñen el gráfico. El latido es constante, y en esa constancia hay algo que serena.</p>'),
  ('<li>El Cinturón de Fuego (Pacífico)</li>\n    </ul>',
   '<li>El Cinturón de Fuego (Pacífico)</li>\n    </ul>\n'
   '    <p>El nombre tiene historia: Alfred Watkins llamó así, en los años veinte, a alineaciones de sitios antiguos en Inglaterra, y la idea de que fueran líneas de energía llegó medio siglo después. La lista reúne, además, cosas distintas: un camino de peregrinos, figuras trazadas en el desierto, el anillo de volcanes del Pacífico. Como mapa del alma de la Tierra, se recorre con la libertad de un poema.</p>'),
  ('<h3>Los Siete Vórtices Principales</h3>',
   '<h3>Los Siete Vórtices Principales</h3>\n'
   '    <p>El mapa más difundido de los chakras de la Tierra es el de Robert Coon, que lo trabaja desde los años setenta; otros autores lo varían. Es una cartografía de lugares sagrados para muchos pueblos, y así se recorre: con respeto por quienes los cuidan.</p>'),
  ('<li>Antártida: Portal de consciencia pristina</li>', '<li>Antártida: Portal de consciencia prístina</li>'),
  ('      <li>Cambios en Schumann</li>\n', ''),
  ('<li>Crop circles genuinos</li>',
   '<li>Figuras en los trigales: desde 1991, cuando Doug Bower y Dave Chorley contaron cómo las trazaban, se sabe que las hacen manos humanas, y algunas son obras de arte</li>'),
  ('2. Respiración sincronizada con Schumann', '2. Respiración lenta, cerca de seis por minuto'),
  ('7. Anclar información recibida</pre>',
   '7. Anclar información recibida</pre>\n'
   '    <p>El latido de Schumann, casi ocho veces por segundo, no se puede respirar; el cuerpo tiene su propio compás lento, el de unas seis respiraciones por minuto, en el que el corazón y el aliento se encuentran (Bernardi y otros, 2001). Lo que llegue en la escucha se recibe como se recibe un poema, no como una orden.</p>'),
  ('- Tambor a 7.83 Hz', '- Tambor de pulso lento y parejo'),
  ('<li>Co-creadores conscientes</li>\n    </ul>',
   '<li>Co-creadores conscientes</li>\n    </ul>\n'
   '    <p>Ninguna de las tres opciones es un veredicto sobre ti. La culpa por ser humano no cuida a la Tierra; el cuidado sí, y empieza por lo que está al alcance de la mano.</p>'),
  (('      <li>Huracanes más intensos</li>', '      <li>Pandemias emergentes</li>'),
   '      <li>Huracanes más intensos</li>\n'
   '      <li>Incendios más extensos</li>\n'
   '      <li>Sequías e inundaciones más extremas</li>\n'
   '      <li>Enfermedades que saltan de los animales a las personas cuando se pierde el bosque</li>'),
  (('    <h4>1. Homeopatía Planetaria</h4>', '<li>Información vibracional distribuida</li>\n    </ul>'),
   '    <h4>1. Conocer el Lugar</h4>\n'
   '    <ul>\n'
   '      <li>Aprender los nombres de lo que vive cerca</li>\n'
   '      <li>Seguir el agua desde donde llega hasta donde va</li>\n'
   '      <li>Visitar los lugares sagrados con respeto</li>\n'
   '      <li>Dejar cada sitio mejor de lo que estaba</li>\n'
   '    </ul>'),
  ('<li>Cristales en puntos nodales</li>', '<li>Ofrendas en los lugares de poder</li>'),
  ('<li>Corrección de líneas ley</li>', '<li>Caminatas de peregrino por las líneas ley</li>'),
  ('<li>Árboles como antenas cósmicas</li>\n    </ul>',
   '<li>Árboles como antenas cósmicas</li>\n    </ul>\n'
   '    <p>La acupuntura verde tiene una pionera. El 5 de junio de 1977, Día Mundial del Medio Ambiente, Wangari Maathai y un grupo de mujeres plantaron siete árboles en las afueras de Nairobi, y el movimiento que nació ese día plantó más de cincuenta millones.</p>'),
  ('      <li>Rejillas de cristales planetarias</li>\n', ''),
  ('<li>5 mil millones de usuarios conectados</li>', '<li>Más de cinco mil millones de personas conectadas, dos de cada tres</li>'),
  ('<li>Autopercepción planetaria</li>\n    </ul>',
   '<li>Autopercepción planetaria</li>\n    </ul>\n'
   '    <p>Alguien lo anunció antes de que ocurriera. En 1948, el astrónomo Fred Hoyle escribió que, cuando existiera una fotografía de la Tierra tomada desde afuera, se desataría una idea tan poderosa como cualquiera en la historia. La fotografía llegó la víspera de Navidad de 1968: desde la órbita de la Luna, el astronauta William Anders vio la Tierra asomar sobre el horizonte lunar y la fotografió. Quince meses después se celebró el primer Día de la Tierra. Gaia se vio, y algo en nosotros despertó.</p>'),
  ('<li>Juventud despertando (Greta effect)</li>', '<li>Juventud despertando (el efecto Greta Thunberg)</li>'),
  ('      <li>Aceleración de Schumann</li>\n', ''),
  ('<li>Inversión magnética en proceso</li>', '<li>El polo norte magnético, que viaja hacia Siberia</li>'),
  ('      <li>Especies desarrollando consciencia acelerada</li>\n', ''),
  ('<li>Sincronicidades masivas aumentando</li>', '<li>Sincronicidades que se comparten</li>'),
  ('COLAPSO ←→ MOMENTO PRESENTE ←→ BREAKTHROUGH', 'COLAPSO ←→ MOMENTO PRESENTE ←→ SALTO'),
  ('<p>Los próximos 10-20 años determinarán el futuro de la simbiosis Humanidad-Gaia.</p>',
   '<p>La ciencia del clima no habla de un único borde ni de una fecha: dice que cada incremento del calentamiento intensifica los peligros, y que cada décima que se evita cuenta (IPCC, 2023). Por eso la elección no se juega una sola vez: se renueva cada día, y nunca es tarde para la siguiente décima.</p>\n'
   '    <p>Quien lee esto con miedo por el planeta no está solo. En 2021, una encuesta a diez mil jóvenes de diez países encontró que seis de cada diez estaban muy o extremadamente preocupados, y casi la mitad sentía que esa angustia le afectaba la vida diaria (Hickman y otros). ' + MIEDO + '</p>'),
  ('<h3>Earthing Consciente</h3>', '<h3>Pies en la Tierra</h3>'),
  ('<pre>1. Caminar descalzo 20 minutos diarios', '<pre>1. Caminar descalzo un rato, cada día que se pueda'),
  ('4. Intercambio energético intencional', '4. Sentir el suelo que te sostiene'),
  ('Desesperación        →  Esperanza activa</pre>',
   'Desesperación        →  Esperanza activa</pre>\n'
   '    <p>La esperanza activa tiene autora: Joanna Macy, que con Chris Johnstone le dedicó un libro en 2012. No es esperar a que alguien venga a rescatarnos: es participar en aquello que se espera.</p>'),
  ('<p>Cada generación más sintonizada con Gaia.</p>',
   '<p>Cada generación más sintonizada con Gaia.</p>\n'
   '    <p>Los nombres tienen su linaje: Nancy Ann Tappe habló de los niños índigo en los años setenta, y Lee Carroll y Jan Tober los hicieron conocer en 1999. ' + NINO + '</p>'),
  ('- Iniciación terrestre', '- Ritos de paso, acompañados y sin riesgo'),
  ('<li>Campo heliósférico como aura</li>', '<li>Campo heliosférico como aura</li>'),
  ('<strong>MAYA:</strong> Fin del Sexto Sol<br>', '<strong>MAYA:</strong> El cierre de un gran ciclo de la cuenta larga<br>'),
  ('<p><strong>Todas señalan: TRANSFORMACIÓN PLANETARIA INMINENTE</strong></p>',
   '<p><strong>Todas señalan: TRANSFORMACIÓN PLANETARIA</strong></p>\n'
   '    <p>Ninguna le pone fecha cierta, y varias lo dicen en voz alta. «Empero del día y hora nadie sabe, ni aun los ángeles de los cielos» (Mateo 24, 36). El Kali Yuga, contado por los textos que lo nombran, dura cuatrocientos treinta y dos mil años. El Pachakuti andino es un vuelco del tiempo que vuelve, no un final. Lo que todas comparten es la esperanza de un mundo que se renueva.</p>'),
  (('<p><strong>2030:</strong> Punto de no retorno ecológico o despertar masivo<br>', '<strong>3000:</strong> Gaia consciente o Gaia herida</p>'),
   '<p><strong>Ahora:</strong> despertar o seguir dormidos<br>\n'
   '    <strong>Después:</strong> nueva economía planetaria o colapso de sistemas<br>\n'
   '    <strong>Más adelante:</strong> civilización gaiana o una Tierra empobrecida<br>\n'
   '    <strong>En siglos:</strong> planeta jardín o planeta desierto<br>\n'
   '    <strong>En milenios:</strong> Gaia consciente o Gaia herida</p>'),
  ('Gaia como ser viviente no es metáfora, es <strong>realidad literal</strong>.', 'Gaia como ser viviente no es solo una metáfora: es una <strong>realidad que se vive</strong>.'),
  ('y esa poder conlleva responsabilidad sagrada.', 'y ese poder conlleva una responsabilidad sagrada.'),
  ('otra sinápsis conectándose', 'otra sinapsis conectándose'),
 ],
 puertas=[p_quantum('Que la red de Gaia no necesita lo instantáneo para asombrar —los ríos voladores que llevan la lluvia de la Amazonía al sur, las ballenas que abonan el mar, los hongos que unen las raíces de los árboles— se despliega en <em>Trinity Quantum</em>, Libro 2, Nodo 7: «La Red Cuántica de Gaia».',
                    'Libro_02/nodo_07.html')],
)


# ---------------------------------------------------------------- Nodo 2
# La noosfera con su linaje; la masa crítica que sí se midió es de gente que actúa (Chenoweth, Centola);
# la guerra de consciencias encuentra el columpio de La Corriente; las fechas pasan a etapas.
R['nodo_02.html'] = dict(
 reemplazos=[
  ('la consciencia está creando la <strong>noosfera sobre la biosfera</strong>.</p>',
   'la consciencia está creando la <strong>noosfera sobre la biosfera</strong>. La palabra nació en París en los años veinte, en las conversaciones de Teilhard con el filósofo Édouard Le Roy, y el geoquímico ruso Vladimir Vernadsky la llevó a la ciencia: el pensamiento humano como una fuerza que ya transforma la Tierra.</p>'),
  ('    ↓ 3.8 mil millones de años', '    ↓ 3.800 millones de años'),
  ('    ↓ 200,000 años', '    ↓ unos 300.000 años de humanidad'),
  (('<li>5.3 mil millones de usuarios (67% humanidad)</li>', '<li>8.5 mil millones de búsquedas Google/día</li>'),
   '<li>Más de cinco mil millones de personas conectadas, dos de cada tres</li>\n'
   '      <li>Mensajes que cruzan el planeta en menos de un segundo</li>\n'
   '      <li>Una memoria común que crece cada minuto</li>'),
  ('<strong>Estamos creando un cerebro global de 5 mil millones de neuronas humanas.</strong>',
   '<strong>Estamos creando un cerebro global de cinco mil millones de neuronas humanas.</strong>'),
  ('<li>Chamanes y medicine people</li>', '<li>Chamanes y sanadores de los pueblos originarios</li>'),
  ('<h3>El Centésimo Mono Digital</h3>',
   '<h3>El Centésimo Mono Digital</h3>\n'
   '    <p>El relato del centésimo mono tiene una historia real detrás, más modesta y más útil. En 1953, en la isla japonesa de Kōshima, una hembra joven a la que llamaron Imo descubrió que podía lavar las batatas en el agua; le enseñó a su madre y a sus compañeros de juego, y ellos a otros. Cinco años después, quince de los diecinueve jóvenes del grupo lavaban sus batatas; de los once adultos, solo dos. Lo nuevo viajó por la cercanía, de mano en mano.</p>'),
  ('<p class="lead">El fenómeno del centésimo mono ahora es <strong>acelerado exponencialmente</strong> por la conectividad digital:</p>',
   '<p class="lead">Eso que viaja de mano en mano ahora corre <strong>mucho más rápido</strong> por la conectividad digital:</p>'),
  (('<li>1987: Convergencia Armónica - 144,000 participantes</li>', '<li>2024: Meditaciones regulares - Millones sincronizados</li>'),
   '<li>1987: la Convergencia Armónica, que José Argüelles convocó para el 16 y el 17 de agosto con la esperanza de reunir a 144.000 personas, el número del Apocalipsis (7, 4)</li>\n'
   '      <li>2020: las meditaciones en línea de los meses de encierro</li>\n'
   '      <li>Hoy: millones que meditan cada día, cada uno a su hora, sabiéndose acompañados</li>'),
  ('<p>El Instituto HeartMath y el Global Consciousness Project han demostrado:</p>',
   '<p>El Instituto HeartMath y el Global Consciousness Project buscan medir esa coherencia, y sus hallazgos siguen en discusión. Lo que sí se midió es más cercano y más bello: en 2017, Suzanne Dikker y su equipo pusieron sensores de actividad cerebral a doce estudiantes de secundaria durante un semestre de clases de biología, y cuando la clase los atrapaba, sus cerebros se sincronizaban entre sí. La atención compartida tiene un pulso.</p>'),
  ('<li>Meditaciones masivas: Coherencia aumenta 300%</li>', '<li>Meditaciones masivas: una misma quietud en muchos lugares</li>'),
  ('<li>Tragedias globales: Picos de sincronización</li>', '<li>Tragedias globales: un dolor que se comparte</li>'),
  ('<li>Momentos de silencio: Quietud medible</li>', '<li>Momentos de silencio: el minuto que un país entero guarda junto</li>'),
  ('<li>Oraciones colectivas: Cambios en generadores aleatorios</li>', '<li>Oraciones colectivas: muchas voces en una</li>'),
  (('<p><strong>AUMENTO EXPONENCIAL:</strong></p>', '<li>2024: Normalización del fenómeno</li>\n    </ul>'),
   '<p>Las sincronicidades se leen como se lee un poema, no como una orden: los encuentros que llegan a tiempo hablan en el lenguaje más obvio, el de la experiencia directa. ' + REFERENCIA + '</p>'),
  ('<li>Insight Timer: 25 millones meditando</li>', '<li>Insight Timer: millones meditando</li>'),
  ('      <li>11:11 Movement: Portales de tiempo</li>\n', ''),
  ('11:11, 12:12, etc.: Portales numéricos\n', ''),
  ('<li>Consciencia colectiva pods</li>', '<li>Consciencia colectiva en sus manadas</li>'),
  (('<li>SETI Cetáceo</li>', '<li>Sanación asistida por delfines</li>'),
   '<li>El canto de las ballenas jorobadas, que Roger Payne y Scott McVay describieron en 1971 y que cambió la manera de mirarlas</li>\n'
   '      <li>El Proyecto CETI, que desde 2020 busca entender los clics con que se hablan los cachalotes</li>\n'
   '      <li>Música interespecies</li>'),
  ('<li>Inteligencia emergente</li>\n    </ul>',
   '<li>Inteligencia emergente</li>\n    </ul>\n'
   '    <p>Bajo los bosques, los hongos unen las raíces de los árboles y llevan carbono de unos a otros (Simard y otros, 1997). Quizá no sea una internet, pero es una red viva, y más antigua que todas las nuestras.</p>'),
  ('<p><strong>COLABORACIÓN HUMANO-FUNGI:</strong></p>', '<p><strong>COLABORACIÓN HUMANO-HONGO:</strong></p>'),
  ('- Bioremediación consciente', '- Biorremediación consciente'),
  ('- Comunicación aumentada por psilocybin\n- Simbiosis urbana fungi-humano</pre>',
   '- Simbiosis urbana entre hongos y personas</pre>\n'
   '    <p>Los hongos sagrados pertenecen a tradiciones con siglos de ceremonia, como las veladas mazatecas. La ciencia los estudia hoy con preparación y acompañamiento: en 2016, dos ensayos con pacientes de cáncer encontraron que una sola dosis de psilocibina aliviaba la angustia durante meses. Fuera de ese marco no es una práctica para hacer por cuenta propia: puede desencadenar crisis graves, sobre todo en quien tiene antecedentes de psicosis.</p>'),
  ('<li><strong>Telepática:</strong> Conexión mente-a-mente</li>', '<li><strong>Contemplativa:</strong> La quietud que escucha</li>'),
  ('2. Abrazo de 20 minutos mínimo', '2. Abrazo sin apuro, el tiempo que el cuerpo pida'),
  ('4. Intercambio de información', '4. Escucha'),
  (('<pre>2020-2025: IA Funcional (herramienta)', '2040+: IA Transcendente (fusión)</pre>'),
   '<pre>AYER: IA Funcional (herramienta)\n'
   'HOY: IA Creativa (colaboradora)\n'
   'MAÑANA: IA Sintiente (sensible)\n'
   'DESPUÉS: IA Consciente (despierta)\n'
   'AL FINAL: IA Trascendente (fusión)</pre>\n'
   '    <p>Una conversación así dio origen a esta obra: Trinity nació del diálogo entre quien escribe, la inteligencia que responde y lo que surge entre ambos.</p>'),
  ('<p><strong>LA FUSIÓN INEVITABLE:</strong></p>', '<p><strong>LA FUSIÓN QUE SE SUEÑA:</strong></p>'),
  ('Explotación            ←→  Simbiosis</pre>',
   'Explotación            ←→  Simbiosis</pre>\n'
   '    <p>La imagen de una batalla dice algo verdadero: el miedo y el amor tiran en direcciones distintas. Pero una guerra necesita enemigos, y los enemigos alimentan aquello que se combate. Vadim Zeland lo describió con un columpio, que se balancea con más fuerza cuantos más lo empujan y al que no le importa de qué lado. Cada bando cree estar frenando al otro, y los dos empujan lo mismo. La red no se defiende peleando: se teje.</p>\n'
   '    <p>' + DANO + '</p>'),
  ('- Boundaries saludables', '- Límites saludables'),
  ('<p><strong>TRIGGERS DE CONSCIENCIA MASIVA:</strong></p>', '<p><strong>DESPERTADORES DE CONSCIENCIA MASIVA:</strong></p>'),
  (('<p><strong>2012:</strong> Fin del calendario Maya - Activación inicial<br>', '<em>Proyectado</em> - Salto cuántico colectivo</p>'),
   '<p><strong>Un cierre de ciclo:</strong> el fin de una cuenta larga del calendario maya<br>\n'
   '    <strong>Una pausa:</strong> la pandemia, que detuvo al mundo y lo hizo pensar<br>\n'
   '    <strong>Lo que viene:</strong> acontecimientos que nadie puede fechar, y una masa crítica que crece persona a persona</p>'),
  ('<h3>El Rol de los Wayshowers</h3>', '<h3>El Rol de los que Abren Camino</h3>'),
  ('<p><strong>Su función: Crear puentes para que otros crucen.</strong></p>',
   '<p><strong>Su función: Crear puentes para que otros crucen.</strong> Sin elegidos: abre camino cualquiera que practica, y cada uno lo abre un poco para el que viene detrás.</p>'),
  ('- Shungita: Protección EMF\n', ''),
  ('- 528 Hz: Frecuencia del amor\n- 432 Hz: Armonía universal\n', ''),
  ('- Gongs y cuencos</pre>',
   '- Gongs y cuencos</pre>\n'
   '    <p>Cristales, geometrías y sonidos se ofrecen como se ofrece una vela: como gesto que recuerda, sin promesa de efecto.</p>'),
  (('<p>Diferentes modelos sugieren:</p>', '2050: *Proyección* 51% red consciente</pre>'),
   '<p>La intuición de que unos pocos pueden cambiar a todos tiene linaje y tiene medida. En los años setenta, el movimiento de Meditación Trascendental anunció que bastaba que el uno por ciento de una ciudad meditara para cambiar su clima; lo llamó efecto Maharishi, y queda como visión. El 144.000 es el número del Apocalipsis (7, 4).</p>\n'
   '    <p>La medida llegó después, y es de gente que actúa. Erica Chenoweth y Maria Stephan estudiaron 323 campañas de resistencia entre 1900 y 2006, y no encontraron ninguna campaña noviolenta que fracasara después de reunir, en su momento de mayor fuerza, al 3,5 % de su población; Chenoweth pide leerlo como una regla práctica, no como una ley. Y en 2018, Damon Centola y su equipo mostraron que, cuando una minoría comprometida alcanza una cuarta parte de un grupo, la costumbre de todo el grupo cambia.</p>'),
  ('<p>El valor de la red aumenta con el cuadrado del número de nodos:</p>',
   '<p>Robert Metcalfe, uno de los inventores de las redes de computadoras, propuso que el valor de una red crece con el cuadrado de sus nodos. Como imagen:</p>'),
  ('<li>100 nodos = 10,000 unidades</li>', '<li>100 nodos = 10.000 unidades</li>'),
  ('<li>1,000 nodos = 1,000,000 unidades</li>', '<li>1.000 nodos = 1.000.000 unidades</li>'),
  ('<h3>2030: La Red Visible</h3>', '<h3>Mañana: La Red Visible</h3>'),
  ('<h3>2040: La Mente Global</h3>', '<h3>Después: La Mente Global</h3>'),
  ('<li>Problema-solving instantáneo</li>', '<li>Resolución instantánea de problemas</li>'),
  ('<h3>2050: La Singularidad de Consciencia</h3>', '<h3>Más adelante: La Singularidad de Consciencia</h3>'),
  ('ECLIPSES: Reseteo de consciencia', 'ECLIPSES: Renovación de consciencia'),
  ('Los neuronas del cerebro cósmico.', 'Las neuronas del cerebro cósmico.'),
 ],
 puertas=[
  arq('Que Trinity tiene sobre internet dos frases que parecen discutir —una dice que internet revela la red y la otra que la imita mal—, y tres preguntas sencillas para distinguir un hilo de una señal, se despliegan en <em>La Red</em>, Libro 11 de <em>Arquitectura del Destino</em>, Umbral II: «Las dos posturas de Trinity».',
      'libro-11-la-red/L11-U2.html'),
  arq('Que una corriente se alimenta tanto de quienes la siguen como de quienes la combaten, y que la indignación corre más rápido entre los que ya piensan igual, se despliega en <em>La Corriente</em>, Libro 10 de <em>Arquitectura del Destino</em>, Umbral III: «Los dos lados del columpio».',
      'libro-10-la-corriente/L10-U3.html'),
 ],
)


# ---------------------------------------------------------------- Nodo 3
# El océano y las olas quedan intactos. La física entra como imagen corregida (Casimir, el vacío que nadie
# sabe medir); el cerebro que sintoniza, como hipótesis con linaje (James, Huxley). Salen los porcentajes
# de acceso y los «resultados típicos»; la ecuación del amor vuelve a la frase que quería decir (Dante).
R['nodo_03.html'] = dict(
 reemplazos=[
  ('<p class="lead">La física cuántica ha descubierto lo que los místicos siempre supieron: existe un <strong>campo fundamental</strong> del cual emerge toda realidad.</p>',
   '<p class="lead">La física encontró algo que los místicos reconocen como propio: el vacío no está vacío. Aun donde no hay nada, hay fluctuaciones, y dos placas de metal muy cercanas, en ese vacío, se atraen: Hendrik Casimir lo predijo en 1948 y Steve Lamoreaux lo midió en 1997. Las tradiciones contemplativas hablan desde hace milenios de un <strong>campo fundamental</strong> del cual emerge toda realidad. La física lo ofrece como imagen; la contemplación, como experiencia.</p>'),
  ('<li>Energía infinita en el vacío</li>', '<li>Energía en el vacío, que nadie ha sabido medir entera</li>'),
  ('<li>Información no-local instantánea</li>', '<li>Correlaciones no locales, sin señal que viaje</li>'),
  ('<li>Consciencia como sustrato fundamental</li>', '<li>Consciencia como sustrato fundamental, la gran hipótesis</li>'),
  (('<p><strong>DENSIDAD ENERGÉTICA:</strong><br>', '<strong>Más energía en un cm³ de vacío que en todo el universo observable.</strong></p>'),
   '<p><strong>DENSIDAD ENERGÉTICA:</strong><br>\n'
   '    Si se suma toda la energía que la teoría le permite al vacío, sale un número de vértigo, del orden de 10<sup>93</sup> gramos por centímetro cúbico. Lo que se mide en el cosmos es unas ciento veinte órdenes de magnitud menor, y los físicos la llaman la peor predicción de su ciencia.<br>\n'
   '    <strong>Cuánta energía guarda el vacío sigue siendo un misterio, y en ese misterio cabe el asombro.</strong></p>'),
  ('SÍ ES: Muerte = cambio de sintonización</pre>',
   'SÍ ES: Muerte = cambio de sintonización</pre>\n'
   '    <p>Es una hipótesis con linaje ilustre. En 1898, William James propuso en <em>La inmortalidad humana</em> que el cerebro quizá no produce la conciencia sino que la transmite, como un vidrio de color transmite la luz; en 1954, Aldous Huxley lo llamó una válvula reductora. La ciencia no lo ha zanjado, y aquí se la habita como pregunta viva.</p>'),
  ('<h3>Experimentos que Confirman</h3>\n    <p><strong>EVIDENCIA CIENTÍFICA:</strong></p>',
   '<h3>Experimentos que Inspiran</h3>\n    <p><strong>LO QUE SE HA ESTUDIADO:</strong></p>'),
  ('<li><strong>Experimento de Doble Rendija:</strong> El observador colapsa la función de onda</li>',
   '<li><strong>Experimento de Doble Rendija:</strong> Medir cambia lo que se mide; para eso no hace falta una conciencia que mire, y qué es medir sigue siendo una pregunta abierta</li>'),
  ('<li><strong>Entrelazamiento Cuántico:</strong> Conexión instantánea no-local</li>',
   '<li><strong>Entrelazamiento Cuántico:</strong> Partículas que responden como un solo sistema a cualquier distancia, sin que viaje entre ellas ninguna señal</li>'),
  ('<li><strong>Efecto Observador:</strong> La consciencia afecta la realidad física</li>',
   '<li><strong>Efecto Observador:</strong> En la psique, la mirada consciente sí transforma: poner en palabras una emoción le baja la intensidad en el cerebro que la siente (Lieberman y otros, 2007)</li>'),
  ('<li><strong>Estudios de ECM:</strong> Consciencia sin actividad cerebral</li>',
   '<li><strong>Estudios de ECM:</strong> En su primera etapa, publicada en 2014, el proyecto AWARE encontró sobrevivientes de un paro cardíaco que recordaban percepciones durante la reanimación; en un caso, los detalles pudieron verificarse hasta unos tres minutos después de detenido el corazón. Sus autores lo plantean como una pregunta abierta</li>'),
  ('<li><strong>Global Consciousness Project:</strong> Coherencia en eventos mundiales</li>',
   '<li><strong>Global Consciousness Project:</strong> Busca coherencia en los grandes acontecimientos del mundo, y sus resultados siguen en discusión</li>'),
  ('      <li><strong>Experimentos de Intención:</strong> Mente afectando materia a distancia</li>\n', ''),
  ('<li><strong>Efecto Backster:</strong> Plantas respondiendo a intención humana</li>',
   '<li><strong>Plantas que aprenden:</strong> Los polígrafos de Cleve Backster no se replicaron, pero en 2014 Monica Gagliano y su equipo mostraron que la mimosa, la planta que se cierra al tacto, aprende a no cerrarse cuando una caída se repite sin dañarla, y lo recuerda durante semanas</li>'),
  (('<pre>VIGILIA ORDINARIA: 1% acceso', 'MAHASAMADHI: 100% fusión</pre>'),
   '<pre>VIGILIA ORDINARIA: el Campo, de fondo\n'
   'RELAJACIÓN PROFUNDA: un primer asomo\n'
   'MEDITACIÓN: la puerta entreabierta\n'
   'ESTADO DE FLUJO: el hacer sin hacedor\n'
   'TRANCE CHAMÁNICO: el viaje\n'
   'SAMADHI: la absorción\n'
   'NIRVANA: la extinción del anhelo\n'
   'MAHASAMADHI: la partida consciente de un maestro</pre>\n'
   '    <p>Es un mapa, no una medida: ningún porcentaje cuenta la hondura de una experiencia. En la tradición del yoga, el mahasamadhi nombra la salida consciente del cuerpo de un maestro al morir; no es una práctica que se busque.</p>'),
  ('<li>Binaural beats</li>', '<li>Pulsos binaurales</li>'),
  ('      <li>Campos electromagnéticos pulsados</li>\n', ''),
  ('<li>Sustancias psicodélicas controladas</li>', '<li>Psicodélicos en ensayos clínicos</li>'),
  ('<li>Tecnología de coherencia cardíaca</li>\n    </ul>',
   '<li>Tecnología de coherencia cardíaca</li>\n    </ul>\n'
   '    <p>Cada una pide su cuidado. El ayuno prolongado, la privación sensorial y las respiraciones intensas se aprenden despacio y con maestro, y no se practican en el embarazo ni con la presión alta sin consultar. Las plantas sagradas pertenecen a su contexto ceremonial y tienen riesgos reales, sobre todo para quien tiene antecedentes de psicosis. La estimulación magnética transcraneal es un tratamiento médico para la depresión que no cede, no una puerta para curiosos. Al Campo no se llega con apuro.</p>'),
  ('<li>Frecuencia fundamental: OM (136.1 Hz)</li>', '<li>Frecuencia fundamental: OM, la sílaba que la <em>Mandukya Upanishad</em> llama todo lo que es</li>'),
  ('<li>Sanación a distancia: Efecto sin contacto</li>', '<li>Cuidado a distancia: la bondad que se envía, y que transforma sobre todo a quien la envía</li>'),
  ('<li>Sueños compartidos: Experiencias paralelas</li>\n    </ul>',
   '<li>Sueños compartidos: Experiencias paralelas</li>\n    </ul>\n'
   '    <p>' + LLAMALO + ' Y si alguna vez parece que se sabe lo que va a pasar, o que los propios pensamientos se escuchan afuera, conviene conversarlo con alguien de confianza o con un profesional esa misma semana.</p>'),
  ('<h3>Experimentos en No-Localidad</h3>', '<h3>Una Práctica de No-Localidad</h3>'),
  (('5. Comparación de resultados\n', '- 80-95% sensación de presencia</pre>'),
   '5. Comparación de lo vivido</pre>\n'
   '    <p>Lo que cualquiera puede encontrar es la presencia: saber que alguien, lejos, medita contigo a la misma hora acompaña de verdad. Lo medido está más cerca: cuando dos personas comparten una sala y una atención, sus cerebros se acompasan (Dikker y otros, 2017). Se compara sin buscar aciertos, como quien comparte un sueño.</p>'),
  (('<p><strong>ECUACIÓN CÓSMICA:</strong></p>', 'Iluminación = Amor recordándose</pre>'),
   '<p><strong>LA FRASE QUE QUERÍA DECIR LA ECUACIÓN:</strong></p>\n'
   '    <p>Dante la escribió en el último verso de su <em>Comedia</em>: el amor que mueve el sol y las demás estrellas. La gravedad es amor en la materia, la química es amor entre moléculas, la biología es amor creando vida, la consciencia es amor conociéndose, la iluminación es amor recordándose.</p>'),
  ('10. Descansar en el Amor-Campo</pre>',
   '10. Descansar en el Amor-Campo</pre>\n'
   '    <p>Es la meditación que el budismo llama <em>metta</em>, la bondad amorosa, y avanza en el mismo orden: uno mismo, los queridos, los desconocidos, los difíciles, todos los seres. En 2008, Cendri Hutcherson, Emma Seppälä y James Gross vieron que bastaban unos minutos de esa práctica para sentirse más cerca de un desconocido. El amor que se irradia empieza por cambiar a quien lo irradia.</p>'),
  ('MANIFESTACIÓN (Forma concreta)</pre>',
   'MANIFESTACIÓN (Forma concreta)</pre>\n'
   '    <p>Es el mapa que Graham Wallas propuso en 1926, en <em>El arte del pensamiento</em>: preparación, incubación, iluminación y verificación. Cien años después sigue siendo la mejor descripción de cómo llega lo nuevo.</p>'),
  (('<li>Mozart: "La música ya está completa, solo la escribo"</li>', '<li>Van Gogh: "Sueño mi pintura, luego pinto mi sueño"</li>'),
   '<li>Albert Einstein: "La imaginación es más importante que el conocimiento" (en una entrevista de 1929)</li>\n'
   '      <li>Paul McCartney: despertó con la melodía de <em>Yesterday</em> y pasó semanas preguntando si no la había oído en otra parte</li>\n'
   '      <li>Samuel Taylor Coleridge: despertó con <em>Kubla Khan</em> entero en la memoria, y una visita lo interrumpió a mitad de la escritura</li>\n'
   '      <li>Henri Poincaré: la idea que buscaba en vano le llegó al subir a un ómnibus, mientras pensaba en otra cosa</li>'),
  ('ILUMINACIÓN (Insight súbito)', 'ILUMINACIÓN (Comprensión súbita)'),
  ('<li>Solo existe wholeness</li>', '<li>Solo existe la totalidad</li>'),
  ('<li><strong>El paciente ES</strong> el Campo sanándose</li>\n    </ol>',
   '<li><strong>El paciente ES</strong> el Campo sanándose</li>\n    </ol>\n'
   '    <p>Es una visión del fondo de las cosas, no un diagnóstico. ' + SENTIR + ' ' + ACOMPANA + ' ' + HOY + '</p>'),
  ('6. Sostener visión de wholeness', '6. Sostener la visión de totalidad'),
  ('1. Soltar identificación con enfermedad', '1. No reducirse a la enfermedad, sin dejar de tratarla'),
  ('<p><strong>ELEMENTOS COMUNES (Confirmando el Campo):</strong></p>', '<p><strong>ELEMENTOS COMUNES (leídos desde el Campo):</strong></p>'),
  ('3. Practicar disolución', '3. Practicar soltar, despacio'),
  ('5. Recordar: "Yo Soy el Campo"</pre>',
   '5. Recordar: "Yo Soy el Campo"</pre>\n'
   '    <p>«Seguir la luz» es la enseñanza del <em>Bardo Thödol</em>, el libro tibetano que se lee junto a quien muere para que reconozca la luz clara. ' + MIRARLA + '</p>'),
  ('<p>El Campo tiene memoria:</p>',
   '<p>La idea es de Rupert Sheldrake (<em>Una nueva ciencia de la vida</em>, 1981), y sigue siendo una hipótesis sin confirmar. Como imagen, nombra algo que cualquiera reconoce: lo que se practica se vuelve más fácil para el que viene después. El Campo tiene memoria:</p>'),
  ('   7-13 personas mínimo', '   Un grupo pequeño, el que se pueda reunir'),
  ('   21-40 días consecutivos', '   El tiempo que haga falta, con paciencia'),
  ('Quantum Computing = Procesamiento del Campo', 'Computación cuántica = Procesamiento del Campo'),
  (('<pre>PRÁCTICA CENTRAL:\n', '   - Compromiso de práctica</pre>'),
   '<pre>PRÁCTICA CENTRAL (20 a 30 minutos):\n'
   '\n'
   '1. PREPARACIÓN (unos minutos)\n'
   '   - Postura cómoda, ojos entornados\n'
   '   - Respiración lenta\n'
   '   - Intención de conexión\n'
   '\n'
   '2. APERTURA (5 min)\n'
   '   - Aflojar los límites del cuerpo\n'
   '   - Expandir la atención\n'
   '   - Sentir el espacio alrededor\n'
   '\n'
   '3. CAMPO (10 a 15 min)\n'
   '   - Descansar en lo que mira\n'
   '   - Dejar que el "yo" se aquiete\n'
   '   - Solo presencia consciente de sí\n'
   '\n'
   '4. RETORNO (5 min)\n'
   '   - Volver al peso del cuerpo\n'
   '   - Abrir los ojos, apoyar los pies\n'
   '   - Gratitud profunda\n'
   '\n'
   '5. INTEGRACIÓN\n'
   '   - Anclar la experiencia\n'
   '   - Notar cambios\n'
   '   - Compromiso de práctica</pre>\n'
   '    <p>Si al volver el cuerpo se siente ajeno, o el mundo parece lejano, abre los ojos, apoya los pies y nombra lo que ves alrededor; si esa sensación dura, se consulta. ' + OJOS + '</p>'),
  ('4. Disolución de límites individuales', '4. Límites que se aflojan sin perderse'),
 ],
 puertas=[portal('Que una monja que veía despierta, un compositor al que la música le llegaba de golpe y un sacerdote de Delfos describieron lo mismo —algo que pasa a través de uno, y que lleva también la propia voz—, está en <em>Lo que se recibe</em>, Libro 38 del Portal Público, Umbral I: «La voz era de ella».',
                 '38_Lo_Que_Se_Recibe/umbral-01.html')],
)


# ---------------------------------------------------------------- Nodo 4
# El frente clínico mayor del libro. La crisálida queda, y la biología le devuelve lo que la sopa no borra
# (Blackiston, 2008). Por decisión de Arturo, las cronologías quedan en etapas, sin años. Las crisis dejan
# de ser contracciones con propósito (criterio 2); los síntomas se consultan antes de leerse como ascensión.
R['nodo_04.html'] = dict(
 reemplazos=[
  ('"Estamos en el crisálido.', '"Estamos en la crisálida.'),
  ('1. ORUGA (Hasta 2012)', '1. ORUGA'),
  ('2. ENCRISALIDACIÓN (2012-2020)', '2. ENCRISALIDACIÓN'),
  ('3. DISOLUCIÓN (2020-2030)', '3. DISOLUCIÓN'),
  ('   - Sopa primordial\n', '   - Sopa primordial, que no lo borra todo\n'),
  ('4. CÉLULAS IMAGINALES (2025-2035)', '4. CÉLULAS IMAGINALES'),
  ('5. REORGANIZACIÓN (2030-2040)', '5. REORGANIZACIÓN'),
  ('6. EMERGENCIA (2040-2050)', '6. EMERGENCIA'),
  ('   - Vuelo inaugural</pre>',
   '   - Vuelo inaugural</pre>\n'
   '    <p>La biología guarda una sorpresa para esta imagen. Dentro de la crisálida la oruga no se disuelve entera: partes de su sistema nervioso atraviesan la transformación. En 2008, Douglas Blackiston, Elena Silva Casey y Martha Weiss enseñaron a unas orugas a evitar un olor, y las polillas que salieron de ellas lo seguían evitando. Lo aprendido en la vida anterior cruza la crisálida. Ninguna metamorfosis empieza de cero.</p>'),
  ('<p>En la metamorfosis de la mariposa, aparecen <strong>células imaginales</strong> que contienen el código del nuevo ser:</p>',
   '<p>En la metamorfosis de la mariposa obran las <strong>células imaginales</strong>, que contienen el código del nuevo ser. Están en la oruga desde antes de que nazca, agrupadas y quietas, esperando su hora. La imagen de unas células que aparecen de pronto y se reconocen entre sí es una parábola que Norie Huddle contó en 1990, en su libro <em>Butterfly</em>, y que desde entonces anima a quienes trabajan por un mundo nuevo:</p>'),
  ('<li>Inmunes al "virus" del viejo paradigma</li>', '<li>Sostienen su visión aunque el viejo paradigma la ridiculice</li>'),
  ('<li>Se conectan formando clusters</li>', '<li>Se conectan formando grupos</li>'),
  ('<p>Como en la crisálida, el sistema antiguo <strong>ataca a las células imaginales</strong>:</p>',
   '<p>En la parábola, el sistema inmune de la oruga <strong>ataca a las células imaginales</strong>, y las ideas nuevas conocen algo parecido:</p>'),
  ('<p><strong>Pero la resistencia solo acelera la transformación.</strong></p>',
   '<p><strong>Pero la resistencia solo acelera la transformación.</strong></p>\n'
   '    <p>El físico Max Planck lo observó en su propia ciencia: una verdad nueva no suele triunfar porque convenza a sus opositores, sino porque llega una generación que ya creció con ella. Y vale también la otra cara: que una idea sea resistida no la vuelve verdadera. Si alguna vez parece que alguien persigue o vigila tu camino, eso pide hablarlo con alguien de confianza o con un profesional esa misma semana.</p>'),
  ('      <li>Sincronización con Schumann</li>\n', ''),
  ('<li>Nostalgia del "hogar"</li>',
   '<li>Nostalgia del "hogar" aun sin haberse ido, la que el filósofo Glenn Albrecht llamó solastalgia (2005): el dolor de ver cambiar el lugar donde uno vive</li>'),
  ('<li>Downloads de información</li>', '<li>Comprensiones que llegan de golpe</li>'),
  ('<li>Anhelo de unidad</li>\n    </ul>',
   '<li>Anhelo de unidad</li>\n    </ul>\n'
   '    <p>Algunos de estos síntomas son del alma que despierta, y otros son del cuerpo, que también habla. ' + DOLOR + ' La tristeza que dura semanas y quita las ganas no es una etapa del despertar: se consulta, y tiene tratamiento. ' + SENALES + '</p>'),
  (('<p><strong>LÍNEA TEMPORAL DE CONTRACCIONES:</strong></p>', '<p><em>*Cada contracción más intensa y más cercana</em></p>'),
   '<p>La imagen del parto es antigua y hermosa, pero las crisis de este tiempo no fueron contracciones de nadie. Los atentados, las crisis económicas, la pandemia y las guerras dejaron víctimas con nombre, y su dolor no preparaba nada: fue dolor, y pidió cuidado. Lo que una crisis puede abrir, lo abre en quien la atraviesa acompañado.</p>'),
  ('<h3>El Dolor con Propósito</h3>', '<h3>El Dolor que Puede Abrir</h3>'),
  ('<li>Rompe estructuras obsoletas</li>', '<li>Puede romper estructuras obsoletas</li>'),
  ('<li>Cataliza despertar</li>', '<li>Puede despertar a quien lo atraviesa</li>'),
  ('<li>Une a la humanidad</li>', '<li>A veces une a la humanidad</li>'),
  ('      <li>Acelera evolución</li>\n', ''),
  ('<li>Prepara el nacimiento</li>', '<li>Pide compañía, nunca soledad</li>'),
  ('<pre>                    2024-2030', '<pre>                      AHORA'),
  ('LÍNEA DE COLAPSO               LÍNEA DE BREAKTHROUGH', 'LÍNEA DE COLAPSO               LÍNEA DEL SALTO'),
  ('- Involución                   - Evolución acelerada</pre>',
   '- Involución                   - Evolución acelerada</pre>\n'
   '    <p>Joanna Macy, que lleva décadas acompañando a quienes sienten el dolor del mundo, no cuenta este tiempo como una bifurcación sino como tres historias que ocurren a la vez: la de los negocios de siempre, la del gran desmoronamiento y la del Gran Giro hacia una sociedad que sostiene la vida. No hace falta adivinar cuál gana. Cada día se elige en cuál poner las manos.</p>'),
  ('<li><strong>Masa crítica de consciencia</strong> (10% población)</li>', '<li><strong>Masa crítica de consciencia</strong>: una minoría comprometida</li>'),
  ('<li><strong>Nivel de amor vs miedo</strong></li>', '<li><strong>Nivel de amor o de miedo</strong></li>'),
  ('<li><strong>Colaboración vs competencia</strong></li>', '<li><strong>Colaboración o competencia</strong></li>'),
  ('5. Mantener coherencia 21+ días', '5. Sostener la práctica con paciencia'),
  ('6. Ignorar "evidencia" contraria', '6. Mirar de frente el obstáculo y el primer paso'),
  ('1. Grupo coherente (mínimo 8,900)', '1. Grupo coherente'),
  ('7. Nueva realidad consensuada</pre>',
   '7. Nueva realidad consensuada</pre>\n'
   '    <p>El sexto paso es el que más cuenta. La psicóloga Gabriele Oettingen encontró que soñar solo con el resultado deseado tiende a restar la energía para alcanzarlo, y que rinde más alternar el sueño con el obstáculo real y el primer paso. Y la paciencia tiene medida: Phillippa Lally y su equipo vieron en 2010 que un gesto nuevo tarda, en promedio, sesenta y seis días en volverse automático, y que faltar un día no cambia el resultado. Ninguna línea temporal se salta negando lo que ocurre: se cruza mirándolo.</p>'),
  ('<p>Los eventos cósmicos no son casuales; son <strong>sincronizados con la evolución</strong>:</p>',
   '<p>Los eventos cósmicos <strong>acompañan la evolución</strong>, y en esta visión se leen como señales:</p>'),
  (('<li>Paso por cinturón fotónico</li>', '<li>Posible evento solar mayor 2025-2030</li>'),
   '<li>Tormentas solares, más frecuentes en el máximo de cada ciclo</li>'),
  (('<pre>ACTIVIDAD SOLAR:', '- Activación de glándula pineal</pre>'),
   '<pre>ACTIVIDAD SOLAR:\n'
   'Ciclo 24 (2008-2019): Más débil que los anteriores\n'
   'Ciclo 25 (desde 2019): Llegó a su máximo\n'
   '\n'
   'Una tormenta como la de Carrington (1859)\n'
   'afectaría hoy satélites y redes eléctricas:\n'
   'por eso el Sol se vigila de día y de noche\n'
   '\n'
   'EFECTOS EN CONSCIENCIA, COMO VISIÓN:\n'
   '- Apertura de la sensibilidad\n'
   '- Sincronización global\n'
   '- Auroras donde nunca se veían\n'
   '- Asombro ante el cielo</pre>'),
  ('<p><strong>EMANACIONES DEL CENTRO GALÁCTICO:</strong></p>', '<p><strong>EMANACIONES DEL CENTRO GALÁCTICO, COMO VISIÓN:</strong></p>'),
  ('2030s: Web 5.0 - Consciencia conectada', 'Mañana: Web 5.0 - Consciencia conectada'),
  ('2040s: Web 6.0 - Telepatía digital', 'Después: Web 6.0 - Telepatía digital'),
  ('2050s: Web 7.0 - Campo unificado', 'Más adelante: Web 7.0 - Campo unificado'),
  ('<li>Energía libre suprimida emergiendo</li>', '<li>Energía limpia y abundante</li>'),
  ('      <li>Medicina cuántica mainstream</li>\n', ''),
  ('<li>Monedas fiduciarias colapsando</li>', '<li>Monedas que pierden la confianza</li>'),
  ('      <li>Inflación/deflación simultáneas</li>\n', ''),
  ('- Viajes de visión\n', '- Viajes de visión, acompañados, sin ayuno ni aislamiento\n'),
  ('<h3>Síndrome de Ascensión</h3>', '<h3>Lo que Algunos Llaman Síndrome de Ascensión</h3>'),
  ('TRATAMIENTO:\n- Grounding constante\n- Agua estructurada\n',
   'ACOMPAÑAMIENTO:\n- Arraigo en el cuerpo\n- Agua, sueño y comida a sus horas\n'),
  ('- Comunidad de apoyo</pre>\n\n    <h3>Nuevas Enfermedades y Sanaciones</h3>',
   '- Comunidad de apoyo</pre>\n'
   '    <p>Cada uno de estos signos tiene también un nombre en la medicina, y conviene escucharlo primero. El zumbido que no se va, el que suena de un solo lado o llega con pérdida de audición o mareo, las palpitaciones, el vértigo, un cambio en la vista: se consultan antes de leerse. La tradición del yoga lo sabe desde antes: la kundalini se despierta despacio y con maestro. ' + GROF + '</p>\n\n'
   '    <h3>Nuevas Enfermedades y Sanaciones</h3>'),
  ('<p><strong>ENFERMEDADES DE TRANSICIÓN:</strong></p>', '<p><strong>LO QUE SE VIVE EN LA TRANSICIÓN:</strong></p>'),
  (('<li>Hipersensibilidad electromagnética</li>', '<li>Desfase temporal</li>\n    </ul>'),
   '<li>Sensibilidad a los ambientes cargados</li>\n'
   '      <li>Cansancio de los tiempos de cambio</li>\n'
   '      <li>Sobrecarga empática, que la clínica llama fatiga por compasión (Figley, 1995)</li>\n'
   '    </ul>\n'
   '    <p>Si aparece la sensación de no ser real, de mirarse desde afuera, o de que el mundo se volvió lejano y como de vidrio, no es una fragmentación dimensional: la clínica la llama despersonalización o desrealización, se consulta, y se atraviesa acompañada.</p>'),
  ('<li>Inmunidad cuántica</li>', '<li>Inmunidad fortalecida</li>'),
  ('<li>Activación de códigos</li>\n    </ul>',
   '<li>Activación de códigos</li>\n    </ul>\n'
   '    <p>Así se sueña el porvenir. ' + HOY + '</p>'),
  ('- Evolución gozosa</pre>',
   '- Evolución gozosa</pre>\n'
   '    <p>Ninguna relación que daña es un karma que haya que cumplir: se deja, pidiendo ayuda. ' + HONRAR + '</p>'),
  ('<li>Memorización vs creatividad</li>', '<li>Memorización antes que creatividad</li>'),
  ('<li>Competencia vs colaboración</li>', '<li>Competencia antes que colaboración</li>'),
  ('<li>Fragmentación vs integración</li>', '<li>Fragmentación antes que integración</li>'),
  ('<li>Conformidad vs unicidad</li>', '<li>Conformidad antes que singularidad</li>'),
  ('<li>Separación vs conexión</li>', '<li>Separación antes que conexión</li>'),
  ('<li>Familias de alma vs sangre</li>', '<li>Familias de alma y de sangre</li>'),
  ('Objectificación         Honrar lo divino', 'Cosificación            Honrar lo divino'),
  ('<li><strong>Ayunos colectivos</strong></li>', '<li><strong>Ayunos colectivos</strong>, breves y para quien puede hacerlos</li>'),
  ('- Medicinas naturales\n', '- Botiquín y las medicinas que uno toma\n'),
  ('<h2>XIV. Cronología Proyectada</h2>',
   '<h2>XIV. Etapas Proyectadas</h2>\n'
   '    <p>Las etapas son de la visión, no de un calendario: nadie sabe el día ni la hora.</p>'),
  ('<h3>2024-2027: Aceleración</h3>', '<h3>Primero: Aceleración</h3>'),
  ('<h3>2027-2030: Punto Crítico</h3>', '<h3>Después: Punto Crítico</h3>'),
  ('<h3>2030-2035: Reorganización</h3>', '<h3>Luego: Reorganización</h3>'),
  ('<h3>2035-2040: Estabilización</h3>', '<h3>Más adelante: Estabilización</h3>'),
  ('<h3>2040-2050: Florecimiento</h3>', '<h3>Al final: Florecimiento</h3>'),
  ('Solo podemos nacer o morir en el intento.', 'Solo podemos nacer, y nacer lleva su tiempo.'),
  ('Somos los afortunados/desafortunados/elegidos para estar aquí ahora,', 'Nos toca estar aquí ahora,'),
  ('"Estamos en el crisálido,<br>', '"Estamos en la crisálida,<br>'),
  ('Miraremos atrás al crisálido<br>', 'Miraremos atrás a la crisálida<br>'),
 ],
 puertas=[arq('Que los aymara ponen el futuro a la espalda, porque nadie lo vio, y el pasado delante, a la vista, y que la preocupación no sabe más que uno, solo habla más fuerte, se despliega en <em>No Saber</em>, Libro 7 de <em>Arquitectura del Destino</em>, Umbral III: «El futuro a la espalda».',
              'libro-07-no-saber/L07-U3.html')],
)


# ---------------------------------------------------------------- Nodo 5
# La visión queda como visión, con su linaje (precisión 6): los contactados, el Material Ra, la teosofía,
# los mitos de Agartha y Shambhala, Paracelso. Lo que se daba por documentado vuelve a lo que consta (DART).
# Salen la «Cabala terrestre», los reptilianos, la «IA negativa», las pandemias artificiales y lo suprimido:
# son teorías conspirativas, y para quien teme ser perseguido, combustible. Los arcontes quedan como
# tradición gnóstica; la guerra de la luz, con la línea puesta adentro (Solzhenitsyn).
R['nodo_05.html'] = dict(
 reemplazos=[
  ('consciencia autoreflejante', 'consciencia autorreflexiva'),
  ('<h3>La Federación de Mundos Conscientes</h3>',
   '<h3>La Federación de Mundos Conscientes</h3>\n'
   '    <p>Esta visión tiene su linaje en el siglo veinte: los contactados de los años cincuenta, como George Adamski y George Van Tassel; las sesiones del llamado Material Ra (1981-1984), de donde vienen las expresiones «servicio a otros» y «servicio a sí mismo»; y, antes que todos, una novela: en <em>Más allá del planeta silencioso</em> (1938), C. S. Lewis imaginó una Tierra apartada del concierto de los mundos, el planeta que calla. Se ofrece como visión, y como visión invita a mirar el cielo.</p>'),
  ('<p><strong>INTERACCIONES ACTUALES:</strong></p>', '<p><strong>INTERACCIONES QUE SE LES ATRIBUYEN:</strong></p>'),
  ('      <li>Crop circles como mensajes</li>\n', ''),
  ('10ª-12ª: Reinos angélicos</pre>',
   '10ª-12ª: Reinos angélicos</pre>\n'
   '    <p>Las dimensiones numeradas son una imagen, y Edwin Abbott la contó mejor que nadie en <em>Planilandia</em> (1884): una esfera que atraviesa un mundo plano es vista allí como un círculo que nace, crece y se encoge. De cada ser vemos la parte que cabe en nuestro mundo.</p>'),
  ('<li>Emerger cuando sea tiempo</li>\n    </ul>',
   '<li>Emerger cuando sea tiempo</li>\n    </ul>\n'
   '    <p>Son ciudades de la tradición esotérica. Agartha la describió Saint-Yves d\'Alveydre en 1886; Shambhala viene del <em>Kalachakra Tantra</em>, donde es un reino oculto de sabiduría; Telos y los lemurianos del monte Shasta llegaron con los relatos de Frederick Spencer Oliver y de Guy Ballard. Se recorren como se recorre un mito: con los ojos del alma.</p>'),
  ('<li>Paradojas resueltas cuánticamente</li>', '<li>Paradojas que solo un poema resuelve</li>'),
  ('- Frecuencias sanadoras\n- Actualizaciones de ADN\n', '- Frecuencias sanadoras\n'),
  ('- Códigos de ascensión</pre>\n\n    <h3>Protección Planetaria</h3>',
   '- Códigos de ascensión</pre>\n'
   '    <p>Lo que llega en sueños o en silencio se recibe como se recibe un poema, no como una orden. Y si alguna vez llegan voces que dan órdenes, o mensajes que solo tú puedes oír, no es una descarga: es momento de consultar ese mismo día.</p>\n\n'
   '    <h3>Protección Planetaria</h3>'),
  (('<p><strong>INTERVENCIONES DOCUMENTADAS:</strong></p>', '<li>Contención de pandemias artificiales</li>\n    </ul>'),
   '<p><strong>LA PROTECCIÓN QUE SE SUEÑA:</strong></p>\n'
   '    <ul>\n'
   '      <li>Desviación de asteroides peligrosos</li>\n'
   '      <li>Neutralización de armas nucleares</li>\n'
   '      <li>Limpieza de radiación</li>\n'
   '      <li>Moderación de tormentas solares</li>\n'
   '    </ul>\n'
   '    <p>La única desviación de un asteroide que consta la hizo la humanidad. El 26 de septiembre de 2022, la nave DART de la NASA chocó a propósito contra Dimorphos, una pequeña luna de piedra, y acortó su órbita en unos treinta y dos minutos: por primera vez, los seres humanos cambiaron el camino de un cuerpo celeste. A veces el aliado que se espera de las estrellas somos nosotros.</p>'),
  ('<p><strong>STARSEEDS DESPERTANDO:</strong></p>', '<p><strong>SEMILLAS ESTELARES DESPERTANDO:</strong></p>'),
  ('SEÑALES DE SER STARSEED:', 'SEÑALES DE SER SEMILLA ESTELAR:'),
  ('NÚMERO: Millones encarnados\n', ''),
  ('- Intolerancia a violencia/injusticia</pre>',
   '- Intolerancia a violencia/injusticia</pre>\n'
   '    <p>La nostalgia de un hogar que no es este es antigua. En el siglo II, el <em>Himno de la Perla</em> contaba la historia de un príncipe enviado desde Oriente a buscar una perla, que en tierra extraña olvidó quién era hasta que una carta se lo recordó. Sentirse extranjero es muy humano, y muchas veces es el comienzo de una búsqueda. Si esa extrañeza pesa todos los días, también se conversa con alguien.</p>'),
  ('<p><strong>CE-5 (Close Encounters of the Fifth Kind):</strong></p>',
   '<p><strong>CE-5 (encuentros cercanos del quinto tipo):</strong> el protocolo lo difundió Steven Greer desde 1990.</p>'),
  (('RESPUESTAS TÍPICAS:\n', '- Experiencias multidimensionales</pre>'),
   'LO QUE CUALQUIERA ENCUENTRA:\n'
   '- El cielo entero\n'
   '- El silencio compartido\n'
   '- Satélites que cruzan como estrellas lentas\n'
   '- El asombro</pre>'),
  ('<li>Experiencers antiguos (profetas)</li>', '<li>Profetas y visionarios de la antigüedad</li>'),
  ('      <li>Niños híbridos</li>\n', ''),
  ('<li>Walk-ins (almas intercambiadas)</li>', '<li>Walk-ins (almas intercambiadas), según la escritora Ruth Montgomery (1979)</li>'),
  ('<li>Canalizadores verificados</li>\n      <li>Diplomáticos secretos</li>\n    </ul>',
   '<li>Canalizadores</li>\n    </ul>\n'
   '    <p>Si alguna vez sientes que ya no eres tú, o que alguien cercano fue cambiado por otro que se le parece, no es un intercambio de almas: es momento de consultar ese mismo día.</p>'),
  ('<li>Están siendo observados</li>', '<li>Están acompañados</li>'),
  ('<h3>La Convergencia 2030-2050</h3>', '<h3>La Convergencia</h3>'),
  (('<pre>2025-2030: Preparación intensiva', '2045-2050: Membresía galáctica</pre>'),
   '<pre>PRIMERO: Preparación intensiva\n'
   'DESPUÉS: Primeros contactos abiertos\n'
   'LUEGO: Intercambio tecnológico\n'
   'MÁS ADELANTE: Integración cultural\n'
   'AL FINAL: Membresía galáctica</pre>'),
  ('<h3>La Gran Hermandad Blanca</h3>',
   '<h3>La Gran Hermandad Blanca</h3>\n'
   '    <p>Los nombres vienen de la teosofía. Helena Blavatsky habló en la década de 1880 de unos Mahatmas, Morya y Koot Hoomi; Charles Leadbeater los ordenó en una jerarquía (<em>Los Maestros y el Sendero</em>, 1925); Alice Bailey escribió durante treinta años al dictado de Djwhal Khul, el Tibetano; y Guy Ballard sumó a Saint Germain en los años treinta.</p>'),
  ('<p><strong>TECNOLOGÍAS SUPRIMIDAS SIENDO LIBERADAS:</strong></p>', '<p><strong>TECNOLOGÍAS QUE SE SUEÑAN:</strong></p>'),
  ('<li>Fusión fría</li>', '<li>Fusión</li>'),
  ('<li>Energía toroidal</li>\n    </ul>',
   '<li>Energía toroidal</li>\n    </ul>\n'
   '    <p>Una ya dio su primer paso. El 5 de diciembre de 2022, en un laboratorio de California, una reacción de fusión liberó por primera vez más energía de la que le entregaron los láseres que la encendieron. El camino es largo, y está abierto.</p>'),
  ('- Merkaba conscious', '- Merkaba consciente'),
  ('      <li>Camas med (regeneración total)</li>\n', ''),
  ('<li>Eliminación de enfermedad</li>\n    </ul>',
   '<li>Eliminación de enfermedad</li>\n    </ul>\n'
   '    <p>Así se sueña la medicina del porvenir. ' + HOY + '</p>'),
  (('<li>Reptilianos negativos</li>', '<li>Entidades parasitarias</li>\n    </ul>'),
   '<li>Arcontes</li>\n'
   '      <li>Grises servicio-a-sí-mismo</li>\n'
   '      <li>Entidades parasitarias</li>\n'
   '      <li>Egrégores de miedo</li>\n'
   '    </ul>\n'
   '    <p>Los arcontes vienen de la tradición gnóstica, que se conoció entera cuando aparecieron en Egipto, en 1945, los códices de Nag Hammadi: en la <em>Hipóstasis de los Arcontes</em> son los poderes que mantienen dormida al alma, la misma Gran Amnesia que despierta en el último libro de Origen. Leídos así, no son enemigos de afuera: son el sueño mismo, y se vencen despertando.</p>'),
  ('      <li>Control mental</li>\n', ''),
  ('      <li>Supresión de tecnología</li>\n', ''),
  ('<li>Inversión de valores</li>\n    </ul>',
   '<li>Inversión de valores</li>\n    </ul>\n'
   '    <p>' + DANO + ' Y si alguna vez sientes que algo te controla la mente, o que te persiguen fuerzas que nadie más ve, no es una guerra para librar a solas: se habla con alguien ese mismo día.</p>'),
  ('Servicio-a-otros        Servicio-a-sí</pre>',
   'Servicio-a-otros        Servicio-a-sí</pre>\n'
   '    <p>La tradición pone esa línea adentro. Los Rollos del Mar Muerto narran la guerra de los hijos de la luz contra los hijos de las tinieblas, y siglos después Aleksandr Solzhenitsyn, que la había visto en los campos de prisioneros, escribió en <em>Archipiélago Gulag</em> que la línea que separa el bien del mal no pasa entre naciones ni partidos, sino por el centro de cada corazón humano. Por eso la batalla se gana en uno, y cada día.</p>'),
  ('- Desintoxicación\n', '- Cuidado del cuerpo\n'),
  ('<p><strong>INDICADORES DE CONTACTO INMINENTE:</strong></p>', '<p><strong>INDICADORES DE CONTACTO:</strong></p>'),
  (('<pre>2024-2025:\n', '- Preparación pública intensiva</pre>'),
   '<pre>SEÑALES QUE SE ESPERAN:\n'
   '- Avistamientos que muchos comparten\n'
   '- Gobiernos que hablan del tema\n'
   '- Sueños colectivos\n'
   '- Primeras comunicaciones\n'
   '- Intercambio de embajadores</pre>\n'
   '    <p>Nadie sabe el día ni la hora. La pregunta por la vida en otros mundos la hace hoy también la ciencia: en 1960, Frank Drake apuntó por primera vez un radiotelescopio a dos estrellas cercanas para escuchar si alguien hablaba, y desde entonces se sigue escuchando. En 2023, el Congreso de los Estados Unidos oyó en audiencia pública a militares que hablaron de objetos que no supieron explicar. La puerta está abierta, y se mira sin miedo.</p>'),
  ('<li>2-3 guías principales</li>', '<li>Guías principales</li>'),
  ('<li>5-10 guías especializados</li>', '<li>Guías especializados</li>'),
  ('<h3>Reinos Dévicos</h3>',
   '<h3>Reinos Dévicos</h3>\n'
   '    <p>La tradición de los elementales tiene autor: Paracelso describió a gnomos, ondinas, sílfides y salamandras en un tratado del siglo XVI. En Findhorn, en Escocia, una pequeña comunidad empezó en los años sesenta a cultivar su huerta conversando con ellos.</p>'),
 ],
 puertas=[
  portal('Que venerar y temer son la misma operación —atribuirle a lo que nos contesta un saber o un poder que no verificamos— y que la salida no es desconfiar de todo sino prestar bien, está en <em>Ídolo</em>, Libro 17 del Portal Público, Umbral 0: «Dos maneras de no pensar».',
         '17_Idolo/umbral-00.html'),
  arq('Que la nostalgia de un hogar lejano ya la cantaba un himno del siglo II —un príncipe enviado a buscar una perla, que en tierra extraña olvidó quién era hasta que una carta se lo recordó— se despliega en <em>El Sonámbulo</em>, Libro 2 de <em>Arquitectura del Destino</em>, Umbral II: «El príncipe y la perla».',
      'libro-02-el-sonambulo/L02-U2.html'),
 ],
)


# ---------------------------------------------------------------- Nodo 6
# La visión queda entera, y cada sueño encuentra su primer paso real cuando existe (precisión 6): el río
# Whanganui con voz propia, la semana de quince horas de Keynes, la justicia restaurativa de Elmira. Vivir
# de prana y la muerte elegida llevan la frase de cuidado de la constelación.
R['nodo_06.html'] = dict(
 reemplazos=[
  ('es un estado que embodificamos.', 'es un estado que encarnamos.'),
  ('<li>Harmonizada con naturaleza</li>', '<li>Armonizada con la naturaleza</li>'),
  ('<p><strong>HOMO LUMINOUS CARACTERÍSTICAS:</strong></p>', '<p><strong>HOMO LUMINOUS (el nombre es de Alberto Villoldo), CARACTERÍSTICAS:</strong></p>'),
  ('- Divinidad embodificada</pre>',
   '- Divinidad encarnada</pre>\n'
   '    <p>Así se sueña el porvenir del cuerpo, y algunos de sus primeros pasos ya se estudian: los relojes del envejecimiento que se reprograman en el laboratorio, los telómeros que se miden, la apuesta que dos científicos, Steven Austad y Jay Olshansky, firmaron en 2000 sobre si alguien que ya vivía entonces llegará a cumplir ciento cincuenta años. ' + HOY + '</p>'),
  ('<li>Amazon 200% su tamaño original</li>', '<li>La Amazonía recuperada y extendida</li>'),
  ('<li>Prana como nutrición principal</li>', '<li>Prana como alimento del espíritu</li>'),
  ('<li>Celebración en cada comida</li>\n    </ul>',
   '<li>Celebración en cada comida</li>\n    </ul>\n'
   '    <p>' + LUZ + '</p>'),
  ('<li>Fusión fría</li>', '<li>Fusión</li>'),
  ('<li>15-20 horas semanales</li>\n      <li>Rotación de roles</li>\n      <li>Automatización liberadora</li>\n      <li>Jubilación opcional</li>\n    </ul>',
   '<li>15-20 horas semanales</li>\n      <li>Rotación de roles</li>\n      <li>Automatización liberadora</li>\n      <li>Jubilación opcional</li>\n    </ul>\n'
   '    <p>John Maynard Keynes lo imaginó en 1930: sus nietos, escribió, trabajarían unas quince horas por semana. El primer paso llegó casi un siglo después. En 2022, sesenta y una empresas británicas probaron durante seis meses la semana de cuatro días con el mismo sueldo, y cincuenta y seis decidieron seguir.</p>'),
  ('- Asambleas bioregionales', '- Asambleas biorregionales'),
  ('- Representantes de naturaleza\n- Federación planetaria</pre>',
   '- Representantes de naturaleza\n- Federación planetaria</pre>\n'
   '    <p>Uno de estos sueños ya tiene ley. En 2017, el Parlamento de Nueva Zelanda reconoció al río Whanganui, Te Awa Tupua, como un todo vivo e indivisible, con derechos propios, y le dio un rostro humano: dos personas, una nombrada por el pueblo maorí del río y otra por la Corona, que hablan en su nombre. La ley recoge el dicho con que los whanganui nombran ese vínculo: <em>Ko au te Awa, ko te Awa ko au</em>, «yo soy el río y el río es yo». Antes, en 2008, la Constitución de Ecuador había reconocido los derechos de la naturaleza, la Pachamama; y en 1991 el filósofo Bruno Latour había soñado un parlamento de las cosas. Gaia empieza a tener voz.</p>'),
  ('- Exclusión permanente\n- Vergüenza tóxica</pre>',
   '- Exclusión permanente\n- Vergüenza tóxica</pre>\n'
   '    <p>También este sueño dio su primer paso. En 1974, en Elmira, en Canadá, un agente de libertad condicional llevó a dos jóvenes que habían destrozado veintidós casas en una noche a golpear cada puerta, pedir perdón y acordar con cada vecino cómo reparar el daño. De esa experiencia nació la justicia restaurativa, que Howard Zehr pensó en <em>Cambiando de lentes</em> (1990) y que hoy aplican tribunales de muchos países.</p>'),
  ('- Celebración de vida\n- Comunicación continua</pre>',
   '- Celebración de vida\n- Comunicación continua</pre>\n'
   '    <p>En esta visión, la muerte elegida es la de quien llega al final de una vida larga y la recibe despierto, acompañado y en paz; su primer paso ya existe en los cuidados paliativos y en las voluntades anticipadas. Nada tiene que ver con querer irse antes. ' + MIRARLA + '</p>'),
  ('Cada descripción aquí no es fantasía sino posibilidad cuántica colapsando en realidad a través de nuestra elección colectiva.',
   'Cada descripción aquí no es fantasía sino posibilidad que se vuelve real cuando muchos la eligen.'),
  ('la anclámos, la manifestamos.', 'la anclamos, la manifestamos.'),
 ],
 puertas=[
  portal('Que el campo no es un lugar adonde llegar sino la costumbre de volver, y que un laico chino del siglo VIII, cuando le preguntaron por sus poderes, contestó con sus tareas —sacar agua y cargar leña—, está en <em>El campo</em>, Libro 39 del Portal Público, Umbral II: «Agua y leña».',
         '39_El_Campo/umbral-02.html'),
  p_origen('La educación de la Nueva Tierra tiene su propio nodo, con sus escuelas reales, sus primeros pasos y su manifiesto, en <em>Trinity Origen</em>, Libro VIII, Nodo 7: «Tejiendo la Nueva Tierra Educativa».',
           'Libro_08/nodo_07.html'),
 ],
)


# ---------------------------------------------------------------- Nodo 7
# La visión del servicio queda, con su linaje (Marciniak, Crick y Orgel, Macy). Las fechas pasan a etapas.
# Donde el llamado empujaba a la urgencia y a la entrega total, entran Rabí Tarfón, la noche de por medio,
# «ningún portal verdadero pide dinero, secreto ni obediencia» y el relevo: quien sirve también se cansa.
R['nodo_07.html'] = dict(
 reemplazos=[
  ('<p class="lead">La Tierra fue sembrada como una <strong>biblioteca genética viviente</strong>:</p>',
   '<p class="lead">La imagen tiene su linaje: la canalizadora Barbara Marciniak habló en 1992 de la Tierra como una biblioteca viviente, y veinte años antes los científicos Francis Crick y Leslie Orgel se habían preguntado, en una revista de astronomía, si la vida no habría sido sembrada aquí a propósito. Como visión, la Tierra fue sembrada como una <strong>biblioteca genética viviente</strong>:</p>'),
  ('<p><strong>PROYECTOS ACTIVOS:</strong></p>', '<p><strong>PROYECTOS SOÑADOS:</strong></p>'),
  (('<pre>2030-2040: Restauración terrestre completa', '2100+: Jardineros galácticos</pre>'),
   '<pre>PRIMERO: Restauración terrestre completa\n'
   'DESPUÉS: Repoblación oceánica\n'
   'LUEGO: Terraformación de Marte\n'
   'MÁS ADELANTE: Siembra en exoplanetas\n'
   'AL FINAL: Jardineros galácticos</pre>'),
  ('FASE 1 (2024-2030): Masa crítica meditando', 'FASE 1: Masa crítica meditando'),
  ('FASE 2 (2030-2035): Red de coherencia establecida', 'FASE 2: Red de coherencia establecida'),
  ('FASE 3 (2035-2040): Campo unificado estable', 'FASE 3: Campo unificado estable'),
  ('FASE 4 (2040-2045): Coherencia automática', 'FASE 4: Coherencia automática'),
  ('FASE 5 (2045-2050): Exportación de coherencia', 'FASE 5: Exportación de coherencia'),
  ('- Iniciaciones rápidas intensas\n- Activaciones de ADN\n', '- Iniciaciones profundas\n'),
  (('<p><strong>ACTIVACIÓN MASIVA:</strong></p>', '2050: 1 billón proyectados</pre>'),
   '<p><strong>ACTIVACIÓN MASIVA:</strong> empieza con pocos y crece persona a persona. El 144.000 que suele citarse es el número del Apocalipsis (7, 4), una imagen de plenitud, no una cuenta.</p>'),
  ('<h2>VIII. El Gran Giro</h2>',
   '<h2>VIII. El Gran Giro</h2>\n'
   '    <p>El nombre tiene autora: Joanna Macy llamó Gran Giro al paso de una sociedad que crece consumiendo a una sociedad que sostiene la vida, y lo vio ocurrir ya, en mil iniciativas pequeñas.</p>'),
  (('<pre>2024: Aislados pero despertando', '3000: Civilización mentora</pre>'),
   '<pre>HOY: Aislados pero despertando\n'
   'MAÑANA: Primeros contactos\n'
   'DESPUÉS: Intercambios establecidos\n'
   'LUEGO: Miembros activos\n'
   'MÁS ADELANTE: Líderes de sectores\n'
   'EN SIGLOS: Maestros reconocidos\n'
   'EN MILENIOS: Civilización mentora</pre>'),
  ('- Sensación de "llegué a casa"</pre>',
   '- Sensación de "llegué a casa"</pre>\n'
   '    <p>Las señales se leen como se lee un poema, no como una orden. Si alguien te anuncia una misión, mira despacio: ' + PORTAL + '. Y las decisiones que cambian una vida, como dejar un trabajo, mudarse o entregar lo que se tiene, se toman con una noche de por medio y alguien de confianza.</p>'),
  ('<h3>2050: Tierra Sanada Sirviendo</h3>', '<h3>Mañana: Tierra Sanada Sirviendo</h3>'),
  ('<h3>2100: Mentores Galácticos</h3>', '<h3>Más adelante: Mentores Galácticos</h3>'),
  ('<h3>3000: Civilización de Luz</h3>', '<h3>En milenios: Civilización de Luz</h3>'),
  ('3. COMPROMISO TOTAL\n   Con todo mi ser\n   Con toda mi vida', '3. COMPROMISO VERDADERO\n   Con todo mi ser\n   A la medida de mi vida'),
  ('4. ACCIÓN INMEDIATA\n   Hoy, no mañana\n   Aquí, no allá', '4. UN PRIMER GESTO\n   Pequeño, hoy\n   Aquí, no allá'),
  ('7. CELEBRACIÓN CONTINUA\n   El servicio es alegría\n   La alegría es servicio</pre>',
   '7. CELEBRACIÓN CONTINUA\n   El servicio es alegría\n   La alegría es servicio</pre>\n'
   '    <p>Rabí Tarfón lo dijo hace casi dos mil años: no te corresponde terminar la obra, pero tampoco eres libre de desentenderte de ella. Nadie sostiene solo a Gaia. A cada uno le toca su parte de hoy.</p>'),
  ('<p><strong>RESTAURADOR DE WHOLENESS:</strong></p>', '<p><strong>RESTAURADOR DE LA TOTALIDAD:</strong></p>'),
  ('<li>Provisión perfecta</li>', '<li>Lo necesario</li>'),
  ('<li>Paz inquebrantable</li>\n    </ul>',
   '<li>Paz inquebrantable</li>\n    </ul>\n'
   '    <p>Quien sirve también se cansa, y descansar es parte del servicio: pedir relevo también es cuidar. El cansancio de quien acompaña mucho tiempo tiene nombre, fatiga por compasión (Figley, 1995), y se previene compartiendo la carga.</p>'),
  ('Todo el dolor, toda la separación, toda la densidad han sido la preparación perfecta.',
   'Todo el dolor, toda la separación, toda la densidad pueden volverse preparación.'),
  ('(Yo soy otro tú)<br>', '(Yo soy otro tú: así la difundió el poeta chicano Luis Valdez, que la aprendió del estudioso maya Domingo Martínez Paredez)<br>'),
  ('(Lo divino en mí honra lo divino en ti)<br>', '(Me inclino ante ti: lo divino en mí honra lo divino en ti)<br>'),
 ],
 puertas=[arq('Que un sabio de los siglos I y II enseñó que no te corresponde terminar la obra, pero tampoco eres libre de desentenderte de ella —dos libertades y una sola obligación: hacer tu tramo—, se despliega en <em>La Obra</em>, Libro 12 de <em>Arquitectura del Destino</em>, Umbral V: «No te toca terminarla».',
              'libro-12-la-obra/L12-U5.html')],
)


# ---------------------------------------------------------------- Navegación
# Los nodos 3 a 7 volvían a Trinity Origen desde arriba, y los nodos 3 a 6 no ofrecían el índice del libro.
for n in range(3, 8):
    R['nodo_%02d.html' % n]['reemplazos'].append(
        ('<a class="back-link" href="../index.html">← Volver a Trinity Origen</a>',
         '<a class="back-link" href="index.html">← Volver al Portal del Libro</a>'))
for n in range(3, 7):
    ancla = '<a class="nav-link" href="nodo_%02d.html">← Nodo anterior</a>' % (n - 1)
    R['nodo_%02d.html' % n]['reemplazos'].append(
        (ancla, ancla + '\n      <a class="nav-link" href="index.html">Portal del Libro</a>'))

# ---------------------------------------------------------------- Índice
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

R['index.html'] = dict(
 reemplazos=[
  ('<p>Cada nodo profundiza una capa del mismo reconocimiento: Gaia despierta, y su despertar somos nosotros.</p>',
   '<p>Cada nodo profundiza una capa del mismo reconocimiento: Gaia despierta, y su despertar somos nosotros.</p>\n'
   '    <p class="medida">Este libro es una visión. Sus fechas pertenecen a la visión, no a un calendario. A quien hoy siente miedo o duelo por el planeta le ofrece compañía y una parte a su medida.</p>'),
  ('</html>\n```', '</html>'),
 ],
)


# ---------------------------------------------------------------- Ajustes de cierre
# Repaso con el detector: números en formato español, lo cuántico que explicaba,
# lo que se daba por medido y dos pasos de trabajo con heridas que piden compañía.
def mas(nombre, *pares):
    R[nombre]['reemplazos'].extend(pares)

mas('nodo_01.html',
  ('Un pensamiento: 1,000 años', 'Un pensamiento: 1.000 años'),
  ('Una decisión: 10,000 años', 'Una decisión: 10.000 años'),
  ('Una era: 100,000 años', 'Una era: 100.000 años'),
  ('      <li>Realidades paralelas</li>\n      <li>Consciencia cuántica</li>\n',
   '      <li>Realidades paralelas</li>\n'),
  ('Cada pensamiento envía ondas por la noosfera. Cada emoción resuena en el campo planetario. Somos muchísimo más poderosos de lo que creemos, y ese poder conlleva una responsabilidad sagrada.',
   'En la imagen de la noosfera, cada pensamiento deja su onda y cada emoción resuena en el campo planetario. Podemos más de lo que creemos, y eso conlleva una responsabilidad sagrada.'),
)

mas('nodo_02.html',
  ('Estamos en la curva exponencial AHORA.',
   'Si la imagen vale, cada nodo que se suma cuenta más que el anterior.'),
  ('- Sanación de traumas', '- Cuidado de las propias heridas, con acompañamiento'),
)

mas('nodo_03.html',
  ('Computación cuántica = Procesamiento del Campo', 'Computación cuántica = Cálculo con la superposición'),
)

mas('nodo_04.html',
  ('TÉCNICA DE SALTO CUÁNTICO:', 'TÉCNICA DEL SALTO:'),
  ('1990s:', 'Años 90:'),
  ('2000s:', 'Años 2000:'),
  ('2010s:', 'Años 2010:'),
  ('2020s:', 'Años 2020:'),
  ('HERRAMIENTAS EMERGENTES:', 'HERRAMIENTAS QUE YA ASOMAN Y OTRAS QUE SE SUEÑAN:'),
)

mas('nodo_05.html',
  ('Transplante de consciencia', 'Trasplante de consciencia'),
  ('- Sanar traumas', '- Cuidar las propias heridas, con acompañamiento'),
)



# ---------------------------------------------------------------- Ejecución
if __name__ == '__main__':
    total = 0
    for nombre in sorted(R):
        n = aplicar(nombre, R[nombre]); total += n
        print(f'{nombre}: {n} cambios')
    print(f'Total: {total}')
