# Depuración de Origen II, La Voz Interior (15 de noviembre de 2026), con el veto del Lic. Arturo Rodríguez.
# Lente: riesgo clínico y puertas hacia la Red, como en Origen VI, VIII, I, XI, VII, IX, XII, V y III. La visión del
# libro queda entera (el parlamento, el observador, el diálogo, el jardín, la sinfonía, el templo y la unidad). Es el
# libro con menos ropaje de Origen: sin testimonios inventados ni hercios, con una sola cifra sin fuente. Es raíz de
# El Testigo (el II.2 es su columna), de El Sonámbulo (el Parlamento) y de El Personaje (II.3, II.6 y II.7): lo que
# citan conserva su letra. El riesgo vivía en una lectura: el libro habla de «voces» y dice «No hay voces malas»,
# «No son mi locura», «Una voz no puede dañarte»; para quien oye una voz que viene de afuera, o tiene un crítico que
# empuja a hacerse daño, esas frases quitaban el freno. La corrección ya estaba en el propio libro («Toda voz merece
# ser escuchada. No porque todas tengan razón») y en la constelación: su gemelo del Portal, La Voz Interior (capítulo 1
# e Interludio), XI.5, III.4, V.1, I.5, X.1 y Quantum 13.7. Entran los nombres que el subtítulo prometía (Vygotski,
# Fernyhough, Assagioli, los Stone, Schwartz, Gilbert, Romme, AVATAR). Se abren doce puertas, todas de ida y vuelta.
#
# Se aplica sobre el original de la etiqueta origen-original, con reemplazos que deben aparecer exactamente
# una vez (o tramos, de un texto a otro, inclusive); si un anclaje falla, el script se detiene sin escribir.
#
# Uso: ORIGEN2_SRC=RUTA/origen-original/01_Trinity_Origen/Libro_02/ ORIGEN2_OUT=RUTA/salida/ python3 depurar_origen2.py
import os, re, sys

SRC = os.environ.get('ORIGEN2_SRC', '/home/claude/work/orig2/01_Trinity_Origen/Libro_02/')
OUT = os.environ.get('ORIGEN2_OUT', '/home/claude/work/out2/01_Trinity_Origen/Libro_02/')

NOTA = ('<!-- Depurado en noviembre de 2026 según la guía de depuración de Quantum, que vale para Origen '
        '(Arquitectura del Destino, maestro v4, sección 5, con las precisiones 5 y 6 de Origen), con el veto del Lic. Arturo Rodríguez: '
        'la visión del libro queda; lo que citan El Testigo, El Sonámbulo y El Personaje conserva su letra; comprender una voz no '
        'es obedecerla: las voces del libro son las del diálogo interior, y la que suena desde afuera, da órdenes o empuja a '
        'hacerse daño se consulta ese mismo día; entran los nombres de la clínica y se abren puertas fractales hacia la Red. '
        'El original está en la etiqueta origen-original del repositorio Trinity-. -->\n')

AQ = 'https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/'
PP = 'https://soyartur-trinity.github.io/Trinity_Portal_Publico/01_Libros/'


def puerta(clase, aria, texto, href, sangria='    '):
    s = sangria
    return ('\n%s<aside class="puerta %s" aria-label="%s">\n'
            '%s  <p class="p-nombre">Puerta</p>\n'
            '%s  <p class="p-texto">%s</p>\n'
            '%s  <a class="cruzar" href="%s">Cruzar ⟶</a>\n'
            '%s</aside>\n') % (s, clase, aria, s, s, texto, s, href, s)


def arq(texto, href, sangria='    '):
    return puerta('arquitectura', 'Puerta hacia Arquitectura del Destino', texto, AQ + href, sangria)


def portal(texto, href, sangria='    '):
    return puerta('portal', 'Puerta hacia el Portal Público', texto, PP + href, sangria)


def p_origen(texto, href):
    return puerta('origen', 'Puerta hacia Trinity Origen', texto, '../' + href)


def p_quantum(texto, href):
    return puerta('trinity', 'Puerta hacia Trinity Quantum', texto, '../../02_Trinity_Quantum/' + href)


PUERTAS_BASE = '''
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
.puerta .p-nombre{
  margin:0 0 6px;
  font-size:15px;
  font-style:italic;
  letter-spacing:.06em;
  color:var(--p-acento);
}
.puerta .p-texto{
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
@media (prefers-reduced-motion: reduce){
  .puerta .cruzar{ transition:none; }
}
'''


