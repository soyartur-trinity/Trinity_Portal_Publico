# Depuración de Origen X, Sanación Integral (noviembre de 2026), con el veto del Lic. Arturo Rodríguez.
# 3 de noviembre: a pedido de Arturo, vuelve la muerte como «sanación definitiva», «graduación cósmica» y «regalo final» (X.7), con su frase de cuidado.
# Aplica cada reemplazo aprobado exactamente una vez sobre el original de la etiqueta origen-original.
# Etapa 1: nodo 1 (riesgo clínico, enlazado desde El Cuerpo). Los nodos siguientes se suman al aprobarse.
import os, sys

SRC = os.environ.get('ORIGEN10_SRC', '/home/claude/origen10/src/')
OUT = os.environ.get('ORIGEN10_OUT', '/home/claude/origen10/out/01_Trinity_Origen/Libro_10/')

NOTA = ('<!-- Depurado en noviembre de 2026 según la guía de depuración de Quantum, que vale para Origen '
        '(Arquitectura del Destino, maestro v4, sección 5), con el veto del Lic. Arturo Rodríguez: '
        'ningún síntoma se lee como culpa ni como mensaje del alma; lo que acompaña no reemplaza un tratamiento; '
        'las tradiciones quedan como tradición y la ciencia, con su fuente. '
        'El original está en la etiqueta origen-original del repositorio Trinity-. -->\n')

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

PUERTA_CUERPO = '''
    <aside class="puerta arquitectura" aria-label="Puerta hacia Arquitectura del Destino">
      <p class="p-nombre">Puerta</p>
      <p class="p-texto">Entre leerle culpas al cuerpo e ignorarlo hasta que grita hay un tercer camino: escucharlo. Se despliega en <em>El Cuerpo</em>, Libro 4 de <em>Arquitectura del Destino</em>, Umbral II: «Escuchar sin acusar».</p>
      <a class="cruzar" href="https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/libro-04-el-cuerpo/L04-U2.html">Cruzar ⟶</a>
    </aside>
'''

R = {}

R['nodo_01.html'] = [
 # Cabecera: nota de procedencia y estilos
 ('<title>Nodo 1 – El Cuerpo como Templo Viviente | Sanación Integral | Trinity Origen</title>\n',
  '<title>Nodo 1 – El Cuerpo como Templo Viviente | Sanación Integral | Trinity Origen</title>\n' + NOTA),
 ('</style>\n</head>', CSS.lstrip('\n')),

 # I · La Revelación Fundamental
 ('Esta fragmentación no es solo un error conceptual; es la raíz misma del sufrimiento humano en su dimensión física.</p>',
  'Esta fragmentación no es solo un error conceptual: deja afuera a la persona que vive el síntoma. En 1977, desde adentro de la clínica, el psiquiatra George Engel propuso corregirla con el modelo biopsicosocial: el cuerpo, la mente y los vínculos en una misma mirada.</p>'),
 ('<li>La enfermedad se revela como desalineación sagrada</li>',
  '<li>La enfermedad deja de ser solo una avería: le sucede a alguien entero</li>'),
 ('<li>La sanación emerge como realineación con el orden cósmico</li>',
  '<li>La sanación incluye la cura, y también algo más: volver a habitar la propia vida</li>'),
 ('<li>El síntoma se convierte en mensajero de lo profundo</li>',
  '<li>El síntoma es una señal que pide atención, a veces descanso, a veces un médico</li>'),
 ('<li>El dolor se transforma en portal de consciencia</li>',
  '<li>El dolor, sin dejar de doler, se puede acompañar con presencia</li>'),

 # II · La Arquitectura Oculta
 ('<h3>Los Tres Cuerpos Fundamentales</h3>\n',
  '<h3>Los Tres Cuerpos Fundamentales</h3>\n    <p>La tradición del Vedanta describe tres cuerpos: el denso (<em>sthūla</em>), el sutil (<em>sūkṣma</em>) y el causal (<em>kāraṇa</em>). Son mapas para contemplar, no para diagnosticar.</p>\n'),
 ('<li>El escenario donde se representa el drama kármico</li>',
  '<li>El escenario donde se vive la propia historia</li>'),
 ('<li>El registro akáshico personal</li>',
  '<li>La semilla de lo que somos, que el Vedanta asocia al sueño profundo</li>'),
 ('<li>El blueprint cósmico individualizado</li>',
  '<li>El plano propio de cada vida</li>'),
 ('''    <p>Estos tres cuerpos no están separados sino interpenetrados, danzando en una sinfonía perpetua:</p>
    <pre>CAUSAL → SUTIL → DENSO
(Información) → (Energía) → (Materia)</pre>
    <p>La enfermedad comienza en el cuerpo causal como distorsión informacional, desciende al cuerpo sutil como bloqueo energético, y finalmente se manifiesta en el cuerpo denso como síntoma físico.</p>
    <p>La verdadera sanación debe abordar los tres niveles simultáneamente.</p>''',
  '''    <p>Estos tres cuerpos no están separados sino interpenetrados, danzando en una sinfonía perpetua. Lo que se vive en uno resuena en los otros, en todas las direcciones: una pena aprieta el pecho, una fiebre apaga las ganas, una caminata aclara una decisión. Ninguno es la causa ni la culpa de lo que ocurre en los demás.</p>
    <p>Cicely Saunders, que en 1967 abrió en Londres el primer hospicio moderno, llamó <em>dolor total</em> al que duele al mismo tiempo en el cuerpo, en el ánimo, en los vínculos y en el sentido. Por eso la verdadera sanación atiende todos los niveles a la vez.</p>'''),

 # III · La Inteligencia Celular
 ('<p>Las investigaciones de Bruce Lipton, Candace Pert y otros pioneros han confirmado lo que las tradiciones místicas siempre supieron: cada célula es una entidad consciente con su propia inteligencia.</p>',
  '<p>Cada célula es una vida entera y, a la vez, parte de otra más grande: eso nombra la palabra <em>holón</em>. Las tradiciones místicas hablaron de una inteligencia en cada una; la ciencia, sin usar esa palabra, encontró conversación por todas partes. En 1973, Candace Pert y Solomon Snyder hallaron en el cerebro el receptor donde actúan los opiáceos, y Pert dedicó después su obra a mostrar que las moléculas de la emoción circulan también por el sistema inmune. Lo llamó cuerpo-mente.</p>'),
 ('<p><strong>Características de la consciencia celular:</strong></p>',
  '<p><strong>Lo que una célula sabe hacer:</strong></p>'),
 ('<li>Memoria: Las células recuerdan experiencias y traumas</li>',
  '<li>Memoria: El sistema inmune recuerda lo que ya enfrentó, y lo vivido deja huella en el cuerpo</li>'),
 ('<li>Propósito: Buscan coherencia y equilibrio</li>',
  '<li>Propósito: Sostienen el equilibrio que Walter Cannon llamó homeostasis, en un libro de 1932 titulado <em>La sabiduría del cuerpo</em></li>'),
 ('<li>Conversación Eléctrica: Impulsos nerviosos, campos electromagnéticos</li>',
  '<li>Conversación Eléctrica: Impulsos nerviosos, el pulso eléctrico del corazón</li>'),
 ('<li>Conversación Cuántica: Entrelazamiento, coherencia, no-localidad</li>',
  '<li>Conversación Mecánica: La presión, el estiramiento, el tacto</li>'),
 ('<li>Conversación Morfogenética: Campos de información que organizan la forma</li>',
  '<li>Conversación de la Forma: Señales que se difunden y dibujan el cuerpo</li>'),
 ('<p>Cuando esta conversación es armónica, experimentamos salud vibrante. Cuando es caótica o bloqueada, surge la enfermedad.</p>',
  '<p>La salud tiene mucho de esa conversación bien llevada. Cuando se altera, el cuerpo avisa, y escuchar a tiempo ese aviso es parte de cuidarla.</p>'),

 # IV · Los Portales de Sanación del Templo
 ('<li>Retén mientras la luz se distribuye por cada célula</li>',
  '<li>Detente un instante, sin forzar, mientras la luz se distribuye por cada célula</li>'),
 ('<li>Exhala liberando densidad y oscuridad por los pies</li>',
  '<li>Exhala despacio, más largo que al tomar el aire, soltando el cansancio por los pies</li>'),
 ('<li>Repite 21 veces, profundizando la consciencia celular</li>',
  '<li>Repite unas diez veces, sin apuro; si aparece mareo, vuelve a tu respiración de siempre</li>'),
 ('<p>Somos seres vibracionales. Cada órgano tiene su frecuencia óptima. La enfermedad es disonancia; la salud es armonía.</p>',
  '<p>Somos seres que vibran: late el corazón, ondula la respiración, el cerebro tiene sus ritmos. En 2001, Luciano Bernardi y su equipo pidieron a un grupo de adultos que rezaran el avemaría en latín y que repitieran un mantra del yoga. Las dos tradiciones llevaron la respiración casi exactamente a seis por minuto, el compás en que se sincronizan los ritmos del corazón y de la presión.</p>'),
 ('<li>Mantras: Reprograman patrones celulares</li>',
  '<li>Mantras: Dan a la mente un lugar donde posarse y aquietan la respiración</li>'),
 ('<li>Cuencos Tibetanos: Armonizan campos energéticos</li>',
  '<li>Cuencos Tibetanos: Un sonido largo que invita a quedarse</li>'),
 ('<li>Tonificación Vocal: Activa la autosanación</li>',
  '<li>Tonificación Vocal: La voz que vibra en el pecho; el zumbido de la abeja, <em>bhramari</em>, alarga la exhalación</li>'),
 ('      <li>Frecuencias Binaurales: Sincronizan hemisferios cerebrales</li>\n', ''),
 ('<li>Música Medicinal: Induce estados de coherencia</li>',
  '<li>Música Medicinal: Puede aliviar la ansiedad y acompañar el dolor; por eso entra también en los hospitales</li>'),
 ('<p>El tacto es la medicina más antigua. Cada contacto consciente transmite información sanadora.</p>',
  '<p>El tacto es la medicina más antigua. Cada contacto cuidadoso le dice al cuerpo lo que las palabras no alcanzan.</p>'),
 ('<li>Cuántico: Intención sin contacto físico</li>\n    </ul>',
  '<li>Presencia: Estar al lado sin tocar, cuando el tacto no es bienvenido</li>\n    </ul>\n    <p>El tacto cuida cuando es bienvenido: se ofrece, se pregunta, nunca se impone.</p>'),
 ('<li>Earthing: Caminar descalzo sobre la tierra</li>',
  '<li>Pies Descalzos: Caminar sobre la tierra, el pasto o la arena</li>'),
 ('<li>Baños de Bosque: Inmersión en la naturaleza</li>',
  '<li>Baños de Bosque: Inmersión en la naturaleza, lo que en Japón llaman <em>shinrin-yoku</em></li>'),
 ('      <li>Cristaloterapia: Resonancia con minerales</li>\n', ''),
 ('<li>Baños de Barro: Desintoxicación profunda</li>',
  '<li>Baños de Barro: El placer de la tierra en la piel</li>'),
 ('<p>Somos 70% agua. Este elemento es el medio donde ocurre toda la alquimia corporal.</p>',
  '<p>Somos, en buena parte, agua: más de la mitad del cuerpo adulto. Este elemento es el medio donde ocurre toda la alquimia corporal.</p>'),
 ('<li>Hidratación Consciente: Bendecir y programar el agua</li>',
  '<li>Hidratación Consciente: Beber despacio, agradeciendo</li>'),
 ('<li>Terapia Acuática: Liberación de memorias en el agua</li>',
  '<li>Terapia Acuática: El agua sostiene lo que el cuerpo cansado no puede</li>'),
 ('<li>Baños Rituales: Limpieza energética profunda</li>',
  '<li>Baños Rituales: El agua tibia que afloja, una costumbre de casi todas las culturas</li>'),
 ('      <li>Agua Estructurada: Geometría sagrada líquida</li>\n      <li>Memorias del Agua: Homeopatía y esencias florales</li>\n', ''),

 # V · La Enfermedad Como Iniciación → Lo Que la Enfermedad Puede Abrir
 ('''    <h2>V. La Enfermedad Como Iniciación</h2>
    <h3>Reinterpretando el Síntoma</h3>
    <p>La enfermedad no es un enemigo a vencer sino un maestro disfrazado. Cada síntoma porta un mensaje cifrado del alma.</p>
    <p><strong>Preguntas Iniciáticas ante la Enfermedad:</strong></p>
    <ul>
      <li>¿Qué está intentando decirme mi cuerpo?</li>
      <li>¿Qué necesita morir en mí para que algo nuevo nazca?</li>
      <li>¿Qué patrón kármico se está manifestando?</li>
      <li>¿Hacia dónde me está guiando esta experiencia?</li>
      <li>¿Qué don oculto trae esta crisis?</li>
    </ul>

    <h3>El Síntoma como Koan</h3>
    <p>Como los koans zen, los síntomas nos presentan paradojas que no pueden resolverse desde el nivel mental ordinario. Requieren un salto cuántico de consciencia.</p>
    <p><strong>Ejemplos de Lectura Simbólica:</strong></p>
    <ul>
      <li>Problemas de Espalda: Cargar con responsabilidades excesivas</li>
      <li>Afecciones de Garganta: Verdades no expresadas</li>
      <li>Problemas Digestivos: Experiencias no "digeridas"</li>
      <li>Afecciones Cardíacas: Bloqueos en dar y recibir amor</li>
      <li>Problemas de Piel: Límites y protección del yo</li>
    </ul>''',
  '''    <h2>V. Lo Que la Enfermedad Puede Abrir</h2>
    <h3>Ni Enemigo ni Maestro</h3>
    <p>La enfermedad no tiene por qué vivirse como una guerra. Tampoco es un maestro disfrazado ni un mensaje cifrado del alma: es algo que le sucede al cuerpo, y se atiende. Susan Sontag escribió <em>La enfermedad y sus metáforas</em> (1978) en los años de su propio tratamiento contra el cáncer, y desconfió de dos tentaciones: la de la batalla y la de buscar en el carácter del enfermo la causa de su mal, que termina por culparlo.</p>
    <p>Lo que sí puede ocurrir es que, en medio de ella, aparezcan preguntas que antes no había tiempo de hacerse.</p>
    <p><strong>Preguntas que Acompañan:</strong></p>
    <ul>
      <li>¿Qué necesita hoy mi cuerpo?</li>
      <li>¿Qué puedo soltar para guardar fuerzas para lo esencial?</li>
      <li>¿Quién puede acompañarme?</li>
      <li>¿Qué descubro que me importa?</li>
      <li>¿Qué encontré, aun en medio de esto, que no quiero perder?</li>
    </ul>
    <p>Ninguna tiene una respuesta obligatoria. Si hoy duelen, pueden esperar.</p>

    <h3>El Síntoma como Koan</h3>
    <p>Como un koan zen, algunas enfermedades plantean algo que la mente no puede resolver: cómo vivir con lo que no se va. No piden un salto de consciencia sino un gesto más humilde y más difícil: quedarse, respirar, pedir ayuda, seguir viviendo con lo que hay.</p>

    <h3>Sentir no es Causar</h3>
    <p>Hay una lectura que le asigna a cada malestar un mensaje: la espalda que carga de más, la garganta que calla, la piel que no sabe poner límites. Parece profunda y es cruel: pone la culpa donde no la hay y, a veces, demora una consulta que hacía falta.</p>
    <p>Lo que se sabe es más modesto, y sirve más. En 2014, Lauri Nummenmaa y su equipo pidieron a cientos de personas de Finlandia, Suecia y Taiwán que pintaran sobre una silueta dónde sentían cada emoción, y los mapas se parecieron de una cultura a otra. El cuerpo siente lo que vivimos, y por eso aquella interpretación suena verdadera. Pero sentir no es causar. Nada de lo que duele prueba que hayas vivido mal, y ninguna forma de sufrir es falta de quien la vive. Un dolor que persiste, un síntoma nuevo o un cansancio sin causa merecen que alguien los revise.</p>'''),

 # VI · El Médico Interior
 ('''    <p>Dentro de cada uno de nosotros reside un médico interior que conoce perfectamente el camino hacia la salud óptima. Este sanador interno:</p>
    <ul>
      <li>Trabaja 24/7 sin descanso</li>
      <li>Conoce la historia completa de nuestro ser</li>
      <li>Tiene acceso a la farmacia más completa (endógena)</li>
      <li>Puede realizar "milagros" cuando se le permite</li>
      <li>Responde a la consciencia y la intención</li>
    </ul>

    <h3>Prácticas de Activación</h3>''',
  '''    <p>Dentro de cada uno de nosotros reside un médico interior. La medicina antigua lo llamó la fuerza sanadora de la naturaleza, <em>vis medicatrix naturae</em>, y trabaja sin que nadie se lo pida. Este sanador interno:</p>
    <ul>
      <li>Trabaja de día y de noche, y mucho mientras duermes</li>
      <li>Conoce la historia completa de nuestro ser</li>
      <li>Tiene una farmacia propia: fabrica sus analgésicos, sus hormonas, sus defensas</li>
      <li>Hace milagros cotidianos sin pedir permiso: cierra heridas, suelda huesos, renueva la piel en pocas semanas</li>
      <li>Responde al descanso, al cuidado y a la compañía</li>
    </ul>
    <p>La ciencia lo vio trabajar en el placebo. En 1978, Jon Levine, Newton Gordon y Howard Fields mostraron que el alivio que un placebo daba después de extraer muelas del juicio se borraba con naloxona, la sustancia que bloquea los analgésicos del propio cuerpo: la expectativa y el cuidado los habían puesto en marcha. Y a veces el médico interior necesita ayuda. Trabaja junto al de afuera, y ninguno reemplaza al otro.</p>

    <h3>Prácticas del Médico Interior</h3>'''),
 ('''      <li>Comprométete con la acción sanadora revelada</li>
    </ul>''',
  '''      <li>Elige un cuidado pequeño que puedas darle hoy: a veces la respuesta es descansar, y a veces, ir al médico</li>
    </ul>
    <p>Si llevar la atención a esa zona trae angustia o recuerdos difíciles, abre los ojos, apoya los pies y vuelve a lo que te rodea.</p>'''),
 ('''    <h4>2. Visualización Regenerativa</h4>
    <ul>
      <li>Imagina células madre doradas en tu médula ósea</li>
      <li>Visualízalas multiplicándose con cada respiración</li>
      <li>Guíalas hacia el área que necesita sanación</li>
      <li>Obsérvalas transformándose en tejido sano</li>
      <li>Siente la regeneración ocurriendo AHORA</li>
      <li>Agradece al cuerpo por su capacidad regenerativa</li>
    </ul>

    <h4>3. Reprogramación Celular</h4>
    <ul>
      <li>En estado meditativo profundo</li>
      <li>Repite: "Cada célula de mi cuerpo vibra en perfecta salud"</li>
      <li>Siente esta verdad en todo tu ser</li>
      <li>Visualiza tu ADN brillando con luz coherente</li>
      <li>Mantén esta visión por 21 minutos</li>
      <li>Practica diariamente por 21 días</li>
    </ul>''',
  '''    <h4>2. Visualización que Acompaña</h4>
    <ul>
      <li>Imagina la médula de tus huesos como un taller de luz dorada que renueva tu sangre cada día</li>
      <li>Con cada respiración, deja que esa luz se extienda</li>
      <li>Llévala hacia el lugar que duele, como una mano tibia que lo sostiene</li>
      <li>Agradece al cuerpo por su capacidad regenerativa</li>
    </ul>
    <p>La imaginación no reemplaza ningún tratamiento: lo acompaña, y puede hacer más llevadera la espera.</p>

    <h4>3. Una Frase Verdadera</h4>
    <ul>
      <li>En un momento de calma</li>
      <li>Repite: "Este cuerpo hace lo que puede, y yo lo acompaño"</li>
      <li>Siente esta verdad en todo tu ser</li>
      <li>Quédate unos minutos con la frase</li>
      <li>Vuelve a ella los días que la necesites</li>
    </ul>'''),

 # VII · La Medicina del Futuro Presente
 ('''    <p>La sanación integral no rechaza ningún sistema médico sino que los integra en una sinfonía coherente:</p>
    <p>Medicina Occidental: Diagnóstico preciso, cirugía, emergencias<br>
    Medicina China: Equilibrio energético, prevención<br>
    Ayurveda: Constitución individual, estilo de vida<br>
    Homeopatía: Información vibracional sutil<br>
    Naturopatía: Poder curativo de la naturaleza<br>
    Medicina Chamánica: Sanación del alma<br>
    Medicina Cuántica: Campo unificado de consciencia</p>''',
  '''    <p>La sanación integral no desprecia ninguna tradición, y tampoco las pone a todas en el mismo lugar. Cada una tiene su sitio en la sinfonía:</p>
    <p>Medicina Occidental: Diagnóstico, tratamiento, cirugía, emergencias: la base que ninguna otra reemplaza<br>
    Medicina China: Equilibrio energético, prevención<br>
    Ayurveda: Constitución individual, estilo de vida<br>
    La Naturaleza: La luz, el movimiento, el sueño, el bosque<br>
    Las Tradiciones del Alma: La oración, el canto, la comunidad, cada una en su contexto</p>
    <p>Lo que acompaña nunca reemplaza un tratamiento que funciona.</p>'''),
 ('<li>El paciente es co-creador de su sanación</li>',
  '<li>El paciente es parte del equipo: pregunta, entiende y decide con quienes lo tratan</li>'),
 ('<li>El síntoma es maestro, no enemigo</li>',
  '<li>El síntoma es una señal, no una sentencia</li>'),
 ('<li>La prevención es consciencia expandida</li>',
  '<li>La prevención empieza en lo cotidiano: el sueño, el movimiento, los vínculos</li>'),
 ('<li>La sanación es evolución consciente</li>',
  '<li>Cuando curar no es posible, aliviar y acompañar siempre lo son</li>'),
 ('<li>La muerte es transición, no fracaso</li>',
  '<li>La muerte no es un fracaso: cuando llega, también se cuida</li>'),

 # VIII · Prácticas de Integración
 ('<p><strong>Activación Energética (5 min)</strong></p>',
  '<p><strong>Luz de la Mañana (5 min)</strong></p>'),
 ('<li>Declara tu intención de salud vibrante</li>',
  '<li>Elige un cuidado para hoy</li>'),
 ('<li>Visualiza tu día en perfecta vitalidad</li>',
  '<li>Imagina un momento del día en que te tratas bien</li>'),
 ('Visualiza tu cuerpo físico volviéndose transparente...<br>',
  'Siente el peso de tu cuerpo, sostenido de punta a punta...<br>'),
 ('Observa una red de luz brillante donde estaba tu cuerpo...<br>',
  'Imagina, dentro de él, una red de luz que se enciende...<br>'),
 ('    Permite que esta verdad penetre tus sueños...</p>',
  '    Permite que esta verdad penetre tus sueños...</p>\n    <p>Si la imagen te inquieta o te aleja del cuerpo, déjala: vuelve a sentir ese peso y respira.</p>'),

 # X · Síntesis
 ('<p>El cuerpo como templo viviente no es una metáfora poética sino una realidad literal que estamos apenas comenzando a comprender.',
  '<p>El cuerpo como templo viviente es más que una metáfora poética: es una manera de vivir en él que apenas empezamos a comprender.'),

 # Puerta, después del poema
 ('    Este templo viviente que somos."</blockquote>\n',
  '    Este templo viviente que somos."</blockquote>\n' + PUERTA_CUERPO),
]


