#!/usr/bin/env python3
"""Vuelta de las puertas fractales de Origen XI, La Consciencia Planetaria (noviembre de 2026).

La depuración de Origen XI abre diez puertas, todas de ida y vuelta:

  XI.1 → Trinity Quantum, Libro 2, Nodo 7 (La Red Cuántica de Gaia)
  XI.2 → La Red, Umbral II, y La Corriente, Umbral III
  XI.3 → Lo que se recibe (38), Umbral I
  XI.4 → No saber, Umbral III
  XI.5 → Ídolo (17), Umbral 0, y El Sonámbulo, Umbral II
  XI.6 → El campo (39), Umbral II, y Origen VIII, Nodo 7 (dorada)
  XI.7 → La Obra, Umbral V

Este script agrega las vueltas:

  1. En las «Puertas laterales» de El Sonámbulo, No saber, La Corriente, La Red
     y La Obra (Arquitectura del Destino), el enlace al nodo de Origen XI, después
     de las entradas de Origen que ya estaban (en orden de libro) y en el formato
     de cada lista.
  2. En el Portal Público, la línea de Origen XI antes de las de Quantum en
     Lo que se recibe y en El campo; en Ídolo, que no tenía, un bloque nuevo
     «Puerta lateral» con la paleta del de El ayudante.
  3. En Trinity Quantum 2.7 y en Origen VIII.7, una línea «Viene de» marcada
     <a class="vuelta"> hacia el nodo de Origen XI que las abre.

Cada reemplazo se aplica exactamente una vez: si el anclaje no aparece una sola
vez, el script se detiene sin escribir nada. Si la vuelta ya está, la salta (se
puede correr de nuevo sin duplicar).

Uso: python3 vuelta_puertas_origen11.py RUTA/Trinity_Portal_Publico RUTA/Trinity-
"""
import os, sys

T = 'https://soyartur-trinity.github.io/Trinity-/'
O11 = T + '01_Trinity_Origen/Libro_11/'
MARCA = '01_Trinity_Origen/Libro_11/nodo_%02d'

AD = '02_Arquitectura_del_Destino/'


def li(nodo, titulo, em=False):
    t = '<em>%s</em>' % titulo if em else titulo
    return '<li><a href="%snodo_%02d.html">Trinity Origen, Libro XI, Nodo %d: %s</a></li>' % (O11, nodo, nodo, t)


# (archivo, anclaje: la entrada que sigue a la última de Origen, línea nueva, marca)
ARQ = [
    (AD + 'libro-02-el-sonambulo/L02-cierre.html',
     '<li><a href="%s00_Portal_Trinity/nodo_13.html">' % T,
     li(5, 'Colaboración Cósmica'), MARCA % 5),
    (AD + 'libro-07-no-saber/L07-cierre.html',
     '<li><a href="%sTrinity_Infinito/Libro7/L7-Nodo1.html">' % T,
     li(4, 'La Gran Transición'), MARCA % 4),
    (AD + 'libro-10-la-corriente/L10-cierre.html',
     '<li><a href="%s02_Trinity_Quantum/Libro_10/index.html">' % T,
     li(2, 'La Red de Consciencias Despiertas'), MARCA % 2),
    (AD + 'libro-11-la-red/L11-cierre.html',
     '<li><a href="%s02_Trinity_Quantum/Libro_04/nodo_02.html">' % T,
     li(2, 'La Red de Consciencias Despiertas'), MARCA % 2),
    (AD + 'libro-12-la-obra/L12-cierre.html',
     '<li><a href="%sTrinity_Infinito/Libro_10/L_10-Nodo1.html">' % T,
     li(7, 'El Servicio Planetario', em=True), MARCA % 7),
]


def fila(nodo, titulo):
    return ('  <div class="puerta"><a href="%snodo_%02d.html">⟐ <em>Trinity Origen, Libro XI, Nodo %d: '
            '<strong>%s</strong></em></a></div>\n' % (O11, nodo, nodo, titulo))


# (archivo, anclaje: la primera fila de Quantum, fila nueva, marca)
PORTAL = [
    ('01_Libros/38_Lo_Que_Se_Recibe/cierre.html',
     '  <div class="puerta"><a href="%s02_Trinity_Quantum/Libro_06/nodo_06.html">' % T,
     fila(3, 'El Campo Unificado de Consciencia'), MARCA % 3),
    ('01_Libros/39_El_Campo/cierre.html',
     '  <div class="puerta"><a href="%s02_Trinity_Quantum/Libro_07/nodo_07.html">' % T,
     fila(6, 'La Nueva Tierra'), MARCA % 6),
]

