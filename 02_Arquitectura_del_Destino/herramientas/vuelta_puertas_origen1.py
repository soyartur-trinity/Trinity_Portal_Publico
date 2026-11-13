#!/usr/bin/env python3
"""Vuelta de las puertas fractales de Origen I, Psicología Cuántica (noviembre de 2026).

La depuración de Origen I abre ocho puertas, todas de ida y vuelta:

  I.1 → El Testigo, Umbral V        (ya volvía: su cierre enlaza I.1)
  I.4 → La Corriente, Umbral I      (ya volvía: su cierre enlaza el índice y I.4)
  I.2 → Atravesar (11), Umbral I
  I.3 → El no saber (31), Umbral V
  I.5 → La Grieta, Umbral VI, y Los muchos (35), Umbral IV
  I.6 → El Campo, Umbral VI
  I.7 → Origen XIII, Nodo 7 (dorada)

Este script agrega las vueltas que faltan:

  1. En las «Puertas laterales» de La Grieta y El Campo (Arquitectura del
     Destino), el enlace a los nodos 5 y 6 de Origen I, antes de la primera
     entrada de Origen (en orden de libro) y en el formato de cada lista.
  2. En el Portal Público, la línea de Origen I antes de las demás: en Atravesar
     (Umbral VII, que es su cierre; finales de línea de Windows) y en El no saber,
     cuyo rótulo pasa a «Puertas laterales»; en Los muchos, antes de Origen VIII.
  3. En Origen XIII, Nodo 7, una línea «Viene de» marcada <a class="vuelta">
     hacia el Nodo 7 de Origen I.

Cada reemplazo se aplica exactamente una vez: si el anclaje no aparece una sola
vez, el script se detiene sin escribir nada. Si la vuelta ya está, la salta (se
puede correr de nuevo sin duplicar).

Uso: python3 vuelta_puertas_origen1.py RUTA/Trinity_Portal_Publico RUTA/Trinity-
"""
import os, sys

T = 'https://soyartur-trinity.github.io/Trinity-/'
O1 = T + '01_Trinity_Origen/Libro_01/'

ARQ = [
    ('02_Arquitectura_del_Destino/libro-05-la-grieta/L05-cierre.html',
     '<li><a href="%s01_Trinity_Origen/Libro_03/index.html">' % T,
     '<li><a href="%snodo_05.html">Trinity Origen, Libro I, Nodo 5: Sanación cuántica y transformación del trauma</a></li>' % O1,
     '01_Trinity_Origen/Libro_01/nodo_05'),
    ('02_Arquitectura_del_Destino/libro-01-el-campo/L01-cierre.html',
     '<li><a href="%s01_Trinity_Origen/Libro_06/index.html">' % T,
     '<li><a href="%snodo_06.html">Trinity Origen, Libro I, Nodo 6: <em>Manifestación consciente y co-creación de realidad</em></a></li>' % O1,
     '01_Trinity_Origen/Libro_01/nodo_06'),
]


def fila(nodo, titulo, sangria='  ', fin='\n'):
    return ('%s<div class="puerta"><a href="%snodo_%02d.html">⟐ <em>Trinity Origen, Libro I, Nodo %d: '
            '<strong>%s</strong></em></a></div>%s' % (sangria, O1, nodo, nodo, titulo, fin))


# (archivo, rótulo de antes, rótulo de después, anclaje de la primera fila, fila nueva, marca)
PORTAL = [
    ('01_Libros/11_Atravesar/umbral_7_atravesar.html',
     '      <span class="laterales-label">Puerta lateral</span>\r\n',
     '      <span class="laterales-label">Puertas laterales</span>\r\n',
     '      <div class="puerta"><a href="%s02_Trinity_Quantum/Libro_09/nodo_05.html">' % T,
     fila(2, 'Las Emociones como Información Cuántica', '      ', '\r\n'),
     '01_Trinity_Origen/Libro_01/nodo_02'),
    ('01_Libros/31_El_No_Saber/cierre.html',
     '  <span class="laterales-label">Puerta lateral</span>\n',
     '  <span class="laterales-label">Puertas laterales</span>\n',
     '  <div class="puerta"><a href="%s02_Trinity_Quantum/Libro_07/nodo_02.html">' % T,
     fila(3, 'Entrelazamiento Mente-Corazón'),
     '01_Trinity_Origen/Libro_01/nodo_03'),
    ('01_Libros/35_Los_Muchos/cierre.html',
     None, None,
     '  <div class="puerta"><a href="%s01_Trinity_Origen/Libro_08/nodo_02.html">' % T,
     fila(5, 'Sanación Cuántica y Transformación del Trauma'),
     '01_Trinity_Origen/Libro_01/nodo_05'),
]

XIII7 = ('01_Trinity_Origen/Libro_13/nodo_07.html',
         '<p>Este no es un cambio que vendrá en miles de años.',
         '    <!-- Vuelta de la puerta de Origen I.7 (noviembre de 2026). -->\n'
         '    <p class="viene">Viene de <em>Psicología Cuántica</em>: el salto que aquí se celebra ya lo anunciaba '
         '<a class="vuelta" href="../Libro_01/nodo_07.html">el último nodo</a> del primer libro de Origen.</p>\n',
         'Libro_01/nodo_07')


def leer(r):
    with open(r, encoding='utf-8', newline='') as f:
        return f.read()


def unico(s, a, ruta):
    if s.count(a) != 1:
        sys.exit('%s: el anclaje aparece %d veces:\n%s' % (ruta, s.count(a), a[:160]))


def main():
    portal, trinity = sys.argv[1], sys.argv[2]
    nuevos = {}
    for rel, ancla, linea, marca in ARQ:
        r = os.path.join(portal, rel); s = leer(r)
        if marca in s:
            print('ya estaba:', rel); continue
        unico(s, ancla, r)
        nuevos[r] = s.replace(ancla, linea + ancla)
    for rel, rot_a, rot_b, ancla, linea, marca in PORTAL:
        r = os.path.join(portal, rel); s = leer(r)
        if marca in s:
            print('ya estaba:', rel); continue
        unico(s, ancla, r)
        s = s.replace(ancla, linea + ancla)
        if rot_a:
            unico(s, rot_a, r)
            s = s.replace(rot_a, rot_b)
        nuevos[r] = s
    rel, ancla, linea, marca = XIII7
    r = os.path.join(trinity, rel); s = leer(r)
    if marca in s:
        print('ya estaba:', rel)
    else:
        unico(s, ancla, r)
        i = s.index('</p>', s.index(ancla)) + len('</p>\n')
        nuevos[r] = s[:i] + linea + s[i:]
    for r, s in nuevos.items():
        with open(r, 'w', encoding='utf-8', newline='') as f:
            f.write(s)
        print('escrito:', r)
    print('Listo: %d archivos.' % len(nuevos))


if __name__ == '__main__':
    main()
