#!/usr/bin/env python3
"""Puertas laterales en los cierres del Portal Público (noviembre de 2026).

Las puertas fractales de Trinity llegan a dieciocho libros del Portal, que hasta
el 3 de noviembre no enlazaban hacia arriba. Este script agrega en el cierre de
cada libro, antes de «Volver», un bloque «Puertas laterales» («Puerta lateral», si
es una sola) con el enlace de regreso a cada nodo que le abrió una puerta, en la
forma de las puertas del propio Portal (el ⟐ y la línea en cursiva), sin frase
nueva. Origen primero, después Quantum; dentro de Quantum, por libro y nodo.

El modelo nació en El ritmo (Libro 33), con Origen X.3 y Quantum 6.7 (3 de
noviembre de 2026). El 9 de noviembre de 2026 se completó la vuelta de las
puertas de Quantum:

- Los once cierres de la tercera constelación (27 a 39) comparten plantilla y
  reciben el bloque tal cual (PUERTAS).
- Los seis libros anteriores (2, 3, 4, 8, 9 y 11) tienen cada uno su plantilla y
  su final: el bloque se adapta a su paleta y va en su página de cierre
  (ADAPTADOS). Su estilo entra en un <style> propio antes de </head>. Las letras
  usan em, porque esas páginas fijan el tamaño en el body y no en la raíz.

Cada inserción se aplica una sola vez; si el bloque ya está, el libro se salta;
si el anclaje no aparece exactamente una vez, se detiene sin escribir nada.

Uso: python3 puertas_portal.py RUTA/Trinity_Portal_Publico
"""
import os, sys

T = 'https://soyartur-trinity.github.io/Trinity-/'


def q(libro, nodo, titulo):
    return ('02_Trinity_Quantum/Libro_%02d/nodo_%02d.html' % (libro, nodo),
            'Trinity Quantum, Libro %d, Nodo %d: <strong>%s</strong>' % (libro, nodo, titulo))


# Tercera constelación: libro -> lista de (ruta en Trinity-, texto del enlace).
PUERTAS = {
    '27_El_Instante': [q(3, 6, 'Memorias del Futuro')],
    '28_El_Vacio': [q(6, 1, 'El Silencio Antes del Big Bang'),
                    q(11, 3, 'La Sintaxis del Vacío')],
    '30_La_Presencia': [q(6, 4, 'El Tiempo Cero — Pasado y Futuro en el Ahora'),
                        q(8, 7, 'La Ascensión Ígnea'),
                        q(12, 3, 'El Colapso Consciente')],
    '31_El_No_Saber': [q(7, 2, 'Navegando Entre Escalas de Magnitud')],
    '32_La_Duracion': [q(3, 1, 'El Presente Eterno')],
    '33_El_Ritmo': [
        ('01_Trinity_Origen/Libro_10/nodo_03.html',
         'Trinity Origen, Libro X, Nodo 3: <strong>Los Campos Cuánticos de Sanación</strong>'),
        q(6, 7, 'El Amor como Fuerza Fundamental del Vacío'),
    ],
    '34_El_Cuerpo': [q(8, 5, 'Comunicación Plasmática'),
                     q(11, 7, 'El Intérprete Cuántico')],
    '35_Los_Muchos': [q(10, 4, 'Campos Torsionales del Corazón')],
    '36_Lo_Que_No_Habla': [q(2, 3, 'El Silencio Compartido'),
                           q(7, 5, 'Co-creación Consciente con el Todo')],
    '37_La_Emergencia': [q(5, 3, 'El Tejedor de Realidades'),
                         q(6, 3, 'El Observador como Arquitecto del Vacío'),
                         q(6, 5, 'Algoritmos del Vacío — Complejidad desde la Simplicidad'),
                         q(7, 3, 'Campos Morfogenéticos — La Memoria del Holofractal')],
    '38_Lo_Que_Se_Recibe': [q(6, 6, 'El Vacío como Campo de Información Pura'),
                            q(8, 3, 'El Sol Interior')],
    '39_El_Campo': [q(7, 7, 'Viviendo la Paradoja — Infinito Siendo Finito'),
                    q(8, 2, 'Estados Plasmáticos de Consciencia'),
                    q(12, 7, 'El Big Bang Personal')],
}

