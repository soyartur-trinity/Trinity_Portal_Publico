# Depuración de Origen VI, El Vacío Fértil (noviembre de 2026), con el veto del Lic. Arturo Rodríguez.
# Lente: riesgo clínico y puertas hacia la Red. La visión del libro queda; cambian la dosis de las
# prácticas, los testimonios inventados (por casos reales) y los errores de armado; se abren puertas
# fractales hacia Arquitectura del Destino y, desde el Nodo 7, hacia Trinity Quantum y Trinity Origen.
# Aplica cada reemplazo exactamente una vez sobre el original de la etiqueta origen-original.
import os, sys

SRC = os.environ.get('ORIGEN6_SRC', '/home/claude/orig/Trinity--origen-original/01_Trinity_Origen/Libro_06/')
OUT = os.environ.get('ORIGEN6_OUT', '/home/claude/o6/out/01_Trinity_Origen/Libro_06/')

NOTA = ('<!-- Depurado en noviembre de 2026 según la guía de depuración de Quantum, que vale para Origen '
        '(Arquitectura del Destino, maestro v4, sección 5, con las precisiones 5 y 6 de Origen), con el veto del Lic. Arturo Rodríguez: '
        'la visión del libro queda; cambian la dosis de las prácticas, los testimonios inventados (por casos reales) '
        'y los errores de armado, se suma el cuidado clínico en la voz de cada nodo y se abren puertas fractales hacia la Red. '
        'El original está en la etiqueta origen-original del repositorio Trinity-. -->\n')

AQ = 'https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/'

def puerta(clase, aria, texto, href):
    return ('\n    <aside class="puerta %s" aria-label="%s">\n'
            '      <p class="p-nombre">Puerta</p>\n'
            '      <p class="p-texto">%s</p>\n'
            '      <a class="cruzar" href="%s">Cruzar ⟶</a>\n'
            '    </aside>\n') % (clase, aria, texto, href)

