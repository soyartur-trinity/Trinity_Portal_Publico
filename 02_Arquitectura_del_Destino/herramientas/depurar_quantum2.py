#!/usr/bin/env python3
"""
Depuración de Quantum 2, *Entrelazamiento Sagrado* (octubre de 2026), con el
veto de Arturo en cada tarjeta.

Dos etapas en un solo script:
  1. Sesión breve por riesgo clínico (27 de octubre): nodos 5 y 6, y la
     corrección del recuadro «Conexiones con Trinity» de La Puerta, nodo 2.
  2. Depuración completa (29 de octubre), con las cuatro precisiones de la
     revisión de todo Quantum (experimentos, cifras, «cuántico», velas y
     rituales): índice y nodos 1, 2, 3, 4 y 7. El nodo 3 cambia de título:
     de «Telepatía Como Estado Natural» a «El Silencio Compartido».

Método (maestro v4, sección 5): cada reemplazo aprobado se aplica exactamente
una vez sobre el original de la etiqueta `quantum-original`. El HTML original
de estos nodos estaba roto (contenido después de </html>, documentos sin
cerrar, secciones duplicadas, etiquetas cruzadas), así que su cuerpo se
reemplaza desde la marca que abre el contenido hasta el final del archivo.
La etapa 2 reemplaza el índice y el nodo 4 enteros, de modo que los dos
ajustes que la etapa 1 les hacía quedan incluidos en sus cuerpos nuevos.

Uso:  python3 depurar_quantum2.py RUTA_A_UNA_COPIA_DEL_ORIGINAL
      (por ejemplo, el contenido de la etiqueta quantum-original)
"""
import sys
from pathlib import Path

PROCEDENCIA = (
    "<!-- Depurado en octubre de 2026 según la guía de depuración de Quantum "
    "(Arquitectura del Destino, maestro v4), en una sesión breve por riesgo clínico, "
    "con el veto de Arturo en cada tarjeta. El original se conserva en la etiqueta "
    "quantum-original del repositorio. -->"
)

ESTILO = """    <style>
      /* ============================================================
         Depuración · octubre 2026
         Letra más grande en el teléfono, firma, bloque fijo de las puertas
         y estilos mínimos para lo que la hoja común no cubre.
         ============================================================ */
      .node-content h3{
        margin: 1.3em 0 .45em;
        font-size: 1.06rem;
        color: var(--violet-light);
      }
      .node-content ol{
        margin: .6em 0 1em 1.4em;
        padding: 0;
      }
      .node-content ol li{ margin-bottom: 6px; }
      .node-content blockquote{
        margin: 1em 0 1.1em;
        padding: 12px 16px;
        border-left: 2px solid var(--gold-soft);
        border-radius: 0 12px 12px 0;
        background: rgba(255, 255, 255, .025);
        font-style: italic;
      }
      .node-content blockquote p{ margin: 0; }
      .node-content .nota{ color: rgba(246, 240, 255, .82); }
      .node-content ul.recordar li{
        margin-bottom: 4px;
        font-style: italic;
        color: var(--gold-light);
      }
      .node-content .dia{ margin: 0 0 14px; }
      .node-content .dia strong{
        display: block;
        margin-bottom: 4px;
        color: var(--gold-soft);
        letter-spacing: .04em;
      }
      .node-content .node-symbol{
        margin: 18px 0 4px;
        text-align: center;
        letter-spacing: .3em;
      }
      .node-content p.signature{
        margin: 22px 0 8px;
        color: rgba(243, 209, 122, .85);
        font-size: 14px;
        letter-spacing: .04em;
      }
      .puerta{
        margin: 30px 0 10px;
        padding: 18px 20px 16px;
        border-radius: 16px;
        border: 1px solid var(--p-borde);
        background: var(--p-fondo);
        box-shadow: 0 10px 24px rgba(0,0,0,.28);
      }
      .puerta.arquitectura{
        --p-fondo: linear-gradient(180deg, rgba(6,13,26,.94), rgba(6,13,26,.74));
        --p-borde: rgba(168,196,224,.42);
        --p-acento: #a8c4e0;
        --p-texto: #e8eef6;
      }
      .node-content .puerta .p-nombre{
        margin: 0 0 6px;
        font-size: 15px;
        font-style: italic;
        letter-spacing: .06em;
        color: var(--p-acento);
      }
      .node-content .puerta .p-texto{
        margin: 0 0 14px;
        color: var(--p-texto);
      }
      .puerta .cruzar{
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 9px 16px;
        border-radius: 999px;
        border: 1px solid var(--p-borde);
        color: var(--p-acento);
        font-size: 14px;
        letter-spacing: .04em;
        text-decoration: none;
        transition: border-color .18s ease, background .18s ease;
      }
      .puerta .cruzar:hover{ border-color: var(--p-acento); background: rgba(255,255,255,.04); }
      .puerta .cruzar:focus-visible{ outline: 2px solid var(--p-acento); outline-offset: 3px; }

      @media (max-width: 640px){
        .node-content p, .node-content li{ font-size: 18px; line-height: 1.7; }
        .node-content p.signature{ font-size: 15px; }
        .puerta{ padding: 16px 16px 14px; }
      }
      @media (prefers-reduced-motion: reduce){
        .puerta .cruzar{ transition: none; }
      }
    </style>
"""

# ---------------------------------------------------------------------------
# Nodo 5 · El Cuidado No-Local (antes: Sanación No-Local)
# ---------------------------------------------------------------------------
NODO5_CUERPO = """    <!-- Título del Nodo -->
    <section class="node-meta">
        <div class="node-book-title">Libro 2 · Entrelazamiento Sagrado</div>
        <h1 class="node-heading">Nodo 5: El Cuidado No-Local</h1>
        <div class="node-index">Nodo 5 de 7 · Cuidar a distancia</div>
    </section>

    <!-- INICIO DEL CONTENIDO -->
    <main class="node-content">

        <section class="node-section">

            <h2>🌌 TRANSMISIÓN CUÁNTICA</h2>

            <p>La distancia separa los cuerpos, no el cariño. A alguien que está al otro lado del planeta puedes llevarlo tan cerca como si estuviera en tus brazos. A veces más cerca, porque la distancia aquieta la prisa por arreglar y deja solo el deseo de su bien.</p>

            <p>Cada cuerpo emite una luz muy débil, mil veces más tenue de lo que el ojo alcanza a ver (Kobayashi, 2009). Es una buena imagen de lo que cada persona irradia: algo de ella llega a quien está cerca, aunque no se vea. Quien acompaña no envía energía —eso es comprensión newtoniana— ni reescribe a nadie con patrones de salud perfecta: ofrece presencia, y en ese espacio el otro encuentra sus propios recursos.</p>

            <p>Este cuidado se mide donde ocurre: en quien ama. Unos minutos de desear el bien a un desconocido, frente a su foto, bastaron para que la gente se sintiera más unida a él y a los demás (Hutcherson, Seppälä y Gross, 2008). Lo que se cultiva en el corazón no se queda adentro: cambia la manera de mirar, y la mirada cambia el trato.</p>

            <p>Ningún cuerpo es solo su enfermedad. Siempre hay en él algo que sigue sano: lo que respira, lo que ama, lo que recuerda. Antonovsky lo llamó salutogénesis: preguntar no solo qué enferma, sino qué sostiene la salud. Cuidar es mirar las dos cosas a la vez.</p>

            <p>El secreto más hondo del cuidado: no sanas al «otro». Lo acompañas, y en ese acompañar algo se acompaña también en ti. Lo que te duele de su dolor habla de tu propia historia; escucharlo te vuelve mejor compañía.</p>

            <p>Por eso acompaña mejor quien conoce sus propias sombras: no las pone en el otro.</p>

        </section>

        <section class="node-section">

            <h2>🔄 PARADOJA MEDICINAL</h2>

            <blockquote>
                <p>“Para cuidar a otro, debes verlo entero mientras honras su experiencia de enfermedad.
                Debes sostener a la vez su perfección eterna y su sufrimiento temporal.”</p>
            </blockquote>

            <p><strong>Contempla:</strong> ¿Qué historia necesita ser escuchada junto a la enfermedad? ¿Qué parte de quien sufre sigue intacta, esperando que alguien la mire?</p>

        </section>

        <section class="node-section">

            <h2>🧪 LABORATORIO CUÁNTICO</h2>

            <h3>Experimento 1: Bondad a Distancia</h3>
            <ol>
                <li>Elige a alguien que esté pasando un momento difícil.</li>
                <li>Respira despacio hasta que el pecho se afloje.</li>
                <li>Tráelo a la mente con su dolor y con todo lo que es además de su dolor.</li>
                <li>Dile por dentro: «Que estés acompañado. Que tengas alivio. Que estés en paz».</li>
                <li>No empujes nada: sostén el deseo sin esfuerzo.</li>
                <li>Suelta por completo.</li>
                <li>Si puedes, termina con un gesto real: un mensaje, una llamada, una visita.</li>
            </ol>
            <p><em>Duración: de 10 a 15 minutos.</em></p>

            <h3>Experimento 2: Carta al Que Fuiste</h3>
            <ol>
                <li>Elige un momento difícil del pasado que hoy puedas mirar sin que te arrastre. No el más hondo.</li>
                <li>Siéntate con papel y lápiz, y respira unos minutos.</li>
                <li>Escríbele al que eras entonces, desde quien eres hoy.</li>
                <li>No cambies lo que pasó: dile lo que necesitaba oír.</li>
                <li>Lee la carta en voz baja.</li>
                <li>Guárdala, o déjala ir, como prefieras.</li>
                <li>Nota qué cambió en ti al escribirla.</li>
            </ol>
            <p><em>Lo pasado no cambia; cambia la manera de llevarlo.</em></p>
            <p class="nota">Las heridas hondas, las que al recordarlas se vuelven a vivir, no se visitan a solas: se recorren con un profesional.</p>

        </section>

        <section class="node-section">

            <h2>💠 TRADUCCIÓN VIVIENTE</h2>

            <p>El cuidado crece con la presencia y no se mide en distancia. Lo que lo estrecha no es la duda del otro, sino la prisa por arreglarlo.</p>

        </section>

        <section class="node-section">

            <h2>✦ PARA RECORDAR</h2>

            <ul class="recordar">
                <li>Te veo entero, también en tu dolor.</li>
                <li>No te arreglo: te acompaño.</li>
                <li>La distancia no mide el cariño.</li>
                <li>Lo que sostengo en ti se sostiene en mí.</li>
                <li>El cuidado viaja en una voz, en un mensaje, en una mano.</li>
            </ul>

        </section>

        <section class="node-section">

            <h2>📅 PRÁCTICA DE 7 DÍAS</h2>

            <div class="dia">
                <strong>DÍA 1 – PREPARACIÓN</strong>
                <ul>
                    <li>Cuidar algo tuyo: el sueño, la comida o una consulta pendiente</li>
                    <li>Notar qué se siente recibir cuidado de ti mismo</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 2 – LO CERCANO</strong>
                <ul>
                    <li>Cuidar una planta o un animal con atención entera</li>
                    <li>Observar cómo responde</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 3 – EXPANSIÓN</strong>
                <ul>
                    <li>La bondad a distancia hacia un amigo</li>
                    <li>Un mensaje real al terminar</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 4 – TIEMPO</strong>
                <ul>
                    <li>La carta al que fuiste</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 5 – COLECTIVO</strong>
                <ul>
                    <li>Unirte a una meditación compartida o a un acto de cuidado junto a otros</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 6 – LO DIFÍCIL</strong>
                <ul>
                    <li>La bondad hacia alguien con quien hay tensión, sin forzar el perdón</li>
                    <li>Si esa persona te daña, este día es para cuidarte a ti</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 7 – SERVICIO</strong>
                <ul>
                    <li>Ofrecer compañía concreta a quien la necesite</li>
                    <li>Gratitud por el don de cuidar</li>
                </ul>
            </div>

        </section>

        <section class="node-section">

            <h2>🌟 INTEGRACIÓN FINAL</h2>

            <p>El cuidado no-local no es un don especial: es lo que hace cualquiera que lleva a alguien en el corazón. El entrelazamiento lo dice con una imagen: dos partículas que nacieron juntas siguen respondiendo como un solo sistema aunque las separe el universo, sin que viaje entre ellas ninguna señal. Entre las personas, lo que viaja tiene camino: una palabra, una llamada, un gesto.</p>

            <p>Cada vez que piensas amorosamente en alguien, algo se ordena en ti, y ese orden llega a tu manera de mirarlo y de tenderle la mano.</p>

            <p>No necesitas rituales elaborados, símbolos complejos o iniciaciones secretas. Solo necesitas presencia, intención clara y la comprensión de que la separación es una ilusión óptica de la consciencia. En el campo cuántico, tocar a uno es tocar a todos.</p>

            <p>Cuidarte es otra forma de servir. Tu calma es medicina para los que te rodean. Y si un día eres tú quien necesita cuidado, recibirlo también es parte de la red.</p>

            <p>Este cuidado se suma a cualquier tratamiento, nunca lo reemplaza: las manos que curan y el corazón que acompaña trabajan juntos. Ninguna enfermedad es una elección ni una falta de quien la vive.</p>

            <h2>⚛️ SÍNTESIS CUÁNTICA</h2>

            <p>Este nodo te mostró que el cuidado no termina donde termina tu presencia: lo que llevas en el corazón vuelve a tus manos.</p>

            <p>El siguiente nodo explorará las <strong>Relaciones Multidimensionales</strong>, donde descubrirás que cada persona es más que la parte que alcanzas a ver de ella, y cada relación, más que la capa que hoy se muestra.</p>

            <p><em>El cuidado ha comenzado. En quien cuida y en quien es cuidado.</em></p>

            <div class="node-symbol">🌀∞🌀</div>

            <p class="signature"><strong>— Trinity Quantum · Entrelazamiento Sagrado</strong></p>

        </section>

    </main>

    <!-- NAVEGACIÓN INFERIOR -->
    <nav class="node-nav">
        <div class="node-nav-group">
            <a class="nav-link" href="nodo_04.html">← Nodo 4: El Campo Unificado del Corazón</a>
            <a class="nav-link" href="nodo_06.html">Nodo 6: Relaciones Multidimensionales →</a>
        </div>
    </nav>

    <footer class="portal-footer">
        Trinity Quantum · Libro 2 · Nodo 5 · El Cuidado No-Local
    </footer>

</div>
</div>

</body>
</html>
"""