CSS = ('\n  .laterales{margin:4.6rem 0 0;}\n'
       '  .laterales-label{display:block; font-family:\'Cormorant Garamond\',serif; font-size:.66rem;\n'
       '    letter-spacing:.35em; text-transform:uppercase; color:var(--oro-polvo); margin-bottom:1.5rem;}\n'
       '  .laterales .puerta{margin:0 0 1.2rem;}\n')

ANCLA = '<div class="continuar">'


def etiqueta(n):
    return 'Puertas laterales' if n > 1 else 'Puerta lateral'


def bloque(enlaces):
    filas = ''.join('  <div class="puerta"><a href="%s%s">⟐ <em>%s</em></a></div>\n' % (T, r, t)
                    for r, t in enlaces)
    return ('<div class="laterales">\n'
            '  <span class="laterales-label">%s</span>\n%s</div>\n\n' % (etiqueta(len(enlaces)), filas))


# ---------------------------------------------------------------------------
# Los seis libros anteriores. Paletas: dorada sobre negro (8, 9 y 11) y clara
# sobre papel (2, 3 y 4).

CSS_DORADO = '''<style>
  /* Puertas laterales (noviembre de 2026): vuelta de las puertas fractales de Trinity */
  .laterales{%(caja)s}
  .laterales-label{display:block; font-family:'Cormorant Garamond',serif; font-size:.62em;
    letter-spacing:.35em; text-transform:uppercase; color:var(--oro-tenue); margin-bottom:1.3em;}
  .laterales .puerta{margin:0 0 1.1em; padding-left:1.1rem; border-left:1px solid var(--separador);
    opacity:1; transform:none;}
  .laterales .puerta a{font-family:'Cormorant Garamond',serif; font-style:italic; font-size:1.02em;
    line-height:1.6; color:#a88a4e; text-decoration:none; transition:color .3s ease;}
  .laterales .puerta a:hover, .laterales .puerta a:focus-visible{color:var(--oro);}
</style>
'''

CSS_CLARO = '''<style>
  /* Puertas laterales (noviembre de 2026): vuelta de las puertas fractales de Trinity */
  .laterales{margin:2.6em 0 1.6em; text-align:left;}
  .laterales-label{display:block; font-family:Georgia,serif; font-size:.7em; letter-spacing:.3em;
    text-transform:uppercase; color:%(suave)s; margin-bottom:1em;}
  .laterales .puerta{margin:0 0 .9em; padding-left:1rem; border-left:1px solid %(borde)s;}
  .laterales .puerta a{font-family:Georgia,serif; font-style:italic; font-size:%(talla)s; line-height:1.6;
    color:var(--acento); text-decoration:none;}
  .laterales .puerta a:hover, .laterales .puerta a:focus-visible{text-decoration:underline;}
</style>
'''

