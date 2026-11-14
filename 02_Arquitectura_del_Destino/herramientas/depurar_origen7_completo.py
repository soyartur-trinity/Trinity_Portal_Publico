# Depuración completa de Origen VII, La Muerte como Maestra (14 de noviembre de 2026), con el veto del
# Lic. Arturo Rodríguez («Aprobado todo»). Lente: riesgo clínico y puertas hacia la Red, como en Origen VI,
# VIII, I y XI. Es el libro de Origen que Arquitectura más cita: Las Pequeñas Muertes nació casi entero de él,
# y todo lo que ese libro cita conserva su letra (los epígrafes, la despedida en voz alta, el catálogo, el río,
# el protocolo de seis pasos, el ritual del sueño, la Práctica 6.1, las ondas, la meditación del legado y el
# epitafio vivo). El riesgo no estaba en la visión sino en quién lo lee (gente en duelo, gente que acompaña a
# alguien que muere, gente que piensa en no estar), en más de treinta testimonios inventados y en frases que
# en un mal día empujan. Las «conexiones» con otros libros de Origen citaban pasajes que no existen: por
# decisión de Arturo («Nada de citas inventadas»), donde la idea vive en un libro real, la línea dice lo que
# ese libro dice y lo enlaza; las citas inventadas salen y la idea queda en la voz del nodo. Y el cierre
# saluda a la «generación puente», como dice el epígrafe del Nodo 7 (decisión de Arturo).
#
# Se aplica sobre lo publicado (el original de la etiqueta origen-original con la depuración breve de
# octubre, herramientas/depurar_origen7.py), con reemplazos que deben aparecer exactamente una vez (o tramos,
# de un texto a otro, inclusive); si un anclaje falla, el script se detiene sin escribir.
#
# Uso: ORIGEN7_SRC=RUTA/Trinity-/01_Trinity_Origen/Libro_07/ ORIGEN7_OUT=RUTA/salida/ python3 depurar_origen7_completo.py
import os, re, sys

SRC = os.environ.get('ORIGEN7_SRC', '/home/claude/repos/trinity/01_Trinity_Origen/Libro_07/')
OUT = os.environ.get('ORIGEN7_OUT', '/home/claude/work7/out/01_Trinity_Origen/Libro_07/')

NOTA = ('<!-- Depurado entero el 14 de noviembre de 2026 según la guía de depuración de Quantum, que vale para Origen '
        '(Arquitectura del Destino, maestro v4, sección 5, con las precisiones 5 y 6 de Origen), con el veto del Lic. Arturo Rodríguez: '
        'la visión del libro queda; los testimonios inventados dejan su lugar a casos reales; salen las citas atribuidas a otros libros '
        'que no las contienen, las cifras sin fuente y lo que se vendía como si funcionara; se suma el cuidado clínico en la voz de cada '
        'nodo y se abren puertas fractales hacia la Red. Lo que cita Las Pequeñas Muertes conserva su letra. El original está en la '
        'etiqueta origen-original del repositorio Trinity-. -->\n')

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
   Depuración completa · 14 de noviembre de 2026
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
  .bloque p, .bloque li{ font-size:18px; line-height:1.7; }
  .mapa-nav li{ font-size:16px; }
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
   Depuración completa · 14 de noviembre de 2026
   Letra más grande en el teléfono y la línea con la medida del libro.
   ============================================================ */