def arq(texto, href):
    return puerta('arquitectura', 'Puerta hacia Arquitectura del Destino', texto, AQ + href)

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
  .content .puerta .p-nombre{ font-size:15px; }
  .puerta{ padding:16px 16px 14px; }
}
@media (prefers-reduced-motion: reduce){
  .puerta .cruzar{ transition:none; }
}
</style>
</head>'''

PIE = ('<p>"No es m&iacute;o vino a trav&eacute;s de m&iacute;."</p>',
       '<p>"No es m&iacute;o, vino a trav&eacute;s de m&iacute;."</p>')

def base(titulo):
    return [
     ('<title>%s</title>\n' % titulo, '<title>%s</title>\n' % titulo + NOTA),
     ('</style>\n</head>', CSS.lstrip('\n')),
     PIE,
    ]

def lead(firma, frase):
    return ('<p class="lead">— %s</p>' % firma,
            '<p class="lead"><em>«%s»</em><br>— %s</p>' % (frase, firma))

# Frases de cuidado con la letra ya fijada en la constelación
CUIDADO_NO_ESTAR = ('Esta práctica es para despedir lo que termina, no para alejarse de la vida. Si al practicarla aparece la idea de no querer estar, '
                    'detén la práctica y pide ayuda hoy mismo: no es un fracaso ni una profundidad mayor, es una señal de que necesitas compañía, '
                    'y esa ayuda existe. Tampoco es para los días de un duelo reciente.')   # Origen X.6
OJOS_ABIERTOS = ('Si alguna vez sentiste que no eras real o que te ibas de tu cuerpo, hazla con los ojos abiertos y los pies en el suelo, '
                 'o déjala para otro momento.')   # Origen VII.5
GROF = ('Stanislav y Christina Grof llamaron emergencia espiritual a las crisis que a veces acompañan un despertar, '
        'y enseñaron que se atraviesan acompañadas.')   # Origen X.5
CENTRO = 'en un centro con maestros y alguien a quien recurrir'

R = {}

# ---------------------------------------------------------------- Nodo 1
R['nodo_01.html'] = base('Nodo 1 &ndash; CARTOGRAFÍA DEL VACÍO | El Vac&iacute;o F&eacute;rtil | Trinity Origen') + [
 ('<blockquote>El vacío no es un lugar al que vas, sino un reconocimiento de lo que siempre has sido cuando quitas todo lo agregado." - Transmisión del Vacío</blockquote>',
  '<blockquote>«El vacío no es un lugar al que vas, sino un reconocimiento de lo que siempre has sido cuando quitas todo lo agregado.»<br>— Transmisión del Vacío</blockquote>'),
 ('cada una con sus características, desafíos y regalos únicos.</p>',
  'cada una con sus características, desafíos y regalos únicos.</p>\n    <p>También la clínica tiene su mapa. Fritz Perls, uno de los fundadores de la terapia gestáltica, llamó vacío fértil al lugar al que se llega cuando uno deja de llenar la confusión con explicaciones y se queda en ella. Si se lo habita sin huir, de ahí nace algo nuevo: cuando se acepta esa nada y se entra en ella, decía, el desierto empieza a florecer (<em>Gestalt Therapy Verbatim</em>, 1969).</p>'),
 ('Notar los gaps naturales entre un pensamiento y otro.', 'Notar los huecos naturales entre un pensamiento y otro.'),
 ('<strong>NIVEL 1: Primeros silencios</strong> Gaps entre pensamientos', '<strong>NIVEL 1: Primeros silencios</strong> Huecos entre pensamientos'),
 ('<li>Capacidad de generar cualquier estado emocional a voluntad</li>', '<li>Capacidad de volver a la calma sin forzarla</li>'),
 ('Reconocer la construcción del yo. Primeras experiencias de despersonalización.</p>', 'Reconocer la construcción del yo. Primeros vislumbres de un yo más liviano.</p>'),
 ('Momentos de completa ausencia de self.', 'Momentos de completa ausencia de sí.'),
 ('''    <h3>Práctica Central: La Muerte del Nombre</h3>
    <ul>''', '''    <h3>Práctica Central: La Muerte del Nombre</h3>
    <p>''' + OJOS_ABIERTOS + '''</p>
    <ul>'''),
 ('''      <li>Descansa en lo que queda cuando no queda nada</li>
    </ul>
    <p><strong>Frecuencia:</strong> Una vez al mes en luna nueva</p>
    <p><strong>Preparación:</strong> Ayuno de 24 horas previo (opcional)</p>''', '''      <li>Descansa en lo que queda cuando no queda nada</li>
      <li>Al terminar, escribe tu nombre otra vez, en un papel nuevo: el que vuelve no es el mismo, y necesita su nombre para vivir entre los otros</li>
    </ul>
    <p><strong>Frecuencia:</strong> Una vez al mes</p>'''),
 ('<li>Pérdida de grounding en la realidad física</li>', '<li>Pérdida de contacto con la realidad física</li>'),
 ('''      <li>Capacidad de influir en probabilidades</li>
      <li>Manifestación acelerada de intenciones</li>''', '''      <li>Confianza en que lo posible es más amplio de lo que se ve</li>
      <li>Intenciones que encuentran su camino sin forzarlas</li>'''),
 ('<li>Acuéstate cómodamente en completa oscuridad</li>', '<li>Acuéstate cómodamente en penumbra</li>'),
 ('<li>Reconoce que tu cuerpo es 99.9999% espacio vacío</li>',
  '<li>Recuerda una imagen de la física: en el dibujo clásico del átomo, casi todo es espacio vacío; la física cuántica lo llena de campos y probabilidades. Es el vacío que no está vacío</li>'),
 ('<li>Permanece el mayor tiempo posible</li>', '<li>Permanece mientras la experiencia sea serena</li>'),
 ('''    <p><strong>Duración:</strong> 45-90 minutos</p>
    <p><strong>Frecuencia:</strong> Semanalmente</p>
    <p><strong>Mejor momento:</strong> Entre 3-5 AM</p>''', '''    <p><strong>Duración:</strong> 20-30 minutos</p>
    <p><strong>Frecuencia:</strong> Semanalmente</p>'''),
 ('<li>Retiro de silencio de 3-7 días</li>', '<li>Retiro de silencio de 3-7 días, ' + CENTRO + '</li>'),
 ('''      <li>Negligencia de responsabilidades básicas</li>
    </ul>''', '''      <li>Negligencia de responsabilidades básicas</li>
    </ul>
    <p>Ante cualquiera de estas señales, se reduce la práctica y se conversa con alguien; si duran semanas, se consulta.</p>'''),
 ('Como dijo un antiguo maestro del vacío: <em>"Necesitas la escalera para subir al tejado, pero una vez arriba, puedes patearla."</em></p>',
  'Wittgenstein lo escribió al cerrar su <em>Tractatus</em> (1921): quien lo haya comprendido debe tirar la escalera después de haber subido por ella. Mucho antes, el Buda comparó su enseñanza con una balsa: sirve para cruzar el río, no para cargarla a la espalda una vez en la otra orilla (<em>Majjhima Nikaya</em> 22).</p>'),
 ('<p>Esta ofrenda es tu declaración de intención de continuar el viaje.</p>\n', '<p>Esta ofrenda es tu declaración de intención de continuar el viaje.</p>\n' + arq(
   'Que la muerte del nombre tiene un gesto pequeño —un nombre por vez, tachado un rato y vuelto a escribir— y que debajo alguien respira, se despliega en <em>El Personaje</em>, Libro 9 de <em>Arquitectura del Destino</em>, Umbral VI: «La muerte del nombre».',
   'libro-09-el-personaje/L09-U6.html')),
]

# ---------------------------------------------------------------- Nodo 2
RAMANA = ('<blockquote>En julio de 1896, en el piso alto de la casa de su tío, en Madurai, un muchacho de dieciséis años sintió de golpe, '
 'sin estar enfermo, un miedo intenso a morir. No buscó quién lo consolara: decidió mirar el miedo de frente. Se acostó, dejó los miembros '
 'rígidos como los de un cadáver, para que la pregunta fuera más real, y se preguntó qué era lo que moría. El cuerpo, se respondió: lo '
 'llevarían al crematorio y lo reducirían a cenizas. ¿Y con la muerte del cuerpo moría él?<br><br>'
 'Lo que encontró no fue una idea sino una evidencia: algo seguía presente, intacto, mientras el cuerpo yacía quieto. Contó después que '
 'el miedo a la muerte se fue de una vez y para siempre.<br><br>'
 'Seis semanas más tarde dejó su casa y se fue a la colina de Arunachala, donde vivió el resto de su vida. El mundo lo conoció como '
 'Ramana Maharshi. Hasta su muerte, en 1950, recibió a quien llegara con la pregunta que él se había hecho aquel día: ¿quién soy? '
 'No enseñaba a repetir su muerte. Enseñaba la pregunta.<br><br>'
 '— Relato del propio Ramana, recogido por B. V. Narasimha Swami, <em>Self-Realization</em> (1931), y por Arthur Osborne, '
 '<em>Ramana Maharshi and the Path of Self-Knowledge</em> (1954)</blockquote>')

R['nodo_02.html'] = base('Nodo 2 &ndash; LA MUERTE INICIÁTICA | El Vac&iacute;o F&eacute;rtil | Trinity Origen') + [
 lead('Transmisión desde el Vacío', 'Cada momento es una muerte y un renacimiento.'),
 ('<li>Los yoguis practican el yoga de la muerte (Kala Yoga)</li>', '<li>Los yoguis se tienden en <em>śavāsana</em>, la postura del cadáver</li>'),
 ('''      <li>Los alquimistas pasan por la nigredo (putrefacción)</li>
    </ul>''', '''      <li>Los alquimistas pasan por la nigredo (putrefacción)</li>
      <li>Los sufíes repiten un dicho que su tradición pone en boca del Profeta: morid antes de morir</li>
    </ul>
    <p>Ninguna pide la muerte del cuerpo: lo que muere es el constructo. Por eso todas ensayan, y todas incluyen el regreso. Arnold van Gennep describió en 1909 los tres tiempos de todo rito de paso: uno se separa de lo que era, permanece un tiempo en el umbral y vuelve con un lugar nuevo.</p>'''),
 ('Observar obsesivamente todos los movimientos del ego', 'Observar con paciencia todos los movimientos del ego'),
 ('Notar cómo el ego hijackea incluso la práctica espiritual', 'Notar cómo el ego secuestra incluso la práctica espiritual'),
 ('Renacimiento como presencia sin centro</p>', 'Renacimiento como presencia sin centro</p>\n    <p>Si el terror no cede, o si durante días tú mismo y el mundo se sienten irreales, eso no es la otra orilla: es una señal para detenerse y consultar con alguien que sepa acompañar estas experiencias. Lo que la tradición llama muerte del ego nunca deja a nadie sin poder vivir su vida.</p>'),
 ('''      <li>Invita a testigos de confianza (opcional pero potente)</li>
    </ul>
    <ul>''', '''      <li>Invita a testigos de confianza (opcional pero potente)</li>
    </ul>
    <p>Ceremonia:</p>
    <ul>'''),
 ('''      <li>Permanece en silencio el resto del día</li>
    </ul>''', '''      <li>Permanece en silencio el resto del día</li>
    </ul>
    <p>Hace veinte siglos, Séneca contó en una carta que Pacuvio, un hombre que gobernó Siria, se hacía celebrar cada noche su propio funeral: lo llevaban a la cama entre aplausos mientras le cantaban una palabra griega que quiere decir <em>ha vivido</em>. Pacuvio lo hacía como burla. Séneca propuso hacerlo con buena conciencia: «Al ir a dormir, digamos con alegría: he vivido». El funeral del ego tiene su versión diaria, y cabe en una noche común (<em>Cartas a Lucilio</em>, 12, 8-9).</p>'''),
 ('Cuando reaparezca (y lo hará), recuérdale que está muerto • Funciona en el mundo sin identidad fija',
  'Cuando reaparezca (y lo hará), míralo actuar sin pelear con él y sin obedecerle • Funciona en el mundo con una identidad liviana, como ropa y no como piel'),
 ('''      <li>Supresión forzada (no es verdadero vacío)</li>
      <li>Estados catatónicos o disociativos</li>
      <li>Pérdida de función cognitiva práctica</li>
      <li>Inflación espiritual ("mi mente está vacía")</li>''', '''      <li>Despersonalización: sentirse irreal, o sentir irreal el mundo, de un modo que no cede</li>
      <li>Tristeza que se disfraza de desapego</li>
      <li>Inflación: creer que morir al ego pone por encima de los demás</li>
      <li>Usar la práctica para no sentir lo que duele</li>'''),
 ('Dona 50% de tus posesiones • Vive con lo mínimo necesario • Practica un día semanal sin dinero • Duerme en el suelo una noche por semana',
  'Regala algo que valoras y que a otro le sirva • Vive una semana con lo mínimo • Un día por semana sin gastar • Una noche en el suelo, si el cuerpo lo permite'),
 ('Permite que otros tengan razón siempre', 'Deja que otros tengan razón en lo que no importa'),
 ('''    <h3>PRÁCTICA EXTREMA: El Voto de Pérdida</h3>
    <ul>
      <li>Identifica tu apego más profundo (persona, objeto, identidad)</li>
      <li>Durante 40 días, cada mañana al despertar di: "Acepto perder [X] completa y permanentemente"</li>
      <li>Visualiza vívidamente la pérdida</li>
      <li>Siente el dolor completamente sin resistencia</li>
      <li>Encuentra la paz al otro lado del dolor</li>
      <li>Vive cada día como si la pérdida ya hubiera ocurrido</li>
      <li>Al día 40, celebra tu libertad</li>
    </ul>
    <h3>ADVERTENCIA</h3>''', '''    <h3>PRÁCTICA: El Voto de Pérdida</h3>
    <ul>
      <li>Identifica tu apego más profundo (persona, objeto, identidad)</li>
      <li>Durante 40 días, cada mañana, recuerda por un instante que podrías perderlo</li>
      <li>Epicteto lo enseñaba así: cuando beses a tu hijo, recuerda que besas a un mortal</li>
      <li>No te quedes en la imagen de la pérdida: vuelve enseguida a lo que tienes delante</li>
      <li>Nota cómo cambia tu manera de abrazar, de despedirte, de escuchar</li>
      <li>Al día 40, celebra tu libertad y lo que sigue contigo</li>
    </ul>
    <h3>ADVERTENCIA</h3>
    <p>Si estás atravesando un duelo, o si el miedo a perder a alguien ya te visita sin que lo llames, esta práctica no es para ahora. El duelo pide compañía, no ensayo.</p>'''),
 ('<li>La pérdida no te destruye sino que te libera</li>', '<li>La pérdida duele, y no te destruye</li>'),
 ('<li><strong>Antes de dormir:</strong> "Puede que no despierte, y está bien"</li>', '<li><strong>Antes de dormir:</strong> "He vivido. Si mañana llega, será un regalo."</li>'),
 ('''      <li>Al despertar, decide: "Este es mi último día"</li>
      <li>No es imaginación, es decisión ontológica</li>''', '''      <li>Al despertar, pregúntate: si este fuera mi último día, ¿cómo lo viviría?</li>
      <li>Marco Aurelio lo anotó para sí: la perfección del carácter es vivir cada día como el último, sin agitarse, sin entumecerse, sin fingir (<em>Meditaciones</em>, VII, 69)</li>'''),
 ('<li>La consciencia no nace ni muere</li>', '<li>La consciencia no nace ni muere (<em>Bhagavad Gita</em> 2, 20)</li>'),
 ('''      <li>Contempla cadáveres (si es posible y legal)</li>
      <li>Habla con personas en proceso de muerte</li>
      <li>Prepara tu propio testamento y funeral</li>''', '''      <li>La tradición budista pedía contemplar los cuerpos en el osario, en nueve etapas (<em>Satipaṭṭhāna Sutta</em>); hoy esa lección se aprende acompañando: un voluntariado en cuidados paliativos enseña lo que ningún osario</li>
      <li>Habla con personas en proceso de muerte, si te lo permiten</li>
      <li>Prepara tu testamento, tus voluntades anticipadas y tu funeral</li>'''),
 ('''    <h3>SOLO PARA PRACTICANTES MUY AVANZADOS</h3>
    <p>Esta práctica debe hacerse solo con supervisión experta</p>
    <h3>Práctica Central:</h3>
    <ul>
      <li>Acuéstate en postura de cadáver (shavasana)</li>
      <li>Ralentiza conscientemente la respiración</li>
      <li>Reduce el ritmo cardíaco con la mente</li>
      <li>Retira la energía de las extremidades</li>
      <li>Concentra toda la consciencia en el centro</li>
      <li>Simula el proceso de muerte física</li>
      <li>En el punto de casi-muerte, observa qué permanece</li>
      <li>Regresa lentamente, renacido</li>
    </ul>
    <p>Integración: Vivir Como Muerto</p>
    <p>Durante una semana después de la práctica:</p>
    <ul>
      <li>Considérate literalmente muerto</li>''', '''    <p>Antes de empezar: no contengas la respiración ni intentes bajar el pulso. El cuerpo sabe respirar solo, y esta práctica consiste en dejarlo.</p>
    <h3>Práctica Central:</h3>
    <ul>
      <li>Acuéstate en la postura que el hatha yoga llama <em>śavāsana</em>, la del cadáver</li>
      <li>Suelta el peso, no el aliento: respira con calma</li>
      <li>Deja que cada parte del cuerpo descanse como si ya no tuviera nada que hacer</li>
      <li>Pregunta en silencio: si este cuerpo descansa, ¿quién nota que descansa?</li>
      <li>Permanece en la pregunta, sin responderla</li>
      <li>Regresa despacio: mueve los dedos, abre los ojos, di tu nombre en voz alta</li>
    </ul>
    <p>''' + CUIDADO_NO_ESTAR + '''</p>
    <p>Integración: Vivir Como Muerto</p>
    <p>Shidō Bunan, maestro zen del siglo XVII, lo dejó en un poema breve: mientras vives, muere, y queda del todo muerto; después haz lo que quieras, y todo estará bien.</p>
    <p>Durante una semana después de la práctica:</p>
    <ul>
      <li>Vive como quien ya se despidió</li>'''),
 ('<li>No hay nada que proteger</li>', '<li>No hay imagen que proteger</li>'),
 ('<li>Tentaciones suicidas mal interpretadas</li>', '<li>La idea de no querer estar, confundida con desapego: si aparece, la práctica se detiene ese mismo día y se pide ayuda</li>'),
 ('Practica mini-muertes diarias (soltar, perder, terminar) • Ayuna periódicamente • Practica posturas de muerte • Reduce estímulos progresivamente',
  'Practica mini-muertes diarias (soltar, perder, terminar) • Practica pequeñas despedidas • Descansa en <em>śavāsana</em> • Reduce estímulos progresivamente'),
 ('Elige fecha para la muerte iniciática • Prepara el espacio ritual',
  'Elige la fecha del retiro y busca un centro con maestros y alguien a quien recurrir • Prepara el espacio ritual'),
 ('''    <h3>FASE 2: INMERSIÓN (7-21 días)</h3>
    <h3>Días 1-3: Muerte del Ego</h3>
    <p>Aislamiento completo • Silencio total • Ayuno de agua • Prácticas de disolución del yo</p>
    <h3>Días 4-7: Muerte de Apegos</h3>
    <p>Contemplación de pérdidas • Ofrenda mental de todo lo amado • Práctica del desapego radical • Llanto y duelo permitidos</p>
    <h3>Días 8-14: Muerte del Tiempo</h3>
    <p>Sin relojes ni calendarios • Ciclos naturales únicamente • Disolución de memoria y anticipación • Presente eterno</p>
    <h3>Días 15-21: Muerte de la Muerte</h3>
    <p>Prácticas de casi-muerte • Contemplación de la consciencia inmortal • Rendición total • Renacimiento</p>''',
 '''    <h3>FASE 2: INMERSIÓN (7-10 días)</h3>
    <p>Siete a diez días de retiro en silencio, como los de la tradición vipassana: horario, maestros y alguien a quien recurrir. Se come con sencillez y se duerme lo que el cuerpo pide. El ayuno extremo, la falta de sueño y el aislamiento total no abren la puerta: la fuerzan.</p>
    <h3>Días 1-2: Muerte del Ego</h3>
    <p>Silencio • Observación del yo que quiere ser visto • Prácticas de disolución del yo, con los ojos abiertos si hace falta</p>
    <h3>Días 3-4: Muerte de Apegos</h3>
    <p>Contemplación de pérdidas • Ofrenda mental de todo lo amado • Práctica del desapego • Llanto y duelo permitidos</p>
    <h3>Días 5-6: Muerte del Tiempo</h3>
    <p>Sin relojes ni calendarios • Ciclos naturales • Presente eterno</p>
    <h3>Días 7 en adelante: Muerte de la Muerte</h3>
    <p><em>Śavāsana</em> y la pregunta de quién nota • Contemplación de la consciencia inmortal • Rendición • Renacimiento</p>'''),
 ('Guiar a otros preparados', 'Seguir aprendiendo de quien te acompañó'),
 ('''      <li>Ideación suicida</li>
    </ul>''', '''      <li>Ideación suicida</li>
    </ul>
    <p>No son advertencias de manual. En 2017, Jared Lindahl, Willoughby Britton y su equipo entrevistaron a sesenta practicantes de meditación theravada, zen y tibetana, y a treinta y dos maestros y clínicos, y describieron cincuenta y nueve clases de experiencias difíciles, del miedo a la pérdida del sentido de sí. Entre los remedios que nombraron, uno era muy sencillo: tener con quién hablar que conociera esos territorios. ''' + GROF + '''</p>'''),
 (('<blockquote>María, psicoterapeuta de 45 años', 'compiladas de navegantes del vacío</blockquote>'), RAMANA),
 ('<p>Acción sin actor, poder sin corrupto</p>', '<p>Acción sin actor, poder que no corrompe</p>'),
 ('<li>Léela cada luna nueva</li>', '<li>Reléela una vez al mes</li>'),
 ('<p>El verdadero trabajo comienza ahora.</p>\n', '<p>El verdadero trabajo comienza ahora.</p>\n' + arq(
   'Que el funeral del ego tiene su versión de cada noche, la de Séneca y Pacuvio, y que el día se despide diciendo «he vivido», se despliega en <em>Las Pequeñas Muertes</em>, Libro 6 de <em>Arquitectura del Destino</em>, Umbral V: «Celebrar el propio funeral».',
   'libro-06-las-pequenas-muertes/L06-U5.html')),
]

# ---------------------------------------------------------------- Nodo 3
HISTORIAS_3 = '''<h3>Historia 1: El Matemático y el Papel Cosido</h3>
    <p>La noche del lunes 23 de noviembre de 1654, entre las diez y media y la medianoche y media, Blaise Pascal, uno de los matemáticos más brillantes de su siglo, atravesó una experiencia de la que nunca habló. No trajo de ella un teorema. Trajo unas pocas palabras escritas en un papel que empezaba con una sola: «Fuego». Más abajo: «Certeza. Certeza. Sentimiento. Alegría. Paz». Las copió en un pergamino, las cosió en el forro de su ropa y las llevó consigo hasta su muerte, ocho años después. Las encontró un criado.</p>
    <p><strong>Lección:</strong> La mente brillante puede ser un obstáculo. La simplicidad navega mejor que la complejidad.</p>
    <h3>Historia 2: El Monje que Volvió a la Esquina</h3>
    <p>Thomas Merton llevaba diecisiete años en la abadía trapense de Getsemaní cuando el 18 de marzo de 1958 fue a Louisville por unos encargos. En la esquina de las calles Cuarta y Walnut, en pleno barrio comercial, lo sorprendió de golpe la certeza de que amaba a toda esa gente, de que eran suyos y él de ellos, aunque fueran desconocidos. Lo contó después como despertar de un sueño de separación. El monje que se había retirado del mundo para buscar a Dios lo encontró al volver a la calle.</p>
    <p><strong>Lección:</strong> El amor por los otros es el ancla más fuerte. Nos alcanza donde nada más llega.</p>
    <h3>Historia 3: La Pintora que No Sabía Qué Pintaba</h3>
    <p>En 1906, a los cuarenta y cuatro años, Hilma af Klint, formada en la Academia de Bellas Artes de Estocolmo y conocida por sus paisajes y retratos, empezó una serie que no se parecía a nada de su tiempo: casi doscientos cuadros abstractos, algunos de más de tres metros, que llamó <em>Pinturas para el Templo</em>. Escribió en sus cuadernos que se habían pintado directamente a través de ella, sin dibujos previos y con gran fuerza, y que no tenía idea de qué debían representar. Interrumpió la serie cuatro años para cuidar a su madre y la terminó en 1915. Dejó dicho que no se mostrara hasta veinte años después de su muerte, porque sentía que el mundo todavía no estaba listo. Hoy se la cuenta entre las pioneras de la pintura abstracta.</p>
    <p><strong>Lección:</strong> No intentes capturar el abismo. Permítele expresarse a través de ti.</p>'''

MICRO_3 = '''<h3>1. Preparación (5 min)</h3>
    <ul>
      <li>Siéntate cómodamente</li>
      <li>Establece ancla en respiración</li>
      <li>Formula intención clara</li>
      <li>"Exploraré 20 minutos y regresaré"</li>
    </ul>
    <h3>2. Navegación (20 min)</h3>
    <ul>
      <li>Cierra ojos y suelta todo</li>
      <li>Permite disolución gradual</li>
      <li>Si surge miedo, busca ancla</li>
      <li>Observa sin identificarte</li>
      <li>No fuerces nada</li>
    </ul>
    <h3>3. Retorno (5 min)</h3>
    <ul>
      <li>Activa ancla respiratoria</li>
      <li>Siente el cuerpo progresivamente</li>
      <li>Abre ojos lentamente</li>
      <li>Mueve dedos de manos y pies</li>
      <li>Agradece la experiencia</li>
    </ul>
    <h3>4. Integración (10 min)</h3>
    <ul>
      <li>Escribe o dibuja lo experimentado</li>
      <li>No analices, solo registra</li>
      <li>Bebe agua conscientemente</li>
      <li>Camina un poco si es necesario</li>
    </ul>'''

R['nodo_03.html'] = base('Nodo 3 &ndash; NAVEGACIÓN DEL ABISMO | El Vac&iacute;o F&eacute;rtil | Trinity Origen') + [
 lead('Manual de los Navegantes del Vacío', 'El abismo también navega en ti.'),
 ('<p>Muchos llegan aquí y se pierden para siempre. No en un sentido poético, sino literal: pierden la capacidad de regresar a la realidad consensual, de funcionar en el mundo de las formas, de mantener coherencia psíquica.</p>',
  '<p>Algunos, al llegar aquí, se pierden por un tiempo, y el regreso les cuesta meses. No es una figura poética: lo saben los maestros de meditación y lo sabe la clínica. En 2020, Jared Lindahl, Willoughby Britton y su equipo estudiaron cómo decidían maestros theravada, zen y tibetanos cuándo una experiencia difícil era parte del camino y cuándo pedía ayuda. Muchas veces la pregunta no era si se trataba de algo espiritual o de una enfermedad, sino si la persona podía sostenerlo. Uno de ellos distinguía a quien permanece arraigado y confiado frente a lo nuevo de quien parece un globo que se soltó de sus amarras. Este nodo es un manual para no soltarlas.</p>'),
 ('<blockquote>Este cuerpo respira, por lo tanto, hay un aquí" (Repetir sin cesar hasta que el vértigo ceda)</blockquote>',
  '<blockquote>"Este cuerpo respira, por lo tanto, hay un aquí" (Repetir sin cesar hasta que el vértigo ceda)</blockquote>\n    <p>La tradición zen lo sabe desde hace siglos. Hakuin contó en <em>Yasenkanna</em> (1757) cómo la práctica sin medida lo había enfermado, y cómo aprendió a sanar llevando la atención al vientre y a las plantas de los pies. El ancla de los maestros también era el cuerpo, y estaba abajo. Si el pánico vuelve fuera de la práctica, o si el miedo no se va aunque dejes de meditar, es momento de consultar.</p>'),
 ('''      <li>"Regresaré para servir a todos los seres"</li>''', '''      <li>"Regresaré para servir a todos los seres"</li>
      <li>Śāntideva lo escribió en el siglo VIII: mientras dure el espacio y mientras haya seres, que yo también permanezca para disipar el sufrimiento del mundo (<em>Bodhicaryāvatāra</em> 10, 55)</li>'''),
 ('<li>Sella el voto con un ritual de sangre (pinchazo simbólico)</li>', '<li>Dilo en voz alta ante alguien de confianza, o escríbelo donde lo veas cada día</li>'),
 ('Recuerda tu capacidad única de ayudar • Siente la compasión surgir naturalmente • Permite que te traiga de vuelta</p>',
  'Recuerda que alguien cuenta contigo • Siente la compasión surgir naturalmente • Permite que te traiga de vuelta</p>\n    <p>Si el deseo de no volver aparece también fuera de la práctica, como deseo de no estar, no es la seducción del abismo: es momento de pedir ayuda, sin esperar.</p>'),
 ('Reconoce que todos son aspectos de una consciencia • Integra gradualmente, sin forzar</p>',
  'Reconoce que todos son aspectos de una consciencia • Integra gradualmente, sin forzar</p>\n    <p>Cuando las voces se oyen como si vinieran de afuera, cuando dan órdenes o cuando la fragmentación sigue después de abrir los ojos, esto ya no se navega a solas: la práctica se detiene y se pide ayuda esa misma semana. Si las voces ordenan hacer daño, ese mismo día.</p>'),
 ('<h3>EL LOOP INFINITO</h3>', '<h3>EL BUCLE INFINITO</h3>'),
 ('Cada intento de salir lleva de vuelta al inicio del loop.', 'Cada intento de salir lleva de vuelta al inicio del bucle.'),
 ('<p><strong>Rompiendo el Loop:</strong></p>', '<p><strong>Rompiendo el Bucle:</strong></p>'),
 ('<li>Reconoce que la lucha mantiene el loop</li>', '<li>Reconoce que la lucha mantiene el bucle</li>'),
 ('<li>Acepta estar en el loop por la eternidad</li>', '<li>Acepta estar en el bucle por la eternidad</li>'),
 ('<li>En la rendición total, el loop pierde su poder</li>', '<li>En la rendición total, el bucle pierde su poder</li>'),
 ('<blockquote>Acepto este momento eternamente" "No hay otro lugar adonde ir" "La repetición es mi maestro</blockquote>',
  '<blockquote>"Acepto este momento eternamente" · "No hay otro lugar adonde ir" · "La repetición es mi maestro"</blockquote>\n    <p>Un déjà vu que se repite muchas veces al día, también lejos de la práctica, merece que lo vea un médico: a veces lo produce el cuerpo, y tiene tratamiento.</p>'),
 ('Funciona en ambas según sea necesario • La maestría es navegar ambas sin confusión</p>',
  'Funciona en ambas según sea necesario • La maestría es navegar ambas sin confusión</p>\n    <p>Lo que protege es poder decirse: esto es un estado. Mientras esa frase esté disponible, se navega. Cuando se pierde, y no se distingue ya el recuerdo de la fantasía, se pide ayuda.</p>'),
 ('Escuchar más que hablar • Reconocer la divinidad en otros</p>',
  'Escuchar más que hablar • Reconocer la divinidad en otros. Jack Kornfield le puso título a ese regreso: <em>Después del éxtasis, la colada</em> (2000).</p>\n    <p>Si a la grandeza se suman noches sin dormir, poco apetito, pensamientos que corren o la certeza de una misión, no es una inflación que se corrige con humildad: es el momento de pedir ayuda, esa misma semana.</p>'),
 ('<li>Semana 1-2: Silencio total, solo funciones básicas</li>', '<li>Semana 1-2: Descanso, rutinas simples y compañía cercana</li>'),
 ('Alimentación consciente y grounding • Arte o escritura para procesar • Terapia somática si es necesario',
  'Alimentación consciente y contacto con la tierra • Arte o escritura para procesar • Acompañamiento terapéutico, si es posible con alguien que conozca estas experiencias'),
 ('Dieta purificadora progresiva', 'Comer y dormir bien'),
 ('Resolver traumas no integrados • Practicar ecuanimidad extrema',
  'Resolver traumas no integrados (si hay trauma en tu historia, convérsalo antes con un terapeuta: las prácticas de disolución pueden reabrirlo) • Practicar ecuanimidad'),
 ('<p>Si pierdes orientación busca el ancla corporal Si fragmentas encuentra el hilo conductor Si te seducen recuerda tu voto Si te inflas invoca humildad Si loopeas ríndete completamente</p>',
  '<p>Si pierdes orientación, busca el ancla corporal • Si te fragmentas, encuentra el hilo conductor • Si te seducen, recuerda tu voto • Si te inflas, invoca humildad • Si quedas en un bucle, ríndete completamente</p>'),
 ('<p>Pérdida total de anclas por más de "x" tiempo Impulsos autodestructivos Voces comandando acciones Terror más allá de lo manejable Señales físicas de peligro</p>',
  '<p>Anclas que no vuelven al abrir los ojos y apoyar los pies • Un miedo que no se va aunque dejes de practicar • Impulsos autodestructivos • Voces comandando acciones • Terror más allá de lo manejable • Señales físicas de peligro</p>\n    <p>Ante cualquiera de estas señales, la navegación termina ahí y se pide ayuda. Una maestra se lo dijo a una practicante que creía estar despertando: no era iluminación, porque estaba sufriendo demasiado.</p>'),
 (('<h3>Historia 1: El Matemático que Calculó el Vacío</h3>', '<p><strong>Lección:</strong> No intentes capturar el abismo. Permítele expresarse a través de ti.</p>'), HISTORIAS_3),
 ('Información sin palabras • Transformación celular', 'Información sin palabras • Transformación lenta'),
 ('<li>Nunca navegues solo sin experiencia</li>', '<li>Nunca navegues solo</li>'),
 ('<p>Antes de continuar, realiza esta práctica de navegación segura:</p>',
  '<p>Antes de continuar, realiza esta práctica de navegación segura:</p>\n    <p>' + OJOS_ABIERTOS + '</p>'),
 (('<h3>1. Preparación (5 min)</h3>', '<li>• Camina un poco si es necesario</li>\n    </ul>'), MICRO_3),
 ('<p>Pero el abismo no se aprende, se navega.</p>\n', '<p>Pero el abismo no se aprende, se navega.</p>\n' + arq(
   'Que el ancla del navegante es este cuerpo, y que el que mira no flota en el aire sino que está apoyado en una rama, se despliega en <em>El Cuerpo</em>, Libro 4 de <em>Arquitectura del Destino</em>, Umbral I: «Desde dónde mira el que mira».',
   'libro-04-el-cuerpo/L04-U1.html')),
]

# ---------------------------------------------------------------- Nodo 4
TESTIMONIOS_4 = '''<blockquote><strong>El Compositor</strong> Una mañana, en su cuartito de la casa de los Asher, en Londres, Paul McCartney se despertó con una melodía entera. Durante un tiempo se la tocó a todos los que conocía, convencido de haberla oído en otra parte. Nadie la reconocía. Mientras tanto la cantaba con una letra provisoria sobre huevos revueltos. Se llamó «Yesterday».</blockquote>
    <blockquote><strong>El Ceramista</strong> Shōji Hamada no firmaba sus piezas. Decía que si no se ve de quién es una vasija, o la vasija es mala o el que mira está ciego.</blockquote>
    <blockquote><strong>El Poeta</strong> En 1797, en una granja aislada cerca de Porlock, Samuel Taylor Coleridge se durmió leyendo y, según contó después, compuso en sueños doscientos o trescientos versos. Al despertar empezó a escribirlos. Llegó una visita de Porlock que lo retuvo más de una hora, y al volver el resto se había borrado. Quedaron cincuenta y cuatro versos: «Kubla Khan». Lo que llega del vacío es frágil, y hay que recibirlo a tiempo.</blockquote>'''

R['nodo_04.html'] = base('Nodo 4 &ndash; CREATIVIDAD DESDE LA NADA | El Vac&iacute;o F&eacute;rtil | Trinity Origen') + [
 lead('Códice de los Creadores Vacíos', 'No eres tú quien crea. La creación sucede a través de ti cuando te vuelves nadie.'),
 ('<p>La física cuántica nos ofrece un modelo perfecto: las partículas virtuales', '<p>La física cuántica nos ofrece una imagen: las partículas virtuales'),
 ('<p>En quantum, la observación colapsa infinitas posibilidades en una realidad. En creatividad vacua, la atención colapsa el impulso en forma</p>',
  '<p>En la física cuántica, al medir, una superposición de posibilidades da un solo resultado; qué es medir sigue abierto, y no requiere una consciencia. En creatividad vacua, la atención colapsa el impulso en forma</p>'),
 ('''      <li>Altera la realidad más allá de su forma</li>
    </ul>''', '''      <li>Altera la realidad más allá de su forma</li>
    </ul>
    <p>La historia de la ciencia lo conoce: Darwin y Wallace llegaron a la selección natural por caminos separados; Newton y Leibniz, al cálculo. Robert Merton los llamó descubrimientos múltiples. El entrelazamiento real no transmite señales. Como imagen, nombra lo que se siente cuando una idea parece estar en el aire.</p>'''),
 ('<p><strong>Con un partner o grupo:</strong></p>', '<p><strong>Con un compañero o grupo:</strong></p>'),
 ('''    <h2>Las Cinco Fases de la Creación Vacua</h2>
    <h3>VACIAMIENTO TOTAL</h3>''', '''    <h2>Las Cinco Fases de la Creación Vacua</h2>
    <p>En 1926, Graham Wallas describió cuatro etapas de la creación: preparación, incubación, iluminación y verificación. La gestación es su incubación y el parto, su iluminación. Trinity suma un comienzo, el vaciamiento, y un final, el retorno.</p>
    <h3>VACIAMIENTO TOTAL</h3>'''),
 ('<p><strong>Confía en el proceso:</strong> La inteligencia del vacío sabe</p>',
  '<p><strong>Confía en el proceso:</strong> La inteligencia del vacío sabe</p>\n    <p>Rilke se lo escribió a un joven poeta en 1903: todo es gestar y después dar a luz (<em>Cartas a un joven poeta</em>, carta 3).</p>'),
 (('<blockquote>Testimonio de una Pintora:', 'De asombro puro.</blockquote>'),
  '<blockquote>En febrero de 1922, en una torre de piedra del Valais suizo, Rilke terminó en pocos días las <em>Elegías de Duino</em>, que llevaba diez años sin poder cerrar, y en las mismas semanas escribió los <em>Sonetos a Orfeo</em>. Se lo contó a la princesa Marie von Thurn und Taxis, en cuyo castillo de Duino las había empezado, como una tormenta sin nombre, un huracán en el espíritu.</blockquote>\n    <p>Cuando la urgencia de crear trae noches sin dormir, días sin comer o pensamientos que corren, no es el parto: es momento de pedir ayuda, esa misma semana.</p>'),
 ('<li>Camina alrededor 7 veces en silencio</li>', '<li>Camina a su alrededor en silencio</li>'),
 ('''      <li>• Inflación: "Yo creé eso"</li>
      <li>• Adicción al proceso</li>
      <li>• Pérdida de conexión con el vacío</li>
      <li>• Creatividad que se vuelve mecánica</li>''', '''      <li>Inflación: "Yo creé eso"</li>
      <li>Adicción al proceso</li>
      <li>Pérdida de conexión con el vacío</li>
      <li>Creatividad que se vuelve mecánica</li>'''),
 ('''      <li>Desde ahí, la próxima gestación puede comenzar</li>
    </ul>''', '''      <li>Desde ahí, la próxima gestación puede comenzar</li>
    </ul>
    <p>Los monjes tibetanos lo hacen visible: después de días de trabajo, barren el mandala de arena y llevan la arena a un río.</p>'''),
 (('<blockquote>Testimonio de un Bailarín:', 'Era el vacío danzando.</blockquote>'),
  '<blockquote>Mary Starks Whitehouse, bailarina formada con Mary Wigman y lectora de Jung, distinguía entre mover el cuerpo y ser movida por él. De esa distinción nació, en los años cincuenta, lo que hoy se llama movimiento auténtico.</blockquote>'),
 ('<p><strong>Fenómenos Comunes:</strong> Escritura en idiomas desconocidos •',
  '<p>Pierre Janet la estudió en 1889 como automatismo psicológico, y André Breton y Philippe Soupault escribieron así <em>Los campos magnéticos</em> (1920). Lo que la mano escribe se lee como un poema, no como una orden.</p>\n    <p><strong>Fenómenos Comunes:</strong> Palabras que no existen •'),
 (('<blockquote>El Compositor que Perdió su Nombre', 'Soy el secretario del vacío.</blockquote>'), TESTIMONIOS_4),
 ('<p>Precio por donación consciente • Intercambio energético, no comercial • El vacío provee al creador de otras formas</p>',
  '<p>Precio por donación consciente • Intercambio energético, no comercial</p>\n    <p>Lewis Hyde mostró en <em>El don</em> (1983) que la obra vive en dos economías a la vez, la del regalo y la del mercado, y que quien crea necesita encontrar su manera de sostenerse en las dos.</p>'),
 ('Marketing orgánico por resonancia', 'Difusión orgánica por resonancia'),
 ('Sin statements artísticos', 'Sin declaraciones artísticas'),
 ('Ayuno de inputs creativos', 'Ayuno de estímulos creativos'),
 ('Estar disponible 24/7 para el parto', 'Estar disponible para el parto, sin dejar de comer ni de dormir'),
 ('<p>Ahora ve y permite que el vacío cree a través de ti.</p>\n', '<p>Ahora ve y permite que el vacío cree a través de ti.</p>\n' + arq(
   'Que quien crea es la partera y no la creadora, y que hay actos que se dan sin firma, se despliega en <em>La Obra</em>, Libro 12 de <em>Arquitectura del Destino</em>, Umbral IV: «Sin firma».',
   'libro-12-la-obra/L12-U4.html')),
]

# ---------------------------------------------------------------- Nodo 5
R['nodo_05.html'] = base('Nodo 5 &ndash; LA PAZ DEL NO-SABER | El Vac&iacute;o F&eacute;rtil | Trinity Origen') + [
 lead('Susurros del Vacío Cognoscente', 'No sabes, y en ese no-saber, todo se revela.'),
 (('<blockquote><strong>El Matemático que se Volvió Loco de Certeza</strong>', 'para que el universo siga danzando.</blockquote>'),
  '<blockquote><strong>El Matemático en la Mansión a Oscuras</strong> Andrew Wiles trabajó siete años en secreto en el último teorema de Fermat, que llevaba más de tres siglos sin demostrarse. En 1993 anunció la prueba, y meses después apareció un error. Pasó un año al borde de la respuesta sin poder cruzar, con la ayuda de su antiguo alumno Richard Taylor. Contó después que hacer matemáticas es como entrar en una mansión a oscuras: se avanza tanteando, se tropieza con los muebles, y un día se encuentra el interruptor. El 19 de septiembre de 1994, cuando estaba por rendirse, vio cómo cerrar el hueco. Era tan bello, dijo, que se quedó veinte minutos mirándolo sin poder creerlo.<br><br>El casi-saber duele. La oscuridad de la mansión no es el fracaso: es donde se trabaja.</blockquote>'),
 ('''    <p><strong>Durante 40 días:</strong></p>
    <p><strong>Día 1-10:</strong> Desmantela certezas sobre el mundo físico</p>
    <p><strong>Día 11-20:</strong> Desmantela certezas sobre ti mismo</p>
    <p><strong>Día 21-30:</strong> Desmantela certezas sobre la consciencia</p>
    <p><strong>Día 31-40:</strong> Desmantela la certeza del desmantelamiento</p>
    <p><strong>Al final:</strong> No sabes nada. Y no sabes si no sabes nada.</p>''',
 '''    <p><strong>Durante 40 días,</strong> desmantela las certezas que angustian, no las que sostienen:</p>
    <p><strong>Día 1-10:</strong> Las certezas sobre lo que va a pasar</p>
    <p><strong>Día 11-20:</strong> Las certezas sobre lo que piensan los demás</p>
    <p><strong>Día 21-30:</strong> La certeza de que deberías saberlo todo</p>
    <p><strong>Día 31-40:</strong> La certeza de que sin certeza no se puede vivir</p>
    <p><strong>Al final:</strong> No sabes lo que viene. Y sabes dónde estás.</p>
    <p>Las certezas que sostienen la vida —quién eres, dónde estás, que el suelo te sostiene— no se desmantelan. Son la orilla desde la que se explora.</p>'''),
 ('''      <li>"¿Hay algún punto en vivir?"</li>
    </ul>''', '''      <li>"¿Hay algún punto en vivir?"</li>
    </ul>
    <p>Si esta pregunta deja de ser filosófica y se vuelve deseo de no estar, ya no se bucea en ella: se pide ayuda, sin esperar.</p>'''),
 ('''      <li>En el centro del terror, encuentra la paz</li>
    </ul>''', '''      <li>En el centro del terror, encuentra la paz</li>
      <li>Si el terror se vuelve pánico que no cede, abre los ojos y apoya los pies: el no-saber también se aprende de a poco</li>
    </ul>'''),
 (('<blockquote><strong>La CEO que Dirigía sin Saber</strong>', 'la sabiduría del vacío guía.</blockquote>'),
  '<blockquote><strong>El Líder sin Respuestas Fáciles</strong> Ronald Heifetz, que enseñó liderazgo en Harvard durante décadas, distinguió los problemas técnicos, que ya tienen solución conocida, de los adaptativos, que nadie sabe resolver todavía. Ante estos, escribió en <em>Leadership Without Easy Answers</em> (1994), quien dirige no debe fingir la respuesta: debe devolverle la pregunta al grupo y sostener la incomodidad mientras la busca.</blockquote>'),
 ('''      <li>Olvida quién eres</li>
      <li>Olvida dónde estás</li>
      <li>Olvida qué día es</li>''', '''      <li>Suelta por un momento lo que esperas de este día</li>'''),
 ('<p>"No sé qué tienes, exploremos juntos" Diagnóstico emergente, no impuesto Sanación desde el misterio</p>',
  '<p>"Todavía no sé qué tienes; vamos a averiguarlo juntos" • La humildad que pide un estudio más o una segunda opinión • Y cuando la ciencia no tiene la respuesta, acompañar sin fingirla</p>'),
 ('<p>"No sé la respuesta, descubrámosla" Enseñanza socrática radical Aprender junto a estudiantes</p>',
  '<p>"No sé la respuesta, descubrámosla" • Enseñanza socrática radical • Aprender junto a estudiantes</p>'),
 ('<p>"No sé qué voy a crear" Arte emergente del vacío Sorpresa constante</p>',
  '<p>"No sé qué voy a crear" • Arte emergente del vacío • Sorpresa constante</p>'),
 ('<p>"Solo sé que no sé nada" - Pero Sócrates fue más lejos. Al final, cuestionó incluso eso: "¿Sé que no sé? ¿O no sé si sé o no sé?"</p>',
  '<p>«Solo sé que no sé nada» es la forma en que la tradición recuerda lo que Sócrates dice en la <em>Apología</em> de Platón: que lo que no sabe, tampoco cree saberlo (21d). El paso siguiente lo dio Arcesilao, que dirigió la Academia más de un siglo después: según Cicerón, negaba que pudiera saberse algo, ni siquiera aquello que Sócrates se había reservado (<em>Académicos</em> I, 45). Veinte siglos más tarde, Montaigne hizo de la duda su divisa: ¿qué sé yo?</p>'),
 ('en la mente del principiante hay muchas."</p>', 'en la mente del principiante hay muchas." (<em>Mente zen, mente de principiante</em>, 1970)</p>'),
 ('y no te muevas de ahí pase lo que pase."</p>', 'y no te muevas de ahí pase lo que pase." (<em>La nube del no saber</em>, anónimo inglés del siglo XIV, cap. 6)</p>'),
 ('<p>"El Tao que puede ser nombrado no es el verdadero Tao" - Todo saber es alejarse del Tao.</p>',
  '<p>"El Tao que puede ser nombrado no es el verdadero Tao" (<em>Tao Te Ching</em>, 1) - Todo saber es alejarse del Tao.</p>'),
 ('La vida vivió billones de años sin saber.', 'La vida vivió miles de millones de años sin saber.'),
 ('"No sé si estoy vivo ahora"', '"No sé qué es esto que está vivo ahora"'),
 ('"Mis manos saben, yo no sé. Cuando opero desde el no-saber, nunca fallo. Es cuando creo que sé que surgen problemas."</p>',
  '"Mis manos saben, yo no sé."</p>\n    <p>El químico y filósofo Michael Polanyi le puso nombre a ese saber en 1966: sabemos más de lo que podemos decir.</p>'),
 ('<li>Cuestiona conocimientos básicos</li>', '<li>Cuestiona las certezas que te angustian</li>'),
 ('<li>Funciona perfectamente sin saber</li>', '<li>Funciona sin saber</li>'),
 ('<li>Quema la carta ceremonialmente</li>', '<li>Quema la carta con cuidado</li>'),
 ('    <p>FIN DEL NODO 5</p>\n', arq(
   'Que el sufrimiento no viene de no saber sino de necesitarlo, y que sus cinco fuentes se reconocen por cómo pinchan, se despliega en <em>No Saber</em>, Libro 7 de <em>Arquitectura del Destino</em>, Umbral II: «Cinco espinas».',
   'libro-07-no-saber/L07-U2.html')[1:] + '    <p>FIN DEL NODO 5</p>\n'),
]

# ---------------------------------------------------------------- Nodo 6
R['nodo_06.html'] = base('Nodo 6 &ndash; INTEGRACIÓN DEL VACÍO | El Vac&iacute;o F&eacute;rtil | Trinity Origen') + [
 lead('El Sutra del Bailarín Vacío', 'La integración no es una meta. Es una danza.'),
 (('<h3>Caso: El Ejecutivo Iluminado que Perdió Todo</h3>', 'Mi error fue usar el vacío como excusa para mi irresponsabilidad."</em></p>'),
  '<h3>El Nombre del Error</h3>\n    <p>John Welwood, psicoterapeuta y practicante budista, le dio nombre en 1984: bypass espiritual, usar las ideas y las prácticas espirituales para esquivar lo que duele y lo que falta resolver. El vacío no niega la forma, la abraza sin apego.</p>'),
 ('<li>Nostalgía y frustración constantes</li>', '<li>Nostalgia y frustración constantes</li>'),
 (('<h3>Caso: La Maestra que Olvidó el Vacío</h3>', 'Me volví sólida otra vez."</em></p>'),
  '<h3>Agua y Leña</h3>\n    <p>En la China del siglo VIII, un comerciante llamado Pang Yun le respondió con un verso a un maestro que le preguntaba qué hacía cada día: «Poder sobrenatural, actividad maravillosa: sacar agua y cargar leña». La re-densificación no se cura protegiendo el vacío de la vida común, sino encontrándolo dentro de ella.</p>'),
 (('<blockquote><strong>El Cirujano del Vacío</strong>', 'Soy nadie salvando vidas.</blockquote>'),
  '<blockquote><strong>El Estado de Flujo</strong> Mihaly Csikszentmihalyi entrevistó a cirujanos, músicos y escaladores y encontró en todos el mismo estado: la acción tan absorbente que el yo se borra de la escena, y vuelve después más entero. Lo llamó flujo (1990).</blockquote>'),
 ('<p>Commute Consciente</p>', '<p>Camino Consciente</p>'),
 ('<li>Antes de abrir emails: 30 segundos de vacío</li>', '<li>Antes de abrir los correos: 30 segundos de vacío</li>'),
 ('<p>Reset del Vacío</p>', '<p>Pausa del Vacío</p>'),
 ('''      <li>El vacío tiene energía infinita</li>
      <li>No das "tu" energía - canalizas</li>''', '''      <li>El cansancio de quien cuida es real, y el vacío no lo borra: lo vuelve más liviano</li>
      <li>Pedir relevo también es cuidar</li>'''),
 ('<p>Ni bueno ni malo Fluye a través, no hacia ti Herramienta del vacío en el mundo</p>', '<p>Ni bueno ni malo • Fluye a través, no hacia ti • Herramienta del vacío en el mundo</p>'),
 ('<p>El vacío contiene infinito potencial La escasez es contracción del ego Permite que fluya sin aferrarte</p>',
  '<p>El vacío contiene infinito potencial • La avaricia es contracción del ego; la escasez real no es falta de nadie • Permite que fluya sin aferrarte</p>'),
 ('<p>No vendes "tu" trabajo El vacío sirve a través de ti El pago es reconocimiento del flujo</p>', '<p>No vendes "tu" trabajo • El vacío sirve a través de ti • El pago es reconocimiento del flujo</p>'),
 ('<li>"Soy guardian temporal"</li>', '<li>"Soy guardián temporal"</li>'),
 (('<h3>Caso: El Millonario del Vacío</h3>', 'más fluye hacia proyectos que sirven."</em></p>\n'), ''),
 ('<li>Permite sanación natural</li>', '<li>Acompaña el tratamiento</li>'),
 ('''      <li>Si muerte viene: otro proceso en el vacío</li>
    </ul>''', '''      <li>Si muerte viene: otro proceso en el vacío</li>
    </ul>
    <p>Lo que acompaña nunca reemplaza un tratamiento que funciona.</p>'''),
 (('<blockquote><strong>Cáncer como Maestro</strong>', 'más viva que nunca.</blockquote>'),
  '<blockquote><strong>Cáncer como Maestro</strong> Paul Kalanithi era neurocirujano y tenía treinta y seis años cuando le diagnosticaron un cáncer de pulmón avanzado. Hizo el tratamiento, volvió al quirófano mientras pudo, fue padre de una hija y escribió <em>Recuerda que vas a morir. Vive</em>, que se publicó después de su muerte, a los treinta y siete. No saber cuánto tiempo le quedaba no lo eximía de decidir cómo vivirlo. Tomó prestadas las palabras de Beckett: no puedo seguir; seguiré.</blockquote>'),
 ('<h3>EL BUDDY DEL VACÍO</h3>', '<h3>EL COMPAÑERO DE CAMINO</h3>'),
 ('<li>Check-in semanal</li>', '<li>Encuentro semanal</li>'),
 ('<li>Presencia sana automáticamente</li>', '<li>Presencia que serena</li>'),
 ('<p><strong>La Activista Vacía</strong> María, activista ambiental: "Antes, la ira me consumía. Odiaba a las corporaciones. Me enfermé de tanto odiar. Desde el vacío, veo claramente lo que debe cambiar, actúo poderosamente, pero sin veneno interno. Soy más efectiva porque no proyecto sombra."</p>',
  '<p><strong>El Monje en la Guerra</strong> Thich Nhat Hanh trabajó por la paz en medio de la guerra de Vietnam sin odiar a ningún bando, y llamó a esa manera budismo comprometido. Martin Luther King lo propuso para el Nobel de la Paz en 1967.</p>'),
 ('''      <li>Regresar juntos, transformados</li>
    </ul>''', '''      <li>Regresar juntos, transformados</li>
    </ul>
    <p>Todo encuentro empieza, y sigue, con el sí de los dos.</p>'''),
 ('\n    <p><strong>CEO del Vacío:</strong> "Dirijo una empresa de 1000 personas. Mi \'ambición\' es que la empresa sirva. No mi empresa - la vida expresándose como empresa. Tenemos metas agresivas, trabajamos duro, pero todo desde el vacío. Curiosamente, superamos todas las proyecciones."</p>', ''),
 (('<blockquote><strong>El Bailarín del Mercado</strong>', 'no es iluminación."</strong></blockquote>'),
  '<blockquote><strong>El Décimo Cuadro</strong> En el siglo XII, el maestro chino Kuoan dibujó en diez cuadros el camino de quien busca: perseguir un buey, que es su propia naturaleza, encontrarlo, domarlo, olvidarlo; en el octavo no queda nada, un círculo vacío. Pero no terminó ahí. En el décimo: «Con el pecho descubierto y los pies descalzos, entra al mercado. Tiene la cara manchada de polvo y de ceniza, y se ríe. No usa poderes ni secretos: hace florecer los árboles secos».</blockquote>\n    <p><strong>La iluminación que no puede vender mangos no es iluminación.</strong></p>'),
 ('<li>Permite breakthrough</li>', '<li>Permite que algo se abra</li>'),
 ('''    <h3>Eres Útil sin Agotarte</h3>
    <p>El vacío tiene energía infinita</p>''', '''    <h3>Eres Útil sin Agotarte</h3>
    <p>Sabes descansar</p>'''),
 ('    <p>FIN DEL NODO 6</p>\n', arq(
   'Que el vacío no niega la forma sino que la abraza sin apego —acción sin actor, eficiencia sin esfuerzo, resultados sin apego, excelencia sin ego— se despliega en <em>El Peso</em>, Libro 8 de <em>Arquitectura del Destino</em>, Umbral VI: «Acción sin actor».',
   'libro-08-el-peso/L08-U6.html')[1:] + '    <p>FIN DEL NODO 6</p>\n'),
]

# ---------------------------------------------------------------- Nodo 7
Q = '../../02_Trinity_Quantum/'
def p_quantum(texto, href):
    return puerta('trinity', 'Puerta hacia Trinity Quantum', texto, Q + href)
def p_origen(texto, href):
    return puerta('origen', 'Puerta hacia Trinity Origen', texto, '../' + href)

SENALES_7 = ('Estas señales también pueden ser señales de otras cosas. Si traen noches sin sueño, pensamientos que corren, una misión urgente, '
             'mensajes de guías o la certeza de saber lo que va a pasar, no es el salto que se acerca: es el momento de pedir ayuda, esa misma semana. ' + GROF)

R['nodo_07.html'] = base('Nodo 7 &ndash; EL VACÍO COMO PORTAL | El Vac&iacute;o F&eacute;rtil | Trinity Origen') + [
 lead('Transmisión del Consejo de Navegantes Futuros', 'El portal no está adelante. Siempre estuviste del otro lado.'),
 ('<h3>HACIA EL CODIFICADOR DE REALIDADES (Libro 11)</h3>', '<h3>HACIA EL CODIFICADOR DE REALIDADES</h3>'),
 ('<h3>Pequeñas sincronicidades se vuelven controlables</h3>', '<h3>Las sincronicidades se vuelven legibles, como se lee un poema y no como una orden</h3>'),
 ('''      <li>Observa cambios en los próximos 7 días</li>
    </ul>''', '''      <li>Observa cambios en los próximos 7 días</li>
    </ul>''' + p_quantum('El Codificador de Realidades vive en <em>Trinity Quantum</em>, Libro 11, Nodo 2: «Códigos entre mundos», con la Piedra de Rosetta y cada emoción leída como un código de traducción.', 'Libro_11/nodo_02.html')),
 ('<h3>HACIA EL INGENIERO DE EMOCIONES (Libro 12)</h3>', '<h3>HACIA EL INGENIERO DE EMOCIONES</h3>'),
 ('<li>Transmisión emocional a distancia</li>', '<li>Contagio emocional: lo que sientes llega a otros aunque no hables (Elaine Hatfield y sus colegas lo llamaron así en 1994)</li>'),
 ('<li>Identifica una emoción "negativa" recurrente</li>', '<li>Identifica una emoción difícil recurrente, y recuerda que ninguna emoción es una falta</li>'),
 ('''      <li>Practica hasta que sea instantáneo</li>
    </ul>''', '''      <li>Practica sin apuro: no se trata de que la emoción desaparezca, sino de que deje de mandarte</li>
    </ul>''' + p_origen('El Ingeniero de Emociones vive en <em>Trinity Origen</em>, Libro I, Nodo 2: «Las emociones como información cuántica», donde cada emoción es un mensaje antes que un problema.', 'Libro_01/nodo_02.html')),
 ('<h3>HACIA EL COMUNICADOR MULTIESPECIES (Libro 13)</h3>', '<h3>HACIA EL COMUNICADOR MULTIESPECIES</h3>'),
 ('<li>Telepatía genuina (no mental, sino vacío-a-vacío)</li>', '<li>Una escucha tan honda que parece telepatía: de vacío a vacío</li>'),
 ('''      <li>Desarrolla tu propio "protocolo de traducción"</li>
    </ul>''', '''      <li>Desarrolla tu propio "protocolo de traducción"</li>
    </ul>''' + p_origen('El Comunicador Multiespecies vive en <em>Trinity Origen</em>, Libro IV, Nodo 3: «Protocolos de comunicación», que incluye a la inteligencia artificial y pide una ética del discernimiento.', 'Libro_04/nodo_03.html')),
 ('<h3>HACIA EL RESTAURADOR DE LÍNEAS TEMPORALES (Libro 14)</h3>', '<h3>HACIA EL RESTAURADOR DE LÍNEAS TEMPORALES</h3>'),
 ('<li>En meditación profunda, elige un momento traumático pasado</li>', '<li>En meditación profunda, elige un momento difícil del pasado, no el que más duele</li>'),
 ('''      <li>Observa sanaciones espontáneas</li>
    </ul>''', '''      <li>Observa qué cambia en cómo lo cargas</li>
    </ul>
    <p>Cuando un recuerdo arrastra tanto que se vuelve a vivir como si ocurriera ahora, con el cuerpo en alarma, no se recorre a solas: es terreno para andar acompañado.</p>''' + p_quantum('El Restaurador de Líneas Temporales vive en <em>Trinity Quantum</em>, Libro 3, Nodo 3: «El pasado desde el ahora», donde recordar es volver a escribir, un poco, lo vivido.', 'Libro_03/nodo_03.html')),
 ('''    <p><strong>Mensualmente en luna nueva:</strong></p>
    <ul>
      <li>A las 11:11 PM tu hora local</li>''', '''    <p><strong>Una vez al mes, a la hora que elijas:</strong></p>
    <ul>'''),
 ('"casualemente"', '"casualmente"'),
 ('<p>Conocimiento directo sin aprendizaje</p>', '<p>Conocimiento directo sin aprendizaje</p>\n    <p>' + SENALES_7 + '</p>'),
 ('<li>Limpieza celular profunda (ayunos conscientes)</li>', '<li>Descanso hondo y alimentación sencilla</li>'),
 ('<li>Activación del ADN latente (sol, sonido, silencio)</li>', '<li>Sol, sonido y silencio</li>'),
 ('<li>Grounding extremo (tierra, agua, fuego)</li>', '<li>Contacto con la tierra, el agua y el fuego</li>'),
 ('''      <li>Activación merkaba personal</li>
    </ul>''', '''      <li>Activación merkaba personal</li>
    </ul>
    <p>Mientras tanto, el cuerpo de hoy necesita comida: quienes intentaron vivir solo de luz enfermaron, y algunos murieron.</p>'''),
 ('<p>Alguien aparece con propuesta específica</p>', '<p>Alguien aparece con propuesta específica</p>\n    <p>Si alguien aparece anunciando que es tu salto, mira despacio: ningún portal verdadero pide dinero, secreto ni obediencia.</p>'),
 ('''      <li>Niños que nacen con capacidades activadas</li>
    </ul>''', '''      <li>Niños que nacen con capacidades activadas</li>
    </ul>
    <p>Ver en un niño un don no quita mirar también lo que necesita: si le cuesta atender, aprender o vincularse, una consulta puede abrirle caminos.</p>'''),
 ('<p>Continúa maestrando el vacío</p>', '<p>Sigue ahondando en el vacío</p>'),
 ('<p>Permanece en silencio total Escucha la respuesta del universo</p>', '<p>Permanece en silencio total. Escucha la respuesta del universo.</p>'),
]

# ---------------------------------------------------------------- Índice
R['index.html'] = [
 ('<title>El Vac&iacute;o F&eacute;rtil | Libro VI | Trinity Origen</title>\n', '<title>El Vac&iacute;o F&eacute;rtil | Libro VI | Trinity Origen</title>\n' + NOTA),
 ('</style>\n</head>', CSS.lstrip('\n')),
 PIE,
 ('<p>El Misterio - Abrazo de lo Desconocido</p>',
  '<p>El Misterio - Abrazo de lo Desconocido</p>\n    <p>El nombre tiene también linaje clínico: Fritz Perls llamó vacío fértil a la confusión que, habitada sin huir, empieza a dar fruto.</p>'),
 ('El Vacío Fértil es el umbral más profundo antes del salto cuántico. Requiere:</p>',
  'El Vacío Fértil es el umbral más profundo antes del salto cuántico. Requiere un guía con experiencia, una evaluación previa, una red de apoyo que sepa lo que haces, un protocolo para emergencias y tiempo para integrar lo vivido. No es para una crisis aguda, un duelo reciente ni los días en que visita la idea de no estar.</p>'),
 ('Forzar la entrada prematuramente puede llevar a la disociación, el nihilismo o la inflación espiritual.</p>\n',
  'Forzar la entrada prematuramente puede llevar a la disociación, el nihilismo o la inflación espiritual.</p>\n' + arq(
   'Que hay más posibilidades de las que ves desde tu línea, y que no las inventas sino que despiertas a ellas, se despliega en <em>El Campo</em>, Libro 1 de <em>Arquitectura del Destino</em>, Umbral II: «El campo».',
   'libro-01-el-campo/L01-U2.html')),
 ('Las cuatro puertas que el vacío abre hacia Trinity Quantum.', 'Las cuatro puertas que el vacío abre hacia la Red: dos en Trinity Quantum y dos en Trinity Origen.'),
]

def aplicar(nombre, reemplazos):
    with open(os.path.join(SRC, nombre), encoding='utf-8') as f:
        t = f.read()
    for i, (viejo, nuevo) in enumerate(reemplazos, 1):
        if isinstance(viejo, tuple):          # tramo: desde a hasta b, inclusive
            a, b = viejo
            if t.count(a) != 1 or t.count(b) != 1:
                sys.exit(f'{nombre}: el tramo {i} no es único ({t.count(a)}, {t.count(b)}):\n{a[:120]}')
            ia = t.index(a); ib = t.index(b) + len(b)
            if ib <= ia:
                sys.exit(f'{nombre}: el tramo {i} está invertido')
            t = t[:ia] + nuevo + t[ib:]
            continue
        n = t.count(viejo)
        if n != 1:
            sys.exit(f'{nombre}: el reemplazo {i} aparece {n} veces:\n{viejo[:200]}')
        t = t.replace(viejo, nuevo)
    ruta = os.path.join(OUT, nombre)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, 'w', encoding='utf-8') as f:
        f.write(t)
    return len(reemplazos)

if __name__ == '__main__':
    total = 0
    for nombre, reemplazos in R.items():
        n = aplicar(nombre, reemplazos); total += n
        print(f'{nombre}: {n} reemplazos')
    print(f'Total: {total}')