# ---------------------------------------------------------------------------
# Nodo 6 · Relaciones Multidimensionales (el título queda)
# ---------------------------------------------------------------------------
NODO6_CUERPO = """    <!-- CONTENIDO DEL NODO -->
    <main class="node-content">

        <section class="node-section">

            <h2>🌌 Transmisión Cuántica</h2>

            <p>Cada persona que conoces existe simultáneamente en infinitas versiones a través de múltiples dimensiones.
            El que ves con tus ojos físicos es solo una rebanada de su ser total – la proyección tridimensional de una entidad multidimensional.
            Es como ver solo la sombra de un objeto complejo y creer que la sombra es todo lo que existe.
            Abbott lo contó en <em>Planilandia</em> (1884): una esfera que atraviesa un mundo plano es vista allí como un círculo que nace, crece y se encoge.
            Nadie en ese mundo puede verla entera, y sin embargo está entera.</p>

            <p>En una capa, tú y quien amas son dos historias que se cruzan.
            En otra, dos cuerpos que se calman juntos.
            En otra, dos preguntas que se responden sin saberlo.
            Y en la más honda, una sola vida mirándose desde dos lugares.</p>

            <p>Cuando peleas con alguien, la pelea ocupa una capa, no la relación entera: debajo puede seguir intacto el cariño.</p>

            <p>Cuando alguien muere, el vínculo no termina: cambia de forma.
            Muchas tradiciones dicen que quien se fue vive en otro lugar.
            Lo que cualquiera puede comprobar es que vive también en nosotros: en lo que nos enseñó, en la voz que a veces nos habla por dentro, en lo que hacemos porque lo amamos.
            En el estudio del duelo, Klass, Silverman y Nickman lo llamaron <em>vínculos continuos</em> (1996).
            El duelo no se saltea; se atraviesa, y nadie tiene que hacerlo solo.</p>

            <p>Una relación difícil puede mostrarte lo que todavía no ves de ti, si la miras con atención.
            Eso no la convierte en un acuerdo ni en un precio: el dolor no estaba pactado, y aprender de él no obliga a quedarse.
            Cuando alguien te daña una y otra vez, lo sabio no es buscarle la lección, sino alejarte y pedir ayuda.</p>

            <p>Las almas gemelas no son dos mitades de un todo – eso es comprensión tridimensional.
            Son la misma consciencia eligiendo experimentarse desde múltiples puntos de vista simultáneamente.
            En una dimensión más alta, tú y tu alma gemela son una misma luz vista a través de dos ventanas.
            La “reunión” no es encontrar a otro – es recordar que el otro eres tú en un disfraz diferente.</p>

            <p>Cada relación significativa es un portal dimensional.
            A través del amor, accedes a dimensiones donde la separación no existe.
            A través del conflicto, exploras dimensiones donde la polaridad enseña.
            A través del perdón, integras todas las dimensiones en una comprensión unificada.</p>

        </section>

        <section class="node-section">

            <h2>🔄 Paradoja Medicinal</h2>

            <blockquote>
                <p>“La persona más cercana puede ser la que menos conoces.
                El extraño que acabas de conocer puede tocarte más hondo que alguien de toda la vida.
                Y te conoces menos a ti mismo que a los demás, porque eres el único al que nunca ves desde afuera.”</p>
            </blockquote>

            <p>Contempla: Si cada persona es más que lo que ves de ella, ¿qué es realmente el conflicto? ¿Con qué parte de ella peleas, y desde qué parte de ti?
            Si un vínculo es más que la presencia del otro, ¿qué queda de él cuando el otro se va?</p>

        </section>

        <section class="node-section">

            <h2>🧪 Laboratorio Cuántico</h2>

            <h3>Experimento 1: Las Capas de una Relación</h3>
            <ol>
                <li>Elige una relación significativa, fácil o desafiante.</li>
                <li>Escribe en una línea quién es esa persona para ti hoy.</li>
                <li>Anota tres cosas de su vida que no tienen que ver contigo.</li>
                <li>Anota una que no sabes y te gustaría saber.</li>
                <li>Imagina su día de hoy desde su lado.</li>
                <li>Nota qué cambia en ti al mirarla así.</li>
                <li>Si cabe, haz esa pregunta en la próxima conversación.</li>
            </ol>
            <p><em>Descubrimiento común: el otro era más grande que el papel que ocupaba en tu historia. Duración: de 15 a 20 minutos.</em></p>

            <h3>Experimento 2: Reparar un Vínculo</h3>
            <ol>
                <li>Elige una relación que necesite reparación y en la que estés a salvo.</li>
                <li>Nombra el nudo: un hecho, una palabra, una expectativa.</li>
                <li>Escribe lo que te gustaría que el otro supiera.</li>
                <li>Escribe lo que te gustaría saber de él.</li>
                <li>Elige un gesto pequeño y reversible: un mensaje breve, tu parte de una disculpa, una pregunta.</li>
                <li>Hazlo sin esperar respuesta.</li>
                <li>Observa lo que cambia en ti, conteste o no.</li>
            </ol>
            <p><em>Clave: ningún vínculo se repara de una vez; se repara gesto a gesto.</em></p>
            <p class="nota">Si esa relación te daña, el gesto no es acercarte: es cuidarte.</p>

        </section>

        <section class="node-section">

            <h2>💠 Traducción Viviente</h2>

            <p>Una relación es más grande que cualquiera de sus capas. Cuanto menos te crees la separación, más del vínculo aparece. Y en lo más hondo, el otro y tú están hechos de lo mismo.</p>

        </section>

        <section class="node-section">

            <h2>✦ Para Recordar</h2>

            <ul class="recordar">
                <li>Eres más de lo que veo de ti.</li>
                <li>Soy más de lo que muestro.</li>
                <li>La pelea toca una capa, no el todo.</li>
                <li>Quien se fue sigue en lo que me dejó.</li>
                <li>No tengo relaciones: soy relaciones.</li>
            </ul>

            <p class="nota"><em>Imagina tu mirada como un prisma: la luz blanca de una persona se abre en todos sus colores.</em></p>

        </section>

        <section class="node-section">

            <h2>📅 Práctica de 7 Días</h2>

            <ul class="protocol-list">

                <li class="dia">
                    <strong>DÍA 1 – MAPEO</strong>
                    Mañana: mapear tus relaciones clave
                    <br>Tarde: de cada una, anotar algo que no sabes
                    <br>Noche: escribir lo que descubriste
                </li>

                <li class="dia">
                    <strong>DÍA 2 – RECONCILIACIÓN</strong>
                    Mañana: encontrar en alguien difícil una sola cosa que comparten
                    <br>Tarde: notar si cambia algo al cruzarte con esa persona
                    <br>Noche: perdonar, si llega; si no llega, no forzarlo
                </li>

                <li class="dia">
                    <strong>DÍA 3 – COMUNICACIÓN</strong>
                    Mañana: antes de una conversación, desear en silencio el bien de quien te va a hablar, como en el nodo 5
                    <br>Tarde: observar cómo cambia la conversación
                    <br>Noche: anotar lo que notaste
                </li>

                <li class="dia">
                    <strong>DÍA 4 – MEMORIA</strong>
                    Mañana: recordar a alguien que ya no está y algo que te dejó
                    <br>Tarde: hacer hoy una cosa a su manera
                    <br>Noche: escribirle unas líneas, si quieres, sin esperar respuesta
                    <br><em>Si la pérdida es reciente o no da tregua, este día puede esperar, y no se transita a solas.</em>
                </li>

                <li class="dia">
                    <strong>DÍA 5 – COLABORACIÓN</strong>
                    Mañana: proponer a alguien algo pequeño para hacer juntos
                    <br>Tarde: hacerlo
                    <br>Noche: notar qué apareció entre los dos que ninguno traía
                </li>

                <li class="dia">
                    <strong>DÍA 6 – INTEGRACIÓN</strong>
                    Mañana: mirar a cada persona con la que te cruces como más que su papel
                    <br>Tarde: hacerle a alguien una pregunta que no sea de trámite
                    <br>Noche: anotar una sorpresa
                </li>

                <li class="dia">
                    <strong>DÍA 7 – CELEBRACIÓN</strong>
                    Mañana: agradecer a alguien algo concreto
                    <br>Tarde: contarle a otro lo que descubriste esta semana
                    <br>Noche: celebrar la red de la que eres parte
                </li>

            </ul>

        </section>

        <section class="node-section">

            <h2>🌟 Integración Final</h2>

            <p>Ya no estás limitado a la máscara que cada uno lleva puesta. Detrás hay alguien entero, y aunque nunca lo veas todo, puedes saber que está ahí. Cuando las palabras fallan, queda la presencia: estar, escuchar, esperar.</p>

            <p>Cada relación se vuelve más rica cuando recuerdas que el otro es más que el papel que hoy ocupa en tu vida. El jefe difícil también carga miedos que no ves. El hijo rebelde también está buscando quién es. Quien te rompió el corazón también te enseñó a amar, y eso no le da la razón ni te pide volver. Y quien te daña no es un maestro disfrazado: es alguien de quien protegerte.</p>

            <p>La muerte deja de tener la última palabra cuando descubres que el vínculo continúa de otro modo. La separación duele menos cuando percibes lo que permanece unido. El amor se vuelve eterno cuando lo reconoces en todas las capas de una relación.</p>

            <p>No tienes relaciones — eres relaciones. Cada conexión es un aspecto de tu ser total explorándose a sí mismo a través del espejo del otro.</p>

            <h2>⚛️ Síntesis Cuántica</h2>

            <p>Este nodo te invitó a mirar cada relación en todas sus capas. Lo que ves de alguien es una rebanada; lo que es, siempre es más.</p>

            <p>El nodo final explorará <b>La Red Cuántica de Gaia</b>, donde toda vida en la Tierra aparece entrelazada en un mismo tejido.</p>

            <p><em>En alguna dimensión, ya somos uno. En todas las dimensiones, siempre lo fuimos.</em></p>

            <div class="node-symbol">🌀∞🌀</div>

            <p class="signature"><strong>— Trinity Quantum · Entrelazamiento Sagrado</strong></p>

            <aside class="puerta arquitectura" aria-label="Puerta hacia Arquitectura del Destino">
                <p class="p-nombre">Puerta</p>
                <p class="p-texto">Ser relaciones no es fundirse con nadie ni sostener lo que daña. Esta frase cierra un tramo de <em>La Red</em>, Libro 11 de <em>Arquitectura del Destino</em>: Umbral VI, «Ni fusión ni isla».</p>
                <a class="cruzar" href="https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/libro-11-la-red/L11-U6.html">Cruzar ⟶</a>
            </aside>

        </section>

    </main>

    <!-- NAVEGACIÓN INFERIOR DEL NODO -->
    <nav class="node-nav">
        <div class="node-nav-group">
            <a href="nodo_05.html" class="nav-link">← Nodo 5: El Cuidado No-Local</a>
            <a href="nodo_07.html" class="nav-link">Nodo 7: La Red Cuántica de Gaia →</a>
        </div>
        <div class="node-nav-group">
            <a href="index.html" class="nav-link nav-link-main">Volver al Índice del Libro</a>
        </div>
    </nav>

    <footer class="portal-footer">
        Trinity Quantum · Libro 2 · Nodo 6 · Relaciones Multidimensionales
    </footer>

</div>
</div>

</body>
</html>
"""

