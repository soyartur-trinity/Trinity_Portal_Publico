#!/usr/bin/env python3
"""Vuelta de las puertas fractales de Origen XII, La Civilización Galáctica (14 de noviembre de 2026).

La depuración completa de Origen XII abre diez puertas, todas de ida y vuelta:

  XII.1 → Origen XI, Nodo 5 (dorada: Colaboración Cósmica)
  XII.2 → El Testigo, Umbral V («El maestro de la pregunta»)
  XII.3 → Lo que se recibe (Portal Público, Libro 38), Umbral II («El que se dice elegido»),
          y La Red, Umbral I («Los más conectados»)
  XII.4 → Origen X, Nodo 7 (dorada: La Gran Síntesis)
  XII.5 → Lo que se recibe, Umbral IV («El regalo tiene que moverse»),
          y Origen IX, Nodo 5 (dorada: Economías de la Consciencia)
  XII.6 → Habitar, Umbral I («Un castillo de cristal»)
  XII.7 → El Cuerpo, Umbral VI («Lo que los ángeles no conocen»),
          y Origen XIII, Nodo 1 (dorada: La Gran Amnesia)

Este script agrega las vueltas:

  1. En las «Puertas laterales» de El Testigo, La Red y El Cuerpo (Arquitectura del Destino),
     el enlace al nodo de Origen XII, en el orden de cada lista y en su formato
     (título en cursiva solo en El Cuerpo).
  2. En Habitar, que ya tiene nueve puertas laterales (el máximo de la serie), una línea
     discreta «Viene de Trinity Origen» debajo de la de Quantum (decisión de Arturo).
  3. En el cierre de Lo que se recibe (Portal Público), las dos filas de Origen XII
     después de la de Origen XI y antes de las de Quantum.
  4. En Origen XI.5, X.7, IX.5 y XIII.1, una línea «Viene de» marcada <a class="vuelta">.

Cada reemplazo se aplica exactamente una vez: si el anclaje no aparece una sola
vez, el script se detiene sin escribir nada. Si la vuelta ya está, la salta (se
puede correr de nuevo sin duplicar).

Uso: python3 vuelta_puertas_origen12.py RUTA/Trinity_Portal_Publico RUTA/Trinity-
"""
import os, sys

T = 'https://soyartur-trinity.github.io/Trinity-/'
O12 = T + '01_Trinity_Origen/Libro_12/'
MARCA = '01_Trinity_Origen/Libro_12/nodo_%02d'

AD = '02_Arquitectura_del_Destino/'


def li(nodo, titulo, em=False):
    t = '<em>%s</em>' % titulo if em else titulo
    return '<li><a href="%snodo_%02d.html">Trinity Origen, Libro XII, Nodo %d: %s</a></li>' % (O12, nodo, nodo, t)


# (archivo, anclaje: la entrada antes de la cual va la nueva, línea nueva, marca)
ARQ = [
    (AD + 'libro-03-el-testigo/L03-cierre.html',
     '<li><a href="%s01_Trinity_Origen/Libro_13/nodo_01.html">' % T,
     li(2, 'El Protocolo de Contacto Interior'), MARCA % 2),
    (AD + 'libro-11-la-red/L11-cierre.html',
     '<li><a href="%s02_Trinity_Quantum/Libro_04/nodo_02.html">' % T,
     li(3, 'Los Embajadores de la Humanidad'), MARCA % 3),
    (AD + 'libro-04-el-cuerpo/L04-cierre.html',
     '<li><a href="%s01_Trinity_Origen/Libro_13/nodo_06.html">' % T,
     li(7, 'La Graduación Cósmica', em=True), MARCA % 7),
]

# Habitar: la vuelta va después de la línea de Quantum, en una línea propia.
HABITAR = (AD + 'libro-13-habitar/L13-cierre.html',
           'El Diccionario Holográfico</a></li></ul></div>',
           '<div class="vienen"><p class="vienen-t">Viene de <em>Trinity Origen</em></p><ul>'
           '<li><a class="vuelta" href="%snodo_06.html">Libro XII, Nodo 6: Las Ciudades de Luz</a></li></ul></div>' % O12,
           MARCA % 6)


