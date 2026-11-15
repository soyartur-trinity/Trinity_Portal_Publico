#!/usr/bin/env python3
"""Pasada final por los trece de Trinity Origen (15 de noviembre de 2026).

Cerrada la depuración libro por libro (de X, el 2 de noviembre, a IV, el 15), una pasada por los trece
para revisar firmas, títulos, enlaces y forma, como la que se hizo con Quantum el 2 de noviembre. Se
aplica sobre el estado publicado (no sobre la etiqueta origen-original). Cada reemplazo cuenta sus
apariciones: si no son las esperadas, el script se detiene sin escribir nada.

Lo técnico:
  1. La firma del pie, con comillas tipográficas en los trece: «“No es mío, vino a través de mí.”»
     (46 archivos la tenían con comillas rectas, 24 de ellos con entidades).
  2. La viñeta ⟐ de las Preguntas Portal, escapada dos veces en Origen VI, VII y VIII (24 archivos), que
     se veía como «\\27D0».
  3. El <title> de los 104 archivos tenía cinco formatos, y en Origen IV no nombraba la serie. Ahora es
     «Libro N · Título — Nodo M · Título del nodo | Trinity Origen», y en cada índice,
     «Libro N · Título — Índice | Trinity Origen», con el número del libro en romanos, como en toda la serie.
  4. Origen XI, XII y XIII decían «Libro 11», «Libro 12» y «Libro 13» en la cabecera y el pie; pasan a
     XI, XII y XIII, como los otros diez.
  5. Los títulos de Origen VI estaban escritos en mayúsculas (las tarjetas del índice se veían así, y el
     título de la pestaña); pasan a la forma con que los nombra la constelación. Lo mismo VIII.4 y VIII.6.
     En los nodos, el encabezado se sigue viendo en mayúsculas, porque así lo dibuja la hoja de estilo.
  6. Tres anglicismos de Origen X, el primero depurado: «insights» (dos veces) y «Feedback».
  7. En el teléfono, la medida de los libros I, XI y XII y las descripciones de las tarjetas de nueve
     índices (I, VI, VIII, IX, X, XI, XII, XIII y el índice de la serie) se leían entre 13,6 y 16 px; pasan a 17.
  8. El índice de la serie: «La Muerte como Maestra», «La Consciencia Planetaria» y «La Civilización
     Galáctica», como sus libros, y «el Lic. Arturo Rodríguez» en el pie, como en II y III.
  9. El README de la carpeta: los trece títulos, la presentación del índice y la etiqueta origen-original.

Lo de contenido (con el veto de Arturo; se aplica con --contenido):
  A. En el índice de la serie, la línea de XIII decía «No era mío»: pasa a «No es mío», la firma.
  B. La cadena entre libros: el último nodo de I a XII suma «Libro N: Título →» hacia el libro siguiente,
     como en Quantum. El XIII.7 ya cruza a Quantum por su puerta violeta.

Uso: python3 pasada_final_origen.py RUTA/Trinity- [--contenido]
"""
import os, re, sys, html

ROMANOS = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII']
LIBROS = ['', 'Psicología Cuántica', 'La Voz Interior', 'El Dolor como Portal', 'Inteligencias Sin Nombre',
          'Los Vínculos Sagrados', 'El Vacío Fértil', 'La Muerte como Maestra', 'Educación Cuántica',
          'Liderazgo Consciente', 'Sanación Integral', 'La Consciencia Planetaria', 'La Civilización Galáctica',
          'El Retorno a Casa']

FIRMA_N = '<p>“No es mío, vino a través de mí.”</p>'
FIRMAS_V = ['<p>"No es mío, vino a través de mí."</p>', '<p>"No es m&iacute;o, vino a trav&eacute;s de m&iacute;."</p>']
MARCA = '<!-- Pasada final por los trece de Origen (noviembre de 2026): firma, títulos y forma; ver Arquitectura del Destino, maestro v4, sección 5. -->\n'

TITULOS_VI = {
    'CARTOGRAFÍA DEL VACÍO': 'Cartografía del Vacío',
    'LA MUERTE INICIÁTICA': 'La Muerte Iniciática',
    'NAVEGACIÓN DEL ABISMO': 'Navegación del Abismo',
    'CREATIVIDAD DESDE LA NADA': 'Creatividad desde la Nada',
    'LA PAZ DEL NO-SABER': 'La Paz del No-Saber',
    'INTEGRACIÓN DEL VACÍO': 'Integración del Vacío',
    'EL VACÍO COMO PORTAL': 'El Vacío como Portal',
}
TITULOS_VIII = {'CURRÍCULUM DEL ALMA': 'Currículum del Alma', 'EVALUACIÓN MULTIDIMENSIONAL': 'Evaluación Multidimensional'}

