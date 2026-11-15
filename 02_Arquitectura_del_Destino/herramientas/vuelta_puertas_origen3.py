#!/usr/bin/env python3
"""Vuelta de las puertas fractales de Origen III, El Dolor como Portal (15 de noviembre de 2026).

La depuración completa de Origen III abre trece puertas, todas de ida y vuelta:

  índice → La Grieta, Umbral III («Acompañar sin apurar»)
  III.1 → La Grieta, Umbral I («Lo que se rompe no siempre termina algo»),
          y El Duelo (Portal Público, Libro 5), nodo 1 («La Primera Grieta»)
  III.2 → La Grieta, Umbral II («La muchacha que no podía contarlo»),
          y Origen I, Nodo 5 (dorada: Sanación Cuántica y Transformación del Trauma)
  III.3 → La Grieta, Umbral IV («El madero»), y Origen XI, Nodo 4 (dorada: La Gran Transición)
  III.4 → El Testigo, Umbral III («Las cualidades del que mira»)
  III.5 → La Grieta, Umbral V («Sentir sin hundirse»), y Origen XI, Nodo 1 (dorada: Gaia como Ser Viviente)
  III.6 → La Grieta, Umbral VI («Cinco señales»)
  III.7 → La Grieta, Umbral VI («El fin de la guerra»), y Quantum 9, Nodo 5 (violeta: La Grieta Donde Entra la Luz)

El cierre de La Grieta ya enlazaba el índice de Origen III y su Nodo 7: esas dos vuelven solas.
Este script agrega las otras:

  1. En el cierre de La Grieta, debajo de «Vienen de Trinity Quantum», una línea discreta
     «Vienen de Trinity Origen» con los nodos 1, 2, 3, 5 y 6 (decisión de Arturo: la lista
     «Puertas laterales», que tiene ocho, queda intacta, como en Habitar).
  2. En las «Puertas laterales» de El Testigo (pasa de siete a ocho), el Nodo 4, después de
     Origen I, Nodo 1.
  3. En el bloque del nodo 12 de El Duelo (Portal Público), la fila de Origen III antes de la de
     Origen VII; el rótulo pasa de «Puerta lateral» a «Puertas laterales».
  4. En Origen I.5, Origen XI.4, Origen XI.1 y Quantum 9.5, una línea «Viene de» marcada <a class="vuelta">.

Además, dos correcciones de paso en Trinity-:
  - Origen XI.4: Joanna Macy murió en julio de 2025; «que lleva décadas acompañando» pasa a
    «que acompañó durante décadas».
  - Índice de Trinity Origen: «El Dolor Como Portal» pasa a «El Dolor como Portal».

Cada reemplazo se aplica exactamente una vez: si el anclaje no aparece una sola
vez, el script se detiene sin escribir nada. Si la vuelta ya está, la salta (se
puede correr de nuevo sin duplicar).

Uso: python3 vuelta_puertas_origen3.py RUTA/Trinity_Portal_Publico RUTA/Trinity-
"""
import os, sys

T = 'https://soyartur-trinity.github.io/Trinity-/'
O3 = T + '01_Trinity_Origen/Libro_03/'
AD = '02_Arquitectura_del_Destino/'


def vuelta_li(nodo, titulo):
    return '<li><a class="vuelta" href="%snodo_%02d.html">Libro III, Nodo %d: %s</a></li>' % (O3, nodo, nodo, titulo)


GRIETA = (AD + 'libro-05-la-grieta/L05-cierre.html',
          '</ul></div><section class="notas"',
          '</ul></div><div class="vienen"><p class="vienen-t">Vienen de <em>Trinity Origen</em></p><ul>'
          + vuelta_li(1, 'La Primera Grieta')
          + vuelta_li(2, 'El Trauma como Memoria Suspendida')
          + vuelta_li(3, 'El Fuego del Dolor')
          + vuelta_li(5, 'Dolor Colectivo, Dolor Planetario')
          + vuelta_li(6, 'Reconfiguración')
          + '</ul></div><section class="notas"',
          'Libro_03/nodo_01')

TESTIGO = (AD + 'libro-03-el-testigo/L03-cierre.html',
           '<li><a href="%s01_Trinity_Origen/Libro_10/nodo_04.html">' % T,
           '<li><a href="%snodo_04.html">Trinity Origen, Libro III, Nodo 4: El Silencio que el Dolor Revela</a></li>' % O3,
           'Libro_03/nodo_04')

DUELO = ('01_Libros/05_Duelo/duelo_nodo_12.html',
         '    <div class="puerta"><a href="%s01_Trinity_Origen/Libro_07/nodo_04.html">' % T,
         '    <div class="puerta"><a href="%snodo_01.html">⟐ <em>Trinity Origen, Libro III, Nodo 1: '
         '<strong>La Primera Grieta</strong></em></a></div>\n' % O3,
         'Libro_03/nodo_01')
RO_SING = '<span class="laterales-label">Puerta lateral</span>'
RO_PLUR = '<span class="laterales-label">Puertas laterales</span>'

