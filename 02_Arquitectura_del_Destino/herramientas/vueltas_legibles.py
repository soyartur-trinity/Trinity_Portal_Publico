#!/usr/bin/env python3
"""Vueltas legibles (15 de noviembre de 2026).

Las líneas «Viene de» que devuelven las puertas fractales (<p class="viene"> con <a class="vuelta">)
heredan el estilo de enlaces de cada página. En las que no tienen uno, el enlace salía con el azul
del navegador (Origen IV.2, IV.3, X.3 y X.7; Quantum 2.2, 2.7, 3.3, 13.2 y 13.7), y en dos (Quantum
9.5 y 11.2) heredaba el color del texto, sin subrayado: no se veía que era un enlace.

Este script agrega, antes de </head>, un estilo de una línea: el enlace toma el oro de Origen
(#d6b36a) o el violeta de Quantum (#c4a8e0), los mismos de las puertas, con un subrayado tenue.
Si el estilo ya está, salta el archivo (se puede correr de nuevo sin duplicar).

Uso: python3 vueltas_legibles.py RUTA/Trinity-
"""
import os, sys

ORO = '#d6b36a'
VIOLETA = '#c4a8e0'

ARCHIVOS = [
    ('01_Trinity_Origen/Libro_04/nodo_02.html', ORO),
    ('01_Trinity_Origen/Libro_04/nodo_03.html', ORO),
    ('01_Trinity_Origen/Libro_10/nodo_03.html', ORO),
    ('01_Trinity_Origen/Libro_10/nodo_07.html', ORO),
    ('02_Trinity_Quantum/Libro_02/nodo_02.html', VIOLETA),
    ('02_Trinity_Quantum/Libro_02/nodo_07.html', VIOLETA),
    ('02_Trinity_Quantum/Libro_03/nodo_03.html', VIOLETA),
    ('02_Trinity_Quantum/Libro_09/nodo_05.html', VIOLETA),
    ('02_Trinity_Quantum/Libro_11/nodo_02.html', VIOLETA),
    ('02_Trinity_Quantum/Libro_13/nodo_02.html', VIOLETA),
    ('02_Trinity_Quantum/Libro_13/nodo_07.html', VIOLETA),
]

MARCA = '/* Vueltas legibles'


def estilo(color):
    return ('<style>/* Vueltas legibles (noviembre de 2026): el enlace de la línea «Viene de» toma el color de su serie. */\n'
            'p.viene a.vuelta{color:%s; text-decoration:underline; text-decoration-color:%s73; text-underline-offset:3px;}\n'
            'p.viene a.vuelta:hover, p.viene a.vuelta:focus-visible{text-decoration-color:currentColor;}</style>\n'
            % (color, color))


def main():
    raiz = sys.argv[1]
    nuevos = {}
    for rel, color in ARCHIVOS:
        r = os.path.join(raiz, rel)
        with open(r, encoding='utf-8', newline='') as f:
            s = f.read()
        if MARCA in s:
            print('ya estaba:', rel); continue
        if 'class="vuelta"' not in s:
            sys.exit('%s: no tiene ninguna vuelta' % rel)
        if s.count('</head>') != 1:
            sys.exit('%s: </head> aparece %d veces' % (rel, s.count('</head>')))
        nuevos[r] = s.replace('</head>', estilo(color) + '</head>')
    for r, s in nuevos.items():
        with open(r, 'w', encoding='utf-8', newline='') as f:
            f.write(s)
        print('escrito:', r)
    print('Listo: %d archivos.' % len(nuevos))


if __name__ == '__main__':
    main()