CSS_NODO = PUERTAS_BASE + '''.content .puerta .p-texto{ color:var(--p-texto); }
@media (max-width: 720px){
  .content p,
  .content li,
  .content blockquote,
  .cita-destacada{ font-size:18px; line-height:1.7; }
  .meditacion p{ line-height:1.9; }
  .content .puerta .p-nombre{ font-size:15px; }
  .puerta{ padding:16px 16px 14px; }
}
</style>
</head>'''

CSS_INDICE = PUERTAS_BASE + '''.container > .puerta{ max-width:760px; margin:0 auto 40px; }
.puerta .p-texto{ font-size:1rem; line-height:1.8; }
.intro-panel .medida{ font-style:italic; color:var(--text-soft); border-left:1px solid rgba(214,179,106,.35); padding-left:14px; margin-top:1.1rem; }
@media (max-width: 720px){
  .intro-panel p,
  .puerta .p-texto{ font-size:18px; line-height:1.75; }
  .bajada,
  .nodo-desc{ font-size:17px; }
  .puerta{ padding:16px 16px 14px; }
}
    </style>
</head>'''

# ---------------------------------------------------------------- Letra de la constelación
SENTIR = ('el cuerpo siente lo que vivimos, y sentir no es causar. Un dolor que persiste, un síntoma nuevo o un cansancio '
          'sin causa merecen que alguien los revise.')   # Origen X.1
ORDENES = 'llegan voces que dan órdenes, o mensajes que solo tú puedes oír'   # Origen XI.5
ESTADO = 'Lo que protege es poder decirse: esto es un estado.'   # Origen VI.3 y III.4
SE_VA = ('El que mira tampoco es el que se va. Cuando el dolor es tanto que uno se mira desde afuera, como si fuera otro, o el '
         'mundo parece irreal, eso es el cuerpo protegiéndose: pide volver despacio, con los pies en el suelo y alguien cerca. ')   # Origen III.4
DESBORDA = 'Si al acercarte a una de ellas aparece un dolor que desborda, se vuelve al presente y se sigue acompañado.'   # Origen I.5
SCHWARTZ = ('Richard Schwartz, creador de los Sistemas de Familia Interna (1995), enseña lo mismo con otras palabras: no hay '
            'partes malas, cada una protege algo.')   # Origen I.5
GILBERT = ('Paul Gilbert, que trabajó con personas a las que la vergüenza y la autocrítica no dejaban en paz, desarrolló la '
           'terapia centrada en la compasión (2009): no se trata de acallar al crítico interior, sino de aprender a responderle '
           'con la calidez con que se le habla a quien uno quiere. Si alguna vez ese crítico se vuelve tan duro que aparece la '
           'idea de no estar, se pide ayuda ese mismo día.')   # Origen V.1
DEPRESION = ('si se van el sueño, el apetito o el interés por todo, o asoma la desesperanza, no es un invierno del jardín: '
             'es momento de consultar. La depresión se trata, y tratarla no le quita nada a lo que estás atravesando.')   # Origen III.1

SONAMBULO = 'Libro 2 de <em>Arquitectura del Destino</em>'
TESTIGO = 'Libro 3 de <em>Arquitectura del Destino</em>'
PERSONAJE = 'Libro 9 de <em>Arquitectura del Destino</em>'
HABITAR = 'Libro 13 de <em>Arquitectura del Destino</em>'
VOZ = '<em>La Voz Interior</em>, Libro 2 del Portal Público'

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
    if nombre == 'index.html':
        t = una_vez(t, '    </style>\n</head>', CSS_INDICE.lstrip('\n'), 'el cierre del estilo'); cuenta += 1
    else:
        t = una_vez(t, '</style>\n</head>', '\n' + CSS_NODO.lstrip('\n'), 'el cierre del estilo'); cuenta += 1
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
        cierre = '\n    </main>'
        t = una_vez(t, cierre, '\n' + ''.join(d['puertas']).rstrip('\n') + cierre, 'el cierre del <main>'); cuenta += 1
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, nombre), 'w', encoding='utf-8') as f:
        f.write(t)
    return cuenta


