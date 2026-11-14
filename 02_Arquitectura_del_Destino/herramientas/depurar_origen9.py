# Depuración completa de Origen IX, Liderazgo Consciente (14 de noviembre de 2026), con el veto del
# Lic. Arturo Rodríguez («Aprobado todo»). Lente: riesgo clínico y puertas hacia la Red, como en Origen VI,
# VIII, I, XI y VII. Es el único libro de Origen escrito para quien decide sobre otros adultos: como en VIII,
# el riesgo se mide por quien no puede vetar (el empleado, el equipo), y el libro obedece a sus mejores
# frases («coherencia tóxica», «siempre voluntario», «el martirio no es noble»). La Obra lo tomó como
# columna: todo lo que cita conserva su letra (las etapas 1 y 4, el hambre de reconocimiento, el Salvador,
# «Me fui 6 meses…», «¿A quién serví hoy?», la vela, el salvador exhausto, Atlas, los «Reframes necesarios»,
# la meditación de renovación, el llamado final y el cierre). Tres decisiones de Arturo: la metáfora del
# cáncer pasa al monocultivo; las fechas de la evolución pasan a etapas; salen los testimonios anónimos,
# salvo los dos que cita La Obra.
#
# Se aplica sobre lo publicado (el original de la etiqueta origen-original, con la depuración breve de
# octubre en el Nodo 6), con reemplazos que deben aparecer exactamente una vez (o tramos, de un texto a otro,
# inclusive); si un anclaje falla, el script se detiene sin escribir.
#
# Uso: ORIGEN9_SRC=RUTA/Trinity-/01_Trinity_Origen/Libro_09/ ORIGEN9_OUT=RUTA/salida/ python3 depurar_origen9.py
import os, re, sys

SRC = os.environ.get('ORIGEN9_SRC', '/home/claude/repos/Trinity-/01_Trinity_Origen/Libro_09/')
OUT = os.environ.get('ORIGEN9_OUT', '/home/claude/work9/out/01_Trinity_Origen/Libro_09/')

NOTA = ('<!-- Depurado entero el 14 de noviembre de 2026 según la guía de depuración de Quantum, que vale para Origen '
        '(Arquitectura del Destino, maestro v4, sección 5, con las precisiones 5 y 6 de Origen), con el veto del Lic. Arturo Rodríguez: '
        'la visión del libro queda, con su linaje; los testimonios inventados salen o dejan su lugar a casos reales; las frases puestas '
        'en boca de personas reales pasan a lo que hicieron; salen las cifras sin fuente, la vigilancia de los cuerpos y lo que se vendía '
        'como si funcionara; se suma el cuidado clínico en la voz de cada nodo y se abren puertas fractales hacia la Red. Lo que cita '
        'La Obra conserva su letra. El original está en la etiqueta origen-original del repositorio Trinity-; el Nodo 6 traía la '
        'depuración breve de octubre. -->\n')

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


PUERTA_CSS = '''.puerta{
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

CSS = ('''
/* ============================================================
   Depuración completa · 14 de noviembre de 2026
   Letra más grande en el teléfono y bloque fijo de las puertas.
   ============================================================ */
''' + PUERTA_CSS + '''.content p a, .content li a{
  color:var(--gold);
  text-decoration:underline;
  text-decoration-color:rgba(214,179,106,.45);
  text-underline-offset:3px;
}
.content p a:hover, .content li a:hover{ text-decoration-color:var(--gold); }
@media (max-width: 720px){
  .content p,
  .content li{ font-size:18px; line-height:1.7; }
  .content blockquote{ font-size:17px; line-height:1.7; }
  .puerta{ padding:16px 16px 14px; }
  .puerta .p-nombre{ font-size:15px; }
}
</style>
</head>''')

CSS_INDEX = ('''
/* ============================================================
   Depuración completa · 14 de noviembre de 2026
   Letra más grande en el teléfono, la línea con la medida del libro
   y la puerta del índice.
   ============================================================ */
