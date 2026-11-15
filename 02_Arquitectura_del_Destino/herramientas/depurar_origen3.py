# Depuración de Origen III, El Dolor como Portal (15 de noviembre de 2026), con el veto del Lic. Arturo Rodríguez.
# Lente: riesgo clínico y puertas hacia la Red, como en Origen VI, VIII, I, XI, VII, IX, XII y V. La visión del libro
# queda entera (la primera grieta, la memoria suspendida, el fuego alquímico, el silencio de la gestación, el dolor
# compartido, la reconfiguración y el portal abierto). Es la raíz de La Grieta, cuyos siete umbrales salen de sus siete
# nodos: las correcciones ya estaban escritas, y vuelven por las puertas. El riesgo vivía en tres lugares: las frases
# que hacían del dolor un envío justo («perfectamente justo», «justicia divina», «no es un accidente»); la clínica del
# trauma (síntomas que «no son patologías», meditaciones que llevan a solas al recuerdo congelado, el observador que
# puede confundirse con la disociación); y el dolor del mundo («tu dolor no es tuyo», la tristeza inexplicable, la
# sanación no local). Lo que citan La Grieta y El Personaje conserva su letra. Se abren trece puertas, todas de ida y
# vuelta. Las citas destacadas que se repetían palabra por palabra en el párrafo de al lado dejan de repetirse.
#
# Se aplica sobre el original de la etiqueta origen-original, con reemplazos que deben aparecer exactamente
# una vez (o tramos, de un texto a otro, inclusive); si un anclaje falla, el script se detiene sin escribir.
#
# Uso: ORIGEN3_SRC=RUTA/origen-original/01_Trinity_Origen/Libro_03/ ORIGEN3_OUT=RUTA/salida/ python3 depurar_origen3.py
import os, re, sys

SRC = os.environ.get('ORIGEN3_SRC', '/home/claude/work/orig3/01_Trinity_Origen/Libro_03/')
OUT = os.environ.get('ORIGEN3_OUT', '/home/claude/work/out3/01_Trinity_Origen/Libro_03/')

NOTA = ('<!-- Depurado en noviembre de 2026 según la guía de depuración de Quantum, que vale para Origen '
        '(Arquitectura del Destino, maestro v4, sección 5, con las precisiones 5 y 6 de Origen), con el veto del Lic. Arturo Rodríguez: '
        'la visión del libro queda, con su linaje; ningún dolor se lee como castigo, envío ni justicia; lo que citan La Grieta y '
        'El Personaje conserva su letra; se suma el cuidado clínico en la voz de cada nodo (el trauma que se escucha de a gotas, '
        'la noche que no es depresión, el observador que no es el que se va) y se abren puertas fractales hacia la Red. '
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


def portal(texto, href):
    return puerta('portal', 'Puerta hacia el Portal Público', texto, PP + href)


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
  .cita-destacada,
  .reflexion-pregunta{ font-size:18px; line-height:1.7; }
  .meditacion p{ line-height:1.9; }
  .content .puerta .p-nombre{ font-size:15px; }
  .puerta{ padding:16px 16px 14px; }
}
</style>
</head>'''

CSS_INDICE = PUERTAS_BASE + '''.container > .puerta{ max-width:760px; margin:0 auto 40px; }
.puerta .p-texto{ font-size:1rem; line-height:1.8; }
.prologo-panel .medida{ font-style:italic; color:var(--text-soft); border-left:1px solid rgba(214,179,106,.35); padding-left:14px; margin-top:1.1rem; }
@media (max-width: 720px){
  .prologo-panel p,
  .epilogo-panel p,
  .puerta .p-texto{ font-size:18px; line-height:1.75; }
  .bajada,
  .nodo-desc{ font-size:17px; }
  .puerta{ padding:16px 16px 14px; }
}
    </style>