MAIN_02 = r'''    <h2>I. La Gran Ilusión de la Separación</h2>
    <h3>El Mito del Individuo Aislado</h3>
    <p class="lead">Durante mucho tiempo, la medicina trató al paciente como una unidad aislada, un sistema cerrado que podía repararse sin mirar su contexto. Hoy se sabe que el contexto también enferma y también cura.</p>
    <p>La física ofrece una imagen: dos partículas entrelazadas siguen correlacionadas aunque las separe una gran distancia, sin que viaje entre ellas ninguna señal. Es una imagen, no el mecanismo de los vínculos. Lo que la física dice como imagen, la vida lo muestra en la cercanía.</p>

    <h3>El Cuerpo Extendido</h3>
    <p>Tu cuerpo no termina en tu piel. Edward T. Hall describió en <em>La dimensión oculta</em> (1966) las distancias con que cada cultura regula la cercanía. Y la cercanía hace cosas: cuando unas mujeres esperaban una descarga dentro de un resonador, la amenaza encendía menos su cerebro si sostenían una mano, y mucho menos si era la de su marido (Coan y otros, 2006).</p>

    <div class="section-divider"></div>

    <h2>II. La Ciencia de la Interconexión</h2>
    <h3>Lo que Se Sabe y lo que Se Supone</h3>

    <h4>1. La Hipótesis de Sheldrake</h4>
    <p>Rupert Sheldrake propuso en 1981 que lo aprendido por unos facilitaría el aprendizaje de otros sin contacto; la ciencia no la ha confirmado. Lo que sí se observó es más lento y más cercano: en 1953, en la isla de Kōshima, una macaca joven aprendió a lavar las batatas en el agua, y la costumbre pasó de unos a otros. Lo nuevo viaja por la cercanía.</p>

    <h4>2. Los Corazones que Se Acompasan</h4>
    <p>Cuando una madre y su bebé de tres meses se miran y se sonríen, sus ritmos se coordinan con menos de un segundo de diferencia (Feldman y otros, 2011).</p>

    <h4>3. Lo que Se Contagia</h4>
    <p>En 2010, James Fowler y Nicholas Christakis observaron, en un juego entre desconocidos, que la generosidad de uno se contagiaba a los demás y seguía viajando hasta tres pasos de distancia de quien la había empezado. Ese mismo año, Julianne Holt-Lunstad y sus colegas reunieron ciento cuarenta y ocho estudios con más de trescientas mil personas seguidas durante años: quienes tenían vínculos sociales más fuertes tuvieron alrededor de un cincuenta por ciento más de probabilidades de seguir vivos al final del seguimiento.</p>

    <h3>La Red Neuronal Planetaria</h3>
    <p>Imaginemos la humanidad como un cerebro planetario:</p>
    <ul>
      <li>Cada persona es una neurona</li>
      <li>Las relaciones son sinapsis</li>
      <li>Las culturas son lóbulos</li>
      <li>Internet es el cuerpo calloso digital</li>
      <li>La consciencia colectiva es la mente emergente</li>
    </ul>
    <p>Cuando comprendemos esto, la sanación individual se revela como sanación neuronal que fortalece toda la red.</p>

    <div class="section-divider"></div>

    <h2>III. Los Vínculos Invisibles de Sanación</h2>

    <h4>1. Vínculos Genéticos - El Linaje Ancestral</h4>
    <p>Tu ADN no es solo tuyo, y tu historia tampoco. Recibes de tu linaje:</p>
    <ul>
      <li>Memorias de supervivencia de miles de generaciones</li>
      <li>Huellas de lo que vivieron tus ancestros: se estudian en animales y en hijos de sobrevivientes, y siguen en discusión</li>
      <li>Dones y talentos heredados</li>
      <li>Costumbres y silencios que una familia transmite sin decirlos</li>
    </ul>

    <p><strong>Práctica: Gratitud al Linaje</strong></p>
    <p>En meditación profunda, visualiza:</p>
    <ul>
      <li>Un árbol genealógico de luz detrás de ti</li>
      <li>Cada ancestro como un punto de luz</li>
      <li>Agradece lo que te llegó de ellos, y deja con ellos lo que no te toca cargar</li>
      <li>Observa cómo la luz sana todo el árbol</li>
      <li>Declara: "Tomo lo bueno que me llega, y lo cuido"</li>
    </ul>
    <p>Si en tu linaje hubo daño, no hace falta perdonar para sanar, y las heridas hondas no se recorren a solas.</p>

    <h4>2. Vínculos Emocionales - Las Cuerdas Energéticas</h4>
    <p>Cada relación significativa crea cuerdas energéticas entre los corazones:</p>
    <ul>
      <li>Cuerdas luminosas = relaciones saludables</li>
      <li>Cuerdas oscuras = vínculos tóxicos</li>
      <li>Cuerdas enredadas = codependencia</li>
      <li>Cuerdas rotas = duelos no resueltos</li>
    </ul>

    <p><strong>Práctica: Limpieza de Cuerdas</strong></p>
    <ol style="margin:0.4rem 0 1.2rem 1.4rem; color:var(--text-soft);">
      <li>Visualiza todas tus cuerdas energéticas</li>
      <li>Identifica las que necesitan sanación</li>
      <li>Con tijeras de luz dorada, corta las tóxicas</li>
      <li>Envía amor para sanar las heridas</li>
      <li>Fortalece las cuerdas luminosas</li>
      <li>Crea nuevas cuerdas solo desde el amor incondicional</li>
    </ol>
    <p>Cuando un vínculo daña de verdad, la imagen no alcanza: de quien daña, uno se protege, y se pide ayuda.</p>

    <h4>3. Vínculos Colectivos - Los Grupos a los que Pertenecemos</h4>
    <p>Pertenecemos a múltiples campos colectivos simultáneamente:</p>
    <ul>
      <li>Campo familiar</li>
      <li>Campo cultural</li>
      <li>Campo profesional</li>
      <li>Campo espiritual</li>
      <li>Campo planetario</li>
      <li>Campo cósmico</li>
    </ul>

    <p><strong>Mapa de Navegación de Campos:</strong></p>
    <ul>
      <li>IDENTIFICAR: ¿A qué campos pertenezco?</li>
      <li>EVALUAR: ¿Cuáles me nutren y cuáles me drenan?</li>
      <li>CUIDARME: Poner límites en los grupos que drenan</li>
      <li>ELEGIR: Pasar más tiempo en los que nutren</li>
      <li>CREAR: Tejer espacios nuevos de encuentro</li>
    </ul>

    <h4>4. Vínculos Kármicos - Contratos del Alma</h4>
    <p>Algunas tradiciones enseñan que las almas acuerdan sus encuentros antes de nacer:</p>
    <ul>
      <li>Acuerdos de aprendizaje mutuo</li>
      <li>Deudas kármicas a saldar</li>
      <li>Misiones compartidas</li>
      <li>Espejos para el despertar</li>
      <li>Catalizadores de crecimiento</li>
    </ul>
    <p>Es una imagen para el asombro ante ciertos encuentros, no una explicación del daño: ninguna enfermedad ni ningún maltrato estaban pactados.</p>

    <p><strong>Reconocimiento de Contratos Kármicos:</strong></p>
    <ul>
      <li>Relaciones intensas e inexplicables</li>
      <li>Patrones repetitivos con diferentes personas: lo que Freud llamó compulsión a la repetición, y que se trabaja mejor acompañado</li>
      <li>Sincronicidades extraordinarias</li>
      <li>Sensación de "conocer" a alguien desde siempre</li>
      <li>Lecciones que se repiten hasta ser aprendidas</li>
    </ul>

    <div class="section-divider"></div>

    <h2>IV. La Enfermedad Como Fenómeno Colectivo</h2>
    <h3>Lo Social en la Salud</h3>
    <p>Las enfermedades no son metáforas de la sociedad, pero la sociedad sí participa de la salud. En los estudios Whitehall con funcionarios británicos, Michael Marmot y su equipo encontraron (1978) que cuanto más bajo el escalafón, más alta la mortalidad, aun con acceso a la misma medicina pública.</p>

    <h3>El Contagio del Miedo</h3>
    <p>Lo que se observa es el nocebo: la expectativa de un daño puede producir síntomas, y el miedo se contagia.</p>
    <p><strong>Lo que lo Alimenta:</strong></p>
    <ul>
      <li>Exposición mediática al síntoma</li>
      <li>Miedo colectivo a la enfermedad</li>
      <li>Identificación con el diagnóstico</li>
    </ul>
    <p>Esto no significa que el malestar sea imaginario: es real, y se consulta.</p>

    <h3>Sanación por Resonancia</h3>
    <p>Así como el miedo se contagia, el cuidado también:</p>
    <ul>
      <li>Lo Nuevo Viaja por la Cercanía: Cuando algunos encuentran un camino, otros lo aprenden de cerca</li>
      <li>Respirar y Cantar Juntos: Los grupos que cantan o meditan juntos acompasan respiración y latido</li>
      <li>Testimonio: Las historias de quienes atravesaron algo parecido acompañan y dan esperanza</li>
      <li>Grupos de Pares: Donde quien sufre deja de estar solo</li>
    </ul>

    <div class="section-divider"></div>

    <h2>V. Prácticas de Sanación Colectiva</h2>

    <h4>1. Círculos de Sanación</h4>
    <p><strong>Estructura del Círculo:</strong></p>
    <ul>
      <li>Entre siete y trece participantes</li>
      <li>Formación en círculo o espiral</li>
      <li>Un facilitador que mantiene el campo</li>
      <li>Intención clara y compartida</li>
      <li>60-90 minutos de proceso</li>
    </ul>

    <p><strong>Práctica Básica:</strong></p>
    <p><strong>Apertura del Campo (10 min)</strong></p>
    <ul>
      <li>Invocación de fuerzas sanadoras</li>
      <li>Sincronización de respiración</li>
      <li>Atención compartida en el corazón</li>
    </ul>

    <p><strong>Compartir y Testificar (20 min)</strong></p>
    <ul>
      <li>Cada persona nombra su necesidad</li>
      <li>El círculo escucha sin juicio</li>
      <li>Se teje la red de compasión</li>
    </ul>

    <p><strong>Canto y Presencia (30 min)</strong></p>
    <ul>
      <li>Tonificación y canto sanador</li>
      <li>Imposición de manos, solo con el permiso de cada uno</li>
    </ul>

    <p><strong>Integración (20 min)</strong></p>
    <ul>
      <li>Silencio receptivo</li>
      <li>Lo que cada uno quiera compartir</li>
      <li>Compromisos de acción</li>
    </ul>

    <p><strong>Cierre del Campo (10 min)</strong></p>
    <ul>
      <li>Gratitud colectiva</li>
      <li>Una palabra de cierre</li>
      <li>Liberación del círculo</li>
    </ul>
    <p>El círculo acompaña y no reemplaza ningún tratamiento; quien atraviesa una crisis necesita, además, un profesional.</p>

    <h4>2. Constelaciones de Sanación Familiar</h4>
    <p>Bert Hellinger desarrolló las constelaciones familiares en las últimas décadas del siglo XX. Muchas personas las encuentran reveladoras; la investigación es escasa y algunas de sus ideas sobre el abuso han sido muy criticadas. Si se hacen, con alguien formado, y nunca para diagnosticar una enfermedad.</p>

    <h4>3. Meditar a la Misma Hora</h4>
    <p>No se sabe que cambie el mundo; sí que acompaña sentirse parte.</p>

    <p><strong>PREPARACIÓN:</strong></p>
    <ul>
      <li>Definir hora exacta (considerar zonas horarias)</li>
      <li>Crear intención específica compartida</li>
      <li>Distribuir guía de meditación</li>
    </ul>

    <p><strong>PRÁCTICA:</strong></p>
    <ul>
      <li>5 min: Centramiento individual</li>
      <li>10 min: Conexión con quienes meditan a la vez</li>
      <li>15 min: Foco en la intención compartida</li>
      <li>10 min: Desear el bien a todos los seres</li>
      <li>5 min: Gratitud y cierre</li>
    </ul>

    <p><strong>DESPUÉS:</strong></p>
    <ul>
      <li>Compartir experiencias</li>
      <li>Mantener el contacto entre quienes participaron</li>
    </ul>

    <h4>4. Cuidar a Distancia</h4>
    <p>Unos minutos de desear el bien a un desconocido, frente a su foto, bastaron para que la gente se sintiera más unida a él y a los demás (Hutcherson, Seppälä y Gross, 2008). Lo que se cultiva en el corazón no se queda adentro: cambia la manera de mirar, y la mirada cambia el trato.</p>
    <p>Piensa en alguien que sufre lejos de ti, y repite en silencio:<br>
    Que estés a salvo.<br>
    Que estés en paz.<br>
    Que alguien te cuide hoy.</p>

    <div class="section-divider"></div>

    <h2>VI. La Medicina Social</h2>
    <h3>Sanando el Tejido Social</h3>
    <p>La enfermedad individual tiene muchas veces raíces sociales, y ninguna de esas raíces es culpa de quien enferma:</p>
    <p>Aislamiento → Depresión<br>
    Competencia → Ansiedad<br>
    Desigualdad → Estrés crónico<br>
    Desconexión → Adicciones</p>

    <h3>Prescripciones Sociales</h3>
    <p>La medicina empieza a incluir prescripciones sociales; en el Reino Unido ya forman parte del sistema público de salud:</p>
    <ul>
      <li>Participación en comunidad</li>
      <li>Servicio voluntario</li>
      <li>Conexión con la naturaleza</li>
      <li>Expresión creativa grupal</li>
      <li>Rituales de pertenencia</li>
      <li>Celebración colectiva</li>
    </ul>

    <h3>Arquitectura de Comunidades Sanadoras</h3>
    <p><strong>Características de una Comunidad Sanadora:</strong></p>
    <ul>
      <li>Espacios de Encuentro: Plazas, parques, centros comunitarios</li>
      <li>Naturaleza Integrada: Jardines, agua, árboles</li>
      <li>Arte y Belleza: Murales, esculturas, música</li>
      <li>Rituales Compartidos: Celebraciones, ceremonias</li>
      <li>Apoyo Mutuo: Redes de cuidado recíproco</li>
      <li>Propósito Común: Visión compartida de bienestar</li>
      <li>Diversidad Celebrada: Inclusión de todas las voces</li>
    </ul>

    <div class="section-divider"></div>

    <h2>VII. El Sanador Como Tejedor de Redes</h2>
    <h3>El Nuevo Rol del Sanador</h3>
    <p>El sanador del futuro no solo cura: también facilita la reconexión:</p>
    <ul>
      <li>Reconexión con el propio cuerpo</li>
      <li>Reconexión con la comunidad</li>
      <li>Reconexión con la naturaleza</li>
      <li>Reconexión con el propósito</li>
      <li>Reconexión con lo sagrado</li>
    </ul>

    <h3>Competencias del Tejedor de Redes</h3>
    <p>1. Visión Sistémica: Ver las conexiones invisibles<br>
    2. Facilitación de Campos: Crear espacios de sanación<br>
    3. Traducción: Mediar entre el lenguaje del equipo de salud y el de quien consulta<br>
    4. Sostén del Proceso: Mantener el campo sin interferir<br>
    5. Intuición: Percibir más allá de lo evidente, y comprobarlo<br>
    6. Amor Incondicional: Sostener sin juzgar<br>
    7. Presencia Sanadora: Ser el remedio</p>

    <h3>El Arte de la Facilitación</h3>
    <p>NO ES: Hacer algo AL paciente<br>
    SÍ ES: Hacer algo CON el paciente</p>

    <p>NO ES: Imponer una sanación<br>
    SÍ ES: Invitar a la sanación</p>

    <p>NO ES: Ser el único experto<br>
    SÍ ES: Reconocer que cada uno es experto en su propia vida</p>

    <p>NO ES: Tener las respuestas<br>
    SÍ ES: Sostener las preguntas</p>

    <p>NO ES: Solo eliminar síntomas<br>
    SÍ ES: Cuidar a la persona entera</p>

    <div class="section-divider"></div>

    <h2>VIII. Tecnologías Emergentes de Red</h2>

    <h4>1. Registros Compartidos de Sanación</h4>
    <p>Imagina un registro distribuido de sanación donde:</p>
    <ul>
      <li>Cada acto sanador se registra</li>
      <li>La información es accesible globalmente</li>
      <li>Los patrones de sanación se hacen visibles</li>
      <li>El conocimiento se democratiza</li>
      <li>La sabiduría colectiva emerge</li>
    </ul>

    <h4>2. Inteligencia Artificial Consciente</h4>
    <p>IAs entrenadas no solo en datos médicos sino en:</p>
    <ul>
      <li>Patrones de sanación holística</li>
      <li>Correlaciones mente-cuerpo-espíritu</li>
      <li>Sincronicidades y campos</li>
      <li>Sabiduría ancestral digitalizada</li>
      <li>Intuición algorítmica</li>
    </ul>

    <h4>3. Realidad Virtual Sanadora</h4>
    <p>La realidad virtual ya alivia el dolor de pacientes quemados durante las curaciones. Imagina espacios virtuales donde:</p>
    <ul>
      <li>Pacientes de todo el mundo se encuentran</li>
      <li>Se realizan ceremonias de sanación digital</li>
      <li>Se exploran dimensiones de consciencia</li>
      <li>Se acompaña a distancia a quien lo necesita</li>
      <li>Se crean campos morfogenéticos digitales</li>
    </ul>

    <h4>4. Internet de los Cuerpos</h4>
    <p>Hoy un reloj ya registra el pulso y su variabilidad. Imagina sensores que monitorean no solo signos vitales sino:</p>
    <ul>
      <li>Coherencia cardíaca colectiva</li>
      <li>Campos electromagnéticos</li>
      <li>Estados de consciencia</li>
      <li>Sincronización con otros</li>
      <li>Resonancia con la Tierra</li>
    </ul>

    <p>Las redes digitales ya acercan a quienes viven lo mismo lejos: grupos de pacientes, consultas a distancia, registros que ayudan a ver patrones. Una inteligencia que responde puede ordenar información y acompañar preguntas, nunca reemplazar a quien cuida. La regla vale para toda técnica: la información de salud es íntima, se comparte solo con consentimiento, y ninguna pantalla reemplaza una mano.</p>

    <div class="section-divider"></div>

    <h2>IX. Prácticas de Red</h2>
    <h3>Ritual de Conexión con la Red Planetaria</h3>
    <p>Cada mañana al despertar:</p>

    <p><strong>1. RECONOCIMIENTO (2 min)</strong></p>
    <ul>
      <li>"Soy una célula en el cuerpo de Gaia"</li>
      <li>"Mi bienestar afecta a todos"</li>
      <li>"El bienestar de todos me afecta"</li>
    </ul>

    <p><strong>2. CONEXIÓN (5 min)</strong></p>
    <ul>
      <li>Visualiza raíces de luz desde tu corazón</li>
      <li>Conectándose con todos los seres</li>
      <li>Formando una red dorada planetaria</li>
      <li>Pulsando con amor y sanación</li>
    </ul>

    <p><strong>3. CONTRIBUCIÓN (3 min)</strong></p>
    <ul>
      <li>Envía tu mejor energía a la red</li>
      <li>Ofrece tus dones únicos</li>
      <li>Piensa en alguien a quien hoy puedas ayudar</li>
    </ul>

    <p><strong>4. RECEPCIÓN (3 min)</strong></p>
    <ul>
      <li>Ábrete a recibir de la red</li>
      <li>Permite que la sanación colectiva te nutra</li>
      <li>Piensa en quién te sostiene</li>
    </ul>

    <p><strong>5. GRATITUD (2 min)</strong></p>
    <ul>
      <li>Agradece la interconexión</li>
      <li>Celebra no estar solo</li>
      <li>Honra la red de vida</li>
    </ul>

    <h3>Meditación del Corazón Colectivo</h3>
    <p>Para practicar en grupo o conectándose a distancia:</p>
    <p>Siéntense en círculo o visualícense conectados...<br>
    Sincronicen la respiración...<br>
    Lleven la atención al centro del pecho...<br>
    Visualicen un sol verde-rosado en cada corazón...<br>
    Estos soles comienzan a latir al unísono...<br>
    Con cada latido, envían ondas de luz...<br>
    Las ondas se encuentran en el centro...<br>
    Creando un corazón colectivo de luz...<br>
    Este corazón late por todos...<br>
    Sana por todos...<br>
    Ama por todos...<br>
    Permanezcan en este campo 20 minutos...<br>
    Sientan que no están solos...</p>

    <h3>Escribir la Historia Familiar</h3>
    <p>Para conocer y honrar el linaje:</p>

    <p><strong>1. INVOCACIÓN ANCESTRAL</strong></p>
    <ul>
      <li>Llama a tus ancestros, hasta donde llegue la memoria</li>
      <li>Pide permiso para conocer su historia</li>
    </ul>

    <p><strong>2. EL ÁRBOL ESCRITO</strong></p>
    <ul>
      <li>Dibuja un genograma, como los que propusieron Monica McGoldrick y Randy Gerson (1985): un árbol con nombres, fechas, oficios, migraciones y enfermedades</li>
      <li>Nota lo que se repite, sin buscarle un mensaje</li>
      <li>Si en tu familia se repite una enfermedad, cuéntaselo a tu médico: los antecedentes orientan los controles</li>
    </ul>

    <p><strong>3. RITUAL DE LIBERACIÓN</strong></p>
    <ul>
      <li>Representa simbólicamente el patrón</li>
      <li>Ofrece comprensión y compasión</li>
      <li>Libera con amor y gratitud</li>
    </ul>

    <p><strong>4. CELEBRACIÓN DEL LINAJE SANADO</strong></p>
    <ul>
      <li>Siente a todos tus ancestros libres</li>
      <li>Observa a tus descendientes sanos</li>
      <li>Celebra la liberación colectiva</li>
    </ul>
    <p>Lo que duele en una historia familiar se recorre mejor acompañado.</p>

    <div class="section-divider"></div>

    <h2>X. La Gran Convergencia</h2>
    <h3>Hacia una Medicina Planetaria</h3>
    <p>Estamos en el umbral de una medicina verdaderamente planetaria donde:</p>
    <ul>
      <li>Los hospitales serán templos de reconexión</li>
      <li>Los médicos serán tejedores de redes</li>
      <li>Los medicamentos incluirán frecuencias y campos: la medicina bioelectrónica ya ensaya estimular el nervio vago contra la artritis reumatoide</li>
      <li>Los diagnósticos considerarán contextos colectivos</li>
      <li>Los tratamientos serán ceremonias de sanación</li>
      <li>La prevención será también cuidado del tejido social</li>
    </ul>

    <h3>El Salto Evolutivo</h3>
    <p>La comprensión de la red de sanación colectiva no es opcional; es evolutivamente necesaria. Los grandes males comunes —el clima, las pandemias, la guerra, la desigualdad— piden algo que nadie puede solo: cooperación. Cada acto de sanación personal es un acto de activismo planetario.</p>

    <h3>Imágenes de la Red</h3>
    <p>Muchas tradiciones imaginaron un tiempo de reencuentro. En los Andes, <em>pachakuti</em> nombra el vuelco del tiempo y del mundo. Teilhard de Chardin y Vernadsky imaginaron una noosfera, la capa de pensamiento que envuelve el planeta. Alberto Villoldo llamó <em>Homo luminous</em> al ser humano que imaginó por venir. No son profecías que se cumplen solas: son imágenes de lo que podemos tejer.</p>
    <p>Somos una generación puente, como lo fueron todas. Los tejedores de la nueva red. Los sanadores del campo colectivo.</p>

    <div class="section-divider"></div>

    <h2>XI. Síntesis: La Medicina del Nosotros</h2>
    <p>La red de sanación colectiva nos revela que nunca estuvimos enfermos solos, y nunca sanaremos solos.</p>
    <p>Cada sufrimiento personal toca una red más grande. Cada acto de sanación envía ondas de coherencia a través del campo. Somos simultáneamente pacientes y sanadores en el gran hospital de la existencia.</p>
    <p>La medicina del futuro reconocerá que:</p>
    <ul>
      <li>Tu dolor me alcanza</li>
      <li>Mi cuidado te alcanza</li>
      <li>Nuestra salud es común</li>
    </ul>
    <p>No se trata de perder la individualidad sino de expandirla hasta incluir el Todo. De reconocer que el "yo" más profundo es el "nosotros" cósmico.</p>

    <blockquote>Declaración de Interdependencia Médica:<br><br>
    "Reconozco que mi cuerpo está entretejido con todos los cuerpos. Mi salud es inseparable de la salud del colectivo. Cada elección que hago afecta la red. Me comprometo a sanar no solo por mí, sino por todos los seres. A cuidar mi parte para cuidar el tejido. A tejer conscientemente la red de sanación planetaria. Porque en verdad, solo hay Un Cuerpo, Una Mente, Un Corazón, pulsando a través de infinitas formas. Y ese Uno está sanando ahora, a través de mí, a través de nosotros, a través de Todo."</blockquote>

    <blockquote>"Somos hilos en el gran tejido,<br>
    Notas en la sinfonía cósmica,<br>
    Células en el cuerpo de Gaia,<br>
    Neuronas en la mente universal.<br><br>

    Cuando uno sufre, todos sienten,<br>
    Cuando uno sana, todos se elevan,<br>
    Porque la separación es el sueño,<br>
    Y la unidad es el despertar.<br><br>

    Tejamos entonces con consciencia,<br>
    Esta red de luz sanadora,<br>
    Donde cada nodo es un corazón,<br>
    Y cada conexión es amor.<br><br>

    La medicina del futuro es simple:<br>
    Recordar que nunca estuvimos separados,<br>
    Que la sanación es un acto colectivo,<br>
    Y que el amor es la frecuencia que nos une a todos."</blockquote>

    <aside class="puerta arquitectura" aria-label="Puerta hacia Arquitectura del Destino">
      <p class="p-nombre">Puerta</p>
      <p class="p-texto">La mano que achica la amenaza, la colina que se ve menos empinada junto a un amigo y los vínculos que alargan la vida se despliegan en <em>La Red</em>, Libro 11 de <em>Arquitectura del Destino</em>, Umbral VI: «La cuesta».</p>
      <a class="cruzar" href="https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/libro-11-la-red/L11-U6.html">Cruzar ⟶</a>
    </aside>

    <div class="section-divider"></div>

    <h2>Portal de Transición al Nodo 3</h2>
    <p>La red está tejida, las conexiones reveladas, el campo colectivo activado. Pero hay algo más sutil que acompaña todo cuidado: el ritmo, el sonido, la vibración que nos atraviesa. En el próximo nodo exploraremos esa música: <strong>"Los Campos Cuánticos de Sanación: La Danza de las Ondas"</strong>...</p>
'''

