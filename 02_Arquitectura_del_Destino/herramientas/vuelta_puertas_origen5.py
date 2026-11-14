#!/usr/bin/env python3
"""Vuelta de las puertas fractales de Origen V, Los Vínculos Sagrados (14 de noviembre de 2026).

La depuración completa de Origen V abre diez puertas, todas de ida y vuelta:

  índice → La Red, Umbral I («Una pregunta sin respuesta»)
  V.1 → La Voz Interior (Portal Público, Libro 2), capítulo 5 («La actitud del diálogo»)
  V.2 → Encuentro Real (Portal Público, Libro 3), Territorio 3 («Tolerancia al otro real»)
  V.3 → Encuentro Real, Territorio 1 («Proyecciones cruzadas»),
        y Quantum 2, Nodo 2 (violeta: Almas Entrelazadas Cuánticamente)
  V.4 → El Personaje, Umbral II («Detrás de cada máscara»)
  V.5 → La Red, Umbral VI («La red te sostiene»)
  V.6 → Origen XI, Nodo 3 (dorada: El Campo Unificado de Consciencia)
  V.7 → Origen XIII, Nodo 1 (dorada: La Gran Amnesia),
        y Las Pequeñas Muertes, Umbral III («Lo que encontraron en Harvard»)

El cierre de La Red ya enlazaba el índice de Origen V y su Nodo 5: esas dos vuelven solas.
Este script agrega las otras:

  1. En las «Puertas laterales» de El Personaje (pasa de ocho a nueve, decisión de Arturo)
     y de Las Pequeñas Muertes, el enlace al nodo de Origen V, en el orden de cada lista.
  2. En el bloque «Puertas laterales» del epílogo de La Voz Interior y del cierre de
     Encuentro Real (Portal Público), las filas de Origen V antes de la de Quantum; el
     rótulo pasa de «Puerta lateral» a «Puertas laterales».
  3. En Quantum 2.2, Origen XI.3 y Origen XIII.1, una línea «Viene de» marcada <a class="vuelta">.

Cada reemplazo se aplica exactamente una vez: si el anclaje no aparece una sola
vez, el script se detiene sin escribir nada. Si la vuelta ya está, la salta (se
puede correr de nuevo sin duplicar).

Uso: python3 vuelta_puertas_origen5.py RUTA/Trinity_Portal_Publico RUTA/Trinity-
"""
import os, sys

T = 'https://soyartur-trinity.github.io/Trinity-/'
O5 = T + '01_Trinity_Origen/Libro_05/'
MARCA = '01_Trinity_Origen/Libro_05/nodo_%02d'

AD = '02_Arquitectura_del_Destino/'


def li(nodo, titulo):
    return '<li><a href="%snodo_%02d.html">Trinity Origen, Libro V, Nodo %d: %s</a></li>' % (O5, nodo, nodo, titulo)


# (archivo, anclaje: la entrada antes de la cual va la nueva, línea nueva, marca)
ARQ = [
    (AD + 'libro-09-el-personaje/L09-cierre.html',
     '<li><a href="%s01_Trinity_Origen/Libro_06/nodo_01.html">' % T,
     li(4, 'Vínculos de Sombra y Sanación'), MARCA % 4),
    (AD + 'libro-06-las-pequenas-muertes/L06-cierre.html',
     '<li><a href="%s01_Trinity_Origen/Libro_06/nodo_02.html">' % T,
     li(7, 'Ritual de Reconexión'), MARCA % 7),
]


def fila(sangria, nodo, titulo):
    return ('%s<div class="puerta"><a href="%snodo_%02d.html">⟐ <em>Trinity Origen, Libro V, Nodo %d: '
            '<strong>%s</strong></em></a></div>\n' % (sangria, O5, nodo, nodo, titulo))


# (archivo, sangría, filas nuevas, marca): las filas van antes de la fila de Quantum,
# y el rótulo pasa a plural.
PORTAL = [
    ('01_Libros/02_La_Voz_Interior/epilogo.html', '      ',
     [(1, 'El Vínculo Primordial')], MARCA % 1),
    ('01_Libros/03_Encuentro_Real/cierre.html', '              ',
     [(2, 'Los Puentes del Corazón'), (3, 'Contratos y Pactos Invisibles')], MARCA % 2),
]
RO_SING = '<span class="laterales-label">Puerta lateral</span>'
RO_PLUR = '<span class="laterales-label">Puertas laterales</span>'
QUANTUM = '<div class="puerta"><a href="%s02_Trinity_Quantum/' % T

# (archivo, anclaje: el párrafo después del cual va la línea, línea nueva, marca)
VIENE = [
    ('02_Trinity_Quantum/Libro_02/nodo_02.html',
     '<p>Hay seres con los que compartes un entrelazamiento',
     '      <!-- Vuelta de la puerta de Origen V.3 (noviembre de 2026). -->\n'
     '      <p class="viene">Viene de <em>Los Vínculos Sagrados</em>: el «ya te conozco» de los contratos del alma, en '
     '<a class="vuelta" href="../../01_Trinity_Origen/Libro_05/nodo_03.html">el tercer nodo</a> del quinto libro de Origen, '
     'se mira aquí desde la física.</p>\n',
     'Libro_05/nodo_03'),
    ('01_Trinity_Origen/Libro_11/nodo_03.html',
     '<p>Dante la escribió en el último verso de su <em>Comedia</em>',
     '    <!-- Vuelta de la puerta de Origen V.6 (noviembre de 2026). -->\n'
     '    <p class="viene">Viene de <em>Los Vínculos Sagrados</em>: el amor como fuerza que estructura el cosmos, en '
     '<a class="vuelta" href="../Libro_05/nodo_06.html">el sexto nodo</a> del quinto libro de Origen, encuentra aquí su verso.</p>\n',
     'Libro_05/nodo_06'),
    ('01_Trinity_Origen/Libro_13/nodo_01.html',
     '<p class="viene">Viene de <em>La Civilización Galáctica</em>',
     '    <!-- Vuelta de la puerta de Origen V.7 (noviembre de 2026). -->\n'
     '    <p class="viene">Viene de <em>Los Vínculos Sagrados</em>: la separación que '
     '<a class="vuelta" href="../Libro_05/nodo_07.html">el ritual de reconexión</a>, al cierre del quinto libro de Origen, '
     'llama ilusión necesaria es este mismo olvido.</p>\n',
     'Libro_05/nodo_07'),
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

    for rel, ancla, linea, marca in ARQ:
        r = os.path.join(portal, rel); s = leer(r)
        if marca in s:
            print('ya estaba:', rel); continue
        unico(s, ancla, r)
        nuevos[r] = s.replace(ancla, linea + ancla)

    for rel, sangria, filas, marca in PORTAL:
        r = os.path.join(portal, rel); s = leer(r)
        if marca in s:
            print('ya estaba:', rel); continue
        unico(s, RO_SING, r)
        ancla = sangria + QUANTUM
        unico(s, ancla, r)
        s = s.replace(RO_SING, RO_PLUR)
        s = s.replace(ancla, ''.join(fila(sangria, n, t) for n, t in filas) + ancla)
        nuevos[r] = s

    for rel, ancla, linea, marca in VIENE:
        r = os.path.join(trinity, rel); s = leer(r)
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