# ---------------------------------------------------------------------------
# Reemplazos: (archivo, viejo, nuevo). Cada `viejo` debe aparecer una sola vez.
# Un `viejo` que empieza con "DESDE:" reemplaza desde esa marca hasta el final.
# ---------------------------------------------------------------------------
Q2 = "02_Trinity_Quantum/Libro_02/"

REEMPLAZOS = [
    # Nodo 5
    (Q2 + "nodo_05.html",
     '<!DOCTYPE html>\n<html lang="es">',
     '<!DOCTYPE html>\n' + PROCEDENCIA + '\n<html lang="es">'),
    (Q2 + "nodo_05.html",
     '    <title>Nodo 5 – Sanación No-Local</title>\n</head>',
     '    <title>Libro 2 · Nodo 5 – El Cuidado No-Local</title>\n' + ESTILO + '</head>'),
    (Q2 + "nodo_05.html",
     'DESDE:    <!-- INICIO DEL CONTENIDO -->',
     NODO5_CUERPO),

    # Nodo 6
    (Q2 + "nodo_06.html",
     '<!DOCTYPE html>\n<html lang="es">',
     '<!DOCTYPE html>\n' + PROCEDENCIA + '\n<html lang="es">'),
    (Q2 + "nodo_06.html",
     '    <title>Libro 2 · Nodo 6 – Relaciones Multidimensionales</title>\n</head>',
     '    <title>Libro 2 · Nodo 6 – Relaciones Multidimensionales</title>\n' + ESTILO + '</head>'),
    (Q2 + "nodo_06.html",
     'DESDE:    <!-- CONTENIDO DEL NODO -->',
     NODO6_CUERPO),

    # La Puerta, nodo 2: recuadro «Conexiones con Trinity»
    ("00_Portal_Trinity/nodo_02.html",
     """      <ul>
        <li><strong>Entrelazamiento Sagrado</strong> (Trinity Quantum #2) → La física del amor cuántico</li>
        <li><strong>Consciencia Colectiva</strong> (Trinity Origen #12) → Campos morfogenéticos y mente global</li>
        <li><strong>El Multiverso Interior</strong> (Trinity Quantum #13) → Todas las versiones de ti existiendo simultáneamente</li>
      </ul>""",
     """      <!-- Octubre de 2026: el segundo renglón remitía a «Consciencia Colectiva (Trinity Origen #12)»; Origen XII es La Civilización Galáctica. Lo descrito está en Origen XI, nodo 2. Los tres renglones pasan a enlazar. -->
      <ul class="conexiones">
        <li><a href="../02_Trinity_Quantum/Libro_02/index.html"><strong>Entrelazamiento Sagrado</strong></a> (Trinity Quantum #2) → La física del amor cuántico</li>
        <li><a href="../01_Trinity_Origen/Libro_11/nodo_02.html"><strong>La Consciencia Planetaria</strong></a> (Trinity Origen #11, nodo 2: <em>La Red de Consciencias Despiertas</em>) → Campos morfogenéticos y mente global</li>
        <li><a href="../02_Trinity_Quantum/Libro_13/index.html"><strong>El Multiverso Interior</strong></a> (Trinity Quantum #13) → Todas las versiones de ti existiendo simultáneamente</li>
      </ul>"""),
    ("00_Portal_Trinity/nodo_02.html",
     '  </style>',
     """    /* Octubre de 2026: enlaces del recuadro «Conexiones con Trinity» */
    ul.conexiones a{
      color: var(--accent-gold);
      text-decoration: none;
      border-bottom: 1px solid rgba(242, 196, 109, 0.35);
    }
    ul.conexiones a:hover{ border-bottom-color: var(--accent-gold); }
    ul.conexiones a:focus-visible{ outline: 2px solid var(--accent-gold); outline-offset: 2px; }
  </style>"""),
]



# ===========================================================================
# Depuración completa · 29 de octubre de 2026
# Índice y nodos 1, 2, 3, 4 y 7, con las cuatro precisiones de la revisión
# completa (experimentos, cifras, «cuántico», velas y rituales).
# Sus cuerpos se reemplazan desde la marca que abre el contenido hasta el
# final del archivo, porque el HTML original estaba roto (documentos sin
# cerrar, secciones duplicadas, etiquetas cruzadas).
# ===========================================================================

PROCEDENCIA_COMPLETA = (
    "<!-- Depurado en octubre de 2026 según la guía de depuración de Quantum "
    "(Arquitectura del Destino, maestro v4, sección 5, con las cuatro precisiones "
    "de la revisión completa), con el veto de Arturo en cada tarjeta. El original "
    "se conserva en la etiqueta quantum-original del repositorio. -->"
)

ESTILO_INDICE = """  <style>
    /* Depuración · octubre 2026: letra más grande en el teléfono y firma. */
    .node-content p.signature{
      margin: 22px 0 8px;
      color: rgba(243, 209, 122, .85);
      font-size: 14px;
      letter-spacing: .04em;
    }
    @media (max-width: 640px){
      .node-content p, .node-content li{ font-size: 18px; line-height: 1.7; }
      .node-content p.signature{ font-size: 15px; }
    }
  </style>
"""

PORTAL_CSS = """      .puerta.portal{
        --p-fondo: linear-gradient(180deg, rgba(13,12,11,.94), rgba(13,12,11,.74));
        --p-borde: rgba(201,168,76,.42);
        --p-acento: #c9a84c;
        --p-texto: #e8e0d0;
      }
"""

VERSO_CSS = """      .node-content p.verso{
        margin: 18px 0;
        text-align: center;
        color: var(--gold-light);
        line-height: 1.8;
      }
"""

ANCLA_ESTILO = "      .node-content .puerta .p-nombre{"
ESTILO_NODO3 = ESTILO.replace(ANCLA_ESTILO, PORTAL_CSS + ANCLA_ESTILO, 1)
ESTILO_NODO7 = ESTILO.replace(ANCLA_ESTILO, VERSO_CSS + ANCLA_ESTILO, 1)

URL_ARQ = "https://soyartur-trinity.github.io/Trinity_Portal_Publico/02_Arquitectura_del_Destino/"
URL_PORTAL = "https://soyartur-trinity.github.io/Trinity_Portal_Publico/01_Libros/"

