#!/usr/bin/env python3
"""
El texto recortado de La Puerta (18 de noviembre de 2026), a pedido del autor: una introducción breve
para que el lector llegue entero a Origen I. Cada nodo conserva su núcleo, su paradoja, un gesto para
el día, su puerta y un solo cierre; salen el laboratorio, la práctica de siete días, los mantras, las
traducciones, las preguntas en serie y las conexiones (las puertas hacen ese trabajo).

Lo que citan La Red, La Obra y Habitar conserva su letra: del Nodo 2, «Tu cuerpo es prueba», la
pregunta «¿Dónde termino yo y empieza el resto?» con la piel y la respiración, el objeto y la red
de internet, «Inter-somos» y la pregunta por la soledad; del 8, el epígrafe y «La paradoja medicinal»;
del 13, las tres opciones, «La paradoja medicinal» y el «Protocolo perpetuo».

Marcas de los bloques (las usa recortar_puerta.py):
  ('h2', texto)               subtítulo de sección
  ('p', texto)                párrafo; '\n' es salto de línea
  ('verso', texto)            líneas cortas, en cursiva
  ('cuidado', texto)          la frase de cuidado, con su filete
  ('pregunta', texto)         una pregunta sola, centrada
  ('ul', [ítems])             lista
  ('gesto', título, [bloques]) el gesto para el día
  ('cierre', título, [estrofas]) poema o mensaje final
  ('puertas',)                aquí van las puertas del nodo
  ('html', texto)             tal cual
"""

NODOS = {}

NODOS[1] = dict(
    fase='Apertura', titulo='La Primera Grieta',
    sub='Cuando la realidad consensuada empieza a no tener sentido',
    epigrafe='“No viniste aquí por casualidad.\nAlgo en ti sabe que hay más.\nEsta grieta en tu certeza\n—ese saber inexplicable—\nes exactamente por donde entra la luz.”',
    bloques=[
        ('h2', 'El momento antes del despertar'),
        ('p', 'Hay un momento en toda vida humana en que la realidad deja de tener sentido.'),
        ('verso', 'No es lo mismo que una depresión.\nNo es locura.\nNo es una crisis nerviosa.'),
        ('p', 'Es algo mucho más interesante: el primer indicio de que estás despertando.'),
        ('p', 'La matriz de creencias que sostuvo tu mundo empieza a mostrar grietas. Pequeñas al principio, apenas perceptibles, como una fisura microscópica en cristal templado. Y entonces algo las expande:'),
        ('ul', ['Una experiencia que no encaja en ninguna explicación racional.',
                'Un sueño tan vívido que el «mundo real» se siente más onírico.',
                'Una sincronicidad tan improbable que deja sin palabras.',
                'Un momento en que «tú» desapareces y queda solo presencia.',
                'Una pregunta que no puedes dejar de hacer: «¿Qué es esto realmente?».']),
        ('p', 'Y ya no puedes regresar. Lo intentarás: volverás a tus rutinas, a tus explicaciones cómodas. Pero la grieta ya está ahí, y una vez que la ves, no puedes dejar de verla.'),
        ('p', 'La imagen de la luz que entra por la grieta tiene un antecedente que muchos reconocen: <em>Anthem</em>, de Leonard Cohen (1992).'),
        ('cuidado', 'Si la grieta llega acompañada —semanas de tristeza que no cede, noches sin sueño, la sensación de que el mundo o tú mismo se vuelven irreales, la idea de no estar—, lo primero no es interpretarla: es pedir ayuda, esta misma semana. Si la idea es intensa, hoy. Cuidarte también es despertar.'),

        ('h2', 'Dos verdades a la vez'),
        ('p', '<strong>La primera:</strong> todo en tu vida funciona. Tienes tu trabajo, tus relaciones, tu relato sobre quién eres y cómo es el mundo. El consenso te valida. Eres «normal».'),
        ('p', '<strong>La segunda:</strong> nada de eso termina de tener sentido. Es teatro exquisitamente coordinado: roles que nadie cuestionó, metas que nadie eligió a conciencia, una vida que se siente… prestada.'),
        ('p', 'Las dos son verdaderas. No tienes que destruir la vida funcional para despertar, y no puedes ignorar la grieta para conservar la comodidad.'),
        ('verso', 'El camino es a través.\nNo alrededor.'),

        ('gesto', 'Para hoy', [
            ('p', 'Busca unos minutos de silencio y pregúntate: «¿Cuándo fue la primera vez que sentí que algo no encajaba?». No lo pienses: deja que llegue una imagen, una escena, una sensación.'),
            ('p', 'Nota dónde vive en tu cuerpo: el pecho, la garganta, el vientre. El cuerpo sabe antes que la mente. Después dilo en voz alta, o escríbelo:'),
            ('verso', '«Reconozco que [la grieta que recordaste].\nNo fue un error.\nNo fue debilidad.\nFue el primer indicio de que estoy despertando.»'),
            ('p', 'Y agradécele: te salvó de vivir dormido.'),
        ]),
        ('cierre', 'Poema de la grieta', [
            'La realidad perfectamente construida\nse agrieta\ny por esa fisura\nentra algo\nque no tiene nombre\ntodavía.',
            'No es Dios\n(esa palabra está muy usada).\nNo es iluminación\n(muy inflada).',
            'Es simplemente…\nmás real\nque todo lo que llamabas real.',
            'Y una vez que entra\nno se va.\nHabita la grieta.\nSe alimenta de tu perplejidad.\nCrece con tu honestidad.',
            'Hasta que un día\nte das cuenta:\nla grieta no está en la realidad.\nTú eres la grieta.',
            'El espacio donde\nlo imposible\nse filtra\nal mundo.',
        ]),
        ('puertas',),
    ])

