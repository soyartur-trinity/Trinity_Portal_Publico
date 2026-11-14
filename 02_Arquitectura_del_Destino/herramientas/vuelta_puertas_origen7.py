#!/usr/bin/env python3
"""Vuelta de las puertas fractales de Origen VII, La Muerte como Maestra (14 de noviembre de 2026).

La depuración completa de Origen VII abre ocho puertas, todas de ida y vuelta:

  VII.1 → Las Pequeñas Muertes, Umbral I («La puerta más grande»)
  VII.2 → Las Pequeñas Muertes, Umbral IV («El vaso que ya está roto»); ya volvía
  VII.3 → Origen X, Nodo 7 (dorada: David Tasma y Cicely Saunders)
  VII.4 → El Duelo (Portal Público, Libro 5), nodo 10 («El Bardo Permanente»)
  VII.5 → El Personaje, Umbral VI («La cebolla»), y La Grieta, Umbral IV («Noche no es depresión»)
  VII.6 → La Obra, Umbral IV («La cámara de los discretos»)
  VII.7 → Origen XI, Nodo 4 (dorada: La Gran Transición)

Este script agrega las vueltas que faltan:

  1. En las «Puertas laterales» de Las Pequeñas Muertes, El Personaje, La Grieta
     y La Obra (Arquitectura del Destino), el enlace al nodo de Origen VII, en el
     orden de libro de cada lista (en La Obra, después de la última entrada de
     Origen, como con Origen XI) y en su formato.
  2. En El Duelo, que no tenía puertas laterales, un bloque «Puerta lateral» en su
     último nodo, antes de la navegación, con la paleta de pergamino del libro.
  3. En Origen X.7 y en Origen XI.4, una línea «Viene de» marcada <a class="vuelta">.

Cada reemplazo se aplica exactamente una vez: si el anclaje no aparece una sola
vez, el script se detiene sin escribir nada. Si la vuelta ya está, la salta (se
puede correr de nuevo sin duplicar).

Uso: python3 vuelta_puertas_origen7.py RUTA/Trinity_Portal_Publico RUTA/Trinity-
"""
import os, sys

T = 'https://soyartur-trinity.github.io/Trinity-/'
O7 = T + '01_Trinity_Origen/Libro_07/'
MARCA = '01_Trinity_Origen/Libro_07/nodo_%02d'

AD = '02_Arquitectura_del_Destino/'


def li(nodo, titulo, em=False):
    t = '<em>%s</em>' % titulo if em else titulo
    return '<li><a href="%snodo_%02d.html">Trinity Origen, Libro VII, Nodo %d: %s</a></li>' % (O7, nodo, nodo, t)


# (archivo, anclaje: la entrada antes de la cual va la nueva, línea nueva, marca)
ARQ = [
    (AD + 'libro-06-las-pequenas-muertes/L06-cierre.html',
     '<li><a href="%s01_Trinity_Origen/Libro_07/nodo_02.html">' % T,
     li(1, 'El Tabú Primordial'), MARCA % 1),
    (AD + 'libro-09-el-personaje/L09-cierre.html',
     '<li><a href="%sTrinity_Infinito/Libro3/L3-Nodo1.html">' % T,
     li(5, 'La Muerte del Ego'), MARCA % 5),
    (AD + 'libro-05-la-grieta/L05-cierre.html',
     '<li><a href="%s01_Trinity_Origen/Libro_13/nodo_02.html">' % T,
     li(5, 'La Muerte del Ego'), MARCA % 5),
    (AD + 'libro-12-la-obra/L12-cierre.html',
     '<li><a href="%sTrinity_Infinito/Libro_10/L_10-Nodo1.html">' % T,
     li(6, 'El Legado Cuántico', em=True), MARCA % 6),
]

# El Duelo no tenía puertas laterales: estilo y bloque nuevos, en la paleta de pergamino del libro
# (el oro oscuro #6e4f0a sobre #f0eadb se lee con holgura).
DUELO = '01_Libros/05_Duelo/duelo_nodo_12.html'
DUELO_CSS = (
    '\n  /* Puertas laterales (noviembre de 2026): vuelta de las puertas fractales de Trinity */\n'
    '  .laterales{max-width:680px; margin:0 auto 2.4rem; text-align:left;}\n'
    "  .laterales-label{display:block; font-family:'Cinzel',serif; font-size:.68rem; letter-spacing:.3em;\n"
    '    text-transform:uppercase; color:var(--ink-soft); opacity:.7; margin-bottom:1rem;}\n'
    '  .laterales .puerta{margin:0 0 .9rem; padding-left:1rem; border-left:1px solid var(--gold-pale);}\n'
    "  .laterales .puerta a{font-family:'EB Garamond',Georgia,serif; font-style:italic; font-size:1.1rem; line-height:1.6;\n"
    '    color:var(--gold); text-decoration:none;}\n'
    '  .laterales .puerta a:hover, .laterales .puerta a:focus-visible{text-decoration:underline;}\n'
    '</style>')
DUELO_ANCLA = '<div class="container" style="padding-top:0;">\n  <nav class="nav-bottom">'
DUELO_BLOQUE = (
    '<div class="container" style="padding-top:0;">\n'
    '  <!-- Puertas laterales (noviembre de 2026) -->\n'
    '  <div class="laterales">\n'
    '    <span class="laterales-label">Puerta lateral</span>\n'
    '    <div class="puerta"><a href="%snodo_04.html">⟐ <em>Trinity Origen, Libro VII, Nodo 4: '
    '<strong>Tecnologías de Consciencia para el Tránsito</strong></em></a></div>\n'
    '  </div>\n'
    '</div>\n\n' % O7)

# (archivo, anclaje: el párrafo después del cual va la línea, línea nueva, marca)
VIENE = [
    ('01_Trinity_Origen/Libro_10/nodo_07.html',
     '<p>En 1948, en Londres, un refugiado polaco que se moría de cáncer',
     '    <!-- Vuelta de la puerta de Origen VII.3 (noviembre de 2026). -->\n'
     '    <p class="viene">Viene de <em>La Muerte como Maestra</em>: el arte de acompañar a quien muere, que enseña '
     '<a class="vuelta" href="../Libro_07/nodo_03.html">el tercer nodo</a> del séptimo libro de Origen, '
     'tiene en esta ventana su origen moderno.</p>\n',
     'Libro_07/nodo_03'),
    ('01_Trinity_Origen/Libro_11/nodo_04.html',
     '<p>La Gran Transición no es opcional; es <strong>evolutiva e inevitable</strong>.',
     '    <!-- Vuelta de la puerta de Origen VII.7 (noviembre de 2026). -->\n'
     '    <p class="viene">Viene de <em>La Muerte como Maestra</em>: el parto de la Tierra que imagina '
     '<a class="vuelta" href="../Libro_07/nodo_07.html">el último nodo</a> del séptimo libro de Origen '
     'se mira aquí desde la crisálida.</p>\n',
     'Libro_07/nodo_07'),
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
        r = os.path.join(portal, rel)
        s = nuevos.get(r) or leer(r)
        if marca in s:
            print('ya estaba:', rel); continue
        unico(s, ancla, r)
        nuevos[r] = s.replace(ancla, linea + ancla)

    r = os.path.join(portal, DUELO); s = leer(r)
    if MARCA % 4 in s:
        print('ya estaba:', DUELO)
    else:
        for a in ('</style>', DUELO_ANCLA):
            unico(s, a, r)
        s = s.replace('</style>', DUELO_CSS)
        s = s.replace(DUELO_ANCLA, DUELO_BLOQUE + DUELO_ANCLA)
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
