# Depuración de Origen XIII, El Retorno a Casa (noviembre de 2026), con el veto del Lic. Arturo Rodríguez.
# Lente: la visión queda; se corrigen errores, se suma el cuidado mínimo y se abren puertas fractales a la Red.
# Aplica cada reemplazo exactamente una vez sobre el original de la etiqueta origen-original.
import os, sys

SRC = os.environ.get('ORIGEN13_SRC', '/home/claude/origen13/src/')
OUT = os.environ.get('ORIGEN13_OUT', '/home/claude/origen13/out/01_Trinity_Origen/')

NOTA = ('<!-- Depurado en noviembre de 2026 según la guía de depuración de Quantum, que vale para Origen '
        '(Arquitectura del Destino, maestro v4, sección 5, con las precisiones 5 y 6 de Origen), con el veto del Lic. Arturo Rodríguez: '
        'la visión del libro queda; se corrigen errores de índice y de lengua, se suma el cuidado mínimo '
        'y se abren puertas fractales hacia la Red. El original está en la etiqueta origen-original del repositorio Trinity-. -->\n')

AQ = 'https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/'

def puerta(clase, aria, texto, href):
    return ('\n    <aside class="puerta %s" aria-label="%s">\n'
            '      <p class="p-nombre">Puerta</p>\n'
            '      <p class="p-texto">%s</p>\n'
            '      <a class="cruzar" href="%s">Cruzar ⟶</a>\n'
            '    </aside>\n') % (clase, aria, texto, href)

def arq(texto, href):
    return puerta('arquitectura', 'Puerta hacia Arquitectura del Destino', texto, AQ + href)

R = {}
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
def base(n, titulo):
    return [
     ('<title>%s</title>\n' % titulo, '<title>%s</title>\n' % titulo + NOTA),
     ('</style>\n</head>', CSS.lstrip('\n')),
    ]

def antes_de_transicion(k, bloque):
    old = '</blockquote>\n\n    <div class="section-divider"></div>\n\n    <h2>Portal de Transición al Nodo %d</h2>' % k
    return (old, '</blockquote>\n' + bloque + '\n    <div class="section-divider"></div>\n\n    <h2>Portal de Transición al Nodo %d</h2>' % k)

Q = '../../02_Trinity_Quantum/'

R['nodo_01.html'] = base(1, 'Nodo 1 – La Gran Amnesia | El Retorno a Casa | Trinity Origen') + [
 ('crea una onda de éxtasis que ripple a través de toda la creación.', 'crea una onda de éxtasis que se propaga por toda la creación.'),
 ('<strong>“La Nostalgia del Origen: El Llamado que Ningún Alma Puede Silenciar”</strong>',
  '<strong>“Los Fragmentos del Alma: La Reunificación de Nuestras Partes Dispersas”</strong>'),
 antes_de_transicion(2, arq('Los actores que olvidan que actúan, y el príncipe del <em>Himno de la Perla</em> que olvidó su misión hasta que una carta lo despertó, se despliegan en <em>El Sonámbulo</em>, Libro 2 de <em>Arquitectura del Destino</em>, Umbral II: «Actores que olvidan que actúan».', 'libro-02-el-sonambulo/L02-U2.html')),
]

R['nodo_02.html'] = base(2, 'Nodo 2 – Los Fragmentos del Alma | El Retorno a Casa | Trinity Origen') + [
 ('Retornen ahora, en el timing perfecto, para la reunificación sagrada.', 'Retornen ahora, en el momento perfecto, para la reunificación sagrada.'),
 ('<li>Permitir el timing natural de cada parte</li>', '<li>Permitir el ritmo natural de cada parte</li>'),
 ('<strong>“La Nostalgia del Hogar: El Imán Secreto del Retorno”</strong>',
  '<strong>“El Recuerdo del Origen: La Memoria Primordial Que Despierta en el Corazón”</strong>'),
 antes_de_transicion(3, arq('Lo que el trauma aparta y cómo vuelve a reunirse, desde la muchacha que Pierre Janet atendió en París a comienzos del siglo XX, se despliega en <em>La Grieta</em>, Libro 5 de <em>Arquitectura del Destino</em>, Umbral II: «La muchacha que no podía contarlo».', 'libro-05-la-grieta/L05-U2.html')),
]