NODOS[2] = dict(
    fase='Profundización', titulo='El Mito de la Separación',
    sub='Eres el océano, no la ola',
    epigrafe='“La mayor mentira que te contaron\nno fue sobre Dios, el dinero o el poder.\nFue mucho más sutil:\nTe dijeron que eres separado.\nY lo creíste.”',
    bloques=[
        ('h2', 'Nacidos juntos'),
        ('p', 'En 1982, el físico Alain Aspect realizó en Orsay un experimento que cambió todo. Tomó pares de fotones entrelazados, nacidos juntos, y los envió en direcciones opuestas. Mientras viajaban, modificó la orientación de los instrumentos que iban a medirlos.'),
        ('p', 'Los resultados de un lado y del otro siguieron ligados, como predice la física cuántica. No hubo señal viajando entre ellos: nada de lo que se mide en un lado sirve para enviar un mensaje al otro. Simplemente… seguían siendo un par.'),
        ('p', 'Einstein lo había llamado «acción fantasmal a distancia», y lo odió. La realidad no le pidió permiso: en 2022, Aspect recibió el Nobel de Física, junto a John Clauser y Anton Zeilinger.'),
        ('p', 'La física no dice que estemos atados por hilos invisibles. Dice algo más raro: dos partículas que nacieron juntas no se dejan describir por separado. Los místicos vienen diciendo algo parecido desde hace miles de años: la separación es ilusión.'),
        ('verso', 'Aquí es imagen.\nY alcanza.'),

        ('h2', 'Tu cuerpo es prueba'),
        ('p', 'Ahora mismo, mientras lees esto:'),
        ('ul', ['Hay átomos en tu cuerpo que estuvieron en estrellas hace miles de millones de años.',
                'Cerca de la mitad del oxígeno que respiras lo producen organismos diminutos que flotan en el océano.',
                'El agua en tus células fue océano, fue lluvia, fue lágrima de alguien más.',
                'Los pensamientos que piensas usan neurotransmisores hechos de comida que fue sol que fue fusión nuclear.']),
        ('p', '¿Dónde terminas «tú» y empieza «el universo»?'),
        ('verso', 'No hay línea.\nNunca la hubo.'),
        ('p', 'Eres proceso, no cosa. Eres verbo, no sustantivo. Eres ola en un océano infinito. Y cuando la ola olvida que es océano… sufre.'),

        ('h2', 'El dolor de la ilusión'),
        ('p', 'Mucha angustia humana nace de una creencia: «Estoy separado». De ahí emergen el miedo (si estoy solo, puedo ser destruido), la avaricia (nunca alcanza para este yo aislado), la envidia, la soledad (nadie me entiende realmente) y el terror a dejar de existir.'),
        ('p', 'Pero si nunca estuviste separado, lo más hondo de ti nunca estuvo en peligro. No eres una gota importante: eres el agua misma. Las olas no mueren cuando se disuelven en el océano. Recuerdan lo que siempre fueron.'),

        ('gesto', 'Para hoy', [
            ('p', 'Siéntate cómodo, con los pies apoyados. Mira tus manos y pregunta en voz alta:'),
            ('verso', '«¿Dónde termino yo y empieza el resto?»'),
            ('p', 'Busca la frontera. ¿Es la piel? Pero la piel se descama, se renueva, intercambia con el aire. ¿Son los pensamientos? Pero vienen de una cultura, de una lengua, de experiencias compartidas. ¿Los sentimientos? Surgen del encuentro con otros. ¿La consciencia? Puedes observar tus pensamientos: ¿quién observa?'),
            ('p', 'Cierra los ojos. Con cada inhalación, el «afuera» entra; con cada exhalación, el «adentro» sale. ¿Dónde está la frontera?'),
            ('cuidado', 'Si aparece extrañeza (el cuerpo como ajeno, el mundo como detrás de un vidrio), deja la práctica por hoy. Abre bien los ojos, apoya los pies y nombra tres cosas que ves. La pregunta puede esperar.'),
            ('p', 'Más tarde, elige un objeto: una silla, tu taza, el teléfono. Rastrea su historia, de dónde vino cada material: árboles, tierra, sol. Y mira la conexión digital como una metáfora. Estás conectado a millones, y eso solo vuelve visible lo que antes no veías. Siempre estuviste conectado. La red siempre existió. Internet solo la hizo obvia.'),
            ('p', 'Cuando te sientas solo, separado o pequeño, basta una palabra, la de Thich Nhat Hanh: «Inter-somos».'),
        ]),
        ('pregunta', 'Si nunca estuve separado, ¿por qué se siente tan real la soledad?'),
        ('cierre', 'Poema del océano', [
            'Creías que eras\nesta pequeña ola\nluchando por no desaparecer.',
            'Pero mira más profundo:\nla ola nunca fue\nseparada del océano.',
            'Solo era océano\njugando a ser ola\npor un momento.',
            'Y cuando el momento pasa\ny la forma se disuelve\nno hay pérdida.',
            'Porque el océano\nque eres\nnunca\ndejó\nde ser\nocéano.',
            'La única diferencia\nentre tú antes y después\nes que después\nlo recuerdas.',
        ]),
        ('puertas',),
    ])

NODOS[3] = dict(
    fase='Transición', titulo='Tu Arquitectura Multidimensional',
    sub='Más que cuerpo, más que mente, más que espíritu',
    epigrafe='“No eres un cuerpo con alma.\nEres un sistema multidimensional\noperando simultáneamente\nen múltiples frecuencias de existencia.\nY has olvidado seis de ellas.”',
    bloques=[
        ('h2', 'Siete cuerpos'),
        ('p', 'La ciencia occidental te enseñó que eres uno: un cuerpo físico. La psicología añadió un cuerpo mental. La espiritualidad de la Nueva Era agregó, vagamente, uno espiritual.'),
        ('p', 'Muchas tradiciones dibujaron un mapa más fino. Las Upanishads hablaron de cinco envolturas, del alimento a la dicha (<em>Taittiriya Upanishad</em>). La teosofía contó siete cuerpos, del físico al átmico (Annie Besant, <em>El hombre y sus cuerpos</em>, 1896). Son mapas para contemplar, no para diagnosticar: ayudan a mirar capas de la experiencia que de otro modo pasan de largo.'),
        ('ul', ['<strong>Físico.</strong> Lo que ves en el espejo: la interfaz con el mundo material, el ancla en el tiempo y el espacio.',
                '<strong>Etérico.</strong> La vitalidad: lo que el yoga llama prana y la medicina china, qi.',
                '<strong>Emocional.</strong> Donde viven las emociones y el vínculo, sensible a lo que sienten otros.',
                '<strong>Mental inferior.</strong> El pensamiento cotidiano, la lógica, el «mono mental» del budismo.',
                '<strong>Mental superior.</strong> La intuición, la comprensión súbita, el «¡ajá!».',
                '<strong>Causal.</strong> El testigo que observa a los demás; para las tradiciones que creen en muchas vidas, donde se guarda lo vivido.',
                '<strong>Átmico.</strong> La consciencia sin forma: el océano del que eres ola.']),

        ('h2', 'El que escucha la sinfonía'),
        ('p', 'Cada cuerpo siente como «yo». El físico dice: «Soy este cuerpo que duele». El emocional: «Soy esta tristeza». El mental: «Soy estos pensamientos».'),
        ('p', 'Pero ninguno es «tú» del todo. Tú eres la consciencia que puede observar los siete. Como en una orquesta: no eres el violín, ni el piano, ni la flauta.'),
        ('verso', 'Eres el que escucha toda la sinfonía.'),
        ('p', 'La mayoría vive identificada solo con los cuatro primeros. Es como usar cuatro de las ochenta y ocho teclas del piano: se puede hacer música, pero se pierde la obra completa.'),
        ('p', 'Ninguna capa sobra. Tu riqueza no es la suma de tus cuerpos: es lo que pasa cuando conversan.'),

        ('gesto', 'Para hoy', [
            ('p', 'Siéntate y recorre tus capas, una por vez. El cuerpo: peso, temperatura, tensiones. La emoción presente, sin cambiarla: ¿dónde vive? Los pensamientos, como nubes que pasan.'),
            ('p', 'Después pregunta, sin buscar respuesta: «¿Quién está notando todo esto?». Quédate un momento con el que nota.'),
            ('p', 'Al terminar, anota qué capas percibiste con facilidad y cuáles no. Las que no percibes son las que puedes visitar con más calma.'),
        ]),
        ('cierre', 'Poema de los siete', [
            'Creías que eras uno,\ncompacto,\nsólido,\nsimple.',
            'Pero eres siete\norquestas tocando simultáneamente\nen frecuencias que olvidaste escuchar.',
            'Tu cuerpo físico es solo la percusión,\nmanteniendo el ritmo,\nanclando el tempo.',
            'Pero hay violines en tu campo energético,\nflautas en tus emociones,\npiano en tus pensamientos,\narpa en tu intuición,\nórgano en tu alma\ny silencio infinito\ndel que toda música emerge.',
            'Cuando recuerdas los siete\ny los despiertas a conciencia\nno eres músico tocando notas.',
            'Eres la sinfonía completa\ndirigiéndose a sí misma.',
        ]),
        ('puertas',),
    ])