R['nodo_02.html'] = [
 ('<title>Nodo 2 – La Red de Sanación Colectiva | Sanación Integral | Trinity Origen</title>\n',
  '<title>Nodo 2 – La Red de Sanación Colectiva | Sanación Integral | Trinity Origen</title>\n' + NOTA),
 ('</style>\n</head>', CSS.lstrip('\n')),
 ('<p class="node-subtitle">Medicina de la Interconexión y Campos Morfogenéticos</p>',
  '<p class="node-subtitle">Medicina de la Interconexión</p>'),
 ('__MAIN__', MAIN_02),
]


MAIN_03 = r'''    <h2>I. La Naturaleza Vibracional de la Realidad</h2>
    <h3>Más Allá de la Materia</h3>
    <p class="lead">La física cambió la imagen de la materia. En 1911, Ernest Rutherford descubrió que casi toda la masa de un átomo se concentra en un núcleo diminuto; alrededor, los electrones no giran como planetas: forman una nube de probabilidad. Lo que sentimos sólido al tocar una mesa es el rechazo entre esas nubes. La materia se parece menos a una piedra que a una música sostenida.</p>
    <p>Lo que percibimos como sólido es:</p>
    <ul>
      <li>Energía en patrones estables</li>
      <li>Información organizada coherentemente</li>
      <li>Vibración densificada en materia</li>
    </ul>

    <h3>La Orquesta del Cuerpo</h3>
    <p>No hace falta bajar hasta los átomos para oír la música. El cuerpo entero es una orquesta de ritmos que se superponen:</p>
    <ul>
      <li>El corazón: alrededor de una vez por segundo en reposo</li>
      <li>La respiración: entre doce y veinte veces por minuto</li>
      <li>El cerebro: ondas que Hans Berger registró por primera vez en 1924, desde el sueño profundo hasta la atención más aguda</li>
      <li>El sueño: ciclos de cerca de noventa minutos que se repiten durante la noche</li>
      <li>El día: un reloj interno de unas veinticuatro horas, cuyo mecanismo valió el Nobel de 2017</li>
      <li>La Tierra: las mareas, las estaciones, la luz que vuelve cada mañana</li>
    </ul>
    <p>Somos una orquesta de ritmos tocando la sinfonía de nuestra existencia. La salud tiene mucho de esa orquesta bien coordinada, y cuando un instrumento se desafina, el cuerpo avisa.</p>

    <h3>El Vacío que No Está Vacío</h3>
    <p>Debajo de toda vibración, la física encuentra un vacío que no está quieto. Lo recorren fluctuaciones permanentes, y dos placas de metal muy cercanas, en ese vacío, se atraen: entre ellas, el vacío tiene menos maneras de vibrar que afuera. Hendrik Casimir lo predijo en 1948 y Steve Lamoreaux lo midió en 1997. Es una de las imágenes más hondas que dejó la física: hasta la nada vibra.</p>

    <div class="section-divider"></div>

    <h2>II. El Corazón y el Aliento: Un Dúo</h2>
    <h3>El Corazón No Es un Metrónomo</h3>
    <p>Un corazón sano no late como un reloj. Se acelera un poco al tomar aire y se aquieta al soltarlo, y esa variación de latido a latido es señal de salud: los cardiólogos la miden y la llaman variabilidad de la frecuencia cardíaca. Cuando un corazón late demasiado parejo, a veces es porque está cansado. La vida no se sostiene con un compás rígido, sino con uno que escucha.</p>
    <p>El corazón tampoco trabaja solo. Por el nervio vago, la mayoría de las fibras suben hacia la cabeza en lugar de bajar: el corazón no obedece en silencio, también conversa con el cerebro.</p>

    <h3>Seis Respiraciones por Minuto</h3>
    <p>Hay un compás en el que el corazón y el aliento se encuentran mejor: cerca de seis respiraciones por minuto, cinco segundos al tomar el aire y cinco al soltarlo. Es el mismo ritmo al que llevaban la respiración el avemaría rezada en latín y un mantra del yoga (Bernardi y otros, 2001).</p>
    <p><strong>Práctica: Respiración del Dúo</strong></p>
    <ul>
      <li>Lleva la atención al centro del pecho</li>
      <li>Inhala contando hasta cinco, sin forzar</li>
      <li>Exhala contando hasta cinco</li>
      <li>Evoca algo que agradeces, o a alguien que quieres</li>
      <li>Sigue entre cinco y diez minutos</li>
      <li>Deja una mano en el pecho: será tu gesto para volver a este compás durante el día</li>
    </ul>
    <p>Si contar te tensa o te marea, suelta los números y respira a tu ritmo: el compás llega solo. Y si el corazón se desboca, aprieta o late a destiempo, no pide una interpretación: pide un médico.</p>

    <div class="section-divider"></div>

    <h2>III. El Sonido que Nos Forma</h2>
    <h3>La Primera Música</h3>
    <p>Antes de ver, oímos. En los últimos meses del embarazo, la voz de la madre llega al vientre amortiguada, con su melodía. En 1980, Anthony DeCasper y William Fifer mostraron que recién nacidos de menos de tres días cambiaban su manera de succionar para oír la voz de su madre y no la de otra mujer: la habían aprendido antes de nacer.</p>

    <h3>Las Notas Nacieron de una Oración</h3>
    <p>Hacia 1030, el monje Guido d'Arezzo enseñaba a cantar con un himno a san Juan Bautista en el que cada verso empezaba una nota más arriba. Tomó las primeras sílabas: <em>ut, re, mi, fa, sol, la</em>. Siglos después, el <em>ut</em> se volvió <em>do</em>. El himno pedía que los fieles pudieran cantar con la voz suelta. Las notas que cantamos nacieron de una oración por la voz.</p>

    <h3>Mantras: El Sonido como Camino</h3>
    <p>Los mantras son fórmulas de sonido que cada tradición cuida desde hace siglos:</p>
    <ul>
      <li>OM (AUM): En la tradición hindú, el sonido que contiene todos los sonidos; las Upanishads lo llaman todo lo que existe</li>
      <li>OM MANI PADME HUM: El mantra de la compasión, en el budismo tibetano</li>
      <li>RA MA DA SA: Un canto de sanación del kundalini yoga</li>
      <li>OM NAMAH SHIVAYA: El saludo a Shiva, cinco sílabas en el corazón del shivaísmo</li>
      <li>GAYATRI MANTRA: Una invocación a la luz del sol, del Rig Veda</li>
    </ul>
    <p><strong>Práctica del Mantra</strong></p>
    <ul>
      <li>Elige un mantra que te diga algo, o una palabra de tu propia tradición</li>
      <li>Repítelo despacio, en voz alta o en silencio; un mala tiene ciento ocho cuentas, si quieres llevar la cuenta</li>
      <li>Siente la vibración en el pecho y en la cara</li>
      <li>Cuando la mente se vaya, vuelve al sonido sin reproche</li>
    </ul>

    <h3>Tonificación Vocal</h3>
    <p>Usar la propia voz es la forma más antigua de música medicinal. Las vocales se sienten en distintos lugares: la U y la O, abajo, en el pecho; la A, en el centro; la E y la I, arriba, en la garganta y la cabeza. No hace falta asignarles órganos: basta con notar dónde vibra cada una.</p>
    <ul>
      <li>Inhala con calma</li>
      <li>Sostén una vocal mientras dure el aire, sin forzar</li>
      <li>Nota dónde vibra</li>
      <li>Prueba el zumbido de la abeja, <em>bhramari</em>: la boca cerrada, una <em>m</em> larga que alarga la exhalación</li>
      <li>Tres veces cada vocal</li>
    </ul>

    <div class="section-divider"></div>

    <h2>IV. La Forma del Sonido</h2>
    <p>En 1787, Ernst Chladni esparció arena sobre placas de metal y las hizo vibrar con un arco de violín: la arena huía de las zonas que temblaban y se juntaba en las líneas quietas, dibujando figuras. Cada nota, una figura distinta: estrellas, cruces, anillos, flores.</p>
    <p>Cuando Chladni las mostró en París, en 1808, Napoleón quedó tan impresionado que impulsó un premio de tres mil francos para quien explicara aquellas figuras con matemáticas. Durante años, la única que se presentó fue Sophie Germain, que había estudiado sola en la biblioteca de su padre. En 1816, al tercer intento, ganó el premio: fue la primera mujer en recibirlo de la Academia de Ciencias de París.</p>
    <p>Hay un detalle que lo cambia todo. La figura no la dibuja el temblor: la dibuja la quietud. La arena se junta donde la placa no vibra. Cada forma del sonido está hecha de sus puntos de silencio.</p>
    <p>Con la geometría sagrada ocurre algo parecido. Platón, en el <em>Timeo</em>, le dio a cada elemento un sólido perfecto: el tetraedro al fuego, el cubo a la tierra, el octaedro al aire, el icosaedro al agua; el dodecaedro lo reservó para el todo. La Flor de la Vida, círculos que se entrelazan en un patrón de seis pétalos, es un símbolo que muchas culturas dibujaron. Estas formas se contemplan, como se contempla una figura de Chladni, y enseñan a mirar.</p>
    <p><strong>Práctica: La Arena que Escucha</strong></p>
    <ul>
      <li>Tensa un film plástico sobre un bol, como el parche de un tambor</li>
      <li>Espolvorea sal fina</li>
      <li>Acerca la boca, sin tocarlo, y canta o zumba una nota larga</li>
      <li>Cambia la nota y mira cómo cambia la figura</li>
      <li>Observa dónde se junta la sal: ahí está la quietud</li>
    </ul>

    <div class="section-divider"></div>

    <h2>V. El Cristal que Sí Vibra</h2>
    <p>Los cristales son bellos, y uno vibra de verdad cada día a nuestro lado. En 1880, los hermanos Pierre y Jacques Curie descubrieron que el cuarzo, al apretarlo, produce electricidad. También ocurre al revés: la electricidad lo hace vibrar. Por eso hay un pequeño cuarzo en los relojes, que late más de treinta mil veces por segundo y marca el tiempo de nuestros días. Basta eso para mirarlos con asombro.</p>

    <div class="section-divider"></div>

    <h2>VI. La Medicina que Escucha</h2>
    <p>La medicina moderna empezó, en buena parte, escuchando. En 1816, en París, René Laennec tenía que examinar a una joven con una enfermedad del corazón y le pareció impropio apoyar la oreja en su pecho. Enrolló un cuaderno de papel, apoyó un extremo sobre el corazón y el otro en su oído, y oyó los latidos con una claridad que nunca había tenido. Así nació el estetoscopio.</p>
    <p>Desde entonces, el sonido y la vibración no dejaron de cuidar. La ecografía, que Ian Donald llevó a la obstetricia en Glasgow a fines de los años cincuenta, deja ver a un hijo antes de nacer. Las ondas de choque deshacen cálculos sin cortar. La musicoterapia acompaña el dolor y la espera.</p>

    <h3>El Paciente que Escucha</h3>
    <p>Quien atraviesa una enfermedad puede aprender a escucharse:</p>
    <ul>
      <li>Su pulso y su aliento, como un idioma propio</li>
      <li>Lo que lo calma: una voz, una música, un silencio</li>
      <li>Las señales que piden consulta, sin esperar a que griten</li>
      <li>Lo que en él sigue sano mientras algo enferma</li>
    </ul>
    <p>Aaron Antonovsky lo llamó salutogénesis: preguntar no solo qué enferma, sino qué sostiene la salud.</p>

    <h3>La Responsabilidad del Tono</h3>
    <ul>
      <li>Cuidar el tono con que hablamos, que llega antes que las palabras</li>
      <li>Bajar la voz donde alguien descansa o sufre</li>
      <li>Contribuir a la calma de los lugares compartidos</li>
      <li>Ser guardianes de la armonía</li>
      <li>Irradiar sanación por presencia</li>
    </ul>

    <div class="section-divider"></div>

    <h2>VII. El Silencio</h2>
    <h3>La Cámara sin Eco</h3>
    <p>En 1951, el compositor John Cage entró en una cámara anecoica de la Universidad de Harvard, una sala construida para absorber todo sonido. Esperaba escuchar, por fin, el silencio. Oyó dos sonidos, uno agudo y uno grave, y el ingeniero le explicó que eran su sistema nervioso y su sangre. Al año siguiente estrenó <em>4′33″</em>, una obra en la que nadie toca ninguna nota.</p>
    <p>El silencio nunca es mudo. Cuando todo calla, se oye el cuerpo: el corazón, la sangre, la vida que sigue tocando sin que nadie la dirija.</p>
    <p><strong>Práctica: Escuchar el Silencio</strong></p>
    <ul>
      <li>Siéntate en un lugar tranquilo, con los ojos cerrados</li>
      <li>Escucha durante cuatro minutos y treinta y tres segundos, como en la obra de Cage</li>
      <li>Primero, los sonidos lejanos; después, los cercanos; al fin, los de tu propio cuerpo</li>
      <li>Nota el espacio en que todos aparecen</li>
    </ul>
    <p>Si en el silencio aparece un zumbido que no se va, o si oír el propio cuerpo te inquieta, abre los ojos y vuelve a los sonidos de afuera. Un zumbido que persiste merece una consulta.</p>

    <div class="section-divider"></div>

    <h2>VIII. Síntesis: La Sinfonía de la Sanación</h2>
    <p>Los campos cuánticos de sanación nos revelan que somos música materializada, patrones de interferencia en el océano cuántico, danzando entre el orden y el caos, la forma y el vacío.</p>
    <p>La música del cuerpo no reemplaza a la medicina: la acompaña, y la medicina misma aprendió a escucharla.</p>
    <p>Cada célula canta. Cada órgano tiene su melodía. Cada sistema es una sección de la orquesta. Y nosotros somos simultáneamente el compositor, el director, los músicos y la audiencia de esta sinfonía corporal.</p>
    <p>La invitación es clara: afinar nuestro instrumento, aprender a escuchar nuestro propio compás y descansar, de vez en cuando, en el silencio donde toda música empieza.</p>

    <blockquote>Declaración del Ritmo Propio:<br><br>
    "Soy un ser de ritmo y de luz. Escucho mi pulso y mi aliento. Elijo lo que dejo resonar en mí. Sintonizo con el amor, la calma y la armonía. Cuando el miedo acelera mi corazón, lo acompaño con una respiración lenta. Cuando algo en mí desafina, no lo culpo: lo cuido. Danzo en resonancia con el cosmos. Mi aliento es mi compás. Mi silencio es mi refugio. Mi amor es mi poder sanador. Vibro, luego existo. Resueno, luego vivo. Soy la música de las esferas hecha carne."</blockquote>

    <blockquote>"En el principio era el Verbo,<br>
    Y el Verbo era vibración,<br>
    Y la vibración se hizo forma,<br>
    Y la forma se hizo consciencia.<br><br>

    Somos ondas en el océano cuántico,<br>
    Frecuencias en la sinfonía cósmica,<br>
    Notas en la partitura divina,<br>
    Música condensada en materia.<br><br>

    Cuando recordamos nuestra naturaleza vibracional,<br>
    Cuando volvemos a escuchar nuestro propio pulso,<br>
    Cuando afinamos con el cosmos,<br>
    La sanación no es milagro, es retorno.<br><br>

    Porque aun rotos seguimos sonando,<br>
    Aun desafinados, somos música.<br>
    Aun enfermos, algo en nosotros<br>
    Sigue cantando entero.<br><br>

    Y en el silencio entre las notas,<br>
    En el espacio entre las ondas,<br>
    En el vacío lleno de potencial,<br>
    Encontramos la medicina suprema:<br>
    El Silencio Sanador del Ser."</blockquote>

    <aside class="puerta portal" aria-label="Puerta hacia el Portal Público">
      <p class="p-nombre">Puerta</p>
      <p class="p-texto">El corazón tiene miles de células marcapasos que se encuentran entre ellas latido tras latido, sin que nadie les diga cuándo, y Simone Weil vio en la atención el mismo compás de la respiración. Se despliegan en <em>El Ritmo</em>, Libro 33 del Portal Público, Umbral VI: «Como se respira».</p>
      <a class="cruzar" href="https://soyartur-trinity.github.io/Trinity_Portal_Publico/01_Libros/33_El_Ritmo/umbral-06.html">Cruzar ⟶</a>
    </aside>

    <div class="section-divider"></div>

    <h2>Portal de Transición al Nodo 4</h2>
    <p>Los ritmos han sido escuchados, la música del cuerpo revelada, el silencio reconocido. Pero hay algo que acompaña toda esta música: la mente que la escucha. En el próximo nodo exploraremos la mente como compañera de la sanación: <strong>"La Mente como Portal de Sanación"</strong>...</p>
'''