# (archivo, anclaje: el párrafo después del cual va la línea, línea nueva, marca)
VIENE = [
    ('01_Trinity_Origen/Libro_01/nodo_05.html',
     '<p>Así trabajan Peter Levine, que llamó titulación',
     '    <!-- Vuelta de la puerta de Origen III.2 (noviembre de 2026). -->\n'
     '    <p class="viene">Viene de <em>El Dolor como Portal</em>: la memoria suspendida que '
     '<a class="vuelta" href="../Libro_03/nodo_02.html">el segundo nodo</a> del tercer libro de Origen pide escuchar sin '
     'apuro se acerca aquí de a gotas.</p>\n',
     'Libro_03/nodo_02'),
    ('01_Trinity_Origen/Libro_11/nodo_04.html',
     '<p>La biología guarda una sorpresa para esta imagen.',
     '    <!-- Vuelta de la puerta de Origen III.3 (noviembre de 2026). -->\n'
     '    <p class="viene">Viene de <em>El Dolor como Portal</em>: la crisálida en llamas del '
     '<a class="vuelta" href="../Libro_03/nodo_03.html">fuego del dolor</a>, en el tercer libro de Origen, es la misma que '
     'aquí guarda la memoria de la oruga.</p>\n',
     'Libro_03/nodo_03'),
    ('01_Trinity_Origen/Libro_11/nodo_01.html',
     '<p>Quien lee esto con miedo por el planeta no está solo.',
     '    <!-- Vuelta de la puerta de Origen III.5 (noviembre de 2026). -->\n'
     '    <p class="viene">Viene de <em>El Dolor como Portal</em>: la Tierra que siente y sufre con nosotros, en '
     '<a class="vuelta" href="../Libro_03/nodo_05.html">el quinto nodo</a> del tercer libro de Origen, encuentra aquí su '
     'ciencia y su cuidado.</p>\n',
     'Libro_03/nodo_05'),
    ('02_Trinity_Quantum/Libro_09/nodo_05.html',
     '<p>La luz que entra por tus grietas no viene de afuera.',
     '        <!-- Vuelta de la puerta de Origen III.7 (noviembre de 2026). -->\n'
     '        <p class="viene">Viene de <em>Trinity Origen</em>: «siempre fuimos luz, solo que brillábamos desde la herida», '
     'escribe <a class="vuelta" href="../../01_Trinity_Origen/Libro_03/nodo_07.html">el último nodo de <em>El Dolor como '
     'Portal</em></a>; aquí es la misma luz, entrando por la grieta.</p>\n',
     'Libro_03/nodo_07'),
]

# (archivo, viejo, nuevo): correcciones de paso, cada una una sola vez
CORRECCIONES = [
    ('01_Trinity_Origen/Libro_11/nodo_04.html',
     '<p>Joanna Macy, que lleva décadas acompañando a quienes sienten el dolor del mundo, no cuenta este tiempo',
     '<!-- Corrección del 15 de noviembre de 2026: Joanna Macy murió en julio de 2025. -->\n'
     '    <p>Joanna Macy, que acompañó durante décadas a quienes sienten el dolor del mundo, no cuenta este tiempo'),
    ('01_Trinity_Origen/index.html',
     '<h2 class="libro-titulo">El Dolor Como Portal</h2>',
     '<h2 class="libro-titulo">El Dolor como Portal</h2>'),
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

    for rel, ancla, nuevo, marca in (GRIETA,):
        r = os.path.join(portal, rel); s = cargar(r)
        if marca in s:
            print('ya estaba:', rel)
        else:
            unico(s, ancla, r)
            nuevos[r] = s.replace(ancla, nuevo)

    rel, ancla, linea, marca = TESTIGO
    r = os.path.join(portal, rel); s = cargar(r)
    if marca in s:
        print('ya estaba:', rel)
    else:
        unico(s, ancla, r)
        nuevos[r] = s.replace(ancla, linea + ancla)

    rel, ancla, fila, marca = DUELO
    r = os.path.join(portal, rel); s = cargar(r)
    if marca in s:
        print('ya estaba:', rel)
    else:
        unico(s, ancla, r); unico(s, RO_SING, r)
        nuevos[r] = s.replace(RO_SING, RO_PLUR).replace(ancla, fila + ancla)

    for rel, ancla, linea, marca in VIENE:
        r = os.path.join(trinity, rel); s = cargar(r)
        if marca in s:
            print('ya estaba:', rel); continue
        unico(s, ancla, r)
        i = s.index('</p>', s.index(ancla)) + len('</p>')
        i = s.index('\n', i) + 1
        nuevos[r] = s[:i] + linea + s[i:]

    for rel, viejo, nuevo in CORRECCIONES:
        r = os.path.join(trinity, rel); s = cargar(r)
        if nuevo in s:
            print('ya estaba:', rel); continue
        unico(s, viejo, r)
        nuevos[r] = s.replace(viejo, nuevo)

    for r, s in nuevos.items():
        with open(r, 'w', encoding='utf-8', newline='') as f:
            f.write(s)
        print('escrito:', r)
    print('Listo: %d archivos.' % len(nuevos))


if __name__ == '__main__':
    main()