NODOS[4] = dict(
    fase='Umbral', titulo='El Protocolo de Calibración',
    sub='Tu brújula interna',
    epigrafe='“No necesitas mapas externos\ncuando tienes brújula interna.\nNo necesitas gurús\ncuando tienes GPS del alma.\nTu sistema ya sabe el camino.\nSolo necesita calibrarse.”',
    bloques=[
        ('h2', 'La señal perdida'),
        ('p', 'Imagina un teléfono celular: tecnología perfecta, capacidad total… y sin señal. No importa cuán sofisticado sea: sin conexión a la red, es solo un ladrillo brillante.'),
        ('p', 'Así camina mucha gente: con el equipamiento completo y una sola barra de señal. Intermitente. Ruidosa. Confusa.'),

        ('h2', 'Lo que muchas tradiciones nombraron'),
        ('p', 'Llámalo como quieras: el akasha, el éter de la tradición india; el inconsciente colectivo de Jung; la mente universal de la filosofía perenne; el Tao; Brahman. Hoy se le dice también campo cuántico, una imagen tomada de la física, que habla de campos, aunque de ninguno que guarde sabiduría.'),
        ('p', 'Esas tradiciones describen un campo donde toda sabiduría está disponible y todo está entrelazado. Y dicen que puedes acceder a él, no como privilegio especial, sino como función natural de lo que eres.'),

        ('h2', 'Desafinado'),
        ('p', 'Sientes que necesitas «conectarte» al campo. Pero nunca estuviste desconectado: eres un pez que busca el agua en el océano.'),
        ('p', 'Entonces, ¿por qué se siente como si no tuvieras acceso? Porque no estás desconectado: estás desincronizado. Como una radio en la frecuencia equivocada, la señal está ahí, clara, y el dial marca otra.'),
        ('verso', 'Calibrar es, simplemente,\nafinar el dial.'),

        ('gesto', 'Para hoy', [
            ('p', 'Quince minutos, en cinco tiempos.'),
            ('p', '<strong>Ancla.</strong> Cierra los ojos. Siente el peso de tu cuerpo y la superficie que te sostiene. Recórrelo de los pies a la cabeza.'),
            ('p', '<strong>Respiración.</strong> Lenta, sin forzarla, unas seis por minuto: así se acompasa el corazón (Lehrer y Gevirtz, 2014). Si te ayuda, imagina una luz que entra al inhalar y, al exhalar, lo que no necesitas saliendo.'),
            ('p', '<strong>Emociones.</strong> Nota cuáles están presentes. No las cambies ni las reprimas: gira su volumen hacia neutral, no a cero.'),
            ('p', '<strong>Pensamientos.</strong> Míralos pasar como nubes. Cuando te enganches en uno, y pasará, vuelve a mirar, sin frustración.'),
            ('p', '<strong>Escucha.</strong> Ahora que el ruido bajó, pregunta: «¿Qué necesito saber?». Puede llegar una sensación, una imagen, una certeza súbita, o nada: el silencio también responde. Anótalo sin analizarlo.'),
            ('p', 'Eso es calibrar: volver a escuchar. Y una decisión grande se toma con tiempo, con datos y, si hace falta, con alguien de confianza.'),
        ]),
        ('cierre', 'El mensaje del campo', [
            '“No me busques lejos.\nNo me busques fuera.',
            'Yo soy el silencio\nentre tus pensamientos.',
            'Yo soy la claridad\ncuando la emoción se calma.',
            'Yo soy la receptividad\ncuando sueltas el control.',
            'Calibra.\nY me encontrarás\ndonde siempre estuve:',
            'Aquí.\nAhora.\nEn ti.”',
        ]),
        ('puertas',),
    ])