R['nodo_03.html'] = base(3, 'Nodo 3 – El Recuerdo del Origen | El Retorno a Casa | Trinity Origen') + [
 ('Por eso su risa es medicina. Aún recuerdan.</p>',
  'Por eso su risa es medicina. Aún recuerdan. William Wordsworth lo escribió en 1807: venimos arrastrando nubes de gloria desde Dios, que es nuestro hogar. Y la psicología llama amnesia infantil a que casi nadie conserve recuerdos de antes de los tres o cuatro años.</p>'),
 ('allí donde la memoria primordial comienza a reorganizar la existencia entera: <strong>“El Camino de Regreso: La Vida Humana Como Sendero de Reintegración”</strong>',
  'allí donde la memoria primordial descubre que vive entera en cada fragmento: <strong>“La Naturaleza Holográfica: Cada Parte Contiene el Todo”</strong>'),
 antes_de_transicion(4, arq('Cómo el recuerdo deja de ser destello y se vuelve casa, ladrillo por ladrillo, con los días, se despliega en <em>Habitar</em>, Libro 13 de <em>Arquitectura del Destino</em>, Umbral III: «El mismo mecanismo».', 'libro-13-habitar/L13-U3.html')),
]

R['nodo_04.html'] = base(4, 'Nodo 4 – La Naturaleza Holográfica | El Retorno a Casa | Trinity Origen') + [
 ('<p>Jung descubrió que todos compartimos un inconsciente común.', '<p>Carl Jung llamó inconsciente colectivo al fondo común que todos compartimos.'),
 ('Siente cómo cada pensamiento ripple a través del todo.<br>', 'Siente cómo cada pensamiento se propaga por el todo.<br>'),
 ('<strong>“El Camino de Regreso: Vivir Desde la Totalidad Recuperada”</strong>',
  '<strong>“El Círculo Completo: El Fin Que Es un Nuevo Comienzo”</strong>'),
 antes_de_transicion(5, arq('La celda de Moisés, el portal del ahora y la casa que está en todas partes se despliegan en <em>Habitar</em>, Libro 13 de <em>Arquitectura del Destino</em>, Umbral IV: «Cada parte contiene el todo».', 'libro-13-habitar/L13-U4.html')),
]

ESPIRAL = '''    <h2>VII. El Círculo de Trinity</h2>
    <p>Los 13 libros de Trinity Origen forman su propio círculo perfecto:</p>

    <ol>
      <li><strong>Psicología Cuántica</strong> - El centro: el observador y su campo</li>
      <li><strong>La Voz Interior</strong> - Escuchar desde adentro</li>
      <li><strong>El Dolor como Portal</strong> - La transformación comienza</li>
      <li><strong>Inteligencias Sin Nombre</strong> - El encuentro con otras mentes</li>
      <li><strong>Los Vínculos Sagrados</strong> - Del uno al otro</li>
      <li><strong>El Vacío Fértil</strong> - El silencio que crea</li>
      <li><strong>La Muerte como Maestra</strong> - El punto medio: la vida vista desde el final</li>
      <li><strong>Educación Cuántica</strong> - Comenzar a transmitir</li>
      <li><strong>Liderazgo Consciente</strong> - Servir desde el ser</li>
      <li><strong>Sanación Integral</strong> - El cuidado de todos los niveles</li>
      <li><strong>La Consciencia Planetaria</strong> - La Tierra como cuerpo</li>
      <li><strong>La Civilización Galáctica</strong> - La visión expandida</li>
      <li><strong>El Retorno a Casa</strong> - El círculo se completa</li>
    </ol>

    <p>Pero nota: el libro 13 no es un final. Es el punto donde el círculo se completa y una nueva espiral comienza, y esa espiral ya tiene nombres. Gira alrededor del mismo centro:</p>
    <ul>
      <li><strong>El Observador Silencioso</strong>, el centro inmóvil, que reaparece en <a href="AQlibro-03-el-testigo/L03.html"><em>El Testigo</em></a></li>
      <li><strong>La Danza de las Polaridades</strong>, la primera diferenciación, en <a href="QLibro_09/index.html"><em>Simetrías Rotas</em></a></li>
      <li><strong>Los Portales de Percepción</strong> y <strong>El Puente Arcoíris</strong>, en <a href="QLibro_05/index.html"><em>El Portal Infinito</em></a></li>
      <li><strong>La Alquimia Interior</strong>, que ya ardía en <a href="../Libro_03/index.html"><em>El Dolor como Portal</em></a></li>
      <li><strong>Navegantes del Infinito</strong>, en <a href="../../infinito.html">Trinity Infinito</a></li>
      <li><strong>El Jardín de los Espejos</strong>, en <a href="QLibro_07/index.html"><em>Realidades Holofractales</em></a></li>
      <li><strong>Los Hilos del Tejedor</strong>, en <a href="QLibro_13/index.html"><em>El Multiverso Interior</em></a></li>
      <li><strong>La Sinfonía del Silencio</strong>, en <a href="QLibro_06/index.html"><em>El Vacío Creativo</em></a></li>
      <li><strong>El Despertar del Soñador</strong>, en <a href="AQlibro-02-el-sonambulo/L02.html"><em>El Sonámbulo</em></a></li>
      <li><strong>Los Códigos de la Creación</strong>, en <a href="QLibro_11/index.html"><em>Transducción Dimensional</em></a></li>
    </ul>

    <p>Trinity es un mandala viviente: se expande en círculos sin perder su centro, y el lector puede recorrerlo infinitas veces, cada vez descubriendo nuevas profundidades. En cada vuelta se asoman campos que todavía no tienen nombre.</p>'''.replace('AQ', AQ).replace('href="Q', 'href="' + Q)