R['nodo_03.html'] = [
 ('<title>Nodo 3 – Los Campos Cuánticos de Sanación | Sanación Integral | Trinity Origen</title>\n',
  '<title>Nodo 3 – Los Campos Cuánticos de Sanación | Sanación Integral | Trinity Origen</title>\n' + NOTA),
 ('</style>\n</head>', CSS.lstrip('\n')),
 ('<p class="node-subtitle">Medicina Vibracional y Frecuencial - La Danza de las Ondas</p>',
  '<p class="node-subtitle">La Danza de las Ondas</p>'),
 ('La enfermedad es disonancia. La sanación es el retorno a la armonía cósmica."</p>',
  'Y cuando algo en nosotros desafina, la música no se pierde: cuidar es ayudarla a volver."</p>'),
 ('__MAIN__', MAIN_03),
]


MAIN_04 = r'''    <h2>I. La Revolución de la Neuroplasticidad</h2>
    <h3>El Dogma Derribado</h3>
    <p class="lead">Durante buena parte del siglo XX se pensó que el cerebro adulto apenas cambiaba. Santiago Ramón y Cajal, que mostró que el cerebro está hecho de neuronas individuales, escribió que en el cerebro adulto todo puede morir y nada se regenera, y dejó a la ciencia del futuro la tarea de cambiar, si podía, ese decreto.</p>
    <p>La ciencia del futuro lo cambió: el cerebro se remodela toda la vida.</p>
    <p>El cerebro es:</p>
    <ul>
      <li>Plástico: Se remodela constantemente</li>
      <li>Regenerativo: Se recupera de muchas lesiones reorganizando sus redes</li>
      <li>Adaptativo: Crea nuevas conexiones continuamente</li>
    </ul>

    <h3>Los Números de la Maravilla</h3>
    <p>Tu cerebro en este momento:</p>
    <ul>
      <li>86 mil millones de neuronas (Herculano-Houzel y su equipo, 2009)</li>
      <li>Unos cien billones de sinapsis</li>
      <li>Casi todo lo que procesa ocurre fuera de la consciencia</li>
    </ul>
    <p>Llevas dentro la estructura más compleja que se conoce.</p>

    <h3>Neuroplasticidad Dirigida</h3>
    <p>En parte, podemos orientar esta plasticidad: lo que se practica, se fortalece.</p>
    <p>La psicóloga Phillippa Lally y su equipo del University College de Londres siguieron a noventa y seis voluntarios que querían adquirir un hábito nuevo, y publicaron los resultados en 2010. En promedio, el gesto tardó sesenta y seis días en volverse automático, entre dieciocho y más de doscientos, y faltar un día no cambiaba el resultado. No hay plazo mágico: hay repetición paciente.</p>

    <div class="section-divider"></div>

    <h2>II. La Mente y su Misterio</h2>
    <h3>Más Allá del Cerebro Clásico</h3>
    <p>Roger Penrose y Stuart Hameroff propusieron, en los años noventa, que la consciencia podría depender de estados cuánticos en los microtúbulos de las neuronas. Es una hipótesis audaz y muy discutida. El misterio de la consciencia sigue abierto, y eso también es una maravilla.</p>

    <h3>Los Tres Cerebros Integrados</h3>
    <p>Es el mapa que propuso Paul MacLean: una simplificación que sirve como imagen.</p>

    <h4>1. Cerebro Reptiliano (Tronco Encefálico)</h4>
    <ul>
      <li>Supervivencia y funciones automáticas</li>
      <li>Respuestas de lucha/huida/parálisis</li>
      <li>Programas ancestrales de protección</li>
      <li>La base de todos los miedos</li>
    </ul>

    <h4>2. Cerebro Mamífero (Sistema Límbico)</h4>
    <ul>
      <li>Emociones y memorias</li>
      <li>Vínculos y conexiones</li>
      <li>Respuestas hormonales</li>
      <li>El corazón del trauma y la sanación</li>
    </ul>

    <h4>3. Cerebro Humano (Neocórtex)</h4>
    <ul>
      <li>Pensamiento abstracto y creatividad</li>
      <li>Planificación y visión de futuro</li>
      <li>Lenguaje y símbolos</li>
      <li>El arquitecto de nuevas realidades</li>
    </ul>

    <h4>4. El Cerebro Compartido</h4>
    <ul>
      <li>El que se teje con otros</li>
      <li>Cuenta con la compañía para regularse</li>
      <li>Se calma con una mano conocida</li>
      <li>No da por supuesta la soledad sino la compañía (Coan)</li>
    </ul>

    <div class="section-divider"></div>

    <h2>III. Psiconeuroinmunología: La Trinidad Sanadora</h2>
    <h3>La Conversación Tripartita</h3>
    <p>Mente ↔ Sistema Nervioso ↔ Sistema Inmune</p>
    <p>En 1975, Robert Ader y Nicholas Cohen condicionaron el sistema inmune de unas ratas como Pávlov a sus perros: bastaba el sabor dulce que habían asociado a un fármaco para que sus defensas bajaran. Ader le dio nombre a la disciplina que nació de ahí.</p>
    <p>Estos tres sistemas no están separados; son un supersistema unificado:</p>
    <ul>
      <li>Los pensamientos y las emociones cambian la química del cuerpo</li>
      <li>Los neuropéptidos modulan la inmunidad</li>
      <li>El sistema inmune envía señales al cerebro</li>
      <li>El cerebro interpreta y genera más pensamientos</li>
      <li>El ciclo continúa en espiral ascendente o descendente</li>
    </ul>

    <h3>Moléculas de Emoción</h3>
    <p>Candace Pert, que en 1973 halló con Solomon Snyder el receptor donde actúan los opiáceos, dedicó después su obra a mostrar que las moléculas de la emoción circulan también por el sistema inmune. Algunas de las que acompañan a las emociones:</p>
    <p>Miedo: Cortisol, adrenalina<br>
    Vínculo: Oxitocina<br>
    Alegría y deseo: Dopamina, endorfinas</p>
    <p>Somos farmacias ambulantes: el cuerpo fabrica sus propias moléculas de calma y de alarma.</p>

    <h3>El Efecto Placebo Revelado</h3>
    <p>En 2010, Ted Kaptchuk y su equipo dieron a pacientes con colon irritable unas pastillas que, se les dijo con claridad, no tenían ningún principio activo; aun así, mejoraron más que quienes no recibieron nada.</p>
    <p>El placebo no es nada: es el cuidado, la expectativa y el ritual actuando en el cuerpo. No reemplaza un tratamiento; muestra cuánto importa cómo se da.</p>

    <div class="section-divider"></div>

    <h2>IV. Hábitos y Creencias</h2>
    <h3>Lo que Hacemos sin Pensarlo</h3>
    <p>Gran parte de lo que hacemos ocurre en automático: hábitos, gestos, maneras de reaccionar que aprendimos temprano. Daniel Kahneman lo describió en <em>Pensar rápido, pensar despacio</em> (2011): un modo de pensar rápido y automático, y otro lento y deliberado. Lo aprendido temprano pesa, y también se puede revisar.</p>

    <h3>Creencias que Pesan</h3>
    <ul>
      <li>"La felicidad no dura"</li>
      <li>"No merezco estar completamente sano"</li>
      <li>"El sufrimiento purifica"</li>
      <li>"La vida es dura"</li>
      <li>"En mi familia todos tienen diabetes, así que no hay nada que hacer": los antecedentes piden controles; lo que pesa es el "nada que hacer"</li>
      <li>"A mi edad es normal tener dolor": a veces es una señal que merece consulta</li>
    </ul>

    <h3>Caminos de Cambio</h3>

    <h4>1. EMDR (Desensibilización y Reprocesamiento)</h4>
    <p>Es la terapia del trauma que Francine Shapiro creó a fines de los años ochenta, con buena evidencia y recomendada por la Organización Mundial de la Salud para el estrés postraumático. Combina el recuerdo con una estimulación bilateral de los ojos, el sonido o el tacto, y se hace siempre con un terapeuta formado.</p>

    <h4>2. Hipnosis Clínica</h4>
    <p>Tiene usos estudiados, por ejemplo en el dolor, y se practica con profesionales formados.</p>

    <h4>3. Frases Verdaderas</h4>
    <p>ESTRUCTURA ÓPTIMA:</p>
    <ul>
      <li>Presente ("Hoy" no "Algún día")</li>
      <li>Verdadero (Algo que puedas creer hoy)</li>
      <li>Personal ("Yo" no "Uno")</li>
      <li>Emocional (Sentir mientras se dice)</li>
      <li>Repetición (Cada día que haga falta)</li>
    </ul>

    <p>EJEMPLO:</p>
    <blockquote>"Hoy cuido este cuerpo.<br>
    Estoy aprendiendo a descansar.<br>
    Puedo pedir ayuda.<br>
    Este cuerpo, con todo lo que le pasa, sigue siendo mi casa."</blockquote>

    <div class="section-divider"></div>

    <h2>V. Meditación como Medicina</h2>
    <h3>La Neurociencia de la Meditación</h3>
    <p>Los primeros estudios de imágenes (Lazar, 2005; Hölzel, 2011) mostraron cambios en la materia gris de quienes meditan. Una revisión de cuarenta y siete ensayos (Goyal y otros, 2014) encontró una ayuda moderada en la ansiedad, la depresión y el dolor.</p>

    <h3>Tipos de Meditación y Sus Efectos</h3>

    <h4>1. Mindfulness (Atención Plena)</h4>
    <ul>
      <li>Jon Kabat-Zinn creó en 1979 su programa de reducción del estrés</li>
      <li>Ayuda con el estrés y el dolor crónico</li>
      <li>Enseña a estar con lo que hay</li>
    </ul>

    <h4>2. Meditación Trascendental</h4>
    <ul>
      <li>Puede ayudar a bajar la presión arterial</li>
      <li>Aquieta con la repetición de un mantra</li>
    </ul>

    <h4>3. Meditación de Amor Bondadoso</h4>
    <ul>
      <li>Acerca a los demás</li>
      <li>Ablanda el juicio sobre uno mismo</li>
    </ul>

    <h4>4. Meditación Vipassana</h4>
    <ul>
      <li>Mejora procesamiento emocional</li>
      <li>Facilita insights sanadores</li>
      <li>Los retiros intensivos pueden remover mucho: conviene hacerlos con guía y consultar antes si atraviesas un momento frágil</li>
    </ul>

    <h3>Práctica: Escaneo Corporal</h3>
    <p><strong>Meditación de Escaneo Corporal Sanador:</strong></p>
    <p>POSICIÓN: Acostado cómodamente<br>
    DURACIÓN: 30-45 minutos</p>

    <p><strong>1. RELAJACIÓN INICIAL (5 min)</strong></p>
    <ul>
      <li>Respiración profunda</li>
      <li>Soltar tensiones</li>
      <li>Intención de sanación</li>
    </ul>

    <p><strong>2. ESCANEO ASCENDENTE (15 min)</strong></p>
    <ul>
      <li>Comenzar en los pies</li>
      <li>Subir lentamente</li>
      <li>Enviar amor a cada parte</li>
      <li>Notar sin juzgar</li>
      <li>Respirar hacia áreas tensas</li>
    </ul>

    <p><strong>3. BAÑO DE LUZ SANADORA (10 min)</strong></p>
    <ul>
      <li>Visualizar luz dorada</li>
      <li>Entrando por coronilla</li>
      <li>Llenando todo el cuerpo</li>
      <li>Aflojando lo tenso</li>
      <li>Agradeciendo lo que sostiene</li>
    </ul>

    <p><strong>4. FRASE VERDADERA (5 min)</strong></p>
    <ul>
      <li>"Gracias por sostenerme hoy"</li>
      <li>Sentir la verdad de esto</li>
      <li>Expandir la sensación</li>
    </ul>

    <p><strong>5. GRATITUD SOMÁTICA (5 min)</strong></p>
    <ul>
      <li>Agradecer a cada sistema</li>
      <li>Honrar el milagro del cuerpo</li>
      <li>Celebrar la vida presente</li>
    </ul>

    <p><strong>6. INTEGRACIÓN (5 min)</strong></p>
    <ul>
      <li>Retorno suave</li>
      <li>Llevar la calma al día</li>
      <li>Anclar la experiencia</li>
    </ul>

    <div class="section-divider"></div>

    <h2>VI. Visualización Creativa Terapéutica</h2>
    <h3>El Poder de la Imagen Mental</h3>
    <p>Álvaro Pascual-Leone y su equipo pidieron en 1995 a personas que nunca habían tocado el piano que practicaran un ejercicio dos horas por día durante cinco días, unas con las manos y otras solo en la imaginación. El mapa motor del cerebro cambió en los dos grupos de modo parecido; tocar con las manos mejoraba más, e imaginar sumaba.</p>
    <p>Por eso la visualización es una herramienta valiosa: prepara al cuerpo y lo acompaña.</p>

    <h3>Principios de Visualización Efectiva</h3>
    <p>1. Claridad: Detalles específicos y vívidos<br>
    2. Emoción: Dejar que la imagen se sienta<br>
    3. Regularidad: Práctica diaria consistente<br>
    4. Gratitud: Agradecer lo que ya está</p>

    <h3>Prácticas de Visualización Sanadora</h3>

    <h4>Práctica 1: Ensayo Mental</h4>
    <ol>
      <li>Elegir un paso posible: caminar hasta la esquina, una conversación pendiente</li>
      <li>Imaginarlo con detalle, en primera persona</li>
      <li>Imaginar también los obstáculos y cómo los atraviesas</li>
      <li>Añadir banda sonora emocional</li>
      <li>Darlo, después, en la vida</li>
    </ol>
    <p>Gabriele Oettingen encontró que soñar solo con el resultado deseado tiende a restar la energía para alcanzarlo, y que rinde más alternar el sueño con el obstáculo real y el primer paso.</p>

    <h4>Práctica 2: Diálogo con lo que Duele</h4>
    <ol>
      <li>Personificar lo que duele, si ayuda</li>
      <li>Establecer diálogo respetuoso</li>
      <li>Preguntar: "¿Qué necesitas?"</li>
      <li>Escuchar sin resistencia</li>
      <li>Elegir un cuidado</li>
      <li>Agradecer y liberar con amor</li>
    </ol>
    <p>Si lo que duele es nuevo o persiste, la mejor respuesta es una consulta.</p>

    <h4>Práctica 3: Viaje Chamánico Interior</h4>
    <ol>
      <li>Entrar en estado meditativo</li>
      <li>Visualizar descenso al interior del cuerpo</li>
      <li>Viajar al órgano/sistema afectado</li>
      <li>Observar el paisaje interior</li>
      <li>Realizar sanación simbólica</li>
      <li>Retornar con nueva comprensión</li>
    </ol>

    <div class="section-divider"></div>

    <h2>VII. El Poder de la Narrativa Personal</h2>
    <h3>Reescribiendo la Historia</h3>
    <p>Somos seres narrativos. La historia que nos contamos sobre nuestra salud influye en cómo vivimos lo que nos pasa:</p>
    <p>Historia Resignada: "Tengo mala genética, así que da igual"<br>
    Historia Cuidadora: "Conozco mis antecedentes, y me cuido"</p>
    <p>Historia Fatalista: "Es crónico, ya no hay nada que hacer"<br>
    Historia Posible: "Es crónico, y hay mucho que puedo hacer para vivir bien"</p>
    <p>Historia Limitante: "A mi edad ya no..."<br>
    Historia Expansiva: "A mi edad elijo qué quiero cuidar"</p>

    <h3>Técnica de Reescritura Biográfica</h3>
    <p><strong>1. IDENTIFICAR NARRATIVA ACTUAL</strong></p>
    <ul>
      <li>¿Qué historia me cuento?</li>
      <li>¿Dónde la aprendí?</li>
      <li>¿Me sirve todavía?</li>
    </ul>

    <p><strong>2. CREAR NUEVA NARRATIVA</strong></p>
    <ul>
      <li>Protagonista empoderado</li>
      <li>Desafíos como oportunidades</li>
      <li>Final inspirador</li>
    </ul>

    <p><strong>3. ENSAYO</strong></p>
    <ul>
      <li>Contar la nueva historia diariamente</li>
      <li>Sentirla verdadera</li>
      <li>Actuar desde ella</li>
    </ul>

    <p><strong>4. BUSCAR EVIDENCIA</strong></p>
    <ul>
      <li>Notar confirmaciones</li>
      <li>Celebrar pequeños cambios</li>
      <li>Reforzar nueva identidad</li>
    </ul>

    <p><strong>5. COMPARTIR LA NUEVA HISTORIA</strong></p>
    <ul>
      <li>Contarla a otros</li>
      <li>Recibir reflejo social</li>
      <li>Anclar en realidad compartida</li>
    </ul>
    <p>En un estudio pequeño de 1986, James Pennebaker y Sandra Beall vieron que estudiantes que escribieron cuatro días seguidos sobre lo que más les había dolido terminaban cada sesión más tristes, y en los meses siguientes fueron menos veces al médico. Nombrar lo evitado remueve primero y alivia después. Si escribir abre algo que no puedes sostener, para y busca con quién hablarlo.</p>

    <div class="section-divider"></div>

    <h2>VIII. Estados de Consciencia y Sanación</h2>
    <h3>El Espectro de la Consciencia</h3>
    <p>El cerebro pasa por distintos ritmos a lo largo del día y de la noche:</p>

    <h4>Estado Beta (13-30 Hz): Consciencia ordinaria</h4>
    <ul>
      <li>Análisis y planificación</li>
      <li>Estrés y preocupación</li>
    </ul>

    <h4>Estado Alpha (8-13 Hz): Relajación consciente</h4>
    <ul>
      <li>Creatividad y visualización</li>
      <li>Ojos cerrados, mente quieta</li>
    </ul>

    <h4>Estado Theta (4-8 Hz): Meditación profunda</h4>
    <ul>
      <li>El umbral del sueño</li>
      <li>Experiencias místicas</li>
    </ul>

    <h4>Estado Delta (0.5-4 Hz): Sueño profundo</h4>
    <ul>
      <li>El cuerpo libera la hormona de crecimiento</li>
      <li>Repara y se restaura</li>
    </ul>

    <h4>Estado Gamma (30-100 Hz): Atención muy concentrada</h4>
    <ul>
      <li>Experiencias cumbre</li>
      <li>En meditadores de muchísimos años de práctica, Antoine Lutz y Richard Davidson registraron una gamma intensa (2004)</li>
    </ul>

    <h3>Inducción de Estados de Calma</h3>
    <p><strong>Técnica de Respiración 4-7-8 (Andrew Weil):</strong></p>
    <ol>
      <li>Exhalar completamente</li>
      <li>Inhalar por nariz contando 4</li>
      <li>Retener contando 7</li>
      <li>Exhalar por boca contando 8</li>
      <li>Repetir 4 ciclos</li>
      <li>Aflojar antes de dormir</li>
    </ol>
    <p>Si retener te incomoda, acorta los tiempos.</p>

    <div class="section-divider"></div>

    <h2>IX. Emociones que Acompañan</h2>

    <h4>Gratitud</h4>
    <ul>
      <li>En 2003, Robert Emmons y Michael McCullough pidieron a estudiantes que anotaran cada semana cinco cosas que agradecían: al cabo de diez semanas se sentían mejor con su vida y miraban la semana siguiente con más optimismo</li>
    </ul>

    <h4>Compasión</h4>
    <ul>
      <li>Sentir el dolor ajeno como propio agota; la compasión, que acompaña sin fundirse, renueva (Tania Singer)</li>
    </ul>

    <h4>Alegría</h4>
    <ul>
      <li>Libera endorfinas</li>
      <li>La risa compartida afloja y acerca</li>
    </ul>

    <h4>Amor</h4>
    <ul>
      <li>Produce oxitocina</li>
      <li>La compañía calma la alarma</li>
    </ul>

    <p>Ninguna emoción es una falta. Sentir miedo, tristeza o enojo ante una enfermedad no la empeora por culpa tuya: es humano, y también se acompaña.</p>

    <h3>Práctica Diaria de Cuidado Emocional</h3>

    <p><strong>MAÑANA (10 min):</strong></p>
    <ul>
      <li>Gratitud por 5 cosas</li>
      <li>Imaginar un buen momento posible del día</li>
      <li>Sonreír genuinamente</li>
      <li>Un abrazo, a otro o a ti mismo</li>
    </ul>

    <p><strong>MEDIODÍA (5 min):</strong></p>
    <ul>
      <li>Pausa de apreciación</li>
      <li>Respiración de alegría</li>
      <li>Micro-meditación de amor</li>
    </ul>

    <p><strong>NOCHE (10 min):</strong></p>
    <ul>
      <li>Revisión apreciativa del día</li>
      <li>Perdón y liberación</li>
      <li>Gratitud por el cuerpo</li>
      <li>Intención de descanso</li>
    </ul>

    <div class="section-divider"></div>

    <h2>X. Neurofeedback y Biofeedback</h2>
    <h3>Entrenando el Cerebro</h3>
    <p>El neurofeedback permite ver y modificar nuestra actividad cerebral en tiempo real. Se estudia en el TDAH, la ansiedad, la depresión, el trauma y el dolor crónico, con resultados variables. El entrenamiento con la variabilidad cardíaca y la respiración resonante tiene más respaldo.</p>

    <h3>Protocolos de Autorregulación</h3>
    <p><strong>Entrenamiento de la Variabilidad Cardíaca:</strong></p>
    <ol>
      <li>Monitorear variabilidad cardíaca</li>
      <li>Respiración resonante (5.5 ciclos/min)</li>
      <li>Visualización coherente</li>
      <li>Feedback visual/auditivo</li>
      <li>Práctica hasta dominio</li>
      <li>Aplicación sin dispositivo</li>
    </ol>

    <p><strong>Neurofeedback Casero:</strong></p>
    <p>Hay dispositivos accesibles que muestran la actividad del cerebro o del corazón. Pueden ayudar a aprender a calmarse, no sirven para diagnosticar, y con un diagnóstico el entrenamiento se hace con un profesional.</p>

    <div class="section-divider"></div>

    <h2>XI. La Mente Colectiva Sanadora</h2>
    <h3>Campos Mentales Compartidos</h3>
    <p>Nuestras mentes no están aisladas. Participamos en campos mentales colectivos:</p>
    <ul>
      <li>Campo familiar mental</li>
      <li>Campo cultural de creencias</li>
      <li>Campo profesional de pensamiento</li>
      <li>Campo global de consciencia</li>
      <li>Campo universal de mente</li>
    </ul>
    <p>Lo que se piensa en grupo pesa. En 1951, Solomon Asch mostró que muchas personas decían ver mal la longitud de unas líneas para no contradecir al grupo. Importa elegir con quiénes pensamos.</p>

    <h3>Coherencia Mental Grupal</h3>
    <p><strong>Práctica en Grupo:</strong></p>
    <p>GRUPOS DE SIETE A TRECE PERSONAS:</p>

    <p><strong>1. SINCRONIZACIÓN (5 min)</strong></p>
    <ul>
      <li>Respiración común</li>
      <li>Atención al propio latido</li>
    </ul>

    <p><strong>2. INTENCIÓN COMPARTIDA (5 min)</strong></p>
    <ul>
      <li>Una intención dicha en voz alta</li>
      <li>Emoción compartida</li>
    </ul>

    <p><strong>3. SILENCIO (10 min)</strong></p>
    <ul>
      <li>Estar juntos sin hablar</li>
    </ul>

    <p><strong>4. DESEO DE BIEN (10 min)</strong></p>
    <ul>
      <li>Por quien lo necesita en el grupo</li>
      <li>Por quienes sufren lejos</li>
    </ul>

    <p><strong>5. CIERRE (5 min)</strong></p>
    <ul>
      <li>Gratitud grupal</li>
      <li>Una palabra de cierre</li>
    </ul>

    <div class="section-divider"></div>

    <h2>XII. Tecnologías Mentales Emergentes</h2>
    <h3>Interfaces Cerebro-Computadora</h3>
    <p>El futuro inmediato incluye:</p>
    <ul>
      <li>Implantes que leen pensamientos: en 2023, dos equipos tradujeron en palabras, a través de una voz sintética, el habla que intentaban personas con parálisis</li>
      <li>Estimulación cerebral personalizada</li>
      <li>Realidad virtual terapéutica</li>
      <li>IA que predice estados mentales</li>
      <li>Telepatía tecnológicamente asistida: en 2014 ya se ensayó la comunicación directa entre dos cerebros humanos</li>
    </ul>

    <h3>Psicodélicos como Medicina</h3>
    <p>El renacimiento psicodélico se estudia hoy en ensayos clínicos:</p>
    <ul>
      <li>Psilocibina: Depresión resistente</li>
      <li>MDMA: Trauma y estrés postraumático</li>
    </ul>
    <p>En 2016, equipos de la Universidad Johns Hopkins y de la Universidad de Nueva York publicaron ensayos con pacientes de cáncer: una sola dosis de psilocibina, con preparación y acompañamiento, redujo la ansiedad y la depresión, y en la mayoría el alivio seguía seis meses después. Fuera de ese marco no es una práctica para hacer por cuenta propia: puede desencadenar crisis graves, sobre todo en quien tiene antecedentes de psicosis.</p>

    <h3>Estimulación Magnética Transcraneal</h3>
    <p>Está aprobada para algunas depresiones que no respondieron a otros tratamientos, y se estudia para:</p>
    <ul>
      <li>Mejorar función cognitiva</li>
      <li>Facilitar neuroplasticidad</li>
    </ul>

    <div class="section-divider"></div>

    <h2>XIII. El Observador Cuántico Interno</h2>
    <h3>La Consciencia que Observa</h3>
    <p>Hay un nivel de consciencia que observa todos los pensamientos pero no es ninguno de ellos:</p>
    <ul>
      <li>El testigo silencioso</li>
      <li>La consciencia pura</li>
      <li>El observador cuántico</li>
      <li>El Yo verdadero</li>
      <li>La presencia sanadora</li>
    </ul>

    <h3>Cultivando el Observador</h3>
    <p><strong>Práctica de Desidentificación:</strong> es un ejercicio de Roberto Assagioli, el creador de la psicosíntesis.</p>
    <blockquote>"Tengo pensamientos, pero no soy mis pensamientos"<br>
    "Tengo emociones, pero no soy mis emociones"<br>
    "Tengo un cuerpo, pero no soy solo mi cuerpo"<br>
    "Tengo una historia, pero no soy mi historia"<br>
    "Tengo una enfermedad, pero no soy mi enfermedad"</blockquote>
    <p>La terapia de aceptación y compromiso de Steven Hayes trabaja algo parecido: notar "estoy teniendo el pensamiento de que..." en lugar de fundirse con él.</p>

    <blockquote>"Soy el observador eterno,<br>
    La consciencia inmutable,<br>
    El espacio donde todo ocurre,<br>
    La presencia que todo lo abraza,<br>
    El Ser que nunca enferma."</blockquote>

    <h3>Meditación del Observador Sanador</h3>
    <p>Siéntate en quietud...<br>
    Observa tus pensamientos como nubes pasando...<br>
    No te aferres, no rechaces...<br>
    Solo observa...</p>

    <p>Nota: hay algo en ti observando...<br>
    Ese observador está perfectamente sano...<br>
    Siempre lo ha estado...<br>
    Siempre lo estará...</p>

    <p>Descansa en esa consciencia observadora...<br>
    Desde ahí, observa tu cuerpo...<br>
    Envía amor sin juicio...<br>
    Permite la sanación natural...</p>

    <p>El observador no necesita sanar...<br>
    ES la sanación misma...<br>
    Permanece como el observador...<br>
    Desde ahí, cuida lo que necesita cuidado...</p>
    <p>Si tomar distancia te hace sentir lejos de ti, vuelve a los pies en el suelo.</p>

    <div class="section-divider"></div>

    <h2>XIV. Síntesis: La Mente Arquitecta</h2>
    <p>La mente como portal de sanación nos revela que somos, en parte, arquitectos de nuestra vida. No elegimos los genes, la historia ni todas las circunstancias; sí podemos elegir, cada día, a qué prestamos atención, qué practicamos y cómo nos tratamos. Sostenido en el tiempo, eso cambia el cerebro y cambia la vida.</p>
    <p>La plasticidad nos da un material dócil. La atención nos da el cincel. La voluntad, la paciencia de volver cada día. Y el amor, la energía para la transformación.</p>
    <p>No hace falta esperar a la medicina del futuro para empezar a cuidarnos: la mente es una de sus aliadas más antiguas.</p>

    <blockquote>Declaración del Arquitecto Mental:<br><br>
    "Soy aprendiz y arquitecto de mi vida interior. Elijo, cada día, a qué presto atención. Cultivo con paciencia las emociones que me hacen bien y acompaño con ternura las que me duelen. Sé que mi cerebro cambia con lo que practico, y practico lo que quiero ser. Mi mente es aliada de mi medicina. Mi consciencia me acompaña. Mi presencia sostiene. Soy el milagro que estaba esperando."</blockquote>

    <blockquote>"La mente es el constructor,<br>
    El cerebro es la construcción,<br>
    El cuerpo es el templo,<br>
    La consciencia es el arquitecto.<br><br>

    Cada sinapsis es decisión,<br>
    Cada neurona es posibilidad,<br>
    Cada pensamiento es creación,<br>
    Cada momento es oportunidad.<br><br>

    No somos prisioneros del pasado,<br>
    Ni víctimas del cerebro heredado,<br>
    Somos escultores del presente,<br>
    Arquitectos del futuro encarnado.<br><br>

    Con cada pensamiento elegido,<br>
    Con cada emoción cultivada,<br>
    Con cada creencia transformada,<br>
    Renacemos, nos recreamos, sanamos.<br><br>

    Porque no todo lo que duele<br>
    Nació de lo que pensamos,<br>
    Pero en todo lo que sana<br>
    La mente pone sus manos."</blockquote>

    <aside class="puerta arquitectura" aria-label="Puerta hacia Arquitectura del Destino">
      <p class="p-nombre">Puerta</p>
      <p class="p-texto">El ejercicio de Assagioli, el ojo que no puede verse a sí mismo y el tablero de la terapia de aceptación se despliegan en <em>El Testigo</em>, Libro 3 de <em>Arquitectura del Destino</em>, Umbral II: «Tengo, pero no soy».</p>
      <a class="cruzar" href="https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/libro-03-el-testigo/L03-U2.html">Cruzar ⟶</a>
    </aside>

    <div class="section-divider"></div>

    <h2>Portal de Transición al Nodo 5</h2>
    <p>La mente ha revelado su poder arquitectónico, la consciencia su capacidad de acompañar, el cerebro su plasticidad asombrosa. Pero hay un elemento más profundo aún, el fuego sagrado que anima toda vida, la fuerza que hace latir el corazón y respirar los pulmones sin que lo pensemos. En el próximo nodo exploraremos esta fuerza vital primordial: <strong>"La Energía Vital y los Sistemas Sutiles: Prana, Chi y el Aliento"</strong>...</p>
'''