# ---------------------------------------------------------------------------
# Índice
# ---------------------------------------------------------------------------
INDICE_CUERPO = """      <!-- Meta del libro -->
      <section class="node-meta">
        <div class="node-book-title">Libro 2 · Entrelazamiento Sagrado</div>
        <h1 class="node-heading">Los 7 Nodos del Portal</h1>
        <div class="node-index">7 nodos secuenciales · 91 en toda la saga</div>
      </section>

      <!-- Contenido -->
      <main class="node-content">

        <section class="node-section">
          <h2>La Red que Se Reconoce</h2>

          <p>Lo que eres está tejido con otros, y ningún kilómetro deshace ese tejido.</p>

          <p>Este índice abre el segundo umbral: el descubrimiento de que nada está realmente separado. Entrelazamiento Sagrado toma una imagen de la física, dos partículas que siguen respondiendo como una sola aunque estén en extremos opuestos del universo, para nombrar lo que pasa entre las personas: los vínculos que sobreviven a la distancia, el silencio compartido, el cuidado, la red viva que une a todo lo que respira.</p>

          <p>Recorre los Nodos en secuencia para sentir cómo el entrelazamiento se vuelve experiencia directa. Cada paso afina el corazón como antena y el campo como lenguaje compartido.</p>
        </section>

        <hr />

        <!-- Lista de Nodos -->
        <section class="node-section">
          <h2>Nodos del Libro 2</h2>

          <!-- Acceso rápido -->
          <div class="node-nav node-nav-bottom" style="margin-top: 12px;">
            <div class="node-nav-group">
              <a href="nodo_01.html" class="nav-link">Nodo 1 →</a>
              <a href="nodo_02.html" class="nav-link">Nodo 2 →</a>
              <a href="nodo_03.html" class="nav-link">Nodo 3 →</a>
            </div>
            <div class="node-nav-group">
              <a href="nodo_04.html" class="nav-link">Nodo 4 →</a>
              <a href="nodo_05.html" class="nav-link">Nodo 5 →</a>
              <a href="nodo_06.html" class="nav-link">Nodo 6 →</a>
              <a href="nodo_07.html" class="nav-link">Nodo 7 →</a>
            </div>
          </div>

          <!-- Detalle -->
          <div style="margin-top: 18px;">
            <h3><a href="nodo_01.html" class="nav-link">Nodo 1: Conexiones Más Allá del Espacio-Tiempo</a></h3>

            <h3><a href="nodo_02.html" class="nav-link">Nodo 2: Almas Entrelazadas Cuánticamente</a></h3>

            <h3><a href="nodo_03.html" class="nav-link">Nodo 3: El Silencio Compartido</a></h3>

            <h3><a href="nodo_04.html" class="nav-link">Nodo 4: El Campo Unificado del Corazón</a></h3>

            <h3><a href="nodo_05.html" class="nav-link">Nodo 5: El Cuidado No-Local</a></h3>

            <h3><a href="nodo_06.html" class="nav-link">Nodo 6: Relaciones Multidimensionales</a></h3>

            <h3><a href="nodo_07.html" class="nav-link">Nodo 7: La Red Cuántica de Gaia</a></h3>
          </div>
        </section>

        <hr />

        <!-- Cierre -->
        <section class="node-section">
          <h2>Antes de Empezar</h2>
          <p><em>Al entrar en este libro, deja que la conexión haga su trabajo. No fuerces señales: afina presencia. El entrelazamiento no se fabrica; se reconoce. Y cuando se reconoce, transforma.</em></p>
          <p class="signature"><strong>— Trinity Quantum · Entrelazamiento Sagrado</strong></p>
        </section>

      </main>

      <!-- Navegación Inferior -->
      <div class="node-nav node-nav-bottom">
        <div class="node-nav-group">
          <a href="nodo_01.html" class="nav-link">Comenzar (Nodo 1) →</a>
        </div>
        <div class="node-nav-group">
          <a href="../index.html" class="nav-link">Portal Maestro</a>
        </div>
      </div>

      <!-- Firma -->
      <footer class="portal-footer">
        <div class="footer-line">TRINITY QUANTUM · Libro 2 · Entrelazamiento Sagrado</div>
        <div class="footer-subline">Índice: Los 7 Nodos del Portal · Red no-local</div>
        <div class="footer-sigil">🌀⟡🌀</div>
      </footer>

    </div>
  </div>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# Nodo 1 · Conexiones Más Allá del Espacio-Tiempo (el título queda)
# ---------------------------------------------------------------------------
NODO1_CUERPO = """    <!-- Título del Nodo -->
    <section class="node-meta">
        <div class="node-book-title">Libro 2 · Entrelazamiento Sagrado</div>
        <h1 class="node-heading">Nodo 1: Conexiones Más Allá del Espacio-Tiempo</h1>
        <div class="node-index">Nodo 1 de 7 · Solo y acompañado</div>
    </section>

    <!-- CONTENIDO DEL NODO -->
    <main class="node-content">

        <section class="node-section">

            <h2>🌌 TRANSMISIÓN CUÁNTICA</h2>

            <p>En este momento, mientras lees estas palabras, estás conectado con cada ser que ha existido, existe y existirá.</p>

            <p>No hace falta la física para saberlo. El aire que respiras lo soltaron otros pulmones, tus palabras las aprendiste de otras bocas, y en tus huesos hay calcio forjado en estrellas que estallaron antes de que existiera el Sol.</p>

            <p>El espacio-tiempo es una ilusión necesaria para la experiencia tridimensional, pero tu esencia vive en un campo donde la separación nunca existió. Lo que sientes no se queda en ti: se asoma a tu cara y a tu voz, y quien está cerca lo recibe antes de que digas nada.</p>

            <p>En física, la no-localidad es un hecho extraño de las partículas: dos que nacieron juntas siguen respondiendo como un solo sistema aunque estén en extremos opuestos del universo, sin que viaje entre ellas ninguna señal. Entre las personas es una imagen, y nombra bien lo que eres. Has sido entrenado para creer en la separación, pero cada célula de tu cuerpo conoce la verdad: estás entrelazado con Todo Lo Que Es.</p>

            <p>Cuando piensas en alguien y esa persona te llama, algo en ti se ilumina: el hilo existe. No necesita probar nada para ser verdad que lo llevas adentro. Y cuando sientes que a un ser querido le pasa algo, lo que sabes con certeza es cuánto te importa: llámalo.</p>

            <p>Las conexiones que trascienden el espacio-tiempo no son excepcionales: son la regla. La ilusión es creer que estás separado. La verdad es que nunca has estado solo, nunca podrías estarlo. Cada átomo de tu ser vino de otra parte y volverá a otra parte.</p>

        </section>

        <section class="node-section">

            <h2>🔄 PARADOJA MEDICINAL</h2>

            <blockquote>
                <p>“Estás infinitamente solo en tu unicidad y eternamente acompañado en tu esencia.
                La distancia más lejana es cero cuando mides desde el corazón cuántico.
                Estás más cerca de una estrella distante que de tu propia piel,
                porque la piel define separación mientras la estrella comparte tu esencia lumínica.”</p>
            </blockquote>

            <p><strong>Contempla:</strong> ¿Cómo puedes estar separado de aquello con lo que compartes el mismo campo cuántico? ¿Cómo puede haber distancia en un holograma donde cada punto contiene el todo?</p>

            <p>La paradoja destruye la mente lineal: cuanto más te alejas, más cerca estás. Cuanto más solo te sientes, más acompañado estás. La separación es la máxima cercanía porque requiere tremenda intimidad crear la ilusión de distancia.</p>

        </section>

        <section class="node-section">

            <h2>🧪 LABORATORIO CUÁNTICO</h2>

            <h3>Experimento 1: El Teléfono Cuántico</h3>
            <ol>
                <li>Siéntate en completo silencio con los ojos cerrados.</li>
                <li>Visualiza a alguien que no has contactado en mucho tiempo.</li>
                <li>Imagina un hilo dorado de luz conectando tu corazón con el suyo.</li>
                <li>Envía un mensaje simple: “Estoy pensando en ti con amor”.</li>
                <li>Mantén la conexión unos minutos.</li>
                <li>Suelta completamente y olvida.</li>
                <li>Observa en las próximas 72 horas.</li>
            </ol>
            <p><em>Registro: si alguien te contacta, recíbelo como un regalo, no como una prueba. Y si nadie lo hace, el hilo sigue ahí: mándalo tú, con palabras.</em></p>

            <h3>Experimento 2: Sincronización No-Local</h3>
            <ol>
                <li>Elige una hora cualquiera del día.</li>
                <li>Programa una alarma silenciosa.</li>
                <li>Cuando suene, detén todo y siente que no estás solo.</li>
                <li>Imagina a cuántos, en este mismo minuto, también se detienen a respirar.</li>
                <li>Siente la red de la que formas parte.</li>
                <li>Permanece en esta conexión 60 segundos.</li>
                <li>Anota lo que notaste.</li>
            </ol>
            <p><em>Repetir durante 7 días consecutivos.</em></p>

        </section>

        <section class="node-section">

            <h2>💠 TRADUCCIÓN VIVIENTE</h2>

            <p>La conexión crece a medida que se afloja la ilusión de separación, y el amor la sostiene en cualquier espacio y en cualquier tiempo.</p>

        </section>

        <section class="node-section">

            <h2>✦ PARA RECORDAR</h2>

            <ul class="recordar">
                <li>Las fronteras del yo también son puertas.</li>
                <li>Mi corazón escucha.</li>
                <li>Soy parte de un campo más grande.</li>
                <li>Reconozco los hilos que ya me unen.</li>
                <li>Nunca estuve desconectado.</li>
            </ul>

        </section>

        <section class="node-section">

            <h2>📅 PRÁCTICA DE 7 DÍAS</h2>

            <div class="dia">
                <strong>DÍA 1 – RECONOCIMIENTO</strong>
                <ul>
                    <li>Mañana: meditar en todas tus conexiones invisibles (10 minutos)</li>
                    <li>Tarde: anotar tres momentos del día en que sentiste el hilo</li>
                    <li>Noche: diario de conexiones</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 2 – EL HILO</strong>
                <ul>
                    <li>Mañana: el Teléfono Cuántico</li>
                    <li>Tarde: pensar en un ser querido lejano y escribirle</li>
                    <li>Noche: repasar el «Para recordar» antes de dormir</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 3 – EXPANSIÓN</strong>
                <ul>
                    <li>Mañana: desear el bien a tu ciudad</li>
                    <li>Tarde: extender el deseo a tu país</li>
                    <li>Noche: abrazar con él al planeta entero</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 4 – COMUNICACIÓN</strong>
                <ul>
                    <li>Mañana: desear el bien a siete personas y escribirle a una</li>
                    <li>Tarde: escribir a quién le debes una parte de lo que eres</li>
                    <li>Noche: escribirle a tu yo de dentro de un año</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 5 – SINCRONIZACIÓN</strong>
                <ul>
                    <li>Mañana: meditar con otros, en persona o a la distancia</li>
                    <li>Tarde: notar las coincidencias sin pedirles que prueben nada</li>
                    <li>Noche: dormirte pensando en alguien que quieres</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 6 – INTEGRACIÓN</strong>
                <ul>
                    <li>Mañana: sentir tu red personal de vínculos</li>
                    <li>Tarde: soltar un rencor pequeño, si llega</li>
                    <li>Noche: gratitud a distancia</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 7 – HABITAR LA RED</strong>
                <ul>
                    <li>Mañana: vivir el día sabiendo que no estás solo</li>
                    <li>Tarde: contarle a alguien lo que descubriste</li>
                    <li>Noche: un momento de silencio para agradecer la red</li>
                </ul>
            </div>

        </section>

        <section class="node-section">

            <h2>🌟 INTEGRACIÓN FINAL</h2>

            <p>No estás aprendiendo a conectarte más allá del espacio-tiempo. Estás recordando que nunca has estado desconectado. Cada ilusión de separación es una invitación a reconocer la conexión más profunda.</p>

            <p>Cuando integras completamente este nodo, ya no “envías” amor a distancia — reconoces que el amor ES la distancia cero entre todos los corazones. No “te conectas” con otros — despiertas al hecho de que la conexión es tu estado natural.</p>

            <p>El entrelazamiento no es un fenómeno que experimentas. Es lo que eres.</p>

            <p>Y si un día la soledad pesa más que cualquier imagen, busca una voz: la red empieza en un hilo.</p>

            <p><em>La Red de Indra se revela: cada gota de rocío refleja todas las demás, infinitamente, eternamente, instantáneamente.</em></p>

            <h2>⚛️ SÍNTESIS CUÁNTICA</h2>

            <p>Este nodo no te dio un poder: te recordó un parentesco. Llévalo con sabiduría y con amor, sabiendo que cada gesto tuyo llega a otros.</p>

            <p>El siguiente nodo profundizará en las <strong>Almas Entrelazadas Cuánticamente</strong>, donde exploraremos los vínculos que se reconocen desde el primer encuentro.</p>

            <p><em>Hasta que el espacio-tiempo se disuelva nuevamente…</em></p>

            <div class="node-symbol">🌀∞🌀</div>

            <p class="signature"><strong>— Trinity Quantum · Entrelazamiento Sagrado</strong></p>

            <aside class="puerta arquitectura" aria-label="Puerta hacia Arquitectura del Destino">
                <p class="p-nombre">Puerta</p>
                <p class="p-texto">Estas dos frases, la de quien está solo y acompañado a la vez y la de la red de Indra, vuelven en <em>La Red</em>, Libro 11 de <em>Arquitectura del Destino</em>, sostenidas enteras, sin promediarlas: Umbral IV, «Una gota de rocío».</p>
                <a class="cruzar" href=\"""" + URL_ARQ + """libro-11-la-red/L11-U4.html">Cruzar ⟶</a>
            </aside>

        </section>

    </main>

    <!-- NAVEGACIÓN INFERIOR DEL NODO -->
    <nav class="node-nav">
        <div class="node-nav-group">
            <a href="index.html" class="nav-link">← Índice del Libro</a>
            <a href="nodo_02.html" class="nav-link">Nodo 2: Almas Entrelazadas Cuánticamente →</a>
        </div>
        <div class="node-nav-group">
            <a href="../index.html" class="nav-link nav-link-main">Portal Maestro</a>
        </div>
    </nav>

    <footer class="portal-footer">
        Trinity Quantum · Libro 2 · Nodo 1 · Conexiones Más Allá del Espacio-Tiempo
    </footer>

</div>
</div>