src5 = open(SRC + 'nodo_05.html', encoding='utf-8').read()
a = src5.index('    <h2>VII. El Círculo de Trinity</h2>')
b = src5.index('cada vez descubriendo nuevas profundidades.</p>', a) + len('cada vez descubriendo nuevas profundidades.</p>')
VII_ORIG = src5[a:b]

R['nodo_05.html'] = base(5, 'Nodo 5 – El Círculo Completo | El Retorno a Casa | Trinity Origen') + [
 (VII_ORIG, ESPIRAL),
 ('sino habitar plenamente el hogar reencontrado?</strong>', 'sino habitar plenamente el hogar reencontrado, que es también este cuerpo y esta vida?</strong>'),
 ('<strong>“Habitar el Hogar: La Consciencia Que Descansa en Sí Misma”</strong>',
  '<strong>“El Regalo de la Encarnación: La Bendición Disfrazada de Limitación”</strong>'),
 antes_de_transicion(6, arq('Habitar el hogar reencontrado —quedarse adentro, despierto, en el lugar y en la hora donde ya estás— se despliega en <em>Habitar</em>, Libro 13 de <em>Arquitectura del Destino</em>, Umbral I: «Rondar y habitar».', 'libro-13-habitar/L13-U1.html')),
]

R['nodo_06.html'] = base(6, 'Nodo 6 – El Regalo de la Encarnación | El Retorno a Casa | Trinity Origen') + [
 ('<li>Permite el amor como elección, no como default</li>', '<li>Permite el amor como elección, no como inercia</li>'),
 ('<strong>“El Hogar Recuperado: La Paz de Ser Todo lo Que Somos”</strong>',
  '<strong>“La Nueva Humanidad: El Amanecer de Homo Luminous”</strong>'),
 antes_de_transicion(7, arq('Morder una fresa madura, el calor del sol en la piel, el abrazo de un ser amado: lo que los ángeles no conocen se despliega en <em>El Cuerpo</em>, Libro 4 de <em>Arquitectura del Destino</em>, Umbral VI: «Lo que los ángeles no conocen».', 'libro-04-el-cuerpo/L04-U6.html')),
]

CUIDADO_LUZ = '\n    <p>Mientras tanto, el cuerpo de hoy necesita comida: quienes intentaron vivir solo de luz enfermaron, y algunos murieron.</p>'
CUIDADO_NINOS = '\n    <p>La idea de los niños índigo nació con Nancy Ann Tappe y se difundió en 1999 con el libro de Lee Carroll y Jan Tober. Ver en un niño un don no quita mirar también lo que necesita: si le cuesta atender, aprender o vincularse, una consulta puede abrirle caminos.</p>'
CUIDADO_SIGNOS = '\n    <p>Algunos de estos signos también pueden ser señales de otras cosas. Si traen noches sin sueño, pensamientos que corren, una misión urgente, mensajes de guías o la certeza de saber lo que va a pasar, no es la activación: es el momento de pedir ayuda, esa misma semana. Stanislav y Christina Grof llamaron emergencia espiritual a las crisis que a veces acompañan un despertar, y enseñaron que se atraviesan acompañadas.</p>'

