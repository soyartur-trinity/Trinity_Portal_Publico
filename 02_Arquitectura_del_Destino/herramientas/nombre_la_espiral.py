#!/usr/bin/env python3
"""La entrada de Trinity- se llama La Espiral (9 de noviembre de 2026).

Arturo pidió dejar el nombre «Stargate», que se asocia a la ciencia ficción, y
eligió «La Espiral» («sin dudas»): 🌀 es el símbolo que eligió hace casi tres
años, cuando una IA le preguntó con cuál se identificaba. Resume además el
movimiento de la Constelación: la obra llegó del centro hacia lo cotidiano, y el
lector la recorre de vuelta, hacia el centro vacío, un poco más arriba cada vez.
El subtítulo «Umbral de Consciencia» se conserva.

La dirección no cambia: la entrada es la raíz del repositorio. Cambian el título
y los textos donde aparecía el nombre, y también los enlaces de vuelta de los
índices de serie, que llamaban a la entrada «Portal Trinity», nombre que se
confundía con el Portal Público y con La Puerta. Los nodos de La Puerta que dicen
«Portal Trinity» apuntan al índice de La Puerta y no se tocan. El archivo
stargate_explorar.html conserva su nombre, para no romper enlaces guardados.

Reemplazos contados: si alguno no aparece exactamente una vez, no se escribe
nada. Si ya están hechos, el archivo se salta.

Uso: python3 nombre_la_espiral.py RUTA/Trinity-
"""
import os, sys

NOTA = ('<!-- 9 de noviembre de 2026, a pedido de Arturo (maestro v4 de Arquitectura del Destino, '
        'sección 19): la entrada se llama La Espiral; antes, Stargate. -->\n')

CAMBIOS = {
    'index.html': [
        ('<title>TRINITY · STARGATE</title>', '<title>TRINITY · LA ESPIRAL</title>'),
        ('content="Trinity: Portal de Transformación de Consciencia — STARGATE"',
         'content="Trinity · La Espiral, umbral de consciencia: la entrada a toda la constelación."'),
        ('aria-label="Trinity Stargate"', 'aria-label="Trinity · La Espiral"'),
        ('<div class="subtitle">STARGATE · Umbral de Consciencia</div>',
         '<div class="subtitle">LA ESPIRAL · Umbral de Consciencia</div>'),
        ('<html lang="es">', NOTA + '<html lang="es">'),
    ],
    'stargate_explorar.html': [
        ('← Volver al Stargate</a>', '← Volver a La Espiral</a>'),
    ],
    '01_Trinity_Origen/index.html': [
        ('<div class="hero-topline">Stargate Archive</div>', '<div class="hero-topline">La Espiral</div>'),
        ('class="back-portal">← Volver al Portal Trinity</a>', 'class="back-portal">← Volver a La Espiral</a>'),
    ],
    '00_Portal_Trinity/index.html': [
        ('<a class="volver" href="../index.html">⟵ Portal Trinity</a>',
         '<a class="volver" href="../index.html">⟵ La Espiral</a>'),
    ],
    '02_Trinity_Quantum/index.html': [
        ('<a class="volver" href="../index.html">⟵ Portal Trinity</a>',
         '<a class="volver" href="../index.html">⟵ La Espiral</a>'),
    ],
}


def main():
    raiz = sys.argv[1]
    nuevos = {}
    for archivo, reemplazos in CAMBIOS.items():
        ruta = os.path.join(raiz, archivo)
        s = open(ruta, encoding='utf-8').read()
        if all(b in s and a not in s.replace(b, '') for a, b in reemplazos):
            print('ya estaba:', archivo)
            continue
        for a, b in reemplazos:
            if s.count(a) != 1:
                sys.exit('«%s» aparece %d veces en %s; no se escribe nada.' % (a[:50], s.count(a), archivo))
            s = s.replace(a, b, 1)
        nuevos[ruta] = s
        print('renombrado: %s (%d cambios)' % (archivo, len(reemplazos)))
    for ruta, s in nuevos.items():
        open(ruta, 'w', encoding='utf-8').write(s)
    print('Listo: %d archivos.' % len(nuevos))


if __name__ == '__main__':
    main()