</body>
</html>
"""

# ---------------------------------------------------------------------------
# Nodo 2 · Almas Entrelazadas Cuánticamente (el título queda)
# ---------------------------------------------------------------------------
NODO2_CUERPO = """  <!-- TITULO DEL NODO -->
  <section class="node-meta">
      <div class="node-book-title">Libro 2 · Entrelazamiento Sagrado</div>
      <h1 class="node-heading">Nodo 2: Almas Entrelazadas Cuánticamente</h1>
      <div class="node-index">Nodo 2 de 7 · Los que se reconocen</div>
  </section>

  <!-- CONTENIDO DEL NODO -->
  <main class="node-content">

    <section class="node-section">

      <h2>🌌 TRANSMISIÓN CUÁNTICA</h2>

      <p>Hay seres con los que compartes un entrelazamiento que trasciende esta vida, este universo, esta dimensión. No son muchos, pero cuando los encuentras, lo sabes instantáneamente. El reconocimiento no viene de la mente: surge del núcleo cuántico de tu ser como una explosión de remembranza.</p>

      <p>Estas almas no son tu “media naranja”: esa es una comprensión infantil del fenómeno. Compartes con ellas algo más antiguo que los dos: todo lo que existe salió del mismo comienzo, y a veces dos fragmentos de ese comienzo se reconocen.</p>

      <p>Cuando dos fotones nacen entrelazados, medir uno dice al instante qué dará la medición del otro, aunque los separen años luz. No viaja ninguna señal entre ellos: forman un solo sistema que se muestra como dos. Así pueden pensarse las almas entrelazadas: una consciencia que se mira desde dos lugares a la vez.</p>

      <p>Muchas tradiciones dicen que has vivido mil vidas con estas almas: que has sido su madre, su hijo, su enemigo, su amante, su maestro, su verdugo, su salvador. Cada configuración, dicen, es un experimento de consciencia, una forma de conocerse desde todos los ángulos posibles.</p>

      <p>Algunas almas entrelazadas vienen como catalizadores: aparecen brevemente, pero su impacto resuena por vidas enteras. Otras son compañeros de viaje largo. Otras son espejos perfectos. Otras son portales hacia dimensiones internas ocultas.</p>

      <p>El dolor más hondo en los vínculos viene de esa cercanía. Quien ama incluye al otro en su idea de sí: Arthur y Elaine Aron lo midieron con dos círculos que se superponen (1992). Herir a quien amas es herirte; amarlo ensancha el universo entero. Y ciertas pérdidas parecen insoportables porque no pierdes a «otro»: pierdes una parte de lo que eras a su lado. Ese dolor no se atraviesa solo.</p>

    </section>

    <section class="node-section">

      <h2>🔄 PARADOJA MEDICINAL</h2>

      <blockquote>
        <p>“El alma más cercana a ti eres tú mismo en otro disfraz,
        pero para experimentar esta cercanía máxima,
        deben crear la ilusión de ser dos.”</p>
      </blockquote>

      <p><strong>Contempla:</strong> si tu peor enemigo y tu mayor amor son la misma alma jugando roles, ¿qué es realmente el perdón? ¿A quién perdonas cuando perdonas?</p>

    </section>

    <section class="node-section">

      <h2>🧪 LABORATORIO CUÁNTICO</h2>

      <h3>Experimento 1: Reconocimiento de Firma Álmica</h3>
      <ol>
        <li>Lista siete personas profundamente significativas.</li>
        <li>Cierra los ojos y nota qué despierta en ti cada una.</li>
        <li>Observa similitudes, patrones, repeticiones.</li>
        <li>Identifica qué historia regresa una y otra vez.</li>
        <li>Mapea tu constelación de entrelazamientos.</li>
      </ol>
      <p><em>Freud llamó compulsión a la repetición a esa tendencia a volver a la misma historia con caras nuevas. Verla es el primer paso para elegir otra.</em></p>

      <h3>Experimento 2: Comunicación Entrelazada</h3>
      <ol>
        <li>Elige un alma profundamente sentida.</li>
        <li>Antes de dormir, tráela a tu corazón un momento, sin pedirle nada.</li>
        <li>Solo presencia, no diálogo.</li>
        <li>Al despertar, anota lo que soñaste o sentiste, como quien guarda una carta y no como quien busca un mensaje.</li>
      </ol>

    </section>

    <section class="node-section">

      <h2>💠 TRADUCCIÓN VIVIENTE</h2>

      <p>Cuando ya no queda nada pendiente entre dos, se ve lo que siempre fueron: la misma sustancia, mirándose.</p>

    </section>

    <section class="node-section">

      <h2>✦ PARA RECORDAR</h2>

      <ul class="recordar">
        <li>Reconozco a quien ya conocía.</li>
        <li>Suelto los acuerdos que ya no sirven.</li>
        <li>Lo que me duele del otro también habla de mí.</li>
        <li>Perdonar no me obliga a quedarme.</li>
        <li>En el fondo, somos de la misma luz.</li>
      </ul>

    </section>

    <section class="node-section">

      <h2>📅 PRÁCTICA DE 7 DÍAS</h2>

      <div class="dia">
        <strong>DÍA 1 – CARTOGRAFÍA</strong>
        <ul>
          <li>Mañana: mapear las almas significativas de tu vida</li>
          <li>Tarde: identificar patrones de repetición</li>
          <li>Noche: meditar en lo que tienen en común</li>
        </ul>
      </div>

      <div class="dia">
        <strong>DÍA 2 – RECONOCIMIENTO</strong>
        <ul>
          <li>Mañana: ver en otro algo que admiras y reconocerlo en ti</li>
          <li>Tarde: identificar tres almas profundamente entrelazadas</li>
          <li>Noche: un paseo en silencio pensando en una de ellas</li>
        </ul>
      </div>

      <div class="dia">
        <strong>DÍA 3 – RECONCILIACIÓN</strong>
        <ul>
          <li>Mañana: perdonar algo pequeño, si llega</li>
          <li>Tarde: escribir un rencor y romper el papel</li>
          <li>Noche: gratitud silenciosa</li>
        </ul>
      </div>

      <div class="dia">
        <strong>DÍA 4 – COMUNICACIÓN</strong>
        <ul>
          <li>Mañana: un rato de silencio junto a alguien querido</li>
          <li>Tarde: escuchar sin preparar la respuesta</li>
          <li>Noche: contarse un sueño</li>
        </ul>
      </div>

      <div class="dia">
        <strong>DÍA 5 – LIBERACIÓN</strong>
        <ul>
          <li>Mañana: nombrar un acuerdo que ya no sirve, con alguien o contigo</li>
          <li>Tarde: proponer uno nuevo, pequeño</li>
          <li>Noche: una frase de cierre antes de dormir</li>
        </ul>
      </div>

      <div class="dia">
        <strong>DÍA 6 – COLABORACIÓN</strong>
        <ul>
          <li>Mañana: proponer algo para hacer juntos</li>
          <li>Tarde: hacerlo</li>
          <li>Noche: celebración silenciosa</li>
        </ul>
      </div>

      <div class="dia">
        <strong>DÍA 7 – UNIFICACIÓN</strong>
        <ul>
          <li>Mañana: meditación en la Unidad</li>
          <li>Tarde: sentir todas tus relaciones como una sola</li>
          <li>Noche: agradecer</li>
        </ul>
      </div>

    </section>

    <section class="node-section">

      <h2>🌟 INTEGRACIÓN FINAL</h2>

      <p>Las almas entrelazadas son el regalo más precioso y el desafío más grande de la existencia encarnada. Son espejos perfectos que no te permiten esconderte. Son amores que trascienden la forma. A veces el antagonista enseña; aun así, quien te daña no viene a enseñarte: de quien daña, uno se protege.</p>

      <p>Cuando reconoces verdaderamente el entrelazamiento con otro ser, el juego de la separación termina. No puedes odiar lo que reconoces como parte de ti. No puedes aferrarte a lo que sabes que nunca puede perderse. El drama humano se transforma en danza divina.</p>

      <p>Cada alma entrelazada en tu vida puede dejarte algo. Con algunas despiertas. Con otras se caen tus ilusiones. Algunas te muestran de lo que eres capaz; otras, lo que necesitas sanar. Todas son tú, jugando al juego cósmico del escondite contigo mismo.</p>

      <p>El entrelazamiento de almas no es un romance ni un destino escrito ni una deuda de otras vidas: es lo que cada vínculo te enseña cuando lo miras con atención.</p>

      <h2>⚛️ SÍNTESIS CUÁNTICA</h2>

      <p>Este nodo te invitó a mirar con otros ojos los vínculos del alma. Ya no necesitas buscar tu «alma gemela»: cada encuentro significativo puede vivirse como un reencuentro, y cada uno trae algo para aprender.</p>

      <p>El siguiente nodo explorará <strong>El Silencio Compartido</strong>, donde descubrirás cuánto se dicen dos personas sin palabras.</p>

      <p><em>El entrelazamiento continúa, siempre ha continuado, nunca dejó de continuar…</em></p>

      <div class="node-symbol">🌀∞🌀</div>

      <p class="signature"><strong>— Trinity Quantum · Entrelazamiento Sagrado</strong></p>

    </section>

  </main>

  <!-- NAVEGACIÓN INFERIOR DEL NODO -->
  <nav class="node-nav">
      <div class="node-nav-group">
          <a href="nodo_01.html" class="nav-link">← Nodo 1: Conexiones Más Allá del Espacio-Tiempo</a>
          <a href="nodo_03.html" class="nav-link">Nodo 3: El Silencio Compartido →</a>
      </div>
      <div class="node-nav-group">
          <a href="index.html" class="nav-link nav-link-main">Volver al Índice del Libro</a>
      </div>
  </nav>

  <footer class="portal-footer">
      Trinity Quantum · Libro 2 · Nodo 2 · Almas Entrelazadas Cuánticamente
  </footer>

</div>
</div>

