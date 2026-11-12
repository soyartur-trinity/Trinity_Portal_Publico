#!/usr/bin/env python3
"""Vuelta de las puertas fractales de Quantum en Arquitectura del Destino (noviembre de 2026).

Treinta nodos depurados de Trinity Quantum abren una puerta hacia un umbral de
Arquitectura del Destino (una de ellas, Quantum 1.7, hacia el índice de la serie).
Decisión de Arturo (9 de noviembre de 2026): la lista «Puertas laterales» de cada
cierre queda intacta, porque es el puñado que el libro eligió; la vuelta va debajo,
en una línea más discreta, «Vienen de Trinity Quantum» («Viene de», si es una
sola), con los nodos que le abrieron paso. Tiene el precedente de la línea «Viene
de Trinity Origen» del portal de Quantum. Los enlaces llevan class="vuelta", que el
inventario reconoce.

Quantum 1.7 apunta al índice de la serie, que no enlaza nada de la serie mayor:
vuelve desde el cierre de El Campo, que el mapa de la Red ya trata como entrada.

Los títulos son los de cada nodo depurado. Siguen el formato de su cierre: solo
El Campo, El Cuerpo, El Peso y La Obra llevan el título en cursiva.

Con la ruta de Trinity- como segundo argumento corrige además la puerta de
Quantum 2.3, que decía «Libro XXXVI del Portal Público» (las demás usan arábigos).

Cada cambio se aplica una sola vez: si el bloque ya está, el cierre se salta; si
el anclaje no aparece exactamente una vez, se detiene sin escribir nada.

Uso: python3 vuelta_puertas_quantum.py RUTA/02_Arquitectura_del_Destino [RUTA/Trinity-]
"""
import os, re, sys

Q = 'https://soyartur-trinity.github.io/Trinity-/02_Trinity_Quantum/'

TITULOS = {
    (1, 3): 'Realidades Superpuestas',
    (1, 6): 'El Lenguaje de las Sincronicidades',
    (1, 7): 'El Diseñador de Destinos',
    (2, 1): 'Conexiones Más Allá del Espacio-Tiempo',
    (2, 4): 'El Campo Unificado del Corazón',
    (2, 6): 'Relaciones Multidimensionales',
    (2, 7): 'La Red Cuántica de Gaia',
    (3, 2): 'Vidas Paralelas',
    (3, 3): 'El Pasado Desde el Ahora',
    (3, 4): 'Futuros Probables Como Elección',
    (4, 3): 'El Arte de la Bilocación',
    (4, 7): 'Coherencia en la Paradoja',
    (5, 2): 'El Viajero Dimensional',
    (5, 4): 'El Guardián de los Umbrales',
    (5, 7): 'El Portal Viviente',
    (7, 4): 'La Ilusión del Yo Separado',
    (7, 6): 'Portales Entre Realidades Paralelas',
    (8, 4): 'El Cuerpo de Plasma',
    (8, 6): 'Portales de Plasma',
    (9, 1): 'La Ruptura Que Crea',
    (10, 2): 'Vórtices de Transformación',
    (11, 5): 'El Diccionario Holográfico',
    (12, 1): 'El Punto de No Retorno',
    (12, 2): 'Convergencia de Todas las Líneas',
    (12, 4): 'Densidad Infinita de Amor',
    (12, 5): 'El Horizonte de Eventos Interior',
    (12, 6): 'Compresión de Todas las Posibilidades',
    (13, 1): 'Universos Paralelos Internos',
    (13, 2): 'El Observador de Observadores',
}

# cierre -> (título en cursiva, nodos de Quantum que le abren una puerta)
CIERRES = {
    'libro-01-el-campo/L01-cierre.html': (True, [(1, 6), (1, 7), (7, 6), (9, 1)]),
    'libro-03-el-testigo/L03-cierre.html': (False, [(3, 2), (4, 3), (13, 2)]),
    'libro-04-el-cuerpo/L04-cierre.html': (True, [(2, 4), (4, 7), (8, 4)]),
    'libro-05-la-grieta/L05-cierre.html': (False, [(3, 3), (12, 1)]),
    'libro-06-las-pequenas-muertes/L06-cierre.html': (False, [(5, 7), (8, 6), (12, 1)]),
    'libro-07-no-saber/L07-cierre.html': (False, [(3, 4), (12, 6)]),
    'libro-08-el-peso/L08-cierre.html': (True, [(10, 2)]),
    'libro-09-el-personaje/L09-cierre.html': (False, [(1, 3), (5, 2), (7, 4), (12, 5), (13, 1)]),
    'libro-11-la-red/L11-cierre.html': (False, [(2, 1), (2, 6), (12, 2)]),
    'libro-12-la-obra/L12-cierre.html': (True, [(5, 4), (12, 4)]),
    'libro-13-habitar/L13-cierre.html': (False, [(2, 7), (11, 5)]),
}