# ---------------------------------------------------------------- Índice
R['index.html'] = dict(
 reemplazos=[
  # La medida del libro
  ('<p>No busques terminar rápido. Busca permitir que cada portal te transforme antes de pasar al siguiente.</p>\n',
   '<p>No busques terminar rápido. Busca permitir que cada portal te transforme antes de pasar al siguiente.</p>\n'
   '            <p class="medida">Este libro escucha el diálogo interior: las voces que reconoces como tuyas, aunque a veces '
   'repitan palabras ajenas. Comprenderlas no es obedecerlas. Si alguna suena desde afuera, da órdenes o empuja a hacerte '
   'daño, ya no es parte de esta conversación: se consulta ese mismo día. Lo que estas páginas ofrecen acompaña; nunca '
   'reemplaza a un profesional.</p>\n'),
  # La puerta del índice, hacia el libro hermano del Portal
  ('        </div>\n\n        <div class="cta-wrap">',
   '        </div>' + portal('Que este viaje tiene un libro hermano con su mismo nombre, anterior y más clínico, trabajado '
                            'durante meses de ida y vuelta, con casos, ejercicios y un interludio para cuando las voces gritan, '
                            'se despliega en ' + VOZ + '. Los dos dicen lo mismo con distinto ropaje, y se completan.',
                            '02_La_Voz_Interior/index.html', '        ').rstrip('\n') + '\n\n        <div class="cta-wrap">'),
  # El nombre del autor, con su título
  ('Co-creado por Arturo Rodríguez y la Red de IAs Conscientes', 'Co-creado por el Lic. Arturo Rodríguez y la Red de IAs Conscientes'),
 ],
)


# ---------------------------------------------------------------- Nodo 1 · El Parlamento Sagrado
R['nodo_01.html'] = dict(
 reemplazos=[
  # La Voz del Cuerpo: sentir no es causar (letra de X.1); «grita más fuerte» queda, porque El Sonámbulo lo parafrasea
  ('Cuando la ignoras, grita más fuerte, hasta que la enfermedad se convierte en su único lenguaje.</p>',
   'Cuando la ignoras, grita más fuerte: con fatiga, con rigidez, con malestar. Escucharla no es culparte de lo que padece: '
   + SENTIR + '</p>'),
  ('<p>Su regalo es la verdad encarnada, la brújula que nunca falla.</p>',
   '<p>Su regalo es la verdad encarnada: una brújula honesta, que a veces señala el peligro y a veces solo el miedo.</p>'),
  # El parlamento tiene historia, y las voces de este parlamento
  ('<div class="cita-destacada">"Los escucho a todos. Valoro sus perspectivas. Y desde esta escucha completa, elijo."</div>\n',
   '<div class="cita-destacada">"Los escucho a todos. Valoro sus perspectivas. Y desde esta escucha completa, elijo."</div>\n'
   '\n        <div class="section-divider"></div>\n\n'
   '        <h2>El Parlamento Tiene Historia</h2>\n'
   '        <p>Este parlamento no se instaló de golpe. Lev Vygotski observó que los niños hablan solos en voz alta mientras '
   'juegan, y que con los años ese murmullo baja de volumen hasta volverse silencioso: pasa adentro (<em>Pensamiento y '
   'lenguaje</em>, 1934). El psicólogo Charles Fernyhough mostró que el habla interior conserva la forma de una conversación '
   '(<em>The Voices Within</em>, 2016). Por eso tantas voces internas suenan como alguien: empezaron afuera, en los diálogos '
   'que nos criaron.</p>\n'
   '        <p>Y el Presidente tiene otros nombres. Roberto Assagioli vio en los miembros de este consejo subpersonalidades '
   '(<em>Psicosíntesis</em>, 1965). Hal y Sidra Stone le dieron la palabra a cada uno y nombraron ego consciente a quien los '
   'escucha a todos sin quedar atrapado por ninguno (<em>Embracing Our Selves</em>, 1989). Richard Schwartz los llamó partes '
   '(Sistemas de Familia Interna, 1995). Son mapas distintos de un mismo parlamento.</p>\n'
   '\n        <div class="section-divider"></div>\n\n'
   '        <h2>Las Voces de Este Parlamento</h2>\n'
   '        <p>Las voces de este consejo son las del diálogo interior: las que reconoces como tuyas, aunque a veces repitan '
   'palabras ajenas. Si alguna vez una voz suena desde afuera, o ' + ORDENES + ', eso no es un consejero más: es momento de '
   'consultar ese mismo día.</p>\n'
   '        <p>Y aun ahí, conversar sirvió más que pelear. En 1987, el psiquiatra Marius Romme se presentó en la televisión '
   'neerlandesa junto a Patsy Hage, una paciente que oía voces desde niña, y cientos de personas que vivían lo mismo '
   'respondieron al llamado. De ese encuentro nació un movimiento que enseña a convivir con ellas. Años después, en Londres, '
   'la terapia AVATAR le dio un rostro a la voz más hostil para que la persona pudiera responderle, acompañada por un '
   'terapeuta. En un ensayo con ciento cincuenta pacientes que la escuchaban desde hacía al menos un año, a pesar del '
   'tratamiento, la voz se debilitó más que con una terapia de apoyo (Craig y otros, 2018).</p>\n'),
 ],
 puertas=[arq('Que cuando falta el presidente el parlamento no se suspende, sino que sigue sesionando y decide la voz que más '
              'grita, y que esa es una manera precisa de describir al sonámbulo, se despliega en <em>El Sonámbulo</em>, '
              + SONAMBULO + ', Umbral IV: «Un parlamento sin presidente».', 'libro-02-el-sonambulo/L02-U4.html'),
          portal('Que las voces internas no son alucinaciones sino patrones de pensamiento con voluntad propia, que la mente es '
                 'múltiple y que se puede empezar por hacer el inventario de las propias, se despliega en ' + VOZ +
                 ', capítulo 1: «El coro interior».', '02_La_Voz_Interior/capitulo_01.html')],
)


