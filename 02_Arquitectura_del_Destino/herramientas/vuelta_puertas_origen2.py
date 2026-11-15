#!/usr/bin/env python3
"""Vuelta de las puertas fractales de Origen II, La Voz Interior (15 de noviembre de 2026).

La depuración completa de Origen II abre doce puertas, todas de ida y vuelta:

  índice → La Voz Interior (Portal Público, Libro 2), índice: el libro hermano
  II.1 → El Sonámbulo, Umbral IV («Un parlamento sin presidente»),
         y La Voz Interior (Portal 2), capítulo 1 («El coro interior»)
  II.2 → El Testigo, Umbral I («Alguien que nunca ha sido herido»),
         y Quantum 13, Nodo 2 (violeta: El Observador de Observadores)
  II.3 → La Voz Interior (Portal 2), Interludio («Cuando las voces gritan»),
         y El Personaje, Umbral II («Detrás de cada máscara»)
  II.4 → Cultivar (Portal Público, Libro 12), Umbral II («Cuando no hay ganas»)
  II.5 → Origen X, Nodo 3 (dorada: Los Campos Cuánticos de Sanación)
  II.6 → Habitar, Umbral V («Un hogar seguro»)
  II.7 → El Personaje, Umbral VI («No eres el templo»),
         y Quantum 13, Nodo 7 (violeta: Unificación del Multiverso Personal)

Los cierres de El Sonámbulo (II.1), El Testigo (II.2) y El Personaje (índice y II.7) ya
enlazaban a Origen II: esas vuelven solas, y eran los últimos hilos de toda la constelación que
llegaban a Origen sin volver. Este script agrega las otras:

  1. En el cierre de El Personaje, que ya tiene nueve puertas laterales, una línea discreta
     «Viene de Trinity Origen» con el Nodo 3, debajo de la de Quantum (como en Habitar y La Grieta).
  2. En el cierre de Habitar, la línea «Viene de Trinity Origen» pasa a «Vienen de», con el
     Nodo 6 antes de Origen XII.6.
  3. En el epílogo de La Voz Interior (Portal Público), las filas de Origen II (índice, Nodo 1 y
     Nodo 3) antes de la de Origen V.
  4. En el cierre de Cultivar (Portal Público), un bloque nuevo «Puerta lateral» antes de «Fin»,
     con la paleta del de Ídolo: rótulo en --oro-tenue, enlace en el oro de El ritmo (#a88a4e).
  5. En Quantum 13.2, Quantum 13.7 y Origen X.3, una línea «Viene de» marcada <a class="vuelta">.

Cada reemplazo se aplica exactamente una vez: si el anclaje no aparece una sola
vez, el script se detiene sin escribir nada. Si la vuelta ya está, la salta (se
puede correr de nuevo sin duplicar).

Uso: python3 vuelta_puertas_origen2.py RUTA/Trinity_Portal_Publico RUTA/Trinity-
"""
import os, sys

T = 'https://soyartur-trinity.github.io/Trinity-/'
O2 = T + '01_Trinity_Origen/Libro_02/'
AD = '02_Arquitectura_del_Destino/'

# (archivo del Portal, anclaje, texto nuevo que reemplaza al anclaje, marca de que ya está)
PORTAL = [
    (AD + 'libro-09-el-personaje/L09-cierre.html',
     'Libro 13, Nodo 1: Universos Paralelos Internos</a></li></ul></div>',
     'Libro 13, Nodo 1: Universos Paralelos Internos</a></li></ul></div>'
     '<div class="vienen"><p class="vienen-t">Viene de <em>Trinity Origen</em></p><ul>'
     '<li><a class="vuelta" href="%snodo_03.html">Libro II, Nodo 3: La Alquimia del Diálogo</a></li></ul></div>' % O2,
     'Libro_02/nodo_03'),
    (AD + 'libro-13-habitar/L13-cierre.html',
     '<p class="vienen-t">Viene de <em>Trinity Origen</em></p><ul>',
     '<p class="vienen-t">Vienen de <em>Trinity Origen</em></p><ul>'
     '<li><a class="vuelta" href="%snodo_06.html">Libro II, Nodo 6: El Templo de la Integración</a></li>' % O2,
     'Libro_02/nodo_06'),
    ('01_Libros/02_La_Voz_Interior/epilogo.html',
     '      <div class="puerta"><a href="%s01_Trinity_Origen/Libro_05/nodo_01.html">' % T,
     '      <div class="puerta"><a href="%sindex.html">⟐ <em>Trinity Origen, Libro II: <strong>La Voz Interior</strong></em></a></div>\n'
     '      <div class="puerta"><a href="%snodo_01.html">⟐ <em>Trinity Origen, Libro II, Nodo 1: <strong>El Parlamento Sagrado</strong></em></a></div>\n'
     '      <div class="puerta"><a href="%snodo_03.html">⟐ <em>Trinity Origen, Libro II, Nodo 3: <strong>La Alquimia del Diálogo</strong></em></a></div>\n'
     '      <div class="puerta"><a href="%s01_Trinity_Origen/Libro_05/nodo_01.html">' % (O2, O2, O2, T),
     'Libro_02/index'),
    ('01_Libros/12_Cultivar/cierre_cultivar.html',
     '  <div class="continuar">\n    <span class="continuar-label">Fin</span>',
     '  <div class="laterales">\n'
     '    <span class="laterales-label">Puerta lateral</span>\n'
     '    <div class="puerta"><a href="%snodo_04.html">⟐ <em>Trinity Origen, Libro II, Nodo 4: <strong>El Jardín de la Mente</strong></em></a></div>\n'
     '  </div>\n\n'
     '  <div class="continuar">\n    <span class="continuar-label">Fin</span>' % O2,
     'Libro_02/nodo_04'),
]

