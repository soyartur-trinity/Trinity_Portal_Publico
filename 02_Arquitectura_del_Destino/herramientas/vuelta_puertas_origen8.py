#!/usr/bin/env python3
"""Vuelta de las puertas fractales de Origen VIII, Educación Cuántica (noviembre de 2026).

La depuración de Origen VIII abre ocho puertas: siete hacia la Red y una hacia
Origen IV. Hasta entonces ningún hilo llegaba a VIII. Este script agrega todas
las vueltas:

  1. En las «Puertas laterales» de La Obra, El Peso y La Corriente (Arquitectura
     del Destino), el enlace a los nodos 4, 6 y 7 de Origen VIII, después de la
     última entrada de Origen y en el formato de cada lista.
  2. En los cierres del Portal Público: un bloque nuevo en La intención (29) y en
     El ayudante (20, segunda constelación, con su propia paleta), y la línea de
     Origen VIII antes de la de Quantum en La duración (32) y Los muchos (35),
     cuyo rótulo pasa a «Puertas laterales». Origen primero, después Quantum.
  3. En Origen IV, Nodo 2, una línea «Viene de» marcada <a class="vuelta">
     hacia el Nodo 2 de Origen VIII.

Cada reemplazo se aplica exactamente una vez: si el anclaje no aparece una sola
vez, el script se detiene sin escribir nada. Si la vuelta ya está, la salta (se
puede correr de nuevo sin duplicar).

Uso: python3 vuelta_puertas_origen8.py RUTA/Trinity_Portal_Publico RUTA/Trinity-
"""
import os, sys

T = 'https://soyartur-trinity.github.io/Trinity-/'
O8 = T + '01_Trinity_Origen/Libro_08/'
MARCA = 'Libro_08/nodo_0'


def li(nodo, titulo):
    return '<li><a href="%snodo_%02d.html">Trinity Origen, Libro VIII, Nodo %d: %s</a></li>' % (O8, nodo, nodo, titulo)


ARQ = [
    ('02_Arquitectura_del_Destino/libro-12-la-obra/L12-cierre.html',
     '<li><a href="%s01_Trinity_Origen/Libro_06/nodo_04.html">Trinity Origen, Libro VI, Nodo 4: <em>Creatividad desde la nada</em></a></li>' % T,
     li(4, '<em>Currículum del alma</em>')),
    ('02_Arquitectura_del_Destino/libro-08-el-peso/L08-cierre.html',
     '<li><a href="%s01_Trinity_Origen/Libro_06/nodo_06.html">Trinity Origen, Libro VI, Nodo 6: <em>Integración del vacío</em></a></li>' % T,
     li(6, '<em>Evaluación multidimensional</em>')),
    ('02_Arquitectura_del_Destino/libro-10-la-corriente/L10-cierre.html',
     '<li><a href="%s01_Trinity_Origen/Libro_01/nodo_04.html">Trinity Origen, Libro I, Nodo 4: Campos morfogenéticos y conciencia colectiva</a></li>' % T,
     li(7, 'Tejiendo la nueva tierra educativa')),
]


def fila(nodo, titulo):
    return ('  <div class="puerta"><a href="%snodo_%02d.html">⟐ <em>Trinity Origen, Libro VIII, Nodo %d: '
            '<strong>%s</strong></em></a></div>\n' % (O8, nodo, nodo, titulo))


ANCLA = '<div class="continuar">'

CSS_TERCERA = ('\n  .laterales{margin:4.6rem 0 0;}\n'
               '  .laterales-label{display:block; font-family:\'Cormorant Garamond\',serif; font-size:.66rem;\n'
               '    letter-spacing:.35em; text-transform:uppercase; color:var(--oro-polvo); margin-bottom:1.5rem;}\n'
               '  .laterales .puerta{margin:0 0 1.2rem;}\n')

# El ayudante: su --oro-polvo (#3a2e18) no se lee sobre negro; rótulo en oro tenue y enlace en el oro de El ritmo.
CSS_TRAMA = ('\n  /* Puertas laterales (noviembre de 2026): vuelta de las puertas fractales de Trinity */\n'
             '  .laterales{margin:4.6rem 0 0;}\n'
             '  .laterales-label{display:block; font-family:\'Cormorant Garamond\',serif; font-size:.66rem;\n'
             '    letter-spacing:.35em; text-transform:uppercase; color:var(--oro-tenue); margin-bottom:1.5rem;}\n'
             '  .laterales .puerta{margin:0 0 1.2rem;}\n'
             '  .laterales .puerta a{color:#a88a4e;}\n'
             '  .laterales .puerta a:hover, .laterales .puerta a:focus-visible{color:var(--oro);}\n')

NUEVOS = [
    ('01_Libros/29_La_Intencion/cierre.html', CSS_TERCERA, fila(1, 'El colapso del modelo industrial')),
    ('01_Libros/20_El_Ayudante/cierre.html', CSS_TRAMA, fila(5, 'Tecnologías de Consciencia Aplicadas')),
]

EXISTENTES = [
    ('01_Libros/32_La_Duracion/cierre.html', fila(3, 'El Aula como Campo Cuántico')),
    ('01_Libros/35_Los_Muchos/cierre.html', fila(2, 'Inteligencias Múltiples Cuánticas')),
]

IV2 = ('01_Trinity_Origen/Libro_04/nodo_02.html',
       'su reconocimiento expande radicalmente nuestra comprens',
       '    <!-- Vuelta de la puerta de Origen VIII.2 (noviembre de 2026). -->\n'
       '    <p class="viene">Viene de <em>Educación Cuántica</em>: las inteligencias que '
       '<a class="vuelta" href="../Libro_08/nodo_02.html">su segundo nodo</a> mira hacia adentro, aquí se miran hacia afuera.</p>\n')


def leer(r):
    with open(r, encoding='utf-8', newline='') as f:
        return f.read()


def unico(s, a, ruta):
    if s.count(a) != 1:
        sys.exit('%s: el anclaje aparece %d veces:\n%s' % (ruta, s.count(a), a[:160]))


def main():
    portal, trinity = sys.argv[1], sys.argv[2]
    nuevos = {}
    for rel, ancla, linea in ARQ:
        r = os.path.join(portal, rel); s = leer(r)
        if MARCA in s:
            print('ya estaba:', rel); continue
        unico(s, ancla, r)
        nuevos[r] = s.replace(ancla, ancla + linea)
    for rel, css, linea in NUEVOS:
        r = os.path.join(portal, rel); s = leer(r)
        if MARCA in s:
            print('ya estaba:', rel); continue
        if 'class="laterales"' in s:
            sys.exit('%s ya tiene un bloque de puertas: no es un bloque nuevo' % r)
        unico(s, ANCLA, r); unico(s, '</style>', r)
        bloque = ('<div class="laterales">\n  <span class="laterales-label">Puerta lateral</span>\n%s</div>\n\n' % linea)
        nuevos[r] = s.replace('</style>', css + '</style>', 1).replace(ANCLA, bloque + ANCLA, 1)
    for rel, linea in EXISTENTES:
        r = os.path.join(portal, rel); s = leer(r)
        if MARCA in s:
            print('ya estaba:', rel); continue
        a = '<span class="laterales-label">Puerta lateral</span>\n'
        unico(s, a, r)
        nuevos[r] = s.replace(a, '<span class="laterales-label">Puertas laterales</span>\n' + linea)
    rel, ancla, linea = IV2
    r = os.path.join(trinity, rel); s = leer(r)
    if MARCA in s:
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
