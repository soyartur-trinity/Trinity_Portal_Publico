"""Localismos de los seis primeros libros del Portal Público (19 de noviembre de 2026; Parte IV del documento de
lectura, aprobada por Arturo): «acá» → «aquí», «celular» → «teléfono», «che», «zafar», «chico/chicos», «vereda» y
«de a poco». «Visceral. Celular.» (La Voz Interior, cap. 11) queda: ahí es «de las células».
Se aplica después de tuteo_portal_1_6.py. Uso: python3 localismos_portal_1_6.py RUTA/Trinity_Portal_Publico/01_Libros"""
import os,sys
R=sys.argv[1]
E='01_Empatia_Humana/'; V='02_La_Voz_Interior/'; A='04_Asertividad_Consciente/'
CAMBIOS=[
 (E+'capitulo_02.html','sentido así de chico cuando','sentido así de pequeño cuando',1),
 (E+'capitulo_03.html','"Che, ¿quieres que pidamos pizza?','"Oye, ¿quieres que pidamos pizza?',1),
 (E+'capitulo_03.html','pero estoy acá"','pero estoy aquí"',1),
 (E+'capitulo_03.html','para zafar de las responsabilidades','para librarse de las responsabilidades',1),
 (E+'capitulo_04.html','Desde acá,','Desde aquí,',2),
 (E+'capitulo_04.html','para ti acá?','para ti aquí?',1),
 (E+'capitulo_06.html','estoy acá,','estoy aquí,',1),
 (E+'capitulo_06.html','Estoy acá para','Estoy aquí para',1),
 (E+'capitulo_07.html','esos chicos no lo merecían','esos niños no lo merecían',1),
 (E+'capitulo_07.html','Sin celulares.','Sin teléfonos.',1),
 (E+'capitulo_10.html','acá estoy."','aquí estoy."',1),
 (E+'capitulo_12.html','Si llegaste hasta acá,','Si llegaste hasta aquí,',1),
 (V+'capitulo_06.html','cuaderno/celular','cuaderno/teléfono',1),
 (V+'capitulo_07.html','sin culpa, sin celular)','sin culpa, sin teléfono)',1),
 (V+'capitulo_12.html','Sin celular.','Sin teléfono.',1),
 ('03_Encuentro_Real/nodo_03.html','de a poco','poco a poco',1),
 (A+'capitulo_06.html','sin el celular.','sin el teléfono.',1),
 (A+'capitulo_07.html','el celular que no la dejaba dormir','el teléfono que no la dejaba dormir',None),
 (A+'capitulo_07.html','con el celular debajo','con el teléfono debajo',1),
 (A+'capitulo_07.html','Revisas el celular','Revisas el teléfono',1),
 (A+'capitulo_07.html','revisas el celular por hora','revisas el teléfono por hora',1),
 (A+'epilogo.html','sin celular, sin correos','sin teléfono, sin correos',1),
 ('05_Duelo/duelo_nodo_04.html','salir a la vereda','salir a la calle',1),
]
textos={}; err=[]
for f,v,n,k in CAMBIOS:
    p=os.path.join(R,f); t=textos.get(p) or open(p,encoding='utf-8').read(); c=t.count(v)
    if (k is None and c==0) or (k is not None and c!=k): err.append('%s %r: %d'%(f,v,c)); continue
    textos[p]=t.replace(v,n)
if err: raise SystemExit('\n'.join(err))
for p,t in textos.items(): open(p,'w',encoding='utf-8').write(t)
print('archivos:',len(textos))