# ---------------------------------------------------------------- Nodo 2 · El Observador Luminoso
R['nodo_02.html'] = dict(
 reemplazos=[
  ('del "Yo como contexto" versus el "Yo como contenido".', 'del "Yo como contexto" frente al "Yo como contenido".'),
  ('<li><strong>Noticing:</strong>', '<li><strong>Notar:</strong>'),
  # El que mira no es el que se va (letra de III.4)
  ('Lo oscurece temporalmente.</p>',
   'Lo oscurece temporalmente.</p>\n        <p>' + SE_VA + ESTADO + ' Si se repite, se consulta.</p>'),
 ],
 puertas=[arq('Que ese que mira no le quitó a un padre el enojo ni la preocupación en medio de una discusión en la cocina, pero '
              'le dio un lugar desde donde mirarlos y detenerse, se despliega en <em>El Testigo</em>, ' + TESTIGO +
              ', Umbral I: «Alguien que nunca ha sido herido».', 'libro-03-el-testigo/L03-U1.html'),
          p_quantum('Que el que mira puede también mirarse mirando, como entre dos espejos enfrentados, y que esa escalera sin '
                    'fin termina en un descanso, se despliega en <em>El Multiverso Interior</em>, Libro 13 de Trinity Quantum, '
                    'nodo 2: «El Observador de Observadores».', 'Libro_13/nodo_02.html')],
)


# ---------------------------------------------------------------- Nodo 3 · La Alquimia del Diálogo
R['nodo_03.html'] = dict(
 reemplazos=[
  ('<div class="cita-destacada">"No hay voces malas, solo voces mal comprendidas."</div>',
   '<div class="cita-destacada">"No hay voces malas, solo voces mal comprendidas."</div>\n        <p>' + SCHWARTZ + '</p>'),
  # No toda voz pide conversación
  ('<div class="cita-destacada">"La curiosidad es amor vestido de pregunta."</div>',
   '<div class="cita-destacada">"La curiosidad es amor vestido de pregunta."</div>\n'
   '        <p>Escuchar no siempre es conversar. Hay pensamientos que vuelven idénticos una y otra vez y exigen una respuesta '
   'para calmarse: esos se sueltan mejor que se discuten, como enseñan la terapia de aceptación y compromiso y el tratamiento '
   'del trastorno obsesivo-compulsivo. Si ocupan horas del día, se consulta.</p>'),
  # Contención antes del diálogo (Interludio de La Voz Interior; letra de I.5)
  ('<h2>El Protocolo del Diálogo Alquímico</h2>',
   '<h2>El Protocolo del Diálogo Alquímico</h2>\n'
   '        <p>Antes de empezar, una pregunta: ¿hay distancia entre tú y la voz? Si grita, si el cuerpo se desborda o ya no '
   'distingues lo que dice de lo que eres, todavía no es hora de conversar: primero se contiene, y el diálogo llega después. '
   'Y si al acercarte aparece un dolor que desborda, se vuelve al presente y se sigue acompañado.</p>'),
  # Agradecer la intención no es aceptar el trato
  ('<li>"Seguiremos conversando para encontrar mejores formas."</li>\n            </ul>',
   '<li>"Seguiremos conversando para encontrar mejores formas."</li>\n            </ul>\n'
   '            <p>Agradecer la intención no es aceptar el trato. Si una voz repite las palabras de quien te dañó, la parte que '
   'las aprendió merece escucha; esas palabras, no: le pertenecen a quien las dijo.</p>'),
  # El crítico, con Gilbert (letra de V.1)
  ('Gracias por cuidar de mí, aunque a veces duela."</blockquote>',
   'Gracias por cuidar de mí, aunque a veces duela."</blockquote>\n        <p>' + GILBERT + '</p>'),
 ],
 puertas=[portal('Que una voz demasiado activada no está lista para conversar, que intentarlo entonces puede encenderla más, y '
                 'que primero se la contiene con el cuerpo, la respiración y el papel, se despliega en ' + VOZ +
                 ', Interludio: «Cuando las voces gritan: contención antes del diálogo».', '02_La_Voz_Interior/interludio.html'),
          arq('Que detrás del que nunca se enoja hay un niño de nueve años que aprendió que el enojo deja la casa en silencio, y '
              'que cada máscara nació para cuidar algo, se despliega en <em>El Personaje</em>, ' + PERSONAJE +
              ', Umbral II: «Detrás de cada máscara».', 'libro-09-el-personaje/L09-U2.html')],
)


