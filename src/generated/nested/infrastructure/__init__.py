"""
//infrastructure
new Thing("street",["traffic accident,1%","urban life","Person,0-5","driven car,0-20","driven bike,0-3","car,0-5","road","pavement"],[["*PERSON*|"],[" "],["street","avenue","boulevard","road","alley","bend","drive","place","hill","plaza"]]);
new Thing("road",[["asphalt","stone"]]);
new Thing("pavement",["note,3%","coin,4%","stone","dirt,5%"]);

new Thing("asphalt",["Oil",".concrete"]);
new Thing("car",["engine","mechanics","tire,4"],[["parked "],["blue","red","white","black","grey"],[" "],["Chr","F","Chevr","Cad","H","Hyund","Maz","Niss","Suz","Lex","Merc","Aud","Volv"],["ysler","ord","olet","illac","onda","ai","da","an","uki","us","edes","i","o"]]);
new Thing("driven car",["Person,1-4",".car"],[["blue","red","white","black"],[" "],["Chr","F","Chevr","Cad","H","Hyund","Maz","Niss","Suz","Lex","Merc","Aud","Volv"],["ysler","ord","olet","illac","onda","ai","da","an","uki","us","edes","i","o"]]);
new Thing("tire",["Rubber","metal"]);
new Thing("bike",["mechanics","tire,2"]);
new Thing("driven bike",["Person","Person,5%",".bike"],"bike");
//["Chr","F","Chevr","Cad","H","Hyun","Maz","Niss","Suz","Lex","Merc","Aud","Volv"],["ysler","ord","olet","illac","onda","dai","da","an","uki","us","edes","i","o"]
"""
