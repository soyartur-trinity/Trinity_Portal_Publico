#!/usr/bin/env python3
"""Dos arreglos en libros anteriores del Portal Público (11 de noviembre de 2026).

A pedido de Arturo (maestro v4, sección 19):

1. La Voz Interior (Libro 2). Quince páginas —los doce capítulos, el interludio,
   el epílogo y el apéndice— buscaban su hoja de estilo en ../styles.css, que no
   existe; la hoja está en la carpeta del libro. Se veían sin su diseño (letra
   Times, fondo blanco) y los botones de navegación desbordaban diez píxeles a
   390 px. El enlace pasa a styles.css, como en el índice, el prefacio, la
   introducción y la autoría.

2. Atravesar (Libro 11). Las puertas propias de los umbrales usaban
   var(--oro-polvo) (#3a2e18 sobre el negro #0d0c0b), un contraste de 1,5 a 1:
   casi no se leían. Toman el oro de El ritmo (#a88a4e), el mismo de su bloque de
   puertas laterales; al pasar el cursor, el oro pleno (var(--oro)), porque el
   oro tenue de antes era más oscuro que el nuevo color de reposo. La letra pasa
   de .98rem (15,7 px) a 1.1rem (17,6 px).

Los archivos conservan sus finales de línea (Atravesar usa los de Windows).
Cada cambio se aplica una sola vez; si un anclaje no aparece como se espera, se
detiene sin escribir nada.

Uso: python3 arreglos_voz_atravesar.py RUTA/Trinity_Portal_Publico
"""
import glob, os, re, sys

VIEJO_CSS = b'<link rel="stylesheet" href="../styles.css"'
NUEVO_CSS = b'<link rel="stylesheet" href="styles.css"'

REGLA = re.compile(rb'(\.puerta a\{[^}]*?)font-size:\.98rem;(\s*)color:var\(--oro-polvo\);')
HOVER_VIEJO = b'.puerta a:hover{color:var(--oro-tenue);}'
HOVER_NUEVO = b'.puerta a:hover{color:var(--oro);}'


def main():
    raiz = os.path.join(sys.argv[1], '01_Libros')
    nuevos = {}

    voz = sorted(glob.glob(os.path.join(raiz, '02_La_Voz_Interior', '*.html')))
    for ruta in voz:
        s = open(ruta, 'rb').read()
        n = s.count(VIEJO_CSS)
        if n == 0:
            continue
        if n != 1:
            sys.exit('%s: el enlace a la hoja aparece %d veces; no se escribe nada.' % (ruta, n))
        nuevos[ruta] = s.replace(VIEJO_CSS, NUEVO_CSS, 1)

    atr = sorted(glob.glob(os.path.join(raiz, '11_Atravesar', 'umbral_*.html')))
    for ruta in atr:
        s = open(ruta, 'rb').read()
        if b'color:#a88a4e;' in s and HOVER_VIEJO not in s and not REGLA.search(s):
            continue
        if len(REGLA.findall(s)) != 1 or s.count(HOVER_VIEJO) != 1:
            sys.exit('%s: la regla de la puerta no tiene la forma esperada; no se escribe nada.' % ruta)
        s = REGLA.sub(rb'\1font-size:1.1rem;\2color:#a88a4e;', s, count=1)
        s = s.replace(HOVER_VIEJO, HOVER_NUEVO, 1)
        nuevos[ruta] = s

    for ruta, s in nuevos.items():
        open(ruta, 'wb').write(s)
        print('arreglado:', os.path.relpath(ruta, raiz))
    print('Listo: %d archivos.' % len(nuevos))


if __name__ == '__main__':
    main()