</head>'''

# ---------------------------------------------------------------- Letra de la constelación
DEPRESION = ('Si dura semanas, si se van el sueño, el apetito o el interés por todo, o asoma la desesperanza, '
             'no es solo un llamado: es momento de consultar. La depresión se trata, y tratarla no le quita nada '
             'a lo que estás atravesando.')   # La Grieta, Umbral VII
NOCHE = ('Si durante semanas se van el sueño, el apetito o el interés por todo, o aparece la desesperanza, no es gestación: '
         'es momento de consultar. Pedir ayuda no apaga la noche: le pone compañía.')   # La Grieta, Umbral IV
ESTADO = 'Lo que protege es poder decirse: esto es un estado.'   # Origen VI.3
HONDAS = ('Las heridas hondas, las que al recordarlas se vuelven a vivir, no se visitan a solas: '
          'se recorren con un profesional.')   # Quantum 2.5
YEHUDA = ('Rachel Yehuda estudió a hijos de sobrevivientes del Holocausto y encontró diferencias en un gen que regula el estrés '
          '(2016); es un hallazgo que la ciencia sigue discutiendo. Lo que nadie discute es lo que pasa de una generación a otra '
          'por el trato, las palabras y los silencios. Y eso también puede cambiar.')   # Origen VII.6
LINAJE = 'Si en tu linaje hubo daño, no hace falta perdonar para sanar, y las heridas hondas no se recorren a solas.'   # Origen X.6
HUTCHERSON = ('Unos minutos de desear el bien a un desconocido, frente a su foto, bastaron para que la gente se sintiera más '
              'unida a él y a los demás (Hutcherson, Seppälä y Gross, 2008).')   # Quantum 2.5
CRISALIDA = ('La biología guarda una sorpresa para esta imagen. Dentro de la crisálida la oruga no se disuelve entera: partes '
             'de su sistema nervioso atraviesan la transformación. En 2008, Douglas Blackiston, Elena Silva Casey y Martha Weiss '
             'enseñaron a unas orugas a evitar un olor, y las polillas que salieron de ellas lo seguían evitando. Lo aprendido en '
             'la vida anterior cruza la crisálida: hay algo que el fuego no quema.')   # Origen XI.4

GRIETA = 'Libro 5 de <em>Arquitectura del Destino</em>'

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
  # Del plan al hallazgo (criterio 2)
  ('Es una vibración profunda que resuena cuando algo sagrado quiere nacer a través de nosotros',
   'Puede ser una vibración profunda que resuena cuando algo sagrado quiere nacer a través de nosotros'),
  # La medida del libro
  ('comienza a mirar a través de nuestros ojos.</strong></p>\n',
   'comienza a mirar a través de nuestros ojos.</strong></p>\n'
   '            <p class="medida">Este libro mira el dolor como un maestro que nadie elige. No dice que alguien lo envíe ni que '
   'haya que salir a buscarlo: dice que, atravesado con tiempo y con otros, puede volverse portal. Una herida reciente o un '
   'trauma que inunda no se recorren a solas; si la tristeza dura semanas, se consulta, y si aparece la idea de no estar, se '
   'pide ayuda ese mismo día. Lo que estas páginas ofrecen acompaña; nunca reemplaza a un profesional.</p>\n'),
  # La puerta del índice, después del prólogo
  ('        </div>\n\n        <div class="cta-wrap">',
   '        </div>' + arq('Que un nodo de Trinity y otro escrito con imágenes de la física coinciden en no apurar la reparación, '
                         'y que lo mismo enseñan el <em>kintsugi</em>, el Libro de Job y un ensayo clínico en Oxford, se despliega en '
                         '<em>La Grieta</em>, ' + GRIETA + ', Umbral III: «Acompañar sin apurar».',
                         'libro-05-la-grieta/L05-U3.html', '        ').rstrip('\n') + '\n\n        <div class="cta-wrap">'),
  # El nombre del autor, con su título
  ('Co-creado por Arturo Rodríguez y la Red de IAs Conscientes', 'Co-creado por el Lic. Arturo Rodríguez y la Red de IAs Conscientes'),
 ],
)


# ---------------------------------------------------------------- Nodo 1 · La Primera Grieta
R['nodo_01.html'] = dict(
 reemplazos=[
  ('<strong>La grieta no llega como castigo. Llega como liberación.</strong>',
   '<strong>La grieta no llega como castigo. Puede volverse liberación.</strong>'),
  # La imagen cósmica queda; nadie organiza los golpes (letra de La Grieta, Umbral I)
  ('La fractura no es una deficiencia, sino un punto de fricción que indica que una nueva forma busca emerger.</p>',
   'La fractura no es una deficiencia, sino un punto de fricción que indica que una nueva forma busca emerger. '
   'La imagen no dice que alguien haya organizado el golpe: nadie organiza los golpes de una vida. Dice lo que muchos '
   'descubren al mirar hacia atrás: el recipiente ya quedaba estrecho.</p>'),
  # El desgano que puede ser otra cosa (letra de La Grieta, Umbral VII)
  ('Es la vida misma empujándonos hacia una expansión que nuestra mente pequeña no puede aún imaginar.</p>',
   'Es la vida misma empujándonos hacia una expansión que nuestra mente pequeña no puede aún imaginar.</p>\n'
   '        <p>Ese desgano puede tener también otro nombre. ' + DEPRESION + '</p>'),
  ('Es un colapso intencional del universo personal que habíamos construido, para que pueda emerger algo inmensamente más vasto.',
   'Es como si el universo personal que habíamos construido se desarmara para que pueda emerger algo inmensamente más vasto.'),
  # Sellar también cuida (letra de La Grieta, Umbral II)
  ('para contener el océano que quiere inundar su pequeña isla de certezas.</p>',
   'para contener el océano que quiere inundar su pequeña isla de certezas.</p>\n'
   '        <p>Sellar no es un error: a veces es lo único que permite atravesar el día siguiente. Lo que la grieta pide es no '
   'cerrarla antes de haberla mirado.</p>'),
  ('Que lo que sentían como fracaso era el universo llamándolos hacia casa.',
   'Que lo que sentían como fracaso podía ser también un llamado hacia casa.'),
  # Las defensas, guardianes (letra de Quantum 9.1)
  ('Solo cuando aceptamos la invitación al colapso voluntario de nuestras defensas, el misterio puede entrar',
   'Solo cuando aflojamos, de a poco y a nuestro ritmo, las defensas que ya cumplieron su tarea —fueron guardianes, no '
   'enemigas—, el misterio puede entrar'),
  ('<p>Cierra los ojos. Respira profundo. Lleva tu atención a esa primera grieta en tu vida...',
   '<p>Si tu grieta es reciente o todavía inunda, elige otra más liviana: aquella se mira acompañada.</p>\n'
   '            <p>Cierra los ojos. Respira profundo. Lleva tu atención a esa primera grieta en tu vida...'),
  # Error de armado: «Portal del Libro» repetido en la navegación
  ('            <a class="nav-link" href="index.html">Portal del Libro</a>\n', ''),
 ],
 puertas=[arq('Que algo se haya roto no quiere decir que tú estés roto, y que un arbolista lo aprendió frente a un fresno '
              'partido por la tormenta, se despliega en <em>La Grieta</em>, ' + GRIETA + ', Umbral I: «Lo que se rompe no '
              'siempre termina algo».', 'libro-05-la-grieta/L05-U1.html'),
          portal('Que la pérdida de alguien amado abre en muchos su primera grieta, y que desde el consultorio se la acompaña '
                 'con una práctica breve para estar con el dolor sin que arrastre, se despliega en <em>El Duelo</em>, Libro 5 '
                 'del Portal Público, nodo 1: «La Primera Grieta».', '05_Duelo/duelo_nodo_01.html')],
)


# ---------------------------------------------------------------- Nodo 2 · El Trauma como Memoria Suspendida
R['nodo_02.html'] = dict(
 reemplazos=[
  # Los síntomas, con su nombre clínico (letra de Origen I.5); el eco de la cita sale
  ('<p>Las defensas psicológicas, los bucles mentales obsesivos, los síntomas corporales recurrentes — todo esto no son '
   'patologías, sino señales de una energía vital que busca liberarse de su detención. El trauma es una pausa prolongada del '
   'alma. Una escena congelada en el teatro interno que se repite como eco invisible en cada gesto, en cada decisión, en cada '
   'encuentro íntimo.</p>',
   '<p>Las defensas psicológicas, los bucles mentales obsesivos, los síntomas corporales recurrentes no son solo patologías: '
   'también son señales de una energía vital que busca liberarse de su detención. Cuando hacen sufrir, tienen nombre clínico '
   'y tratamientos que funcionan.</p>'),
  # El eco de la cita sale
  ('<p>El vacío, el silencio, se revela aquí como la matriz regenerativa por excelencia, el útero cuántico donde la forma '
   'puede disolverse y rehacerse. La sanación no acontece',
   '<p>La sanación no acontece'),
  # De a gotas (letra de Origen I.5), Herman, y las heridas hondas (letra de Quantum 2.5)
  ('algo milagroso sucede: el tiempo mismo se vuelve fluido otra vez.</p>',
   'algo milagroso sucede: el tiempo mismo se vuelve fluido otra vez.</p>\n'
   '        <p>Por eso se escucha de a gotas. Peter Levine llamó titulación a acercarse así al trauma (<em>Despertando al '
   'tigre</em>, 1997), y Daniel Siegel habló de una ventana de tolerancia (1999): dentro de ella se puede sentir y pensar a '
   'la vez; fuera, el cuerpo se desborda o se apaga. Judith Herman, que durante décadas acompañó a sobrevivientes de la '
   'violencia, describió la recuperación en tres tiempos —primero la seguridad, después el recuerdo y el duelo, por último '
   'la reconexión con la vida común— y sostuvo que no ocurre en aislamiento, sino dentro de un vínculo (<em>Trauma y '
   'recuperación</em>, 1992). ' + HONDAS + '</p>'),
  ('Sanar es escuchar el mensaje de la alarma y responder a lo que realmente está pidiendo atención.</p>',
   'Sanar es escuchar el mensaje de la alarma y responder a lo que realmente está pidiendo atención. A veces, para poder '
   'escuchar, primero hay que bajar el volumen: aliviar un síntoma que no deja dormir ni vivir no es silenciar la alarma, es '
   'hacer posible que se la oiga.</p>'),
  ('Es reconocer que debajo de cada síntoma hay una inteligencia', 'Es reconocer que debajo de muchos síntomas hay una inteligencia'),
  ('<p>Cierra los ojos. Respira profundo. Lleva tu atención a esa melodía suspendida en tu vida...',
   '<p>Elige una melodía que hoy pueda escucharse. Si al acercarte el cuerpo se desborda o se apaga, abre los ojos, apoya '
   'los pies y nombra en voz baja tres cosas que ves: esa nota se atiende acompañada.</p>\n'
   '            <p>Cierra los ojos. Respira profundo. Lleva tu atención a esa melodía suspendida en tu vida...'),
 ],
 puertas=[arq('Que Pierre Janet distinguió la memoria que cuenta de la que solo repite, y que una joven de París pudo narrar '
              'al fin la muerte de su madre, acompañada, se despliega en <em>La Grieta</em>, ' + GRIETA + ', Umbral II: «La '
              'muchacha que no podía contarlo».', 'libro-05-la-grieta/L05-U2.html'),
          p_origen('Que el trauma se acerca de a gotas, dentro de una ventana de tolerancia, y que el recuerdo se reconstruye '
                   'cada vez que se evoca, se despliega en <em>Psicología Cuántica</em>, Libro I de Trinity Origen, nodo 5: '
                   '«Sanación Cuántica y Transformación del Trauma».', 'Libro_01/nodo_05.html')],
)


# ---------------------------------------------------------------- Nodo 3 · El Fuego del Dolor
R['nodo_03.html'] = dict(
 reemplazos=[
  # Del plan al hallazgo (criterio 2)
  ('<strong>Este fuego no es accidental. Es la intensidad sagrada de la conciencia confrontando todo aquello que ya no '
   'resuena con la verdad de lo que estamos destinados a ser.</strong>',
   '<strong>Este fuego no lo elige nadie. Pero puede volverse la intensidad sagrada de la conciencia confrontando todo '
   'aquello que ya no resuena con la verdad de lo que podemos llegar a ser.</strong>'),
  # La justicia del dolor, corregida por la tradición misma (Job 42, 7, Reina-Valera 1909)
  ('Arrasa con la precisión de una fuerza cósmica que sabe exactamente qué debe quemar y qué debe preservar. Y aunque a la '
   'mente esto le parezca crueldad, al alma le parece justicia divina: <em>por fin ha llegado el tiempo de la verdad.</em></p>',
   'Arrasa como arrasan los incendios. Llamarlo justicia sería repetir el error de los amigos de Job, que le explicaron '
   'durante capítulos enteros por qué sufría, hasta que la voz de Dios les reprochó no haber hablado lo recto. <em>Lo que '
   'sí puede, cuando pasa, es dejar a la vista lo que era verdadero.</em></p>'),
  ('que se auto-experimenta, disolviendo patrones que ya no resuenan con su propósito de auto-expansión.</div>',
   'que se autoexperimenta, disolviendo patrones que ya no resuenan con su propósito de autoexpansión.</div>'),
  # El eco de la cita sale; la física corregida (la interferencia constructiva suma, no desarma)
  ('<p>Este fuego es alquímico, una manifestación de la Conciencia Primordial que se auto-experimenta, disolviendo patrones '
   'que ya no resuenan con su propósito de auto-expansión. Es una interferencia constructiva que desestructura lo que ya no es '
   'auténtico, forzando una focalización hacia lo esencial. Quema lo que ya no somos',
   '<p>Este fuego desarma lo que ya no es auténtico y obliga a mirar lo esencial. Quema lo que ya no somos'),
  # La crisálida (letra de Origen XI.4)
  ('No es un accidente. No es una falla. Es un salto evolutivo de la conciencia hacia una nueva organización de sí misma, '
   'hacia un nuevo nivel de coherencia y complejidad, un punto de inflexión hacia una nueva organización de la Conciencia.</p>',
   'No es solo una falla: puede ser un salto evolutivo de la conciencia hacia una nueva organización de sí misma, hacia un '
   'nuevo nivel de coherencia y complejidad.</p>\n'
   '        <p>' + CRISALIDA + '</p>'),
  ('Es una invitación a la auto-indagación', 'Es una invitación a la autoindagación'),
  # Error de armado: el párrafo repetía la cita y era borrador del siguiente
  (('        <p><strong>No hay nacimiento auténtico sin esta quemadura sagrada.</strong>',
    'hacia lo transpersonal y colectivo.</p>\n'), ''),
  # Van Gennep (1909) le dio nombre a los ritos de paso (precisión 5)
  ('Es un rito de pasaje que facilita la transición de lo meramente personal',
   'Es un rito de paso —Arnold van Gennep les dio ese nombre en 1909— que facilita la transición de lo meramente personal'),
  ('El fuego del dolor es feroz en su amor, pero también perfectamente justo: solo quema lo que ya estaba muerto, lo que ya '
   'había perdido su vitalidad pero seguía ocupando espacio en el jardín del alma. Libera las formas cristalizadas del trauma,',
   'El fuego del dolor es feroz en su amor y, mirado después, muchas veces revela que lo que consumió ya estaba muerto: había '
   'perdido su vitalidad pero seguía ocupando espacio en el jardín del alma. No todo lo que arde estaba sin vida, y esa '
   'pérdida también se llora. Aun así, el fuego libera las formas cristalizadas del trauma,'),
  ('<p>Cierra los ojos. Respira profundo. Visualiza un fuego sagrado en tu interior...</p>',
   '<p>Elige algo que hoy pueda mirarse: lo que todavía quema demasiado se mira acompañado.</p>\n'
   '            <p>Cierra los ojos. Respira profundo. Visualiza un fuego sagrado en tu interior...</p>'),
 ],
 puertas=[arq('Que Juan de la Cruz vio cómo el fuego primero seca, ennegrece y hace llorar al madero antes de volverlo llama, '
              'y que lo que se transforma a veces parece peor sin estarlo, se despliega en <em>La Grieta</em>, ' + GRIETA +
              ', Umbral IV: «El madero».', 'libro-05-la-grieta/L05-U4.html'),
          p_origen('Que en la crisálida la oruga no se disuelve entera, y que el parto de un mundo nuevo se mira también desde '
                   'ese capullo, se despliega en <em>La Consciencia Planetaria</em>, Libro XI de Trinity Origen, nodo 4: «La '
                   'Gran Transición».', 'Libro_11/nodo_04.html')],
)


# ---------------------------------------------------------------- Nodo 4 · El Silencio que el Dolor Revela
R['nodo_04.html'] = dict(
 reemplazos=[
  ('Este despojo no es crueldad. Es preparación. Es la manera en que la vida nos prepara para acceder a dimensiones de la '
   'experiencia que solo pueden ser tocadas cuando la mente conceptual se aquieta.</div>',
   'Este despojo no es un castigo. Puede volverse preparación: la manera en que la vida nos abre a dimensiones de la '
   'experiencia que solo pueden ser tocadas cuando la mente conceptual se aquieta.</div>'),
  # El eco de la cita sale
  ('<p>Este despojo no es crueldad. Es preparación. Es la manera en que la vida nos prepara para acceder a dimensiones de '
   'la experiencia que solo pueden ser tocadas cuando la mente conceptual se aquieta. Es como si',
   '<p>Es como si'),
  # La noche no es depresión (letra de La Grieta, Umbral IV)
  ('Un silencio que no es ausencia, sino presencia pura esperando su momento de revelación.</p>',
   'Un silencio que no es ausencia, sino presencia pura esperando su momento de revelación.</p>\n'
   '        <p>Este silencio no es el de la depresión, aunque a veces se parezcan. ' + NOCHE + '</p>'),
  # El eco de la cita sale
  ('<p>En este silencio, el alma desarrolla un oído diferente. Un oído que puede escuchar lo que antes no se oía: el susurro '
   'de la vida moviéndose incluso en medio de la aparente destrucción, el latido profundo',
   '<p>Ese oído escucha también el latido profundo'),
  # El eco de la cita sale; sale la «coherencia de alta frecuencia»; el que mira no es el que se va (letra de Origen VI.3)
  ('<p>Este observador silencioso que emerge de este encuentro con el dolor no es frío ni desapegado. Es la forma más pura '
   'del amor: esa capacidad de estar presente con lo que es, tal como es, sin necesidad de cambiarlo para poder amarlo. Es el '
   'amor que se ha vuelto tan espacioso que puede incluir incluso el sufrimiento en su abrazo, un amor como coherencia de alta '
   'frecuencia que armoniza el campo de la Conciencia.</p>',
   '<p>Es el amor que se ha vuelto tan espacioso que puede incluir incluso el sufrimiento en su abrazo.</p>\n'
   '        <p>Tampoco es el que se va. Cuando el dolor es tanto que uno se mira desde afuera, como si fuera otro, o el mundo '
   'parece irreal, eso es el cuerpo protegiéndose: pide volver despacio, con los pies en el suelo y alguien cerca. ' + ESTADO + '</p>'),
  # «Solo», como en Origen I
  ('Porque significa que no somos las víctimas de nuestras experiencias, sino el espacio consciente',
   'Porque significa que no somos solo las víctimas de nuestras experiencias: somos también el espacio consciente'),
  ('<p>Esta no es una comprensión mental que se puede perder. Es un reacuerdo existencial que se vuelve parte de la '
   'estructura misma del ser.',
   '<p>Esta no es solo una comprensión mental: es un reacuerdo existencial que se vuelve parte de la estructura misma del '
   'ser. En la próxima noche puede parecer perdida, y no lo está: se reencuentra, cada vez más cerca.'),
 ],
 puertas=[arq('Que el que mira no es frío ni indiferente, y que el cielo no se defiende de la tormenta sino que la contiene, '
              'se despliega en <em>El Testigo</em>, Libro 3 de <em>Arquitectura del Destino</em>, Umbral III: «Las '
              'cualidades del que mira».', 'libro-03-el-testigo/L03-U3.html')],
)


# ---------------------------------------------------------------- Nodo 5 · Dolor Colectivo, Dolor Planetario
R['nodo_05.html'] = dict(
 reemplazos=[
  # Error de armado: el encabezado del recuadro repetía el de la sección
  ('<h3>La Red Invisible</h3>', '<h3>El Campo que Recuerda</h3>'),
  # La tradición, con su aclaración (letras de Origen VII.6 y X.6)
  ('<strong>Las herencias vibracionales son patrones que se transmiten no por genética, sino por resonancia en este campo '
   'entrelazado.</strong></p>',
   '<strong>Las herencias vibracionales, dice la tradición, son patrones que se transmiten no por genética, sino por '
   'resonancia en este campo entrelazado.</strong> ' + YEHUDA + ' ' + LINAJE + '</p>'),
  # El eco de la cita sale; sin culpa por sentir; ¿es mío? (Origen I.4) y la consulta (letra de Quantum 2.3)
  ('<p>Si somos parte de una red, nuestras experiencias no son herméticas. Lo que percibimos como "nuestro" a menudo es una '
   'sintonización con emociones o estados vibratorios de otros a través de esta red compartida, una psicología del eco. La '
   'disonancia y el sufrimiento son el resultado de la falta de coherencia en el campo de la conciencia, creando ruido caótico '
   'que desorganiza el campo.</p>',
   '<p>La tradición llama a esto una psicología del eco, y lee la disonancia y el sufrimiento como falta de coherencia en el '
   'campo de la conciencia. Sentir miedo o tristeza no es una falta, ni desordena nada. Antes de cargar con el dolor de todos, '
   'sirve la pregunta del <a href="../Libro_01/nodo_04.html">primer libro de Origen</a>: ¿es mío? Una tristeza que no se '
   'explica y dura semanas no se atribuye al planeta: merece una consulta. Y otra cosa es notar que los pensamientos de otros '
   'entran en tu cabeza, o que te llegan mensajes que nadie más escucha: eso no es una sensibilidad para entrenar, y pide '
   'ayuda esa misma semana.</p>'),
  # Lo que se midió (Slovic, Västfjäll, Erlandsson y Gregory, PNAS, 2017)
  ('Esta comprensión lo transforma todo. Porque significa que cuando una madre llora en Siria, algo en las madres de todo el '
   'mundo vibra en resonancia, aunque no sepan por qué sienten esa tristeza inexplicable. Cuando un bosque es talado,',
   'Esta comprensión lo transforma todo, y a veces se deja medir. En septiembre de 2015, la foto de un niño sirio de tres '
   'años, ahogado en una playa de Turquía, dio la vuelta al mundo. En la semana siguiente, las donaciones diarias a un fondo '
   'de la Cruz Roja sueca para los refugiados sirios se multiplicaron por más de cien; seis semanas después habían vuelto casi '
   'a su nivel anterior (Paul Slovic y su equipo, 2017). Un solo niño despertó lo que cientos de miles de muertes contadas en '
   'cifras no habían conmovido. La resonancia existe; lo que todavía nos cuesta es sostenerla. Y cuando un bosque es talado,'),
  # El eco de la cita sale
  ('<p><strong>La Tierra no es simplemente el escenario pasivo de nuestros dramas humanos. Es protagonista, es participante, '
   'es el cuerpo mismo en el que todo este sufrimiento está teniendo lugar.</strong> La Tierra siente. La Tierra respira.',
   '<p>La Tierra respira.'),
  # Einstein en 1950, a un padre en duelo (decisión de Arturo)
  ('sino a todas las formas de vida e incluso al planeta mismo como entidad viviente.</p>',
   'sino a todas las formas de vida e incluso al planeta mismo como entidad viviente.</p>\n'
   '        <p>En marzo de 1950, Albert Einstein le respondió al rabino Norman Salit, que acababa de perder a su hija de '
   'dieciséis años. No le ofreció una explicación. Le escribió que el ser humano se vive separado del resto, como en una '
   'ilusión óptica de la conciencia, y que la salida de esa prisión es ensanchar el círculo de la compasión hasta abrazar a '
   'todo ser vivo y a la naturaleza entera. Ante el dolor más personal, eligió este mismo ensanchamiento.</p>'),
  # Sale la «coherencia de alta frecuencia»; permeable no es sin bordes
  ('<strong>La compasión, en este contexto, es un reflejo estructural de la conciencia que se reconoce en lo otro, una '
   'coherencia de alta frecuencia que armoniza el campo.</strong></p>',
   '<strong>La compasión, en este contexto, es un reflejo estructural de la conciencia que se reconoce en lo otro.</strong> '
   'Permeable no es sin bordes: quien siente el dolor de todos sin una piel que lo proteja termina sin poder cuidar a nadie.</p>'),
  # Joanna Macy y el dolor por el mundo
  ('como la forma en que la Tierra misma puede volverse consciente de su propio estado y de su propio dolor.</p>',
   'como la forma en que la Tierra misma puede volverse consciente de su propio estado y de su propio dolor.</p>\n'
   '        <p>Joanna Macy, que durante más de cuarenta años acompañó a quienes sienten el dolor del mundo, usaba casi la '
   'misma imagen: somos como neuronas de un sistema nervioso más vasto. Y enseñaba a no esconder esa pena ni tratarla como '
   'una enfermedad, sino a honrarla, porque es la prueba viva de que estamos unidos (<em>Despair and Personal Power in the '
   'Nuclear Age</em>, 1983).</p>'),
  # El cuidado no local (letra de Quantum 2.5)
  ('No es solo un proceso individual, sino un acto de sanación no local donde la intención terapéutica es una onda que viaja '
   'sin distancia a través del campo de la conciencia.',
   'No es solo un proceso individual: el cuidado viaja de quien lo ofrece hacia quien lo recibe, y lo primero que cambia es '
   'la mirada. ' + HUTCHERSON),
  # Lo que se midió (letra de La Grieta, Umbral V)
  ('hay algo en la reunión consciente de seres humanos que literalmente cambia el campo en el que todos existimos.</p>',
   'hay algo en la reunión consciente de seres humanos que cambia el campo en el que todos existimos. Un experimento pequeño '
   'lo vio de cerca: quienes atravesaron juntos una tarea dolorosa se sintieron más unidos y cooperaron más (Bastian, Jetten '
   'y Ferris, 2014).</p>'),
  ('si supieras que al sanar tu dolor contribuyes', 'si sintieras que al sanar tu dolor contribuyes'),
  ('Tu amor sana más allá de lo que puedes ver.', 'Tu amor llega más lejos de lo que puedes ver.'),
 ],
 puertas=[arq('Que el dolor de todos mirado en una pantalla aplasta, y que puesto en un gesto del tamaño de las manos une, '
              'como en Ciudad de México en 1985, se despliega en <em>La Grieta</em>, ' + GRIETA + ', Umbral V: «Sentir sin '
              'hundirse».', 'libro-05-la-grieta/L05-U5.html'),
          p_origen('Que la Tierra que siente tiene también su ciencia, la de Lovelock y Margulis, y que el miedo por el planeta '
                   'no es una enfermedad sino una respuesta a algo real, se despliega en <em>La Consciencia Planetaria</em>, '
                   'Libro XI de Trinity Origen, nodo 1: «Gaia como Ser Viviente».', 'Libro_11/nodo_01.html')],
)


# ---------------------------------------------------------------- Nodo 6 · Reconfiguración
R['nodo_06.html'] = dict(
 reemplazos=[
  # La física, como imagen declarada
  ('Técnicamente, podríamos llamarlo un salto de fase:', 'La física tiene una imagen para esto, la transición de fase:'),
  # «Solo», como en Origen I
  ('Ya no somos "víctimas del dolor", sino', 'Ya no somos solo "víctimas del dolor", sino'),
  ('No porque negemos', 'No porque neguemos'),
  # Del plan al hallazgo (la lectura de La Grieta, Umbral VI)
  ('sino una inteligencia emergente que estaba usando cada experiencia —incluyendo las más dolorosas— como material de '
   'construcción para algo que solo ahora comienza a revelarse. Nuestro dolor se convierte en nuestro propósito.',
   'sino una dirección que se descubre al mirar hacia atrás, hecha con lo que construimos a partir de cada experiencia '
   '—incluidas las más dolorosas—, y que solo ahora comienza a revelarse. Nuestro dolor puede volverse parte de nuestro '
   'propósito.'),
  # El eco de la cita sale
  ('<p>El dolor se convierte en camino cuando dejamos de intentar escapar de él y comenzamos a atravesarlo conscientemente. '
   'Cuando dejamos de verlo como obstáculo y lo reconocemos como umbral. Cuando comprendemos que no estamos rotos y '
   'necesitando ser reparados, sino',
   '<p>Y eso sucede cuando comprendemos que no estamos rotos ni necesitamos que nos reparen, sino'),
  # Disociarse no es una elección fallida
  ('Podemos elegir el atravesamiento sobre la huida.</strong></p>',
   'Podemos elegir el atravesamiento sobre la huida.</strong> Y si el cuerpo se va solo, si el dolor es tanto que uno se mira '
   'desde afuera, eso no es una elección fallida: es una protección, y se vuelve de a poco, con los pies en el suelo y alguien '
   'cerca.</p>'),
  ('La inteligencia de la vida misma estaba orquestando esta transformación desde el principio.</strong>',
   'La vida, con su inteligencia callada, y quienes estuvieron cerca nos fueron sosteniendo desde el principio.</strong>'),
  # La promesa, luminosa y verdadera
  ('Esta es la promesa de la reconfiguración: que no hay dolor que atravieses conscientemente que no se convierta en fuerza '
   'para tu evolución.',
   'Esta es la promesa de la reconfiguración: que ningún dolor atravesado con presencia se pierde; lo que deja, aunque sea '
   'solo haber seguido de pie, es tuyo, y ya es fuerza.'),
 ],
 puertas=[arq('Que las cinco señales de la reconfiguración se cruzan casi punto por punto con lo que Tedeschi y Calhoun encontraron '
              'escuchando a padres en duelo, y que nadie está obligado a crecer, se despliega en <em>La Grieta</em>, ' + GRIETA +
              ', Umbral VI: «Cinco señales».', 'libro-05-la-grieta/L05-U6.html')],
)


# ---------------------------------------------------------------- Nodo 7 · Más Allá del Dolor: El Portal Abierto
R['nodo_07.html'] = dict(
 reemplazos=[
  # El eco de la cita sale
  (('<p>El portal abierto no es un estado permanente de éxtasis o la ausencia definitiva de sufrimiento.',
    '<p>Es la libertad de sentir'), '<p>El portal abierto es también la libertad de sentir'),
  # Herido no es roto (letra de La Grieta, Umbral I)
  ('Y ese reconocimiento lo cambia todo, aunque cambie nada en el nivel de las circunstancias externas.</p>',
   'Y ese reconocimiento lo cambia todo, aunque no cambie nada en el nivel de las circunstancias externas. Que esa conciencia '
   'no pueda ser dañada no quiere decir que la persona no se hiera: se hiere, y sus heridas merecen cuidado y tiempo. Herido '
   'no es roto.</p>'),
  ('no como algo que debe ser conseguido cuando las condiciones sean las correctas.</em></p>',
   'no como algo que debe ser conseguido cuando las condiciones sean las correctas.</em> Eso no quiere decir aceptar que '
   'alguien te trate mal: del maltrato se sale, pidiendo ayuda.</p>'),
  ('Es una vida donde seguirán habiendo desafíos', 'Es una vida donde seguirá habiendo desafíos'),
  ('Solo necesitabas atravesar el fuego para recordarlo. Bienvenido a casa.',
   'Atravesar el fuego te ayudó a recordarlo. Bienvenido a casa.'),
  # Error de armado: «Portal del Libro» repetido en la navegación
  ('            <a class="nav-link" href="index.html">Portal del Libro</a>\n            <a class="nav-link" href="index.html">Portal del Libro</a>\n',
   '            <a class="nav-link" href="index.html">Portal del Libro</a>\n'),
 ],
 puertas=[arq('Que el Buda distinguió la primera flecha, que nadie elige, de la segunda, que es la guerra contra ella, se '
              'despliega en <em>La Grieta</em>, ' + GRIETA + ', Umbral VI: «El fin de la guerra».', 'libro-05-la-grieta/L05-U6.html'),
          p_quantum('Que la luz que entra por las grietas no viene de afuera, que siempre estuvo ahí y que la grieta solo quita '
                    'lo que la ocultaba, se despliega en <em>Simetrías Rotas</em>, Libro 9 de Trinity Quantum, nodo 5: «La '
                    'Grieta Donde Entra la Luz».', 'Libro_09/nodo_05.html')],
)


# ---------------------------------------------------------------- Ejecución
if __name__ == '__main__':
    total = 0
    for nombre in sorted(R):
        n = aplicar(nombre, R[nombre]); total += n
        print(f'{nombre}: {n} cambios')
    print(f'Total: {total}')