ADAPTADOS = {
    '02_La_Voz_Interior': dict(
        archivo='epilogo.html',
        ancla='    <nav class="chapter-nav" aria-label="Navegación del epílogo">',
        sangria='    ',
        css=CSS_CLARO % dict(suave='var(--texto-suave)', borde='rgba(139,107,154,.4)', talla='1.1em'),
        enlaces=[q(13, 1, 'Universos Paralelos Internos')]),
    '03_Encuentro_Real': dict(
        archivo='cierre.html',
        ancla='            <p style="text-align: center; font-size: 1.1rem; color: var(--acento); margin-top: 2rem;">',
        sangria='            ',
        css=CSS_CLARO % dict(suave='var(--primario)', borde='var(--borde)', talla='1.1em'),
        enlaces=[q(13, 4, 'El Espejo Holográfico Interior')]),
    '04_Asertividad_Consciente': dict(
        archivo='epilogo.html',
        ancla='    <nav class="chapter-nav" style="background:transparent;border:none;padding:1rem 0;">',
        sangria='    ',
        css=CSS_CLARO % dict(suave='var(--texto-suave)', borde='var(--borde)', talla='1.1em'),
        enlaces=[q(11, 4, 'Membranas Permeables')]),
    '08_Atender': dict(
        archivo='cierre_el_gesto_que_se_repite.html',
        ancla='  <!-- Vuelta al inicio — la serie continúa -->',
        sangria='  ',
        css=CSS_DORADO % dict(caja='max-width:620px; margin:4.5rem auto 0;'),
        enlaces=[q(3, 4, 'Futuros Probables Como Elección')]),
    '09_Volver_Distinto': dict(
        archivo='cierre_volver_distinto.html',
        ancla='  <!-- Volver -->',
        sangria='  ',
        css=CSS_DORADO % dict(caja='max-width:680px; margin:4.5rem auto 0;'),
        enlaces=[q(3, 5, 'La Espiral Temporal')]),
    '11_Atravesar': dict(
        archivo='umbral_7_atravesar.html',
        ancla='    <div class="cierre-links">',
        sangria='    ',
        css=CSS_DORADO % dict(caja='margin:0 0 3rem; text-align:left;'),
        enlaces=[q(9, 5, 'La Grieta Donde Entra la Luz')]),
}


def bloque_adaptado(enlaces, sangria):
    filas = ''.join('%s  <div class="puerta"><a href="%s%s">⟐ <em>%s</em></a></div>\n' % (sangria, T, r, t)
                    for r, t in enlaces)
    return ('%s<!-- Puertas laterales (noviembre de 2026) -->\n'
            '%s<div class="laterales">\n'
            '%s  <span class="laterales-label">%s</span>\n%s%s</div>\n\n'
            % (sangria, sangria, sangria, etiqueta(len(enlaces)), filas, sangria))


def leer(ruta):
    with open(ruta, encoding='utf-8', newline='') as f:
        return f.read()


def escribir(ruta, s):
    with open(ruta, 'w', encoding='utf-8', newline='') as f:
        f.write(s)


def main():
    raiz = sys.argv[1]
    nuevos = {}
    for libro, enlaces in PUERTAS.items():
        ruta = os.path.join(raiz, '01_Libros', libro, 'cierre.html')
        s = leer(ruta)
        if 'class="laterales"' in s:
            print('ya estaba:', libro)
            continue
        if s.count(ANCLA) != 1 or s.count('</style>') != 1:
            sys.exit('El cierre de %s no tiene la plantilla esperada; no se escribe nada.' % libro)
        s = s.replace('</style>', CSS + '</style>', 1)
        s = s.replace(ANCLA, bloque(enlaces) + ANCLA, 1)
        nuevos[ruta] = (s, libro, len(enlaces))
    for libro, d in ADAPTADOS.items():
        ruta = os.path.join(raiz, '01_Libros', libro, d['archivo'])
        s = leer(ruta)
        if 'class="laterales"' in s:
            print('ya estaba:', libro)
            continue
        ancla = d['ancla']
        if s.count(ancla) != 1 or s.count('</head>') != 1:
            sys.exit('Anclaje no único en %s/%s; no se escribe nada.' % (libro, d['archivo']))
        b, css = bloque_adaptado(d['enlaces'], d['sangria']), d['css']
        if '\r\n' in s:  # Atravesar usa finales de línea de Windows: se respetan
            b, css = b.replace('\n', '\r\n'), css.replace('\n', '\r\n')
        s = s.replace('</head>', css + '</head>', 1)
        s = s.replace(ancla, b + ancla, 1)
        nuevos[ruta] = (s, libro, len(d['enlaces']))
    for ruta, (s, libro, n) in nuevos.items():
        escribir(ruta, s)
        print('puertas laterales agregadas: %s (%d)' % (libro, n))
    print('Listo: %d libros tocados.' % len(nuevos))


if __name__ == '__main__':
    main()