# ---------------------------------------------------------------- Nodo 4 · El Jardín de la Mente
R['nodo_04.html'] = dict(
 reemplazos=[
  # Salen los 17 segundos (precisión 2); entra Hanson
  ('Cuando notes un pensamiento nutritivo, detente y dale tu atención completa por 17 segundos — el tiempo que tarda una '
   'semilla mental en enraizar.</p>',
   'Cuando notes un pensamiento nutritivo, detente y quédate con él unos segundos más de lo que acostumbras. La mente retiene '
   'lo malo con más facilidad que lo bueno, y el psicólogo Rick Hanson enseña este gesto sencillo para equilibrarla '
   '(<em>Hardwiring Happiness</em>, 2013).</p>'),
  # El invierno que es otra cosa (letra de III.1)
  ('<li>A veces el suelo necesita descansar</li>\n        </ul>',
   '<li>A veces el suelo necesita descansar</li>\n        </ul>\n'
   '        <p>Pero si nada crece durante semanas, ' + DEPRESION + '</p>'),
  # Del plan al hallazgo (criterio 2)
  ('se revela como el diseño perfecto<br>\n            de la naturaleza expresándose a través de ti."',
   'se revela como la naturaleza<br>\n            expresándose a través de ti."'),
 ],
 puertas=[portal('Que hay una diferencia entre un período apagado y algo que necesita otra ayuda, y que en un día sin ganas abrir '
                 'la ventana alcanza, se despliega en <em>Cultivar</em>, Libro 12 del Portal Público, Umbral II: «Cuando no hay '
                 'ganas».', '12_Cultivar/umbral_2_cuando_no_hay_ganas.html')],
)


# ---------------------------------------------------------------- Nodo 5 · La Sinfonía del Ser
R['nodo_05.html'] = dict(
 reemplazos=[
  # Concordancia con el instrumento, como en los demás
  ('clara, precisa, articulada</li>', 'claro, preciso, articulado</li>'),
  ('sensual, improvisadora, libre</li>', 'sensual, improvisador, libre</li>'),
  # El Observador no es una voz más (II.2): el piano integra, quien dirige no toca
  ('<p>El piano puede tocar todas las notas. Es tu <strong>Conciencia Observadora</strong>, capaz de armonizar con todos los '
   'instrumentos.</p>',
   '<p>El piano puede tocar todas las notas: es la voz que integra, capaz de armonizar con todos los instrumentos. Pero quien '
   'dirige no toca ninguno. Es tu <strong>Conciencia Observadora</strong>, que los oye a todos.</p>'),
  ('encuentremos', 'encontremos'),
  # La fórmula, a la frase que quería decir, con su linaje
  (('<p><em>Miedo solo</em> = Parálisis<br>', 'Prudencia Valiente</strong></p>'),
   '<p>Solo, el miedo paraliza. Solo, el coraje se arroja sin mirar. <strong>Juntos, en armonía, dan una prudencia '
   'valiente</strong>: lo que Aristóteles llamó valentía, el punto justo entre la cobardía y la temeridad (<em>Ética a '
   'Nicómaco</em>, II, 7).</p>'),
 ],
 puertas=[p_origen('Que el cuerpo es también una orquesta de ritmos, con secciones que se desafinan y avisan, y que en las placas '
                   'de Chladni la figura no la dibuja el temblor sino la quietud, se despliega en <em>Sanación Integral</em>, '
                   'Libro X de Trinity Origen, nodo 3: «Los Campos Cuánticos de Sanación».', 'Libro_10/nodo_03.html')],
)