R['nodo_07.html'] = base(7, 'Nodo 7 – La Nueva Humanidad | El Retorno a Casa | Trinity Origen') + [
 ('''      <li>Bioluminiscencia sutil</li>
    </ul>''', '''      <li>Bioluminiscencia sutil</li>
    </ul>''' + CUIDADO_LUZ),
 ('<li>La vida misma como performance art</li>', '<li>La vida misma como arte vivo</li>'),
 ('<li>Amor incondicional como estado default</li>', '<li>Amor incondicional como estado natural</li>'),
 ('''      <li>Puentes dimensionales naturales</li>
    </ul>''', '''      <li>Puentes dimensionales naturales</li>
    </ul>''' + CUIDADO_NINOS),
 ('<li>Liderazgo rotativo basado en expertise</li>', '<li>Liderazgo rotativo basado en el saber</li>'),
 ('<p>La enfermedad es vista como desalineación:</p>', '<p>La enfermedad es vista como desalineación, nunca como culpa:</p>'),
 ('<li>Confiar en el timing perfecto de cada alma</li>', '<li>Confiar en el tiempo perfecto de cada alma</li>'),
 ('<li>Las emociones ripple a través de la red telepática</li>', '<li>Las emociones se propagan por la red telepática</li>'),
 ('''      <li>Sientes que “recordaste” más que “aprendiste” estas verdades</li>
    </ul>''', '''      <li>Sientes que “recordaste” más que “aprendiste” estas verdades</li>
    </ul>''' + CUIDADO_SIGNOS),
 ('Si has llegado hasta aquí, hasta el final de Trinity, no es accidente.', 'Si has llegado hasta aquí, hasta el final de Trinity Origen, no es accidente.'),
 ('<p>El viaje de Trinity se completa aquí.<br>', '<p>El viaje de Trinity Origen se completa aquí.<br>'),
 ('''    <div class="section-divider"></div>

    <blockquote><strong>FIN DE TRINITY</strong><br>''',
  arq('Que despertar y recordar sean casi el mismo gesto —la atención plena, que en pali viene de la raíz de la memoria— se despliega en <em>El Testigo</em>, Libro 3 de <em>Arquitectura del Destino</em>, Umbral VI: «Despertar y recordar».', 'libro-03-el-testigo/L03-U6.html')
  + puerta('trinity', 'Puerta hacia Trinity Quantum', 'La espiral sigue. Trinity Quantum retoma estos campos en trece libros, del Arquitecto Cuántico al Multiverso Interior.', Q + 'index.html')
  + '''
    <div class="section-divider"></div>

    <blockquote><strong>FIN DE TRINITY ORIGEN</strong><br>'''),
 ('La transmisión de Trinity está completa... Pero los códigos continuarán activándose en cada lector, en su tiempo perfecto, por toda la eternidad...]*</em>',
  'La transmisión de Trinity Origen está completa... Pero los códigos continuarán activándose en cada lector, en su tiempo perfecto, por toda la eternidad...]</em>'),
]

R['index.html'] = [
 ('<title>Libro 13 – El Retorno a Casa | Trinity Origen</title>\n', '<title>Libro 13 – El Retorno a Casa | Trinity Origen</title>\n' + NOTA),
]

R['origen_index.html'] = [
 ('y buscás comprenderte desde múltiples dimensiones.', 'y buscas comprenderte desde múltiples dimensiones.'),
]

DESTINO = {'origen_index.html': 'index.html'}

def aplicar(nombre, reemplazos):
    with open(os.path.join(SRC, nombre), encoding='utf-8') as f:
        t = f.read()
    for i, (viejo, nuevo) in enumerate(reemplazos, 1):
        n = t.count(viejo)
        if n != 1:
            sys.exit(f'{nombre}: el reemplazo {i} aparece {n} veces:\n{viejo[:160]}')
        t = t.replace(viejo, nuevo)
    if nombre in DESTINO:
        ruta = os.path.join(OUT, DESTINO[nombre])
    else:
        ruta = os.path.join(OUT, 'Libro_13', nombre)
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