# Ídolo no tenía puertas laterales: estilo y bloque nuevos, como en El ayudante.
IDOLO = '01_Libros/17_Idolo/cierre.html'
IDOLO_CSS = (
    '\n  /* Puertas laterales (noviembre de 2026): vuelta de las puertas fractales de Trinity */\n'
    '  .laterales{margin:4.6rem 0 0;}\n'
    "  .laterales-label{display:block; font-family:'Cormorant Garamond',serif; font-size:.66rem;\n"
    '    letter-spacing:.35em; text-transform:uppercase; color:var(--oro-tenue); margin-bottom:1.5rem;}\n'
    '  .laterales .puerta{margin:0 0 1.2rem;}\n'
    '  .laterales .puerta a{color:#a88a4e;}\n'
    '  .laterales .puerta a:hover, .laterales .puerta a:focus-visible{color:var(--oro);}\n'
    '</style>')
IDOLO_BLOQUE = (
    '<div class="laterales">\n'
    '  <span class="laterales-label">Puerta lateral</span>\n'
    + fila(5, 'Colaboración Cósmica') +
    '</div>\n\n'
    '<div class="continuar">')

# (archivo, anclaje: el párrafo después del cual va la línea, línea nueva, marca)
VIENE = [
    ('02_Trinity_Quantum/Libro_02/nodo_07.html',
     '<p>La red de Gaia no necesita lo instantáneo para asombrar.',
     '            <!-- Vuelta de la puerta de Origen XI.1 (noviembre de 2026). -->\n'
     '            <p class="viene">Viene de <em>La Consciencia Planetaria</em>: este mismo planeta vivo abre '
     '<a class="vuelta" href="../../01_Trinity_Origen/Libro_11/nodo_01.html">el primer nodo</a> '
     'del undécimo libro de Origen.</p>\n\n',
     'Libro_11/nodo_01'),
    ('01_Trinity_Origen/Libro_08/nodo_07.html',
     '<p><em>De celebrar el genio individual a tejer la red de consciencia planetaria.</em></p>',
     '    <!-- Vuelta de la puerta de Origen XI.6 (noviembre de 2026). -->\n'
     '    <p class="viene">Viene de <em>La Consciencia Planetaria</em>: la Nueva Tierra que se sueña en '
     '<a class="vuelta" href="../Libro_11/nodo_06.html">el sexto nodo</a> del undécimo libro de Origen '
     'aprende aquí a hacer escuela.</p>\n',
     'Libro_11/nodo_06'),
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

    def antes(r, ancla, linea, marca):
        s = nuevos.get(r) or leer(r)
        if marca in s:
            print('ya estaba:', os.path.relpath(r, portal)); return
        unico(s, ancla, r)
        nuevos[r] = s.replace(ancla, linea + ancla)

    for rel, ancla, linea, marca in ARQ:
        antes(os.path.join(portal, rel), ancla, linea, marca)
    for rel, ancla, linea, marca in PORTAL:
        antes(os.path.join(portal, rel), ancla, linea, marca)

    r = os.path.join(portal, IDOLO); s = leer(r)
    if MARCA % 5 in s:
        print('ya estaba:', IDOLO)
    else:
        for a in ('</style>', '<div class="continuar">'):
            unico(s, a, r)
        s = s.replace('</style>', IDOLO_CSS)
        s = s.replace('<div class="continuar">', IDOLO_BLOQUE)
        nuevos[r] = s

    for rel, ancla, linea, marca in VIENE:
        r = os.path.join(trinity, rel); s = leer(r)
        if marca in s:
            print('ya estaba:', rel); continue
        unico(s, ancla, r)
        i = s.index('</p>', s.index(ancla)) + len('</p>')
        i = s.index('\n', i) + 1
        if linea.endswith('\n\n') and s[i:i + 1] == '\n':
            i += 1
        nuevos[r] = s[:i] + linea + s[i:]

    for r, s in nuevos.items():
        with open(r, 'w', encoding='utf-8', newline='') as f:
            f.write(s)
        print('escrito:', r)
    print('Listo: %d archivos.' % len(nuevos))


if __name__ == '__main__':
    main()