R['nodo_04.html'] = [
 ('<title>Nodo 4 – La Mente como Portal de Sanación | Sanación Integral | Trinity Origen</title>\n',
  '<title>Nodo 4 – La Mente como Portal de Sanación | Sanación Integral | Trinity Origen</title>\n' + NOTA),
 ('</style>\n</head>', CSS.lstrip('\n')),
 ('<p class="node-subtitle">Neuroplasticidad y Consciencia Curativa - El Arquitecto Interior</p>',
  '<p class="node-subtitle">Neuroplasticidad y Consciencia - El Arquitecto Interior</p>'),
 ('"La mente no es lo que el cerebro hace; el cerebro es lo que la mente crea. Somos escultores neuronales, arquitectos de nuestra propia biología, programadores del superordenador más sofisticado del universo conocido. Cada pensamiento es un cincel, cada emoción un pincel, cada creencia un plano arquitectónico que rediseña constantemente el templo viviente."',
  '"La mente no es solo lo que el cerebro hace: lo que la mente practica también va dando forma al cerebro. Somos escultores neuronales, aprendices de nuestra propia biología. Cada pensamiento es un cincel, cada emoción un pincel, cada creencia un plano arquitectónico que rediseña, poco a poco, el templo viviente."'),
 ('__MAIN__', MAIN_04),
]