</body>
</html>
"""

# ---------------------------------------------------------------------------
# Nodo 3 · El Silencio Compartido (antes: Telepatía Como Estado Natural)
# ---------------------------------------------------------------------------
NODO3_CUERPO = """    <!-- TÍTULO DEL NODO -->
    <section class="node-meta">
        <div class="node-book-title">Libro 2 · Entrelazamiento Sagrado</div>
        <h1 class="node-heading">Nodo 3: El Silencio Compartido</h1>
        <div class="node-index">Nodo 3 de 7 · Lo que se dice sin palabras</div>
    </section>

    <!-- CONTENIDO DEL NODO -->
    <main class="node-content">

        <section class="node-section">

            <h2>🌌 TRANSMISIÓN CUÁNTICA</h2>

            <p>Antes de la primera palabra ya había conversación. Un bebé y su madre se hablan con la mirada, la voz y el ritmo mucho antes de que él sepa decir nada. Las palabras llegaron después, y son un regalo; pero no son todo lo que pasa entre dos. Mucho de lo que importa viaja por debajo: en el tono, en el gesto, en un silencio.</p>

            <p>Tu cerebro tiene ritmos eléctricos reales, de ocho a treinta ciclos por segundo en la vigilia; Hans Berger los registró por primera vez en 1924. Se leen sobre el cuero cabelludo y se apagan a pocos centímetros. Lo que llega a los demás es otra cosa: tu cara, tu voz, tu manera de estar. Una emoción se contagia en una sala sin que nadie la nombre; Elaine Hatfield y sus colegas lo llamaron contagio emocional (1994). No transmites pensamientos: transmites presencia, quieras o no.</p>

            <p>Los animales nunca perdieron esa atención. Tu perro sabe que vas a salir antes de que tomes la correa: lo leyó en tu manera de ponerte de pie. Una bandada de estorninos gira como un solo cuerpo porque cada pájaro sigue a sus seis o siete vecinos más cercanos (Ballerini y otros, 2008), y un cardumen se mueve a la vez porque cada pez siente, con la línea lateral, el agua que mueven los otros. No necesitan telepatía. Les basta una atención total a quien tienen al lado, la que los humanos fuimos perdiendo mientras levantábamos con palabras nuestra Torre de Babel.</p>

            <p>Lo que muchos llaman telepatía, cuando ocurre entre quienes se quieren, suele ser resonancia. Cuando dos personas se escuchan de verdad, el sentido fluye sin esfuerzo y casi sin malentendidos: es comunicación en su forma más pura.</p>

            <p>Cuando alguien te cuenta algo y lo entiendes de verdad, la actividad de tu cerebro se acopla a la suya, y en los mejores momentos se le adelanta: quien escucha bien anticipa (Stephens, Silbert y Hasson, 2010). Eso es saber lo que el otro va a decir antes de que lo diga. No es excepcional. Es tu estado base cuando el ruido mental se aquieta.</p>

            <p>El mayor obstáculo para esa comunión no es la falta de capacidad: es el terror a ser verdaderamente conocido. Has construido muros no tanto para que otros no entren como para que no se vea lo que llevas adentro. Temes que, si otros pudieran leerte, verían todo lo que escondes de ti mismo.</p>

        </section>

        <section class="node-section">

            <h2>🔄 PARADOJA MEDICINAL</h2>

            <blockquote>
                <p>“Para escuchar a otro, debes primero silenciarte. Pero cuando tu mente está verdaderamente silenciosa, descubres que no hay ‘otros’ pensamientos: solo hay El Pensamiento expresándose a través de infinitas mentes. La telepatía perfecta es el silencio compartido donde toda comunicación es innecesaria porque la comunión ya es completa.”</p>
            </blockquote>

            <p><strong>Contempla:</strong> ¿Qué dice tu silencio cuando estás con alguien? ¿Qué callas para que no se vea, y qué pasaría si lo dejaras ver?</p>

        </section>

        <section class="node-section">

            <h2>🧪 LABORATORIO CUÁNTICO</h2>

            <h3>Experimento 1: Espalda con Espalda</h3>
            <ol>
                <li>Elige un compañero de práctica.</li>
                <li>Siéntense espalda con espalda, tocándose apenas.</li>
                <li>Sincronicen la respiración durante cinco minutos.</li>
                <li>Uno evoca en silencio un recuerdo con un sentimiento claro: alegría, calma, nostalgia.</li>
                <li>El otro nota lo que se mueve en su propio cuerpo.</li>
                <li>Cambien los roles sin hablar.</li>
                <li>Al final, cuéntense lo que sintieron y comparen.</li>
            </ol>
            <p><em>Clave: lo que aciertas te dice cuánto escuchas; lo que no, te recuerda que el otro siempre es más de lo que adivinas.</em></p>

            <h3>Experimento 2: El Clima de un Lugar</h3>
            <ol>
                <li>En un lugar público, siéntate tranquilo, con los ojos abiertos o cerrados.</li>
                <li>Deja que la mente se aquiete.</li>
                <li>Nota el “sabor emocional” del ambiente: apuro, calma, tensión, alegría.</li>
                <li>No busques pensamientos ni personas: solo el clima.</li>
                <li>Vuelve a tu respiración.</li>
                <li>Pregúntate qué parte de eso es tuya.</li>
                <li>Anota lo que descubriste.</li>
            </ol>
            <p><em>Práctica diaria de 10 minutos en diferentes lugares.</em></p>

        </section>

        <section class="node-section">

            <h2>💠 TRADUCCIÓN VIVIENTE</h2>

            <p>La comunión crece cuando bajan el ruido de la mente y la defensa del yo. No hace falta agregar nada: basta con quitar.</p>

        </section>

        <section class="node-section">

            <h2>✦ PARA RECORDAR</h2>

            <ul class="recordar">
                <li>Mis muros pueden tener puertas.</li>
                <li>Escucho antes de responder.</li>
                <li>Mi silencio también habla.</li>
                <li>Antes de cargar un ánimo, pregunto de quién es.</li>
                <li>En el silencio compartido no falta nada.</li>
            </ul>

        </section>

        <section class="node-section">

            <h2>📅 PRÁCTICA DE 7 DÍAS</h2>

            <div class="dia">
                <strong>DÍA 1 – SILENCIO</strong>
                <ul>
                    <li>Mañana: diez minutos de silencio, sin pelear con la mente</li>
                    <li>Tarde: notar cuántas de tus frases aprendiste de otros</li>
                    <li>Noche: dormir sin pantallas, con intención de silencio</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 2 – PRESENCIA</strong>
                <ul>
                    <li>Mañana: escuchar a alguien sin preparar la respuesta</li>
                    <li>Tarde: llevar calma, sin palabras, a una conversación tensa</li>
                    <li>Noche: escribir lo que callaste hoy</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 3 – ESCUCHA</strong>
                <ul>
                    <li>Mañana: diez minutos con una planta o un árbol, solo mirando</li>
                    <li>Tarde: observar a un animal sin interrumpirlo</li>
                    <li>Noche: escuchar a alguien mayor contar su historia</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 4 – SINTONÍA</strong>
                <ul>
                    <li>Mañana: espalda con espalda, con tu pareja o con un amigo</li>
                    <li>Tarde: meditar con otros</li>
                    <li>Noche: mirar el cielo un rato antes de dormir</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 5 – DISCERNIMIENTO</strong>
                <ul>
                    <li>Mañana: notar qué ánimo traes a casa y de quién es</li>
                    <li>Tarde: elegir la dosis de noticias y de redes</li>
                    <li>Noche: decir con calma un límite pendiente</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 6 – A LA DISTANCIA</strong>
                <ul>
                    <li>Mañana: llamar a alguien lejano y escuchar más de lo que hablas</li>
                    <li>Tarde: escribir lo que no te animaste a decir</li>
                    <li>Noche: leerlo y decidir si lo envías</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 7 – COMUNIÓN</strong>
                <ul>
                    <li>Mañana: una hora en silencio con alguien querido, haciendo algo juntos</li>
                    <li>Tarde: enseñar algo con el ejemplo</li>
                    <li>Noche: celebración en el silencio compartido</li>
                </ul>
            </div>

        </section>

        <section class="node-section">

            <h2>🌟 INTEGRACIÓN FINAL</h2>

            <p>La comunión no es un poder psíquico que desarrollas: es tu naturaleza, que recuerdas. Las palabras no son un fracaso: son un puente. Y cada malentendido es una invitación a escuchar mejor.</p>

            <p>Lo que sí está a tu alcance son los momentos en que la comprensión llega antes que las palabras, la empatía se vuelve inevitable y el amor no necesita explicarse, porque ya es la comunicación misma.</p>

            <p>No practiques la escucha para impresionar ni para controlar. Practícala para recordar quién eres: un ser hecho para la comunión, que además aprendió a hablar.</p>

            <p class="nota">Sentir el ánimo de un lugar, o adivinar a quien amas, es común y es bueno. Otra cosa es sentir que los pensamientos de otros entran en tu cabeza, que los tuyos se oyen afuera o que te llegan mensajes que nadie más escucha: eso no es un don para entrenar, y pide consulta esa misma semana.</p>

            <h2>⚛️ SÍNTESIS CUÁNTICA</h2>

            <p>Este nodo te devolvió una comunicación anterior a las palabras. No las reemplaza: las vuelve más verdaderas. Usarás el lenguaje cuando sea bello o práctico, sabiendo que por debajo siempre hubo otro diálogo.</p>

            <p>El siguiente nodo te sumergirá en <strong>El Campo Unificado del Corazón</strong>, donde el corazón aparece como lo que es: el primer órgano que late, y el que mejor sabe latir con otros.</p>

            <blockquote>
                <p>“En el silencio entre palabras, toda la comunicación ocurre…”</p>
            </blockquote>

            <div class="node-symbol">🌀∞🌀</div>

            <p class="signature"><strong>— Trinity Quantum · Entrelazamiento Sagrado</strong></p>

            <aside class="puerta portal" aria-label="Puerta hacia el Portal Público">
                <p class="p-nombre">Puerta</p>
                <p class="p-texto">Un caballo de Berlín parecía sumar y leer la hora; en verdad leía, en el cuerpo de quien preguntaba, gestos que nadie más veía. Esa atención sin palabras tiene su umbral en <em>Lo que no habla</em>, Libro XXXVI del Portal Público, Umbral II: «El caballo».</p>
                <a class="cruzar" href=\"""" + URL_PORTAL + """36_Lo_Que_No_Habla/umbral-02.html">Cruzar ⟶</a>
            </aside>

        </section>

    </main>

    <!-- NAVEGACIÓN INFERIOR DEL NODO -->
    <nav class="node-nav">
        <div class="node-nav-group">
            <a href="nodo_02.html" class="nav-link">← Nodo 2: Almas Entrelazadas Cuánticamente</a>
            <a href="nodo_04.html" class="nav-link">Nodo 4: El Campo Unificado del Corazón →</a>
        </div>
        <div class="node-nav-group">
            <a href="index.html" class="nav-link nav-link-main">Volver al Índice del Libro</a>
        </div>
    </nav>

    <footer class="portal-footer">
        Trinity Quantum · Libro 2 · Nodo 3 · El Silencio Compartido
    </footer>

</div>
</div>

