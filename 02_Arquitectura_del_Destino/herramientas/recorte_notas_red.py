#!/usr/bin/env python3
"""
La Red, al día con el recorte de La Puerta (18 de noviembre de 2026).

El Nodo 2 de La Puerta conserva todo lo que La Red cita (la pregunta por la soledad, «Tu cuerpo es
prueba», «¿Dónde termino yo y empieza el resto?», el objeto, la red de internet e «Inter-somos»),
pero ya no tiene semana de práctica, laboratorio ni mantras: lo que La Red tomaba de allí vive ahora
en el gesto del nodo, «Para hoy». Este script ajusta dos frases del texto de La Red que nombraban
la semana, y las notas que nombraban las secciones, en los umbrales y en el registro.

Escribe solo si encuentra cada anclaje exactamente una vez; si ya está hecho, lo dice y no toca nada.
Uso: python3 recorte_notas_red.py RUTA/Trinity_Portal_Publico
"""
import os, sys

RAIZ = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/trinity_portal_publico'
A = os.path.join(RAIZ, '02_Arquitectura_del_Destino')

CAMBIOS = {
    'libro-11-la-red/L11-U1.html': [
        ('Nodo 2: «El mito de la separación», «Preguntas sin respuesta (por ahora)». Fragmento.',
         'Nodo 2: «El mito de la separación», la pregunta final. Fragmento.'),
    ],
    'libro-11-la-red/L11-U2.html': [
        ('Entre las prácticas de una semana, propone mirar la conexión digital como una metáfora, y concluye:',
         'Entre sus gestos para el día, propone mirar la conexión digital como una metáfora, y concluye:'),
        ('Nodo 2: «El mito de la separación», «Práctica de 7 días», día 6. Fragmento.',
         'Nodo 2: «El mito de la separación», «Para hoy». Fragmento.'),
    ],
    'libro-11-la-red/L11-U3.html': [
        ('Es el primer día de la semana que propone La Puerta, y el ejercicio de la hoja de papel.',
         'Es uno de los gestos que propone La Puerta, y el ejercicio de la hoja de papel.'),
        ('Nodo 2: «El mito de la separación», «Tu cuerpo es prueba», «Laboratorio cuántico», fases 1 y 2, y «Para recordar». Fragmentos y paráfrasis; el ejercicio, sin espejo.',
         'Nodo 2: «El mito de la separación», «Tu cuerpo es prueba» y «Para hoy». Fragmentos y paráfrasis; el ejercicio, sin espejo.'),
    ],
    'registro.md': [
        ('Nodo 2: «El mito de la separación», «Preguntas sin respuesta (por ahora)». Fragmento.',
         'Nodo 2: «El mito de la separación», la pregunta final. Fragmento.'),
        ('Nodo 2: «El mito de la separación», «Práctica de 7 días», día 6. Fragmento.',
         'Nodo 2: «El mito de la separación», «Para hoy». Fragmento.'),
        ('Nodo 2: «El mito de la separación», «Tu cuerpo es prueba», «Laboratorio cuántico», fases 1 y 2, y «Para recordar». Fragmentos y paráfrasis; el ejercicio, sin espejo.',
         'Nodo 2: «El mito de la separación», «Tu cuerpo es prueba» y «Para hoy». Fragmentos y paráfrasis; el ejercicio, sin espejo.'),
    ],
}

def main():
    nuevos, errores = {}, []
    for rel, pares in CAMBIOS.items():
        ruta = os.path.join(A, rel)
        t = open(ruta, encoding='utf-8').read()
        orig = t
        for viejo, nuevo in pares:
            if t.count(viejo) == 1:
                t = t.replace(viejo, nuevo)
            elif t.count(nuevo) == 1:
                print('ya estaba:', rel, '·', nuevo[:60])
            else:
                errores.append('%s: %s' % (rel, viejo[:70]))
        if t != orig:
            nuevos[ruta] = t
    if errores:
        sys.exit('No se escribió nada. Sin anclaje: ' + ' | '.join(errores))
    for ruta, t in nuevos.items():
        open(ruta, 'w', encoding='utf-8').write(t)
        print('escrito:', ruta)

if __name__ == '__main__':
    main()
