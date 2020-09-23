"""
//terrain stuff
new Thing("ocean",["sea water","sea life","beach,10-20",["iceberg,2-6","","","",""],"abyss"]);
new Thing("sea",["sea water","sea life","beach,2-6"],[["great","wide","big","old","young","large","small","dead","shallow","deep","red","yellow","green","blue","orange","brown","grey","black","white","purple","shady","bright","silver"],[" sea"]]);
new Thing("sea water",["Water","Salt"]);
new Thing("iceberg",["bear,30%","bear,10%","Ice"]);
new Thing("beach",["beach life","sand"]);
new Thing("abyss",["sand","abyss life"]);
new Thing("sand",["Silica"]);
new Thing("soil",[["worm,0-2","",""],["insect,0-2","",""],"Silica"],"dirt");
new Thing("mud",[["worm,0-2","",""],["insect,0-2","",""],"Water","Silica"]);

new Thing("river",["river life","Water","soil","mud"],["river","stream","brook","creek"]);
new Thing("lake",["lake life","Water","soil","mud"],["lake","lagoon","pond","marsh","creek","cove"]);
new Thing("plain",["Fire,0.3%","land life","river,0-3","lake,0-1","grass","soil","Snow,5%"],["plain","steppe","valley","canyon","flatland","moor","grassland","prairie","desert","savannah","tundra","wasteland"]);
new Thing("forest",["Fire,0.5%","forest life","river,0-2","trees","grass","humus","soil","Snow,5%"],["forest","woods","copse"]);
new Thing("jungle",["Fire,0.5%","jungle life","river,0-2","jungle trees","grass","humus","soil"],["jungle","rainforest"]);
new Thing("mountain",["mountain life","river,0-3","lake,0-1","cave,30%","cave,30%","cave,20%","trees","soil","Rock","Snow,40%"],["mountain","peak","hill","volcano","bluff","cliff","mesa","plateau"]);
new Thing("cave",["cave life","dragon lair,1%","river,20%","lake,10%","Rock","Iron,2%"],["cave","cavern","grotto"]);

new Thing("ancient plain",["Fire,0.3%","caveman settlement,40%","ancient land life","river,0-3","lake,0-1","grass","soil","Snow,5%"],["plain","steppe","valley","canyon","flatland","moor","grassland","prairie","desert","savannah","tundra","wasteland"]);
new Thing("ancient forest",["Fire,0.5%","caveman settlement,40%","ancient forest life","river,0-2","trees","grass","humus","soil","Snow,5%"],["forest","woods","copse"]);
new Thing("ancient jungle",["Fire,0.5%","caveman settlement,40%","ancient jungle life","river,0-2","jungle trees","grass","humus","soil"],["jungle","rainforest"]);
new Thing("ancient mountain",["caveman settlement,40%","ancient mountain life","ancient cave,30%","ancient cave,20%","ancient cave,10%","river,0-3","lake,0-1","trees","soil","Rock","Snow,40%"],["mountain","peak","hill","volcano","bluff","cliff","mesa","plateau"]);
new Thing("ancient cave",["caveman settlement,65%","wall painting,50%","wall painting,30%","wall painting,30%",".cave"],["cave","cavern","grotto"]);

new Thing("future sky",["sprowseship,4-12",".sky"],"sky");
new Thing("terraformed sky",["plane,1-8","rocketship,20%",".sky"],"sky");
new Thing("sky",["visitor ship,10%","meteorite,3%","sky life","precipitation,50%","cloud,2-8","Oxygen","Carbon","ozone"],"sky");
new Thing("meteorite",["space animal,6%","Ice,60%","Rock","Iron,40%"],"meteorite");
new Thing("ozone",["Oxygen"]);
new Thing("cloud",["Water"]);
new Thing("precipitation",["Water"],["rain","snow","hail","mist","fog","drizzle","storm"]);
"""