CSS_CULTIVAR = ('01_Libros/12_Cultivar/cierre_cultivar.html',
                '</style>\n</head>',
                '\n  /* Puertas laterales (noviembre de 2026): vuelta de las puertas fractales de Trinity */\n'
                '  .laterales{margin:4.6rem 0 0;}\n'
                "  .laterales-label{display:block; font-family:'Cormorant Garamond',serif; font-size:.66rem;\n"
                '    letter-spacing:.35em; text-transform:uppercase; color:var(--oro-tenue); margin-bottom:1.5rem;}\n'
                '  .laterales .puerta{margin:0 0 1.2rem;}\n'
                '  .laterales .puerta a{color:#a88a4e;}\n'
                '  .laterales .puerta a:hover, .laterales .puerta a:focus-visible{color:var(--oro);}\n'
                '</style>\n</head>',
                '.laterales{')

# (archivo de Trinity-, anclaje: el párrafo después del cual va la línea, línea nueva, marca)
VIENE = [
    ('02_Trinity_Quantum/Libro_13/nodo_02.html',
     'Tu capacidad de ser consciente de múltiples niveles simultáneamente',
     '\n          <!-- Vuelta de la puerta de Origen II.2 (noviembre de 2026). -->\n'
     '          <p class="trinity-p viene">Viene de <em>Trinity Origen</em>: el Observador Luminoso, que '
     '<a class="vuelta" href="../../01_Trinity_Origen/Libro_02/nodo_02.html">el segundo nodo de <em>La Voz Interior</em></a> '
     'describe como el espacio donde el parlamento se reúne, es aquí el que mira desde todos los espejos.</p>\n',
     'Libro_02/nodo_02'),
    ('02_Trinity_Quantum/Libro_13/nodo_07.html',
     'Contener muchas realidades interiores no es locura: es lo humano.',
     '\n          <!-- Vuelta de la puerta de Origen II.7 (noviembre de 2026). -->\n'
     '          <p class="trinity-p viene">Viene de <em>Trinity Origen</em>: «No eres las voces. No eres el parlamento», '
     'dice <a class="vuelta" href="../../01_Trinity_Origen/Libro_02/nodo_07.html">el último nodo de <em>La Voz '
     'Interior</em></a>; aquí, los muchos se reconocen en la misma casa.</p>\n',
     'Libro_02/nodo_07'),
    ('01_Trinity_Origen/Libro_10/nodo_03.html',
     '<p>Somos una orquesta de ritmos tocando la sinfonía de nuestra existencia.',
     '    <!-- Vuelta de la puerta de Origen II.5 (noviembre de 2026). -->\n'
     '    <p class="viene">Viene de <em>La Voz Interior</em>: la orquesta que '
     '<a class="vuelta" href="../Libro_02/nodo_05.html">el quinto nodo</a> del segundo libro de Origen escucha en las voces '
     'suena aquí en el cuerpo.</p>\n',
     'Libro_02/nodo_05'),
]


def leer(r):
    with open(r, encoding='utf-8', newline='') as f:
        return f.read()


def unico(s, a, ruta):
    if s.count(a) != 1:
        sys.exit('%s: el anclaje aparece %d veces:\n%s' % (ruta, s.count(a), a[:160]))


def main():
    portal, trinity = sys.argv[1], sys.argv[2]
    nuevos = {}

    def cargar(r):
        return nuevos[r] if r in nuevos else leer(r)

    for rel, ancla, nuevo, marca in PORTAL:
        r = os.path.join(portal, rel); s = cargar(r)
        if marca in s:
            print('ya estaba:', rel); continue
        unico(s, ancla, r)
        nuevos[r] = s.replace(ancla, nuevo)

    rel, ancla, nuevo, marca = CSS_CULTIVAR
    r = os.path.join(portal, rel); s = cargar(r)
    if marca in s:
        print('ya estaba el estilo:', rel)
    else:
        unico(s, ancla, r)
        nuevos[r] = s.replace(ancla, nuevo)

    for rel, ancla, linea, marca in VIENE:
        r = os.path.join(trinity, rel); s = cargar(r)
        if marca in s:
            print('ya estaba:', rel); continue
        unico(s, ancla, r)
        i = s.index('</p>', s.index(ancla)) + len('</p>')
        i = s.index('\n', i) + 1
        nuevos[r] = s[:i] + linea + s[i:]

    for r, s in nuevos.items():
        with open(r, 'w', encoding='utf-8', newline='') as f:
            f.write(s)
        print('escrito:', r)
    print('Listo: %d archivos.' % len(nuevos))


if __name__ == '__main__':
    main()