def fila(nodo, titulo):
    return ('  <div class="puerta"><a href="%snodo_%02d.html">⟐ <em>Trinity Origen, Libro XII, Nodo %d: '
            '<strong>%s</strong></em></a></div>\n' % (O12, nodo, nodo, titulo))


# (archivo, anclaje: la primera fila de Quantum, filas nuevas, marca)
PORTAL = [
    ('01_Libros/38_Lo_Que_Se_Recibe/cierre.html',
     '  <div class="puerta"><a href="%s02_Trinity_Quantum/Libro_06/nodo_06.html">' % T,
     fila(3, 'Los Embajadores de la Humanidad') + fila(5, 'La Economía Galáctica'), MARCA % 3),
]

# (archivo, anclaje: el párrafo después del cual va la línea, línea nueva, marca)
VIENE = [
    ('01_Trinity_Origen/Libro_11/nodo_05.html',
     '<p>Nadie sabe el día ni la hora.',
     '    <!-- Vuelta de la puerta de Origen XII.1 (noviembre de 2026). -->\n'
     '    <p class="viene">Viene de <em>La Civilización Galáctica</em>: la cuarentena que se levanta en '
     '<a class="vuelta" href="../Libro_12/nodo_01.html">el primer nodo</a> del duodécimo libro de Origen '
     'termina ante la misma puerta abierta.</p>\n',
     'Libro_12/nodo_01'),
    ('01_Trinity_Origen/Libro_10/nodo_07.html',
     '<p>Este es el horizonte.',
     '    <!-- Vuelta de la puerta de Origen XII.4 (noviembre de 2026). -->\n'
     '    <p class="viene">Viene de <em>La Civilización Galáctica</em>: las tecnologías estelares que sueña '
     '<a class="vuelta" href="../Libro_12/nodo_04.html">el cuarto nodo</a> del duodécimo libro de Origen '
     'encuentran aquí, en el cuerpo, su primer paso.</p>\n',
     'Libro_12/nodo_04'),
    ('01_Trinity_Origen/Libro_09/nodo_05.html',
     '<p>Por todo el planeta, experimentos económicos están probando que otro mundo es posible.</p>',
     '    <!-- Vuelta de la puerta de Origen XII.5 (noviembre de 2026). -->\n'
     '    <p class="viene">Viene de <em>La Civilización Galáctica</em>: la economía de la abundancia que sueña '
     '<a class="vuelta" href="../Libro_12/nodo_05.html">el quinto nodo</a> del duodécimo libro de Origen '
     'tiene aquí sus laboratorios.</p>\n',
     'Libro_12/nodo_05'),
    ('01_Trinity_Origen/Libro_13/nodo_01.html',
     '<p class="lead">Hay un momento, justo antes de encarnar,',
     '    <!-- Vuelta de la puerta de Origen XII.7 (noviembre de 2026). -->\n'
     '    <p class="viene">Viene de <em>La Civilización Galáctica</em>: el aula Tierra de '
     '<a class="vuelta" href="../Libro_12/nodo_07.html">la graduación cósmica</a>, al cierre del duodécimo '
     'libro de Origen, empieza por este olvido.</p>\n',
     'Libro_12/nodo_07'),
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

    def antes(r, ancla, linea, marca, base):
        s = nuevos.get(r) or leer(r)
        if marca in s:
            print('ya estaba:', os.path.relpath(r, base), marca[-7:]); return
        unico(s, ancla, r)
        nuevos[r] = s.replace(ancla, linea + ancla)

    for rel, ancla, linea, marca in ARQ:
        antes(os.path.join(portal, rel), ancla, linea, marca, portal)
    for rel, ancla, linea, marca in PORTAL:
        antes(os.path.join(portal, rel), ancla, linea, marca, portal)

    rel, ancla, linea, marca = HABITAR
    r = os.path.join(portal, rel); s = nuevos.get(r) or leer(r)
    if marca in s:
        print('ya estaba:', rel)
    else:
        unico(s, ancla, r)
        nuevos[r] = s.replace(ancla, ancla + linea)

    for rel, ancla, linea, marca in VIENE:
        r = os.path.join(trinity, rel); s = nuevos.get(r) or leer(r)
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
