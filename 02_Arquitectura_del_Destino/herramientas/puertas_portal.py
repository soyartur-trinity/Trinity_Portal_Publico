#!/usr/bin/env python3
"""Puertas laterales en los cierres del Portal Público (noviembre de 2026).

Las puertas fractales de Trinity llegan a dieciocho libros del Portal, que hasta
ahora no enlazaban hacia arriba. Este script agrega en el cierre de cada libro,
antes de «Volver», un bloque «Puertas laterales» con el enlace de regreso a cada
nodo que le abrió una puerta, en la forma de las puertas del propio Portal
(el ⟐ y la línea en cursiva), sin frase nueva.

El modelo nació en El ritmo (Libro 33), con Origen X.3 y Quantum 6.7. Sirve tal
cual para los cierres de la tercera constelación (27 a 39), que comparten la
plantilla; los libros anteriores (2, 3, 4, 8, 9, 11) tienen otra y piden su
propia adaptación.

Cada inserción se aplica una sola vez; si el bloque ya está, el libro se salta.

Uso: python3 puertas_portal.py RUTA/Trinity_Portal_Publico
"""
import os, sys

T = 'https://soyartur-trinity.github.io/Trinity-/'

# libro -> lista de (ruta en Trinity-, texto del enlace). Origen primero, después Quantum.
PUERTAS = {
    '33_El_Ritmo': [
        ('01_Trinity_Origen/Libro_10/nodo_03.html',
         'Trinity Origen, Libro X, Nodo 3: <strong>Los Campos Cuánticos de Sanación</strong>'),
        ('02_Trinity_Quantum/Libro_06/nodo_07.html',
         'Trinity Quantum, Libro 6, Nodo 7: <strong>El Amor como Fuerza Fundamental del Vacío</strong>'),
    ],
}

CSS = ('\n  .laterales{margin:4.6rem 0 0;}\n'
       '  .laterales-label{display:block; font-family:\'Cormorant Garamond\',serif; font-size:.66rem;\n'
       '    letter-spacing:.35em; text-transform:uppercase; color:var(--oro-polvo); margin-bottom:1.5rem;}\n'
       '  .laterales .puerta{margin:0 0 1.2rem;}\n')

ANCLA = '<div class="continuar">'


def bloque(enlaces):
    filas = ''.join('  <div class="puerta"><a href="%s%s">⟐ <em>%s</em></a></div>\n' % (T, r, t)
                    for r, t in enlaces)
    return ('<div class="laterales">\n'
            '  <span class="laterales-label">Puertas laterales</span>\n%s</div>\n\n' % filas)


def main():
    raiz = sys.argv[1]
    for libro, enlaces in PUERTAS.items():
        ruta = os.path.join(raiz, '01_Libros', libro, 'cierre.html')
        s = open(ruta, encoding='utf-8').read()
        if 'class="laterales"' in s:
            print('ya estaba:', libro)
            continue
        if s.count(ANCLA) != 1 or s.count('</style>') != 1:
            sys.exit('El cierre de %s no tiene la plantilla esperada; no se escribe nada.' % libro)
        s = s.replace('</style>', CSS + '</style>', 1)
        s = s.replace(ANCLA, bloque(enlaces) + ANCLA, 1)
        open(ruta, 'w', encoding='utf-8').write(s)
        print('puertas laterales agregadas: %s (%d)' % (libro, len(enlaces)))


if __name__ == '__main__':
    main()