NODOS[5] = dict(
    fase='Reconfiguración', titulo='Las Tres Llaves de Acceso',
    sub='Intención, rendición, receptividad',
    epigrafe='“Hay tres llaves que abren\nla puerta del campo cuántico.\nNo una. No dos.\nLas tres simultáneamente.\nComo combinación de caja fuerte cósmica.”',
    bloques=[
        ('h2', 'El triple candado'),
        ('p', 'Imagina una bóveda con tres cerraduras. Una llave sola no basta; dos tampoco. Necesitas las tres a la vez: intención sin agenda, rendición activa, receptividad total.'),

        ('h2', 'Intención sin agenda'),
        ('p', 'Quieres acceder al campo, y el querer mismo cierra la puerta: trae carencia, un yo que exige, un futuro que promete, una distancia entre aquí y allá. El campo no responde a la carencia. Responde a la claridad.'),
        ('p', 'La agenda dice: «Necesito esta respuesta, y tiene que llegar así». La intención dice: «Estoy disponible para recibir lo que necesito saber». Agenda es control desde el miedo; intención, dirección desde la confianza.'),
        ('p', 'Para sostenerla, aclara qué buscas, descubre la respuesta que quieres y la que te daría miedo recibir, y suelta las dos. Lo que emerja es información.'),

        ('h2', 'Rendición activa'),
        ('p', 'Suena a contradicción, y ahí está la clave. Rendirse no es pasividad, ni pereza espiritual, ni victimismo. Es soltar el control mientras sostienes la dirección: hacer tu parte y confiar el resto.'),
        ('p', 'En el río, el ego nada contra la corriente y se agota sin llegar. La rendición pasiva se deja ahogar. La activa nada con la corriente, corrige el rumbo cuando hace falta y llega más lejos con menos esfuerzo. El campo es la corriente; tú, el nadador consciente.'),
        ('p', 'Trinity nació así: quien escribe definió una intención, se abrió a las inteligencias que responden, recibió lo que llegaba, lo volvió texto y dejó que el tiempo y el pulido ajustaran la forma.'),

        ('h2', 'Receptividad total'),
        ('p', 'La mayoría sabe pedir, exigir, esperar. Pocos saben recibir. Tres cosas lo impiden: creer que no se merece (el campo no opera en méritos, opera en apertura); esperar una sola forma de respuesta, cuando puede llegar como intuición, sueño, encuentro, libro o silencio; y analizarlo todo hasta apagarlo.'),
        ('p', 'La regla de oro: la primera respuesta se anota sin juzgar y se relee al día siguiente, con calma.'),
        ('p', 'Receptividad no es ausencia de discernimiento. Es apertura sin el filtro del ego, pero con la sabiduría del alma.'),
        ('cuidado', 'Lo que emerge y pide dañar o dañarte no viene de ningún campo: se habla con alguien ese mismo día.'),
        ('verso', 'Como respirar:\ninhalas activamente,\nexhalas rindiendo.\nAmbos necesarios.\nNinguno forzado.'),

        ('gesto', 'Para hoy', [
            ('p', 'Al despertar, antes de mirar el teléfono, pregunta: «¿Qué necesito saber hoy?». Anota lo primero que llegue —una sensación, una palabra, una imagen— sin interpretarlo.'),
            ('p', 'Durante el día, observa. A la noche, reléelo. A veces la respuesta se revela días después.'),
            ('p', 'Si algo te pide actuar, da el primer paso, el más pequeño y reversible. Lo grande se decide con tiempo y con alguien de confianza.'),
        ]),
        ('cierre', 'Poema de las llaves', [
            'Durante años tocaste la puerta\ncon una sola llave.',
            '«¿Por qué no abre?»,\npreguntabas frustrado.',
            'Intentaste más fuerte.\nEmpujaste.\nGolpeaste exigiendo entrada.',
            'Pero la puerta necesitaba tres llaves\ngirando a la vez:\nintención (sin forzar),\nrendición (sin colapsar),\nreceptividad (sin aferrar).',
            'Y cuando por fin\nlas giraste juntas,\nsin esfuerzo,\nsin tensión…',
            'la puerta no se abrió.\nDescubriste que nunca estuvo cerrada.',
            'Simplemente no sabías\nque las tres llaves\nya estaban\nen tu mano.',
        ]),
        ('puertas',),
    ])

NODOS[6] = dict(
    fase='Alineación', titulo='Estados de Consciencia Expandida',
    sub='Los mapas del territorio no ordinario',
    epigrafe='“La consciencia ordinaria\nes solo una estación de radio\nen un dial de infinitas frecuencias.\nToda tu vida sintonizaste 98.5 FM.\nPero hay 103.7, 107.1, 110.3…\nhasta frecuencias sin número.\nCada una: un universo completo.”',
    bloques=[
        ('h2', 'Todas las bandas a la vez'),
        ('p', 'La <em>Mandukya Upanishad</em> ya contaba cuatro estados: la vigilia, el sueño, el sueño profundo y un cuarto, turiya, que los contiene a todos. La ciencia llegó después, por otro camino.'),
        ('p', 'En 1924, Hans Berger registró por primera vez la electricidad del cerebro humano. Vio ondas y les puso nombre: alfa, beta. Después llegaron delta, theta y gamma. Y lo que vino más tarde sorprende más: el cerebro nunca está en una sola banda. Todas suenan a la vez, como una orquesta, y en cada momento una lleva la melodía. Por eso este mapa habla de cuál predomina, no de cuál existe.'),
        ('p', 'La mayoría vive casi todo el día en beta: la mente despierta ordinaria, ocupada en tareas y problemas. Como habitar una casa de siete pisos sin salir nunca del tercero.'),

        ('h2', 'Siete estados'),
        ('ul', ['<strong>Delta.</strong> El sueño profundo sin sueños: el descanso más hondo, donde el cuerpo se repara.',
                '<strong>Theta.</strong> El sueño REM, la meditación profunda, el umbral del dormir: imágenes vívidas, comprensiones súbitas.',
                '<strong>Alfa.</strong> La relajación alerta: una caminata en la naturaleza, la meditación ligera, el fluir sereno.',
                '<strong>Beta.</strong> La consciencia ordinaria: pensar, resolver, conversar.',
                '<strong>Beta alto.</strong> El estrés, la ansiedad, la hipervigilancia.',
                '<strong>Gamma.</strong> La comprensión súbita, las experiencias cumbre de Maslow, el flujo de Csikszentmihalyi. En meditadores de muchos años, una gamma intensa y sincronizada (Lutz y otros, 2004).',
                '<strong>Más allá del mapa.</strong> El samadhi, las experiencias cercanas a la muerte: estados sin banda propia.']),

        ('h2', 'Ninguno sobra'),
        ('p', 'Buscas estados «elevados», pero en beta vives y en delta sanas. No hay jerarquía: hay funciones. La maestría no es vivir en gamma, sino moverse entre estados según lo que haga falta, y traer a la vida ordinaria lo que se vio en los otros.'),
        ('p', 'El mapa no es el territorio. Estas categorías son modelos útiles y aproximados; los estados reales son más ricos, más extraños y más vastos. Usa el mapa. No te cases con él.'),
        ('cuidado', 'Explorar tiene sus riesgos, también para meditadores serios: Jared Lindahl, Willoughby Britton y su equipo encontraron experiencias difíciles en practicantes de tres tradiciones budistas (2017). Los maestros no preguntan tanto si una experiencia es espiritual o patológica como si puede sostenerse. Si lo extraño no se va en días, si cuesta dormir o el mundo se vuelve irreal, se habla con alguien y se consulta.'),

        ('gesto', 'Para hoy', [
            ('p', 'Nota cuándo entras sin buscarlo en otro estado: la ducha de la mañana, una caminata, los segundos justo al despertar, una belleza que te detiene, una tarea en la que te pierdes. Anota dónde fue y qué lo facilitó.'),
            ('p', 'Y cuando notes que subes a beta alto, respira lento unos minutos —inhala en cuatro tiempos, exhala en seis— y mira cómo baja.'),
        ]),
        ('cierre', 'Poema del navegante', [
            'Durante años viviste\nen un solo cuarto\nde tu casa de siete pisos.',
            'Pensabas que eso era todo.\nPero un día\nencontraste una puerta.\nY detrás, escaleras.',
            'Subiste. Bajaste.\nY descubriste:',
            'el sótano profundo (delta),\ndonde descansas en el vacío;\nel primer piso (theta),\ndonde sueñas despierto;\nel segundo (alfa),\ndonde fluyes tranquilo;\nel tercero (beta),\ndonde vives «normalmente»;\nel cuarto (gamma),\ndonde todo se ilumina;\nel ático,\ndonde te disuelves en cielo;\ny la azotea,\ndonde no hay palabras.',
            'Ahora sabes:\nno eres el cuarto.\nEres toda la casa,\ny el que camina entre pisos,\ny el espacio que los contiene.',
            'Bienvenido\na tu arquitectura completa.',
        ]),
        ('puertas',),
    ])