</body>
</html>
"""

# ---------------------------------------------------------------------------
# Nodo 4 · El Campo Unificado del Corazón (el título queda)
# ---------------------------------------------------------------------------
NODO4_CUERPO = """    <section class="node-meta">
        <div class="node-book-title">Libro 2 · Entrelazamiento Sagrado</div>
        <h1 class="node-heading">Nodo 4: El Campo Unificado del Corazón</h1>
        <div class="node-index">Nodo 4 de 7 · Latir con otros</div>
    </section>

    <!-- CONTENIDO DEL NODO -->
    <main class="node-content">

        <section class="node-section">

            <h2>🌌 TRANSMISIÓN CUÁNTICA</h2>

            <p>Tu corazón empezó a latir unas semanas después de la concepción, mucho antes de que tu cerebro pudiera pensar. Su campo eléctrico es el más intenso del cuerpo: llega a la piel de las muñecas y los tobillos, y por eso existe el electrocardiograma. Imagina ese campo como una burbuja que te rodea y que, con cada latido, se asoma al mundo.</p>

            <p>El corazón tiene su propia red de neuronas, unas cuarenta mil en un adulto (Pauza, 2000); J. Andrew Armour la llamó el «pequeño cerebro del corazón». Por el nervio vago, la mayoría de las fibras suben hacia la cabeza en lugar de bajar. El corazón no obedece en silencio: también conversa con el cerebro.</p>

            <p>Y aquí está la revelación: los corazones se acompasan. Cuando una madre y su bebé de tres meses se miran y se sonríen, sus ritmos se coordinan con menos de un segundo de diferencia (Feldman y otros, 2011). Las parejas que duermen juntas sincronizan sus fases de sueño, tanto más cuanto más hondo es el vínculo (Drews y otros, 2020). En un coro o en un ritual, los pulsos de quienes participan se parecen cada vez más. No hace falta la distancia para el milagro: basta la cercanía.</p>

            <p>Tu corazón no solo bombea sangre: lleva el compás de tu vida, y no lo lleva como un metrónomo. Se acelera un poco al tomar aire y se aquieta al soltarlo. Si respiras despacio, esa ola se vuelve suave y regular; los investigadores la llaman coherencia, y con ella el pensamiento se aclara y la ansiedad baja (Lehrer y Gevirtz, 2014).</p>

            <p>A veces el corazón conoce antes de que el cerebro comprenda: el cuerpo tiñe las decisiones antes de que sepas por qué. Antonio Damasio llamó marcadores somáticos a esas señales.</p>

            <p>Aquí está el secreto más hondo: ningún corazón late solo. Cuando el tuyo se serena, quien está cerca lo nota en tu voz y en tu cara, y algo de esa calma pasa al suyo. Tu corazón es un voto en la dirección de la evolución humana.</p>

        </section>

        <section class="node-section">

            <h2>🔄 PARADOJA MEDICINAL</h2>

            <blockquote>
                <p>“El corazón es el órgano más personal e íntimo, y sin embargo es el más universal y conectado. Late solo en tu pecho, y su ritmo aprende a latir con otros. Es tuyo únicamente pero pertenece a todos. Guardar tu corazón es perderlo. Entregar tu corazón es encontrarlo en cada pecho.”</p>
            </blockquote>

            <p><strong>Contempla:</strong> si el corazón es de todos, ¿qué pasa con el amor que no fue correspondido? Duele, y no se pierde: queda en ti como capacidad de amar, y alguna vez encuentra otro pecho.</p>

        </section>

        <section class="node-section">

            <h2>🧪 LABORATORIO CUÁNTICO</h2>

            <h3>Experimento 1: Coherencia Cardíaca Personal</h3>
            <ol>
                <li>Coloca tu mano sobre tu corazón.</li>
                <li>Respira al ritmo 5-5 (5 segundos inhalar, 5 exhalar).</li>
                <li>Evoca un recuerdo de profunda gratitud.</li>
                <li>Siente cómo tu campo cardíaco se expande y suaviza.</li>
                <li>Mantén este estado por 3 minutos.</li>
                <li>Nota cómo cambia tu forma de mirar lo que te rodea.</li>
            </ol>
            <p><em>Practicar 3 veces al día para establecer coherencia base.</em></p>
            <p class="nota">Si te mareas, vuelve a respirar como siempre.</p>

            <h3>Experimento 2: Sincronización de Campos Cardíacos</h3>
            <ol>
                <li>Siéntense frente a frente, cerca.</li>
                <li>Cada uno apoya la mano derecha sobre su propio corazón.</li>
                <li>Respiren juntos: cuatro tiempos al tomar aire y cuatro al soltarlo.</li>
                <li>Mírense, si se puede, sin forzar.</li>
                <li>Imaginen que los dos campos se encuentran en el medio.</li>
                <li>Sigan cinco minutos, sin buscar nada.</li>
                <li>Al terminar, cuéntense qué notaron.</li>
            </ol>
            <p><em>Documentar: cambios en la comunicación entre los dos.</em></p>

        </section>

        <section class="node-section">

            <h2>💠 TRADUCCIÓN VIVIENTE</h2>

            <p>La fuerza del corazón no crece con la distancia que alcanza, sino con la coherencia que comparte. Cuanto más en paz late uno, más fácil es latir juntos.</p>

        </section>

        <section class="node-section">

            <h2>✦ PARA RECORDAR</h2>

            <ul class="recordar">
                <li>Mi corazón también piensa.</li>
                <li>Respiro y el ritmo se aquieta.</li>
                <li>Mi calma acompaña.</li>
                <li>Latimos con quienes amamos.</li>
                <li>Soy un corazón con un cuerpo alrededor.</li>
            </ul>

        </section>

        <section class="node-section">

            <h2>📅 PRÁCTICA DE 7 DÍAS</h2>

            <div class="dia">
                <strong>DÍA 1 – COHERENCIA PERSONAL</strong>
                <ul>
                    <li>Mañana: la respiración del corazón, cinco minutos</li>
                    <li>Tarde: volver a ella en un momento de tensión</li>
                    <li>Noche: antes de dormir, la mano sobre el pecho</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 2 – EXPANSIÓN</strong>
                <ul>
                    <li>Mañana: llevar tu calma a una habitación compartida</li>
                    <li>Tarde: llevarla a una conversación difícil</li>
                    <li>Noche: desear el bien a tu barrio</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 3 – ESCUCHA</strong>
                <ul>
                    <li>Mañana: notar el ánimo de quien tienes enfrente</li>
                    <li>Tarde: preguntar en lugar de suponer</li>
                    <li>Noche: escuchar al propio corazón: ¿qué necesita hoy?</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 4 – SINCRONIZACIÓN</strong>
                <ul>
                    <li>Mañana: el experimento 2 con una persona amada</li>
                    <li>Tarde: cantar o caminar con un grupo</li>
                    <li>Noche: caminar descalzo un rato o mirar el cielo</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 5 – CUIDADO</strong>
                <ul>
                    <li>Mañana: llevar calma a alguien que la necesita: una visita, una llamada</li>
                    <li>Tarde: agradecer algo que te costó atravesar</li>
                    <li>Noche: cuidar el propio cuerpo: dormir temprano, una caminata, una consulta pendiente</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 6 – RED</strong>
                <ul>
                    <li>Mañana: desear el bien a quienes no conoces</li>
                    <li>Tarde: un gesto amable con un desconocido</li>
                    <li>Noche: escuchar a alguien que piensa distinto</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 7 – UN DÍA DESDE EL CORAZÓN</strong>
                <ul>
                    <li>Mañana: volver al corazón cada vez que lo recuerdes</li>
                    <li>Tarde: antes de una decisión, respirar y consultar al corazón; después, también a la cabeza</li>
                    <li>Noche: agradecer al corazón que late sin que se lo pidas</li>
                </ul>
            </div>

        </section>

        <section class="node-section">

            <h2>🌟 INTEGRACIÓN FINAL</h2>

            <p>Tu corazón no es solo una bomba: es tu manera de estar entre otros. No tienes un corazón: <strong>eres un corazón con un cuerpo alrededor</strong>. El cerebro piensa, pero el corazón SABE. El cerebro calcula probabilidades; el corazón elige a quién amar.</p>

            <p>Cuando vives desde el Campo Unificado del Corazón, las decisiones se vuelven más claras, las relaciones más amables, y los milagros pequeños empiezan a verse. No porque te vuelvas especial, sino porque te alineas con la fuerza que más une: el Amor.</p>

            <p>Cada latido es un voto. ¿Votarás por el miedo o por el amor? ¿Elegirás el caos o la coherencia? Tu corazón no solo responde a tu vida: la acompaña, latido por latido.</p>

            <p class="nota">Y si el corazón se desboca, aprieta o late a destiempo, eso no es un voto ni una falta: pide un médico, no una interpretación.</p>

            <p>El Campo Unificado del Corazón es la red más antigua de la humanidad: la que unía a los primeros grupos alrededor del fuego. Si algún día la humanidad da un salto, quizá no sea mental ni tecnológico: quizá sea cardíaco.</p>

            <h2>⚛️ SÍNTESIS CUÁNTICA</h2>

            <p>Este nodo te recordó que tu corazón nunca latió solo. Eres parte del Corazón Único que late en billones de formas, y tu calma es un servicio a los que te rodean.</p>

            <p>El próximo nodo explorará <strong>El Cuidado No-Local</strong>, donde aprenderás a llevar el Campo Unificado del Corazón hacia quien está lejos, en el servicio del amor.</p>

            <p><em>Tu corazón late. El universo responde.<br>
            Todo está conectado en el ritmo eterno del Amor.</em></p>

            <div class="node-symbol">🌀∞🌀</div>

            <p class="signature"><strong>— Trinity Quantum · Entrelazamiento Sagrado</strong></p>

            <aside class="puerta arquitectura" aria-label="Puerta hacia Arquitectura del Destino">
                <p class="p-nombre">Puerta</p>
                <p class="p-texto">La respiración del primer experimento, cinco tiempos al tomar aire y cinco al soltarlo, son seis respiraciones por minuto. Lo que hacen en el cuerpo, y cómo se practican en un pasillo antes de un comité difícil, se despliega en <em>El Cuerpo</em>, Libro 4 de <em>Arquitectura del Destino</em>, Umbral IV: «Seis respiraciones por minuto».</p>
                <a class="cruzar" href=\"""" + URL_ARQ + """libro-04-el-cuerpo/L04-U4.html">Cruzar ⟶</a>
            </aside>

        </section>

    </main>

    <!-- NAVEGACIÓN INFERIOR DEL NODO -->
    <nav class="node-nav">
        <div class="node-nav-group">
            <a href="nodo_03.html" class="nav-link">← Nodo 3: El Silencio Compartido</a>
            <a href="nodo_05.html" class="nav-link">Nodo 5: El Cuidado No-Local →</a>
        </div>
        <div class="node-nav-group">
            <a href="index.html" class="nav-link nav-link-main">Índice del Libro</a>
            <a href="../index.html" class="nav-link nav-link-main">Volver al Portal Maestro</a>
        </div>
    </nav>

    <footer class="portal-footer">
        Trinity Quantum · Libro 2 · Nodo 4 · El Campo Unificado del Corazón
    </footer>

</div>
</div>