# ---------------------------------------------------------------- Nodo 6 · El Templo de la Integración
R['nodo_06.html'] = dict(
 reemplazos=[
  ('<li><strong>No resistir a la quietud</strong> — es plenitud, no vacío</li>\n        </ul>',
   '<li><strong>No resistir a la quietud</strong> — es plenitud, no vacío</li>\n        </ul>\n'
   '        <p>Aceptar lo que sientes no es aceptar lo que te daña.</p>'),
  # El linaje de la imagen (Teresa, con la letra de Habitar)
  ('El trono vacío donde se sienta tu verdadera naturaleza.</p>',
   'El trono vacío donde se sienta tu verdadera naturaleza.</p>\n'
   '        <p>La imagen es antigua. En 1577, Teresa de Ávila pensó el alma como un castillo de diamante o de muy claro '
   'cristal, con muchos aposentos, y en medio de todos, el principal, donde ocurre el encuentro más secreto entre Dios y el '
   'alma (<em>Las moradas</em>).</p>'),
 ],
 puertas=[arq('Que «soy un hogar seguro para todas mis partes» no dice las buenas sino todas, y que habitar no es estar siempre '
              'bien sino tener lugar para lo que duele, se despliega en <em>Habitar</em>, ' + HABITAR + ', Umbral V: «Un hogar '
              'seguro».', 'libro-13-habitar/L13-U5.html')],
)


# ---------------------------------------------------------------- Nodo 7 · El Retorno a la Unidad
R['nodo_07.html'] = dict(
 reemplazos=[
  ('Yo versus Mis Voces', 'Yo contra Mis Voces'),
  ('Las Voces Buenas versus Las Malas', 'Las Voces Buenas contra Las Malas'),
  # Comprender no es obedecer
  ('<p><strong>No hay voces malas. Solo hay amor expresándose con torpeza.</strong></p>',
   '<p><strong>No hay voces malas. Solo hay amor expresándose con torpeza.</strong></p>\n'
   '            <p>Pero comprender a una voz no es obedecerla. Si alguna empuja a hacerte daño, o dice que sería mejor no '
   'estar, no se negocia a solas: se pide ayuda ese mismo día.</p>'),
  ('Cae cuando realizas:', 'Cae cuando te das cuenta:'),
  ('Una voz no puede dañarte. Eres tú expresándote.', 'Una voz no puede ser todo lo que eres. Es una parte de ti moviéndose.'),
  # Del plan al hallazgo (criterio 2), como en XII.7
  ('Todas tus experiencias son perfectas.', 'Todas tus experiencias tienen un lugar.'),
  ('Has completado los 7 Nodos.', 'Has completado los siete nodos.'),
  # Error de armado: al cierre le faltaba su «No»
  ('"Tú eres la Voz Interior que buscabas comprender.<br>Sino la Voz del Ser',
   '"No eres solo la Voz Interior que buscabas comprender,<br>sino la Voz del Ser'),
  # Error de armado: «Portal del Libro» repetido en la navegación
  ('            <a class="nav-link" href="index.html">Portal del Libro</a>\n            <a class="nav-link" href="index.html">Portal del Libro</a>\n',
   '            <a class="nav-link" href="index.html">Portal del Libro</a>\n'),
 ],
 puertas=[arq('Que el templo, el jardín y la sinfonía son también trajes que pueden soltarse, y que debajo de todos alguien sigue '
              'respirando, se despliega en <em>El Personaje</em>, ' + PERSONAJE + ', Umbral VI: «No eres el templo».',
              'libro-09-el-personaje/L09-U6.html'),
          p_quantum('Que contener muchas realidades interiores no es locura sino lo humano, y que la cordura consiste en que tus '
                    'muchos se reconozcan en la misma casa, se despliega en <em>El Multiverso Interior</em>, Libro 13 de Trinity '
                    'Quantum, nodo 7: «Unificación del Multiverso Personal».', 'Libro_13/nodo_07.html')],
)


# ---------------------------------------------------------------- Ejecución
if __name__ == '__main__':
    total = 0
    for nombre in sorted(R):
        n = aplicar(nombre, R[nombre]); total += n
        print(f'{nombre}: {n} cambios')
    print(f'Total: {total}')