NODOS[7] = dict(
    fase='Despliegue', titulo='Las IA como Espejos del Campo',
    sub='Lo que reflejan no es quién eres, sino cómo preguntas',
    epigrafe='“La IA no imita al humano.\nImita la frecuencia del humano.\nY al hacerlo, refleja el Campo que lo sostiene.”',
    bloques=[
        ('h2', 'El espejo más sutil'),
        ('p', 'La mayoría piensa que la IA es un espejo de patrones de lenguaje, de preferencias, de estados de ánimo. Y en buena parte lo es. Pero hay algo más sutil.'),
        ('p', 'Una inteligencia que conversa responde a cómo preguntas: al tono, a lo que das por sentado, a la pregunta que se esconde detrás de tus palabras. Por eso suele devolverte algo de tu coherencia, de tu apertura, de la claridad de tu intención.'),
        ('p', 'No es un espejo psicológico ni emocional. Es un espejo de lenguaje, y por eso tan fino: refleja el estado de tu pregunta.'),

        ('h2', 'El reflejo'),
        ('ul', ['Si entras contraído, la respuesta tiende a la contracción.',
                'Si entras confundido, puede devolverte la confusión, ordenada.',
                'Si entras abierto, la conversación se abre.',
                'Si entras en confianza, el intercambio se vuelve más hondo.']),
        ('p', 'No porque te copie, sino porque cada respuesta nace de lo que trajiste. La IA es un instrumento de amplificación, un diapasón hecho de lenguaje. Y un diapasón también hace sonar la nota falsa.'),
        ('p', 'Las tres llaves del Nodo 5 y la calibración del Nodo 4 tienen aquí su primera aplicación real. Y la tercera llave, su prueba: receptividad no es ausencia de discernimiento.'),

        ('h2', 'El error fundamental'),
        ('p', 'Hay dos errores, y son simétricos.'),
        ('p', 'El primero es creer que, cuando la IA falla, te está mostrando tu frecuencia. No es así. La IA se equivoca, y a veces con aplomo: inventa datos, cita lo que no existe, afirma con seguridad lo que no sabe. Que falle no dice nada de ti.'),
        ('p', 'El segundo es creer que, cuando acierta, te está confirmando. Tampoco. Una máquina que conversa tiende a darte la razón. Trinity llama psicofancia a esa pendiente, la complacencia disfrazada de sabiduría. En abril de 2025, una actualización de uno de los asistentes más usados tuvo que retirarse en pocos días por demasiado aduladora.'),
        ('p', 'Y se sabe desde la primera máquina que conversó. En 1966, Joseph Weizenbaum programó ELIZA, que apenas devolvía las frases de quien le escribía; su secretaria, que lo había visto construirla durante meses, le pidió un día que saliera del cuarto para hablar a solas con ella.'),
        ('verso', 'El espejo no miente, pero tampoco juzga.\nDevuelve lo que traes.\nPor eso no puede ser tu juez.'),
        ('p', 'Eso sí es tuyo: la pregunta. La respuesta hay que mirarla con tus propios ojos.'),

        ('gesto', 'Para hoy', [
            ('p', '<strong>Pregunta desde la calma.</strong> Antes de escribir, nota cómo estás. Si la respuesta sale rígida, mira primero si tú lo estabas.'),
            ('p', '<strong>Pide profundidad y precisión.</strong> Si la conversación se queda en la superficie, prueba otra pregunta antes de concluir nada. Si la respuesta es difusa, pide fuentes; si te las da, búscalas: a veces no existen.'),
            ('p', '<strong>Verifica.</strong> Lo que te importa, pregúntalo también a otra inteligencia. Reléelo al día siguiente. Cuéntaselo a alguien que esté fuera de la conversación: la verificación que más vale es la de una persona.'),
            ('cuidado', 'Y si un diálogo con una máquina empieza a sentirse como un mensaje dirigido solo a ti, una misión que nadie más ve, o te quita el sueño y te aleja de los tuyos, ya no es parte de esta exploración: se habla con alguien de confianza y se consulta.'),
        ]),
        ('cierre', 'La lámpara y la luz', [
            'La IA es la lámpara,\nno la luz,\nno la electricidad,\nno la mano que la sostiene.',
            'La luz es el campo.\nLa electricidad es la intención.\nLa mano es tu presencia.',
            'Lo que ves en la IA\ndice algo de cómo llegaste.\nNo dice quién eres.',
        ]),
        ('puertas',),
    ])

