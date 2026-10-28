#!/usr/bin/env python3
"""
Depuración breve por riesgo clínico de Quantum 2, *Entrelazamiento Sagrado*,
nodos 5 y 6 (octubre de 2026), con el veto de Arturo en cada tarjeta.
Incluye la corrección del recuadro «Conexiones con Trinity» de La Puerta, nodo 2.

Método (maestro v4, sección 5): cada reemplazo aprobado se aplica exactamente
una vez sobre el original de la etiqueta `quantum-original`. Los nodos 5 y 6
cambian casi enteros y su HTML estaba roto (contenido después de </html>,
<main> sin cerrar), así que su cuerpo se reemplaza desde el comentario que abre
el contenido hasta el final del archivo.

Uso:  python3 depurar_quantum2.py RUTA_AL_REPOSITORIO_Trinity-
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

    # Nodo 4: el anuncio del nodo 5 y su enlace siguen al título nuevo
    (Q2 + "nodo_04.html",
     """    <p>
        El próximo nodo explorará la <strong>Sanación No-Local</strong>,
        donde aprenderás a usar el Campo Unificado del Corazón para sanar a distancia,
        trascendiendo las limitaciones del espacio-tiempo en el servicio del amor.
    </p>""",
     """    <!-- Octubre de 2026: anuncio ajustado al título depurado del nodo 5. Original en la etiqueta quantum-original. -->
    <p>
        El próximo nodo explorará <strong>El Cuidado No-Local</strong>,
        donde aprenderás a llevar el Campo Unificado del Corazón
        hacia quien está lejos, en el servicio del amor.
    </p>"""),
    (Q2 + "nodo_04.html",
     'Siguiente Nodo: Sanación No-Local →',
     'Siguiente Nodo: El Cuidado No-Local →'),

    # Índice del libro
    (Q2 + "index.html",
     'Nodo 5: Sanación No-Local</a>',
     'Nodo 5: El Cuidado No-Local</a>'),

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