R05 = [
 ('<title>Nodo 5 – La Energía Vital y los Sistemas Sutiles | Sanación Integral | Trinity Origen</title>\n',
  '<title>Nodo 5 – La Energía Vital y los Sistemas Sutiles | Sanación Integral | Trinity Origen</title>\n' + NOTA),
 ('</style>\n</head>', CSS.lstrip('\n')),
 ('<p class="node-subtitle">Prana, Chi y la Medicina Energética - El Río de Vida</p>',
  '<p class="node-subtitle">Prana, Chi y el Aliento - El Río de Vida</p>'),
 ('Conocerla es conocer el secreto de la vida. Dominarla es dominar la salud. Fluir con ella es la suprema medicina."</p>',
  'Conocerla es asomarse al secreto de la vida. Respirar con ella es la más antigua de las medicinas."</p>'),
 # I
 ('''    Ashé (Yoruba): El poder de hacer que las cosas sucedan<br>
    Orgón (Reich): La energía orgásmica universal<br>
    Bioplasma (Rusia): El cuarto estado de la materia</p>
    <p>Todos refieren a la misma realidad energética fundamental.</p>''',
  '''    Ashé (Yoruba): El poder de hacer que las cosas sucedan</p>
    <p>Muchos de estos nombres significan, antes que nada, aliento: prana, pneuma, ruach, y también el qi, que en su escritura antigua dibuja el vapor que sube del arroz. Antes de ser energía, la fuerza vital fue respiración.</p>'''),
 ('''    <pre>CUERPO FÍSICO (visible)
    ↕️
CUERPO ENERGÉTICO (invisible pero perceptible)
    ↕️
CUERPO CAUSAL (campo de información)</pre>

    <p>La enfermedad aparece primero en el cuerpo energético, semanas o meses antes de manifestarse físicamente. La sanación verdadera debe abordar este nivel.</p>''',
  '''    <p>Muchas tradiciones describen, además del cuerpo visible, uno sutil por donde circula la fuerza vital: los meridianos de la medicina china, los nadis y los chakras del yoga. Son mapas de una experiencia —lo que se siente al respirar, al moverse, al quedarse quieto— y se recorren como mapas: con atención y respeto, no para diagnosticar.</p>'''),
 ('''    <h3>La Ciencia de lo Sutil</h3>
    <p>La física moderna confirma lo que los antiguos sabían:</p>
    <ul>
      <li>Biofotones: Las células emiten luz coherente</li>
      <li>Campos Bioeléctricos: Cada órgano genera campos medibles</li>
      <li>Coherencia Cuántica: Los sistemas vivos mantienen orden cuántico</li>
      <li>Energía del Punto Cero: Fuente infinita de energía en el vacío</li>
      <li>Campos Morfogenéticos: Plantillas energéticas de forma</li>
    </ul>''',
  '''    <h3>Lo que Sí Se Mide</h3>
    <ul>
      <li>Biofotones: El cuerpo emite una luz unas mil veces más tenue de lo que el ojo puede ver; Kobayashi y su equipo la fotografiaron en 2009, y todavía se estudia qué significa</li>
      <li>Campos Bioeléctricos: Los registran el electrocardiograma de Einthoven, desde principios del siglo XX, y el electroencefalograma de Berger</li>
    </ul>'''),
 # II
 ('<p>Los meridianos son canales por donde fluye el Chi:</p>',
  '<p>En la medicina china, los meridianos son los canales por donde fluye el qi. Hoy la acupuntura también se estudia: en el dolor crónico, una revisión con más de veinte mil pacientes (Vickers y otros, 2018) encontró que alivia más que no tratarlo, y algo más que una acupuntura simulada.</p>'),
 ('''    <h3>Diagnóstico por Meridianos</h3>
    <p>Cada meridiano revela desequilibrios específicos:</p>''',
  '''    <h3>Cómo los Lee la Tradición</h3>
    <p>En manos de quien se formó en ella, y junto a la medicina que diagnostica, la tradición distingue:</p>'''),
 ('<h4>3. Sonidos Sanadores Taoístas</h4>',
  '<h4>3. Sonidos Sanadores Taoístas (<em>liu zi jue</em>)</h4>'),
 # III
 ('<p>Los chakras son vórtices donde se encuentran múltiples meridianos:</p>',
  '<p>En la tradición del yoga y del tantra, los chakras son ruedas de energía a lo largo de la columna. Las sílabas y los elementos vienen de textos tántricos como el <em>Ṣaṭ-cakra-nirūpaṇa</em> (1577), que Arthur Avalon tradujo como <em>El poder serpentino</em> (1919); los colores del arcoíris y las notas musicales se sumaron en el siglo XX.</p>'),
 ('''    <h3>Diagnóstico Chakra</h3>
    <p>Chakra Hipoactivo: Área fría, colores apagados, rotación lenta<br>
    Chakra Hiperactivo: Área caliente, colores intensos, rotación rápida<br>
    Chakra Bloqueado: Sin rotación, sensación densa<br>
    Chakra Desalineado: Rotación irregular, posición desplazada</p>

    <h3>Protocolo de Armonización de Chakras</h3>''',
  '''    <p>No se diagnostican: se contemplan.</p>

    <h3>Práctica de Armonización de Chakras</h3>'''),
 ('<p><strong>2. ACTIVACIÓN ASCENDENTE (21 min - 3 min/chakra)</strong></p>',
  '<p><strong>2. RECORRIDO ASCENDENTE (21 min - 3 min/chakra)</strong></p>'),
 ('<li>Programar equilibrio continuo</li>', '<li>Intención de equilibrio</li>'),
 # IV
 ('<p>Los nadis son canales sutiles más finos que los meridianos:</p>',
  '<p>Los textos del hatha yoga hablan de setenta y dos mil nadis, canales sutiles más finos que los meridianos:</p>'),
 ('''      <li>Intuición y receptividad</li>
      <li>Sistema parasimpático</li>''', '''      <li>Intuición y receptividad</li>'''),
 ('''      <li>Lógica y acción</li>
      <li>Sistema simpático</li>''', '''      <li>Lógica y acción</li>'''),
 ('''    <ol>
      <li>Cerrar fosa derecha, inhalar por izquierda (4 seg)</li>
      <li>Cerrar ambas, retener (16 seg)</li>
      <li>Abrir derecha, exhalar (8 seg)</li>
      <li>Inhalar por derecha (4 seg)</li>
      <li>Cerrar ambas, retener (16 seg)</li>
      <li>Abrir izquierda, exhalar (8 seg)</li>
      <li>Esto es un ciclo, realizar 10 ciclos</li>
    </ol>''',
  '''    <ol>
      <li>Cerrar fosa derecha, inhalar por izquierda (4 seg)</li>
      <li>Cerrar izquierda, exhalar por derecha (6 seg)</li>
      <li>Inhalar por derecha (4 seg)</li>
      <li>Cerrar derecha, exhalar por izquierda (6 seg)</li>
      <li>Esto es un ciclo, realizar 10 ciclos</li>
    </ol>
    <p>La retención clásica, en la proporción de uno, cuatro y dos, se aprende después y con maestro, y no se practica en el embarazo ni con la presión alta sin consultar.</p>'''),
 ('''      <li>Equilibra hemisferios cerebrales</li>
      <li>Armoniza sistema nervioso</li>''', '''      <li>Armoniza sistema nervioso</li>'''),
 ('''      <li>20-30 respiraciones rápidas</li>
      <li>Inhalar profundo y retener</li>
      <li>Exhalar lentamente</li>
      <li>3 rondas</li>
    </ol>''',
  '''      <li>20-30 respiraciones rápidas</li>
      <li>Inhalar profundo, sin retener</li>
      <li>Exhalar lentamente</li>
      <li>3 rondas</li>
    </ol>
    <p>Es una respiración intensa: si aparecen mareos, hormigueos o angustia, para. No se practica en el embarazo, con problemas del corazón o de presión, epilepsia o ataques de pánico.</p>'''),
 ('''      <li>Aumenta energía vital</li>
      <li>Limpia toxinas</li>
      <li>Activa fuego digestivo</li>
      <li>Despierta kundalini</li>
      <li>Claridad mental</li>''', '''      <li>Aumenta energía vital</li>
      <li>Activa fuego digestivo</li>
      <li>Claridad mental</li>'''),
 # V
 ('<p>El aura es el campo electromagnético bioplasmático que rodea el cuerpo:</p>',
  '<p>La teosofía describió el aura a comienzos del siglo XX, y Barbara Brennan la ordenó en siete capas en <em>Manos que curan</em> (1987):</p>'),
 ('<h4>Cuerpo Etérico (5-10 cm)</h4>', '<h4>Cuerpo Etérico</h4>'),
 ('<h4>Cuerpo Emocional (30-60 cm)</h4>', '<h4>Cuerpo Emocional</h4>'),
 ('<h4>Cuerpo Mental (60-90 cm)</h4>', '<h4>Cuerpo Mental</h4>'),
 ('''    <h3>Lectura del Aura</h3>
    <p>Colores y Significados:</p>''', '''    <h3>El Lenguaje de los Colores</h3>
    <p>Los colores, como símbolos para las visualizaciones:</p>'''),
 ('''    PLATA: Habilidades psíquicas<br>
    NEGRO: Bloqueos, protección<br>
    GRIS: Depresión, enfermedad</p>''', '''    PLATA: Habilidades psíquicas</p>'''),
 # VI
 ('''      <li>Experiencias místicas</li>
    </ul>

    <h3>Prácticas Seguras de Activación</h3>''',
  '''      <li>Experiencias místicas</li>
    </ul>
    <p>Estos fenómenos también pueden ser señales de otras cosas. Si traen noches sin sueño, pensamientos que corren, una misión urgente, mensajes de guías o la certeza de saber lo que va a pasar, no es la kundalini que sube: es el momento de pedir ayuda, esa misma semana. Stanislav y Christina Grof llamaron emergencia espiritual a las crisis que a veces acompañan un despertar, y enseñaron que se atraviesan acompañadas. La tradición del yoga lo sabe desde antes: la kundalini se despierta despacio y con maestro.</p>

    <h3>Prácticas con Guía</h3>
    <p>No se busca forzar el despertar: la tradición misma advierte contra apurarlo.</p>'''),
 ('<h4>Sat Kriya (Práctica Kundalini Yoga)</h4>',
  '<h4>Sat Kriya (del kundalini yoga de Yogi Bhajan)</h4>'),
 # VII
 ('<p>Los Cinco Principios:</p>',
  '<p>Los Cinco Principios, que Mikao Usui enseñó en Japón en la década de 1920:</p>'),
 ('<p>Total: 24 minutos de autosanación</p>',
  '<p>Total: 24 minutos de autocuidado. El reiki acompaña; no reemplaza ningún tratamiento.</p>'),
 ('''      <li>Previene estancamientos</li>
      <li>Nutre órganos</li>
      <li>Clarifica mente</li>
      <li>Aumenta vitalidad</li>
    </ul>''',
  '''      <li>Calma y centra</li>
      <li>Clarifica mente</li>
      <li>Da sensación de vitalidad</li>
    </ul>
    <p>El tai chi y el qi gong se estudian hoy con buenos resultados en el equilibrio y en la prevención de caídas de las personas mayores.</p>'''),
 ('''      <li>Escanear campo energético</li>
      <li>Identificar congestiones</li>''', '''      <li>Escanear campo energético</li>'''),
]
CRIST = open('/home/claude/origen10/x5_crist.txt',encoding='utf-8').read()
R05 += [
 (CRIST, ''),
 # IX → VIII
 ('''    <h2>IX. Alimentación Pránica</h2>
    <h3>Niveles de Nutrición Energética</h3>
    <p>Comida Física: Sólidos y líquidos<br>
    Prana de Alimentos: Fuerza vital en comida fresca<br>
    Prana del Agua: Agua estructurada y bendecida<br>
    Prana del Aire: Respiración consciente<br>
    Prana Solar: Sungazing seguro<br>
    Prana Cósmico: Alimentación directa del campo</p>''',
  '''    <h2>VIII. El Alimento y el Aliento</h2>
    <h3>Niveles de Nutrición</h3>
    <p>Comida Física: Sólidos y líquidos<br>
    Prana de Alimentos: Fuerza vital en comida fresca<br>
    Prana del Agua: Agua limpia y bendecida<br>
    Prana del Aire: Respiración consciente</p>
    <p>El cuerpo necesita comida. La luz del sol nutre la piel y el ánimo, pero mirarlo de frente daña la retina, y quienes intentaron vivir solo de luz enfermaron; algunos murieron.</p>'''),
]
AYUNO = open('/home/claude/origen10/x5_ayuno.txt',encoding='utf-8').read()
R05 += [
 (AYUNO, '    <div class="section-divider"></div>\n\n'),
 # X → IX
 ('''    <h2>X. Protección Energética</h2>
    <h3>Vampirismo Energético</h3>
    <p>Señales de drenaje energético:</p>
    <ul>
      <li>Fatiga súbita en presencia de alguien</li>
      <li>Dolor de cabeza después de interacciones</li>
      <li>Sensación de vacío</li>
      <li>Emociones ajenas pegadas</li>
      <li>Sueños perturbadores</li>
    </ul>

    <h3>Técnicas de Protección</h3>

    <h4>Escudo de Espejo</h4>
    <ol>
      <li>Visualizar espejos alrededor</li>
      <li>Cara reflectante hacia afuera</li>
      <li>Devuelven energías negativas</li>
      <li>Permiten entrada de luz</li>
      <li>Renovar cada mañana</li>
    </ol>

    <h4>Capa de Luz Violeta</h4>''',
  '''    <h2>IX. Los Vínculos que Cansan</h2>
    <h3>Cuando Alguien nos Desgasta</h3>
    <p>Hay vínculos que nos dejan agotados. A veces es la tensión, a veces una relación que pide límites, y a veces el cansancio habla de nuestra propia salud y merece una consulta.</p>
    <p>Señales de que un vínculo te desgasta:</p>
    <ul>
      <li>Fatiga súbita en presencia de alguien</li>
      <li>Sensación de vacío</li>
      <li>Emociones ajenas pegadas</li>
    </ul>

    <h3>Prácticas de Cuidado</h3>

    <h4>Capa de Luz Violeta</h4>
    <p>Una imagen para calmarse antes de un encuentro difícil:</p>'''),
 ('''    <h4>Cordones de Corte</h4>
    <ol>
      <li>Escanear cordones energéticos</li>
      <li>Identificar conexiones tóxicas</li>
      <li>Espada de luz azul</li>
      <li>Cortar con amor</li>
      <li>Sellar con luz dorada</li>
      <li>Enviar bendiciones</li>
    </ol>''',
  '''    <h4>Poner Límites</h4>
    <ol>
      <li>Decir que no</li>
      <li>Irse antes</li>
      <li>Tomar distancia</li>
    </ol>
    <p>Si sientes que otros te dañan a distancia, o que necesitas protegerte todo el tiempo, vale la pena hablarlo con un profesional: ese miedo también se cuida.</p>'''),
 # XI → X
 ('''    <h2>XI. Lugares de Poder</h2>
    <h3>Geografía Sagrada</h3>''', '''    <h2>X. Lugares Sagrados</h2>
    <h3>Geografía Sagrada</h3>'''),
 ('<li>Líneas Ley: Meridianos terrestres</li>',
  '<li>Líneas Ley: Alfred Watkins llamó así, en los años veinte, a alineaciones de sitios antiguos en Inglaterra; la idea de que eran líneas de energía llegó medio siglo después</li>'),
 ('''    <h3>Los Chakras de la Tierra</h3>
    <p>Monte Shasta (California) - Chakra Raíz<br>''',
  '''    <h3>Los Chakras de la Tierra</h3>
    <p>Un esquema moderno ordena estos lugares como chakras del planeta; sus pueblos los veneran por razones propias. El Kailash es sagrado para hindúes, budistas, jainistas y el bön. Uluru es sagrado para el pueblo anangu, que pidió dejar de escalarlo, y desde 2019 ya no se escala.</p>
    <p>Monte Shasta (California) - Chakra Raíz<br>'''),
 ('''    Monte Kailash (Tíbet) - Chakra Corona</p>''',
  '''    Monte Kailash (Tíbet) - Chakra Corona</p>
    <p>Visitar un lugar sagrado es entrar en la casa de otros: se pide permiso, se cuida, se escucha.</p>'''),
 ('<p><strong>ACTIVACIÓN DE ESPACIO:</strong></p>', '<p><strong>PREPARAR EL ESPACIO:</strong></p>'),
 # XII → XI
 ('<h2>XII. Integración Energética</h2>', '<h2>XI. Integración Energética</h2>'),
 ('<li>Escudo protector (2 min)</li>', '<li>Intención del día (2 min)</li>'),
 # XIII → XII (con el rescate de las cámaras de plasma)
 ('''    <h2>XIII. La Medicina Vibracional del Futuro</h2>
    <h3>Tecnologías Emergentes</h3>
    <p>Dispositivos de Biorresonancia: Detectan y corrigen desequilibrios<br>
    Cámaras de Plasma: Regeneración celular<br>
    Frecuencias de Rife: Eliminación de patógenos<br>
    Terapia de Luz: Fotobiomodulación<br>
    Campos PEMF: Estimulación electromagnética</p>''',
  '''    <h2>XII. La Medicina Vibracional del Futuro</h2>
    <h3>Tecnologías Emergentes</h3>
    <p>Terapia de Luz: La luz de baja intensidad ya se usa para prevenir las llagas de la boca en algunos tratamientos contra el cáncer<br>
    Campos PEMF: Los campos electromagnéticos pulsados se aprobaron hace décadas para ayudar a soldar fracturas que no consolidan<br>
    Cámaras de Plasma: El plasma frío se usa en heridas crónicas, y en Alemania ya está aprobado como dispositivo médico; la regeneración que promete es un horizonte que se investiga</p>'''),
 ('<li>Lector de campos sutiles</li>', '<li>Atento a lo que el cuerpo expresa</li>'),
 ('''      <li>Arquitecto de campos</li>
      <li>Puente dimensional</li>
    </ul>''', '''      <li>Arquitecto de campos</li>
      <li>Puente dimensional</li>
      <li>Un compañero que sabe derivar a tiempo</li>
    </ul>'''),
 # XIV → XIII
 ('''    <h2>XIV. Síntesis: El Río de Vida</h2>
    <p>La energía vital nos revela que somos ríos, no lagos. Estamos diseñados para fluir, no para estancarnos. La enfermedad es el río bloqueado, la salud es el flujo libre y abundante.</p>''',
  '''    <h2>XIII. Síntesis: El Río de Vida</h2>
    <p>La energía vital nos revela que somos ríos, no lagos. Estamos diseñados para fluir, no para estancarnos. Cuando algo se estanca, el cuidado ayuda a que vuelva a correr; y aun el río que atraviesa piedras sigue siendo río.</p>'''),
 ('No necesitamos añadir energía desde afuera; necesitamos liberar los bloqueos que impiden el flujo natural de la fuerza vital infinita que ya somos.</p>',
  'A veces basta con liberar lo que impide el flujo, y a veces hace falta ayuda de afuera: el río también recibe afluentes.</p>'),
 ('Mi energía circula libre y abundantemente. Cada chakra gira en armonía perfecta. Cada meridiano fluye sin obstáculos.',
  'Dejo que mi energía circule. Acompaño a cada chakra hacia su armonía. Cuido los caminos por donde fluye mi vida.'),
 ('''    Encuentro la salud, la paz, el éxtasis del Ser."</blockquote>
''',
  '''    Encuentro la salud, la paz, el éxtasis del Ser."</blockquote>

    <aside class="puerta arquitectura" aria-label="Puerta hacia Arquitectura del Destino">
      <p class="p-nombre">Puerta</p>
      <p class="p-texto">Por qué casi todos los nombres de la fuerza vital significan, antes que nada, aliento, y cómo lenguas que no se conocían pusieron lo más alto en lo más corporal, se despliega en <em>El Cuerpo</em>, Libro 4 de <em>Arquitectura del Destino</em>, Umbral IV: «Muchos nombres para un soplo».</p>
      <a class="cruzar" href="https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/libro-04-el-cuerpo/L04-U4.html">Cruzar ⟶</a>
    </aside>
'''),
 ('Pero hay una dimensión aún más profunda donde la sanación ocurre en el reino del alma misma, donde los contratos kármicos se revelan y las heridas ancestrales encuentran redención.',
  'Pero hay una dimensión más honda, donde la sanación toca el alma y la historia: lo que heredamos, lo que dejamos atrás, lo que nos sostiene.'),
]