CSS = ('.vienen{margin:1.5rem 0 0}'
       '.vienen-t{font-family:\'Cormorant Garamond\',Georgia,serif;font-size:1.12rem;color:var(--plata);margin:0 0 .55rem}'
       '.vienen ul{list-style:none;margin:0;padding:0}'
       '.vienen li{margin:0 0 .5rem;padding-left:.9rem;border-left:1px solid var(--border)}'
       '.vienen a{font-family:\'Cormorant Garamond\',Georgia,serif;font-size:1.1rem;line-height:1.4;'
       'color:var(--text-soft);text-decoration:none}'
       '.vienen a:hover{color:var(--plata-clara);text-decoration:underline}\n')

LISTA = re.compile(r'<h2>Puertas laterales</h2><ul class="enlaces">.*?</ul>', re.S)


def bloque(em, nodos):
    filas = []
    for libro, nodo in nodos:
        t = TITULOS[(libro, nodo)]
        t = '<em>%s</em>' % t if em else t
        filas.append('<li><a class="vuelta" href="%sLibro_%02d/nodo_%02d.html">Libro %d, Nodo %d: %s</a></li>'
                     % (Q, libro, nodo, libro, nodo, t))
    verbo = 'Vienen' if len(nodos) > 1 else 'Viene'
    return ('<div class="vienen"><p class="vienen-t">%s de <em>Trinity Quantum</em></p><ul>%s</ul></div>'
            % (verbo, ''.join(filas)))


def arquitectura(raiz):
    nuevos = {}
    for archivo, (em, nodos) in CIERRES.items():
        ruta = os.path.join(raiz, archivo)
        s = open(ruta, encoding='utf-8').read()
        if 'class="vienen"' in s:
            print('ya estaba:', archivo)
            continue
        listas = LISTA.findall(s)
        if len(listas) != 1 or s.count('</style>') != 1:
            sys.exit('Plantilla inesperada en %s; no se escribe nada.' % archivo)
        s = s.replace(listas[0], listas[0] + bloque(em, nodos), 1)
        s = s.replace('</style>', CSS + '</style>', 1)
        nuevos[ruta] = s
        print('vuelta agregada: %s (+%d)' % (archivo, len(nodos)))
    for ruta, s in nuevos.items():
        open(ruta, 'w', encoding='utf-8').write(s)
    print('Listo: %d cierres tocados, %d vueltas.' % (
        len(nuevos), sum(len(CIERRES[os.path.relpath(r, raiz).replace(os.sep, '/')][1]) for r in nuevos)))


def quantum_2_3(trinity):
    ruta = os.path.join(trinity, '02_Trinity_Quantum', 'Libro_02', 'nodo_03.html')
    s = open(ruta, encoding='utf-8').read()
    viejo, nuevo = 'Lo que no habla</em>, Libro XXXVI del Portal Público', 'Lo que no habla</em>, Libro 36 del Portal Público'
    if nuevo in s:
        print('ya estaba: Quantum 2.3, «Libro 36»')
        return
    if s.count(viejo) != 1:
        # el título puede no ir en cursiva: se busca la forma sin etiqueta
        viejo, nuevo = 'Libro XXXVI del Portal Público', 'Libro 36 del Portal Público'
        if s.count(viejo) != 1:
            sys.exit('Quantum 2.3: no se encontró «Libro XXXVI» una sola vez; no se escribe nada.')
    open(ruta, 'w', encoding='utf-8').write(s.replace(viejo, nuevo, 1))
    print('corregido: Quantum 2.3, «Libro XXXVI» → «Libro 36»')


def main():
    arquitectura(sys.argv[1])
    if len(sys.argv) > 2:
        quantum_2_3(sys.argv[2])


if __name__ == '__main__':
    main()
