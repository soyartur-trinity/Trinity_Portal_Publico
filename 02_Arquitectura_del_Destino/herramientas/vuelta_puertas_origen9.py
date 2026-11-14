#!/usr/bin/env python3
"""Vuelta de las puertas fractales de Origen IX, Liderazgo Consciente (14 de noviembre de 2026).

La depuración completa de Origen IX abre diez puertas, todas de ida y vuelta:

  Índice → La Obra, Umbral I («El llamado»); ya volvía
  IX.1   → La Obra, Umbral III («Sin mí, nada»), y La Grieta, Umbral IV («Noche no es depresión»)
  IX.2   → Los muchos (Portal Público, Libro 35), Umbral II («Orientar sin mandar»)
  IX.3   → Los muchos, Umbral III («La noche de San Juan»)
  IX.4   → La emergencia (Portal Público, Libro 37), Umbral IV («Sin director ni libreto»)
  IX.5   → Origen XI, Nodo 6 (dorada: La Nueva Tierra)
  IX.6   → La Obra, Umbral VI («Empatía que agota, compasión que sostiene»); ya volvía
  IX.7   → La Obra, Umbral V («El algarrobo»), y Origen XI, Nodo 1 (dorada: Gaia como Ser Viviente)

Este script agrega las vueltas que faltan:

  1. En las «Puertas laterales» de La Obra y La Grieta (Arquitectura del Destino),
     el enlace al nodo de Origen IX, en el orden de cada lista y en su formato
     (en La Obra, junto a las entradas de Origen IX que ya estaban).
  2. En el cierre de Los muchos y de La emergencia (Portal Público), las filas de
     Origen IX después de las de Origen y antes de las de Quantum.
  3. En Origen XI.1 y XI.6, una línea «Viene de» marcada <a class="vuelta">.

Cada reemplazo se aplica exactamente una vez: si el anclaje no aparece una sola
vez, el script se detiene sin escribir nada. Si la vuelta ya está, la salta (se
puede correr de nuevo sin duplicar).

Uso: python3 vuelta_puertas_origen9.py RUTA/Trinity_Portal_Publico RUTA/Trinity-
"""
import os, sys

T = 'https://soyartur-trinity.github.io/Trinity-/'
O9 = T + '01_Trinity_Origen/Libro_09/'
MARCA = '01_Trinity_Origen/Libro_09/nodo_%02d'

AD = '02_Arquitectura_del_Destino/'


def li(nodo, titulo, em=False):
    t = '<em>%s</em>' % titulo if em else titulo
    return '<li><a href="%snodo_%02d.html">Trinity Origen, Libro IX, Nodo %d: %s</a></li>' % (O9, nodo, nodo, t)


# (archivo, anclaje: la entrada antes de la cual va la nueva, línea nueva, marca)
ARQ = [
    (AD + 'libro-12-la-obra/L12-cierre.html',
     '<li><a href="%s01_Trinity_Origen/Libro_09/nodo_06.html">' % T,
     li(1, 'La Muerte del Líder-Ego', em=True), MARCA % 1),
    (AD + 'libro-12-la-obra/L12-cierre.html',
     '<li><a href="%s01_Trinity_Origen/Libro_06/nodo_04.html">' % T,
     li(7, 'Liderazgo al Servicio de la Vida', em=True), MARCA % 7),
    (AD + 'libro-05-la-grieta/L05-cierre.html',
     '<li><a href="%s01_Trinity_Origen/Libro_13/nodo_02.html">' % T,
     li(1, 'La Muerte del Líder-Ego'), MARCA % 1),
]


def fila(nodo, titulo):
    return ('  <div class="puerta"><a href="%snodo_%02d.html">⟐ <em>Trinity Origen, Libro IX, Nodo %d: '
            '<strong>%s</strong></em></a></div>\n' % (O9, nodo, nodo, titulo))


# (archivo, anclaje: la primera fila de Quantum, filas nuevas, marca)
PORTAL = [
    ('01_Libros/35_Los_Muchos/cierre.html',
     '  <div class="puerta"><a href="%s02_Trinity_Quantum/Libro_10/nodo_04.html">' % T,
     fila(2, 'Liderazgo Holárquico') + fila(3, 'Tecnologías de Coherencia Colectiva'), MARCA % 2),
    ('01_Libros/37_La_Emergencia/cierre.html',
     '  <div class="puerta"><a href="%s02_Trinity_Quantum/Libro_05/nodo_03.html">' % T,
     fila(4, 'Liderazgo desde el Vacío'), MARCA % 4),
]

# (archivo, anclaje: el párrafo después del cual va la línea, línea nueva, marca)
VIENE = [
    ('01_Trinity_Origen/Libro_11/nodo_01.html',
     '<p>Ninguno de estos números lo <strong>calibró</strong> alguien, y en eso está el asombro.',
     '    <!-- Vuelta de la puerta de Origen IX.7 (noviembre de 2026). -->\n'
     '    <p class="viene">Viene de <em>Liderazgo Consciente</em>: la Tierra que '
     '<a class="vuelta" href="../Libro_09/nodo_07.html">el último nodo</a> del noveno libro de Origen sienta en la mesa '
     'de cada decisión es la misma que aquí se mira como un ser vivo.</p>\n',
     'Libro_09/nodo_07'),
    ('01_Trinity_Origen/Libro_11/nodo_06.html',
     '<p>John Maynard Keynes lo imaginó en 1930:',
     '    <!-- Vuelta de la puerta de Origen IX.5 (noviembre de 2026). -->\n'
     '    <p class="viene">Viene de <em>Liderazgo Consciente</em>: las economías que miden la riqueza en salud, en tiempo '
     'y en vínculos, que se ensayan en <a class="vuelta" href="../Libro_09/nodo_05.html">el quinto nodo</a> del noveno '
     'libro de Origen, se vuelven aquí la vida de todos los días.</p>\n',
     'Libro_09/nodo_05'),
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