.closing .medida{color:var(--text-soft);font-style:italic;margin-top:1rem;}
''' + PUERTA_CSS + '''.container > .puerta{ margin:28px 0 8px; }
@media (max-width: 720px){
  .intro-panel p, .closing p, .book-description{ font-size:18px; line-height:1.7; }
  .card-desc{ font-size:16px; }
  .puerta .p-texto{ font-size:18px; line-height:1.7; }
  .puerta{ padding:16px 16px 14px; }
}
</style>
</head>''')

R = {}


def Q(linea):
    """Quita una línea entera, con su sangría de cuatro espacios."""
    return ('    ' + linea + '\n', '')


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
        cierre = d.get('cierre', '\n  </main>')
        t = una_vez(t, cierre, '\n' + ''.join(d['puertas']).rstrip('\n') + cierre, 'el cierre del <main>'); cuenta += 1
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, nombre), 'w', encoding='utf-8') as f:
        f.write(t)
    return cuenta


# Frases de cuidado con la letra ya fijada en la constelación
MIEDO = ('Ese miedo no es una enfermedad: es una respuesta a algo real. Si quita el sueño o las ganas durante semanas, se consulta; '
         'y se alivia más haciendo con otros que leyendo a solas.')   # Origen XI.1
OJOS = ('Si alguna vez sentiste que no eras real o que te ibas de tu cuerpo, hazla con los ojos abiertos y los pies en el suelo, '
        'o déjala para otro momento.')   # Origen VII.5
ESTADO = 'Lo que protege es poder decirse: esto es un estado.'   # Origen VI.3
POEMA = 'Lo que llega en sueños o en silencio se recibe como se recibe un poema, no como una orden.'   # Origen XI.5
PERDONAR = 'Perdonar no obliga a quedarse, ni a callar, ni a reconciliarse, y no hace falta perdonar para sanar.'   # Origen X.6
COMPANIA = 'Pedir ayuda no apaga la noche: le pone compañía.'   # La Grieta, Umbral IV
NO_CARGAR = 'No hace falta cargar el dolor del otro para acompañarlo.'   # La Obra, Umbral VI


# ---------------------------------------------------------------- Índice
# La definición de liderar que dio La Obra, el linaje (Greenleaf, 1970) y la medida del libro; la puerta
# hacia el umbral donde La Obra lo presenta.
R['index.html'] = dict(
 reemplazos=[
  ('      No se trata de aprender técnicas para tener más poder, sino de atravesar una mutación interior que permita\n'
   '      sostener organizaciones más sabias, economías regenerativas, comunidades coherentes y formas de decisión\n'
   '      alineadas con el florecimiento del todo.\n'
   '    </p>\n',
   '      No se trata de aprender técnicas para tener más poder, sino de atravesar una mutación interior que permita\n'
   '      sostener organizaciones más sabias, economías regenerativas, comunidades coherentes y formas de decisión\n'
   '      alineadas con el florecimiento del todo.\n'
   '    </p>\n'
   '    <p>\n'
   '      En este libro, liderar no es mandar sobre otros: es cuidar algo para ellos, sea un equipo de cinco personas,\n'
   '      una escuela, una familia o una casa. La idea tiene nombre desde 1970, cuando Robert Greenleaf, que había pasado\n'
   '      casi cuatro décadas en una gran empresa de teléfonos, escribió <em>El servidor como líder</em> a partir de un relato\n'
   '      de Hermann Hesse: Leo, el criado que sostenía a todos en un viaje, resultó ser el guía de la orden.\n'
   '    </p>\n'),
  ('<strong>Liderazgo Consciente</strong> no propone una mejora cosmética del management,',
   '<strong>Liderazgo Consciente</strong> no propone una mejora cosmética de la gestión,'),
  ('auto-cuidado radical', 'autocuidado radical'),
  ('      El viaje comienza cuando decides no esperar a estar listo.\n    </p>\n',
   '      El viaje comienza cuando decides no esperar a estar listo.\n    </p>\n'
   '    <p class="medida">Ninguna práctica de este libro se impone a un equipo: se ofrece, y quien no quiere, no entra. '
   'Quien sostiene también es un cuerpo: si el cansancio no cede con el descanso, o aparece la idea de no estar, '
   'se pide ayuda ese mismo día.</p>\n'),
 ],
 puertas=[arq('Que liderar no es mandar sobre otros sino cuidar algo para ellos, y que la crisis de sentido no es una falla de quien '
              'la vive sino un llamado, se despliega en <em>La Obra</em>, Libro 12 de <em>Arquitectura del Destino</em>, Umbral I: «El llamado».',
              'libro-12-la-obra/L12-U1.html').replace('\n    ', '\n  ').replace('\n      ', '\n    ')],
 cierre='\n\n  <footer class="footer">',
)


# ---------------------------------------------------------------- Nodo 1
# Las «señales de que la muerte está ocurriendo» llevan primero su nombre médico; muere un papel, nunca un
# cuerpo. La ceremonia sigue, con el perdón que no daña (AA), śavāsana y el nombre propio; nadie del equipo
# está obligado a ser testigo. Semler, con lo que consta. Los testimonios anónimos salen (quedan los dos que
# cita La Obra); Chapman y Edmondson entran como casos reales; dos ideas quedan en la voz del nodo.
R['nodo_01.html'] = dict(reemplazos=[
  ('<li>Micromanagement obsesivo</li>', '<li>Microgestión obsesiva</li>'),
  ('<p><strong>Origen profundo:</strong></p>', '<p><strong>Raíces frecuentes:</strong></p>'),
  Q('<blockquote>Caso clínico: "Dirigía una empresa de 1000 personas. Revisaba cada email, aprobaba cada decisión. Mi infarto a los 45 fue mi despertar. El control era mi droga, y casi me mata."</blockquote>'),
  Q('<blockquote>Testimonio de sanación: "Cuando mi equipo ganó el premio sin mencionarme, sentí rabia. Ahí vi mi sombra. Tres años de terapia después, su éxito es mi alegría real."</blockquote>'),
  Q('<blockquote>Revolución silenciosa: "Eliminamos todos los títulos. Ahora somos \'contribuyentes\'. La productividad subió 200%. Pero lo más importante: la gente volvió a sonreír."</blockquote>'),
  ('<p><strong>Delirio compartido:</strong></p>', '<p><strong>Fantasía compartida:</strong></p>'),
  ('<li>Bypass espiritual corporativo</li>', '<li>Atajo espiritual corporativo: la espiritualidad usada para no mirar lo que duele</li>'),
  ('<li>Burnout silencioso</li>', '<li>Agotamiento silencioso</li>'),
  ('<blockquote>Momento de quiebre: "Lloré frente a mi equipo al compartir mi diagnóstico de cáncer. Por primera vez en 20 años fui humano. Ese día nació el verdadero liderazgo."</blockquote>',
   '<p>En 1996, Amy Edmondson estudió los errores con la medicación en los equipos de enfermería de dos hospitales y encontró lo que no esperaba: '
   'los equipos mejor liderados reportaban más errores, no menos. No se equivocaban más: podían decirlo. Años después llamó seguridad psicológica '
   'a ese clima, en el que nadie teme pedir ayuda ni admitir un error (1999).</p>'),
  ('<li>Paranoia funcional</li>', '<li>Desconfianza como método</li>'),
  Q('<blockquote>Transformación: "Dejamos de ver competidores y empezamos a ver ecosistema. Ahora co-creamos con quienes antes combatíamos."</blockquote>'),
  ('<blockquote>Despertar de consciencia: "Visité las casas de los 100 empleados que iba a despedir. Vi sus vidas, sus hijos, sus sueños. No pude hacerlo. Encontramos otra solución."</blockquote>',
   '<p>En enero de 2009, con los pedidos en caída, el directorio de Barry-Wehmiller le preguntó a Bob Chapman si no convenía despedir gente. '
   'Chapman se preguntó qué haría una familia en una crisis así, y la respuesta fue que todos cargaran un poco para que nadie cargara mucho: '
   'cada persona de la empresa tomó cuatro semanas de licencia sin goce de sueldo, se suspendieron los bonos de los directivos y no hubo despidos. '
   'Lo contó con Raj Sisodia en <em>Everybody Matters</em> (2015).</p>'),
  ('<p>La muerte del líder-ego no es un workshop de fin de semana. Es un proceso iniciático profundo que destruye la identidad construida sobre el poder.</p>',
   '<p>La muerte del líder-ego no es un taller de fin de semana. Es un proceso iniciático profundo que destruye la identidad construida sobre el poder.</p>\n'
   '    <p>Muere un papel, nunca el cuerpo. Si en algún momento de este descenso aparece la idea de no estar, no es parte del proceso: '
   'se pide ayuda ese mismo día.</p>'),
  Q('<blockquote>Experiencia común: "Caí de rodillas en mi oficina vacía. Por primera vez en mi vida adulta, me rendí completamente. En esa rendición encontré mi poder real."</blockquote>'),
  ('<h4>Etapa 5: La Revelación (El Insight)</h4>', '<h4>Etapa 5: La Revelación (La Comprensión)</h4>'),
  Q('<blockquote>Regalo al mundo: "Ahora ayudo a otros líderes a morir y renacer. Es el trabajo más difícil y más sagrado que existe."</blockquote>'),
  ('<blockquote>Transformación en acción: "Cambié mi lenguaje. No más \'batalla por market share\' sino \'servicio a más familias\'. No más \'crushing competition\' sino \'elevando el estándar juntos\'."</blockquote>',
   '<p>Cambia el lenguaje: ya no «batalla por la cuota de mercado» sino «servicio a más familias»; ya no «aplastar a la competencia» sino «elevar el estándar juntos».</p>'),
  ('<blockquote>Reconocimiento humilde: "Las mejores ideas no vienen DE mí, vienen A TRAVÉS de mí. Soy antena, no estación."</blockquote>',
   '<p>Las mejores ideas no vienen de ti: vienen a través de ti. Eres antena, no estación.</p>'),
  ('<li>Testigos presentes (equipo/mentores)</li>', '<li>Testigos presentes (mentores, y del equipo solo quien quiera estar)</li>'),
  ('<li>Pedir perdón a afectados</li>', '<li>Pedir perdón a quienes dañaste, salvo cuando hacerlo los dañe otra vez (así lo pide el noveno paso de Alcohólicos Anónimos, desde 1939)</li>'),
  ('<li>Acostarse en tierra (muerte simbólica)</li>', '<li>Acostarse en tierra unos minutos, en la postura que el hatha yoga llama <em>śavāsana</em>, la del cadáver</li>'),
  ('<li>Nuevo nombre/rol</li>', '<li>Escribir otra vez el propio nombre, y debajo, el nuevo rol</li>'),
  ('<li>Check-in semanal con testigos</li>', '<li>Encuentro semanal con los testigos</li>'),
  ('<h4>3. Activación del Servidor Cuántico Interno</h4>', '<h4>3. Activación del Servidor Interno</h4>'),
  # Semler, con lo que consta
  ('<blockquote>"Tenía 21 años cuando heredé la empresa familiar. A los 25, casi muero de estrés. Esa casi-muerte mató mi ego-líder. Lo que nació después revolucionó el management mundial."</blockquote>',
   '<p>Ricardo Semler tenía 21 años cuando, en 1980, su padre le dejó la conducción de Semco, una fábrica de São Paulo. A los 25 se desmayó durante '
   'la visita a una fábrica de bombas en Baldwinsville, Nueva York. Los médicos no le encontraron nada en el cuerpo: era el estrés. Cambió primero '
   'su manera de trabajar, y después la empresa. Lo contó en <em>Maverick</em> (1993).</p>'),
  ('<p><strong>1979-1984: El colapso</strong></p>', '<p><strong>1980-1984: El colapso</strong></p>'),
  ('<li>Desmayo en reunión directiva</li>', '<li>Un desmayo en una fábrica de Nueva York, a los 25</li>'),
  Q('<blockquote>El despertar: "En la camilla del hospital, lo vi claro: estaba matándome por mantener una ilusión de control. O moría yo o moría el ego. Elegí vivir."</blockquote>'),
  ('      <li>Eliminó su oficina</li>\n', ''),
  ('<li>Quitó todos los títulos</li>', '<li>Redujo la jerarquía a tres círculos</li>'),
  ('<li>Prensa: "Experimento naive"</li>', '<li>Prensa: "Experimento ingenuo"</li>'),
  ('<p><strong>1985-2020: Semco florece</strong></p>', '<p><strong>Después: Semco florece</strong></p>'),
  ('<li>Crecimiento 3000%</li>', '<li>De 4 millones de dólares de facturación en 1982 a 212 millones en 2003</li>'),
  ('      <li>Rotación &lt;2%</li>\n', ''),
  ('      <li>Sin departamento de RRHH</li>\n', ''),
  ('<li>Empleados eligen líderes</li>', '<li>Los equipos entrevistan y evalúan a sus jefes</li>'),
  ('<li>Salarios auto-determinados</li>', '<li>Muchos fijan su propio salario</li>'),
  ('<li>Horarios libres totales</li>', '<li>Horarios flexibles</li>'),
  ('<li>Decisiones por consenso</li>', '<li>Decisiones compartidas</li>'),
  ('<li>Modelo estudiado en Harvard</li>', '<li>Su artículo «Managing Without Managers», en la <em>Harvard Business Review</em> (1989)</li>'),
  ('      <li>Miles de empresas inspiradas</li>\n', ''),
  Q('<blockquote>Ricardo hoy: "No dirijo nada. No tengo oficina. No sé cuánta gente trabaja en Semco. Y la empresa nunca ha estado mejor. Matar mi ego-líder fue mi mejor decisión ejecutiva."</blockquote>'),
  # Las señales, con su nombre médico primero
  ('<h3>Síntomas de Transformación Genuina</h3>',
   '<h3>Síntomas de Transformación Genuina</h3>\n'
   '    <p>Estas señales tienen primero un nombre médico. La fatiga, el insomnio, la falta de apetito, la tristeza honda y la confusión '
   'acompañan muchas veces una transformación, y son también los signos de una depresión o de un agotamiento. Si duran más de dos semanas, '
   'si apagan las ganas de todo o si aparece la idea de no estar, no es la muerte del ego: es momento de consultar. ' + COMPANIA + '</p>'),
  ('<li>Pérdida de apetito (ayuno natural)</li>', '<li>Pérdida de apetito</li>'),
 ],
 puertas=[arq('Que el hambre de reconocimiento crece sobre una raíz, la valía atada a los logros, y que debajo del «sin mí, nada» suele haber '
              'alguien que aprendió muy temprano que valía lo que rendía, se despliega en <em>La Obra</em>, Libro 12 de <em>Arquitectura del Destino</em>, '
              'Umbral III: «Sin mí, nada».', 'libro-12-la-obra/L12-U3.html'),
          arq('Que la noche oscura y la depresión se parecen, que Juan de la Cruz ya enseñaba a distinguirlas y que pedir ayuda no apaga la '
              'noche sino que le pone compañía, se despliega en <em>La Grieta</em>, Libro 5 de <em>Arquitectura del Destino</em>, Umbral IV: '
              '«Noche no es depresión».', 'libro-05-la-grieta/L05-U4.html')],
)


# ---------------------------------------------------------------- Nodo 2
# Linaje (Taylor, Koestler, Maturana y Varela, Laloux; Robertson; Boeke y Endenburg; los cuáqueros e Ignacio)
# y la sombra de la resonancia (Janis, Harvey). Los lobos salen (Mech, 1999); entran los ibis y las abejas.
# Gore y Buurtzorg, con lo que consta. «No cuenta las horas» obedece al Nodo 6.
R['nodo_02.html'] = dict(reemplazos=[
  ('cada célula tiene el ADN completo.</p>',
   'cada célula tiene el ADN completo.</p>\n'
   '    <p>La imagen tiene historia. En 1911, Frederick Taylor escribió <em>Principios de la administración científica</em>, el manual de la '
   'empresa como máquina. En 1967, Arthur Koestler llamó holón a lo que es a la vez un todo y la parte de un todo mayor, y holarquía a la trama '
   'que forman. En 1973, los chilenos Humberto Maturana y Francisco Varela llamaron autopoiesis a la capacidad de los seres vivos de producirse '
   'a sí mismos. Y en 2014, Frederic Laloux reunió en <em>Reinventar las organizaciones</em> las empresas que ya funcionaban como organismos, '
   'guiadas por lo que llamó propósito evolutivo.</p>'),
  Q('<blockquote>Caso vivo: "Nuestra empresa no tiene departamentos fijos. Cada proyecto crea su propia estructura. Es como un río: siempre fluyendo, siempre río."</blockquote>'),
  Q('<blockquote>Testimonio: "El conserje propuso nuestra mejor innovación. En una estructura tradicional, nunca lo habríamos escuchado."</blockquote>'),
  ('<blockquote>Ejemplo transformador: Patagonia: El propósito "Salvar el planeta" organiza todo, desde productos hasta activismo. No es marketing, es ADN.</blockquote>',
   '<blockquote>Ejemplo transformador: Patagonia. Desde 2018, su propósito dice: «Estamos en el negocio para salvar nuestro planeta hogar». '
   'Organiza todo, desde los productos hasta el activismo. No es marketing, es ADN.</blockquote>'),
  ('<li>No es un slogan en la pared</li>', '<li>No es un eslogan en la pared</li>'),
  ('<li>Gaia como stakeholder</li>', '<li>Gaia como parte interesada (en 2022, Patagonia la hizo su única accionista)</li>'),
  ('<blockquote>Aplicación revolucionaria: "Cerramos la empresa cada invierno por un mes. Todos descansan, reflexionan, sueñan. Volvemos renovados. La productividad anual aumentó 40%."</blockquote>',
   '<p>El Eclesiastés lo dijo antes que nadie: «Todo tiene su tiempo» (3, 1).</p>'),
  ('<h2>Holocracia Consciente y Sociocracia Sagrada</h2>', '<h2>Holacracia Consciente y Sociocracia Sagrada</h2>'),
  ('<p>La holocracia y sociocracia no son solo metodologías - son tecnologías de consciencia organizacional que distribuyen el poder mientras mantienen coherencia.</p>',
   '<p>La holacracia y la sociocracia no son solo metodologías: son tecnologías de consciencia organizacional que distribuyen el poder mientras mantienen coherencia.</p>\n'
   '    <p>La holacracia la creó Brian Robertson en su empresa de software, Ternary, y la difundió desde 2007 con HolacracyOne; la contó en un libro '
   'de 2015. La sociocracia es más antigua: la pensó el pedagogo holandés Kees Boeke para su escuela, en los años cuarenta, y el ingeniero Gerard '
   'Endenburg la llevó a su empresa en los setenta, con el consentimiento y el doble enlace.</p>'),
  ('<h3>Holocracia Consciente: El Arte de los Círculos</h3>', '<h3>Holacracia Consciente: El Arte de los Círculos</h3>'),
  ('<li>Accountabilities: Actividades recurrentes</li>', '<li>Responsabilidades: Actividades recurrentes</li>'),
  ('<p><strong>Diferencia crítica con holocracia tradicional:</strong></p>', '<p><strong>Diferencia crítica con la holacracia tradicional:</strong></p>'),
  ('<li>Honra emociones como data</li>', '<li>Honra emociones como información</li>'),
  ('<li>CFO → Stewardo de Recursos</li>', '<li>CFO → Custodio de Recursos</li>'),
  ('<li>HR → Cultivador de Talentos</li>', '<li>Recursos Humanos → Cultivador de Talentos</li>'),
  ('<li>Modificación - Proponente integra feedback</li>', '<li>Modificación - Proponente integra los aportes</li>'),
  Q('<blockquote>Testimonio práctico: "Una decisión que tomaba semanas ahora toma una hora. Y todos la sienten suya porque sus objeciones la mejoraron."</blockquote>'),
  Q('<blockquote>Magia documentada: "La persona correcta siempre emerge. No la que quiere el poder, sino la que el círculo necesita. Es místico y práctico a la vez."</blockquote>'),
  ('<p>En la naturaleza, el liderazgo rota: los gansos cambian quién va al frente, las hormigas alternan exploradoras, los lobos rotan alfa según contexto. Solo los humanos creemos en líderes permanentes.</p>',
   '<p>En la naturaleza, el liderazgo rota. En la formación en V, las aves se turnan al frente, donde el vuelo cuesta más: en 2015, un equipo que siguió '
   'con sensores a una bandada de ibis eremitas vio que cada uno devolvía con su tiempo adelante el que había volado detrás, al reparo de otro (Voelkl y otros). '
   'Las abejas eligen casa sin una reina que decida: las exploradoras debaten con danzas hasta que una opción reúne a bastantes (Thomas Seeley, '
   '<em>Honeybee Democracy</em>, 2010). Los lobos, en cambio, no sirven de ejemplo: el «alfa» de una manada salvaje son los padres, y el biólogo '
   'que había difundido la idea la corrigió en 1999 (David Mech). Muchos humanos todavía creemos en líderes permanentes.</p>'),
  ('<h4>Rotación por Expertise</h4>', '<h4>Rotación por Saber</h4>'),
  Q('<blockquote>Caso empresarial: "En nuestra agencia, el becario de 22 años lidera el proyecto de TikTok. Es quien mejor entiende la plataforma. Los seniors aprenden de él."</blockquote>'),
  ('<li>No cuenta las horas</li>', '<li>No cuenta las horas (y aun así, alguien se las cuenta: la pasión también se agota, como recuerda el <a href="nodo_06.html">Nodo 6</a>)</li>'),
  Q('<blockquote>Testimonio: "Dejamos que quien más ama el proyecto lo lidere. La energía es contagiosa. Proyectos que arrastraban ahora vuelan."</blockquote>'),
  ('<li>Q1: Líder visionario (siembra)</li>', '<li>Primer trimestre: Líder visionario (siembra)</li>'),
  ('<li>Q2: Líder ejecutor (cultivo)</li>', '<li>Segundo trimestre: Líder ejecutor (cultivo)</li>'),
  ('<li>Q3: Líder integrador (cosecha)</li>', '<li>Tercer trimestre: Líder integrador (cosecha)</li>'),
  ('<li>Q4: Líder reflexivo (preparación)</li>', '<li>Cuarto trimestre: Líder reflexivo (preparación)</li>'),
  Q('<blockquote>Implementación: "Cada trimestre rotamos liderazgo. Evita burnout, trae perspectivas frescas, desarrolla a todos."</blockquote>'),
  Q('<blockquote>Flexibilidad radical: "No tenemos plan de sucesión. Confiamos que el líder correcto emergerá cuando se necesite. Siempre ocurre."</blockquote>'),
  ('<p>Las mejores decisiones no se toman - emergen. No se votan - se sienten. No se imponen - resuenan.</p>',
   '<p>Las mejores decisiones no se toman: emergen. No se votan: se sienten. No se imponen: resuenan.</p>\n'
   '    <p>Tiene linaje. Desde el siglo XVII, las reuniones de los cuáqueros deciden sin votar: esperan, en silencio y escuchándose, a que aparezca '
   'el sentido de la reunión. Y la pregunta del cuerpo que este proceso hace, ¿expansión o contracción?, es la que Ignacio de Loyola enseñaba a '
   'escuchar en sus <em>Ejercicios espirituales</em> con dos nombres: consolación y desolación.</p>'),
  ('<li>Campo unificado</li>', '<li>Campo compartido</li>'),
  ('<p><strong>Pasos cuánticos:</strong></p>', '<p><strong>Pasos:</strong></p>'),
  ('<p><strong>Presentación de opciones</strong></p>\n    <ul>\n      <li>Sin advocación</li>',
   '<p><strong>Presentación de opciones</strong></p>\n    <ul>\n      <li>Sin abogar por ninguna</li>'),
  ('      <li>Implementación pesada</li>\n    </ul>\n',
   '      <li>Implementación pesada</li>\n    </ul>\n'
   '    <p>La resonancia tiene una sombra. En 1972, Irving Janis llamó pensamiento de grupo a lo que pasa cuando el deseo de estar de acuerdo apaga '
   'las dudas, y en 1974 Jerry Harvey contó la paradoja de Abilene: una familia hace un viaje que ninguno quería, porque cada uno creyó que los demás '
   'sí. Si nadie se anima a decir «contracción», no es resonancia: es miedo. Por eso la ronda pregunta a cada uno, y una sola duda se escucha entera.</p>\n'),
  # Gore, con lo que consta
  ('<h4>La Empresa sin Jefes que Inventó el Gore-Tex</h4>',
   '<h4>La Empresa sin Jefes que Inventó el Gore-Tex</h4>\n'
   '    <p>Bill y Vieve Gore la fundaron en 1958, y en 1976 Bill escribió los principios de lo que llamó organización en enrejado: una trama en la '
   'que cada uno habla directamente con cualquier otro, sin pasar por jefes.</p>'),
  ('<li>10,000 empleados</li>', '<li>Unas 12.000 personas (2022), que no se llaman empleados sino asociados</li>'),
  ('<li>Equipos de máximo 150 personas</li>', '<li>Plantas pequeñas, de unas 150 personas, para que todos se conozcan (lo contó Malcolm Gladwell en 2000)</li>'),
  ('      <li>Decisiones por resonancia</li>\n', ''),
  ('<li>Waterline: Consultar si puede hundir el barco</li>', '<li>Línea de flotación: consultar con otros antes de lo que podría abrir un agujero bajo el agua y hundir el barco</li>'),
  ('      <li>Rotación &lt;5%</li>\n', ''),
  ('<li>Fortune "Best Companies" repetido</li>', '<li>En la lista de las mejores empresas para trabajar de <em>Fortune</em>, de 1984 a 2017</li>'),
  ('<li>Crecimiento sostenido 60 años</li>', '<li>Más de sesenta años de vida</li>'),
  Q('<blockquote>Testimonio empleado: "No tengo jefe. Tengo compromisos con mi equipo. Lidero algunos proyectos, sigo en otros. Es la forma más natural de trabajar."</blockquote>'),
  # Buurtzorg, con lo que consta
  ('<h4>12,000 Enfermeras, 0 Managers, Mejor Cuidado del Mundo</h4>', '<h4>Diez Mil Enfermeras, Ningún Gerente</h4>'),
  ('<li>Sin managers ni oficinas</li>', '<li>Sin gerentes</li>'),
  (('<pre>12,000 enfermeras', '15 personas en oficina central</pre>'),
   '<pre>Unas 10.000 enfermeras\n    ↓\n850 equipos autónomos\n    ↓\n0 gerentes\n    ↓\nUnos 15 coaches\n    ↓\n45 personas en la oficina central</pre>'),
  (('      <li>40% menos horas de cuidado necesarias</li>', '<li>Mejor empleador de Holanda: 5 años</li>'),
   '      <li>Menos horas de cuidado por paciente: cerca de la mitad, según el estudio de KPMG (2015)</li>\n'
   '      <li>La hora de una enfermera cuesta más, pero el total resulta más barato: Ernst &amp; Young calculó hasta un 40 % menos (2009)</li>\n'
   '      <li>Gastos de administración cercanos al 8 %, contra un 25 % en el sector</li>\n'
   '      <li>Las mejores calificaciones de pacientes y de enfermeras</li>'),
  Q('<blockquote>Premio Ernst &amp; Young: "Modelo más innovador de cuidado de salud global"</blockquote>'),
  (('    <h4>Expansión Global</h4>', 'las enfermeras saben cuidar mejor que cualquier manager."</blockquote>'),
   '    <h4>Más Allá de los Países Bajos</h4>\n'
   '    <p>Hay equipos inspirados en Buurtzorg en Japón, Estados Unidos, Suecia y el Reino Unido, entre otros países. Lo difícil, contó quien lo siguió '
   'de cerca, no fue que las enfermeras trabajaran solas, sino cambiar los sistemas que debían sostenerlas.</p>\n'
   '    <p>Cuando un diario presentó como algo malo que Buurtzorg diera menos horas de cuidado, Jos de Blok respondió que los pacientes no esperan '
   'horas: esperan soluciones.</p>'),
  ('<p><strong>Check-in (15 min)</strong></p>', '<p><strong>Ronda de llegada (15 min)</strong></p>'),
  ('<li>Solo hechos</li>\n      <li>Sin advocación</li>', '<li>Solo hechos</li>\n      <li>Sin abogar por ninguna opción</li>'),
  ('<p><strong>Check-out (5 min)</strong></p>', '<p><strong>Ronda de salida (5 min)</strong></p>'),
  ('<li>Shadow del rol actual</li>', '<li>Acompañar como sombra a quien hoy tiene el rol</li>'),
  ('<h3>Los Desafíos Reales de la Holocracia</h3>', '<h3>Los Desafíos Reales de la Holacracia</h3>'),
  ('<p>El secreto: No puedes instalar holocracia como un software.', '<p>El secreto: No puedes instalar la holacracia como un software.'),
  ('<h2>Reflexión Cuántica Final</h2>', '<h2>Reflexión Final</h2>'),
 ],
 puertas=[portal('Que bastan unos pocos que saben adónde ir, sin que nadie los reconozca como jefes, para que un grupo entero encuentre el '
                 'camino —en los cardúmenes y en un salón de una universidad inglesa—, se despliega en <em>Los muchos</em>, Libro 35 del Portal '
                 'Público, Umbral II: «Orientar sin mandar».', '35_Los_Muchos/umbral-02.html')],
)


# ---------------------------------------------------------------- Nodo 3
# La coherencia del corazón, con lo que se midió (Vickhoff, Konvalinka, Wiltermuth y Heath, Hatfield,
# Bernardi, el Proyecto Aristóteles, Edmondson, Woolley); sin HeartMath ni sus cifras. La IA no lee cuerpos ni
# caras (Barrett, 2019; el Reglamento europeo): el tablero queda como imaginado, con lo que cada uno elige
# contar. Aetna, Automattic y Sounds True, con lo que consta. La crítica (Purser) y el trauma (Treleaven).
R['nodo_03.html'] = dict(reemplazos=[
  ('su poder no es diez - es cien.', 'su poder no es diez: es cien.'),
  ('<p class="lead">El Instituto HeartMath ha demostrado que el campo electromagnético del corazón es 60 veces más potente que el del cerebro. Cuando',
   '<p class="lead">Cuando un coro canta, los corazones de quienes cantan se aceleran y se frenan juntos: lo midió Björn Vickhoff en 2013, en Gotemburgo, '
   'con estudiantes que entonaban un himno. Y en un pueblo de Soria, el equipo de Ivana Konvalinka vio (2011) que el corazón de quienes cruzaban las brasas '
   'en la noche de San Juan latía a la par del de sus allegados, que solo miraban. Cuando'),
  ('<li>HRV (Heart Rate Variability): Variabilidad del ritmo cardíaco</li>', '<li>Variabilidad del ritmo cardíaco: cuánto cambia el intervalo entre un latido y otro</li>'),
  ('<li>Coherencia individual: 0.0 (caos) a 1.0 (coherencia perfecta)</li>', '<li>Coherencia individual: un pulso que sube y baja con la respiración, parejo como una ola</li>'),
  ('<li>Coherencia grupal: Sincronización entre miembros</li>', '<li>Coherencia grupal: corazones y respiraciones que se acompasan entre los miembros</li>'),
  ('      <li>Amplitud del campo: Radio de influencia medible</li>\n', ''),
  ('<blockquote>Descubrimiento revolucionario: Cuando un grupo alcanza coherencia &gt;0.7, las decisiones mejoran 300%, los conflictos disminuyen 80%, y la creatividad aumenta 250%.</blockquote>',
   '<p>Y la sincronía une. En 2009, Scott Wiltermuth y Chip Heath, en Stanford, pidieron a unos grupos que caminaran al mismo paso o cantaran juntos antes '
   'de un juego económico: después cooperaron más que quienes habían hecho lo mismo sin acompasarse.</p>'),
  (('<pre>Centro: Líder coherente (0.8+)', 'Periferia: Resistentes (eventualmente sincronizados)</pre>'),
   '<pre>Centro: Líder coherente\n    ↓ (contagio)\nPrimer anillo: Quienes se suman primero\n    ↓ (contagio)\nSegundo anillo: La mayoría\n'
   '    ↓ (arrastre)\nPeriferia: Quienes prefieren quedarse afuera, y están en su derecho</pre>'),
  ('<blockquote>Fenómeno documentado: "Una sola persona en coherencia profunda puede elevar a todo un equipo. Es contagioso como la risa, pero más profundo."</blockquote>',
   '<p>En 1994, Elaine Hatfield, John Cacioppo y Richard Rapson llamaron contagio emocional a esa transmisión: imitamos sin darnos cuenta los gestos, la voz y '
   'la postura de los demás, y con ellos nos llega lo que sienten. Una sola persona serena puede serenar una sala.</p>'),
  ('<li>Manos en corazón</li>', '<li>Manos en el corazón, si se quiere</li>'),
  ('<li>Sentir expansión con cada respiración</li>\n    </ul>\n',
   '<li>Sentir expansión con cada respiración</li>\n    </ul>\n'
   '    <p>Ese ritmo, de unas seis respiraciones por minuto, no lo inventó ninguna empresa. En 2001, Luciano Bernardi y su equipo, en Pavía, vieron que rezar '
   'el rosario en latín o recitar un mantra de yoga lleva la respiración justamente ahí, y que con ella el corazón y la presión se acompasan.</p>\n'),
  ('<p><strong>Minuto 3-5: Activación de apreciación</strong></p>', '<p><strong>Minuto 3-5: Apreciación</strong></p>'),
  (('    <h4>Resultados Medidos</h4>', 'Ahorramos horas de discusión improductiva."</blockquote>'),
   '    <h4>Lo Que Se Midió de Verdad</h4>\n'
   '    <p>En 2012, Google estudió 180 de sus equipos para entender por qué unos funcionaban y otros no, en lo que llamó Proyecto Aristóteles. Pesaba menos '
   'quiénes estaban que la manera en que se trataban, y sobre todo la seguridad psicológica que Amy Edmondson venía estudiando desde los noventa: poder '
   'hablar, preguntar o equivocarse sin miedo. En 2010, Anita Woolley y sus colegas habían encontrado que los grupos tienen algo parecido a una inteligencia '
   'propia, y que la explicaban menos el talento del miembro más brillante que la sensibilidad de todos para leer a los otros y el reparto de los turnos '
   'para hablar.</p>\n'
   '    <p>Seis minutos de respiración compartida preparan ese terreno: cada uno llega, se calma y empieza a escuchar.</p>'),
  ('<h3>No Mindfulness Light - Práctica Profunda Colectiva</h3>', '<h3>No una Atención Plena Ligera: Práctica Profunda Colectiva</h3>'),
  ('<p>La meditación corporativa no es una app de 5 minutos. Es una práctica transformadora que rewirea el cerebro colectivo de la organización.</p>',
   '<p>La meditación corporativa no es una aplicación de 5 minutos. Es una práctica transformadora que va cambiando, de a poco, los hábitos de atención de toda la organización.</p>\n'
   '    <p>Su camino hacia el trabajo empezó en un hospital. En 1979, Jon Kabat-Zinn abrió en la Facultad de Medicina de la Universidad de Massachusetts un '
   'programa de ocho semanas de reducción del estrés basada en la atención plena, para pacientes con dolor crónico a los que la medicina ya no sabía qué '
   'ofrecer. De allí salió casi todo lo que hoy se enseña en las empresas.</p>'),
  ('<li>15 minutos diarios a las 8:45 AM</li>', '<li>15 minutos diarios, a primera hora</li>'),
  ('<li>Opcional pero encourageado</li>', '<li>De verdad opcional: nadie anota quién vino</li>'),
  ('      <li>Trackeo de asistencia sin presión</li>\n', ''),
  ('<li>Semanas 5-8: Body scan</li>', '<li>Semanas 5-8: Recorrido atento del cuerpo</li>'),
  ('<li>"No tengo tiempo" → "15 min te ahorran 2 horas"</li>', '<li>"No tengo tiempo" → "Empieza por tres minutos; y si tampoco hay, está bien"</li>'),
  ('<li>"No es para mí" → "Prueba 1 semana"</li>', '<li>"No es para mí" → "Prueba una semana; y si no, no pasa nada"</li>'),
  ('<li>"Es religioso" → "Es neurociencia"</li>', '<li>"Choca con mi fe" → "Se respeta: la atención plena se enseña sin creencias, y ese tiempo también sirve para rezar a tu manera"</li>'),
  ('<blockquote>Caso transformador: Google: \'Search Inside Yourself\' - 5000+ empleados entrenados, reducción 50% en burnout, aumento 32% en liderazgo efectivo.</blockquote>',
   '<p>En 2007, Chade-Meng Tan, un ingeniero de Google, armó con un grupo de maestros de meditación y científicos, entre ellos Daniel Goleman, un curso '
   'de atención plena e inteligencia emocional para sus compañeros. Lo llamó <em>Search Inside Yourself</em>, «Busca dentro de ti». En 2012 se volvió un '
   'instituto independiente, que lo lleva a otras organizaciones.</p>'),
  ('<li>Pausas mindful institucionalizadas</li>', '<li>Pausas de atención plena en la rutina</li>'),
  ('<li>Walking meetings meditativos</li>', '<li>Reuniones caminando, en silencio atento</li>'),
  ('<li>Retiros trimestrales</li>\n      <li>Cultura de presencia</li>', '<li>Retiros trimestrales, para quien quiera</li>\n      <li>Cultura de presencia</li>'),
  (('<h3>Resultados Documentados: Aetna Insurance</h3>', 'Es la intervención de productividad más hardcore que existe."</blockquote>'),
   '<h3>Un Caso Real: Aetna</h3>\n'
   '    <h4>El Director Que Llevó el Yoga a una Aseguradora</h4>\n'
   '    <p><strong>2004: Mark Bertolini, entonces ejecutivo de Aetna, se quiebra el cuello esquiando</strong></p>\n'
   '    <ul>\n'
   '      <li>Le queda un dolor que los analgésicos no calman</li>\n'
   '      <li>Encuentra alivio en el yoga y la meditación</li>\n'
   '      <li>En 2010 llega a dirigir la empresa</li>\n'
   '    </ul>\n'
   '    <p><strong>Implementación:</strong></p>\n'
   '    <ul>\n'
   '      <li>Clases gratuitas y voluntarias de yoga y de atención plena</li>\n'
   '      <li>Un estudio con la Universidad Duke para saber si servían (2012)</li>\n'
   '      <li>Más de una cuarta parte de sus cincuenta mil empleados tomó al menos una clase</li>\n'
   '      <li>Líderes modelando práctica</li>\n'
   '    </ul>\n'
   '    <p><strong>Lo que reportaron quienes participaron:</strong></p>\n'
   '    <ul>\n'
   '      <li>Estrés: 28 % menos</li>\n'
   '      <li>Calidad del sueño: 20 % mejor</li>\n'
   '      <li>Dolor: 19 % menos</li>\n'
   '      <li>Unos 62 minutos más de trabajo eficaz por semana, que Aetna calculó en unos 3.000 dólares por persona al año</li>\n'
   '    </ul>\n'
   '    <p>Lo contó David Gelles en <em>The New York Times</em> (2015).</p>'),
  (('<h3>Sistema RESONANCE: IA de Coherencia</h3>', '<li>Derecho a desconexión</li>\n    </ul>'),
   '<h3>Lo Que la IA No Debe Leer</h3>\n'
   '    <p>Hubo un tiempo en que se prometieron sistemas capaces de leer en las caras, las voces y los pulsos de un equipo cuánta coherencia había en una '
   'reunión. La ciencia los desmintió primero: en 2019, Lisa Feldman Barrett y un grupo de colegas revisaron más de mil estudios y concluyeron que un gesto '
   'no revela con certeza lo que alguien siente: se frunce el ceño por enojo, por concentración o por un dolor de cabeza. Y la ley los siguió: desde 2025, '
   'el Reglamento europeo de inteligencia artificial prohíbe usar sistemas que infieran las emociones de las personas en el trabajo y en la escuela, salvo '
   'por razones médicas o de seguridad.</p>\n'
   '    <p>Lo que un cuerpo siente le pertenece a ese cuerpo. La IA que sirve a la coherencia trabaja con lo que el grupo dice y elige compartir, nunca con lo que se le extrae.</p>\n'
   '\n'
   '    <h4>Privacidad y Ética</h4>\n'
   '    <p><strong>Principios no negociables:</strong></p>\n'
   '    <ul>\n'
   '      <li>Ningún dato del cuerpo ni de la cara de nadie</li>\n'
   '      <li>Participación voluntaria siempre, y salida sin explicaciones</li>\n'
   '      <li>Transparencia total sobre qué se usa y para qué</li>\n'
   '      <li>Lo que cada uno aporta le sigue perteneciendo</li>\n'
   '      <li>Derecho a la desconexión</li>\n'
   '      <li>Nada de lo que se comparte sirve para evaluar a una persona</li>\n'
   '    </ul>'),
  Q('<blockquote>Caso de uso: "Nuestro equipo de diseño usa IA para amplificar brainstorming. No reemplaza nuestra creatividad - la multiplica por 10."</blockquote>'),
  (('<h4>Predicción de Dinámicas Grupales</h4>', 'Conflictos reales: -70%."</blockquote>'),
   '<h4>Escuchar Antes de Predecir</h4>\n'
   '    <p>Una IA puede ayudar a un equipo a verse: ordenar lo que se dijo en las rondas, mostrar qué temas vuelven, recordar qué se decidió y qué quedó '
   'pendiente. Lo que no le corresponde es adivinar quién va a pelearse con quién o quién está por agotarse: esa pregunta se hace en persona, y en persona se responde.</p>\n'
   '    <p><strong>Si el equipo lo pide, la IA puede ayudar a ver:</strong></p>\n'
   '    <ul>\n'
   '      <li>Qué temas vuelven una y otra vez a las reuniones</li>\n'
   '      <li>Qué decisiones quedaron sin cerrar</li>\n'
   '      <li>Qué voces se oyeron poco, para invitarlas y no para señalarlas</li>\n'
   '      <li>Qué momentos del año suelen pesar más</li>\n'
   '    </ul>'),
  ('El biofeedback organizacional hace exactamente eso.</p>',
   'El biofeedback organizacional se propone algo parecido, con una condición: que cada persona decida qué cuenta de sí.</p>'),
  ('<h3>Dashboard de Vitalidad Organizacional</h3>', '<h3>Tablero de Vitalidad Organizacional</h3>'),
  ('<p><strong>Panel en tiempo real:</strong></p>', '<p><strong>Un tablero imaginado, hecho solo con lo que cada uno elige contar:</strong></p>'),
  ('║ ⚠️ Alerta: Equipo Ventas bajo coherencia║\n', ''),
  ('║ ✨ Destacado: I+D en flow creativo      ║', '║ ✨ Destacado: I+D en flujo creativo     ║'),
  (('    <h4>Sensores Distribuidos</h4>', '<p>Integración holística: Todos los datos crean una imagen viva del organismo organizacional.</p>'),
   '    <h4>Fuentes Elegidas</h4>\n'
   '    <p><strong>De dónde sale lo que se ve:</strong></p>\n'
   '    <ul>\n'
   '      <li>Encuestas breves y anónimas, que se responden si se quiere</li>\n'
   '      <li>Lo que cada equipo cuenta en sus rondas</li>\n'
   '      <li>Pedidos y propuestas que llegan por escrito</li>\n'
   '      <li>El ambiente de los espacios (ruido, luz, temperatura)</li>\n'
   '    </ul>\n'
   '    <p>Integración holística: lo que cada uno elige contar crea una imagen viva del organismo organizacional. Nadie lleva sensores, nadie es leído '
   'en secreto, y nada de esto sirve para evaluar a una persona.</p>'),
  ('<h3>Intervenciones Basadas en Data</h3>', '<h3>Intervenciones Basadas en Datos</h3>'),
  (('<p><strong>Cuando coherencia &lt;50%:</strong></p>', 'enfermedades -40%."</blockquote>'),
   '<p><strong>Cuando el equipo lo pide:</strong></p>\n'
   '    <ul>\n'
   '      <li>Una invitación suave en las pantallas</li>\n'
   '      <li>Respiración de 3 minutos</li>\n'
   '      <li>Guía visual/auditiva sincronizada</li>\n'
   '      <li>Quien no quiere, sigue con lo suyo</li>\n'
   '    </ul>'),
  ('<li>Mejor momento para reunión (energía alta)</li>', '<li>Mejor momento para reunirse, según lo que el equipo cuenta de sus días</li>'),
  ('<li>Participantes óptimos (coherencia entre ellos)</li>', '<li>Participantes necesarios, y nadie de más</li>'),
  ('<li>Breaks necesarios (caída de atención)</li>', '<li>Pausas necesarias, antes de que caiga la atención</li>'),
  Q('<blockquote>Testimonio: "La IA nos dijo que nuestras reuniones de los lunes a las 9 AM eran las peores. Las movimos a martes 10 AM. Game changer."</blockquote>'),
  ('equipos globales pueden alcanzar coherencia mayor que equipos presenciales.</p>', 'equipos globales pueden alcanzar una coherencia tan honda como la de los equipos presenciales.</p>'),
  ('      <li>Biométricos compartibles (opcional)</li>\n', ''),
  ('<p><strong>8:00 AM (cada zona horaria)</strong></p>', '<p><strong>A primera hora, en cada zona horaria</strong></p>'),
  ('<p><strong>Check-in energético (3 min)</strong></p>', '<p><strong>Ronda de llegada (3 min)</strong></p>'),
  ('<li>Cámara on</li>', '<li>Cámara encendida, si se quiere</li>'),
  ('<li>Compartir número 1-10</li>', '<li>Compartir un número del 1 al 10, o pasar</li>'),
  ('<li>Coherencia medible vía app</li>', '<li>Sin medir a nadie</li>'),
  (('<p><strong>1,300 empleados, 77 países, 0 oficinas:</strong></p>', '<blockquote>Matt Mullenweg (CEO): "La distancia física es irrelevante cuando hay coherencia de propósito y práctica."</blockquote>'),
   '<p>Automattic, la empresa detrás de WordPress.com, trabaja de manera distribuida desde que nació, en 2005: sus personas viven en decenas de países y '
   'casi nunca coinciden en un mismo lugar.</p>\n'
   '    <p><strong>Prácticas de coherencia:</strong></p>\n'
   '    <ul>\n'
   '      <li>Un gran encuentro anual, en persona</li>\n'
   '      <li>Encuentros más pequeños de cada equipo</li>\n'
   '      <li>Tres meses de licencia sabática pagada cada cinco años</li>\n'
   '      <li>Comunicación asincrónica y por escrito, que deja tiempo para pensar</li>\n'
   '      <li>Cultura de presencia sobre presencialismo</li>\n'
   '    </ul>'),
  ('<h3>La Editorial Que Medita Antes de Cada Decisión</h3>', '<h3>La Editorial Que Hace Silencio Antes de Hablar</h3>'),
  ('<p>Tami Simon funda Sounds True en 1985.</p>',
   '<p>Tami Simon funda Sounds True en 1985, en Colorado, a los 22 años, con una herencia y unas grabaciones de conferencias de Ram Dass y Stephen Levine.</p>'),
  (('<p><strong>Tecnologías de coherencia implementadas:</strong></p>', '<blockquote>Tami Simon: "Cada decisión de negocio es una práctica espiritual. La coherencia no es una herramienta - es nuestra forma de ser."</blockquote>'),
   '<p><strong>Tecnologías de coherencia que la revista <em>Workforce</em> encontró en 2001:</strong></p>\n'
   '\n'
   '    <p><strong>1. La Campana</strong></p>\n'
   '    <ul>\n'
   '      <li>Cada día, a las 11, una campana de bronce suena tres veces</li>\n'
   '      <li>Quien quiere, se suma a una meditación o a quince minutos de silencio</li>\n'
   '      <li>Una sala de meditación siempre abierta</li>\n'
   '    </ul>\n'
   '\n'
   '    <p><strong>2. Silencio Antes de Hablar</strong></p>\n'
   '    <ul>\n'
   '      <li>Las reuniones grandes empiezan con dos minutos de silencio</li>\n'
   '      <li>Arribar completamente</li>\n'
   '    </ul>\n'
   '\n'
   '    <p><strong>3. Preguntas Abiertas</strong></p>\n'
   '    <ul>\n'
   '      <li>Cada lunes, cualquiera puede preguntarle a cualquier responsable, también a la presidenta, por el presupuesto o las contrataciones</li>\n'
   '      <li>Las cuentas, a la vista de todos</li>\n'
   '      <li>Los equipos evalúan a sus responsables</li>\n'
   '    </ul>\n'
   '\n'
   '    <p><strong>4. La Vida Entra a la Oficina</strong></p>\n'
   '    <ul>\n'
   '      <li>Horarios flexibles</li>\n'
   '      <li>Sin código de vestimenta</li>\n'
   '      <li>Los animales son bienvenidos, y los perros acompañan el trabajo</li>\n'
   '    </ul>\n'
   '\n'
   '    <h4>Los Resultados</h4>\n'
   '    <p><strong>Décadas después:</strong></p>\n'
   '    <ul>\n'
   '      <li>Una de las editoriales de sabiduría espiritual más conocidas del mundo</li>\n'
   '      <li>Audios, libros y cursos de maestros de muchas tradiciones</li>\n'
   '      <li>Propósito intacto</li>\n'
   '    </ul>\n'
   '    <p>Lo que Tami Simon aprendió en el camino lo contó en <em>Being True</em>, un libro sobre lo que importa en el trabajo, en la vida y en el amor.</p>'),
  (('<p><strong>Presupuesto &lt;$1000:</strong></p>', '<li>IA personalizada</li>\n    </ul>'),
   '<p>Para empezar alcanza con muy poco: una campana o un cuenco, algunos cojines, un temporizador, un rincón tranquilo y alguien que se ofrezca a guiar. '
   'Ningún sensor, ningún programa: lo esencial es gratis.</p>'),
  ('<li>Medir baseline de métricas</li>', '<li>Tomar un punto de partida con encuestas voluntarias</li>'),
  ('<li>Identificar early adopters</li>', '<li>Encontrar a quienes se suman primero</li>'),
  ('<li>Celebrar pequeños wins</li>', '<li>Celebrar los pequeños logros</li>'),
  ('<li>Coherencia como práctica standard</li>', '<li>La coherencia como práctica habitual</li>'),
  ('<li>Métricas en dashboards</li>', '<li>Lo que el equipo elige compartir, a la vista de todos</li>'),
  ('<li>Ajustes basados en feedback</li>', '<li>Ajustes basados en lo que cada uno cuenta</li>'),
  ('      <li>Coherencia promedio (HRV)</li>\n', ''),
  (('<p><strong>Fórmula de ROI:</strong></p>', '<p><strong>Donde Beneficios incluyen:</strong></p>'),
   '<p><strong>El retorno:</strong> se compara lo que se invirtió con lo que se ganó en tiempo, en permanencia y en salud.</p>\n'
   '\n'
   '    <p><strong>Lo ganado incluye:</strong></p>'),
  ('<li>Bypass de conflictos necesarios</li>', '<li>Atajo para esquivar conflictos necesarios</li>'),
  ('<li>Métricas como KPIs punitivos</li>', '<li>Métricas usadas para castigar</li>'),
  ('<li>Trauma previo con "mindfulness corporativo"</li>', '<li>Una herida previa con la «atención plena corporativa»</li>'),
  ('<li>Timing inadecuado</li>', '<li>Un momento inadecuado</li>'),
  ('<li>Respetar opt-out</li>', '<li>Respetar a quien prefiere no participar</li>'),
  ('<li>Demostrar por resultados</li>\n      <li>Paciencia infinita</li>\n    </ul>\n',
   '<li>Mostrar con resultados</li>\n      <li>Paciencia infinita</li>\n    </ul>\n'
   '    <p>La crítica más dura vino de adentro. En 2019, Ronald Purser, profesor de gestión y maestro budista, llamó <em>McMindfulness</em> a la meditación '
   'vendida a las empresas como una técnica para que cada uno aguante mejor lo que no debería aguantar: el estrés se vuelve un problema privado y nadie mira '
   'lo que lo causa. La coherencia verdadera empieza por la otra punta: por lo que la organización cambia.</p>\n'
   '    <p>Y la quietud no le hace bien a todos de la misma manera. En 2018, David Treleaven mostró en <em>Trauma-Sensitive Mindfulness</em> que, para quien '
   'vivió un trauma, cerrar los ojos y mirar hacia adentro puede despertar el recuerdo en lugar de calmarlo. Por eso, en cada una de estas prácticas los ojos '
   'pueden quedar abiertos, la atención puede posarse afuera y cualquiera puede parar. Si alguna vez sentiste que no eras real o que te ibas de tu cuerpo, '
   'hazlas con los ojos abiertos y los pies en el suelo, o déjalas para otro momento.</p>\n'),
  ('<h2>Meditación de Campo Unificado</h2>', '<h2>Meditación del Campo Compartido</h2>'),
  ('<h2>Reflexión Cuántica Final</h2>', '<h2>Reflexión Final</h2>'),
  ('no son lujos new age - son necesidades evolutivas.', 'no son lujos pasajeros: son necesidades evolutivas.'),
  ('<p>La paradoja: Mientras más tecnología usamos para medirnos, más humanos nos volvemos.</p>',
   '<p>La paradoja: la tecnología que mejor nos sirve es la que, en vez de medirnos, nos ayuda a escucharnos.</p>'),
 ],
 puertas=[portal('Que el corazón de quien cruza las brasas en la noche de San Juan arrastra el de los suyos, aunque solo estén mirando, y que un coro '
                 'respira hasta latir junto, se despliega en <em>Los muchos</em>, Libro 35 del Portal Público, Umbral III: «La noche de San Juan».',
                 '35_Los_Muchos/umbral-03.html')],
)


# ---------------------------------------------------------------- Nodo 4
# La física queda como imagen, y corregida. Las preguntas tienen linaje (Rilke, Cooperrider, Schein); Interface
# toma el lugar de Starbucks (su historia sigue en el Nodo 7). Fritz y Senge; Lao Tse; Scharmer. La retención
# del aire es opcional y la tensión que dura días se habla. La meditación del vacío, con los ojos que pueden
# quedar abiertos y la frase que protege. Robertson, sin cifras ni frases puestas en su boca.
R['nodo_04.html'] = dict(reemplazos=[
  ('<p class="lead">El vacío del que hablamos no es emptiness nihilista. Es el vacuum cuántico de la física: aparentemente vacío pero hirviendo con potencial infinito, donde partículas virtuales danzan constantemente entre existencia y no-existencia.</p>',
   '<p class="lead">El vacío del que hablamos no es la nada del nihilismo. Se parece más a la imagen que ofrece la física: el vacío cuántico, que parece '
   'desierto y sin embargo fluctúa sin cesar, nunca del todo quieto. Un espacio aparentemente vacío y lleno de posibilidad.</p>'),
  ('<h3>Física Cuántica del Liderazgo Vacío</h3>', '<h3>La Física como Imagen del Liderazgo Vacío</h3>'),
  ('<h4>El Campo de Punto Cero Organizacional</h4>', '<h4>El Punto Cero Organizacional</h4>'),
  ('<li>El vacío contiene energía infinita</li>', '<li>El vacío nunca está del todo quieto</li>'),
  ('<li>Todas las posibilidades coexisten</li>', '<li>Un sistema puede estar en varios estados a la vez</li>'),
  ('<li>La observación colapsa potencial en realidad</li>', '<li>La medición define un resultado entre varios posibles</li>'),
  ('<li>El observador afecta lo observado</li>', '<li>Medir es intervenir en lo que se mide</li>'),
  ('<p><strong>En liderazgo cuántico:</strong></p>', '<p><strong>En liderazgo, como imagen:</strong></p>'),
  ('<li>El no-saber contiene todas las soluciones</li>', '<li>El no-saber deja lugar a soluciones que nadie traía</li>'),
  ('<li>La pregunta correcta colapsa la respuesta</li>', '<li>La pregunta que se hace orienta la respuesta que llega</li>'),
  Q('<blockquote>Testimonio de físico-CEO: "Cuando dejé de aplicar mecánica newtoniana a mi empresa y empecé a liderar cuánticamente, todo cambió. Ahora sostengo el campo de posibilidad y dejo que las soluciones emerjan."</blockquote>'),
  ('<p>En física: No puedes conocer simultáneamente posición y momentum. En liderazgo: No puedes controlar dirección y permitir innovación.</p>',
   '<p>En física, no se pueden conocer a la vez, con precisión total, la posición y el momento de una partícula. En liderazgo, como imagen: cuanto más se controla la dirección, menos lugar le queda a la innovación.</p>'),
  Q('<blockquote>Aplicación revolucionaria: "Dejé de dar respuestas y empecé a hacer preguntas. Mi equipo encontró soluciones que yo jamás hubiera imaginado."</blockquote>'),
  ('<p>Una pregunta poderosa es un vórtice que succiona respuestas del campo cuántico. No busca confirmar lo que sabemos - invita lo que no sabemos que sabemos.</p>',
   '<p>Una pregunta poderosa es un vórtice que atrae respuestas del campo de posibilidad. No busca confirmar lo que sabemos: invita lo que no sabemos que sabemos.</p>\n'
   '    <p>Las preguntas tienen linaje. En 1903, Rainer Maria Rilke le aconsejó a un joven poeta tener paciencia con lo que no estaba resuelto en su corazón '
   'y amar las preguntas mismas, vivirlas, hasta entrar un día en la respuesta casi sin notarlo. En 1987, David Cooperrider y Suresh Srivastva propusieron '
   'la indagación apreciativa: una organización crece en la dirección de lo que se pregunta. Y en 2013, Edgar Schein llamó indagación humilde al arte de '
   'preguntar en lugar de decir.</p>'),
  ('<h3>Anatomía de una Pregunta Cuántica</h3>', '<h3>Anatomía de una Pregunta Abierta</h3>'),
  ('<p><strong>Pregunta Tradicional → Pregunta Cuántica:</strong></p>', '<p><strong>Pregunta Tradicional → Pregunta Abierta:</strong></p>'),
  (('<h3>Caso: La Pregunta de $1 Billón de Howard Schultz</h3>', 'No necesitaba respuestas - necesitaba una mejor pregunta."</blockquote>'),
   '<h3>Caso: La Pregunta que Interface No Supo Responder</h3>\n'
   '    <p><strong>1994, una pregunta incómoda:</strong></p>\n'
   '    <p>Algunos clientes empezaron a preguntarle a Interface, una gran fabricante de alfombras de Georgia, qué hacía por el ambiente. Cuando invitaron a '
   'Ray Anderson, su fundador, a hablar de la visión ambiental de la empresa, descubrió que no tenía ninguna.</p>\n'
   '    <p><strong>Pregunta tradicional (que no hizo):</strong> "¿Cómo cumplimos con la ley sin gastar de más?"</p>\n'
   '    <p><strong>Pregunta que transformó todo:</strong> "¿Cómo sería una empresa que no le quita a la Tierra nada que la Tierra no pueda reponer?"</p>\n'
   '    <p><strong>Resultado:</strong></p>\n'
   '    <ul>\n'
   '      <li>Anderson leyó <em>La ecología del comercio</em>, de Paul Hawken, y lo sintió, contó después, como una lanza en el pecho</li>\n'
   '      <li>Se propuso que la empresa dejara de dañar el planeta</li>\n'
   '      <li>Reconexión con el propósito</li>\n'
   '      <li>Innovación desde el alma, que se cuenta en el <a href="nodo_07.html">Nodo 7</a></li>\n'
   '    </ul>'),
  ('<li>Profit Y Propósito</li>', '<li>Ganancia Y Propósito</li>'),
  ('<p>No resuelve la tensión - la sostiene hasta que algo nuevo emerge.</p>', '<p>No resuelve la tensión: la sostiene hasta que algo nuevo emerge.</p>'),
  ('Opción 2: Negar la realidad (delusión)', 'Opción 2: Negar la realidad (negación)'),
  ('<p>El vacío elige opción 3.</p>',
   '<p>El vacío elige opción 3.</p>\n'
   '    <p>Robert Fritz describió esa tensión en <em>El camino de la menor resistencia</em> (1984), y Peter Senge la volvió una disciplina del aprendizaje '
   'en las organizaciones en <em>La quinta disciplina</em> (1990): la distancia entre la visión y la realidad no es un problema, es una fuente de energía.</p>'),
  ('<p><strong>Cuando la tensión es insoportable:</strong></p>', '<p><strong>Cuando la tensión aprieta:</strong></p>'),
  ('<li>Sostener la tensión (7 seg)</li>', '<li>Sostener la tensión (7 seg), si es cómodo; si no, se pasa directo a exhalar</li>'),
  ('<li>Sostener el vacío (4 seg)</li>', '<li>Sostener el vacío (4 seg), también si es cómodo</li>'),
  ('<p>Efecto: Expande capacidad de contener paradojas.</p>',
   '<p>Efecto: Expande capacidad de contener paradojas.</p>\n'
   '    <p>Cuando la tensión dura días, quita el sueño o ya no deja pensar, no es tensión creativa: es momento de hablarlo con alguien y, si hace falta, de consultar.</p>'),
  Q('<blockquote>Resultado típico: "Las soluciones emergen días después, siempre mejores que lo que hubiéramos decidido en la reunión."</blockquote>'),
  ('<h4>Práctica 3: La Pausa Cuántica Ejecutiva</h4>', '<h4>Práctica 3: La Pausa Ejecutiva</h4>'),
  Q('<blockquote>Testimonio CEO: "La Pausa Cuántica me ha ahorrado millones. Las decisiones que emergen del vacío son siempre superiores a las que vienen de la mente."</blockquote>'),
  ('es el salto cuántico que ocurre cuando el grupo trasciende sus partes.</p>', 'es el salto que ocurre cuando el grupo trasciende sus partes.</p>'),
  ('<li>Authenticidad recompensada</li>', '<li>Autenticidad recompensada</li>'),
  ('<li>Confiar en el timing</li>', '<li>Confiar en los tiempos</li>'),
  ('<li>Desaparecer cuando emerge</li>\n    </ul>\n',
   '<li>Desaparecer cuando emerge</li>\n    </ul>\n'
   '    <p>Lao Tse lo dijo hace más de dos mil años: del mejor gobernante, la gente apenas sabe que existe, y cuando la obra está hecha, todos dicen '
   '«lo hicimos nosotros» (<em>Tao Te Ching</em>, 17).</p>\n'),
  ('<h3>Caso: Teoría U del MIT</h3>', '<h3>Caso: La Teoría U</h3>'),
  ('<p>Otto Scharmer documenta el proceso:</p>', '<p>Otto Scharmer, del MIT, la describió en <em>Teoría U</em> (2007):</p>'),
  ('   VACÍO/PRESENCING', '   VACÍO / <em>PRESENCING</em>'),
  ('Suspender - Soltar certezas', 'Suspender - Poner en pausa las certezas'),
  ('Letting Go - Morir al viejo ser', 'Soltar - Despedir al viejo ser'),
  ('Presencing - Tocar el vacío', '<em>Presencing</em> - Tocar el vacío'),
  ('Letting Come - Permitir emergencia', 'Dejar venir - Permitir emergencia'),
  ('<blockquote>Aplicación en 1000+ organizaciones: "El punto más profundo del U - el vacío - es donde ocurre toda la magia. Es aterrador y transformador."</blockquote>',
   '<p>La palabra <em>presencing</em> la inventó Scharmer uniendo presencia y percepción: sentir, desde el fondo de la U, lo que el futuro está pidiendo.</p>'),
  ('<p><strong>Reacciones documentadas:</strong></p>', '<p><strong>Reacciones frecuentes:</strong></p>'),
  ('<li>Intención: vaciarse para llenarse</li>\n    </ul>\n',
   '<li>Intención: vaciarse para llenarse</li>\n    </ul>\n'
   '    <p>' + OJOS + '</p>\n'),
  ('<li>No engagement</li>', '<li>Sin engancharse</li>'),
  ('<li>Perdonar todo</li>', '<li>Perdonar lo que puedas hoy</li>'),
  ('<li>Solo presencia</li>\n    </ul>\n\n    <p><strong>Minuto 20: Retorno</strong></p>',
   '<li>Solo presencia</li>\n    </ul>\n'
   '    <p>Si en el silencio aparece la sensación de no ser nadie o de no estar en ningún lugar, se abren los ojos, se apoyan los pies y se vuelve al cuarto. ' + ESTADO + '</p>\n'
   '\n    <p><strong>Minuto 20: Retorno</strong></p>'),
  ('<li>Menos reactividadreactividad</li>', '<li>Menos reactividad</li>'),
  ('<li>"Downloads" frecuentes</li>\n    </ul>\n', '<li>Ideas que llegan solas</li>\n    </ul>\n    <p>' + POEMA + '</p>\n'),
  ('<p>Question Circle semanal:</p>', '<p>Círculo de preguntas semanal:</p>'),
  Q('<blockquote>Resultado típico: "La solución siempre emerge, no de las preguntas sino del espacio entre ellas."</blockquote>'),
  Q('<blockquote>Success rate reportado: 87% encuentran solución superior a opciones originales.</blockquote>'),
  ('<h2>Caso Transformador: Brian Robertson y Holocracia</h2>', '<h2>Caso Transformador: Brian Robertson y la Holacracia</h2>'),
  ('<p><strong>2001: Brian Robertson, CEO de Ternary Software</strong></p>', '<p><strong>2001: Brian Robertson funda Ternary Software</strong></p>'),
  ('<blockquote>El momento de vacío: "Me di cuenta que yo era el problema. Mi necesidad de control, de saber, de dirigir. Decidí experimentar: ¿Qué pasaría si yo NO supiera? ¿Si el poder no viniera de mí sino del propósito mismo?"</blockquote>',
   '<p>Robertson notaba que muchas tensiones que la gente percibía no tenían por dónde ir, y que demasiadas terminaban en el escritorio del fundador. '
   'Decidió probar qué pasaba si la autoridad no venía de él, sino del propósito y de unas reglas que todos conocieran.</p>'),
  ('<p><strong>2001-2007: Desarrollo de Holocracia</strong></p>', '<p><strong>2001-2007: Desarrollo de la Holacracia</strong></p>'),
  ('<li>Elimina su propio rol de CEO</li>', '<li>Cede su autoridad de fundador</li>'),
  ('<li>Crea "constitución" organizacional</li>', '<li>Escribe una "constitución" organizacional</li>'),
  ('      <li>Productividad +300%</li>\n', '      <li>El laboratorio donde nació el método</li>\n'),
  ('      <li>Cero política organizacional</li>\n      <li>Vendida exitosamente</li>\n', ''),
  ('<p><strong>Holocracia global:</strong></p>', '<p><strong>La holacracia en el mundo:</strong></p>'),
  ('<li>1000+ organizaciones adoptadas</li>', '<li>Organizaciones de muchos países la adoptaron</li>'),
  ('<li>Libro bestseller</li>', '<li>Un libro, <em>Holacracia</em> (2015)</li>'),
  Q('<blockquote>Robertson hoy: "Mi mayor acto de liderazgo fue dejar de liderar. Mi mayor conocimiento fue admitir que no sabía. Mi mayor poder vino de renunciar al poder."</blockquote>'),
  ('<p><strong>Reframe mental:</strong></p>', '<p><strong>Cambio de mirada:</strong></p>'),
  ('<li>Check-ins frecuentes</li>', '<li>Encuentros breves y frecuentes</li>'),
  ('<li>Celebrar emergencias</li>', '<li>Celebrar lo que emerge</li>'),
  ('<li>Documentar insights</li>', '<li>Anotar lo que se comprende</li>'),
  ('<li>¿Qué expertise estorba?</li>', '<li>¿Qué pericia estorba?</li>'),
  ('<h2>Reflexión Cuántica Final</h2>', '<h2>Reflexión Final</h2>'),
  ('El vacío no está vacío - está embarazado', 'El vacío no está vacío: está embarazado'),
 ],
 puertas=[portal('Que en el teatro improvisado ningún actor tiene en la cabeza la obra entera, y que la escena aparece entre todos sin que nadie pueda '
                 'decir de quién fue, se despliega en <em>La emergencia</em>, Libro 37 del Portal Público, Umbral IV: «Sin director ni libreto».',
                 '37_La_Emergencia/umbral-04.html')],
)


# ---------------------------------------------------------------- Nodo 5
# La metáfora del cáncer pasa al monocultivo (decisión de Arturo): una enfermedad no se usa como insulto, y
# quien lee puede estar atravesándola. Cada pecado y cada principio, con su fuente (Pigou, Meadows, Kennedy,
# Oxfam, EPI, Kropotkin, Simard, Krenak, McDonough y Braungart, Mondragón, Bután, Volvo, Salk, B Lab,
# Chouinard, Raworth, Felber, Gesell, Wörgl, Scholz); las frases puestas en boca de Polman, Faber, Pauli,
# Fink, Mullenweg y de Blok pasan a lo que hicieron o escribieron. Sale Tesla.
R['nodo_05.html'] = dict(reemplazos=[
  ('<p class="node-quote">"La economía del futuro no medirá el PIB sino el FIB - Felicidad Interna Bruta.',
   '<p class="node-quote">"La economía del futuro no medirá el PIB sino la FNB, la Felicidad Nacional Bruta.'),
  ('<h3>Del Paradigma del Cáncer al Paradigma del Jardín</h3>', '<h3>Del Paradigma del Monocultivo al Paradigma del Jardín</h3>'),
  ('<p class="lead">El capitalismo extractivo opera como célula cancerosa: crecimiento infinito en un planeta finito, extrayendo valor hasta matar al huésped. La economía consciente opera como jardín: ciclos regenerativos donde cada elemento nutre al todo.</p>',
   '<p class="lead">El capitalismo extractivo opera como un monocultivo: una sola especie, sembrada hasta el horizonte, que exprime el suelo cosecha tras '
   'cosecha y necesita cada vez más insumos para rendir lo mismo, hasta dejar la tierra exhausta. La economía consciente opera como jardín: muchas especies, '
   'ciclos regenerativos, cada elemento nutriendo al todo.</p>'),
  ('<blockquote>Costo real oculto: Un iPhone de $1,000 costaría $15,000 si incluyera: daño ambiental de minería, salarios dignos en toda cadena, disposición responsable, salud de trabajadores y regeneración de recursos.</blockquote>',
   '<p>En 1920, el economista inglés Arthur Pigou describió estos costos que una empresa traslada a otros sin pagarlos, y propuso cobrarlos con impuestos. '
   'Hoy se llaman externalidades.</p>'),
  ('<h4>2. Crecimiento Canceroso</h4>', '<h4>2. Crecimiento sin Límite</h4>'),
  ('<li>GDP sube con desastres y enfermedades</li>', '<li>El PIB sube con desastres y enfermedades</li>'),
  ('<blockquote>Reflexión de célula cancerosa: "Nuestro trimestre fue excelente. Crecimos 40%. El huésped está muriendo pero eso es su problema."</blockquote>',
   '<p>En 1972, un equipo del MIT encabezado por Donella y Dennis Meadows publicó <em>Los límites del crecimiento</em>: con un modelo de computadora mostró '
   'que un crecimiento sin freno en un planeta finito termina por chocar con sus bordes.</p>'),
  ('<blockquote>Economista honesto: "Hemos creado un sistema donde destruir un bosque aumenta el GDP pero conservarlo no cuenta."</blockquote>',
   '<p>En 1968, Robert Kennedy dijo en la Universidad de Kansas que el producto bruto lo mide todo, menos aquello que hace que la vida valga la pena. '
   'Talar un bosque lo hace subir; conservarlo no cuenta.</p>'),
  ('<p>1% posee más que 99%.</p>', '<p>El 1 % posee más que el 99 % restante (Oxfam, 2016).</p>'),
  ('<li>8 personas = riqueza de 3.5 billones</li>', '<li>8 hombres = la misma riqueza que la mitad más pobre de la humanidad (Oxfam, 2017)</li>'),
  ('<li>CEO promedio gana 350x trabajador</li>', '<li>En las grandes empresas de Estados Unidos, el director gana más de 300 veces lo que un trabajador típico (Economic Policy Institute)</li>'),
  Q('<blockquote>Síntoma terminal: "Jeff Bezos gana por segundo lo que empleado de Amazon gana por año."</blockquote>'),
  ('<p>Quarterly earnings sobre supervivencia planetaria.</p>', '<p>Ganancias trimestrales sobre supervivencia planetaria.</p>'),
  ('<p><strong>Miopía suicida:</strong></p>', '<p><strong>Miopía que se devora a sí misma:</strong></p>'),
  ('<li>Stock price &gt; Stakeholder wellbeing</li>', '<li>Precio de la acción &gt; Bienestar de las partes interesadas</li>'),
  ('<li>Exit strategy &gt; Permanencia</li>', '<li>Estrategia de salida &gt; Permanencia</li>'),
  ('<li>ROI inmediato &gt; Regeneración</li>', '<li>Retorno inmediato &gt; Regeneración</li>'),
  Q('<blockquote>CEO anónimo: "Sé que esto destruirá la empresa en 10 años, pero mi bonus depende de este trimestre."</blockquote>'),
  ('<blockquote>Realidad natural: En la naturaleza, 90% es colaboración. Los árboles se nutren mutuamente bajo tierra. Solo los humanos creen que todo es competencia.</blockquote>',
   '<p>En 1902, Piotr Kropotkin, que había recorrido Siberia como naturalista, publicó <em>El apoyo mutuo</em>: en la naturaleza, la cooperación es tan '
   'decisiva para sobrevivir como la lucha. Y en 1997, Suzanne Simard mostró en <em>Nature</em> que los abedules y los abetos de un bosque canadiense '
   'intercambian carbono por las redes de hongos que unen sus raíces.</p>'),
  ('<li>Agua: commodity</li>', '<li>Agua: mercancía</li>'),
  ('<li>Enfermera menos que trader</li>', '<li>Enfermera menos que operador de bolsa</li>'),
  ('<blockquote>Indígena amazónico: "Me preguntan cuánto vale el bosque. Es como preguntar cuánto vale mi madre."</blockquote>',
   '<p>Ailton Krenak, líder del pueblo krenak, en Brasil, llama abuelo al río Doce, Watu, y en <em>Ideas para postergar el fin del mundo</em> (2019) se '
   'pregunta qué humanidad es esta que se separó de la Tierra hasta verla como un recurso.</p>'),
  ('<p>No es suficiente "no dañar" - necesitamos activamente sanar.</p>', '<p>No es suficiente "no dañar": necesitamos activamente sanar.</p>'),
  ('<li>Conocimiento open source</li>', '<li>Conocimiento abierto</li>'),
  ('<blockquote>Caso Patagonia: Ropa diseñada para durar generaciones, reparación gratuita de por vida, reventa usada y materiales reciclados/reciclables.</blockquote>',
   '<p>El principio tiene nombre desde 2002, cuando el arquitecto William McDonough y el químico Michael Braungart publicaron <em>De la cuna a la cuna</em>: '
   'diseñar cada producto para que, al terminar su vida, vuelva a ser alimento de la tierra o materia de otro producto.</p>\n'
   '    <blockquote>Caso Patagonia: ropa pensada para durar, un programa para repararla y revenderla usada, y materiales reciclados.</blockquote>'),
  ('<li>Antes de profit: ¿Qué contribuyo?</li>', '<li>Antes de ganar: ¿Qué contribuyo?</li>'),
  ('<blockquote>Interface Inc: Más producen, más sanan planeta. Profit como consecuencia, no meta.</blockquote>',
   '<blockquote>Interface se propuso que cuanto más produjera, más sanara el planeta: la ganancia como consecuencia, no como meta. Su historia sigue en el <a href="nodo_07.html">Nodo 7</a>.</blockquote>'),
  ('<li>Comunidades son stakeholders</li>', '<li>Comunidades son partes interesadas</li>'),
  ('<blockquote>Mondragón Cooperativa: 75,000 trabajador-dueños, ratio salarial 6:1 y 10% de ganancias a comunidad.</blockquote>',
   '<blockquote>Mondragón, en el País Vasco, nació en 1956 con un sacerdote, José María Arizmendiarrieta, y un puñado de jóvenes técnicos. Hoy reúne a '
   'decenas de miles de personas en cooperativas donde muchos trabajadores son también dueños, la distancia entre el sueldo más alto y el más bajo es corta, '
   'y una parte de los excedentes va a la comunidad.</blockquote>'),
  Q('<blockquote>Empresa brasileña que cierra en invierno: "Julio es nuestro mes de barbecho. Todos descansan. Volvemos renovados. Productividad anual subió 30%."</blockquote>'),
  ('<li>Propósito = ROI supremo</li>', '<li>Propósito = el mayor retorno</li>'),
  ('<li>Alegría = bottom line</li>', '<li>Alegría = el resultado final</li>'),
  ('<blockquote>Bután y Felicidad Nacional Bruta: decisiones evaluadas por impacto en felicidad, salud y medio ambiente.</blockquote>',
   '<blockquote>Bután y la Felicidad Nacional Bruta: en 1972, su joven rey dijo que la felicidad de su pueblo importaba más que el producto bruto, y desde '
   '2008 la Constitución le pide al Estado que la promueva, evaluando sus políticas por su efecto en la felicidad, la salud y el ambiente.</blockquote>'),
  ('<blockquote>Buffer: todos los salarios online, fórmula pública y finanzas en tiempo real.</blockquote>',
   '<blockquote>Buffer, una empresa de software, publica desde 2013 el salario de cada persona y la fórmula con que lo calcula.</blockquote>'),
  ('<li>Innovación open source</li>', '<li>Innovación abierta</li>'),
  ('<blockquote>Tesla liberando patentes: "No competimos contra otros autos eléctricos. Competimos contra combustión. Si nosotros ganamos y otros pierden, todos perdemos."</blockquote>',
   '<blockquote>En 1959, Volvo patentó el cinturón de seguridad de tres puntos que había diseñado su ingeniero Nils Bohlin, y dejó que cualquier fabricante '
   'lo usara gratis: salvó más vidas así que guardándolo. Cuatro años antes, en 1955, cuando le preguntaron a Jonas Salk de quién era la patente de su '
   'vacuna contra la polio, respondió con otra pregunta: «¿Se puede patentar el sol?».</blockquote>'),
  ('<h4>8. Propósito Antes que Profit</h4>', '<h4>8. Propósito Antes que Ganancia</h4>'),
  ('<li>Profit (¿Cómo sostenemos lo anterior?)</li>', '<li>Ganancia (¿Cómo sostenemos lo anterior?)</li>'),
  ('<h3>El Dashboard de Consciencia Corporativa</h3>', '<h3>El Tablero de Consciencia Corporativa</h3>'),
  ('<li>Revenue regenerativo (% que sana)</li>', '<li>Ingresos regenerativos (% que sana)</li>'),
  ('<li>Profit distributivo (% compartido)</li>', '<li>Ganancia distribuida (% compartido)</li>'),
  ('<li>ROI social (retorno a comunidad)</li>', '<li>Retorno social (a la comunidad)</li>'),
  ('<li>Confianza index</li>', '<li>Índice de confianza</li>'),
  ('<li>Colaboración frecuencia</li>', '<li>Frecuencia de la colaboración</li>'),
  ('<li>Open source contribuciones</li>', '<li>Aportes al conocimiento abierto</li>'),
  ('<h3>B-Corps: Midiendo Beneficio Total</h3>', '<h3>Empresas B: Midiendo Beneficio Total</h3>'),
  ('<li>3,500+ empresas certificadas</li>', '<li>Miles de empresas certificadas en todo el mundo</li>'),
  ('<li>Evaluación rigurosa 200 puntos</li>', '<li>Una evaluación rigurosa, de hasta 200 puntos: se certifica desde 80</li>'),
  ('<li>Compromiso legal con stakeholders</li>', '<li>Compromiso legal con todas las partes interesadas</li>'),
  ('<li>Gobierno (accountability)</li>', '<li>Gobierno (rendición de cuentas)</li>'),
  ('<blockquote>Caso Patagonia: Puntuación B-Corp 151.4/200. “La Tierra es ahora nuestro único accionista.”</blockquote>',
   '<blockquote>Caso Patagonia: en 2022, Yvon Chouinard cedió la empresa a un fideicomiso y a una organización dedicada a la crisis climática. '
   '“La Tierra es ahora nuestro único accionista”, escribió.</blockquote>'),
  ('<h3>Economía del Donut (Kate Raworth)</h3>', '<h3>Economía Rosquilla (Kate Raworth, 2017)</h3>'),
  ('<blockquote>Amsterdam adoptándolo: primera ciudad “donut”, circularidad como norma y vivienda como derecho.</blockquote>',
   '<blockquote>Ámsterdam la adoptó en 2020, en plena pandemia, como brújula para salir de la crisis: fue la primera gran ciudad en hacerlo.</blockquote>'),
  ('<h3>Economía del Bien Común (Christian Felber)</h3>', '<h3>Economía del Bien Común (Christian Felber, 2010)</h3>'),
  ('<p>Por cada stakeholder:</p>', '<p>Por cada parte interesada:</p>'),
  (('<p><strong>Puntuación:</strong></p>', '<li>1000+ empresas participando</li>'),
   '<p><strong>Puntuación y propuesta:</strong></p>\n'
   '    <ul>\n'
   '      <li>Hasta 1000 puntos posibles</li>\n'
   '      <li>Auditoría externa</li>\n'
   '      <li>La propuesta: que las empresas con mejor puntuación paguen menos impuestos</li>\n'
   '      <li>y tengan preferencia en los contratos públicos</li>\n'
   '      <li>Empresas de muchos países ya hicieron su balance</li>'),
  ('<h3>Economía Sagrada (Charles Eisenstein)</h3>', '<h3>Economía Sagrada (Charles Eisenstein, 2011)</h3>'),
  ('<p><strong>Principios místicos:</strong></p>', '<p><strong>Principios:</strong></p>'),
  ('<li>Interés negativo (incentiva préstamos)</li>', '<li>Interés negativo (desalienta acumular)</li>'),
  ('<li>Deuda jubilar</li>\n    </ul>\n',
   '<li>Jubileo de las deudas, como el que pide el Levítico (25)</li>\n    </ul>\n'
   '    <p>La idea del dinero que se oxida es de Silvio Gesell, un comerciante alemán que vivió muchos años en la Argentina y la expuso en <em>El orden '
   'económico natural</em> (1916). En 1932, en plena Gran Depresión, el pueblo austríaco de Wörgl la puso a prueba con billetes que perdían valor cada mes '
   'si no se gastaban: el dinero circuló, se hicieron obras y bajó el desempleo, hasta que el banco central lo prohibió en 1933.</p>\n'),
  ('<li>Freicoin (crypto con oxidación)</li>', '<li>Freicoin (una criptomoneda que se oxida)</li>'),
  ('<li>Time banks (intercambio de tiempo)</li>', '<li>Bancos de tiempo: una hora de trabajo vale una hora, sea cual sea el oficio</li>'),
  ('<li>Gift circles (economía del regalo)</li>', '<li>Círculos de regalo (economía del don)</li>'),
  ('      <li>Permacultura financiera</li>\n      <li>Abundance leagues</li>\n', ''),
  ('<h4>No Uber - Cooperativismo de Plataforma</h4>', '<h4>No Uber: Cooperativismo de Plataforma</h4>\n'
   '    <p>Trebor Scholz le dio nombre en 2014: plataformas digitales que pertenecen a quienes trabajan en ellas.</p>'),
  ('<p><strong>Problema con “sharing economy”:</strong></p>', '<p><strong>Problema con la “economía colaborativa” de las grandes plataformas:</strong></p>'),
  ('<li>Fairbnb: Coop de hospedaje, 50% a comunidad</li>', '<li>Fairbnb: hospedaje en cooperativa; la mitad de su comisión va a proyectos del barrio</li>'),
  ('<li>Eva: Ride-sharing coop en Montreal</li>', '<li>Eva: viajes compartidos en cooperativa, en Montreal</li>'),
  ('<li>Stocksy: Fotografía coop, artistas dueños</li>', '<li>Stocksy: fotografía en cooperativa, con los artistas como dueños</li>'),
  ('<li>Resonate: Streaming música, músicos dueños</li>', '<li>Resonate: música por internet, en cooperativa con los músicos</li>'),
  ('el líder no maximiza profit sino que guarda la llama', 'el líder no maximiza la ganancia sino que guarda la llama'),
  ('<li>Defender propósito contra profit</li>', '<li>Defender el propósito frente a la ganancia fácil</li>'),
  ('<blockquote>Paul Polman (Ex-CEO Unilever): "Mi trabajo no es maximizar valor para accionistas. Es maximizar valor para el mundo."</blockquote>',
   '<blockquote>Cuando Paul Polman llegó a dirigir Unilever, en 2009, dejó de dar previsiones de ganancias cada trimestre y les dijo a los inversores que solo '
   'buscaban el corto plazo que pusieran su dinero en otra parte.</blockquote>'),
  ('<li>Conectar stakeholders diversos</li>', '<li>Conectar partes interesadas diversas</li>'),
  ('<blockquote>Emmanuel Faber (Ex-CEO Danone): "Fui despedido por poner propósito primero. Lo volvería a hacer."</blockquote>',
   '<blockquote>En 2020, Emmanuel Faber hizo de Danone la primera gran empresa francesa de la bolsa en adoptar la figura de sociedad con misión, que obliga '
   'por estatuto a cumplir un propósito social y ambiental. Al año siguiente, el directorio lo apartó, bajo la presión de inversores que reclamaban más rentabilidad.</blockquote>'),
  ('<blockquote>Gunter Pauli: "No hay desecho en la naturaleza. Desecho es falta de imaginación."</blockquote>',
   '<blockquote>Gunter Pauli, el empresario belga que propuso la economía azul (2010), parte de una observación: en la naturaleza no existe el desecho, porque '
   'lo que a uno le sobra es alimento de otro.</blockquote>'),
  ('<blockquote>Ejemplo: transición del carbón con re-entrenamiento pagado, pensiones garantizadas y regeneración de tierras.</blockquote>',
   '<blockquote>Ejemplo: en 2018, España acordó con los sindicatos el cierre de sus minas de carbón con jubilaciones anticipadas, formación para nuevos empleos '
   'y restauración de las tierras.</blockquote>'),
  ('<li>Total autonomía</li>\n      <li>Sin managers</li>', '<li>Total autonomía</li>\n      <li>Sin gerentes</li>'),
  (('<p><strong>Métricas tradicionales:</strong></p>', '<li>Mejor empleador Holanda: 5 años</li>\n    </ul>'),
   '<p>Buurtzorg cuida con menos horas por paciente y cuesta menos en total que el resto del sector, aunque la hora de cada enfermera valga más: los datos '
   'están en el <a href="nodo_02.html">Nodo 2</a>. Hoy reúne a cerca de la mitad de las enfermeras de barrio de los Países Bajos.</p>\n'
   '    <p><strong>Lo que más le importa:</strong></p>\n'
   '    <ul>\n'
   '      <li>Pacientes que recuperan su autonomía</li>\n'
   '      <li>Enfermeras que vuelven a sentir el sentido de su oficio</li>\n'
   '      <li>Vecinos que aprenden a cuidarse entre sí</li>\n'
   '    </ul>'),
  Q('<blockquote>Jos de Blok: "Probamos que poner humanidad primero es también el mejor negocio. La economía del cuidado es la economía del futuro."</blockquote>'),
  ('<li>Talking stick</li>', '<li>Un objeto de la palabra que pasa de mano en mano</li>'),
  ('<li>Check-in: relación con dinero (20 min)</li>', '<li>Ronda de llegada: la relación con el dinero (20 min)</li>'),
  ('<p><strong>Fase 1: Mapeo linear actual</strong></p>', '<p><strong>Fase 1: Mapeo lineal actual</strong></p>'),
  ('<li>Compartir open source</li>', '<li>Compartir en abierto</li>'),
  ('<p><strong>Respuestas probadas:</strong></p>', '<p><strong>Respuestas posibles:</strong></p>'),
  ('<li>Considerar estructura B-Corp</li>', '<li>Considerar la certificación de Empresa B</li>'),
  ('<blockquote>Larry Fink (CEO BlackRock): "Propósito no es \'woke\'. Es capitalismo consciente. Las empresas sin propósito no sobrevivirán."</blockquote>',
   '<blockquote>En su carta anual de 2022, Larry Fink, que dirige BlackRock, escribió que pensar en todas las partes interesadas no es una postura política: '
   'es capitalismo, hecho de relaciones que benefician a ambos lados.</blockquote>'),
  ('<li>Interface domina su mercado</li>', '<li>Interface sigue entre las mayores fabricantes de losetas de alfombra del mundo</li>'),
  ('<li>Buurtzorg es líder global</li>', '<li>Buurtzorg reúne a la mitad de las enfermeras de barrio de su país</li>'),
  ('      <li>Tesla es más valiosa que GM + Ford</li>\n', ''),
  ('<li>Premium por propósito</li>', '<li>Valor agregado por propósito</li>'),
  ('Mi ROI en regeneración. Mi legacy en amor.', 'Mi retorno en regeneración. Mi legado en amor.'),
  ('<h2>Reflexión Cuántica Final</h2>', '<h2>Reflexión Final</h2>'),
  ('<p>La economía de la consciencia no es utopía - es supervivencia evolucionada. No es idealismo - es pragmatismo supremo. No es sacrificio - es prosperidad real.</p>',
   '<p>La economía de la consciencia no es utopía: es supervivencia evolucionada. No es idealismo: es pragmatismo supremo. No es sacrificio: es prosperidad real.</p>'),
  ('<p>El sistema económico actual es un suicidio colectivo en cámara lenta.', '<p>El sistema económico actual se consume a sí mismo en cámara lenta.'),
  ('El capitalismo extractivo está matando el planeta y nuestra alma.', 'El capitalismo extractivo está agotando el planeta y nuestra alma.'),
 ],
 puertas=[p_origen('Que John Maynard Keynes imaginó en 1930 que sus nietos trabajarían unas quince horas por semana, y que en 2022 sesenta y una empresas '
                   'británicas probaron la semana de cuatro días con el mismo sueldo, se despliega en <em>La Consciencia Planetaria</em>, Libro XI de Trinity '
                   'Origen, nodo 6: «La Nueva Tierra».', 'Libro_11/nodo_06.html')],
)


# ---------------------------------------------------------------- Nodo 6
# El nodo que La Obra más cita: la vela, el salvador exhausto, Atlas y sus «Reframes necesarios», las señales
# de alerta y la meditación de renovación conservan su letra. El agotamiento, con su nombre clínico
# (Freudenberger, Maslach, la OMS); Figley y Singer con la letra de La Obra. Muere un rol, nunca una persona:
# la etapa 7 deja de llamarse «muerte»; la idea de no estar se habla ese mismo día; el testimonio del suicidio
# deja su lugar a lo que un círculo puede y no puede. YPO, Sagmeister y Huffington, con lo que consta.
R['nodo_06.html'] = dict(reemplazos=[
  ('<h3>Burnout Sagrado vs. Burnout Tóxico</h3>', '<h3>El Fuego que Alumbra y el que Quema</h3>'),
  ('El líder consciente aprende a arder continuamente sin consumirse.</p>',
   'El líder consciente aprende a arder continuamente sin consumirse, como la zarza que Moisés vio en el desierto: ardía y no se consumía (Éxodo 3, 2).</p>'),
  ('<h3>Anatomía del Burnout del Líder Consciente</h3>',
   '<h3>Anatomía del Agotamiento del Líder Consciente</h3>\n'
   '    <p>El agotamiento tiene nombre clínico. En 1974, el psicólogo Herbert Freudenberger describió el <em>burnout</em> en los voluntarios de una clínica '
   'gratuita de Nueva York, y se reconoció a sí mismo entre ellos. En 1981, Christina Maslach creó la escala con que todavía se mide: cansancio emocional, '
   'distancia cínica, sensación de no lograr nada. Y en 2019, la Organización Mundial de la Salud lo incluyó en su clasificación como un fenómeno del trabajo.</p>'),
  ('<li>Perfectionism espiritual: Debes ser ejemplo impecable</li>', '<li>Perfeccionismo espiritual: Debes ser ejemplo impecable</li>'),
  ('<blockquote>Confesión anónima de CEO consciente: "Lidero una empresa regenerativa. Todos me ven como gurú del nuevo paradigma. Nadie sabe que lloro cada noche por el peso de intentar salvar el mundo."</blockquote>',
   '<p>En 1995, el psicólogo Charles Figley llamó fatiga por compasión a algo que veía en enfermeras, médicos, terapeutas y bomberos: un desgaste que no venía '
   'de trabajar mucho, sino de cargar durante años con el dolor de los otros. Años después, la neurocientífica Tania Singer y su equipo en Leipzig compararon '
   'dos entrenamientos breves: ponerse del todo en el lugar del que sufre aumentó el malestar de quienes lo practicaron; cultivar compasión, un afecto cálido '
   'por el que sufre sin hundirse en su dolor, hizo crecer las emociones positivas. ' + NO_CARGAR + '</p>'),
  ('<h4>Las 7 Etapas del Burnout Consciente</h4>', '<h4>Las 7 Etapas del Agotamiento Consciente</h4>'),
  ('<li>Relaciones rotas</li>\n    </ul>\n',
   '<li>Relaciones rotas</li>\n    </ul>\n'
   '    <p>Aquí ya no alcanza con descansar: es momento de consultar.</p>\n'),
  ('<p><strong>Etapa 7: Muerte o Renacimiento</strong></p>', '<p><strong>Etapa 7: Retirada o Renacimiento</strong></p>'),
  ('<li>Opción A: Abandono total (muerte del líder)</li>', '<li>Opción A: Dejar el rol por completo, desde el agotamiento</li>'),
  ('<li>Bypass del dolor: "Debo estar en gratitud siempre"</li>', '<li>Atajo para esquivar el dolor: "Debo estar en gratitud siempre"</li>'),
  ('<blockquote>Caso real documentado: Fundadora de ONG ambiental, 38 años, colapso total: "Salvé 100,000 hectáreas de bosque pero perdí mi salud, mi matrimonio y mi alegría. Me convertí en mártir de mi propia causa."</blockquote>',
   '<p>En noviembre de 2011, a pocos meses de asumir la dirección del Lloyds Banking Group en plena crisis financiera, António Horta-Osório dejó de dormir '
   'hasta quedar exhausto, y tuvo que tomarse una licencia de dos meses. Volvió, y años después lo contó en público para que otros no lo callaran: su banco hizo '
   'de la salud mental de su gente una causa.</p>'),
  ('<h2>Prácticas de Auto-Cuidado Radical</h2>', '<h2>Prácticas de Autocuidado Radical</h2>'),
  ('<p>El auto-cuidado para el líder consciente no es spa ocasional. Es disciplina diaria de guerra santa para mantener el canal limpio y la llama viva.</p>',
   '<p>El autocuidado para el líder consciente no es un spa ocasional. Es una disciplina diaria, como la de quien cuida una lámpara: limpiar el vidrio, recortar '
   'la mecha, cargar el aceite, para que la llama siga viva.</p>'),
  ('<blockquote>Protocolo de CEO: 5:00 AM - Yoga 6:00 AM - Meditación 7:00 AM - Desayuno sin dispositivos 8:00 AM - Inicio día desde plenitud.</blockquote>',
   '<blockquote>Un protocolo posible: 5:00, yoga; 6:00, meditación; 7:00, desayuno sin dispositivos; 8:00, inicio del día desde la plenitud.</blockquote>'),
  Q('<blockquote>"Mi productividad aumentó 50% cuando empecé a dormir 8 horas."</blockquote>'),
  ('<li>Journaling: Procesar no acumular</li>', '<li>Escritura personal: Procesar, no acumular</li>'),
  ('<li>Silencio: Espacios sin input</li>', '<li>Silencio: Espacios sin estímulos</li>'),
  ('<li>Coherencia HeartMath: 3x día</li>', '<li>Respiración coherente: 3 veces al día</li>'),
  Q('<blockquote>Revelación de líder: "Descubrí que mi activismo venía de ira, no amor. Cuando cambié la fuente, todo se transformó."</blockquote>'),
  ('<li>Conexión con misterio: Awe y wonder</li>', '<li>Conexión con misterio: Asombro y maravilla</li>'),
  ('<li>Familia: Boundaries sagrados</li>', '<li>Familia: Límites sagrados</li>'),
  ('<blockquote>Confesión necesaria: "Creí que pedir ayuda era debilidad. Mi breakdown me enseñó que es supervivencia."</blockquote>',
   '<p>Buscar apoyo no es debilidad: es supervivencia. ' + COMPANIA + '</p>'),
  Q('<blockquote>CEO después de burnout: "Tuve que admitir que mi ego había secuestrado el propósito. La humildad me salvó."</blockquote>'),
  ('<li>Risa diaria: Obligatoria</li>', '<li>Risa diaria: Bienvenida</li>'),
  ('<li>Aventura regular: Salir de zona comfort</li>', '<li>Aventura regular: Salir de la zona de confort</li>'),
  Q('<blockquote>Revolución personal: "Instituí \'Viernes de Locura\' en la empresa. Productividad subió, burnout desapareció."</blockquote>'),
  ('<li>Check-in (30 min): Estado real, no máscara</li>', '<li>Ronda de llegada (30 min): Estado real, no máscara</li>'),
  ('<li>Hot seat (90 min): 2 personas, 45 min cada una</li>', '<li>Silla del centro (90 min): 2 personas, 45 min cada una</li>'),
  ('<li>Check-out (10 min): Compromisos de auto-cuidado</li>', '<li>Ronda de salida (10 min): Compromisos de autocuidado</li>'),
  ('<blockquote>Testimonio: "Mi círculo me salvó la vida. Literal. Estaba al borde del suicidio. Ahora somos familia."</blockquote>',
   '<p>Un círculo de pares sostiene mucho, y no reemplaza a un profesional. Si alguien del círculo, o tú, empieza a pensar en no estar, eso no espera a la '
   'reunión del mes: se habla ese mismo día, con alguien que pueda ayudar.</p>'),
  ('<li>Un peer (mismo nivel)</li>', '<li>Un par (mismo nivel)</li>'),
  ('<li>Un mentee (emergente)</li>', '<li>Un aprendiz (emergente)</li>'),
  ('<li>Peer: Espejo y apoyo</li>', '<li>Par: Espejo y apoyo</li>'),
  ('<li>Mentee: Energía e innovación</li>', '<li>Aprendiz: Energía e innovación</li>'),
  ('<p><strong>50,000 CEOs globalmente:</strong></p>',
   '<p>La fundó en 1950 Ray Hickok, que a los 27 años había quedado al frente de la empresa de su familia en Rochester, Nueva York, y no tenía con quién '
   'hablar de lo que eso pesaba. Hoy reúne a decenas de miles de presidentes de empresas en más de cien países.</p>'),
  ('<li>Fórums de 8-10 CEOs</li>', '<li>Foros de 8 a 10 personas</li>'),
  ('<li>Reunión mensual de 4 horas</li>', '<li>Reunión mensual</li>'),
  ('<li>Facilitador profesional</li>', '<li>Facilitación cuidada</li>'),
  ('<li>Gestalt methodology</li>', '<li>El lenguaje de la Gestalt: se comparte la experiencia propia, no se dan consejos</li>'),
  (('<p><strong>Resultados:</strong></p>\n    <ul>\n      <li>93% dicen que salvó su matrimonio</li>', 'Sin ellos, habría colapsado hace años."</blockquote>'),
   '<p>Sus propias reglas lo aclaran: el foro no es un grupo de terapia. Sostiene, escucha y acompaña; cuando hace falta algo más, se busca a un profesional.</p>'),
  ('<h2>Renovación Cíclica y Sabbáticos</h2>', '<h2>Renovación Cíclica y Sabáticos</h2>'),
  ('<p>En una cultura que glorifica el hustle, descansar es rebelión.', '<p>En una cultura que glorifica el ajetreo, descansar es rebelión.'),
  ('<p><strong>Breaks sagrados:</strong></p>', '<p><strong>Pausas sagradas:</strong></p>'),
  (('<p><strong>Mes lunar:</strong></p>', '<li>Cuarto menguante: Reflexión y limpieza</li>'),
   '<p><strong>Mes en cuatro semanas:</strong></p>\n'
   '    <ul>\n'
   '      <li>Primera semana: Siembra de intenciones</li>\n'
   '      <li>Segunda semana: Acción intensiva</li>\n'
   '      <li>Tercera semana: Celebración y cosecha</li>\n'
   '      <li>Cuarta semana: Reflexión y limpieza</li>'),
  ('<li>Invierno: Descanso y visioning</li>', '<li>Invierno: Descanso y visión</li>'),
  ('<h3>El Sabbático Como Tecnología de Renovación</h3>',
   '<h3>El Sabático Como Tecnología de Renovación</h3>\n'
   '    <p>La palabra viene del <em>shabat</em> hebreo, y la idea, del Levítico: cada siete años, la tierra descansa (25, 4). En 1951, Abraham Joshua Heschel '
   'escribió en <em>El Shabat</em> que ese día es un palacio en el tiempo: no se construye nada, se habita.</p>'),
  ('<h4>Tipos de Sabbáticos</h4>', '<h4>Tipos de Sabáticos</h4>'),
  ('<p><strong>Mini-sabbático (1 semana/trimestre):</strong></p>', '<p><strong>Minisabático (1 semana por trimestre):</strong></p>'),
  ('<p><strong>Midi-sabbático (1 mes/año):</strong></p>', '<p><strong>Sabático medio (1 mes por año):</strong></p>'),
  ('<p><strong>Maxi-sabbático (3-12 meses/7 años):</strong></p>', '<p><strong>Gran sabático (3 a 12 meses cada 7 años):</strong></p>'),
  ('<li>Transformación completa</li>\n      <li>Muerte y renacimiento</li>', '<li>Transformación completa</li>\n      <li>Cierre de una etapa y renacimiento</li>'),
  ('<p>Diseñador que cierra estudio 1 año cada 7.</p>', '<p>Diseñador de Nueva York que cierra su estudio un año cada siete.</p>'),
  ('<li>Año 7: Sabbático total</li>', '<li>Año 7: Sabático total</li>'),
  (('<li>Mejores clientes después</li>', '<blockquote>"El sabbático no es pérdida de un año. Es inversión en los próximos seis."</blockquote>'),
   '<li>Alegría restaurada</li>\n'
   '    </ul>\n'
   '    <p>En una charla TED de 2009, Sagmeister contó que todo lo que su estudio hizo en los siete años siguientes nació de ese año sin clientes.</p>'),
  ('<h3>La Locura Sagrada de Cambiar el Mundo</h3>', '<h3>El Precio Íntimo de Cambiar el Mundo</h3>'),
  ('<p>Querer transformar sistemas enfermos desde dentro puede volverte loco. La salud mental no es lujo - es requisito.</p>',
   '<p>Querer transformar sistemas enfermos desde dentro puede enfermarte. La salud mental no es lujo: es requisito.</p>'),
  ('<li>Paralysis por magnitud</li>', '<li>Parálisis por magnitud</li>'),
  ('<li>Comunidades online</li>', '<li>Comunidades en línea</li>'),
  ('<p><strong>Flags rojos:</strong></p>', '<p><strong>Banderas rojas:</strong></p>'),
  ('<li>Propósito cuestionado</li>\n    </ul>\n',
   '<li>Propósito cuestionado</li>\n    </ul>\n'
   '    <p>Y una señal que no espera: si aparece la idea de no estar, se habla ese mismo día con un profesional o con alguien de confianza.</p>\n'),
  ('<li>Medicación si necesaria (sin shame)</li>', '<li>Medicación si es necesaria (sin vergüenza)</li>'),
  Q('<blockquote>Testimonio valiente: "Soy CEO de empresa Fortune 500 y tomo antidepresivos. Mi salud mental es mi ventaja competitiva."</blockquote>'),
  ('<blockquote>"Tuve éxito según todas las métricas excepto las que importan."</blockquote>',
   '<p>Lo contó en <em>Thrive</em> (2014): según las dos medidas habituales del éxito, el dinero y el poder, le iba muy bien; según cualquier medida sensata '
   'de una vida buena, no.</p>'),
  ('<li>Redefinir éxito (Third Metric)</li>', '<li>Redefinir el éxito con una tercera métrica, más allá del dinero y el poder (2013)</li>'),
  ('<li>Desconexión digital</li>\n    </ul>', '<li>Desconexión digital</li>\n      <li>Un libro sobre el sueño: <em>La revolución del sueño</em> (2016)</li>\n    </ul>'),
  ('<li>Misión: Acabar con burnout</li>', '<li>Misión: Terminar con la epidemia de agotamiento</li>'),
  ('      <li>Millones alcanzados</li>\n      <li>Corporaciones transformadas</li>\n', ''),
  Q('<blockquote>"Mi colapso fue mi despertar. Ahora ayudo a otros a despertar sin colapsar."</blockquote>'),
  ('<li>Establecer boundaries</li>', '<li>Establecer límites</li>'),
  ('<li>Crear accountability</li>', '<li>Crear compromisos que alguien acompañe</li>'),
  ('<li>10 AM: Práctica espiritual elegida</li>', '<li>10:00: Práctica espiritual elegida</li>'),
  ('<li>11 AM: Naturaleza (caminar/jardín/agua)</li>', '<li>11:00: Naturaleza (caminar/jardín/agua)</li>'),
  ('<li>1 PM: Comida consciente y nutritiva</li>', '<li>13:00: Comida consciente y nutritiva</li>'),
  ('<li>3 PM: Creatividad sin propósito</li>', '<li>15:00: Creatividad sin propósito</li>'),
  ('<li>5 PM: Reflexión de semana y preparación</li>', '<li>17:00: Reflexión de semana y preparación</li>'),
  ('<li>7 PM: Conexión (familia/amigos/comunidad)</li>', '<li>19:00: Conexión (familia/amigos/comunidad)</li>'),
  ('<li>9 PM: Preparación para dormir</li>', '<li>21:00: Preparación para dormir</li>'),
  ('<li>10 PM: Sueño temprano</li>', '<li>22:00: Sueño temprano</li>'),
  ('<h2>Reflexión Cuántica Final</h2>', '<h2>Reflexión Final</h2>'),
  ('El martirio no es noble - es irresponsable. Tu bienestar no es lujo - es tu primera responsabilidad.',
   'El martirio no es noble: es irresponsable. Tu bienestar no es lujo: es tu primera responsabilidad.'),
  ('<p>El secreto: Tu auto-cuidado ES tu servicio.', '<p>El secreto: Tu autocuidado ES tu servicio.'),
 ],
 puertas=[arq('Que la vela que se consume es la que quiere iluminar sola toda la habitación, y que la compasión, a diferencia de la empatía que agota, '
              'es el amor que dura, se despliega en <em>La Obra</em>, Libro 12 de <em>Arquitectura del Destino</em>, Umbral VI: «Empatía que agota, '
              'compasión que sostiene».', 'libro-12-la-obra/L12-U6.html')],
)


# ---------------------------------------------------------------- Nodo 7
# La vida tiene 3.800 millones de años, no «billones». Gaia, con Lovelock y Margulis; los derechos de la
# naturaleza, con el Mar Menor; Faith in Nature, Interface, Patagonia Provisions, Schiphol y Polman, con lo que
# consta; Benyus, Reed, Meadows (corregida), Holling y Gunderson, Macy y Johnstone, Seed y Macy, Thich Nhat
# Hanh, Parker y Lyons. Las etapas de la evolución quedan sin años (decisión de Arturo). El proverbio
# atribuido deja su lugar a Honi, con la letra de La Obra. «Llamado Final a los Guardianes» y «Reflexión
# Cuántica Final del Libro» conservan su letra y su nombre: La Obra los cita.
R['nodo_07.html'] = dict(reemplazos=[
  ('Sirve a la Vida misma - esa inteligencia de 3.8 billones de años', 'Sirve a la Vida misma: esa inteligencia de 3.800 millones de años'),
  ('<h2>Gaia como Stakeholder Supremo</h2>', '<h2>Gaia como Parte Interesada Suprema</h2>'),
  ('<h3>La Tierra No Es Recurso - Es Ser Sintiente</h3>', '<h3>La Tierra No Es Recurso: Es Ser Sintiente</h3>'),
  ('<p class="lead">El salto cuántico del liderazgo consciente:', '<p class="lead">El gran salto del liderazgo consciente:'),
  ('<h4>Principios de Gaia (James Lovelock)</h4>', '<h4>Principios de Gaia (James Lovelock y Lynn Margulis)</h4>'),
  ('<li>Feedback loops son reales</li>', '<li>Los circuitos de retroalimentación son reales</li>'),
  Q('<blockquote>CEO después de epifanía: "Cuando entendí que mi empresa era una célula en el cuerpo de Gaia, cada decisión cambió. Ya no pregunto \'¿es bueno para el negocio?\' sino \'¿sirve a la Vida?\'"</blockquote>'),
  ('<li>Panamá: Naturaleza tiene derecho a existir (2022)</li>',
   '<li>Panamá: Naturaleza tiene derecho a existir (2022)</li>\n      <li>España: el Mar Menor, primer ecosistema europeo con personalidad jurídica (2022)</li>'),
  ('<li>Naturaleza en el board (voz y voto)</li>', '<li>Naturaleza en el directorio (voz y voto)</li>'),
  (('<p>Empresa de cosméticos nombra a Naturaleza en Board.</p>', '<blockquote>"Gaia es nuestra CEO real. Nosotros solo ejecutamos su visión."</blockquote>'),
   '<p>En 2022, Faith in Nature, una fabricante británica de jabones y champús naturales, se convirtió en la primera empresa en sentar a la Naturaleza en su '
   'directorio.</p>\n'
   '    <p><strong>Proceso:</strong></p>\n'
   '    <ul>\n'
   '      <li>Cambió sus estatutos para que su propósito incluya el bien del planeta</li>\n'
   '      <li>Nombró a una abogada ambiental como directora en nombre de la Naturaleza</li>\n'
   '      <li>Voz y voto en las decisiones del directorio</li>\n'
   '      <li>Reporta a la Vida, no solo a las ganancias</li>\n'
   '    </ul>'),
  ('<h3>3.8 Billones de Años de I+D Gratis</h3>', '<h3>3.800 Millones de Años de I+D Gratis</h3>'),
  ('<p>La naturaleza ha resuelto cada problema que enfrentamos. El líder sabio no inventa - observa, aprende e imita.</p>',
   '<p>La naturaleza ha resuelto cada problema que enfrentamos. El líder sabio no inventa: observa, aprende e imita.</p>\n'
   '    <p>La palabra la popularizó la bióloga Janine Benyus en 1997, con <em>Biomímesis</em>, y al año siguiente cofundó la consultora que hoy se llama '
   'Biomimicry 3.8, por los 3.800 millones de años que la vida lleva investigando. Los principios que siguen son los que ese equipo llama Principios de la Vida.</p>'),
  ('<li>Fail fast, learn faster</li>', '<li>Fallar rápido, aprender más rápido</li>'),
  ('<li>Cero waste como meta</li>', '<li>Cero desperdicio como meta</li>'),
  ('<li>Sourcing local prioritario</li>', '<li>Proveedores locales primero</li>'),
  ('<li>Grassroots innovation</li>', '<li>Innovación desde las bases</li>'),
  ('<p>Auto-organización.</p>', '<p>Autoorganización.</p>'),
  ('<li>Auto-ensamblaje</li>', '<li>Autoensamblaje</li>'),
  ('<li>Equipos auto-organizados</li>', '<li>Equipos autoorganizados</li>'),
  ('<li>KISS principle</li>', '<li>Lo simple primero</li>'),
  ('<li>Think global, act local</li>', '<li>Pensar en global, actuar en local</li>'),
  ('<p>Responder a feedback.</p>', '<p>Responder a la retroalimentación.</p>'),
  ('<li>Data-driven decisions</li>', '<li>Decisiones guiadas por datos</li>'),
  ('<li>Feedback loops cortos</li>', '<li>Ciclos de retroalimentación cortos</li>'),
  ('<li>Learning organization</li>', '<li>Organización que aprende</li>'),
  ('<h4>Interface Inc: Misión Zero</h4>', '<h4>Interface: Misión Cero</h4>'),
  ('<p><strong>Ray Anderson, CEO, 1994: Epifanía ecológica</strong></p>',
   '<p><strong>1994: Ray Anderson, su fundador, y una epifanía ecológica</strong> (la pregunta que la desató se cuenta en el <a href="nodo_04.html">Nodo 4</a>)</p>'),
  ('<li>Alfombras como hojas de bosque (no uniformes)</li>',
   '<li>Alfombras como el suelo de un bosque: el diseñador David Oakey notó que en el bosque no hay dos hojas iguales, y creó losetas sin un patrón '
   'uniforme, que se colocan en cualquier dirección y desperdician menos</li>'),
  ('<li>Adhesivos inspirados en gecko</li>', '<li>Losetas que se unen sin pegamento, con pequeños cuadrados adhesivos inspirados en las patas del gecko (TacTiles)</li>'),
  (('<p><strong>Resultados 2020:</strong></p>', '<blockquote>"No preguntamos \'¿cómo hacer alfombras?\' sino \'¿cómo haría la naturaleza alfombras?\'"</blockquote>'),
   '<p><strong>Resultados:</strong></p>\n'
   '    <p>En 2019, al dar por cumplida su Misión Cero, Interface informó que, comparadas con 1996, sus fábricas de alfombras emitían un 96 % menos de gases '
   'de efecto invernadero, usaban un 89 % de energía renovable y enviaban un 91 % menos de residuos a los vertederos.</p>'),
  ('<h4>Velcro a Eastgate Centre</h4>', '<h4>Del Velcro al Eastgate Centre</h4>'),
  ('<li>Velcro: Inspirado en semillas de bardana</li>', '<li>Velcro: George de Mestral, al volver de una caminata, miró al microscopio los frutos de bardana prendidos a su ropa (1941)</li>'),
  ('<li>Tren bala: Nariz como pico de martín pescador</li>', '<li>Tren bala: el ingeniero Eiji Nakatsu, observador de aves, le dio al Shinkansen la nariz del pico del martín pescador</li>'),
  ('<li>Eastgate Centre: Ventilación como termitero</li>', '<li>Eastgate Centre: el arquitecto Mick Pearce ventiló este edificio de Harare como un termitero (1996)</li>'),
  ('<li>Luces LED: Eficiencia de luciérnagas</li>', '<li>Luces LED: un equipo belga copió las escamas del farol de las luciérnagas y logró que saliera más luz (2013)</li>'),
  ('<li>Turbinas: Aletas de ballena</li>', '<li>Turbinas: los bultos de las aletas de la ballena jorobada, que estudió el biólogo Frank Fish, inspiraron palas más eficientes</li>'),
  ('El líder del futuro no minimiza daño - maximiza beneficio.</p>', 'El líder del futuro no minimiza daño: maximiza beneficio.</p>'),
  ('SOSTENIBLE      ←  Mantiene status quo', 'SOSTENIBLE      ←  Mantiene lo que hay'),
  ('CONVENCIONAL    ←  Business as usual (destructivo)</pre>',
   'CONVENCIONAL    ←  Lo de siempre (destructivo)</pre>\n'
   '    <p>La escalera se inspira en la que dibujó el arquitecto Bill Reed en 2007, de la práctica convencional a la regenerativa.</p>'),
  ('<li>Hoy: Mayoría en convencional</li>', '<li>Primera etapa: la mayoría, en lo convencional</li>'),
  ('<li>2030: Mayoría en reducir daño</li>', '<li>Segunda etapa: la mayoría reduce el daño</li>'),
  ('<li>2040: Mayoría en sostenible</li>', '<li>Tercera etapa: la mayoría, sostenible</li>'),
  ('<li>2050: Mayoría en regenerativo</li>', '<li>Cuarta etapa: la mayoría, regenerativa</li>'),
  ('<li>Salmón de pesca regenerativa</li>', '<li>Salmón de pesca selectiva</li>'),
  ('<li>Buffalo jerky de pastoreo holístico</li>', '<li>Carne seca de búfalo de pastoreo holístico</li>'),
  ('<li>Frutas de agricultura biodinámica</li>', '<li>Frutas de agricultura regenerativa</li>'),
  (('<p><strong>Impacto:</strong></p>\n    <ul>\n      <li>Suelo regenerado: 1M+ acres</li>', '<blockquote>"No vendemos comida. Regeneramos el planeta y la comida es el vehículo."</blockquote>'),
   '<p><strong>Impacto:</strong></p>\n'
   '    <p>En 2017, Patagonia impulsó con otros la certificación Orgánico Regenerativo, que mira tres cosas a la vez: la salud del suelo, el bienestar de los '
   'animales y el trato justo a quienes trabajan la tierra.</p>'),
  ('<h4>Diseño Cradle to Cradle</h4>', '<h4>Diseño De la Cuna a la Cuna</h4>'),
  ('<p><strong>Certificación C2C:</strong></p>', '<p><strong>Certificación De la Cuna a la Cuna:</strong></p>'),
  ('<li>Material health</li>', '<li>Salud de los materiales</li>'),
  ('<li>Material reutilization</li>', '<li>Reutilización de los materiales</li>'),
  ('<li>Renewable energy</li>', '<li>Energía renovable</li>'),
  ('<li>Water stewardship</li>', '<li>Cuidado del agua</li>'),
  ('<li>Social fairness</li>', '<li>Equidad social</li>'),
  ('<h3>Caso: Philips Lighting</h3>', '<h3>Caso: La Luz como Servicio</h3>'),
  ('<p><strong>"Light as a Service":</strong></p>',
   '<p>La idea nació de un pedido del arquitecto Thomas Rau, que le dijo a Philips que no quería comprar lámparas sino luz para su oficina de Ámsterdam. '
   'En 2015, el aeropuerto de Schiphol contrató así su iluminación.</p>\n'
   '    <p><strong>"Luz como servicio":</strong></p>'),
  ('<li>Cliente paga por lumens/hora</li>', '<li>El cliente paga por la luz que usa</li>'),
  ('<li>Reciclaje 100% garantizado</li>', '<li>Al final, Philips recupera y recicla los equipos</li>'),
  (('<li>Desperdicios: -90%</li>', '<li>Modelo copiado globalmente</li>'),
   '<li>Equipos pensados para durar mucho más</li>\n'
   '      <li>Mucho menos consumo de energía</li>\n'
   '      <li>Ingresos recurrentes</li>\n'
   '      <li>Un modelo que se copió en otros lugares</li>'),
  ('<h4>Puntos de Apalancamiento (Donella Meadows)</h4>', '<h4>Puntos de Apalancamiento (Donella Meadows, 1999)</h4>'),
  ('<li>Buffers (tamaños estabilizadores)</li>', '<li>Reservas (su tamaño estabiliza)</li>'),
  ('<li>Delays en feedback loops</li>', '<li>Demoras en los circuitos de retroalimentación</li>'),
  ('<li>Feedback loops negativos</li>', '<li>Circuitos que equilibran</li>'),
  ('<li>Feedback loops positivos</li>', '<li>Circuitos que refuerzan</li>'),
  ('<li>Poder de cambiar reglas</li>', '<li>Poder de cambiar las reglas (autoorganización)</li>'),
  ('<li>Paradigmas/mindset</li>', '<li>Paradigmas y mentalidades</li>'),
  ('<p>El líder consciente opera en nivel 1-3.</p>', '<p>El líder consciente opera en los tres últimos.</p>'),
  ('<blockquote>Ejemplo: Tesla probó que eléctricos son superiores y forzó el pivote de toda la industria.</blockquote>',
   '<blockquote>Ejemplo: el éxito de los autos eléctricos de Tesla empujó a otros fabricantes a acelerar los suyos.</blockquote>'),
  ('<p><strong>Pre-competitive cooperation:</strong></p>', '<p><strong>Cooperación precompetitiva:</strong></p>'),
  ('<li>Open source innovations</li>', '<li>Innovaciones abiertas</li>'),
  ('<li>Lobbying conjunto por regulación</li>', '<li>Gestiones conjuntas por una mejor regulación</li>'),
  ('<blockquote>Fashion Pact: 60+ marcas de moda, 1/3 de industria global, compartiendo compromisos climáticos y mejores prácticas.</blockquote>',
   '<blockquote>Fashion Pact (2019): decenas de empresas de moda, con unas doscientas marcas, comparten compromisos para el clima, la biodiversidad y los océanos.</blockquote>'),
  ('<li>De "maximizar shareholder value" a "optimizar stakeholder wellbeing"</li>', '<li>De "maximizar el valor para el accionista" a "cuidar el bienestar de todas las partes interesadas"</li>'),
  ('<p><strong>2009: Paul Polman nombrado CEO Unilever</strong></p>', '<p><strong>2009: Paul Polman llega a dirigir Unilever</strong></p>'),
  ('<li>Pressure por resultados corto plazo</li>', '<li>Presión por resultados de corto plazo</li>'),
  ('<p>Día 1: Elimina reportes trimestrales. Día 2: Anuncia Sustainable Living Plan.</p>',
   '<p>Al llegar, deja de dar previsiones de ganancias cada trimestre. En 2010 lanza el Plan de Vida Sostenible de Unilever.</p>'),
  ('<li>Duplicar negocio</li>', '<li>Duplicar el negocio</li>'),
  ('<li>Reducir impacto ambiental 50%</li>', '<li>Reducir a la mitad el impacto ambiental de sus productos</li>'),
  ('<li>Mejorar salud 1 billón personas</li>', '<li>Ayudar a más de mil millones de personas a mejorar su salud y su bienestar</li>'),
  ('<li>Mejorar vida millones</li>', '<li>Mejorar el sustento de millones de personas</li>'),
  (('<li>Wall Street: "¡Locura!"</li>', '<blockquote>Polman: "El capitalismo necesita reforma urgente o enfrentaremos revoluciones."</blockquote>'),
   '<li>Parte de los inversores: desconfianza</li>\n'
   '      <li>2017: Kraft Heinz intenta comprar Unilever con una oferta hostil, y Unilever la rechaza</li>\n'
   '      <li>Medios: Escepticismo</li>\n'
   '    </ul>'),
  ('<li>Marcas con propósito crecen 2x más rápido</li>', '<li>Sus marcas de vida sostenible crecen más rápido que el resto, según la empresa</li>'),
  ('<li>100% energía renovable en fábricas</li>', '<li>Electricidad renovable en sus fábricas</li>'),
  ('      <li>Cero deforestación en cadena suministro</li>\n      <li>Salario digno para todos</li>\n', ''),
  ('<li>Paridad de género en management</li>', '<li>Paridad de género en la gerencia (2020)</li>'),
  (('<li>Total shareholder return: 290%</li>', '<li>Modelo para industria</li>'),
   '<li>Un retorno total para el accionista cercano al 290 % en su década</li>\n'
   '      <li>Primera, año tras año, en la encuesta de líderes en sostenibilidad de GlobeScan</li>\n'
   '      <li>Modelo para industria</li>'),
  (('<li>Unilever primera empresa &gt;€50B carbono neutral</li>', '<li>CEOs globales siguiendo modelo</li>'),
   '<li>Un plan que muchas empresas tomaron como modelo</li>\n'
   '      <li>Una conversación nueva sobre para qué existe una empresa</li>'),
  ('<li>Co-fundador IMAGINE</li>', '<li>Cofundador de IMAGINE (2019)</li>'),
  ('<li>Asesor UN Global Compact</li>', '<li>Vicepresidente del Pacto Mundial de las Naciones Unidas</li>'),
  ('<li>Mentor próxima generación</li>', '<li>Coautor, con Andrew Winston, de <em>Net Positive</em> (2021)</li>'),
  Q('<blockquote>"Probamos que liderar con propósito no es solo correcto moralmente - es superior financieramente."</blockquote>'),
  ('<p>No es si el sistema colapsará, sino cuándo y cómo. El líder consciente no previene el colapso - lo navega y facilita el renacimiento.</p>',
   '<p>No es si el sistema colapsará, sino cuándo y cómo. El líder consciente no previene el colapso: lo navega y facilita el renacimiento.</p>\n'
   '    <p>El ciclo que sigue lo describió el ecólogo C. S. Holling estudiando bosques y pesquerías, y lo desarrolló con Lance Gunderson en <em>Panarchy</em> '
   '(2002): todo sistema vivo crece, se conserva, se suelta y se reorganiza. Pensar en el colapso puede dar miedo. ' + MIEDO + '</p>'),
  ('<li>Recursos locked</li>', '<li>Recursos inmovilizados</li>'),
  ('<li>Stasis</li>', '<li>Estancamiento</li>'),
  ('<li>Crisis trigger</li>', '<li>Un detonante de crisis</li>'),
  ('<li>Cuestionar status quo</li>', '<li>Cuestionar lo establecido</li>'),
  ('<h3>Preparación para el Gran Turning</h3>', '<h3>Preparación para el Gran Giro</h3>'),
  ('<p>Joanna Macy: 3 Dimensiones del Gran Turning</p>', '<p>Joanna Macy y Chris Johnstone, en <em>Esperanza activa</em> (2012): las 3 dimensiones del Gran Giro</p>'),
  ('<h3>Práctica Mensual</h3>\n    <p><strong>Proceso:</strong></p>',
   '<h3>Práctica Mensual</h3>\n'
   '    <p>El ritual lo crearon en 1985 el activista australiano John Seed y Joanna Macy, y lo contaron con Pat Fleming y Arne Naess en <em>Pensar como una montaña</em> (1988).</p>\n'
   '    <p><strong>Proceso:</strong></p>'),
  ('<li>Convocar "board meeting" imaginario</li>', '<li>Convocar una reunión de directorio imaginaria</li>'),
  Q('<blockquote>CEO que lo practica: "Mi \'Consejo de Todos los Seres\' me ha salvado de decisiones catastróficas. El salmón vetó nuestra expansión al río."</blockquote>'),
  ('<h4>2. Carta desde 2050</h4>', '<h4>2. Carta desde el Futuro</h4>'),
  ('<p>Escribir carta desde tu yo futuro en 2050:</p>', '<p>Escribir una carta desde tu yo futuro, dentro de veinticinco años:</p>'),
  ('<p>5 minutos cada mañana:</p>',
   '<p>La palabra interser es de Thich Nhat Hanh: nada existe por sí solo, y en una hoja de papel están la nube, la lluvia y el árbol.</p>\n'
   '    <p>5 minutos cada mañana:</p>'),
  ('Si lideras un equipo de 5 o una empresa de 50,000,', 'Si lideras un equipo de 5 o una empresa de 50.000,'),
  ('<li>🙏 Servir a las próximas 7 generaciones</li>\n    </ul>\n',
   '<li>🙏 Servir a las próximas 7 generaciones</li>\n    </ul>\n'
   '    <p>Las siete generaciones vienen de la tradición haudenosaunee: la Gran Ley de los iroqueses, que Arthur Parker publicó en 1916, pide a sus jefes '
   'tener presentes no solo a los vivos sino a las generaciones por venir, y el guardián de la fe onondaga Oren Lyons lo enseña así: cada decisión se '
   'piensa por su efecto siete generaciones adelante.</p>\n'),
  ('A ser guardián de este momento único en 3.8 billones de años.', 'A ser guardián de este momento único en 3.800 millones de años.'),
  ('Y ahora, servo a la Vida misma.', 'Y ahora, sirvo a la Vida misma.'),
  ('<p>El Liderazgo Consciente no es un estilo de management.', '<p>El Liderazgo Consciente no es un estilo de gestión.'),
  ('Del burnout a la sostenibilidad.', 'Del agotamiento a la sostenibilidad.'),
  ('<blockquote>"El mejor momento para plantar un árbol fue hace 20 años. El segundo mejor momento es ahora." - Proverbio chino</blockquote>',
   '<blockquote>El Talmud cuenta que Honi vio a un hombre plantando un algarrobo y le preguntó cuántos años tardaba ese árbol en dar fruto. «Setenta», '
   'le respondió. «¿Y crees que vivirás setenta años?» El hombre le contestó: «Yo encontré el mundo con algarrobos. Así como mis padres plantaron para mí, '
   'yo planto para mis hijos» (Taanit 23a).</blockquote>'),
 ],
 puertas=[arq('Que Honi vio a un hombre plantar un árbol que no iba a ver dar fruto, y que a nadie le toca terminar la obra sino hacer su tramo, se '
              'despliega en <em>La Obra</em>, Libro 12 de <em>Arquitectura del Destino</em>, Umbral V: «El algarrobo».', 'libro-12-la-obra/L12-U5.html'),
          p_origen('Que Lovelock y Andrew Watson imaginaron en 1983 un planeta poblado solo de margaritas, negras y blancas, que mantiene templada su '
                   'temperatura sin que ninguna lo busque, se despliega en <em>La Consciencia Planetaria</em>, Libro XI de Trinity Origen, nodo 1: '
                   '«Gaia como Ser Viviente».', 'Libro_11/nodo_01.html')],
)


if __name__ == '__main__':
    total = 0
    for nombre in ['index.html'] + ['nodo_%02d.html' % i for i in range(1, 8)]:
        n = aplicar(nombre, R[nombre])
        total += n
        print(f'{nombre}: {n} cambios')
    print(f'Total: {total} cambios. Salida en {OUT}')
