"""
//cemeteries
new Thing("cemetery",["gravedigger,0-2","person,0-3","cemetery shed,0-2","mausoleum,0-3","grave,10-30","ghost,20%","ghost,10%"],"cemetery");
new Thing("gravedigger",[".person","shovel,30%"],"*PERSON*| (gravedigger)");
new Thing("shovel",["wood","metal"]);
new Thing("cemetery shed",["gravedigger,0-2","table,20%","tv,20%","fridge,30%","chair,0-2","shovel,0-3","corpse,1%","ghost,1%",".building"],"shed");
new Thing("mausoleum",["tourist,8%","coffin,1-6","ghost,4%",["concrete","rock","marble"]]);
new Thing("grave",["coffin","coffin,5%","worm,0-2","insect,0-1",["concrete","rock","marble"],"dirt"]);
new Thing("coffin",["person,0.2%","corpse,98%","corpse,2%","ghost,2%","worm,0-3","insect,0-2","wood","cloth","nails"]);

new Thing("ectoplasm",[
    ProtonFactory.multiple(3, 7),
],[["purple","fetid","green","yellow","blood-red","shiny","wispy","sparkly"],[" "],["ectoplasm"]]);
new Thing("ghost",["ghost body","ghost thoughts"],[["depressed","sad","lonely","wailing","screaming","stretching","clinking","sneezing","breathing","screeching","spinning","gasping","moaning","regretful","remorseful","vengeful","friendly neighborhood","skeletal","tentacled","conjoined","grasping","slimy","floating","mournful"],[" "],["ghost","spirit","apparition","phantom","poltergeist","specter","hauntling"]]);
new Thing("ghost body",["ectoplasm"],["\"body\""]);
new Thing("ghost thoughts",["ghost thought","ghost thought,20%"],["thoughts"]);
new Thing("ghost thought",[],["if only - she could hear me -","he needs to know - I'm sorry -","alone - I - wait -","I am so - very lonely -","when - will it end -","will it be - over soon -","do I - deserve this -","I regret - so much -","I miss you - so much -","please - never - ever die -","I must - wait here -","how many - centuries -","such is - my burden -","I cannot - feel a thing -","I have lost - all hope -","abandoned -","I float - forever -","I wander - for how long -","so spooky - right now -","that slime - isn't mine -","I rest - at last -","let's - be pals -","I sense - a presence -","you can - see me?","who you - gonna call -","can you - hear me now -"]);
"""