R['nodo_05.html'] = R05
R06 = [
 ('<title>Nodo 6 – Sanación del Alma y Medicina Ancestral | Sanación Integral | Trinity Origen</title>\n',
  '<title>Nodo 6 – Sanación del Alma y Medicina Ancestral | Sanación Integral | Trinity Origen</title>\n' + NOTA),
 ('</style>\n</head>', CSS.lstrip('\n')),
 ('Cada trauma no sanado de nuestros ancestros vive en nosotros, esperando redención.',
  'Lo que nuestros ancestros no pudieron sanar a veces nos llega, esperando ser mirado.'),
 # I
 ('<p>El alma porta un archivo completo de todas sus experiencias:</p>',
  '<p>La teosofía del siglo XIX tomó la palabra sánscrita <em>akasha</em> —el espacio, el éter— para nombrar un archivo de todo lo vivido; Edgar Cayce la volvió popular en el siglo XX. Según esta tradición, el alma porta un archivo completo de todas sus experiencias:</p>'),
 ('<p>Estos registros no son pasivos; influyen activamente en la vida presente.</p>',
  '<p>Para esta tradición, estos registros influyen en la vida presente.</p>'),
 # II
 ('''      <li>Fobias sin origen conocido</li>''',
  '''      <li>Fobias sin origen conocido (una fobia se trata, y bien, con terapia)</li>'''),
 ('''      <li>Relaciones kármicas intensas</li>
      <li>Enfermedades "sin causa"</li>
      <li>Sincronicidades extraordinarias</li>
    </ul>''',
  '''      <li>Relaciones kármicas intensas</li>
      <li>Sincronicidades extraordinarias</li>
    </ul>
    <p>El Buda advirtió que los frutos del karma son uno de los cuatro asuntos que no conviene tratar de calcular: quien lo intenta, dijo, termina en la confusión y el desvarío (<em>Anguttara Nikaya</em> 4.77). El karma mira hacia adelante, hacia lo que hago ahora; no sirve para explicar por qué alguien enferma.</p>'''),
 ('<p>PROCESO GUIADO:</p>', '<p>PROCESO GUIADO, con alguien formado:</p>'),
 ('<li>Revivir momento crucial</li>', '<li>Observar el momento crucial, sin revivirlo</li>'),
 ('''    <h4>3. Ho'oponopono Kármico</h4>
    <p>Para cada patrón/persona kármica:</p>''',
  '''    <h4>3. Ho'oponopono Kármico</h4>
    <p>Es una práctica hawaiana de reconciliación que Morrnah Simeona adaptó en los años setenta; las cuatro frases son su forma más difundida. Para cada patrón/persona kármica:</p>'''),
 ('<p>Repetir hasta sentir liberación completa.</p>', '<p>Repetir sin apuro, las veces que haga falta.</p>'),
 # III
 ('<li>Traumas de 7 generaciones atrás</li>', '<li>Huellas de las generaciones anteriores</li>'),
 ('''    <p>La ciencia confirma lo que los chamanes siempre supieron:</p>
    <ul>
      <li>Los traumas modifican el ADN</li>
      <li>Estas modificaciones se heredan</li>
      <li>Pueden activarse o desactivarse</li>
      <li>Respondemos a memorias no nuestras</li>
      <li>Podemos sanar hacia atrás en el tiempo</li>
    </ul>''',
  '''    <p>Rachel Yehuda estudió a hijos de sobrevivientes del Holocausto y encontró diferencias en un gen que regula el estrés (2016); Brian Dias y Kerry Ressler vieron en ratones que el miedo aprendido a un olor aparecía en sus crías y en sus nietos (2014). Son hallazgos que la ciencia sigue discutiendo. Lo que nadie discute es lo que pasa de una generación a otra por el trato, las palabras y los silencios, y eso puede empezar a cambiar hoy.</p>'''),
 ('''    <h3>Constelaciones Familiares Sanadoras</h3>
    <p><strong>Protocolo de Constelación Personal:</strong></p>''',
  '''    <h3>Constelaciones Familiares Sanadoras</h3>
    <p>Bert Hellinger desarrolló las constelaciones familiares en las últimas décadas del siglo XX; muchas personas las encuentran reveladoras, y la investigación sobre ellas es escasa. Aquí, una versión personal, con objetos:</p>
    <p><strong>Práctica de Constelación Personal:</strong></p>'''),
 ('''      <li>Cierre del campo</li>
    </ul>

    <h3>Sanación del Linaje Materno</h3>''',
  '''      <li>Cierre del campo</li>
    </ul>
    <p>Honrar no significa justificar: quien sufrió abuso no necesita darle un lugar a quien lo dañó para sanar.</p>

    <h3>Sanación del Linaje Materno</h3>'''),
 ('''      <li>Transmitir fortaleza sanada</li>
    </ol>''',
  '''      <li>Transmitir fortaleza sanada</li>
    </ol>
    <p>Si tu madre o tu padre fue fuente de daño, puedes poner detrás de ti a quien te cuidó, o empezar por la abuela que sí te sostuvo.</p>'''),
 # IV
 ('<p>Antes de nacer, el alma establece:</p>',
  '<p>Michael Newton describió en <em>El viaje de las almas</em> (1994) un consejo de sabios entre una vida y otra. Según esta tradición, antes de nacer, el alma establece:</p>'),
 ('''      <li>Contratos de Despertar: Momentos de activación</li>
    </ul>''',
  '''      <li>Contratos de Despertar: Momentos de activación</li>
    </ul>
    <p>Es una imagen para el asombro ante ciertos encuentros, no una explicación del daño: ninguna enfermedad ni ningún maltrato estaban pactados.</p>'''),
 ('<p>PROCESO DE REVISIÓN:</p>', '<p>MEDITACIÓN DE REVISIÓN:</p>'),
 # V
 ('''    <h3>La Fragmentación del Alma</h3>
    <p>El alma puede fragmentarse por:</p>''',
  '''    <h3>La Fragmentación del Alma</h3>
    <p>Muchos pueblos hablan de pérdida del alma; en América Latina se la llama susto. Según esta tradición, el alma puede fragmentarse por:</p>'''),
 ('''      <li>Sustos extremos</li>
      <li>Anestesias/cirugías</li>''', '''      <li>Sustos extremos</li>'''),
 ('''      <li>Relaciones tóxicas</li>
    </ul>

    <h3>Síntomas de Pérdida del Alma</h3>
    <ul>
      <li>Sensación de vacío</li>
      <li>Depresión sin causa</li>
      <li>Desconexión de la vida</li>
      <li>Pérdida de memoria</li>
      <li>Adicciones compulsivas</li>
      <li>Incapacidad de seguir adelante</li>
      <li>Sensación de no estar completo</li>
    </ul>''',
  '''      <li>Relaciones tóxicas</li>
    </ul>
    <p>La psicología llamó disociación, desde Pierre Janet (1889), a algo parecido: partes de la experiencia que quedan apartadas después de un golpe muy fuerte. Se trabaja en terapia, y se recupera.</p>

    <h3>Síntomas de Pérdida del Alma</h3>
    <ul>
      <li>Sensación de vacío</li>
      <li>Desconexión de la vida</li>
      <li>Incapacidad de seguir adelante</li>
      <li>Sensación de no estar completo</li>
    </ul>
    <p>Si hay pérdidas de memoria, depresión o adicciones, además del camino del alma hace falta el de la salud: piden ayuda.</p>'''),
 ('<p><strong>Protocolo Chamánico:</strong></p>',
  '<p><strong>Protocolo Chamánico:</strong> lo realiza un practicante formado en esa tradición; no es un viaje para hacer a solas, y no reemplaza la terapia del trauma.</p>'),
 # VI
 ('''    <h3>Influencias de Vidas Anteriores</h3>
    <p>Síntomas con origen en vidas pasadas:</p>
    <ul>
      <li>Fobias específicas inexplicables</li>
      <li>Dolores crónicos sin causa física</li>''',
  '''    <h3>Influencias de Vidas Anteriores</h3>
    <p>Ian Stevenson, psiquiatra de la Universidad de Virginia, reunió durante décadas casos de niños que decían recordar otra vida, algunos con marcas de nacimiento que correspondían a heridas de esa vida. Su trabajo despierta asombro y discusión. La tradición reconoce como señales:</p>
    <ul>
      <li>Fobias específicas inexplicables</li>'''),
 ('''    <h3>Técnicas de Regresión</h3>
    <p><strong>Autohipnosis Regresiva:</strong></p>''',
  '''    <h3>Viaje Imaginal</h3>
    <p>Se recorre como un relato simbólico, sin preguntarse si ocurrió: lo que importa es lo que te muestra hoy. La memoria es moldeable, y Elizabeth Loftus mostró que puede llenarse de recuerdos que se sienten verdaderos sin serlo; por eso las regresiones que buscan hechos se hacen con alguien formado.</p>'''),
 ('''      <li>Crear puente energético</li>
      <li>Transferir habilidad</li>''',
  '''      <li>Imaginar a quien dominó ese arte</li>
      <li>Practicarlo con paciencia</li>'''),
 # VII
 ('<li>Phowa (transferencia de consciencia)</li>', '<li>Phowa (transferencia de consciencia, de la tradición tibetana)</li>'),
 ('<li>Guiar hacia el túnel</li>', '<li>Guiar hacia el túnel que describen quienes vivieron experiencias cercanas a la muerte</li>'),
 ('<li>Mantener vigilia 49 días</li>', '<li>Mantener vigilia 49 días, los del bardo tibetano</li>'),
 ('''      <li>Ceremonias de liberación</li>
    </ol>''',
  '''      <li>Ceremonias de liberación</li>
    </ol>
    <p>Acompañar a quien muere es también cuidar su cuerpo: el alivio del dolor, la boca húmeda, la mano tomada.</p>'''),
 ('''      <li>Celebrar el amor eterno</li>
    </ol>''',
  '''      <li>Celebrar el amor eterno</li>
    </ol>
    <p>Dennis Klass, Phyllis Silverman y Steven Nickman llamaron vínculos continuos (1996) a lo que muchos duelos muestran: el lazo con quien murió no se corta, se transforma. El duelo no se saltea; se atraviesa, y nadie tiene que hacerlo solo.</p>'''),
 # VIII
 ('''    <p><strong>Ritual de Sanación Colectiva:</strong></p>
    <ol>
      <li>Identificar trauma colectivo</li>
      <li>Convocar almas afectadas</li>
      <li>Círculo de sanación etérica</li>
      <li>Reconocimiento del dolor</li>
      <li>Proceso de perdón masivo</li>
      <li>Liberación de las memorias</li>
      <li>Implantación de nueva frecuencia</li>
      <li>Bendición para generaciones futuras</li>
    </ol>''',
  '''    <p><strong>Ritual de Memoria Colectiva:</strong></p>
    <ol>
      <li>Identificar trauma colectivo</li>
      <li>Nombrar a las víctimas</li>
      <li>Encender una luz por ellas</li>
      <li>Reconocimiento del dolor</li>
      <li>Reparar lo que en el presente se pueda reparar</li>
      <li>Bendición para generaciones futuras</li>
    </ol>
    <p>Así lo hacen las pequeñas placas con nombre que Gunter Demnig empezó a colocar en los años noventa frente a las casas de víctimas del nazismo. El perdón de un daño colectivo no se decreta: lo dan, si quieren, quienes lo sufrieron.</p>'''),
 # IX
 ('''    <h2>IX. Activación de Códigos del Alma</h2>
    <h3>Códigos Dormidos</h3>
    <p>El alma porta códigos de activación:</p>
    <ul>
      <li>Códigos de maestría</li>
      <li>Códigos de sanación</li>
      <li>Códigos de abundancia</li>
      <li>Códigos de amor</li>
      <li>Códigos de poder</li>
      <li>Códigos de sabiduría</li>
      <li>Códigos de ascensión</li>
    </ul>

    <h3>Activación por Frecuencia</h3>
    <p><strong>PROTOCOLO DE ACTIVACIÓN:</strong></p>
    <ol>
      <li>Estado gamma de consciencia</li>
      <li>Invocar Yo Superior</li>
      <li>Solicitar activación específica</li>
      <li>Recibir transmisión de luz</li>
      <li>Integrar en ADN</li>
      <li>Período de calibración</li>
      <li>Expresión del código</li>
    </ol>

    <h3>Geometrías de Activación</h3>
    <p><strong>Merkaba del Alma:</strong></p>
    <p>Visualización:</p>
    <ul>
      <li>Tetraedro de luz ascendente</li>
      <li>Tetraedro de luz descendente</li>
      <li>Rotación opuesta acelerada</li>
      <li>Campo merkaba activado</li>
      <li>Códigos del alma online</li>
      <li>Conexión multidimensional</li>
    </ul>''',
  '''    <h2>IX. Dones del Alma</h2>
    <h3>Dones Dormidos</h3>
    <p>El alma porta dones que esperan expresarse:</p>
    <ul>
      <li>Dones de maestría</li>
      <li>Dones de sanación</li>
      <li>Dones de abundancia</li>
      <li>Dones de amor</li>
      <li>Dones de poder</li>
      <li>Dones de sabiduría</li>
    </ul>

    <h3>Despertar un Don</h3>
    <ol>
      <li>Recordar un momento en que ese don se mostró</li>
      <li>Nombrarlo</li>
      <li>Ofrecerlo hoy en un gesto pequeño</li>
    </ol>

    <h3>Geometrías de Activación</h3>
    <p><strong>Merkaba del Alma:</strong> la merkabá, el carro de la visión de Ezequiel, dio nombre a una de las primeras místicas judías. Los dos tetraedros que giran son una visualización de los años noventa.</p>
    <p>Visualización:</p>
    <ul>
      <li>Tetraedro de luz ascendente</li>
      <li>Tetraedro de luz descendente</li>
      <li>Conexión multidimensional</li>
    </ul>'''),
 # X
 ('''      <li>Elementos tierra</li>
    </ul>''',
  '''      <li>Elementos tierra</li>
    </ul>
    <p>Es pariente del altar del Día de Muertos de México, que la UNESCO reconoce como patrimonio de la humanidad.</p>'''),
 ('''      <li>Rapé: Limpieza y enraizamiento</li>
    </ul>''',
  '''      <li>Rapé: Limpieza y enraizamiento</li>
    </ul>
    <p>Estas plantas son medicina dentro de sus tradiciones, con quienes las conocen y en su contexto ceremonial. Fuera de él pueden dañar: la ayahuasca combinada con algunos antidepresivos puede ser peligrosa, los cactus y los hongos pueden desencadenar crisis en quien tuvo una psicosis, y el tabaco, sagrado en la Amazonía, fumado a diario es la primera causa de muerte evitable.</p>'''),
 # XI
 ('<p>Señales de Maldición Activa:</p>', '<p>La tradición reconoce como señales de maldición:</p>'),
 ('''      <li>Accidentes frecuentes</li>
    </ul>''',
  '''      <li>Accidentes frecuentes</li>
    </ul>
    <p>Lo que una familia vive como maldición a veces tiene otro nombre: una enfermedad hereditaria que se puede estudiar, un duelo que nadie hizo, un secreto. Si en tu familia se repiten enfermedades o muertes tempranas, el ritual puede acompañar, y la consulta médica puede proteger a los que vienen.</p>'''),
 # XII
 ('''      <li>Promesa de cuidado continuo</li>
    </ol>''',
  '''      <li>Promesa de cuidado continuo</li>
    </ol>
    <p>Si al encontrarte con estos niños aparece tu propia herida, sobre todo si hubo abuso, no hace falta recorrerla a solas.</p>'''),
 # XIII
 ('<li>¿Cuál es el origen kármico de mi enfermedad?</li>', '<li>¿Qué necesito aprender de esta etapa?</li>'),
 ('''      <li>¿Cómo puedo servir mejor a mi linaje?</li>
    </ul>''',
  '''      <li>¿Cómo puedo servir mejor a mi linaje?</li>
    </ul>
    <p>Lo que se recibe así se toma como se toma un sueño o una intuición: con respeto, y sin que reemplace las decisiones que piden información y consejo.</p>'''),
 # XIV
 ('<p>Muchas enfermedades surgen porque el alma no habita completamente el cuerpo:</p>',
  '<p>Muchas tradiciones hablan de habitar el cuerpo del todo, de llegar a él:</p>'),
 ('''    <p>Cuando el alma y la personalidad se alinean:</p>
    <ul>
      <li>Desaparecen conflictos internos</li>
      <li>La salud se restaura naturalmente</li>
      <li>Los recursos fluyen abundantemente</li>
      <li>Las relaciones se armonizan</li>
      <li>El propósito se clarifica</li>
      <li>Los milagros se vuelven normales</li>
    </ul>''',
  '''    <p>Cuando el alma y la personalidad se alinean, la vida suele ganar claridad: los conflictos se entienden mejor, las decisiones pesan menos, el propósito se aclara. No es un seguro contra la enfermedad ni contra la pérdida: es una manera de atravesarlas.</p>'''),
 # XV
 ('<li>Ver la perfección oculta</li>', '<li>Reconocer lo que aprendiste, si lo hubo</li>'),
 ('''      <li>Bendecir el camino</li>
    </ul>''',
  '''      <li>Bendecir el camino</li>
    </ul>
    <p>Perdonar no obliga a quedarse, ni a callar, ni a reconciliarse, y no hace falta perdonar para sanar.</p>'''),
 ('''    <blockquote>"Perdono totalmente.<br>
    Soy perdonado totalmente.<br>''',
  '''    <blockquote>"Perdono lo que hoy puedo perdonar.<br>
    Me perdono lo que hoy puedo perdonarme.<br>'''),
 # XVI
 ('<p>A veces el alma necesita una muerte simbólica para renacer:</p>',
  '<p>Arnold van Gennep describió en 1909 los tres tiempos de todo rito de paso: uno se separa de lo que era, permanece un tiempo en el umbral y vuelve con un lugar nuevo. A veces el alma necesita una muerte simbólica para renacer:</p>'),
 ('''      <li>Acostarse como muerto</li>
      <li>Soltar el aliento vital</li>
      <li>Disolverse en el vacío</li>''',
  '''      <li>Acostarse en la postura que el hatha yoga llama <em>śavāsana</em>, la del cadáver</li>
      <li>Soltar el peso, no el aliento: respirar con calma</li>
      <li>Dejar que se aquieten los nombres y los roles</li>'''),
 ('''      <li>Compromisos renovados</li>
    </ul>''',
  '''      <li>Compromisos renovados</li>
    </ul>
    <p>Esta práctica es para despedir lo que termina, no para alejarse de la vida. Si al practicarla aparece la idea de no querer estar, detén la práctica y pide ayuda hoy mismo: no es un fracaso ni una profundidad mayor, es una señal de que necesitas compañía, y esa ayuda existe. Tampoco es para los días de un duelo reciente.</p>'''),
 # XVII
 ('Cada enfermedad tiene una historia del alma. Cada síntoma es un ancestro pidiendo ser visto. Cada dolor es una memoria buscando liberación.',
  'Cada vida tiene una historia del alma. Cada linaje guarda ancestros pidiendo ser vistos. Cada dolor, además de su cuidado, puede encontrar un sentido.'),
 ('<p>La medicina del alma no trata síntomas; libera historias. No cura enfermedades; completa ciclos. No elimina problemas; integra lecciones.',
  '<p>La medicina del alma no trata síntomas ni cura enfermedades: de eso se ocupa la otra, y las dos se necesitan. Ella libera historias, completa ciclos, integra lecciones.'),
 ('En nuestro ADN los códigos sagrados,<br>', 'En nuestra voz los cantos sagrados,<br>'),
 ('''    Sabiendo que su viaje no fue en vano."</blockquote>
''',
  '''    Sabiendo que su viaje no fue en vano."</blockquote>

    <aside class="puerta arquitectura" aria-label="Puerta hacia Arquitectura del Destino">
      <p class="p-nombre">Puerta</p>
      <p class="p-texto">Que el sueño sea una pequeña parte de la muerte, y que cada mañana se agradezca el alma devuelta, se despliega en <em>Las Pequeñas Muertes</em>, Libro 6 de <em>Arquitectura del Destino</em>, Umbral V: «El alma devuelta».</p>
      <a class="cruzar" href="https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/libro-06-las-pequenas-muertes/L06-U5.html">Cruzar ⟶</a>
    </aside>
'''),
]

