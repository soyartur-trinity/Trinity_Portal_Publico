# Voseo -> tuteo. Claves en minúscula; se conserva la mayúscula inicial.
MAPA = {
 # presente de indicativo / subjuntivo
 'abandonés':'abandones','ahogás':'ahogas','amás':'amas','apagás':'apagas','aprendés':'aprendes',
 'asumís':'asumes','avanzás':'avanzas','cerrás':'cierras','comunicás':'comunicas','conectás':'conectas',
 'confundís':'confundes','conocés':'conoces','creés':'crees','cultivás':'cultivas','decidís':'decides',
 'dejás':'dejas','desconectás':'desconectas','descubrís':'descubres','despersonalizás':'despersonalizas',
 'detenés':'detienes','devolvés':'devuelves','diferenciás':'diferencias','elegís':'eliges','empezás':'empiezas',
 'encontrás':'encuentras','entendés':'entiendes','enviás':'envías','escuchás':'escuchas','esforzás':'esfuerzas',
 'esperás':'esperas','evitás':'evitas','existís':'existes','fracasás':'fracasas','fusionás':'fusionas',
 'gritás':'gritas','hablás':'hablas','hacés':'haces','irritás':'irritas','juzgás':'juzgas','llamás':'llamas',
 'merecés':'mereces','mirás':'miras','navegás':'navegas','necesitás':'necesitas','notás':'notas',
 'ofrecés':'ofreces','pasás':'pasas','pensás':'piensas','perdés':'pierdes','podés':'puedes','ponés':'pones',
 'preferís':'prefieres','preguntás':'preguntas','quemás':'quemas','querés':'quieres','recibís':'recibes',
 'reconocés':'reconoces','respondés':'respondes','retrocedés':'retrocedes','sabés':'sabes','sacás':'sacas',
 'sentís':'sientes','silenciás':'silencias','sobrevivís':'sobrevives','sonreís':'sonríes','sos':'eres',
 'sostenés':'sostienes','sufrís':'sufres','temés':'temes','tenés':'tienes','terminás':'terminas',
 'tolerás':'toleras','trabajás':'trabajas','transformás':'transformas','usás':'usas','vivís':'vives',
 # imperativo
 'anotá':'anota','buscá':'busca','cerrá':'cierra','completá':'completa','cuestioná':'cuestiona',
 'cultivá':'cultiva','dejá':'deja','detené':'detén','empezá':'empieza','entrevistá':'entrevista',
 'envolvé':'envuelve','escuchá':'escucha','evaluá':'evalúa','exhalá':'exhala','expresá':'expresa',
 'hablá':'habla','hacé':'haz','identificá':'identifica','imaginá':'imagina','inhalá':'inhala',
 'llevá':'lleva','marcá':'marca','mirá':'mira','nombrá':'nombra','notá':'nota','pensá':'piensa',
 'preguntá':'pregunta','prestá':'presta','reconocé':'reconoce','recordá':'recuerda','respirá':'respira',
 'respondé':'responde','sostené':'sostén','suspendé':'suspende','tolerá':'tolera','tomá':'toma',
 'trabajá':'trabaja','usá':'usa','traé':'trae','validá':'valida','visualizá':'visualiza','volvé':'vuelve',
 # imperativo con pronombre
 'asegurate':'asegúrate','ayudame':'ayúdame','calmate':'cálmate','decime':'dime','dejame':'déjame',
 'exponete':'exponte','hacelo':'hazlo','imaginate':'imagínate','levantate':'levántate','llamala':'llámala',
 'pedile':'pídele','practicala':'practícala','preguntate':'pregúntate','quedate':'quédate','sentate':'siéntate','notálas':'nótalas','mandále':'mándale',
}
# Formas en -í que también son pretérito de primera persona: solo se cambian donde son imperativo
# (se identifican por el texto que las sigue, dentro del archivo indicado).
IMPERATIVOS_I = [
 ('01_Empatia_Humana/capitulo_01.html', 'Sentí</', None),
]

IMPERATIVOS_I = [
 # (archivo, forma, texto que la sigue, tuteo)
 ('01_Empatia_Humana/capitulo_01.html','Sentí',' tus pies en el suelo. Recordá','Siente'),
 ('01_Empatia_Humana/capitulo_02.html','asumí',' menos.','asume'),
 ('01_Empatia_Humana/capitulo_03.html','Resistí',' el impulso de compartir','Resiste'),
 ('01_Empatia_Humana/capitulo_03.html','sentí',' tus pies en el suelo, y','siente'),
 ('01_Empatia_Humana/capitulo_03.html','elegí',' creer que','elige'),
 ('01_Empatia_Humana/capitulo_03.html','Elegí',' UNA barrera','Elige'),
 ('01_Empatia_Humana/capitulo_04.html','resumí',' lo que entendiste','resume'),
 ('01_Empatia_Humana/capitulo_05.html','Sentí',' tus pies en el suelo.</li>','Siente'),
 ('01_Empatia_Humana/capitulo_05.html','Repetí',' internamente','Repite'),
 ('01_Empatia_Humana/capitulo_05.html','Repetí',' este ciclo','Repite'),
 ('01_Empatia_Humana/capitulo_05.html','Sentí',' realmente la disposición','Siente'),
 ('01_Empatia_Humana/capitulo_06.html','Repetí',' estas frases','Repite'),
 ('01_Empatia_Humana/capitulo_06.html','Repetí',':</p>','Repite'),
 ('01_Empatia_Humana/capitulo_06.html','Repetí',' las mismas frases','Repite'),
 ('01_Empatia_Humana/capitulo_06.html','Expandí',' el deseo','Expande'),
 ('01_Empatia_Humana/capitulo_06.html','Abrí',' los ojos lentamente','Abre'),
 ('01_Empatia_Humana/capitulo_09.html','Escribí',' una carta a tu yo','Escribe'),
 ('01_Empatia_Humana/capitulo_12.html','Elegí',' una. Solo una.','Elige'),
]
# «vos» detrás de estas preposiciones pasa a «ti» («con vos», a «contigo»); en los demás casos, a «tú».
PREPS = {'a','ante','de','desde','en','hacia','para','por','sin','sobre','tras','contra','alrededor'}

# Frases donde el cambio de una palabra no alcanza (archivo, antes, después)
FRASES = [
 ('01_Empatia_Humana/capitulo_11.html', 'No es sobre vos ser "buen aliado." Es sobre justicia.',
  'No es sobre ti ni sobre ser "buen aliado." Es sobre justicia.'),
 ('01_Empatia_Humana/capitulo_05.html', 'la sostenes temporalmente', 'la sostienes temporalmente'),
]