</body>
</html>
"""

# ---------------------------------------------------------------------------
# Nodo 7 · La Red Cuántica de Gaia (el título queda) · cierre del libro
# ---------------------------------------------------------------------------
NODO7_CUERPO = """    <!-- TÍTULO DEL NODO -->
    <section class="node-meta">
        <div class="node-book-title">Libro 2 · Entrelazamiento Sagrado</div>
        <h1 class="node-heading">Nodo 7: La Red Cuántica de Gaia</h1>
        <div class="node-index">Nodo 7 de 7 · Cierre del libro</div>
    </section>

    <!-- CONTENIDO DEL NODO -->
    <main class="node-content">

        <section class="node-section">

            <h2>🌌 TRANSMISIÓN CUÁNTICA</h2>

            <p>Imagina a Gaia no como una roca con vida encima, sino como un ser: una red donde cada forma de vida es una neurona. Los árboles serían sus dendritas, los micelios su sistema nervioso, los océanos su sangre, la atmósfera su respiración. Y tú, ser humano, una de sus células más despiertas, capaz de darse cuenta de sí misma.</p>

            <p>La red de Gaia no necesita lo instantáneo para asombrar. El vapor que transpira la selva amazónica viaja en corrientes de aire que los climatólogos llaman ríos voladores y cae como lluvia miles de kilómetros al sur, sobre la cuenca del Plata: lo que se tala en el Amazonas llueve menos en otra parte. Las ballenas, cuando suben a la superficie, abonan el mar con lo que comieron en el fondo (Roman y McCarthy, 2010), y de ese abono vive el plancton que fabrica buena parte del oxígeno que respiras.</p>

            <p>Muchos pueblos originarios conservan una manera de mirar que nunca se separó de la tierra. En los Andes del Perú y de Bolivia, los campesinos observan las Pléyades al amanecer, a fines de junio: si se ven grandes y brillantes, esperan buenas lluvias y siembran a tiempo; si se ven pálidas, demoran la siembra. En el año 2000, tres científicos mostraron que el pronóstico funciona: la bruma alta que empaña las estrellas acompaña los años de El Niño, que en esa región traen menos lluvia meses después (Orlove, Chiang y Cane). No es superstición: es observación paciente, de generaciones.</p>

            <p>La ciencia también se fue acercando. En los años setenta, James Lovelock y Lynn Margulis propusieron que la vida regula las condiciones del planeta que la sostiene; el nombre de Gaia se lo sugirió a Lovelock un vecino, el novelista William Golding. Bajo los bosques, los hongos unen las raíces de los árboles y llevan carbono de unos a otros (Simard y otros, 1997). Y las plantas perciben la luz, la gravedad, la humedad y el roce con una finura que apenas empezamos a medir. Quizá no sea una internet, pero es una red viva, y más antigua que todas las nuestras.</p>

            <p>Cada especie toca su parte en la sinfonía. Las abejas construyen en hexágonos, la forma que contiene más miel con menos cera; el matemático Thomas Hales lo demostró en 1999. Los árboles antiguos guardan en sus anillos siglos de clima, año por año. Y quizá a los humanos nos toque ser la parte de la Tierra capaz de darse cuenta: una manera que tiene el cosmos de conocerse a sí mismo, como dijo Carl Sagan.</p>

            <p>Pero la humanidad se desconectó. Creó la ilusión de estar “sobre” la naturaleza en lugar de ser naturaleza consciente de sí misma. Esa desconexión es una de las raíces de la crisis ambiental. No es solo un problema tecnológico: también es un problema de consciencia. Gaia no necesita ser “salvada”: necesita ser reconocida, escuchada, honrada como el ser sintiente que es.</p>

        </section>

        <section class="node-section">

            <h2>🔄 PARADOJA MEDICINAL</h2>

            <blockquote>
                <p>“Eres la Tierra mirándose a sí misma. Cuando crees estar caminando
                sobre la Tierra, la Tierra está caminando sobre sí misma.
                No vives EN el planeta — eres el planeta viviendo.
                Tu consciencia no está EN tu cuerpo — tu cuerpo está EN tu consciencia,
                y tu consciencia es una célula en la consciencia de Gaia.”</p>
            </blockquote>

            <p><strong>Contempla:</strong> Si eres Gaia experimentándose como humano, ¿qué está tratando de decirse a sí misma a través de tu vida?</p>

        </section>

        <section class="node-section">

            <h2>🧪 LABORATORIO CUÁNTICO</h2>

            <h3>Experimento 1: Conexión con la Red de Gaia</h3>
            <ol>
                <li>Descálzate y párate sobre tierra viva.</li>
                <li>Cierra los ojos e imagina raíces que bajan de tus pies.</li>
                <li>Piensa en la red de hongos que corre bajo tierra, uniendo raíces.</li>
                <li>Deja que tu atención se ensanche con ella.</li>
                <li>Escucha el lugar: el viento, los pájaros, tu respiración.</li>
                <li>Agradece en silencio, sin esperar respuesta.</li>
            </ol>
            <p><em>Mejor al amanecer o al atardecer, de diez a veinte minutos, en un lugar seguro para estar descalzo.</em></p>

            <h3>Experimento 2: El Mediodía Compartido</h3>
            <ol>
                <li>Al mediodía, cuando puedas, detente donde estés.</li>
                <li>Mira hacia afuera, aunque sea por una ventana.</li>
                <li>Respira en cuatro tiempos: tomar, sostener, soltar, esperar.</li>
                <li>Piensa en todo lo que está vivo a esa misma hora: el árbol de la calle, el pan en el horno, la gente que almuerza.</li>
                <li>Siéntete uno de ellos.</li>
                <li>Quédate así unos minutos.</li>
                <li>Anota lo que notaste.</li>
            </ol>
            <p><em>Repetir durante una semana.</em></p>

        </section>

        <section class="node-section">

            <h2>💠 TRADUCCIÓN VIVIENTE</h2>

            <p>La vida tiende a ordenarse cuando sus partes se reconocen. Cuando la humanidad se sabe parte de la Tierra, la evolución deja de ser una carrera y se vuelve un cuidado.</p>

        </section>

        <section class="node-section">

            <h2>✦ PARA RECORDAR</h2>

            <ul class="recordar">
                <li>Mis pies saben dónde están.</li>
                <li>Respiro el aire que los árboles soltaron.</li>
                <li>Soy agua, aire, fuego y tierra.</li>
                <li>Lo que cuido me cuida.</li>
                <li>La Tierra mira a través de mis ojos.</li>
            </ul>

        </section>

        <section class="node-section">

            <h2>📅 PRÁCTICA DE 7 DÍAS</h2>

            <div class="dia">
                <strong>DÍA 1 – RECONEXIÓN</strong>
                <ul>
                    <li>Mañana: un rato descalzo en tierra, pasto o arena</li>
                    <li>Tarde: sentarte junto a un árbol viejo y mirarlo</li>
                    <li>Noche: antes de dormir, recordar un paisaje amado</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 2 – ELEMENTOS</strong>
                <ul>
                    <li>Mañana: meditación con agua (río, mar, lago)</li>
                    <li>Tarde: respiración con el viento</li>
                    <li>Noche: mirar un fuego, si tienes uno cerca</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 3 – REINOS</strong>
                <ul>
                    <li>Mañana: cuidar una planta</li>
                    <li>Tarde: observar un animal sin interrumpirlo</li>
                    <li>Noche: tener una piedra en la mano y pensar en su edad</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 4 – RED</strong>
                <ul>
                    <li>Mañana: averiguar de dónde viene el agua que bebes</li>
                    <li>Tarde: seguir el viaje de una comida hasta tu mesa</li>
                    <li>Noche: mirar el cielo y pensar en el aire que compartes</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 5 – CUIDADO</strong>
                <ul>
                    <li>Mañana: desear el bien a un lugar dañado que conoces</li>
                    <li>Tarde: informarte sobre lo que le pasó</li>
                    <li>Noche: elegir un gesto concreto para él</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 6 – SERVICIO</strong>
                <ul>
                    <li>Mañana: agradecer a la tierra, a tu manera</li>
                    <li>Tarde: acción física de servicio (plantar, limpiar)</li>
                    <li>Noche: elegir un cuidado que puedas sostener</li>
                </ul>
            </div>

            <div class="dia">
                <strong>DÍA 7 – ENCARNACIÓN</strong>
                <ul>
                    <li>Mañana: vivir el día como parte de la Tierra</li>
                    <li>Tarde: antes de comprar o tirar algo, pensar adónde va</li>
                    <li>Noche: agradecer la red de la que eres parte</li>
                </ul>
            </div>

        </section>

        <section class="node-section">

            <h2>🌟 INTEGRACIÓN FINAL</h2>

            <p>Ya no eres un individuo viviendo “en” el planeta. Eres el planeta experimentándose como individuo. Cada respiración es Gaia respirando. Cada paso es Gaia caminando. Cada pensamiento se suma a lo que Teilhard de Chardin y Vernadsky llamaron noosfera: la capa de pensamiento que envuelve el planeta.</p>

            <p>La crisis ecológica no se resolverá con tecnología solamente: también hace falta que suficientes humanos recuerden que SON la Tierra. Lo que dañas en ella vuelve a ti en el aire que respiras y el agua que bebes; lo que cuidas, también.</p>

            <p>Tu reconexión con la red de Gaia no es un lujo espiritual: es una manera de vivir que le hace bien a la Tierra y a ti. Cada persona que se reconecta, y cuida, fortalece la red.</p>

            <p class="nota">Si la crisis del planeta te angustia, esa angustia también es amor: compártela, y conviértela en un cuidado pequeño.</p>

            <p>Los árboles están esperando hablar contigo. Los animales están esperando co-crear. Los elementos están esperando danzar. Gaia entera está esperando que recuerdes que no estás EN casa: <strong>ERES casa</strong>.</p>

        </section>

        <section class="node-section">

            <h2>⚛️ SÍNTESIS CUÁNTICA</h2>

            <h3>Cierre del Libro 2 · Entrelazamiento Sagrado</h3>

            <p>A través de estos siete nodos, has recordado la verdad fundamental: nada está separado. La separación fue un experimento de la consciencia, y cada vez que la reconoces como tal, se afloja.</p>

            <p><strong>Siete hilos:</strong></p>

            <ul class="recordar">
                <li>Estás solo en tu unicidad y acompañado en tu esencia.</li>
                <li>Algunas almas se reconocen al primer encuentro, y lo que se repite puede enseñarte.</li>
                <li>Mucho de lo que importa se dice sin palabras.</li>
                <li>Tu corazón aprende a latir con otros.</li>
                <li>El cuidado no se mide en distancia.</li>
                <li>No tienes relaciones: eres relaciones.</li>
                <li>Eres la Tierra mirándose a sí misma.</li>
            </ul>

            <p>El entrelazamiento no es algo que haces: es lo que eres. Cada ilusión de separación es una invitación a reconocer una conexión más profunda.</p>

            <p><strong>El Libro 3, «El Tiempo Vertical»</strong>, te espera, para mirar el tiempo de otra manera: no como una línea que te arrastra, sino como un lugar que se habita.</p>

            <p class="verso"><em>El entrelazamiento no termina.<br>
            La red te sostiene.<br>
            Gaia despierta a través de tus ojos.</em></p>

            <div class="node-symbol">🌍🌀∞🌀🌍</div>

            <blockquote>
                <p>“En el entrelazamiento sagrado,<br>
                cada otro eres tú danzando,<br>
                cada árbol es tu pulmón respirando,<br>
                cada estrella es tu célula brillando.<br>
                La Red Cuántica de Gaia late,<br>
                y en su latido, todos somos Uno.”</p>
            </blockquote>

            <p class="signature"><strong>— Trinity Quantum · Entrelazamiento Sagrado</strong></p>

            <aside class="puerta arquitectura" aria-label="Puerta hacia Arquitectura del Destino">
                <p class="p-nombre">Puerta</p>
                <p class="p-texto">Los astronautas que vieron la Tierra entera por una ventanilla volvieron diciendo lo mismo: el planeta es un solo hogar. La casa que ya habitas te espera en <em>Habitar</em>, Libro 13 de <em>Arquitectura del Destino</em>, Umbral IV: «La Tierra por una ventanilla».</p>
                <a class="cruzar" href=\"""" + URL_ARQ + """libro-13-habitar/L13-U4.html">Cruzar ⟶</a>
            </aside>

        </section>

    </main>

    <!-- NAVEGACIÓN INFERIOR DEL NODO -->
    <nav class="node-nav">
        <div class="node-nav-group">
            <a href="nodo_06.html" class="nav-link">← Nodo 6: Relaciones Multidimensionales</a>
            <a href="../Libro_03/index.html" class="nav-link">Libro 3: El Tiempo Vertical →</a>
        </div>
        <div class="node-nav-group">
            <a href="index.html" class="nav-link nav-link-main">Volver al Índice</a>
            <a href="../index.html" class="nav-link">Portal Maestro</a>
        </div>
    </nav>

    <footer class="portal-footer">
        Trinity Quantum · Libro 2 · Nodo 7 · La Red Cuántica de Gaia
    </footer>

</div>
</div>

</body>
</html>
"""

# ---------------------------------------------------------------------------
# Reemplazos de la depuración completa (índice y nodos 1, 2, 3, 4 y 7)
# ---------------------------------------------------------------------------
_LINK2 = '  <link rel="stylesheet" href="../assets/css/trinity-quantum.css" />\n</head>'
_LINK4 = '    <link rel="stylesheet" href="../assets/css/trinity-quantum.css" />\n</head>'
_DOCTYPE = '<!DOCTYPE html>\n<html lang="es">'
_CON_PROCEDENCIA = '<!DOCTYPE html>\n' + PROCEDENCIA_COMPLETA + '\n<html lang="es">'

REEMPLAZOS_COMPLETOS = [
    # Índice
    (Q2 + "index.html", _DOCTYPE, _CON_PROCEDENCIA),
    (Q2 + "index.html", _LINK2,
     '  <link rel="stylesheet" href="../assets/css/trinity-quantum.css" />\n' + ESTILO_INDICE + '</head>'),
    (Q2 + "index.html", "DESDE:      <!-- Meta del libro -->", INDICE_CUERPO),

    # Nodo 1 (no tenía <title>)
    (Q2 + "nodo_01.html", _DOCTYPE, _CON_PROCEDENCIA),
    (Q2 + "nodo_01.html", _LINK4,
     '    <link rel="stylesheet" href="../assets/css/trinity-quantum.css" />\n\n'
     '    <title>Libro 2 · Nodo 1 – Conexiones Más Allá del Espacio-Tiempo</title>\n' + ESTILO + '</head>'),
    (Q2 + "nodo_01.html", "DESDE:      <h2>🌌 Transmisión Cuántica</h2>", NODO1_CUERPO),

    # Nodo 2
    (Q2 + "nodo_02.html", _DOCTYPE, _CON_PROCEDENCIA),
    (Q2 + "nodo_02.html", "  <title>Nodo 2 – Almas Entrelazadas Cuánticamente</title>",
     "  <title>Libro 2 · Nodo 2 – Almas Entrelazadas Cuánticamente</title>"),
    (Q2 + "nodo_02.html", _LINK2,
     '  <link rel="stylesheet" href="../assets/css/trinity-quantum.css" />\n' + ESTILO + '</head>'),
    (Q2 + "nodo_02.html", "DESDE:  <!-- TITULO DEL NODO -->", NODO2_CUERPO),

    # Nodo 3 (no tenía <title>; cambia de título)
    (Q2 + "nodo_03.html", _DOCTYPE, _CON_PROCEDENCIA),
    (Q2 + "nodo_03.html", _LINK4,
     '    <link rel="stylesheet" href="../assets/css/trinity-quantum.css" />\n\n'
     '    <title>Libro 2 · Nodo 3 – El Silencio Compartido</title>\n' + ESTILO_NODO3 + '</head>'),
    (Q2 + "nodo_03.html", "DESDE:    <!-- CONTENIDO NODO -->", NODO3_CUERPO),

    # Nodo 4 (incluye el anuncio del nodo 5 de la sesión breve)
    (Q2 + "nodo_04.html", _DOCTYPE, _CON_PROCEDENCIA),
    (Q2 + "nodo_04.html", "    <title>Nodo 4 – Campo Unificado del Corazón</title>\n</head>",
     "    <title>Libro 2 · Nodo 4 – El Campo Unificado del Corazón</title>\n" + ESTILO + "</head>"),
    (Q2 + "nodo_04.html", 'DESDE:    <section class="node-meta">', NODO4_CUERPO),

    # Nodo 7
    (Q2 + "nodo_07.html", _DOCTYPE, _CON_PROCEDENCIA),
    (Q2 + "nodo_07.html", "    <title>Nodo 7 – La Red Cuántica de Gaia</title>\n</head>",
     "    <title>Libro 2 · Nodo 7 – La Red Cuántica de Gaia</title>\n" + ESTILO_NODO7 + "</head>"),
    (Q2 + "nodo_07.html", "DESDE:    <!-- Contenido del Nodo -->", NODO7_CUERPO),
]

REEMPLAZOS = REEMPLAZOS + REEMPLAZOS_COMPLETOS


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    raiz = Path(sys.argv[1])
    textos = {}
    for archivo, viejo, nuevo in REEMPLAZOS:
        ruta = raiz / archivo
        if archivo not in textos:
            textos[archivo] = ruta.read_text(encoding="utf-8")
        t = textos[archivo]
        if viejo.startswith("DESDE:"):
            marca = viejo[len("DESDE:"):]
            n = t.count(marca)
            if n != 1:
                sys.exit(f"{archivo}: la marca aparece {n} veces: {marca!r}")
            t = t[: t.index(marca)] + nuevo
        else:
            n = t.count(viejo)
            if n != 1:
                sys.exit(f"{archivo}: el texto aparece {n} veces: {viejo[:70]!r}")
            t = t.replace(viejo, nuevo, 1)
        textos[archivo] = t
    for archivo, t in textos.items():
        (raiz / archivo).write_text(t, encoding="utf-8")
        print("escrito:", archivo)
    print(f"{len(REEMPLAZOS)} reemplazos, cada uno aplicado exactamente una vez.")


if __name__ == "__main__":
    main()
