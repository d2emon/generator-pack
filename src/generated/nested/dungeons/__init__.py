"""
//dungeons
new Thing("dungeon",["dungeon entrance","dungeon entrance,20%","dungeon entrance,20%","dungeon tower,0-3"],[["sunken","lost","buried","dark","forbidden","unholy","cursed","abandoned","forsaken","forgotten","time-lost","haunted","blood","ghostly","hallowed"],[" "],["catacombs","tomb","pit","tunnels","underground","dungeon","mine","shaft","den","fortress","castle","citadel","temple","cathedral","lair","prison"]]);
new Thing("dungeon building",["dungeon walls"],"building");
new Thing("dungeon walls",["door,20%","door,10%",["dungeon wall,4","dungeon wall,4-8"]],"stone walls");
new Thing("dungeon wall",["stone","dirt,20%"],"stone wall");
new Thing("dungeon clutter",["medieval monument,20%","medieval altar,5%","medieval corpse,3%","medieval corpse,1%","pile of treasure,15%","pile of treasure,10%","treasure,15%","potion,20%","medieval clutter,0-2","medieval chest,0-2","medieval chest,20%","medieval table,5%","medieval table,5%","medieval chair,5%","medieval chair,5%","medieval bed,5%","medieval bed,5%","medieval bench,5%","medieval bench,5%","medieval fireplace,5%"]);
new Thing("dungeon tower",["dungeon life",".dungeon clutter",".dungeon building","roof"],"tower");
new Thing("dungeon passage",["dungeon life",".dungeon clutter","dungeon room,60%","dungeon room,40%","dungeon room,15%",".dungeon building"],[["dark","twisting","damp","hidden","engraved","frozen","submerged"],[" "],["tunnel","corridor","passage","hall"]]);
new Thing("dungeon room",["dungeon life",".dungeon clutter","dungeon passage,60%","dungeon passage,40%","dungeon passage,15%",".dungeon building"],[["dark","tall","damp","engraved","circular","frozen","submerged"],[" "],["hall","room","chamber","alcove","antechamber","cell","gardens","arena"]]);
new Thing("dungeon entrance",["dungeon life,50%",".dungeon clutter","dungeon passage","dungeon passage,20%","dungeon passage,5%",".dungeon building"],["entrance"]);
new Thing("dungeon life",[".dungeon monster","insect,10%"],"life");
new Thing("dungeon monster",[["dragon","ghost,1-3","ghost,1-3","wizard","humanoid creature,1-3","humanoid creature,1-3","fairy,1-3","fairy,1-3","giant bug,1-3","giant bug,1-3","small creature,1-6","small creature,1-6","snake,1-3","bear","space animal,1-3","sea monster"]]);
new Thing("humanoid creature",["medieval weapon,50%","medieval weapon,10%","helmet,30%","armor,40%","armor,20%","armor,10%","medieval clothing set","MammalBody","creature thoughts"],[["fel","giant","cursed","undead","decaying","numb","magic-using","steel","obsidian","tribal","berserker","ranger","caster","necromancer","vampiric","master","chieftain","mutated","possessed"],[" "],["goblin","troll","gremlin","gnome","dwarf","catperson","sharkperson","dogperson","footface","cephalite","demon","imp","minotaur","gemperson","zombie"]]);
new Thing("fairy",["fairy body","creature thoughts"],["fairy","pixie","fey","sugarfey","angel","ladyfly"]);
new Thing("fairy body",[["BirdWing,2","InsectWing,2"],".Body"],"body");
new Thing("small creature",["MammalBody","creature thoughts"],[["giant","feral","mutated","distorted","rabid","plated","armored","stalking","dashing","mangy"],[" "],["rat","sloth","dog","behemoth","wolf","boar","mindsucker","brainblower","oaf"]]);
new Thing("giant bug",["insect body","creature thoughts"],[["giant","huge","poisonous","mutated","distorted","magic","plated","armored","stalking","dashing"],[" "],["spider","scorpion","mantis","moth","crab","tarantula"]]);
new Thing("creature thoughts",["creature thought,1-2"],["thoughts"]);
new Thing("creature thought",[],["INTRUDER, INTRUDER!","You no get out of here alive.","This one, mine!","I will suck its blood and then feast on its skin.","I will rejoice in its blood!","How skin tears joyfully under my teeth!","Skin, blood, yes!","Flesh. I crave flesh.","Soft, juicy, scrumptious brains!","Dibs on your skull.","Fresh flesh ahead!","None, you get none of the treasure!","I detect you.","Time for a feast.","Adventurers are so rare these days.","I have spotted you. You be dead soon.","Crisp ribcages are the best.","I will suck its eyeballs from their sockets.","I will tear apart its ribs one by one.","I will bathe in its red juice.","I will strip it of its skin.","I will puncture its heart."]);
"""