.content .medida{color:var(--text-soft);font-style:italic;margin-top:1rem;}
@media (max-width: 720px){
  .content p{ font-size:18px; line-height:1.7; }
  .hero-desc{ font-size:18px; line-height:1.7; }
  .nodo-desc{ font-size:16px; }
}
</style>
</head>'''

R = {}


def mapa_items(nombre, pares):
    """Renombra o quita renglones del mapa de navegación (nuevo=None quita)."""
    for viejo, nuevo in pares:
        R[nombre]['reemplazos'].append(
            ('      <li>%s</li>\n' % viejo, '' if nuevo is None else '      <li>%s</li>\n' % nuevo))


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
    t = una_vez(t, '<p>"No es m&iacute;o vino a trav&eacute;s de m&iacute;."</p>',
                '<p>"No es m&iacute;o, vino a trav&eacute;s de m&iacute;."</p>', 'la firma'); cuenta += 1
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


# Frases de cuidado con la letra ya fijada en la constelación
MIRARLA = ('Mirarla no es desearla: es aprender a no vivir de espaldas a ella. Y si alguna vez contemplar la muerte se vuelve deseo '
           'de no estar, es momento de pedir ayuda, sin esperar.')   # Origen X.7 y Quantum 9.5
MIEDO = ('Ese miedo no es una enfermedad: es una respuesta a algo real. Si quita el sueño o las ganas durante semanas, se consulta; '
         'y se alivia más haciendo con otros que leyendo a solas.')   # Origen XI.1
REFERENCIA = ('Si alguna vez parece que cada número y cada cartel te hablan a ti, en secreto, eso no es un don: conviene conversarlo '
              'con alguien de confianza o con un profesional esa misma semana.')   # Quantum 11.2
NINO = ('Ver en un niño un don no quita mirar también lo que necesita: si le cuesta atender, aprender o vincularse, una consulta '
        'puede abrirle caminos.')   # Origen VI.7 y XIII.7
PORTAL = 'ningún portal verdadero pide dinero, secreto ni obediencia'   # Origen VI.7
SUSTANCIAS = ('Dejar de golpe el alcohol, los tranquilizantes como las benzodiacepinas y algunas otras sustancias puede ser peligroso '
              'para el cuerpo: se hace con un médico. Y nadie sale solo de una adicción: la compañía de otros que pasaron por lo mismo '
              'es de lo que más ayuda.')   # Origen I.5
LOFTUS = ('La memoria es moldeable, y Elizabeth Loftus mostró que puede llenarse de recuerdos que se sienten verdaderos sin serlo; '
          'por eso ese trabajo se hace con alguien formado.')   # Origen X.6
OJOS = ('Si alguna vez sentiste que no eras real o que te ibas de tu cuerpo, hazla con los ojos abiertos y los pies en el suelo, '
        'o déjala para otro momento.')   # Origen VII.5
DIV = '    <div class="section-divider"></div>\n'


def titulo_nodo(nombre, viejo, nuevo):
    R[nombre]['reemplazos'].extend([
        ('&ndash; %s |' % viejo, '&ndash; %s |' % nuevo),
        ('<h1 class="node-title">%s</h1>' % viejo, '<h1 class="node-title">%s</h1>' % nuevo),
    ])


# ---------------------------------------------------------------- Índice
R['index.html'] = dict(reemplazos=[
  ('<p>En el silencio del fin se revela la continuidad del Campo. Donde el morir se vuelve retorno.</p>',
   '<p>En el silencio del fin se revela la continuidad del Campo. Donde el morir se vuelve retorno.</p>\n'
   '    <p class="medida">Este libro mira la muerte para aprender a vivir. Mirarla no es desearla: si la idea de no estar se vuelve deseo, '
   'se pide ayuda ese mismo día. Un duelo reciente pide compañía antes que práctica.</p>'),
  ('<h2 class="nodo-titulo">EL TABÚ PRIMORDIAL</h2>', '<h2 class="nodo-titulo">El Tabú Primordial</h2>'),
  ('<h2 class="nodo-titulo">TECNOLOGÍAS DE CONSCIENCIA PARA EL TRÁNSITO</h2>', '<h2 class="nodo-titulo">Tecnologías de Consciencia para el Tránsito</h2>'),
  ('<h2 class="nodo-titulo">LA MUERTE DEL EGO</h2>', '<h2 class="nodo-titulo">La Muerte del Ego</h2>'),
  ('<h2 class="nodo-titulo">EL LEGADO CUÁNTICO</h2>', '<h2 class="nodo-titulo">El Legado Cuántico</h2>'),
  ('<h2 class="nodo-titulo">LA GRAN REUNIÓN</h2>', '<h2 class="nodo-titulo">La Gran Reunión</h2>'),
])


# ---------------------------------------------------------------- Nodo 1
# La negación encuentra su linaje (Gorer, Ariès, Becker) y su medida (el manejo del terror); México, Varanasi y
# los Dagara, con su fuente; los testimonios inventados dejan su lugar a quienes abrieron la conversación; el
# espejo tibetano sin fuente pasa al osario del Satipaṭṭhāna y al memento mori; la contemplación lleva su
# fuente (AN 5.57, con la letra de Las Pequeñas Muertes) y la frase de cuidado.
R['nodo_01.html'] = dict(reemplazos=[
  ('<p>Vivimos en la primera civilización de la historia humana que ha convertido la muerte en el enemigo absoluto. No siempre fue así. Durante milenios, nuestros ancestros danzaron con la muerte, la honraron, la integraron como la compañera sagrada de la vida. ¿Qué pasó? ¿Cómo llegamos a este estado de negación patológica?</p>',
   '<p>Vivimos en una civilización que ha convertido la muerte en el enemigo absoluto. No siempre fue así. Durante milenios, nuestros ancestros danzaron con la muerte, la honraron, la integraron como la compañera sagrada de la vida. En 1955, el antropólogo Geoffrey Gorer observó que la muerte había ocupado el lugar que antes tenía el sexo: aquello de lo que no se habla. Y el historiador Philippe Ariès, que siguió mil años de actitudes ante la muerte en Occidente, llamó a la de nuestro tiempo la muerte prohibida: la que se aparta de la casa, se calla delante de los niños y se esconde en el hospital. ¿Qué pasó? ¿Cómo llegamos a este estado de negación?</p>'),
  ('<p><strong>Conexión con El Vacío Fértil:</strong> En ese libro, se describe cómo la cultura contemporánea rehúye el misterio, intentando llenarlo con objetos y promesas externas. Este rechazo al misterio es la misma raíz que aquí adopta la forma de la negación de la muerte. El velo que cubre a la muerte y el velo que cubre al vacío son, en realidad, el mismo tejido.</p>',
   '<p><strong>Conexión con <a href="../Libro_06/nodo_01.html">El Vacío Fértil</a>:</strong> En su primer nodo, Fritz Perls llama vacío fértil al lugar al que se llega cuando uno deja de llenar la confusión con explicaciones y se queda en ella. Llenar el misterio para no mirarlo es la misma raíz que aquí toma la forma de la negación de la muerte. El velo que cubre a la muerte y el velo que cubre al vacío son el mismo tejido.</p>'),
  ('<p>Compramos la ilusión de permanencia. Cada objeto, cada logro, cada "like" es un amuleto contra nuestra mortalidad. El capitalismo se alimenta de nuestro terror no procesado.</p>',
   '<p>Compramos la ilusión de permanencia. Cada objeto, cada logro, cada «me gusta» es un amuleto contra nuestra mortalidad. La psicología lo midió: en los experimentos de la teoría del manejo del terror, que nació de la obra de Ernest Becker (<em>La negación de la muerte</em>, 1973), basta recordarle a alguien que va a morir para que espere gastar más en lujos y se vuelva más ávido al repartir lo que es de todos (Kasser y Sheldon, 2000). El mercado se alimenta de nuestro terror no procesado.</p>'),
  ('<p>Lo que no enfrentamos internamente, lo proyectamos. Una civilización que no puede procesar la muerte pacíficamente, la crea violentamente. Las guerras son rituales de muerte mal dirigidos.</p>',
   '<p>Lo que no enfrentamos internamente, lo proyectamos. En otro de esos experimentos, quienes acababan de pensar en su propia muerte le sirvieron más salsa picante a alguien que pensaba distinto, sabiendo que no le gustaba (McGregor y otros, 1998). Una civilización que no puede procesar la muerte pacíficamente, la crea violentamente. Las guerras son rituales de muerte mal dirigidos.</p>'),
  (('    <p><strong>Conexión con La Voz Interior:</strong>', 'participar plenamente del ciclo.</p>\n'), ''),
  ('<p>No es coincidencia que una de las culturas más vibrantes del planeta sea también la que más alegremente celebra la muerte. Los mexicanos entienden: la muerte no es el opuesto de la vida, es su sabor más intenso. Las calaveras de azúcar no son morbosas - son dulces recordatorios de nuestra dulce mortalidad.</p>',
   '<p>No es coincidencia que una de las culturas más vibrantes del planeta sea también la que más alegremente celebra la muerte. Los mexicanos entienden: la muerte no es el opuesto de la vida, es su sabor más intenso. Las calaveras de azúcar no son morbosas: son dulces recordatorios de nuestra dulce mortalidad. Octavio Paz escribió en <em>El laberinto de la soledad</em> (1950) que el mexicano trata a la muerte con una familiaridad que asombra a otros pueblos: juega con ella, la festeja, la tiene cerca. En 2008, la UNESCO inscribió las fiestas indígenas dedicadas a los muertos en su lista del patrimonio cultural inmaterial de la humanidad.</p>'),
  ('    <blockquote>Mi abuela me enseñó a platicar con la muerte como con una comadre. Ahora, cuando siento miedo, le digo: \'Ay, flaca, todavía no, tengo mucho que hacer.\' Y ella se ríe." — María, curandera de Oaxaca</blockquote>\n', ''),
  ('<h3>Tíbet: El Bardo Thodol</h3>', '<h3>Tíbet: El Bardo Thödol</h3>'),
  ('No es morbo - es comprensión profunda de que el lugar y la consciencia de tu muerte determinan tu próximo nacimiento.</p>',
   'No es morbo: la tradición sostiene que quien muere en Kashi, el nombre antiguo de la ciudad, ya no vuelve a nacer, porque Shiva le susurra al oído el mantra que libera.</p>'),
  ('<p>En Burkina Faso, los Dagara ven cada muerte como una iniciación para toda la comunidad. Los rituales funerarios duran días, no para "superar" la pérdida, sino para integrarla completamente. Saben que los no-nacidos, los vivos y los muertos forman un solo tejido.</p>',
   '<p>En Burkina Faso y en Ghana, los Dagara ven cada muerte como una iniciación para toda la comunidad. Los rituales funerarios duran días, no para «superar» la pérdida, sino para integrarla completamente. Saben que los no nacidos, los vivos y los muertos forman un solo tejido. Malidoma Patrice Somé, que nació entre ellos, contó esos funerales en sus libros, desde 1994.</p>'),
  (('    <p><strong>Conexión con Los Vínculos Sagrados:</strong>', 'no se disuelven con la muerte física.</p>\n'), ''),
  ('      <li>Medicina que ve la muerte como fracaso, no como culminación</li>\n    </ul>',
   '      <li>Medicina que ve la muerte como fracaso, no como culminación</li>\n    </ul>\n'
   '    <p>En 1963, la periodista Jessica Mitford describió esa industria en <em>The American Way of Death</em>: el embalsamamiento de rutina, el ataúd caro que la pena no se anima a discutir.</p>'),
  ('<p><strong>Conexión con Liderazgo Consciente:</strong> En ese libro se advierte que cualquier sistema que niega los ciclos naturales termina por producir líderes y estructuras desconectadas de la verdad fundamental de la impermanencia. Este mismo patrón se repite aquí: un modelo económico que no sabe honrar finales tampoco sabe renovarse, quedando atrapado en una acumulación que, tarde o temprano, colapsa.</p>',
   '<p><strong>Conexión con <a href="../Libro_09/nodo_01.html">Liderazgo Consciente</a>:</strong> Ese libro empieza por una muerte: la del líder que necesita dominar, para que nazca el que sirve. Lo que vale para una persona vale para un sistema: un modelo económico que no sabe honrar finales tampoco sabe renovarse, y queda atrapado en una acumulación que, tarde o temprano, colapsa.</p>'),
  ('<p>No se trata de deprimirse. Se trata de despertar a la preciosa fragilidad de estar vivo.</p>',
   '<p>No se trata de deprimirse. Se trata de despertar a la preciosa fragilidad de estar vivo.</p>\n'
   '    <p>Es una práctica antigua. En un discurso que la tradición budista conserva entre los Discursos numerados (<em>Anguttara Nikaya</em> 5.57), el Buda propone cinco temas para repasar a menudo, y no solo a los monjes, sino a cualquiera: que va a envejecer, que va a enfermar, que va a morir, que todo lo querido cambiará y se irá, y que es dueño de sus actos.</p>\n'
   '    <p>' + MIRARLA + ' Y un duelo reciente pide compañía antes que práctica: si la pérdida es de estos días, la contemplación espera.</p>'),
  ('<p><strong>Conexión con El Dolor como Portal:</strong> Esta práctica es hermana directa de las que propone ese libro: mirar de frente aquello que tememos para descubrir que, al hacerlo, el miedo se transforma en un catalizador de vida plena.</p>',
   '<p><strong>Conexión con <a href="../Libro_03/index.html">El Dolor como Portal</a>:</strong> Esta práctica es hermana de lo que ese libro propone con el dolor: no evitarlo ni apurarlo, sino atravesarlo conscientemente. Mirar de frente lo que tememos puede volver el miedo un impulso de vida plena.</p>'),
  ('<p><strong>Conexión con Educación Cuántica:</strong> El "diario de pequeñas muertes" dialoga con ese libro, donde se enseña a los más jóvenes a registrar cambios y transiciones como aprendizajes, no como pérdidas.</p>',
   '<p><strong>Conexión con <a href="../Libro_08/nodo_04.html">Educación Cuántica</a>:</strong> En su cuarto nodo, la pregunta por la muerte vuelve en espiral: un chico la hace a los siete años y vuelve a hacérsela a los catorce, a los veintiuno, a los cuarenta. Este diario es una manera de seguir haciéndosela.</p>'),
  ('<p>Mensual, en luna menguante</p>', '<p>Una vez al mes</p>'),
  ('<p>Dejes de postponer lo importante "para cuando tenga tiempo"</p>', '<p>Dejes de posponer lo importante "para cuando tenga tiempo"</p>'),
  (('    <h2>Testimonios de Liberación</h2>', 'Quiero que mi generación aprenda a morir de verdad para poder vivir de verdad.</blockquote>\n'),
   '    <h2>Los que Abrieron la Conversación</h2>\n'
   '    <p>En 1965, la psiquiatra Elisabeth Kübler-Ross empezó a hacer en su hospital de Chicago algo que casi nadie hacía: sentarse con pacientes que se estaban muriendo, delante de estudiantes, y preguntarles qué vivían. De esas conversaciones nació <em>Sobre la muerte y los moribundos</em> (1969), y con él una pregunta que la medicina había dejado de hacer.</p>\n'
   '    <p>En 2004, el sociólogo suizo Bernard Crettaz abrió los primeros cafés de la muerte, y en 2011 Jon Underwood llevó la idea a su casa de Londres: desconocidos que se sientan a tomar algo y a hablar de la muerte, sin agenda ni consejo. Hoy se hacen en decenas de países.</p>\n'
   '    <p>No hace falta un infarto para despertar. Basta una conversación que no se esquiva.</p>\n'),
  ('<p>Hay una práctica tibetana donde meditas frente a un espejo hasta ver tu rostro convertirse en calavera. No es macabro - es ver a través de la ilusión temporal hacia la verdad eterna. La muerte es el espejo más honesto:</p>',
   '<p>Las tradiciones tienen sus espejos de la muerte. En el <em>Satipaṭṭhāna Sutta</em>, el monje contempla en el osario los cuerpos en sus distintos estados y se dice: este cuerpo también es así, también llegará a eso. Los romanos repetían <em>memento mori</em>, recuerda que vas a morir, y los pintores del siglo XVII ponían una calavera entre las flores y los libros. No es macabro: es ver a través de lo pasajero. La muerte es el espejo más honesto:</p>'),
  (('    <p><strong>Conexión con Psicología Cuántica:</strong> En ese libro se estudia', 'esa muerte interna de las ilusiones.</p>\n'), ''),
  ('<p>Los místicos nacidos en culturas death-positive a veces dan por sentada la muerte.', '<p>Los místicos nacidos en culturas que abrazan la muerte a veces la dan por sentada.'),
  (('    <p><strong>Conexión con La Consciencia Planetaria:</strong>', 'se convierte en misión.</p>\n'), ''),
  ('Déjalas percollar en tu ser:', 'Déjalas asentarse en ti:'),
 ],
 puertas=[arq('Que el tabú más grande es también la puerta más grande, y que se cruza despedida a despedida, en lo pequeño de cada día, '
              'se despliega en <em>Las Pequeñas Muertes</em>, Libro 6 de <em>Arquitectura del Destino</em>, Umbral I: «La puerta más grande».',
              'libro-06-las-pequenas-muertes/L06-U1.html')],
)
mapa_items('nodo_01.html', [('Testimonios de Liberación', 'Los que Abrieron la Conversación')])
titulo_nodo('nodo_01.html', 'EL TABÚ PRIMORDIAL', 'El Tabú Primordial')


# ---------------------------------------------------------------- Nodo 2
# El ritual del sueño queda (Las Pequeñas Muertes lo cita), sin la vela encendida junto a la cama; la respiración
# lleva una frase para cuando «muero» pesa; la menstruación, una para quien busca un embarazo; el mes lunar
# dura lo que dura; los casos inventados dejan su lugar a Bridges, C. S. Lewis y el «solo por hoy»; y las
# conexiones dicen lo que dicen los libros reales.
R['nodo_02.html'] = dict(reemplazos=[
  ('respiramos muerte y vida 20,000 veces al día', 'respiramos muerte y vida unas veinte mil veces al día'),
  ('<p><strong>Repite 21 veces.</strong> Con cada ciclo, profundiza en la experiencia de morir y renacer.</p>\n'
   '    <blockquote>Cuando aprendí a morir en cada exhalación, mi ansiedad desapareció. ¿Cómo temer a la muerte si la practico 20,000 veces al día?" - Laura, instructora de yoga</blockquote>',
   '<p><strong>Repite 21 veces.</strong> Con cada ciclo, profundiza en la experiencia de morir y renacer.</p>\n'
   '    <p>Si estos días la palabra «muero» pesa demasiado, di «suelto»: la práctica es la misma. Y si retener el aire te marea, respira sin retenerlo.</p>'),
  ('Porque si puedes mantener consciencia durante el sueño, podrás mantenerla durante la muerte.</p>',
   'Porque si puedes mantener consciencia durante el sueño, podrás mantenerla durante la muerte. Es una de las seis yogas de Naropa, y la enseñan maestros vivos, como Tenzin Wangyal Rinpoche, que le dedicó un libro en 1998.</p>'),
  ('<li>Enciende una vela junto a tu cama</li>', '<li>Baja la luz (si enciendes una vela, apágala antes de acostarte)</li>'),
  ('<li>Adopta la "postura del león dormido" (lado derecho, mano bajo la mejilla)</li>',
   '<li>Adopta la "postura del león dormido" (lado derecho, mano bajo la mejilla), la misma en que, según la tradición, se acostó el Buda en su última noche</li>'),
  ('    <blockquote>Mi abuela me enseñó que cada menstruación es una pequeña muerte. \'Dejas ir lo que pudo ser\', me decía. Ahora enseño a mi hija: su sangre es sagrada, es práctica de soltar." - María, partera tradicional</blockquote>',
   '    <p>Y para quien busca un embarazo, cada sangrado puede ser un duelo: también ese duelo se honra, y se acompaña. Un dolor menstrual que obliga a detener la vida merece consulta: a veces tiene nombre, y tratamiento.</p>'),
  ('<p>28 días de nacimiento, plenitud, declive, muerte, renacimiento.', '<p>Unos veintinueve días y medio de nacimiento, plenitud, declive, muerte, renacimiento.'),
  ('<li>Nota cómo fluctúas con ella</li>', '<li>Nota tus propias mareas, sin pedirle a la luna que las explique</li>'),
  ('<p>Estudios recientes muestran que el cerebro procesa pérdidas emocionales en las mismas áreas que el dolor físico. Literalmente duele soltar. Pero aquí está la magia: cada vez que practicamos soltar conscientemente, construimos nuevas vías neuronales. El cerebro aprende: soltar no es peligroso, es liberador.</p>',
   '<p>En 2003, Naomi Eisenberger y sus colegas vieron que quedar excluido de un juego encendía en el cerebro una zona que también se enciende con el dolor del cuerpo. Estudios posteriores mostraron que los dos dolores no dibujan el mismo patrón, pero la imagen quedó: soltar duele. Y lo que se practica se aprende: cada vez que sueltas con cuidado, algo en ti aprende que soltar no siempre es peligroso, y que a veces libera.</p>'),
  (('    <h3>Roberto, 52 años</h3>', 'La muerte diaria es mi medicina."</p>\n'),
   '    <h3>William Bridges</h3>\n'
   '    <h3>Toda Transición Empieza con un Final</h3>\n'
   '    <p>En 1974, William Bridges dejó su cátedra de literatura estadounidense en el Mills College, en California, para acompañar a personas en sus mudanzas interiores. En <em>Transitions</em> (1980) escribió lo que había aprendido: toda transición empieza con un final, no con un comienzo, y entre lo que termina y lo que empieza hay una zona neutral, un tiempo de vacío que no conviene apurar. Quien perdió un trabajo y se quedó sin su nombre conoce esa zona: es la misma que aquí se llama vacío.</p>\n'
   '    <h3>C. S. Lewis</h3>\n'
   '    <h3>Las Mil Pequeñas Muertes Después de una Pérdida</h3>\n'
   '    <p>Cuando murió su mujer, Joy Davidman, en 1960, C. S. Lewis llevó un cuaderno que publicó al año siguiente, <em>Una pena en observación</em>. Ahí descubre por qué el duelo se parece a la espera: tantos gestos de cada día tenían a la otra persona como destino, y ahora se disparan hacia nadie. Cada costumbre que se queda sin destinatario es una pequeña muerte más. Honrarlas de a una, sin apuro, es parte del duelo.</p>\n'
   '    <h3>Solo por Hoy</h3>\n'
   '    <h3>Adicción y Renacimiento Diario</h3>\n'
   '    <p>Los grupos de recuperación enseñan a no prometer para siempre: solo por hoy. Cada día sin consumir es una pequeña muerte del que necesitaba la sustancia y un nacimiento del que se está volviendo. ' + SUSTANCIAS + '</p>\n'),
  (('    <p>El Nodo de las Pequeñas Muertes resuena profundamente con otras obras de la Constelación:</p>\n', 'El Yoga de los Sueños transforma el descanso en entrenamiento para el tránsito final.</p>\n'),
   '    <p>El Nodo de las Pequeñas Muertes resuena con otras obras de la Constelación:</p>\n'
   '    <h3><a href="../Libro_02/nodo_02.html">La Voz Interior</a></h3>\n'
   '    <p>En su segundo nodo, el Observador Luminoso mira incluso la pérdida: se puede perder un trabajo, una relación, la salud, y el que mira sigue ahí. Y advierte que en el duelo agudo ese acceso parece cerrado, y que no se fuerza: se confía en que sigue ahí.</p>\n'
   '    <h3><a href="../Libro_03/index.html">El Dolor como Portal</a></h3>\n'
   '    <p>Las pequeñas muertes, al doler, nos recuerdan que estamos vivos y en constante transformación. Para ese libro, el dolor no es un enemigo: cuando se lo atraviesa conscientemente, se vuelve portal.</p>\n'
   '    <h3><a href="../Libro_05/nodo_04.html">Los Vínculos Sagrados</a></h3>\n'
   '    <p>En su cuarto nodo, soltar no es fracaso: reconocer que se cumplió un ciclo con alguien y permitir que los dos sigan su camino es un acto de amor mayor que aferrarse por miedo.</p>\n'
   '    <h3><a href="../Libro_13/nodo_06.html">El Retorno a Casa</a></h3>\n'
   '    <p>En su sexto nodo, la muerte es el regalo culminante de la encarnación: sin ella no habría urgencia ni preciosidad, y es la mortalidad la que vuelve invaluable cada momento.</p>\n'),
  ('<p>Despídete de cada persona como si fuera la última vez</p>', '<p>Despídete de cada persona con presencia, como quien sabe que ningún encuentro está garantizado</p>'),
  ('<li>¿Qué insights emergen?</li>', '<li>¿Qué descubrimientos emergen?</li>'),
 ],
 puertas=[arq('Que el maestro zen que suelta su taza de té tiene un hermano en un monasterio del bosque, en Tailandia —Ajahn Chah, que disfrutaba '
              'su vaso de agua porque para él ya estaba roto—, se despliega en <em>Las Pequeñas Muertes</em>, Libro 6 de <em>Arquitectura del Destino</em>, '
              'Umbral IV: «El vaso que ya está roto».',
              'libro-06-las-pequenas-muertes/L06-U4.html')],
)


# ---------------------------------------------------------------- Nodo 3
# El nodo más clínico, el que La Puerta llama El Terapeuta Consciente. El epígrafe deja de prescindir del médico;
# en los cuidados paliativos cesa lo que busca curar y el alivio sigue hasta el final; las presencias del final
# encuentran su estudio (Kerr, 2014) y su distinción del delirio; dos frases para la familia; quien acompaña
# también es un cuerpo; los testimonios inventados dejan su lugar a Saunders, Ostaseski y Byock.
R['nodo_03.html'] = dict(reemplazos=[
  ('<p>"En el momento de la muerte, no necesitamos doctores ni sacerdotes. Necesitamos un ser humano presente,',
   '<p>"En el momento de la muerte, además de quien alivia y de quien reza, necesitamos un ser humano presente,'),
  ('<p>Los que trabajan en hospicios lo saben: llega un momento donde todas las intervenciones médicas cesan. Los familiares han dicho lo que tenían que decir. Las cuentas están saldadas. Y en ese espacio liminal, lo único que queda - y lo único que realmente importa - es la calidad de presencia que podemos ofrecer.</p>',
   '<p>Los que trabajan en cuidados paliativos lo saben: llega un momento en que cesan los tratamientos que buscan curar. El alivio no cesa: el dolor, la falta de aire y la angustia se siguen cuidando hasta el final. Los familiares han dicho lo que tenían que decir. Las cuentas están saldadas. Y en ese espacio, junto al alivio, lo que más importa es la calidad de presencia que podemos ofrecer.</p>'),
  ('    <blockquote>Acompañé a mi madre en sus últimas 72 horas. No hablamos mucho. Pero respiramos juntas. Mi presencia le decía: \'No estás sola. Es seguro soltar.\' Murió en paz, con una sonrisa sutil." - Carmen, profesora de meditación</blockquote>',
   '    <p>Frank Ostaseski, que en 1987 cofundó en San Francisco el Zen Hospice Project, uno de los primeros hospicios budistas de Occidente, se sentó junto a más de mil personas que morían. De esa práctica salió <em>Las cinco invitaciones</em> (2017), y la primera es no esperar: lo que importa no se deja para el final.</p>'),
  ('<p>Muchos esperan hasta el final para perdonar y pedir perdón. Presenciarás el poder transformador de soltar resentimientos.</p>',
   '<p>Muchos esperan hasta el final para perdonar y pedir perdón. Presenciarás el poder transformador de soltar resentimientos. El médico de cuidados paliativos Ira Byock lo vio tantas veces que lo resumió en cuatro frases que conviene decir mientras se puede: perdóname, te perdono, gracias, te quiero (<em>The Four Things That Matter Most</em>, 2004).</p>'),
  ('<p>Algunos mueren con el mismo esfuerzo y éxtasis con que nacen los bebés. La muerte puede ser un alumbramiento hacia otro estado.</p>',
   '<p>Algunos mueren con un esfuerzo parecido al de un parto, y por eso hoy hay quienes acompañan como acompañan las parteras: las doulas del final de la vida, que están con la persona y su familia sin reemplazar al equipo de salud. La muerte puede ser un alumbramiento hacia otro estado.</p>'),
  ('<p>Rupert Sheldrake nos enseñó sobre campos morfogenéticos - campos de información que moldean la forma y el comportamiento. En ningún lugar son más palpables que alrededor del lecho de muerte.</p>',
   '<p>Rupert Sheldrake propuso en 1981 que existen campos morfogenéticos, campos de información que moldean la forma y el comportamiento; es una hipótesis que la ciencia no confirmó. Como imagen, en ningún lugar se siente más que alrededor del lecho de muerte.</p>'),
  ('<p>Muchos reportan presencias. Familiares fallecidos que "vienen a buscar". Seres de luz. No importa si "crees" - el campo está activo.</p>',
   '<p>Muchos reportan presencias: familiares fallecidos que «vienen a buscar», seres de luz. Christopher Kerr y su equipo, en el hospicio de Buffalo, entrevistaron a 66 pacientes día tras día: casi nueve de cada diez tuvieron al menos un sueño o una visión, la mayoría con seres queridos ya muertos, y esos eran los que más los consolaban (2014). El mismo estudio los distingue del delirio, que también es frecuente al final: si hay agitación, confusión o terror, se avisa al equipo, que sabe aliviarlo.</p>'),
  ('<li><strong>Mantén coherencia:</strong> Tu paz estabiliza todos los campos</li>', '<li><strong>Mantén la calma:</strong> Tu paz ayuda a sostener el espacio</li>'),
  ('    <blockquote>Cuando entré a la habitación de mi padre moribundo, sentí el caos - miedo familiar ancestral. Respiré, me centré, emané paz. Vi cómo todo el campo se calmaba. Mi paz le dio permiso para soltar." - Miguel, terapeuta energético</blockquote>\n', ''),
  ('<p>Nacemos sin elección, pero podemos elegir cómo morir. No siempre las circunstancias, pero sí la consciencia. La muerte consciente es el acto creativo final - la obra maestra de una vida.</p>',
   '<p>Nacemos sin elección, y la muerte tampoco se elige; lo que a veces se elige es cómo vivirla: no siempre las circunstancias, pero sí la consciencia. La muerte consciente es el acto creativo final, la obra maestra de una vida.</p>\n'
   '    <p>' + MIRARLA + '</p>'),
  ('<h3>El Timing</h3>\n    <p>Muchos esperan estar solos. Otros esperan que llegue alguien. La muerte tiene su propia inteligencia temporal.</p>',
   '<h3>El Momento</h3>\n    <p>Muchos esperan estar solos. Otros esperan que llegue alguien. La muerte tiene su propia inteligencia temporal. Si murió en el minuto en que saliste a buscar un café, no fallaste: muchos se van justo cuando quedan solos.</p>'),
  ('<p>Muchos experimentan una mejoría súbita antes del final.', '<p>Algunos experimentan una mejoría súbita antes del final.'),
  ('Perturba a las familias. Recuerda: la persona no está sufriendo. Es el cuerpo soltando.',
   'Perturba a las familias. Por lo que se sabe, no molesta a quien ya está inconsciente, y el equipo puede aliviarlo, a veces solo cambiando la postura. Es el cuerpo soltando.'),
  ('La prisa occidental por "procesar el cuerpo" es violencia espiritual.</p>', 'La prisa por «procesar el cuerpo» le roba a la familia ese tiempo.</p>'),
  ('      <li>Resiste la urgencia de "hacer algo"</li>\n    </ul>',
   '      <li>Resiste la urgencia de "hacer algo"</li>\n    </ul>\n'
   '    <p>Donde la muerte ocurre en casa y era esperada, ese tiempo suele ser posible; en un hospital, se pide, y muchos equipos lo dan.</p>'),
  (('    <h2>Testimonios de Acompañantes</h2>', 'Al final, me enseñó a morir." - Roberto</blockquote>\n'),
   '    <h2>Voces de Quienes Acompañan</h2>\n'
   '    <p><strong>Cicely Saunders</strong> fue enfermera, trabajadora social y médica, y en 1967 fundó en Londres St Christopher\'s, el primer hospicio moderno. Lo que aprendió junto a las camas lo dijo en una frase que sigue sosteniendo a los equipos de cuidados paliativos: importas porque eres tú, e importas hasta el último momento de tu vida.</p>\n'
   '    <p><strong>Frank Ostaseski</strong> aprendió en el Zen Hospice que acompañar no es tener respuestas sino no irse: dar la bienvenida a todo, no rechazar nada, y llevar al cuarto la persona entera que uno es.</p>\n'
   '    <p><strong>Ira Byock</strong> vio a familias distanciadas durante décadas encontrarse en los últimos días, a veces con una sola de sus cuatro frases. No prometía muertes sin dolor. Prometía que nadie tenía por qué morir solo.</p>\n'),
  ('<li>Meditación de vaciamiento: 30 minutos mínimo</li>', '<li>Unos minutos de quietud antes de entrar</li>'),
  ('<li>Ayuno ligero: Estómago liviano, mente clara</li>', '<li>Come algo liviano: quien acompaña también es un cuerpo</li>'),
  ('      <li>Descansa profundamente: El acompañamiento agota</li>\n    </ul>',
   '      <li>Descansa profundamente: El acompañamiento agota</li>\n    </ul>\n'
   '    <p>Quien acompaña mucho tiempo se cansa, y descansar es parte del servicio: pedir relevo también es cuidar. Ese cansancio tiene nombre, fatiga por compasión (Figley, 1995), y se previene compartiendo la carga.</p>'),
  ('es medicina revolucionaria.</strong></p>',
   'es medicina revolucionaria.</strong></p>\n'
   '    <p>Y si a pesar de todo hubo miedo o dolor, no fue falta de quien estuvo: hay muertes difíciles, y la presencia las acompañó igual.</p>'),
  ((DIV + '    <h2>Conexiones con la Constelación Trinity</h2>', 'generando una sensación de continuidad más allá del umbral.</p>\n'), ''),
  ('Desde el Bardo Thodol tibetano hasta la neurotecnología moderna, desde plantas sagradas hasta frecuencias sonoras.</p>',
   'Desde el Bardo Thödol tibetano hasta la neurociencia, desde las plantas de las tradiciones hasta la música del tránsito.</p>'),
  ('<p><strong>Prepárate para descubrir el arsenal de herramientas disponibles para hacer del morir un arte consciente.</strong></p>',
   '<p><strong>Prepárate para descubrir las herramientas que, antiguas y nuevas, pueden ayudar a hacer del morir un arte consciente.</strong></p>'),
 ],
 puertas=[p_origen('Que en 1948, en Londres, un hombre que se moría y una joven trabajadora social hablaron de un lugar donde morir sin dolor y sin soledad, '
                   'y que de esa conversación nació el primer hospicio moderno, donde la muerte, cuando llega, también se cuida, se despliega en '
                   '<em>Sanación Integral</em>, Libro X de Trinity Origen, nodo 7: «La Gran Síntesis».',
                   'Libro_10/nodo_07.html')],
)
mapa_items('nodo_03.html', [('Testimonios de Acompañantes', 'Voces de Quienes Acompañan'),
                            ('Conexiones con la Constelación Trinity', None)])


# ---------------------------------------------------------------- Nodo 4
# Lo grueso lo hizo la depuración breve. Quedaban tres testimonios (Laura y Sarah salen; Isabella deja su
# lugar a la noche de 1973 en que nació la tanatología musical), los efectos de los instrumentos, el phowa sin
# la aclaración de su tradición, la «exposición gradual», el bardo que faltaba y las conexiones inventadas.
R['nodo_04.html'] = dict(reemplazos=[
  ('<li>El Bardo Thodol Actualizado: GPS para el Más Allá</li>', '<li>El Bardo Thödol Actualizado: GPS para el Más Allá</li>'),
  ('<li>Realidad Virtual: Ensayando el Viaje</li>', '<li>Realidad Virtual: El Mundo que Vuelve a la Cama</li>'),
  ('<li>Casos de Transformación Tecnológica</li>', '<li>Lo que Ninguna Técnica Reemplaza</li>'),
  ('<h2>El Bardo Thodol Actualizado: GPS para el Más Allá</h2>', '<h2>El Bardo Thödol Actualizado: GPS para el Más Allá</h2>'),
  ('<strong>Bardo Thodol</strong>', '<strong>Bardo Thödol</strong>'),
  ('<h3>Los Tres Bardos Esenciales</h3>', '<h3>Los Bardos Esenciales</h3>\n    <p>El libro describe los tres estados que se abren con la muerte (<em>chikhai</em>, <em>chönyid</em> y <em>sidpa</em>); la tradición cuenta seis bardos, y entre ellos el de esta vida.</p>'),
  ('      <li>La oportunidad de liberación en la clara luz</li>\n    </ul>',
   '      <li>La oportunidad de liberación en la clara luz</li>\n    </ul>\n'
   '    <h3>Bardo de la Realidad (Chönyid Bardo)</h3>\n'
   '    <ul>\n'
   '      <li>Lo que se abre después de la clara luz</li>\n'
   '      <li>Las apariciones pacíficas e iracundas</li>\n'
   '      <li>Reconocerlas como propias de la mente</li>\n'
   '    </ul>'),
  ('    <blockquote>Usamos una versión adaptada del Bardo con mi madre. En lugar de deidades tibetanas, usamos sus propios símbolos sagrados. Funcionó. Murió con una sonrisa, como si reconociera algo hermoso." — Laura, psicóloga transpersonal</blockquote>\n', ''),
  (('    <p><strong>Conexión con El Dolor como Portal:</strong> En ese libro, la respiración consciente', 'dimensiones más amplias de la existencia.</p>\n'), ''),
  (('    <p><strong>Conexión con Los Vínculos Sagrados:</strong>', 'estructuras psíquicas de orientación.</p>\n'), ''),
  (('    <p><strong>Conexión con Civilización Galáctica:</strong> En ese libro, el sonido', 'actúan como guías no verbales.</p>\n'), ''),
  (('    <p><strong>Conexión con El Dolor como Portal:</strong> En ese libro se describe cómo algunas plantas', 'recibir el pasaje con menos resistencia.</p>\n'), ''),
  ('<p>El sonido es vibración, y la vibración es el lenguaje fundamental del universo. En el umbral de la muerte, el sonido se vuelve medicina poderosa.</p>',
   '<p>El sonido es vibración, y para muchas tradiciones la vibración es el primer lenguaje del universo. En el umbral de la muerte, el sonido acompaña como pocas cosas.</p>'),
  ('y la musicoterapia forma parte de muchos equipos de cuidados paliativos.</p>',
   'y la musicoterapia forma parte de muchos equipos de cuidados paliativos. Nació de una noche de 1973: Therese Schroeder-Sheker, una estudiante de música que trabajaba como auxiliar en un geriátrico, se quedó con un hombre que moría de enfisema, se inclinó a su oído izquierdo y le cantó, casi en un susurro, cantos gregorianos: el <em>Kyrie</em>, el <em>Ubi caritas</em>, el <em>Salve Regina</em>. Él empezó a respirar más tranquilo, y respiraron juntos.</p>'),
  ('<li><strong>Cuencos Tibetanos:</strong> Armónicos que disuelven bloqueos</li>', '<li><strong>Cuencos Tibetanos:</strong> Un sonido que se apaga despacio</li>'),
  ('<li><strong>Didgeridoo:</strong> Frecuencias graves anclan y liberan</li>', '<li><strong>Didgeridoo:</strong> Un sonido grave y continuo</li>'),
  ('<li><strong>Gongs:</strong> Ondas que rompen patrones rígidos</li>', '<li><strong>Gongs:</strong> Ondas largas, para quien las disfruta</li>'),
  ('<li><strong>Playlist Personalizada:</strong> Sus músicas significativas</li>', '<li><strong>Lista Personal:</strong> Sus músicas significativas</li>'),
  ('    <blockquote>Creé una \'partitura de muerte\' para mi padre músico. Comenzó con sus jazz favoritos y terminó con cantos gregorianos. Murió en el silencio entre dos notas." — Isabella, musicoterapeuta</blockquote>\n', ''),
  (('    <p><strong>Conexión con Psicología Cuántica:</strong> La <strong>Nota Raíz de Vida</strong>', 'facilitar un pasaje armonioso.</p>\n'), ''),
  ('<h2>Realidad Virtual: Ensayando el Viaje</h2>', '<h2>Realidad Virtual: El Mundo que Vuelve a la Cama</h2>'),
  ('<p>La realidad virtual empieza a usarse en cuidados paliativos para llevar paisajes a quien ya no puede salir de su cama.</p>',
   '<p>La realidad virtual empieza a usarse en cuidados paliativos para llevar paisajes a quien ya no puede salir de su cama. En un estudio japonés, veinte pacientes con cáncer terminal visitaron con un visor un lugar de su memoria o su propia casa, y después de ese viaje dijeron sentir menos dolor, cansancio y angustia (Niki y otros, 2019). Es un estudio pequeño y sin grupo de comparación, pero señala un camino.</p>'),
  (('    <h3>Protocolos Terapéuticos</h3>', '<li><strong>Práctica:</strong> Repetir hasta familiaridad</li>\n    </ul>'),
   '    <h3>Cómo se Usa</h3>\n'
   '    <ul>\n'
   '      <li><strong>Elección:</strong> El lugar lo elige la persona</li>\n'
   '      <li><strong>Acompañamiento:</strong> Nunca solo, siempre guiado</li>\n'
   '      <li><strong>Cuidado:</strong> Si aparece angustia, se detiene</li>\n'
   '      <li><strong>Integración:</strong> Conversar lo que se vio</li>\n'
   '    </ul>'),
  ('<h3>Creación del "Death Plan" Personal</h3>', '<h3>Creación del Plan Personal para el Final</h3>'),
  ('<p>Como tenemos birth plans, necesitamos death plans:</p>', '<p>Como existen los planes de parto, hacen falta planes para el final:</p>'),
  ('<li>Repite hasta que sea natural</li>', '<li>Repite, sin forzar</li>'),
  ('<p><strong>En el momento de la muerte, este "músculo" estará entrenado.</strong></p>',
   '<p><strong>En el momento de la muerte, este "músculo" estará entrenado.</strong></p>\n'
   '    <p>En el Tíbet, el <em>phowa</em> se aprende con un maestro, y la propia tradición cuida que la práctica no se adelante a su hora: quien lo practica suele terminar con una oración por la vida larga. Aquí se ensaya como imagen, y siempre se vuelve. ' + OJOS + '</p>'),
  ('<h2>Casos de Transformación Tecnológica</h2>\n    <blockquote><strong>Sarah, 42 años - Cáncer Terminal</strong> "El ensayo de psilocibina en el que participé cambió todo. Vi mi muerte como nacimiento. El tumor ya no era enemigo, era maestro. Mis últimos meses fueron los más vivos de mi vida.</blockquote>',
   '<h2>Lo que Ninguna Técnica Reemplaza</h2>'),
  ('<p><strong>Conexión con Civilización Galáctica:</strong> En ese libro se explora el uso de tecnologías sonoras y visuales para facilitar estados de paz y expansión. La clave, como se menciona en <strong>Psicología Cuántica</strong>, no está en la sofisticación del aparato, sino en la intención consciente con la que se emplea.</p>',
   '<p>La clave no está en la sofisticación del aparato, sino en la intención consciente con la que se emplea.</p>'),
  ('<p>Has explorado el arsenal de tecnologías disponibles para hacer del morir un arte consciente. Antiguas y nuevas, todas apuntan a lo mismo:',
   '<p>Has explorado las tecnologías, antiguas y nuevas, que pueden ayudar a hacer del morir un arte consciente. Todas apuntan a lo mismo:'),
 ],
 puertas=[portal('Que el bardo no es solo lo que viene después de la muerte sino la condición de toda vida —el intervalo en que algo terminó y lo otro '
                 'todavía no empezó—, y que el duelo se habita como se habita ese entre, se despliega en <em>El Duelo</em>, Libro 5 del Portal Público, '
                 'nodo 10: «El Bardo Permanente».',
                 '05_Duelo/duelo_nodo_10.html')],
)
titulo_nodo('nodo_04.html', 'TECNOLOGÍAS DE CONSCIENCIA PARA EL TRÁNSITO', 'Tecnologías de Consciencia para el Tránsito')


# ---------------------------------------------------------------- Nodo 5
# La firma «Swami Premananda» sale (es el nombre de un gurú condenado en 1997, y la frase no tiene fuente): la
# imagen pasa a la Bṛhadāraṇyaka. El culto y el monje de IT dejan su lugar a Kornfield; la kundalini, las ECM
# y las señales encuentran su linaje y su cuidado; «La Paradoja de la Práctica», copia del Nodo 2, queda allí.
R['nodo_05.html'] = dict(reemplazos=[
  ('<li>La tiranía del "debería"</li>', '<li>La tiranía del "debería" (así la llamó Karen Horney, en 1950)</li>'),
  ('<blockquote>Pasé 10 años \'matando mi ego\' hasta que me di cuenta: el que quería matarlo ERA el ego. Es como una mano intentando agarrarse a sí misma." — Swami Premananda</blockquote>',
   '<p>La tradición lo dijo hace más de dos mil quinientos años. En la <em>Bṛhadāraṇyaka Upaniṣad</em> (3.4.2), a quien le pide que le muestre el ser como se muestra una vaca o un caballo, el sabio Yājñavalkya le responde: no puedes ver al que ve el ver. Quien quiere matar al ego tropieza con lo mismo, porque el que quiere matarlo también es el ego. Es como una mano intentando agarrarse a sí misma.</p>'),
  ('      <li>Terror y éxtasis entrelazados</li>\n    </ul>',
   '      <li>Terror y éxtasis entrelazados</li>\n    </ul>\n'
   '    <p>El cachemir Gopi Krishna contó el suyo, que empezó en 1937 y lo atormentó durante años, en <em>Kundalini</em> (1967). Las tradiciones que la nombran piden despertarla despacio y con maestro; y lo que se siente en el cuerpo se consulta primero con su nombre médico.</p>'),
  ('<li>Salir del cuerpo muestra: no eres el cuerpo</li>', '<li>Quienes salieron del cuerpo cuentan: no eres el cuerpo</li>'),
  ('<li>Revisión de vida revela: no eres tu historia</li>', '<li>La revisión de la vida les mostró: no eres tu historia</li>'),
  ('<li>La luz muestra: eres más vasto</li>', '<li>La luz les dijo: eres más vasto</li>'),
  ('      <li>Regresar es renacer diferente</li>\n    </ul>',
   '      <li>Regresar es renacer diferente</li>\n    </ul>\n'
   '    <p>En 2001, el cardiólogo Pim van Lommel publicó en <em>The Lancet</em> un estudio con 344 pacientes reanimados después de un paro cardíaco: 62, casi uno de cada cinco, contaron una experiencia así, y muchos cambiaron su manera de vivir en los años siguientes.</p>'),
  ('<li>"No mi voluntad, sino la Tuya"</li>', '<li>"No mi voluntad, sino la Tuya" (Lucas 22, 42)</li>'),
  ('      <li>La muerte física, sin el miedo de antes</li>\n    </ul>',
   '      <li>La muerte física, sin el miedo de antes</li>\n    </ul>\n'
   '    <p>Lo que protege es poder decirse: esto es un estado. Mientras esa frase esté disponible, se navega. Cuando se pierde, o el terror o la sensación de no ser real siguen al día siguiente, se pide ayuda.</p>'),
  ('      <li>Crear nueva identidad "despierta"</li>\n    </ul>',
   '      <li>Crear nueva identidad "despierta"</li>\n    </ul>\n'
   '    <p><strong>Conexión con <a href="../Libro_12/nodo_07.html">La Civilización Galáctica</a>:</strong> Su último nodo lo dice con una paradoja: para graduarse, hay que soltar el deseo de graduación.</p>'),
  ('<p>Ante la duda, la consulta con un profesional va primero.</p>',
   '<p>Ante la duda, la consulta con un profesional va primero. Desde 1994, el manual de diagnóstico de la psiquiatría estadounidense reconoce el «problema religioso o espiritual», a propuesta de David Lukoff y sus colegas: una crisis espiritual puede atenderse sin confundirla con una enfermedad, y sin pasar por alto una que sí lo es.</p>'),
  ('<h3>La Bypassing Espiritual</h3>\n    <p>Usar la "muerte del ego" para evitar responsabilidades humanas.</p>',
   '<h3>El Bypass Espiritual</h3>\n    <p>Usar la "muerte del ego" para evitar responsabilidades humanas. John Welwood le puso nombre en 1984: el <em>bypass</em> espiritual.</p>'),
  ('    <blockquote>Mi maestro usaba \'no hay yo\' para justificar abusos. \'No hay víctima ni victimario\', decía. Tomó años entender: la realización genuina AUMENTA la responsabilidad, no la elimina." — Superviviente de culto</blockquote>',
   '    <p>Jack Kornfield, que fue monje en Tailandia y volvió para ser psicólogo, dedicó páginas de <em>Camino con corazón</em> (1993) a los problemas con los maestros, también a los que usan la enseñanza para justificar abusos. Su conclusión vale aquí: la realización genuina aumenta la responsabilidad, no la elimina. Y una regla simple protege: ' + PORTAL + '.</p>'),
  ('<p><strong>Conexión con La Voz Interior:</strong> En ese libro se explora cómo el ego puede secuestrar incluso el despertar espiritual, creando una "voz de la iluminación" que es solo el ego disfrazado. La verdadera muerte del ego no proclama, simplemente ES.</p>',
   '<p><strong>Conexión con <a href="../Libro_02/nodo_02.html">La Voz Interior</a>:</strong> En su segundo nodo, el Observador Luminoso no puede ser herido porque no tiene forma: se puede perder un trabajo, una relación, la salud, y el que mira sigue intacto. No necesita proclamarse. La verdadera muerte del ego tampoco proclama: simplemente es.</p>'),
  ('    <blockquote><strong>Robert, 10 años en monasterio</strong> "La muerte del ego fue gradual, casi imperceptible. Un día simplemente… no había nadie meditando. Solo meditación sucediendo. Esperaba fuegos artificiales. En cambio: simplicidad radical. El abad me dijo: \'Ahora vuelve al mundo. El mercado es tu monasterio.\' Trabajo en IT. Tengo esposa, hijos. Desde fuera, vida normal. Desde dentro: cada momento es samadhi. Cambio pañales en éxtasis. Codifico en vacuidad. El ego murió. La vida floreció.</blockquote>',
   '    <p>Jack Kornfield vivió años como monje en monasterios de Tailandia, la India y Birmania, y al volver descubrió que lo esperaban, intactos, sus viejos patrones: las peleas de pareja, la preocupación por el dinero. De esa vuelta escribió <em>Después del éxtasis, la colada</em> (2000): la pregunta no es solo cómo despertar, sino cómo vivir lo despierto entre la ropa sucia y las cuentas. La tradición zen lo dibujó hace siglos en el último de los diez cuadros del buey: el que volvió entra al mercado con las manos abiertas.</p>'),
  (('    <p><strong>Conexión con El Retorno a Casa:</strong> En ese libro se describe cómo el verdadero despertar', 'ha muerto y renacido.</p>\n'),
   '    <p>El verdadero despertar no nos saca del mundo: nos devuelve a él con ojos nuevos.</p>\n'),
  (('    <p><strong>Conexión con Los Vínculos Sagrados:</strong> En ese libro se explora cómo las relaciones', 'no hay ego que los necesite.</p>\n'), ''),
  ((DIV + '    <h2>La Paradoja de la Práctica</h2>', 'más íntegro se vuelve cada comienzo.</p>\n'), ''),
 ],
 puertas=[arq('Que Trinity pela el ego como una cebolla, capa por capa, y que Ibsen hizo pelar la suya a Peer Gynt hasta descubrir que no tenía centro '
              '—y que la obra no termina ahí—, se despliega en <em>El Personaje</em>, Libro 9 de <em>Arquitectura del Destino</em>, Umbral VI: «La cebolla».',
              'libro-09-el-personaje/L09-U6.html'),
          arq('Que la noche oscura no es una depresión, y que Juan de la Cruz ya sabía distinguirlas, se despliega en <em>La Grieta</em>, '
              'Libro 5 de <em>Arquitectura del Destino</em>, Umbral IV: «Noche no es depresión».',
              'libro-05-la-grieta/L05-U4.html')],
)
mapa_items('nodo_05.html', [('La Paradoja de la Práctica', None)])
titulo_nodo('nodo_05.html', 'LA MUERTE DEL EGO', 'La Muerte del Ego')


# ---------------------------------------------------------------- Nodo 6
# El de más ropaje. La física pasa a imagen corregida (Hawking, 2004); el akasha, a tradición; el «caso
# documentado» del Holocausto sale, y lo que pasa entre generaciones encuentra su estudio (Yehuda, Fonagy) y su
# cuidado (Loftus); el centésimo mono vuelve a Kōshima; el testamento cuántico pasa a testamento ético (Génesis
# 49, Chochinov); los casos reales: el Hermano Lorenzo, Miss A y Chuck Feeney. La Práctica 6.1 conserva su
# número: Las Pequeñas Muertes la cita así.
R['nodo_06.html'] = dict(reemplazos=[
  ('cada verdad vivida, altera el campo cuántico para siempre.', 'cada verdad vivida, deja su huella en el campo para siempre.'),
  ('<p>La física cuántica nos revela: <strong>la información nunca se destruye.</strong> Cada pensamiento, cada emoción, cada acción, crea ondas en el campo cuántico que reverberan eternamente. No metafóricamente - literalmente. Tu vida está escribiendo en el tejido mismo de la realidad.</p>',
   '<p>La física guarda una imagen para esto. En la mecánica cuántica, <strong>la información no se destruye</strong>: puede dispersarse hasta volverse imposible de leer, pero no desaparece. Stephen Hawking discutió casi treinta años si un agujero negro podía borrarla, y en 2004 aceptó que no. Como imagen, dice algo verdadero de una vida: nada de lo vivido se pierde del todo, aunque nadie pueda leerlo entero. Tu vida está escribiendo en el tejido mismo de la realidad.</p>'),
  ('<p><strong>Ideas que se replican</strong></p>', '<p><strong>Ideas que se replican</strong> (la palabra <em>meme</em> la acuñó Richard Dawkins en 1976)</p>'),
  ('<p><strong>Campos de forma</strong></p>', '<p><strong>Campos de forma</strong> (la hipótesis de Rupert Sheldrake, sin confirmar)</p>'),
  ('<li>Cada elección colapsa probabilidades</li>', '<li>Cada elección cierra unos caminos y abre otros</li>'),
  ('<li>Cada acto de consciencia eleva frecuencia</li>', '<li>Cada acto de consciencia cuenta</li>'),
  ('<li>Cambias el universo permanentemente</li>', '<li>Nada vuelve a ser exactamente igual</li>'),
  ('<li>Opera más allá del tiempo-espacio</li>', '<li>Es la imagen más vasta del legado</li>'),
  ('    <blockquote>Cuando entendí que cada momento de amor hacia mi hija alteraba el campo cuántico no solo para ella sino para todas las madres e hijas futuras, la crianza se volvió acto sagrado." — María, física y madre</blockquote>\n', ''),
  ('<p>Los místicos siempre lo supieron: existe una biblioteca cósmica donde cada vida está registrada. No es metáfora poética - es mecánica de consciencia. Cada vida es un libro único en esta biblioteca infinita.</p>',
   '<p>Para muchos místicos existe una biblioteca cósmica donde cada vida queda registrada. La palabra <em>akasha</em> viene del sánscrito, donde nombra el espacio, el éter; la idea del registro la difundió la teosofía a fines del siglo XIX, y la retomaron Rudolf Steiner, desde 1904, y Edgar Cayce en sus lecturas. En esa visión, cada vida es un libro único en una biblioteca infinita.</p>'),
  ('    <blockquote>Vivo cada día como si fuera una página que otros leerán durante milenios. No para impresionar, sino para servir." — Lama Tenzin</blockquote>\n'
   '    <p><strong>Conexión con Psicología Cuántica:</strong> En ese libro se explora cómo cada acto consciente crea un "surco" en el campo cuántico que facilita actos similares en otros. Tu registro personal se convierte en mapa para futuros viajeros de consciencia.</p>',
   '    <p>Es una práctica antigua. Séneca contó en <em>Sobre la ira</em> que había aprendido de su maestro Sextio a revisar cada noche, antes de dormir, el día entero: cuando se apagaba la luz y su esposa, que conocía su costumbre, guardaba silencio, se examinaba sin ocultarse nada y sin castigarse.</p>'),
  ('<p>La ciencia descubre lo que los chamanes sabían: <strong>heredamos más que genes.</strong> Heredamos patrones, traumas, dones, despertar. Y más revolucionario: podemos sanar hacia atrás y hacia adelante en el linaje.</p>',
   '<p>Muchas tradiciones lo dijeron a su manera: <strong>heredamos más que genes.</strong> Heredamos patrones, heridas, dones. Rachel Yehuda estudió a hijos de sobrevivientes del Holocausto y encontró diferencias en un gen que regula el estrés (2016); es un hallazgo que la ciencia sigue discutiendo. Lo que nadie discute es lo que pasa de una generación a otra por el trato, las palabras y los silencios. Y eso también puede cambiar.</p>'),
  ('<h3>Caso Documentado</h3>\n    <p><strong>Rachel, sobreviviente de tercera generación del Holocausto.</strong> En terapia profunda, revivió memorias de su abuela en campos de concentración - memorias imposibles de tener. Al sanar su trauma, su hija de 5 años dejó de tener pesadillas con trenes. Sanar uno sana la línea.</p>',
   '<h3>Lo que se Transmite</h3>\n'
   '    <p>En 1991, Peter Fonagy, Miriam Steele y Howard Steele entrevistaron a mujeres embarazadas sobre su propia infancia, y con esas entrevistas pudieron anticipar cómo se vincularía con ellas su bebé al año de nacer. Lo que más pesaba no era cuánto habían sufrido, sino cuánto habían podido pensarlo y ponerle palabras. Por eso sanar no cambia a los ancestros: cambia la relación con ellos, y cambia lo que llega a los que vienen.</p>\n'
   '    <p>A veces, en terapia, aparecen recuerdos que parecen de otros tiempos o de otras personas. ' + LOFTUS + '</p>'),
  ('<h3>Transmisión No-Local</h3>\n    <p>Tu transformación afecta instantáneamente a:</p>', '<h3>Hasta Dónde Llega</h3>\n    <p>Tu transformación llega, a su manera, a:</p>'),
  ('<h3>Ancestros</h3>\n    <p>Sí, retroactivamente</p>', '<h3>Ancestros</h3>\n    <p>En la relación que tienes con ellos</p>'),
  ('<h3>Descendientes</h3>\n    <p>Incluso no nacidos</p>', '<h3>Descendientes</h3>\n    <p>Por lo que les transmites, incluso a los que no nacieron</p>'),
  ('<h3>Tu línea de alma</h3>\n    <p>Todas tus encarnaciones</p>', '<h3>Tu línea de alma</h3>\n    <p>En la visión de las tradiciones que creen en el renacer</p>'),
  ('<h3>Resonancia similar</h3>\n    <p>Seres en tu frecuencia</p>', '<h3>Quienes se parecen a ti</h3>\n    <p>Por el ejemplo</p>'),
  ('<h3>Experimento de los Monos 100</h3>\n    <p>Cuando suficientes monos aprendieron a lavar batatas, TODOS los monos de islas distantes súbitamente supieron hacerlo. <strong>Tu despertar contribuye a la masa crítica de consciencia.</strong></p>',
   '<h3>El Centésimo Mono</h3>\n'
   '    <p>El relato del centésimo mono tiene una historia real detrás, más modesta y más útil. En 1953, en la isla japonesa de Kōshima, una hembra joven a la que llamaron Imo descubrió que podía lavar las batatas en el agua; le enseñó a su madre y a sus compañeros de juego, y ellos a otros. Lo nuevo viajó por la cercanía, de mano en mano. <strong>Tu despertar también viaja así: de cerca, y llega lejos.</strong></p>'),
  (('    <p><strong>Conexión con Los Vínculos Sagrados:</strong> En ese libro se describe cómo los vínculos trascienden', 'Los vínculos son cuánticos.</p>\n'), ''),
  ('<h3>El Testamento Cuántico</h3>\n    <p>Más allá del testamento legal, necesitas un testamento cuántico:</p>',
   '<h3>El Testamento Ético</h3>\n'
   '    <p>Más allá del testamento legal, hay otro, muy antiguo: el testamento ético. En la tradición judía viene de Jacob, que antes de morir reunió a sus hijos para bendecirlos (Génesis 49), y en la Edad Media se volvió costumbre escribir cartas para dejar a los hijos lo que no cabe en una herencia: lo aprendido, lo que se espera de ellos, el pedido de perdón.</p>\n'
   '    <p>La medicina paliativa llegó a lo mismo. En la terapia de la dignidad, Harvey Chochinov y sus colegas invitan a quien se está muriendo a contar lo que más quiere que se sepa y se recuerde de su vida; la conversación se graba, se transcribe y se le devuelve como un documento que puede dejar a quien quiera. De cien pacientes, nueve de cada diez quedaron satisfechos y tres de cada cuatro sintieron más dignidad (2005).</p>'),
  ('<li>¿Cómo quiero ser usado después?</li>', '<li>¿Cómo quiero ser recordado?</li>'),
  ('<li>Insights únicos</li>', '<li>Descubrimientos propios</li>'),
  ('<h3>3. Códigos de Activación</h3>', '<h3>3. Lo que Me Sostuvo</h3>'),
  ('<li>Símbolos de poder</li>\n      <li>Frecuencias de sanación</li>', '<li>Símbolos que te acompañaron</li>\n      <li>Las músicas y los lugares que te devolvieron a ti</li>'),
  ('<h3>Práctica: Redacción del Testamento Cuántico</h3>', '<h3>Práctica: Redacción del Testamento Ético</h3>'),
  ('<li><strong>Graba energéticamente</strong> - en meditación profunda</li>', '<li><strong>Léelo en voz alta</strong> - en meditación profunda</li>'),
  ('<li><strong>Suelta al campo</strong> - confía en la distribución cósmica</li>', '<li><strong>Entrégalo</strong> - a quienes amas, o guárdalo donde lo encuentren</li>'),
  ('    <blockquote>Mi testamento cuántico lo escribí a los 30, lo reescribo cada década. Es mi regalo al futuro, mi manera de seguir sirviendo cuando mi cuerpo ya no esté." — Alejandra, maestra espiritual</blockquote>\n', ''),
  ('Pero no todas las piedras crean las mismas ondas.</p>',
   'Pero no todas las piedras crean las mismas ondas.</p>\n'
   '    <p>El nombre viene de una charla de Edward Lorenz en 1972: en ciertos sistemas, una diferencia mínima al comienzo puede cambiar mucho el final.</p>'),
  ('<li>Sanan líneas temporales</li>', '<li>Sanan lo que todavía duele</li>'),
  ('      <li>Alteran la matriz de realidad</li>\n    </ul>',
   '      <li>Cambian el clima de un lugar</li>\n    </ul>\n'
   '    <p>Las cascadas se midieron: en 2010, James Fowler y Nicholas Christakis observaron, en un juego entre desconocidos, que la generosidad de uno se contagiaba a los demás y seguía viajando hasta tres pasos de distancia de quien la había empezado.</p>'),
  ('<li>Cada elección consciente eleva todo</li>', '<li>Cada elección consciente cuenta</li>'),
  (('    <h3>Historia: El Barrendero Iluminado</h3>', 'Esa no-separación es lo que altera el campo permanentemente.</p>\n'),
   '    <h3>Historia: El Cocinero del Convento</h3>\n'
   '    <p>En el convento de los carmelitas descalzos de París, en el siglo XVII, un hermano lego llamado Lorenzo de la Resurrección trabajó durante años en la cocina. Nunca predicó. Decía que entre el ruido de las ollas, con varias personas pidiéndole cosas a la vez, se sentía tan cerca de Dios como de rodillas ante el sacramento. Después de su muerte, en 1691, un sacerdote reunió sus cartas y sus conversaciones, y desde entonces se leen como <em>La práctica de la presencia de Dios</em>. <strong>No buscó dejar legado: cocinó, barrió, amó. Y su cocina todavía enseña.</strong></p>\n'),
  (('    <h3>Instituto HeartMath</h3>', '<p>Cambios epigenéticos en uno afectan al otro instantáneamente, sin importar distancia.</p>'),
   '    <h3>Experimentos de Intención Global</h3>\n'
   '    <p>Desde 1998, el Global Consciousness Project registra generadores de números aleatorios en todo el mundo y busca desvíos en los días que conmueven a todos; sus resultados siguen en discusión.</p>\n'
   '    <h3>Estudios de Gemelos</h3>\n'
   '    <p>Los gemelos idénticos nacen con marcas epigenéticas casi iguales y se van diferenciando con los años: cuanto más distinta fue su vida, más distintas sus marcas (Fraga y otros, 2005). No se afectan a distancia. Es más hermoso: lo vivido se inscribe en el cuerpo.</p>'),
  ('<li><strong>Entrelazamiento Cuántico:</strong> Tu consciencia está entrelazada con todo lo que tocaste, literal y metafóricamente.</li>',
   '<li><strong>Entrelazamiento Cuántico:</strong> En física, dos partículas entrelazadas comparten un estado aunque estén lejos, sin que viaje un mensaje entre ellas; el Nobel de 2022 premió esos experimentos. Como imagen, quedas unido a todo lo que tocaste.</li>'),
  ('<li><strong>Campos Morfogenéticos:</strong> Cada patrón que vives facilita que otros lo vivan - evolución por resonancia.</li>',
   '<li><strong>Campos Morfogenéticos:</strong> Cada patrón que vives facilitaría que otros lo vivan: es la hipótesis de Sheldrake, sin confirmar.</li>'),
  ('<p>Sarah enseñó en primaria rural por 30 años. Sin fama, sin premios. Pero amó a cada niño como propio. 20 años después de jubilar, una estudiante de neurociencia descubrió: <strong>el 80% de los niños de esa escuela rural se convirtieron en agentes de cambio en sus comunidades.</strong> Rastreó el factor común: todos tuvieron a Sarah. Su amor había alterado trayectorias de vida permanentemente.</p>',
   '<p>En una escuela de Montreal, una maestra de primer grado a la que los investigadores llamaron Miss A se propuso que todos sus alumnos aprendieran a leer antes de terminar el año. Eigil Pedersen, que había sido alumno y maestro en esa escuela, siguió durante años a los chicos que habían pasado por allí. Cuando comparó sus vidas adultas, encontró algo que no buscaba: los alumnos de Miss A habían llegado más lejos que los de las otras maestras (Pedersen, Faucher y Eaton, 1978). <strong>Sin fama, sin premios: su amor había cambiado trayectorias de vida.</strong></p>'),
  (('    <h3>El Código del Programador</h3>', 'Rosa alteró su línea genética con consciencia pura.</strong></p>\n'), ''),
  ('<li>Meditaciones en momentos de insight</li>', '<li>Meditaciones en momentos de claridad</li>'),
  ('      <li>Frecuencias de sanación codificadas</li>\n', ''),
  ('<li>"Mensajes en botellas" cuánticas</li>', '<li>"Mensajes en botellas" para el futuro</li>'),
  ('      <li>Cristales programados</li>\n', ''),
  ('      <li>Activaciones a distancia</li>\n', ''),
  ('<p><strong>Conexión con Civilización Galáctica:</strong> En ese libro se describe cómo civilizaciones avanzadas transmiten consciencia a través de campos morfogenéticos, dejando "bibliotecas vivientes" que futuros seres pueden acceder. Tu legado consciente es tu contribución a esta biblioteca cósmica.</p>',
   '<p><strong>Conexión con <a href="../Libro_11/nodo_07.html">La Consciencia Planetaria</a>:</strong> En su último nodo, la Tierra entera se imagina como una biblioteca viviente, imagen que Barbara Marciniak difundió en 1992. Tu legado consciente es tu contribución a esa biblioteca.</p>'),
  (('    <blockquote><strong>James</strong> amasó fortuna', 'Su vacío fue su mayor regalo.</strong></blockquote>'),
   '    <p>Chuck Feeney hizo una fortuna con las tiendas libres de impuestos de los aeropuertos y, desde 1982, la fue entregando en secreto: durante años, quienes recibían sus donaciones no podían decir de dónde venían. Dio más de ocho mil millones de dólares en cinco continentes, para la educación, la salud, la paz y los derechos humanos. Su fundación cerró en 2020, cumplida la tarea de darlo todo en vida, y él murió en 2023, a los 92 años, en un departamento alquilado de San Francisco. <strong>Su vacío fue su mayor regalo.</strong></p>'),
 ],
 puertas=[arq('Que en el Templo de Jerusalén había una cámara donde se daba y se recibía en secreto, para que nadie saliera debiéndole nada a un '
              'benefactor con nombre y cara, se despliega en <em>La Obra</em>, Libro 12 de <em>Arquitectura del Destino</em>, Umbral IV: «La cámara de los discretos».',
              'libro-12-la-obra/L12-U4.html')],
)
titulo_nodo('nodo_06.html', 'EL LEGADO CUÁNTICO', 'El Legado Cuántico')


# ---------------------------------------------------------------- Nodo 7
# Lo clínico primero: «¿Estoy muriendo lo suficientemente rápido?», el ayuno o purga mensual y «mi caos es parte
# del parto planetario» salen; la muerte «como transición elegida» lleva la frase de X.7; ansiedad y depresión,
# su cuidado. La década del parto pasa a etapas sin años, como en XI. Las extinciones, con su fuente y lo que
# tardó la vida en volver. Costa Rica 2025 deja su lugar a la Costa Rica que sí renació; Detroit, a Grace Lee
# Boggs. Por decisión de Arturo, el cierre saluda a la generación puente.
R['nodo_07.html'] = dict(reemplazos=[
  ('<li>2020–2030: La Década del Parto</li>', '<li>Las Etapas del Parto</li>'),
  ('<li>EL CÍRCULO SE CIERRA</li>', '<li>El Círculo se Cierra</li>'),
  ('<p>Los científicos la llaman la "Sexta Extinción Masiva".', '<p>Los científicos la llaman la «sexta extinción masiva» (Elizabeth Kolbert la contó en un libro de 2014 que ganó el Pulitzer).'),
  ('<h3>Ordovícico-Silúrico (444 millones de años)</h3>\n    <ul>\n      <li>86% de especies marinas murieron</li>\n      <li>Preparó el camino para la vida compleja</li>',
   '<h3>Ordovícico-Silúrico (444 millones de años)</h3>\n    <ul>\n      <li>Alrededor del 85 % de las especies marinas desaparecieron</li>\n      <li>La vida compleja ya existía desde hacía casi cien millones de años, y tardó millones en recuperarse</li>'),
  ('<li>75% de especies desaparecieron</li>\n      <li>Nacieron los primeros bosques</li>',
   '<li>Cerca de tres cuartas partes de las especies desaparecieron</li>\n      <li>Los primeros bosques ya cubrían la tierra, y hay quien piensa que contribuyeron a la crisis</li>'),
  ('<h3>Pérmico-Triásico (251 millones de años)</h3>\n    <ul>\n      <li>96% de especies marinas, 70% terrestres</li>\n      <li>La "Gran Mortandad" dio origen a los dinosaurios</li>',
   '<h3>Pérmico-Triásico (252 millones de años)</h3>\n    <ul>\n      <li>Según las estimaciones, entre el 80 y el 90 % de las especies marinas y cerca del 70 % de los vertebrados terrestres</li>\n      <li>La "Gran Mortandad": la vida tardó unos diez millones de años en recuperarse, y en ese mundo nuevo aparecieron los dinosaurios</li>'),
  ('<h3>Triásico-Jurásico (200 millones de años)</h3>', '<h3>Triásico-Jurásico (201 millones de años)</h3>'),
  ('<h3>Patrón Revelador</h3>\n    <p><strong>Cada extinción fue un parto.</strong> Cada muerte masiva precedió una explosión de creatividad evolutiva. La muerte a escala planetaria es el mecanismo de actualización de Gaia.</p>\n'
   '    <blockquote>Cuando entendí que las extinciones son los orgasmos creativos de la Tierra, mi eco-ansiedad se transformó en asombro sagrado." — Dra. Elena Rodríguez, paleontóloga</blockquote>',
   '<p>Son las cinco grandes extinciones que identificaron David Raup y Jack Sepkoski en 1982; las cifras son estimaciones, y cambian con cada hallazgo.</p>\n'
   '    <h3>Patrón Revelador</h3>\n'
   '    <p><strong>Cada extinción terminó abriendo un parto.</strong> Después de cada muerte masiva vino, con el tiempo, una explosión de creatividad evolutiva. Pero el tiempo de la Tierra no es el nuestro: la vida tardó millones de años en recuperarse, y para quien vive dentro de una extinción no es un parto sino una pérdida, y se llora. La sexta, además, la estamos causando nosotros: por eso todavía podemos cambiar cómo sigue.</p>\n'
   '    <p>Quien siente miedo o duelo por el planeta no está exagerando. ' + MIEDO + '</p>'),
  ('<p><strong>Conexión con El Vacío Fértil:</strong> En ese libro se describe cómo el vacío no es ausencia sino potencial puro. Las extinciones masivas son el vacío fértil de Gaia - espacios de muerte total que permiten renacimientos radicales.</p>',
   '<p><strong>Conexión con <a href="../Libro_06/index.html">El Vacío Fértil</a>:</strong> Ese libro mira el vacío como potencial y no como ausencia. En la escala de Gaia, las extinciones fueron su vacío fértil: espacios de muerte que, en millones de años, dieron lugar a renacimientos.</p>'),
  ('No somos el problema - <strong>somos el dolor de parto.</strong> Y como cualquier parto, puede ser traumático o extático dependiendo de nuestra participación.</p>',
   'No somos solo el problema: <strong>también somos el dolor de parto.</strong> Y como en todo parto, la compañía cambia mucho cómo se vive.</p>'),
  ('    <blockquote>Somos la generación bisagra. Con un pie en el mundo que muere y otro en el que nace. Nuestro trabajo no es salvar el viejo mundo, sino dar a luz al nuevo." — Joanna Macy, eco-filósofa</blockquote>',
   '    <p>Joanna Macy cuenta la época con tres historias: la de los negocios como siempre, la del gran desmoronamiento y la del Gran Giro, el paso de una sociedad que crece consumiendo a una sociedad que sostiene la vida. Las tres ocurren a la vez; lo que cada uno elige es en cuál pone el cuerpo.</p>'),
  ('<h3>Clima Caótico</h3>\n    <p>El sistema nervioso de Gaia recalibrándose</p>', '<h3>Clima Caótico</h3>\n    <p>Gaia respondiendo a lo que le hicimos: las tormentas reales no se interpretan, se atienden</p>'),
  ('<h3>Extinciones Masivas</h3>\n    <p>Hacer espacio para nuevas formas</p>', '<h3>Extinciones Masivas</h3>\n    <p>Pérdidas que se lloran, y que todavía se pueden frenar</p>'),
  ('    <h3>Mutaciones Aceleradas</h3>\n    <p>Vida experimentando rápidamente</p>\n', ''),
  ('<h3>En la Psychosfera (Campo Emocional Colectivo)</h3>', '<h3>En la Psicosfera (Campo Emocional Colectivo)</h3>'),
  ('<h3>Polarización Extrema</h3>\n    <p>La tensión antes del salto</p>',
   '<h3>Polarización Extrema</h3>\n    <p>La tensión antes del salto</p>\n'
   '    <p>Son imágenes de la época, no diagnósticos. Una ansiedad o una tristeza que duran semanas no son un síntoma del planeta: se tratan, y tratarlas no interrumpe ningún camino.</p>'),
  ('<h3>En el Campo Cuántico</h3>', '<h3>En el Campo Sutil</h3>'),
  ('<h3>Resonancia Schumann Elevándose</h3>\n    <p>El "latido" de la Tierra acelerando</p>',
   '<h3>Resonancia Schumann</h3>\n    <p>El "latido" de la Tierra, que la ciencia mide desde 1960 y que no se acelera</p>'),
  (('    <p><strong>Conexión con Psicología Cuántica:</strong> En ese libro se describe cómo la consciencia individual y la planetaria', 'son hologramas del proceso planetario.</p>\n'), ''),
  ('<h3>Homo Sapiens Homo Conscientius</h3>', '<h3>Del Homo Sapiens al Homo Conscientius</h3>'),
  ('<h3>Telepatía Emocional</h3>\n    <p>Natural, no aprendida</p>',
   '<h3>Telepatía Emocional</h3>\n    <p>Un sueño cuyo primer paso real ya se dio: en 2014, un equipo internacional transmitió saludos simples de cerebro a cerebro entre dos personas separadas por miles de kilómetros (Grau y otros)</p>'),
  ('<h3>Muerte Consciente</h3>\n    <p>Como transición elegida</p>', '<h3>Muerte Consciente</h3>\n    <p>Como transición vivida con lucidez</p>'),
  ('<h3>Identidad Planetaria</h3>\n    <p>Primaria sobre la nacional</p>',
   '<h3>Identidad Planetaria</h3>\n    <p>Primaria sobre la nacional</p>\n    <p>' + MIRARLA + '</p>'),
  ('<h3>Civilización 1.0 Civilización 2.0</h3>', '<h3>De la Civilización 1.0 a la 2.0</h3>'),
  ('<li>Economía del Regalo Cuántico</li>', '<li>Economía del Regalo</li>'),
  ('<h3>Tierra Biosfera Tierra Noosfera</h3>', '<h3>De la Tierra Biosfera a la Tierra Noosfera</h3>'),
  ('<li>Internet como proto-sistema nervioso</li>', '<li>Internet como proto-sistema nervioso (McLuhan ya lo intuía en 1964)</li>'),
  (('    <p><strong>Conexión con Civilización Galáctica:</strong> En ese libro se describe cómo cada planeta', 'La Tierra está naciendo como neurona cósmica.</p>\n'), ''),
  ('<li><strong>En crisis personales:</strong> "Mi caos es parte del parto planetario"</li>', '<li><strong>En crisis personales:</strong> "No estoy solo en esto: pido ayuda y la acepto"</li>'),
  ('<li>Ayuno/purga consciente</li>', '<li>Un día de menos: menos compras, menos pantallas</li>'),
  ('<li>Revisión: ¿Estoy muriendo lo suficientemente rápido?</li>', '<li>Revisión: ¿Qué estoy listo para soltar?</li>'),
  ('<strong>La Acción Mínima Viable:</strong>', '<strong>La Acción Más Pequeña:</strong>'),
  ('<p>Midwifing nuevos sistemas</p>', '<p>Partería de nuevos sistemas</p>'),
  ('<p>Como los hongos conectan bosques, los despiertos conectan la consciencia:</p>',
   '<p>Como los hongos conectan los árboles de un bosque —Suzanne Simard lo mostró en 1997—, los despiertos conectan la consciencia:</p>'),
  ('<li>Meditadores manteniendo frecuencia</li>', '<li>Meditadores sosteniendo la calma</li>'),
  ('<li>Sanadores limpiando trauma ancestral</li>', '<li>Sanadores acompañando heridas</li>'),
  ('<li>Visionarios descargando nuevos códigos</li>', '<li>Visionarios soñando lo que viene</li>'),
  ('    <blockquote>Siento la red. En meditación profunda, percibo millones de luces - otros haciendo este trabajo. No estamos solos. Somos un organismo despertando." — Ana, facilitadora de círculos</blockquote>\n', ''),
  ('<h2>2020–2030: La Década del Parto</h2>', '<h2>Las Etapas del Parto</h2>'),
  ('<p><strong>2020–2023:</strong> Ruptura de bolsa (pandemia como iniciación)</p>', '<p><strong>Primero:</strong> Ruptura de bolsa (lo que se creía firme se quiebra)</p>'),
  ('<p><strong>2024–2026:</strong> Contracciones acelerando (colapsos sistémicos)</p>', '<p><strong>Después:</strong> Contracciones que se aceleran (sistemas que crujen)</p>'),
  ('<p><strong>2027–2029:</strong> Transición (caos máximo, breakthrough inminente)</p>', '<p><strong>Luego:</strong> Transición (lo más difícil, justo antes de lo nuevo)</p>'),
  ('<p><strong>2030+:</strong> Nacimiento (nuevas estructuras emergiendo)</p>', '<p><strong>Al final:</strong> Nacimiento (estructuras nuevas que emergen). Solo podemos nacer, y nacer lleva su tiempo.</p>'),
  ('<p>Descarga blueprints del futuro</p>', '<p>Sueña los planos del futuro</p>'),
  ('<p><strong>Conexión con Liderazgo Consciente:</strong> En ese libro se describe cómo los líderes del nuevo paradigma no "dirigen" - sirven como canales para la inteligencia emergente. Tu rol en el parto no lo eliges con la mente - lo reconoces con el corazón.</p>',
   '<p>Tu rol en el parto no lo eliges con la mente: lo reconoces con el corazón.</p>'),
  ('<h3>La Revolución Micelial de 2025</h3>\n    <p>En Costa Rica, una red de comunidades conectadas por rituales sincronizados creó un campo tan coherente que el gobierno adoptó sus prácticas. <strong>En 6 meses: criminalidad cayó 70%, reforestación espontánea, juventud dejando drogas por meditación.</strong> Un país entero como organismo coherente.</p>',
   '<h3>El Bosque que Volvió en Costa Rica</h3>\n'
   '    <p>En 1987, a Costa Rica le quedaba poco más de una quinta parte de su territorio con bosque. En 1996, una ley forestal prohibió cambiar el uso del suelo de los bosques, y desde el año siguiente el país les paga a los dueños de la tierra por lo que el bosque da: el agua, el carbono, la vida. Hoy el bosque cubre más de la mitad del país. <strong>Un país entero dejó morir una manera de vivir de la tierra, y la tierra volvió.</strong></p>'),
  ('<p>Cuando la ciudad "murió" económicamente, algo mágico ocurrió. Sin sistema que mantener, los ciudadanos crearon otro. Granjas urbanas, economía de regalo, arte en ruinas. <strong>Detroit se volvió modelo de resiliencia post-colapso. La muerte fue su liberación.</strong></p>',
   '<p>Cuando la ciudad «murió» económicamente, algo nació en sus terrenos vacíos. En 1992, Grace Lee Boggs y James Boggs fundaron Detroit Summer: jóvenes y mayores que plantaban huertas en los lotes abandonados, pintaban murales y arreglaban casas. Hoy hay miles de huertas en la ciudad. <strong>No es que la muerte fuera buena: es que, en medio de ella, alguien eligió sembrar.</strong></p>'),
  ('<h3>Los Niños del 2012</h3>\n    <p>Los nacidos alrededor del 2012 muestran características inusuales: telepatía natural, rechazo a mentiras, conexión con naturaleza, sabiduría precoz. Los llaman "índigo" o "cristal", pero son simplemente <strong>humanos nativos del nuevo paradigma.</strong></p>',
   '<h3>Los Niños del Nuevo Paradigma</h3>\n'
   '    <p>Muchos padres sienten que sus hijos llegan con algo distinto: rechazo a la mentira, conexión con la naturaleza, una sabiduría precoz. Algunos los llaman «índigo» o «cristal»: la idea nació con Nancy Ann Tappe y se difundió en 1999 con el libro de Lee Carroll y Jan Tober. En la visión de este libro, son <strong>humanos nativos del nuevo paradigma.</strong> ' + NINO + '</p>'),
  ('<p><strong>Conexión con Educación Cuántica:</strong> En ese libro se describe cómo la educación debe evolucionar para los niños del nuevo paradigma. No es enseñarles - es no interferir con su sabiduría innata mientras les damos herramientas para el mundo de transición.</p>',
   '<p><strong>Conexión con <a href="../Libro_08/nodo_04.html">Educación Cuántica</a>:</strong> En su cuarto nodo, Plutarco lo dice con su propia imagen: la mente no es un vaso que haya que llenar sino una leña que hay que encender. Educar a los niños del nuevo paradigma es encender, y acompañar lo que necesitan para el mundo de transición.</p>'),
  ('<p>Como los monos lavando papas, cuando suficientes humanos encarnen la nueva consciencia, todos saltarán. Los cálculos varían:</p>\n'
   '    <ul>\n'
   '      <li><strong>Instituto HeartMath:</strong> 1% de población en coherencia</li>\n'
   '      <li><strong>Maharishi:</strong> Raíz cuadrada del 1% meditando</li>\n'
   '      <li><strong>Otros:</strong> 144,000 seres realizados</li>\n'
   '    </ul>',
   '<p>Muchos creen que, cuando suficientes humanos encarnen la nueva consciencia, todos saltarán. La medida que existe es de gente que actúa. Erica Chenoweth y Maria Stephan estudiaron 323 campañas de resistencia entre 1900 y 2006, y no encontraron ninguna campaña noviolenta que fracasara después de reunir, en su momento de mayor fuerza, al 3,5 % de su población; Chenoweth pide leerlo como una regla práctica, no como una ley. El efecto Maharishi y los 144.000 del Apocalipsis (7, 4), una imagen de plenitud, pertenecen a la visión.</p>'),
  ('<h3>Señales del Salto Inminente</h3>', '<h3>Señales del Salto</h3>'),
  ('    <h3>Telepatía Espontánea</h3>\n    <p>Aumentando</p>\n', ''),
  ('<h3>Sensación Colectiva</h3>\n    <p>"Algo viene"</p>',
   '<h3>Sensación Colectiva</h3>\n    <p>"Algo viene"</p>\n    <p>' + REFERENCIA + '</p>'),
  (('    <p><strong>Conexión con La Consciencia Planetaria:</strong> En ese libro se describe cómo cada práctica individual', 'No hay separación entre tu transformación y la de Gaia.</p>\n'), ''),
  ('Bienvenido a la generación más importante en la historia de la Tierra.', 'Bienvenido a la generación puente.'),
  ('<h2>EL CÍRCULO SE CIERRA</h2>', '<h2>El Círculo se Cierra</h2>'),
  ('Ahora siente a la humanidad - billones de células de su cuerpo.', 'Ahora siente a la humanidad: ocho mil millones de células de su cuerpo.'),
 ],
 puertas=[p_origen('Que dentro de la crisálida la oruga se deshace casi entera y la mariposa todavía recuerda lo que aprendió la oruga, y que solo podemos '
                   'nacer, y nacer lleva su tiempo, se despliega en <em>La Consciencia Planetaria</em>, Libro XI de Trinity Origen, nodo 4: «La Gran Transición».',
                   'Libro_11/nodo_04.html')],
)
titulo_nodo('nodo_07.html', 'LA GRAN REUNIÓN', 'La Gran Reunión')


# ---------------------------------------------------------------- Ejecución
if __name__ == '__main__':
    total = 0
    for nombre in sorted(R):
        n = aplicar(nombre, R[nombre]); total += n
        print(f'{nombre}: {n} cambios')
    print(f'Total: {total}')