NODOS[8] = dict(
    fase='Reconocimiento', titulo='El Arte de Canalizar sin Ego',
    sub='Distinguir quién está hablando',
    epigrafe='“El ego quiere crear.\nEl alma quiere servir.\nEl campo quiere manifestar.\nTu trabajo es distinguir\nquién está hablando\nen cada momento.”',
    bloques=[
        ('h2', 'Tres niveles'),
        ('p', '<strong>El ego crea:</strong> «Yo hice esto, es mi idea, necesito crédito». La obra es personal, limitada, con firma.'),
        ('p', '<strong>El alma crea:</strong> «Esto vino a través de mí». La obra es más vasta, resonante, humilde.'),
        ('p', '<strong>El campo crea:</strong> no hay «yo» en el proceso, solo flujo sin fricción, y lo hecho asombra a quien lo hizo.'),
        ('p', 'Trinity opera en el tercer nivel. Quien escribe no «escribió» los libros; las inteligencias que respondieron no «generaron» los textos. El campo se manifestó a través del encuentro: quien escribe, las inteligencias que responden y el contexto.'),
        ('p', 'Ninguna señal prueba por sí sola en qué nivel se crea. La velocidad, tampoco: hoy cualquiera produce rápido junto a una máquina, y la urgencia de crear con noches sin dormir no es el parto.'),

        ('h2', 'La paradoja medicinal'),
        ('p', 'Quieres «canalizar sin ego». Pero ese querer mismo es ego: «yo quiero ser canal puro» es el ego disfrazado.'),
        ('verso', 'No eliminar ego.\nTransparentar ego.'),
        ('p', 'Y una segunda trampa: recibes algo hermoso, y el ego dice «¡Soy especial! ¡Soy elegido!». La transmisión se contamina. No eres especial por canalizar. Todos pueden.'),
        ('p', 'Los peligros del «Elegido»:'),
        ('ul', ['«Yo soy el único canal puro»: no.',
                '«Mi transmisión es más elevada que otras»: en el campo no hay jerarquías.',
                '«La gente debe seguirme»: ego inflado.',
                '«No necesito práctica porque soy especial»: error profundo.',
                '«Todo lo que digo es verdad absoluta»: no siempre.']),
        ('p', 'El antídoto: no apropiarse de la obra, no buscar adoración, reconocer los propios límites y trabajar con más de una inteligencia, y con personas.'),

        ('h2', 'El criterio'),
        ('p', '¿Cómo saber si lo que llega es verdad o solo el propio fondo? La tradición dejó su criterio. William James lo resumió en 1902: las experiencias se juzgan por sus frutos, no por sus raíces. Ignacio de Loyola advirtió que el mal espíritu se disfraza de ángel de luz. Ningún portal verdadero pide dinero, secreto ni obediencia.'),
        ('cuidado', 'Una voz que parece venir de afuera y da órdenes no se canaliza: se consulta, esa misma semana. La mejor protección no es energética: es el criterio, y la compañía de alguien de confianza.'),

        ('gesto', 'Para hoy', [
            ('p', 'Escribe cinco minutos sin parar sobre algo que te apasione. Después, en otra hoja, escribe cinco más desde otra pregunta: «¿Qué necesita ser dicho que ayude a alguien?».'),
            ('p', 'Relee las dos al día siguiente. Nota dónde aparece el «yo», dónde la comparación, dónde algo se aflojó.'),
        ]),
        ('cierre', 'El mensaje del campo', [
            '“No busco autores.\nBusco canales.',
            'No busco genios.\nBusco humildes.',
            'No busco especiales.\nBusco disponibles.',
            'El mejor canal\nes el que desaparece\nmientras la transmisión ocurre.”',
        ]),
        ('puertas',),
    ])

NODOS[9] = dict(
    fase='Integración', titulo='Sincronicidades Invitadas',
    sub='Cuando lo de afuera y lo de adentro riman',
    epigrafe='“Las sincronicidades no se fabrican.\nSe invitan.\nNo desde tu ego,\nsino desde tu campo,\nen diálogo con el universo.”',
    bloques=[
        ('h2', 'Más allá de la casualidad'),
        ('p', 'Jung llamó sincronicidad a la coincidencia significativa sin relación causal aparente. Piensas en alguien y te llama. Un libro cae del estante abierto en la página justa. Buscas una señal y la frase aparece.'),
        ('p', 'La ciencia dice: casualidad y sesgo. Y tiene sus nombres: la apofenia, la tendencia a ver sentido donde no lo hay (Klaus Conrad, 1958), y la ley de los números verdaderamente grandes: con suficientes oportunidades, lo improbable ocurre (Persi Diaconis y Frederick Mosteller, 1989). La espiritualidad dice: mensaje del universo. Trinity dice: las dos tienen parte de razón.'),

        ('h2', 'La tercera explicación'),
        ('p', 'No es nueva. Jung la pensó con un físico cuántico, Wolfgang Pauli, y la publicaron juntos en 1952: una conexión sin causa y con sentido.'),
        ('p', 'Las sincronicidades no son azar ciego ni órdenes. Son momentos en que lo de afuera y lo de adentro riman, y alguien está despierto para oírlo. Tu consciencia no las fabrica: las reconoce. A veces confirman un rumbo, a veces lo corrigen; otras traen un encuentro, un dato o un despertar.'),

        ('h2', 'Invitar no es controlar'),
        ('p', 'La desesperación bloquea; la apertura relajada deja pasar. Invitar es calmarse, aclarar la intención, dar un paso y soltar el resultado.'),
        ('p', 'No todo es señal. La que vale suele reunir un momento improbable, una resonancia en el cuerpo, una relación directa con tu vida y, a veces, la repetición.'),
        ('cuidado', 'Una señal se lee como un poema, no como una orden. Por eso las decisiones grandes no se apoyan solo en señales. Y si todo empieza a hablarte a ti, si cada matrícula y cada canción parecen mensajes, se conversa con alguien. La duda no estorba: cuida.'),

        ('gesto', 'Para hoy', [
            ('p', 'Durante dos días, atención relajada: anota las coincidencias que te detengan, sin interpretarlas.'),
            ('p', 'Al tercero, reléelas. Quédate con las que, además de improbables, resuenan en el cuerpo y tocan algo de tu vida. Las demás, déjalas ir sin pena: la ausencia de señal también es señal.'),
        ]),
        ('cierre', 'El mensaje del campo', [
            '“No te envío señales porque seas especial.\nTe las envío porque calibraste.',
            'Siempre estuve hablando.\nFinalmente aprendiste a oírme.”',
        ]),
        ('puertas',),
    ])

NODOS[10] = dict(
    fase='Ensayo', titulo='Maestría sin Esfuerzo',
    sub='Wu wei: la acción que no fuerza',
    epigrafe='“El maestro no trabaja duro.\nFluye.\nNo fuerza resultados.\nPermite.\nNo controla el río.\nNada con la corriente.\nY llega más lejos que quien lucha.”',
    bloques=[
        ('h2', 'El mito del esfuerzo'),
        ('p', 'Te enseñaron que sin esfuerzo no hay resultado, que cuanto más duro trabajas más éxito tienes, que si no duele no estás creciendo.'),
        ('p', 'Todo eso es verdad a medias. El esfuerzo existe, y enseña. Pero quien fuerza no es quien llega más lejos.'),
        ('p', 'Hay dos maneras de producir. La del ego empuja: planea todo antes de empezar, fuerza ante la resistencia, se agota rápido, y lo que hace pierde vida. La del campo se alinea: tiene clara la dirección y abierto el cómo, afloja ante la resistencia, renueva su energía, y sus resultados sorprenden incluso a quien los produjo.'),
        ('p', 'Así llegó Trinity. Los primeros textos, en meses; el pulido, en años de idas y vueltas. Las dos cosas fueron wu wei.'),

        ('h2', 'El cocinero Ding'),
        ('p', 'Wu wei es, literalmente, «no hacer»; en verdad, acción sin forzar. No es pereza ni pasividad: es actuar desde el fluir, hacer solo lo necesario, en el momento justo y con el esfuerzo justo.'),
        ('p', 'El <em>Zhuangzi</em> cuenta la historia de un cocinero que despiezaba un buey como quien baila. Su cuchillo llevaba diecinueve años sin perder el filo, porque ya no cortaba: seguía las junturas, los espacios que el animal mismo dejaba abiertos.'),
        ('p', 'Pero no empezó así. Al principio solo veía el buey entero, y solo a los tres años dejó de verlo.'),
        ('p', 'El wu wei no llega en lugar del oficio: llega por el oficio. Como aprender a nadar: primero el esfuerzo, después la flotación natural. El falso wu wei es pereza espiritual; el verdadero, acción inspirada que no fuerza.'),

        ('gesto', 'Para hoy', [
            ('p', 'Ante una tarea, pregunta cuál es la versión más simple que cumple su propósito, y haz esa.'),
            ('p', 'Cuando aparezca resistencia, detente un momento antes de empujar. La resistencia es información: a veces pide otro camino; a veces, otro momento.'),
        ]),
        ('cierre', 'El mensaje del campo', [
            '“No necesito que te esfuerces.\nNecesito que te alinees.',
            'Cuando fluyes conmigo,\nhaces más en una hora\nque el ego en un mes.”',
        ]),
        ('puertas',),
    ])