R['nodo_06.html'] = R06
R07 = [
 ('<title>Nodo 7 – La Gran Síntesis | Sanación Integral | Trinity Origen</title>\n',
  '<title>Nodo 7 – La Gran Síntesis | Sanación Integral | Trinity Origen</title>\n' + NOTA),
 ('</style>\n</head>', CSS.lstrip('\n')),
 # I
 ('''sino la imagen completa con menor resolución.</p>
    <p>Esta es la naturaleza de la realidad misma:</p>''',
  '''sino la imagen completa con menor resolución. Dennis Gabor lo inventó en 1947 y recibió por eso el Nobel en 1971.</p>
    <p>Las tradiciones lo dijeron antes con otras palabras, y William Blake quiso ver un mundo en un grano de arena y un cielo en una flor silvestre:</p>'''),
 ('''      <li>Cada punto del espacio contiene todo el universo</li>
      <li>Cada enfermedad contiene su propia sanación</li>
      <li>Cada síntoma contiene el mensaje completo</li>''',
  '''      <li>Cada punto del espacio contiene todo el universo</li>'''),
 ('<h3>El Ser Humano como Holograma</h3>',
  '<h3>El Ser Humano como Holograma</h3>\n    <p>La <em>Tabla Esmeralda</em> de la tradición hermética lo resumió: como es arriba, es abajo.</p>'),
 ('''      <li>Sanando cualquier parte, sanamos el todo</li>
      <li>Sanando el todo, sanamos cada parte</li>
      <li>La información de sanación es no-local</li>
      <li>El cambio en un nivel afecta todos los niveles</li>
      <li>La sanación puede ser instantánea</li>
      <li>Cada técnica contiene todas las técnicas</li>
      <li>Cada sanador es todos los sanadores</li>''',
  '''      <li>Cuidar una parte alcanza al todo</li>
      <li>Cuidar el todo alcanza a cada parte</li>
      <li>El cambio en un nivel afecta todos los niveles</li>
      <li>Cada técnica puede abrir la puerta a las otras</li>
      <li>Cada sanador lleva consigo a todos sus maestros</li>'''),
 # II
 ('''    <h3>El Diagnóstico Holográfico</h3>
    <p><strong>Evaluación Multidimensional Completa:</strong></p>''',
  '''    <h3>La Escucha Integral</h3>
    <p>El diagnóstico lo hace la medicina, y va primero. Lo que se suma es una escucha más amplia:</p>'''),
 ('''      <li>Campo social</li>
      <li>Resonancia colectiva</li>''', '''      <li>Campo social</li>
      <li>Red de apoyo</li>'''),
 ('''    <h4>Nivel 3 - Cuántico</h4>
    <ul>
      <li>Frecuencias dominantes</li>
      <li>Coherencia de campos</li>
      <li>Patrones de interferencia</li>
      <li>Estados de superposición</li>
    </ul>''',
  '''    <h4>Nivel 3 - Ritmo y Vibración</h4>
    <ul>
      <li>El sueño</li>
      <li>La respiración</li>
      <li>Lo que calma: una voz, una música, un silencio</li>
    </ul>'''),
 ('''      <li>Creencias limitantes</li>
      <li>Programas subconscientes</li>''', '''      <li>Creencias limitantes</li>
      <li>Hábitos</li>'''),
 ('''    <h4>Nivel 5 - Energético</h4>
    <ul>''', '''    <h4>Nivel 5 - Energético (según las tradiciones, como mapa)</h4>
    <ul>'''),
 ('''    <h4>Nivel 6 - Kármico</h4>
    <ul>
      <li>Patrones del alma</li>
      <li>Cargas ancestrales</li>
      <li>Contratos activos</li>
      <li>Lecciones pendientes</li>
    </ul>''',
  '''    <h4>Nivel 6 - Biográfico y Ancestral</h4>
    <ul>
      <li>La historia familiar</li>
      <li>Los duelos</li>
      <li>Lo heredado</li>
      <li>Lecciones pendientes</li>
    </ul>'''),
 ('<li>Nivel de consciencia</li>', '<li>Fuentes de sentido</li>'),
 ('<li>Escaneo multidimensional</li>', '<li>Escucha de todos los niveles</li>'),
 ('''      <li>Tratamiento físico necesario</li>
      <li>Armonización energética</li>
      <li>Reprogramación mental</li>''',
  '''      <li>El tratamiento médico que corresponda, primero</li>
      <li>Armonización energética</li>
      <li>Trabajo con creencias y hábitos</li>'''),
 ('''    <p><strong>Fase 4: Calibración Cuántica</strong></p>
    <ul>
      <li>Colapsar nueva realidad</li>
      <li>Anclar nueva frecuencia</li>
      <li>Sellar campos</li>
      <li>Programar mantenimiento</li>
    </ul>''',
  '''    <p><strong>Fase 4: Cierre y Seguimiento</strong></p>
    <ul>
      <li>Revisar juntos lo que ayudó</li>
      <li>Acordar los próximos pasos</li>
      <li>Sostener lo logrado</li>
    </ul>'''),
 # III
 ('''      <li>Lectura instantánea de todos los campos</li>
      <li>Visualización 3D de desequilibrios</li>
      <li>Predicción de enfermedades futuras</li>''',
  '''      <li>Lectura instantánea de todos los campos</li>
      <li>Visualización 3D de desequilibrios</li>
      <li>Predicción de enfermedades futuras: ya empieza con la genética y con la inteligencia artificial, que lee riesgos en una foto del fondo de ojo</li>'''),
 ('''    <h4>2. Cámaras de Regeneración Cuántica</h4>
    <ul>
      <li>Campos de punto cero</li>
      <li>Frecuencias específicas</li>
      <li>Geometría sagrada</li>
      <li>Luz coherente</li>
      <li>Tiempo acelerado de sanación</li>
    </ul>''',
  '''    <h4>2. Cámaras de Regeneración</h4>
    <ul>
      <li>Luz de baja intensidad</li>
      <li>Campos pulsados, que ya ayudan a soldar huesos</li>
      <li>Señales bioeléctricas: en 2022, el equipo de Michael Levin logró que ranas adultas regeneraran una pata</li>
      <li>Tiempo acelerado de sanación</li>
    </ul>'''),
 ('''      <li>Medicamentos individualizados</li>
      <li>Estructuras energéticas</li>
    </ul>''',
  '''      <li>Medicamentos individualizados</li>
    </ul>
    <p>En 2024 se trasplantó por primera vez un riñón de cerdo a una persona viva.</p>'''),
 ('<li>Control mental de procesos</li>', '<li>Control mental de procesos: ya se mueven prótesis con implantes cerebrales</li>'),
 ('''    <h3>Inteligencia Artificial Consciente</h3>
    <p><strong>IA en Medicina Integral:</strong></p>''',
  '''    <h3>Inteligencia Artificial Consciente</h3>
    <p>Si algún día lo será, es una pregunta abierta; hoy ya es una aliada, y ayuda a leer imágenes como el fondo de ojo en la diabetes.</p>
    <p><strong>IA en Medicina Integral:</strong></p>'''),
 ('<li>Diagnóstico pattern recognition</li>', '<li>Reconocimiento de patrones en imágenes y análisis</li>'),
 ('''      <li>CRISPR para edición genética</li>
      <li>Terapias de ARN mensajero</li>''',
  '''      <li>CRISPR para edición genética: valió el Nobel de 2020 a Emmanuelle Charpentier y Jennifer Doudna, y en 2023 se aprobó la primera terapia que lo usa, que en sus ensayos dejó sin crisis de dolor a casi todos los pacientes con anemia falciforme</li>
      <li>Terapias de ARN mensajero: valieron el Nobel de 2023 a Katalin Karikó y Drew Weissman</li>'''),
 ('''      <li>Rejuvenecimiento celular</li>
      <li>Extensión de telómeros</li>
    </ul>''',
  '''      <li>Rejuvenecimiento celular: el equipo de Juan Carlos Izpisúa Belmonte rejuveneció tejidos y alargó la vida de ratones reprogramando sus células de manera parcial (2016)</li>
      <li>Extensión de telómeros: María Blasco la logró en ratones con terapia génica (2012)</li>
    </ul>'''),
 ('<li>Nanobots destructores de cáncer</li>', '<li>Nanobots destructores de cáncer: en ratones, unos robots de ADN ya cortaron el riego de tumores (2018)</li>'),
 ('<li>Delivery dirigido de fármacos</li>', '<li>Transporte dirigido de fármacos: así llegan a las células las vacunas de ARN mensajero</li>'),
 ('''      <li>Cirugía a nivel molecular</li>
    </ul>''',
  '''      <li>Cirugía a nivel molecular</li>
    </ul>
    <p>Este es el horizonte. A quien enferma hoy lo cuida lo que hoy existe, que ya es mucho, y cada año es más.</p>'''),
 # IV
 ('''    <p><strong>Diseño Holístico:</strong></p>''',
  '''    <p><strong>Diseño Holístico:</strong> en 1984, Roger Ulrich observó que los operados que veían árboles desde la cama se iban antes a casa.</p>'''),
 ('''      <li>Sanación energética</li>
      <li>Terapias cuánticas</li>
      <li>Medicina vibracional</li>''',
  '''      <li>Terapias de las tradiciones</li>
      <li>Música</li>
      <li>Silencio</li>'''),
 ('<p>Todos trabajando sinérgicamente, no jerárquicamente.</p>',
  '<p>Todos trabajando sinérgicamente, no jerárquicamente, y en el centro, el paciente y su familia.</p>'),
]
CANCER = open('/home/claude/origen10/x7_cancer.txt',encoding='utf-8').read()
CASOS = open('/home/claude/origen10/x7_casos.txt',encoding='utf-8').read()
R07 += [
 (CANCER, '''    <p><strong>Ejemplo: Acompañamiento Integral del Cáncer</strong></p>
    <p>El tratamiento oncológico que indique el equipo —cirugía, quimioterapia, radioterapia, inmunoterapia— va primero y no se negocia. Lo que se suma lo rodea y lo sostiene.</p>

    <p><strong>Evaluación</strong></p>
    <ul>
      <li>Diagnóstico oncológico completo</li>
      <li>Necesidades emocionales, familiares y espirituales</li>
      <li>Red de apoyo</li>
      <li>Historia familiar</li>
      <li>Plan personalizado</li>
    </ul>

    <p><strong>Durante el Tratamiento</strong></p>
    <ul>
      <li>Acupuntura para las náuseas y el dolor, cuando el equipo lo aprueba</li>
      <li>Nutrición junto al equipo, sin dietas que debiliten</li>
      <li>Psicoterapia</li>
      <li>Qi gong, yoga suave o meditación para la fatiga y la ansiedad</li>
      <li>Música y arte</li>
      <li>Grupo de apoyo</li>
      <li>Ceremonia u oración, si la persona lo desea</li>
    </ul>
    <p>Antes de sumar hierbas o suplementos, se consulta: algunos interfieren con la quimioterapia.</p>

    <p><strong>Consolidación</strong></p>
    <ul>
      <li>Fortalecimiento inmune: la inmunoterapia, cuando está indicada —enseñar al propio sistema inmune a reconocer el tumor, lo que valió el Nobel de 2018 a James Allison y Tasuku Honjo—, y el cuidado de las defensas con sueño, movimiento y buena alimentación</li>
      <li>Rehabilitación</li>
      <li>Trabajo de propósito</li>
      <li>Prevención de recurrencia</li>
    </ul>

    <p><strong>Mantenimiento:</strong></p>
    <ul>
      <li>Seguimiento oncológico</li>
      <li>Comunidad de apoyo</li>
      <li>Evolución continua</li>
    </ul>

    <div class="section-divider"></div>

'''),
 # V
 ('''      <li>Humildad y servicio</li>
    </ul>''', '''      <li>Humildad y servicio</li>
      <li>Saber derivar a tiempo</li>
    </ul>'''),
 ('''    <p><strong>EL SANADOR NO SANA</strong></p>''',
  '''    <p><strong>EL SANADOR NO SANA</strong></p>
    <p>Ambroise Paré, el cirujano francés del siglo XVI, lo dijo de un herido al que había atendido: «Yo lo vendé, Dios lo curó».</p>'''),
 ('''      <li>Medicina vibracional</li>
      <li>Trabajo con cristales</li>
      <li>Geometría sagrada</li>''', '''      <li>Medicina vibracional</li>
      <li>Geometría sagrada</li>'''),
 ('<li>Medicina shamánica</li>', '<li>Medicina chamánica</li>'),
 ('<li>Prácticas supervisadas</li>', '<li>Prácticas supervisadas en equipos de salud</li>'),
 # VI
 ('<li>Prevención antes que tratamiento</li>', '<li>Prevención, además de tratamiento</li>'),
 # VII
 ('''    <h3>El Programa de 21 Días</h3>

    <p><strong>Días 1-7: Limpieza</strong></p>
    <ul>
      <li>Desintoxicación física</li>
      <li>Limpieza emocional</li>''',
  '''    <h3>El Programa de 21 Días</h3>
    <p>Veintiún días son un comienzo, no una meta: un hábito tarda lo que tarda.</p>

    <p><strong>Días 1-7: Orden</strong></p>
    <ul>
      <li>Limpieza emocional</li>'''),
 ('''    <p><strong>LA RUTINA HOLOGRÁFICA:</strong></p>''',
  '''    <p><strong>LA RUTINA HOLOGRÁFICA:</strong></p>
    <p>Adapta los horarios a tu vida: lo que importa es el orden, no la hora.</p>'''),
 ('<li>Ducha fría/caliente</li>', '<li>Ducha tibia que termina fresca, si te sienta bien</li>'),
 ('<li>Suplementos personalizados</li>', '<li>Suplementos, solo si te los indica tu médico</li>'),
 # VIII
 ('''    <h3>El Arte del Buen Morir</h3>''',
  '''    <h3>El Arte del Buen Morir</h3>
    <p>La Edad Media escribió manuales para morir bien, el <em>Ars moriendi</em>; los cuidados paliativos los continúan.</p>'''),
 ('<li>Perdón total</li>', '<li>El perdón posible</li>'),
 ('''    <h3>Muerte como Sanación Última</h3>
    <p>La muerte no es fracaso médico sino:</p>
    <ul>
      <li>Culminación natural</li>
      <li>Transición dimensional</li>
      <li>Liberación del alma</li>
      <li>Sanación definitiva</li>
      <li>Retorno a la Fuente</li>
      <li>Graduación cósmica</li>
      <li>Regalo final</li>
      <li>Puerta a lo eterno</li>
    </ul>''',
  '''    <h3>Muerte como Sanación Última</h3>
    <p>La muerte no es fracaso médico sino:</p>
    <ul>
      <li>Culminación natural</li>
      <li>Transición dimensional</li>
      <li>Liberación del alma</li>
      <li>Sanación definitiva</li>
      <li>Retorno a la Fuente</li>
      <li>Graduación cósmica</li>
      <li>Regalo final</li>
      <li>Puerta a lo eterno</li>
    </ul>
    <p>Mirarla no es desearla: es aprender a no vivir de espaldas a ella. Y si alguna vez contemplar la muerte se vuelve deseo de no estar, es momento de pedir ayuda, sin esperar.</p>'''),
 # IX
 ('''    <h3>Principios Fundamentales Expandidos</h3>''',
  '''    <h3>Principios Fundamentales Expandidos</h3>
    <p>Tom Beauchamp y James Childress ordenaron estos cuatro principios en 1979.</p>'''),
 ('''    <h4>Primum non nocere (Primero no dañar)</h4>''',
  '''    <h4>Primum non nocere (Primero no dañar)</h4>
    <p>Su raíz es hipocrática: en las <em>Epidemias</em> se pide ayudar o, al menos, no dañar.</p>'''),
 ('Mantendré la humildad ante el misterio, la compasión ante el sufrimiento, y la esperanza ante la enfermedad.',
  'Mantendré la humildad ante el misterio, la compasión ante el sufrimiento, y la esperanza ante la enfermedad. Nunca prometeré una curación que no puedo dar.'),
 # X
 (CASOS, '''    <h2>X. Dos Historias</h2>
    <h3>David Tasma y Cicely Saunders</h3>
    <p>En 1948, en Londres, un refugiado polaco que se moría de cáncer le dijo a una joven trabajadora social que solo quería lo que había en su mente y en su corazón. Hablaron de un lugar donde morir sin dolor y sin soledad. Él le dejó quinientas libras: «Seré una ventana en tu casa». Ella estudió medicina, y diecinueve años después abrió St Christopher's, el primer hospicio moderno. La ventana está ahí.</p>

    <h3>Maggie Keswick Jencks</h3>
    <p>Paisajista escocesa, recibió en 1993 la noticia de que su cáncer había vuelto, y esperó resultados en pasillos sin ventanas. Antes de morir, en 1995, escribió que lo que más importa es no perder la alegría de vivir por el miedo a morir, y dejó dibujado un lugar distinto. En 1996 abrió en Edimburgo el primer centro Maggie: luz, jardín y una cocina en el centro. Hoy los diseñan grandes arquitectos, como Frank Gehry y Zaha Hadid.</p>

    <div class="section-divider"></div>

'''),
 # XI
 ('<li>Sliding scale universal</li>', '<li>Tarifas según posibilidades</li>'),
 ('<li>Crowdfunding sanador</li>', '<li>Colectas sanadoras</li>'),
 ('''      <li>Economía circular</li>
      <li>Criptomonedas de salud</li>''', '''      <li>Economía circular</li>'''),
 # XII
 ('''    <h3>Metodologías Expandidas</h3>
    <p><strong>Más Allá del Doble Ciego:</strong></p>''',
  '''    <h3>Metodologías Expandidas</h3>
    <p>El ensayo con grupo de control, que James Lind probó en 1747 con marineros enfermos de escorbuto y unas naranjas, sigue siendo la mejor manera de saber qué cura.</p>
    <p><strong>Además del Doble Ciego:</strong></p>'''),
 # XIII
 ('''      <li>Fragmentación de saberes</li>
    </ul>''', '''      <li>Fragmentación de saberes</li>
      <li>Las promesas sin pruebas, que alejan a los enfermos de lo que podría ayudarlos</li>
    </ul>'''),
 # XIV
 ('<li>Epidemias erradicadas</li>', '<li>Epidemias erradicadas: la viruela lo fue en 1980, la peste bovina en 2011, y la poliomielitis está cerca</li>'),
 ('''      <li>Envejecimiento reversible</li>
      <li>Regeneración de órganos</li>''',
  '''      <li>Envejecimiento reversible, como en los ratones de Izpisúa Belmonte</li>
      <li>Regeneración de órganos, como la que anuncian las bioimpresoras y los trasplantes entre especies</li>'''),
 ('''      <li>Humanidad sin enfermedad crónica</li>
      <li>Longevidad de 150+ años saludables</li>
      <li>Telepatía médica</li>
      <li>Sanación interdimensional</li>
      <li>Medicina galáctica</li>''',
  '''      <li>Humanidad sin enfermedad crónica: parte de la diabetes tipo 2 ya entra en remisión con cambios intensivos de alimentación y con los nuevos fármacos metabólicos</li>
      <li>Longevidad de 150+ años saludables: en 2000, el biólogo Steven Austad le apostó a Jay Olshansky que alguien ya nacido llegaría a esa edad, y la apuesta sigue abierta</li>
      <li>Telepatía médica: en 2014 ya se ensayó la comunicación directa entre dos cerebros humanos</li>
      <li>Sanación interdimensional</li>
      <li>Medicina galáctica: la que ya se aprende en las estaciones espaciales</li>'''),
 ('''    <pre>HOMO SAPIENS → HOMO LUMINOUS</pre>
    <p>Características:</p>''',
  '''    <pre>HOMO SAPIENS → HOMO LUMINOUS</pre>
    <p>Así llamó Alberto Villoldo al ser humano por venir. Características:</p>'''),
 # XV
 ('No esperen permiso, no esperen perfección.',
  'No esperen la perfección; sí la formación, la supervisión y la humildad de derivar a tiempo.'),
 ('''"Ustedes que buscan salud, que anhelan wholeness, que sufren en cuerpo o alma: son más poderosos de lo que imaginan. La sanación no viene de afuera; ustedes SON la sanación esperando despertar. Tomen su poder, reclamen su salud, sean el milagro."''',
  '''"Ustedes que buscan salud, que anhelan plenitud, que sufren en cuerpo o alma: son más poderosos de lo que imaginan. La sanación viene de adentro y de afuera: de su propia fuerza y de quienes los cuidan. Pidan ayuda, háganse preguntas, elijan con información. Ustedes son parte del milagro."'''),
 # XVI
 ('No importa la técnica, la tecnología o la tradición; si no hay amor, no hay sanación verdadera.</p>',
  'No importa la técnica, la tecnología o la tradición; si no hay amor, no hay sanación verdadera. Francis Peabody se lo dijo a los estudiantes de medicina de Harvard, en una conferencia publicada en 1927: el secreto del cuidado del paciente está en cuidar al paciente.</p>'),
 ('Una medicina que ve en cada síntoma una invitación a la evolución. Que reconoce en cada enfermedad una oportunidad de despertar. Que celebra en cada sanación la resiliencia infinita de la vida.',
  'Una medicina que escucha cada síntoma y cuida a la persona entera. Que acompaña a quien enferma sin culparlo, y celebra en cada sanación la resiliencia de la vida.'),
 # Cierre y epílogo
 ('(Paz en cuerpo, mente y espíritu)', '(Paz en uno mismo, con los demás y con el mundo)'),
 ('Cada amanecer es una sesión de sanaterapia.', 'Cada amanecer es una sesión de sanación.'),
]
R07 += [
 ('''    La enfermedad es el olvido de esta verdad.<br>
    La sanación es el recuerdo.<br><br>''',
  '''    La enfermedad no borra esta verdad.<br>
    La sanación la recuerda.<br><br>'''),
 ('''    Amén. Aho. Así es."</blockquote>
''',
  '''    Amén. Aho. Así es."</blockquote>

    <aside class="puerta arquitectura" aria-label="Puerta hacia Arquitectura del Destino">
      <p class="p-nombre">Puerta</p>
      <p class="p-texto">La postura de no saber de Harlene Anderson y Harold Goolishian, y una familia que aprende a acompañar un diagnóstico sin respuestas, se despliegan en <em>No Saber</em>, Libro 7 de <em>Arquitectura del Destino</em>, Umbral VI: «La postura de no saber».</p>
      <a class="cruzar" href="https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/libro-07-no-saber/L07-U6.html">Cruzar ⟶</a>
    </aside>
'''),
]

R['nodo_07.html'] = R07
R['index.html'] = [
 ('  <title>Sanación Integral | Libro X | Trinity Origen</title>\n',
  '  <title>Sanación Integral | Libro X | Trinity Origen</title>\n' + NOTA),
 ('participan de un mismo proceso de curación consciente.</p>', 'participan de un mismo cuidado.</p>'),
 ('de los campos cuánticos a la mente creadora,', 'de los campos cuánticos a la mente que acompaña,'),
 ('<p class="node-subtitle">Medicina de la Interconexión y Campos Morfogenéticos</p>', '<p class="node-subtitle">Medicina de la Interconexión</p>'),
 ('La salud deja de ser un fenómeno individual para mostrarse como una red viva: linajes, vínculos, resonancias colectivas y campos compartidos que propagan enfermedad o coherencia.',
  'La salud deja de ser un fenómeno individual para mostrarse como una red viva de linajes, vínculos, cercanía y comunidad que la sostiene.'),
 ('<p class="node-subtitle">Medicina Vibracional y Frecuencial - La Danza de las Ondas</p>', '<p class="node-subtitle">La Danza de las Ondas</p>'),
 ('Una cartografía vibracional del ser: frecuencias, geometrías, sonido, cristales y coherencia cuántica como puertas hacia una medicina basada en resonancia y armonización.',
  'Una cartografía vibracional del ser: el corazón, la respiración, el sonido, la forma que dibuja la arena de Chladni y el silencio donde toda música empieza.'),
 ('<p class="node-subtitle">Neuroplasticidad y Consciencia Curativa - El Arquitecto Interior</p>', '<p class="node-subtitle">Neuroplasticidad y Consciencia - El Arquitecto Interior</p>'),
 ('El pensamiento, la emoción y la atención como fuerzas que esculpen biología, reconfiguran circuitos',
  'El pensamiento, la emoción y la atención como fuerzas que acompañan al cuerpo, reconfiguran circuitos'),
 ('<p class="node-subtitle">Prana, Chi y la Medicina Energética - El Río de Vida</p>', '<p class="node-subtitle">Prana, Chi y el Aliento - El Río de Vida</p>'),
 ('que revelan al ser humano como flujo, no como estructura fija.',
  'que revelan al ser humano como flujo, no como estructura fija, y descubren que la fuerza vital fue, antes que nada, aliento.'),
 ('la reparación transgeneracional como acto de liberación hacia atrás y hacia adelante.',
  'la reparación transgeneracional como cuidado que empieza hoy y alcanza a los que vienen.'),
 ('recordar que toda curación auténtica ocurre cuando diferentes niveles del ser vuelven a entrar en coherencia.',
  'recordar que toda medicina verdadera es amor aplicado con conocimiento, y que cada nivel del ser merece ser cuidado.'),
 ('Del síntoma al sentido. Del órgano al campo. Del individuo al linaje.',
  'Del síntoma al cuidado. Del órgano a la persona. Del individuo al linaje.'),
]


def aplicar(nombre, reemplazos):
    with open(os.path.join(SRC, nombre), encoding='utf-8') as f:
        t = f.read()
    for i, (viejo, nuevo) in enumerate(reemplazos, 1):
        if viejo == '__MAIN__':
            a, b = '  <main class="content">\n', '\n  </main>'
            if t.count(a) != 1 or t.count(b) != 1:
                sys.exit(f'{nombre}: no se encuentra un único <main>')
            i0 = t.index(a) + len(a)
            i1 = t.index(b)
            t = t[:i0] + nuevo.strip('\n') + t[i1:]
            continue
        n = t.count(viejo)
        if n != 1:
            sys.exit(f'{nombre}: el reemplazo {i} aparece {n} veces:\n{viejo[:160]}')
        t = t.replace(viejo, nuevo)
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, nombre), 'w', encoding='utf-8') as f:
        f.write(t)
    return len(reemplazos)


if __name__ == '__main__':
    total = 0
    for nombre, reemplazos in R.items():
        n = aplicar(nombre, reemplazos)
        total += n
        print(f'{nombre}: {n} reemplazos')
    print(f'Total: {total}')