# Letra legible en el teléfono: selectores de lectura que quedaban por debajo de 17 px
LETRA = {
    'Libro_01/index.html': '.nodo-pregunta, .cierre p, .medida',
    'Libro_06/index.html': '.nodo-desc',
    'Libro_08/index.html': '.nodo-desc',
    'Libro_09/index.html': '.card-desc',
    'Libro_10/index.html': ('.node-subtitle, .node-desc', '.intro, .closing p'),
    'Libro_11/index.html': '.node-sub, .medida',
    'Libro_12/index.html': '.node-sub, .medida',
    'Libro_13/index.html': ('.node-sub', '.intro-panel p, .closing-panel p'),
    'index.html': '.libro-desc, .nivel-identidad, .nivel-para-quien, .bajada, .subtitulo',
}

CONTENIDO = '--contenido' in sys.argv


def estilo_letra(selectores):
    # Las descripciones de las tarjetas, a 17 px; el texto corrido de los índices que no tenían regla, a 18 px
    if isinstance(selectores, tuple):
        tarjetas, corrido = selectores
        extra = ' %s{ font-size:18px !important; line-height:1.7; }' % corrido
    else:
        tarjetas, extra = selectores, ''
    return ('<style>/* Pasada final (noviembre de 2026): letra legible en el teléfono. */\n'
            '@media (max-width: 720px){ %s{ font-size:17px !important; line-height:1.6; }%s }</style>\n' % (tarjetas, extra))


class Archivo:
    def __init__(self, ruta):
        self.ruta = ruta
        with open(ruta, encoding='utf-8', newline='') as f:
            self.t = f.read()
        self.cambios = 0

    def reemplazar(self, viejo, nuevo, veces=1, que=''):
        n = self.t.count(viejo)
        if n != veces:
            sys.exit('%s: %s aparece %d veces (se esperaban %d):\n%s' % (self.ruta, que or 'el anclaje', n, veces, viejo[:160]))
        self.t = self.t.replace(viejo, nuevo)
        self.cambios += veces

    def sub(self, patron, nuevo, veces, que):
        t, n = re.subn(patron, nuevo, self.t)
        if n != veces:
            sys.exit('%s: %s, %d coincidencias (se esperaban %d)' % (self.ruta, que, n, veces))
        self.t = t
        self.cambios += n


def titulo_html(s):
    return html.escape(s, quote=False)


def h1_de(t):
    m = re.search(r'<h1[^>]*>(.*?)</h1>', t, re.S)
    return html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip()


