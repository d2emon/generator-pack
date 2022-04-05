# Inspired by: https://orteil.dashnet.org/nested

"""
//And now, the fun begins!

//How to add a new Thing :
//	new Thing(name,contains,name generator);
//		-name is the referral name for this Thing. Unless a name generator is specified, this name will be the default name for any instances of this Thing.
//		-contains is an array of Things that an instance of this Thing contains, specified by their name.
//			-For example, ["banana"] means this Thing contains exactly 1 instance of a banana. ["banana","orange"] means it contains 1 banana and 1 orange.
//			-["banana","strawberry,25%"] means it will contain 1 banana, and has a 25% probability of also containing a strawberry.
//			-["banana,2-7"] means it will contain between 2 and 7 bananas.
//			-[".banana"] will not include a banana in the Thing; instead, the Thing will contain whatever the banana normally contains.
//			-["banana",["sugar","honey"]] will include a banana, and either sugar or honey. Unfortunately, this does not work with the format ".sugar" or ".honey".
//		-name generator is optional; if specified, the instance of the Thing will be named according to this.
//			It can be either an array containing other arrays (the name will be patched up from an element of each array) or an identifier for the Name function, like *BOOK*.
//			A name generator of [["blue ","red "],["frog","toad"]] will produce names such as "blue frog" or "red toad".

//basic materials and particles
//(these are very rough simplifications, don't hold all the inaccuracies against me)
new Thing("diamond",["carbon"]);
new Thing("oil",["lipids"]);
new Thing("magma",[".rock"]);
new Thing("rock",["silica","aluminium,30%","iron,20%","potassium,20%","sodium,50%","calcium,50%"]);
new Thing("silica",["silicon","oxygen"]);
new Thing("chitin",["carbon","hydrogen","oxygen","nitrogen"]);
new Thing("salt",["chlorine","sodium"]);
new Thing("water",["hydrogen","oxygen"]);
new Thing("fire",["oxygen","carbon"]);
new Thing("ash",["organic matter","carbon"]);
new Thing("dew",["water"]);
new Thing("ice",["water"]);
new Thing("snow",["snowflakes"]);
new Thing("snowflakes",["water"]);
new Thing("ammonia",["hydrogen","nitrogen"]);
new Thing("methane",["hydrogen","carbon"]);
new Thing("hydrogen",[".hydrogen atom"]);
new Thing("hydrogen atom",["proton","electron"],["atoms"]);
new Thing("plastic",["polymers"]);
new Thing("rubber",["polymers"]);
new Thing("polymers",[".glucids"]);
new Thing("alcohol",[".glucids"]);
new Thing("carbon",[".atom"]);
new Thing("sodium",[".atom"]);
new Thing("chlorine",[".atom"]);
new Thing("oxygen",[".atom"]);
new Thing("helium",[".atom"]);
new Thing("potassium",[".atom"]);
new Thing("aluminium",[".atom"]);
new Thing("iron",[".atom"]);
new Thing("copper",[".atom"]);
new Thing("lead",[".atom"]);
new Thing("steel",["iron","carbon"]);
new Thing("gold",[".atom"]);
new Thing("silver",[".atom"]);
new Thing("silicon",[".atom"]);
new Thing("calcium",[".atom"]);
new Thing("nitrogen",[".atom"]);
new Thing("sulfur",[".atom"]);
new Thing("phosphorus",[".atom"]);
//alright, I'm not doing the whole periodic table.
new Thing("proteins",[".molecule"]);
new Thing("lipids",[".molecule"]);
new Thing("glucids",["carbon","hydrogen","oxygen"],"glucose");
new Thing("organic matter",[["proteins","lipids","glucids"],["proteins","lipids","glucids",""],"salt,30%"]);
new Thing("atom",["proton","neutron","electron"],["atoms"]);
new Thing("molecule",["atom"],["molecules"]);
new Thing("proton",["up quark,2","down quark"]);
new Thing("neutron",["down quark,2","up quark"]);
new Thing("electron",["qwubble"]);
new Thing("up quark",["qwubble"]);
new Thing("down quark",["qwubble"]);
new Thing("qwubble",["multiverse,1-5"]);
new Thing("portal",["universe"]);

//universe stuff
new Thing("multiverse",["universe,10-30"],["multiverse","lasagnaverse","doughnutverse","towelverse","baconverse","sharkverse","nestedverse","tastyverse","upverse","downverse","layerverse","clusterverse","metaverse","quantiverse","paraverse","epiverse","alterverse","hypoverse","dimensioverse","planiverse","pluriverse","polyverse","maniverse","stackoverse","antiverse","superverse","upperverse","maxiverse","megaverse","babyverse","tinyverse","retroverse","ultraverse","topoverse","otherverse","bubbleverse","esreverse","versiverse","'verse","cookieverse","grandmaverse"]);
new Thing("universe",["supercluster,10-30"]);
new Thing("supercluster",["galaxy,10-30"],"galactic supercluster");
new Thing("galaxy",["galaxy center","galaxy arm,2-6"]);
new Thing("galaxy arm",["galactic life,5%","dyson sphere,4%","dyson sphere,2%","star system,20-50","nebula,0-12","black hole,20%","black hole,20%"],"arm");
new Thing("galaxy center",["black hole","galactic life,10%","dyson sphere,4%","dyson sphere,2%","star system,20-50","nebula,0-12"],"galactic center");
new Thing("nebula",["galactic life,15%","star,2%","star,2%","star,2%","interstellar cloud,1-6"]);
new Thing("interstellar cloud",["helium","hydrogen","carbon,80%","water,5%","ammonia,5%","nitrogen,5%","iron,5%","sulfur,5%","oxygen,15%"],[["a bright pink","a faint","a fading","a pale","a fluo","a glowing","a green","a bright green","a dark brown","a brooding","a magenta","a bright red","a dark red","a blueish","a deep blue","a turquoise","a teal","a golden","a multicolored","a silver","a dramatic","a luminous","a colossal","a purple","a gold-trimmed","an opaline","a silvery","a shimmering"],[" "],["interstellar cloud"]]);
new Thing("star system",["star","star,3%","visitor planet,5%","future planet,10%","future planet,10%","terraformed planet,50%","terraformed planet,20%","terraformed planet,10%","medieval planet,30%","medieval planet,20%","ancient planet,50%","ancient planet,30%","ancient planet,10%","barren planet,60%","barren planet,40%","barren planet,20%","gas giant,60%","gas giant,40%","gas giant,20%","gas giant,10%","asteroid belt,0-2"]);
new Thing("dyson sphere",["star","star,3%","dyson surface","future planet,1-8","barren planet,60%","barren planet,40%","barren planet,20%","gas giant,60%","gas giant,40%","gas giant,20%","gas giant,10%","asteroid belt,0-2"]);
new Thing("star",["ghost,0.1%","space monster,0.2%","hydrogen","helium"],[["white","faint","yellow","red","blue","green","purple","bright","double","twin","triple","old","young","dying","small","giant","large","pale","dark","hell","horrific","twisted","spectral"],[" star"]]);
new Thing("planet",[".terraformed planet"],"telluric planet");
new Thing("barren planet",["galactic life,10%","rock","ice,50%",".planet composition"],"telluric planet");
new Thing("visitor planet",["visitor city,1-8","visitor installation,2-6","galactic life","rock","ice,50%",".planet composition"],"telluric planet");
new Thing("future planet",["future continent,2-7","ocean,1-7","future sky",".future moon,30%",".planet composition"],"telluric planet");
new Thing("terraformed planet",["continent,2-7","ocean,1-7","terraformed sky",".terraformed moon,30%",".planet composition"],"telluric planet");
new Thing("medieval planet",["medieval continent,2-4","ancient continent,0-3","ocean,1-7","sky",".planet composition"],"telluric planet");
new Thing("ancient planet",["ancient continent,2-7","ocean,1-7","sky",".planet composition"],"telluric planet");
new Thing("planet composition",["planet core","moon,40%","moon,20%","moon,10%"],"planet");
new Thing("moon",["ghost,0.1%","rock","planet core"],[["young","old","large","small","pale","white","dark","black","old"],[" moon"]]);
new Thing("terraformed moon",[".planet composition","continent,1-4","ocean,1-4","sky"],[["young","old","large","small","pale","white","dark","black","old","green","lush","blue","city","colonized","life"],[" moon"]]);
new Thing("asteroid belt",["galactic life,20%","asteroid,10-30"]);
new Thing("earth",[".asteroid belt"],"Earth");
new Thing("asteroid",["space animal,0.5%","rock","ice,30%"],"asteroid");
new Thing("gas giant",["gas giant atmosphere","planet core,50%","moon,0-3","terraformed moon,20%","terraformed moon,10%"]);
new Thing("gas giant atmosphere",["galactic life,10%","helium","hydrogen","water,50%","ammonia,50%","methane,50%"],"atmosphere");
new Thing("planet core",["space monster,0.5%","iron","rock","diamond,2%","magma"],"core");

new Thing("black hole",["inside the black hole"]);
new Thing("inside the black hole",["end of universe note,0.5%","crustacean,0.2%","white hole"]);
new Thing("white hole",["universe"]);
new Thing("42",["universe"]);
new Thing("everything",["universe"]);
new Thing("end of universe note",["pasta,0.1%"],["Help! I'm trapped in a universe factory!","Okay, you can stop clicking now.","I want to get off Mr Orteil's Wild Ride","my sides"]);
new Thing("orteil",["body","orteil psyche","clothing set","computer"],"Orteil");//I do what I want
new Thing("god",[".orteil"],"Orteil");//I'm a fucking god
new Thing("orteil psyche",["orteil thoughts"],"psyche");
new Thing("orteil thoughts",[],["OH MY GOD WHAT ARE YOU DOING HERE TURN BACK IMMEDIATELY","WHAT IS WRONG WITH YOU","WHAT THE HELL GO AWAY","WHAT ARE YOU DOING OH GOD","WHY THE HELL ARE YOU HERE","I DO WHAT I WANT OKAY","NO I DON'T CARE GO AWAY","WHAT DID I EVEN DO TO YOU","OH NO WHY THIS","OKAY JUST <a href=\"http://orteil.deviantart.com\">GO THERE ALREADY</a>","<a href=\"http://twitter.com/orteil42\">WHATEVER</a>"]);
"""
