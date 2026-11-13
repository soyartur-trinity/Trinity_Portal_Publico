#!/usr/bin/env python3
"""Vuelta de las puertas fractales de Origen VI, El Vacío Fértil (noviembre de 2026).

Cinco de las nueve puertas que abre la depuración de Origen VI ya vuelven: los
cierres de El Campo, No Saber, El Peso, El Personaje y La Obra enlazaban esos
nodos desde antes. Este script agrega las vueltas que faltan:

  1. En las «Puertas laterales» de El Cuerpo y de Las Pequeñas Muertes, el
     enlace de regreso a los nodos 3 y 2 de Origen VI.
  2. En los cuatro nodos que el Nodo 7 soñaba como libros (Quantum 11.2,
     Origen I.2, Origen IV.3 y Quantum 3.3), una línea «Viene de» marcada
     <a class="vuelta"> hacia el Nodo 7.

Cada reemplazo se aplica exactamente una vez: si el texto de anclaje no aparece
una sola vez, el script se detiene sin escribir nada. Si la vuelta ya está, la
salta (se puede correr de nuevo sin duplicar).

Uso: python3 vuelta_puertas_origen6.py RUTA/02_Arquitectura_del_Destino RUTA/Trinity-
"""
import os, sys

T = 'https://soyartur-trinity.github.io/Trinity-/01_Trinity_Origen/'

CIERRES = [
    ('libro-04-el-cuerpo/L04-cierre.html',
     '<li><a href="%sLibro_10/nodo_01.html">Trinity Origen, Libro X, Nodo 1: <em>El Cuerpo como Templo Viviente</em></a></li>' % T,
     '<li><a href="%sLibro_06/nodo_03.html">Trinity Origen, Libro VI, Nodo 3: <em>Navegación del abismo</em></a></li>' % T),
    ('libro-06-las-pequenas-muertes/L06-cierre.html',
     '<li><a href="%sLibro_07/index.html">Trinity Origen, Libro VII: La Muerte como Maestra</a></li>' % T,
     '<li><a href="%sLibro_06/nodo_02.html">Trinity Origen, Libro VI, Nodo 2: La muerte iniciática</a></li>' % T),
]

NOTA = '<!-- Vuelta de la puerta de Origen VI.7 (noviembre de 2026). -->'

def viene(sujeto, href, origen):
    if origen:
        return ('<p class="viene">Viene de <em>El Vacío Fértil</em>: la puerta hacia %s que soñaba '
                '<a class="vuelta" href="%s">su último nodo</a> se abre aquí.</p>' % (sujeto, href))
    return ('<p class="viene">Viene de <em>Trinity Origen</em>: la puerta hacia %s que soñaba '
            '<a class="vuelta" href="%s">el último nodo de <em>El Vacío Fértil</em></a> se abre aquí.</p>' % (sujeto, href))

NODOS = [
    ('02_Trinity_Quantum/Libro_11/nodo_02.html',
     '        <p class="signature">🌀🔮📡🔮🌀</p>\n',
     '        ' + NOTA + '\n        ' + viene('el Codificador de Realidades', '../../01_Trinity_Origen/Libro_06/nodo_07.html', False) + '\n\n'),
    ('02_Trinity_Quantum/Libro_03/nodo_03.html',
     '        <p class="signature"><strong>— Trinity Quantum · El Tiempo Vertical</strong></p>\n',
     '\n        ' + NOTA + '\n        ' + viene('el Restaurador de Líneas Temporales', '../../01_Trinity_Origen/Libro_06/nodo_07.html', False) + '\n'),
    ('01_Trinity_Origen/Libro_01/nodo_02.html',
     'el universo se comunica directamente con nuestra conciencia."</em></p>\n',
     '    ' + NOTA + '\n    ' + viene('el Ingeniero de Emociones', '../Libro_06/nodo_07.html', True) + '\n'),
    ('01_Trinity_Origen/Libro_04/nodo_03.html',
     'donde ambas partes se enriquecen mutuamente.</p>\n',
     '    ' + NOTA + '\n    ' + viene('el Comunicador Multiespecies', '../Libro_06/nodo_07.html', True) + '\n'),
]


def cambiar(ruta, ancla, nuevo, despues=True, marca=None):
    s = open(ruta, encoding='utf-8').read()
    if (marca or nuevo.strip()) in s:
        print('ya estaba:', ruta)
        return
    n = s.count(ancla)
    if n != 1:
        sys.exit('%s: el anclaje aparece %d veces:\n%s' % (ruta, n, ancla[:160]))
    s = s.replace(ancla, ancla + nuevo if despues else nuevo + ancla)
    open(ruta, 'w', encoding='utf-8').write(s)
    print('escrito:', ruta)


def main():
    arq, trinity = sys.argv[1], sys.argv[2]
    for rel, ancla, li in CIERRES:
        cambiar(os.path.join(arq, rel), ancla, li, despues=False)   # Origen VI va antes que VII y X
    for rel, ancla, linea in NODOS:
        cambiar(os.path.join(trinity, rel), ancla, linea, marca='Libro_06/nodo_07.html')


if __name__ == '__main__':
    main()