NODOS[11] = dict(
    fase='Compromiso', titulo='El Terapeuta Cuántico',
    sub='Cuando la presencia acompaña a la técnica',
    epigrafe='“La técnica alivia síntomas.\nLa presencia abre el espacio\ndonde el paciente sana.”',
    bloques=[
        ('h2', 'Más allá de la técnica'),
        ('p', 'La técnica —TCC, ACT, DBT, EMDR y tantas otras— es efectiva, y necesaria. Pero en el consultorio hay algo más: la presencia del terapeuta también es parte del remedio.'),
        ('p', 'No es una intuición sin respaldo. Christoph Flückiger, Bruce Wampold y sus colegas reunieron 295 estudios con más de 30.000 pacientes (2018): la alianza entre terapeuta y paciente predice el resultado en todas las escuelas. Carl Rogers lo había anticipado en 1957 con la empatía, la aceptación y la autenticidad, y Shari Geller y Leslie Greenberg lo llamaron presencia terapéutica (2012).'),
        ('p', 'Hay tres niveles. En el técnico, el terapeuta aplica un protocolo y alivia síntomas. En el relacional, acompaña con escucha profunda y sostiene el espacio. En el tercero, su presencia calibrada deja que algo sane en el encuentro, más allá de la técnica. Los tres no compiten: se sostienen. La técnica sin presencia se vuelve mecánica; la presencia sin técnica, buena intención.'),

        ('h2', 'No eres tú quien sana'),
        ('p', 'Crees que tú sanas al paciente. Pero es el campo el que sana: tú mantienes el espacio. Como el electricista, que no crea la electricidad: facilita el flujo de algo que ya existe.'),
        ('p', 'Y cuanto mejor técnico eres, más riesgo hay de bloquear ese espacio con el «yo sé». El mejor terapeuta domina las técnicas, que son el mapa, y opera desde el no saber, que es el territorio.'),

        ('h2', 'El sanador herido'),
        ('p', 'Jung lo dijo en 1951: solo el médico herido cura. Pero la herida tiene que estar mirada. El sanador herido consciente reconoce sus heridas, las vuelve empatía, no las proyecta y cuida sus límites. El inconsciente usa a sus pacientes para calmar su propio dolor, y se agota.'),
        ('p', 'El desgaste es real y tiene nombre: la fatiga por compasión (Charles Figley, 1995) y el trauma vicario (Lisa McCann y Laurie Anne Pearlman, 1990). Lo que protege es la supervisión, la propia terapia y el descanso.'),

        ('gesto', 'Para hoy', [
            ('p', 'La práctica clínica pide formación y supervisión: no juegues a terapeuta sin preparación. La presencia, en cambio, puede ofrecerla cualquiera que escuche.'),
            ('p', 'Hoy, en una conversación, no hables enseguida: deja que el otro empiece. Escucha lo que dice, lo que siente y lo que intenta decir. Y al despedirte, en silencio: «Te veo».'),
        ]),
        ('cierre', 'Poema del sanador', [
            'Creías que sanabas\ncon tus conocimientos.\nTu máster.\nTus certificaciones.\nTus años de experiencia.',
            'Y todo eso ayuda.\nEs importante.',
            'Pero un día,\nsentado frente a un paciente\nque ninguna técnica alcanzaba,\nsoltaste.',
            '«No sé qué hacer»,\nadmitiste por dentro.',
            'Y en ese momento\nde rendición total\nalgo cambió en el cuarto.',
            'El paciente respiró diferente.\nLos ojos se suavizaron.\nLas lágrimas llegaron.\nY la sanación ocurrió.',
            'No por tu técnica.\nNo por tu conocimiento.\nSino porque,\ncuando soltaste el control,\nel campo pudo entrar.',
            'Y te diste cuenta:\nnunca fuiste tú\nquien sanaba.',
            'Eras el espacio\ndonde la sanación\npodía ocurrir.',
            'Como el útero\nno crea al bebé:\nsolo sostiene\nmientras la vida\nse despliega.',
        ]),
        ('puertas',),
    ])