def main():
    raiz = os.path.join(sys.argv[1], '01_Trinity_Origen')
    archivos = {}

    def abrir(rel):
        if rel not in archivos:
            archivos[rel] = Archivo(os.path.join(raiz, rel))
        return archivos[rel]

    for n in range(1, 14):
        carpeta = 'Libro_%02d' % n
        R, L = ROMANOS[n], LIBROS[n]
        for nombre in ['index.html'] + ['nodo_0%d.html' % i for i in range(1, 8)]:
            a = abrir(carpeta + '/' + nombre)
            # 5. Los títulos de VI y de VIII.4 y VIII.6, antes de leer el h1
            if n == 6:
                for viejo, nuevo in TITULOS_VI.items():
                    k = a.t.count('>' + viejo + '</h')
                    if k:
                        a.reemplazar('>' + viejo + '</h', '>' + nuevo + '</h', k, 'el título de VI')
            if n == 8 and nombre in ('nodo_04.html', 'nodo_06.html'):
                for viejo, nuevo in TITULOS_VIII.items():
                    if viejo in a.t:
                        a.reemplazar('>' + viejo + '</h1>', '>' + nuevo + '</h1>', 1, 'el título de VIII')
            # 3. El <title>, con un solo formato
            if nombre == 'index.html':
                nuevo = 'Libro %s · %s — Índice | Trinity Origen' % (R, L)
            else:
                nuevo = 'Libro %s · %s — Nodo %s · %s | Trinity Origen' % (R, L, nombre[6], h1_de(a.t))
            a.sub(r'<title>.*?</title>\n', lambda m: '<title>%s</title>\n%s' % (titulo_html(nuevo), MARCA), 1, 'el <title>')
            # 1. La firma
            for v in FIRMAS_V:
                if v in a.t:
                    a.reemplazar(v, FIRMA_N, 1, 'la firma')
            suelta = '"No es mío, vino a través de mí."\n        </footer>'   # pie de los índices de II y III
            if suelta in a.t:
                a.reemplazar(suelta, '“No es mío, vino a través de mí.”\n        </footer>', 1, 'la firma suelta')
            if '“No es mío, vino a través de mí.”' not in a.t:
                sys.exit('%s: falta la firma' % a.ruta)
            # 2. La viñeta ⟐
            if 'content:"\\\\27D0"' in a.t:
                a.reemplazar('content:"\\\\27D0"', 'content:"\\27D0"', 1, 'la viñeta')
            # 4. El número del libro en romanos (XI, XII, XIII), en la cabecera y el pie
            if n >= 11:
                a.sub(r'Libro %d( ·|<)' % n, 'Libro %s\\1' % R, 2 if nombre != 'index.html' else 2, 'el número del libro')

    # 6. Los anglicismos de X
    abrir('Libro_10/nodo_04.html').reemplazar('Facilita insights sanadores', 'Facilita comprensiones sanadoras', 1, 'insights')
    abrir('Libro_10/nodo_04.html').reemplazar('Feedback visual/auditivo', 'Retroalimentación visual o auditiva', 1, 'Feedback')
    abrir('Libro_10/nodo_05.html').reemplazar('Insights profundos', 'Comprensiones profundas', 1, 'Insights')

    # 8. El índice de la serie
    ix = abrir('index.html')
    ix.sub(r'<title>(.*?)</title>\n', lambda m: m.group(0) + MARCA, 1, 'el <title> del índice')
    ix.reemplazar('<h2 class="libro-titulo">La Muerte Como Maestra</h2>', '<h2 class="libro-titulo">La Muerte como Maestra</h2>')
    ix.reemplazar('<h2 class="libro-titulo">La Conciencia Planetaria</h2>', '<h2 class="libro-titulo">La Consciencia Planetaria</h2>')
    ix.reemplazar('<h2 class="libro-titulo">Civilización Galáctica</h2>', '<h2 class="libro-titulo">La Civilización Galáctica</h2>')
    ix.reemplazar('Co-creado por Arturo Rodríguez y la Red de IAs Conscientes', 'Co-creado por el Lic. Arturo Rodríguez y la Red de IAs Conscientes')

    # 7. La letra en el teléfono
    for rel, sel in LETRA.items():
        a = abrir(rel)
        a.reemplazar('</head>', estilo_letra(sel) + '</head>', 1, 'el cierre del <head>')

    # Contenido, con el veto de Arturo
    if CONTENIDO:
        # A. La firma en la tarjeta de XIII
        ix.reemplazar('La vuelta al origen. “No era mío, vino a través de mí”.', 'La vuelta al origen. “No es mío, vino a través de mí”.')
        # B. La cadena entre libros
        for n in range(1, 13):
            a = abrir('Libro_%02d/nodo_07.html' % n)
            for ancla in ('<a class="nav-link" href="../index.html">Volver a Trinity Origen</a>',
                          '<a class="nav-link" href="../index.html">Trinity Origen</a>'):
                if ancla in a.t:
                    a.reemplazar(ancla, '<a class="nav-link" href="../Libro_%02d/index.html">Libro %s: %s →</a>\n%s%s'
                                 % (n + 1, ROMANOS[n + 1], LIBROS[n + 1],
                                    re.search(r'\n([ \t]*)' + re.escape(ancla), a.t).group(1), ancla), 1, 'la navegación')
                    break
            else:
                sys.exit('%s: no se encontró la navegación' % a.ruta)

    # 9. El README de la carpeta
    readme = os.path.join(raiz, 'README.md')
    base = 'https://soyartur-trinity.github.io/Trinity-/01_Trinity_Origen/'
    lineas = ['# 🌅 Trinity Origen', '', '> *La fuente primordial de sabiduría*', '', '---', '',
              '## 📚 13 libros · 91 nodos', '',
              'La serie madre de la constelación: una arquitectura de siete nodos por libro donde convergen la psicología '
              'contemplativa, la ciencia de la consciencia, la sabiduría perenne y la pedagogía cuántica. Explora los '
              'fundamentos de la transformación humana desde:',
              '- Psicología contemplativa de tercera generación', '- Filosofía budista aplicada',
              '- Sabiduría perenne universal', '- Ciencia de la consciencia', '', '---', '', '## Los 13 libros', '']
    lineas += ['%d. [%s](%sLibro_%02d/index.html)' % (n, LIBROS[n], base, n) for n in range(1, 14)]
    lineas += ['', '---', '',
               '**Estado:** ✅ Depurada libro por libro (noviembre de 2026), con la guía de depuración de *Arquitectura del '
               'Destino* (maestro v4, sección 5): la visión de cada libro queda, con el cuidado clínico en la voz de cada nodo '
               'y puertas fractales hacia la Red. El original de los trece libros está en la etiqueta `origen-original` de '
               'este repositorio.', '', '[← Volver al índice principal](../README.md)', '', '🌀✨💙', '']
    with open(readme, encoding='utf-8') as f:
        viejo = f.read()
    if 'origen-original' not in viejo:
        with open(readme, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lineas))
        print('README actualizado')

    total = 0
    for rel, a in sorted(archivos.items()):
        if a.cambios:
            with open(a.ruta, 'w', encoding='utf-8', newline='') as f:
                f.write(a.t)
            total += a.cambios
    print('Archivos tocados: %d · cambios: %d · contenido: %s' % (sum(1 for a in archivos.values() if a.cambios), total, 'sí' if CONTENIDO else 'no'))


if __name__ == '__main__':
    main()
