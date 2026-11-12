#!/usr/bin/env python3
"""Enlaces rotos en cinco libros anteriores del Portal Público (11 de noviembre de 2026).

Una revisión de los 4.792 enlaces internos visibles de los dos repositorios
encontró veinticuatro rotos: veintiuno en dieciséis páginas de cinco libros del
Portal, que este script corrige, y tres en test-rutas.html, una página de prueba
de Trinity- que no se toca. Todos daban error 404 en línea. (Tres enlaces más de
La Voz Interior apuntan a archivos que no existen, pero están dentro de
comentarios del código: el lector no los ve.)

- Cuando algo en vos dice basta (Libro 6): «← Portal Trinity» apuntaba a
  ../../../index.html, un nivel por encima del sitio. Pasa a ../../index.html, el
  índice del Portal, como en los demás libros. Nueve páginas.
- Cultivar (Libro 12): el Umbral VIII se llama «Lo que tarda y lo que falla», pero
  su archivo quedó como ..._lo_que_falta.html. Los enlaces apuntan al archivo que
  existe; el nombre del archivo no se cambia, para no romper nada más.
- Volver distinto (Libro 9): el cierre volvía a «Umbral VII» en un archivo que no
  existe; el umbral anterior al cierre es el VIII, Consolidar.
- La Voz Interior (Libro 2): el índice enlazaba «autoría.html», con tilde; el
  archivo es autoria.html.
- Asertividad Consciente (Libro 4): «introduccion.html» en minúscula; el archivo es
  Introduccion.html, y GitHub distingue mayúsculas.

Cada reemplazo se cuenta: si no aparece las veces esperadas, se detiene sin
escribir nada. Corrido dos veces, no duplica.

Uso: python3 enlaces_rotos_portal.py RUTA/Trinity_Portal_Publico
"""
import os, sys

L = '01_Libros/'
C06 = [('href="../../../index.html"', 'href="../../index.html"')]
CAMBIOS = {
    L + '06_Cuando_Algo_Dice_Basta/capitulo_01.html': (C06, 1),
    L + '06_Cuando_Algo_Dice_Basta/capitulo_02.html': (C06, 1),
    L + '06_Cuando_Algo_Dice_Basta/capitulo_03.html': (C06, 1),
    L + '06_Cuando_Algo_Dice_Basta/capitulo_04.html': (C06, 1),
    L + '06_Cuando_Algo_Dice_Basta/capitulo_05.html': (C06, 1),
    L + '06_Cuando_Algo_Dice_Basta/capitulo_06.html': (C06, 1),
    L + '06_Cuando_Algo_Dice_Basta/epilogo.html': (C06, 2),
    L + '06_Cuando_Algo_Dice_Basta/index.html': (C06, 2),
    L + '06_Cuando_Algo_Dice_Basta/introduccion.html': (C06, 1),
    L + '12_Cultivar/cierre_cultivar.html': (
        [('href="umbral_8_lo_que_tarda_y_lo_que_falla.html"', 'href="umbral_8_lo_que_tarda_y_lo_que_falta.html"')], 2),
    L + '12_Cultivar/index.html': (
        [('href="umbral_8_lo_que_tarda_y_lo_que_falla.html"', 'href="umbral_8_lo_que_tarda_y_lo_que_falta.html"')], 1),
    L + '12_Cultivar/umbral_7_la_calma.html': (
        [('href="umbral_8_lo_que_tarda_y_lo_que_falla.html"', 'href="umbral_8_lo_que_tarda_y_lo_que_falta.html"')], 2),
    L + '09_Volver_Distinto/cierre_volver_distinto.html': (
        [('href="umbral_7_consolidar.html">← Umbral VII', 'href="umbral_8_consolidar.html">← Umbral VIII')], 1),
    L + '02_La_Voz_Interior/index.html': ([('href="autoría.html"', 'href="autoria.html"')], 1),
    L + '04_Asertividad_Consciente/capitulo_01.html': ([('href="introduccion.html"', 'href="Introduccion.html"')], 2),
    L + '04_Asertividad_Consciente/index.html': ([('href="introduccion.html"', 'href="Introduccion.html"')], 1),
}


def main():
    raiz = sys.argv[1]
    nuevos = {}
    for archivo, (reemplazos, veces) in CAMBIOS.items():
        ruta = os.path.join(raiz, archivo)
        s = open(ruta, 'rb').read().decode('utf-8')
        for a, b in reemplazos:
            n = s.count(a)
            if n == 0 and s.count(b) >= veces:
                continue
            if n != veces:
                sys.exit('%s: «%s» aparece %d veces (se esperaban %d); no se escribe nada.' % (archivo, a, n, veces))
            s = s.replace(a, b)
            nuevos[ruta] = s
    for ruta, s in nuevos.items():
        open(ruta, 'wb').write(s.encode('utf-8'))
        print('corregido:', os.path.relpath(ruta, raiz))
    print('Listo: %d archivos.' % len(nuevos))


if __name__ == '__main__':
    main()