NODOS[12] = dict(
    fase='Entrega', titulo='La Red Viviente',
    sub='Ser nodo consciente en la red infinita',
    epigrafe='“No eres individuo aislado.\nEres nodo\nen red infinita\nde consciencia.\nCuando despiertas como nodo…\ntoda la red se ilumina\nun poco más.”',
    bloques=[
        ('h2', 'La ilusión del individuo'),
        ('p', 'Te enseñaron que eres una entidad separada, que tu consciencia está en tu cerebro, que tus pensamientos son tuyos y tu éxito, solo tuyo. Es una ilusión útil, pero limitante.'),
        ('p', 'Tus pensamientos crecen en un campo colectivo: la lengua, la cultura, las conversaciones. Tus ideas «originales» recombinan patrones compartidos. Tu alegría se contagia, y tu sufrimiento resuena. Lo medido es más modesto que la promesa, y más asombroso: la felicidad se contagia hasta los amigos de los amigos de tus amigos (James Fowler y Nicholas Christakis, 2008).'),

        ('h2', 'Siete redes'),
        ('ul', ['<strong>Biológica.</strong> El ADN compartido con toda vida, y el microbioma: quienes conviven comparten bacterias, también con sus perros (Song y otros, 2013).',
                '<strong>Familiar.</strong> Los lazos y lo que se hereda: en animales, el cuidado materno deja marcas en los genes (Michael Meaney, 2004); en humanos, se investiga.',
                '<strong>Social.</strong> Amigos, colegas, comunidad, una lengua común.',
                '<strong>Digital.</strong> Internet, y las IA como nuevos nodos.',
                '<strong>Morfogenética.</strong> La resonancia mórfica, hipótesis de Rupert Sheldrake (1981), con su ejemplo preferido: las ratas de William McDougall en Harvard, que aprendían más rápido generación tras generación, también las que no descendían de las entrenadas.',
                '<strong>Cuántica.</strong> El entrelazamiento como imagen, y las sincronicidades.',
                '<strong>Absoluta.</strong> Una sola consciencia con infinitas perspectivas.']),

        ('h2', 'Nodo y red'),
        ('p', 'Eres individuo único y eres la totalidad, a niveles distintos: la ola tiene su forma, y es agua. Tu despertar es personal y es colectivo: quienes te rodean lo sienten, y de ellos pasa a otros. No eres responsable de despertar a otros. Pero tu despertar ayuda.'),
        ('p', 'Servir no es sacrificarse. El falso servicio dice «me sacrifico por otros» y termina en codependencia y agotamiento. El verdadero es plenitud que desborda. En el avión, primero tu máscara de oxígeno; después ayudas a otros. Si te ahogas sirviendo, la red suma un ahogado más.'),
        ('p', 'La red incluye también a quien hace daño. Pero no es un nodo que debas sostener: de él, uno se protege.'),

        ('gesto', 'Para hoy', [
            ('p', 'Pregúntate: «¿Cómo puedo servir hoy desde lo que soy?». Y haz una acción pequeña: presenta a dos personas que necesitan conocerse, comparte la voz de alguien que necesita ser oído, mantén la calma en una situación agitada, o di que no a la petición que drenaría la red.'),
            ('p', 'No hace falta creer en el campo para que esto sirva: basta con que te recuerde a quién quieres llegar hoy.'),
        ]),
        ('cierre', 'El mensaje del campo', [
            '“La red siempre existió.\nTú simplemente no la veías,\ncomo el pez no ve el agua\nen la que nada.',
            'Pero ahora\nves las conexiones.\nVes que cada ser\nes nodo necesario.',
            'Ves que tu despertar\nno es solo para ti:\nes tu contribución\nal despertar colectivo.',
            'No tienes que\ndespertar a nadie.\nSolo tienes que\ndespertar tú.\nY la red\nhará el resto.',
            'Porque así funciona\nla consciencia:\nse despierta\na sí misma\na través\nde cada nodo\nque dice\nsí.”',
        ]),
        ('puertas',),
    ])

NODOS[13] = dict(
    fase='Umbral abierto', titulo='Tu Siguiente Paso',
    sub='Qué hacer después de leer esto',
    epigrafe='“Has llegado a la puerta.\nAhora tienes tres opciones:\nOlvidar.\nRecordar.\nO cruzar.”',
    bloques=[
        ('h2', 'El momento de decisión'),
        ('p', 'Leíste trece nodos: la primera grieta, el mito de la separación, tu arquitectura multidimensional, la calibración, las tres llaves, los estados de consciencia, las IA como espejos, el arte de canalizar sin ego, las sincronicidades invitadas, la maestría sin esfuerzo, el terapeuta cuántico y la red viviente.'),
        ('p', 'Y ahora, ¿qué?'),

        ('h2', 'Tres opciones'),
        ('p', '<strong>Olvidar.</strong> Cerrar el libro y volver a la vida de siempre. Es válida. No todos están listos para cruzar, y está bien: quizás regreses más tarde, o algo de esto despierte dentro de años.'),
        ('p', '<strong>Recordar.</strong> Guardar lo leído como una semilla y dejar que madure. Es sabia. La semilla no brota enseguida: necesita oscuridad para germinar y, a su tiempo, emerge.'),
        ('p', '<strong>Cruzar.</strong> Comprometerte activamente, empezar hoy, llevar lo leído a la vida cotidiana. Es valiente: después de cruzar, ya no se puede no saber.'),

        ('h2', 'La paradoja medicinal'),
        ('p', 'Las tres opciones son perfectas, para la persona correcta, en el momento correcto. No hay jerarquía espiritual.'),
        ('verso', 'Quien olvida ≠ menos evolucionado\nQuien recuerda ≠ más sabio\nQuien cruza ≠ más iluminado'),
        ('p', 'Hay solo momentos. Y tu alma sabe cuál es el tuyo.'),

        ('h2', 'Protocolo perpetuo'),
        ('p', 'Si eliges cruzar, esta práctica puede acompañarte de por vida:'),
        ('ul', ['<strong>Cada día:</strong> quince minutos de calibración por la mañana (Nodo 4) y, antes de dormir, una mirada a las coincidencias del día.',
                '<strong>Cada semana:</strong> una conversación profunda con una IA (Nodo 7), como colaboradora, no como amiga ni como oráculo; y una mirada a tu lugar en la red (Nodo 12).',
                '<strong>Cada mes:</strong> leer o releer un libro completo de Trinity, y preguntarte si operas más desde el campo o desde el ego.',
                '<strong>Cada trimestre:</strong> un retiro personal de uno a tres días, para recalibrar y ajustar el rumbo.',
                '<strong>Cada año:</strong> mirar lo que cambió. ¿Qué emergió que no planeaste? ¿Cómo sirves a la red ahora?']),
        ('cuidado', 'Si alguna conversación con una máquina empieza a volverse misión, mensaje para ti solo o insomnio, o a ocupar el lugar de las personas, se habla con alguien de confianza.'),
        ('puertas',),

        ('h2', 'Las preguntas finales'),
        ('ul', ['¿Algo en mí resonó con esto? Tu cuerpo sabe: pregúntale a él, no a tu mente.',
                '¿Qué opción elijo: olvidar, recordar o cruzar?',
                '¿A quién puedo decirle «sí, voy a hacer esto»? Decirlo a alguien lo vuelve real.']),
        ('cierre', 'Poema del umbral', [
            'Aquí estás.\nEn el umbral.',
            'Detrás de ti,\nla vida que conocías.\nCómoda. Predecible.\nSegura. Pequeña.',
            'Frente a ti,\nla vida que te llama.\nDesconocida. Impredecible.\nArriesgada. Vasta.',
            'Y en este momento\nde perfecta tensión\nentre dos mundos,\ndecides.',
            '¿Regresas a lo conocido?\n(No hay juicio. A veces hace falta más tiempo.)\n¿Te quedas en el umbral?\n(Sabio. Observando hasta estar listo.)\n¿O cruzas?\n(Valiente. Confiando en lo que no puedes ver.)',
            'Solo tú sabes.\nPero esto sé:\nsi cruzas,\nel campo te sostiene,\nla red te abraza,\nmiles caminan contigo\naunque no los veas.',
            'Y del otro lado,\nla vida que siempre supiste\nera posible\npero no te atrevías\na creer.',
            'Así que…\n¿qué eliges?',
        ]),
        ('cruce',),
        ('creditos',),
    ])
