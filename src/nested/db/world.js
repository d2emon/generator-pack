//world subdivisions
new Thing("biome",["plain,1-5",["forest,0-4","jungle,0-4"],"mountain,0-3"]);

new Thing("continent",["country,1-10","sea,1-5"],[["continent of "],["A","Eu","Ame","Ocea","Anta","Atla"],["frica","rtica","ropa","rica","nia","sia","ntide"]]);//[["Eu","A","O","E"],["rt","lt","rm","t","tr","tl","str","s","m","fr"],["a","o","e","i"],["ri","ni","ti","fri","",""],["sia","nia","ca"]]);
new Thing("country",["region,1-10","battlefield,10%",".biome"],[["country of "],["Li","Arme","Le","Molda","Slove","Tur","Afgha","Alba","Alge","Tu","Fran","Baha","Su","Austra","Germa","In","Ara","Austri","Be","Ba","Bra","Ru","Chi","Ja","Tai","Bangla","Gha","Bou","Bo","Tas","Ze","Mon","Mo","Ne","Neder","Spai","Portu","Po","Por","Mol","Bul","Bru","Bur","Gro","Syl","Gui","Da","Gree","Bri","Ita"],["ly","dania","mas","vania","ce","nea","nau","topia","garia","gal","laska","golia","nisia","land","snia","livia","mania","than","nin","pan","wan","zil","ssia","na","rein","lgium","bia","ny","ce","stan","distan","nistan","dan","lia","nia","via","sia","tia","key","desh","dia"]]);
new Thing("region",["capital","city,1-10","village,2-15"],[["north ","east ","south ","west ","north-west ","north-east ","south-west ","south-east ","center ","oversea "],["hilly","rainy","lush","foggy","desertic","green","tropical","rich","barren","scorched"],[" region"]]);

//towns
new Thing("village",["residential area,1-4","commercial area,90%","police station,50%","fire department,40%","museum,5%","library,40%","farm,0-6","factory,0-2","cemetery,60%","research facility,4%"],"village");
new Thing("city",["monument,15%","monument,5%","residential area,4-9","commercial area,1-5","police station","police station,50%","fire department","fire department,50%","museum,40%","library,60%","hospital","farm,0-3","factory,1-4","cemetery","research facility,2%"],"city");
new Thing("capital",["monument,70%","monument,40%","monument,10%","residential area,7-15","commercial area,3-9","police station,2-5","fire department,1-3","museum,1-2","library,1-3","hospital,1-3","farm,0-2","factory,2-6","cemetery","cemetery,50%","research facility,1%"],"capital city");

//buildings
new Thing("monument",["tourist,5-30","souvenir shop,70%","souvenir shop,30%"],"*MONUMENT*");
new Thing("tourist",[".person"],"*PERSON*| (tourist)");

new Thing("commercial area",["street,1-5","bargain shop,60%","bargain shop,30%","souvenir shop,10%","fresh produce shop,60%","pet shop,60%","toy shop,60%","game shop,60%","office building,1-12"]);
new Thing("office building",["building hall","office,6-20",".building"],[["a tall","a stout","an unimpressive","a large","a humongous","a modern","a classic","a historic","a gray","a dull","a white","a black","a concrete","a glass-covered","an impressive","a beautiful","an old-fashioned","a boring","a newly-built","a fancy"],[" "],["office building","skyscraper","building"]]);

new Thing("residential area",["street,1-5","house,5-20","apartment building,0-5"]);
new Thing("house",["fire,0.3%","living-room","kitchen","bathroom,1-3","bedroom,2-5","attic","study,0-2","garden,90%","garage,90%",".building"],[["a small","a large","a big","a cozy","a bland","a boring","an old","a new","a freshly-painted","a pretty","an old-fashioned","a creepy","a spooky","a gloomy","a tall","a tiny","a fine","a happy little"],[" pink"," grey"," green"," yellow"," orange"," red"," blue"," white"," brick"," stone"," wooden","","",""],[" house"]]);
new Thing("apartment",["living-room,90%","kitchen","bathroom,1","bedroom,1-3","study,20%"]);
new Thing("apartment building",["fire,0.3%","apartment,6-20",".building"]);

//farms
new Thing("farm",["fire,0.3%","house,1-3","farmer,1-4","field,1-8","horse,30%","horse,30%","horse,30%","poultry,0-3","grain silo,0-2","barn,0-2","warehouse,0-2","storage shed,0-2"]);
new Thing("field",["grain","insect,5%","bird,10%","bird,5%","haystack,30%"],["wheat field","corn field","soy field","rice field","oat field","peanut field","tomato field","grape field","barley field","canola field","rye field","flower field"]);
new Thing("farmer",[".person"],"*PERSON*| (farmer)");
new Thing("grain",["plant cell"]);
new Thing("grain silo",["metal","grain"]);
new Thing("warehouse",["worker,0-2","small mammal,8%","ghost,0.3%","machine,0-4",".building"]);
new Thing("barn",[".building"]);
new Thing("storage shed",[".building"]);
new Thing("haystack",["grain","insect,10%","needle,0.1%"]);
new Thing("needle",["metal"]);

new Thing("factory",["worker,2-12","machine,1-12","pipes,40%","cables,0-1","public bathroom,60%","warehouse,0-2",".building"],[["toy","chocolate","car","yoghurt","processed food","pork products","canned beef","juice","soda","shoe","textile","computer","weapon","hardware"],[" factory"]]);
new Thing("worker",[".person"],"*PERSON*| (worker)");

new Thing("public bathroom",[".room","person,10%","person,1%","sink,1-4","toilet,1-4","mirror,0-3"],"restroom");

//offices
new Thing("building hall",["office worker,0-3","elevator,1-3","public bathroom,75%"],"entrance hall");
new Thing("elevator",["ghost,0.3%","office worker,0-3","metal","cables","mechanics"]);
new Thing("office",["office worker,0-3","cat,2%","meeting room,0-2","boss's office","cubicle,2-12","water cooler,0-2","public bathroom,75%","elevator"],[["Social","Web","Swift","Smart","Smooth","Huge","Large","Greed","Bank","Media","World","Smith","Channel","Stock","Dream","One","True","We","You","People","Planet","Wild","Standard","Ever","Quick","Fast","Real","Good","Great","Neat","Soft","Hard","Right","Evil","Okay","Nice","Mascot","Clever","Green","Blue","White","Black","Time","Century","Millenium","NotCorrupt","PrettyAlright","PrettyDamnGood","Actual","Apex","Nested","Star","Opti","General","Easy","What","Who","Where","This","That","Dat","Dem","Invest","Painless","Death","First","Shark","Bear","Truth","Trust","Venture","Swell","Kind","Myth","Mythic","Crown","Silver","Gold","Twin","Single","Double","Triple","Marvel","Wonder","Way","Ward","e","I"],["co","alys","isium","arium","orium","orius","arius","aria","oria","arion","orion","ilton","son","cube","Monkey","Dog","Century","Year","TV","Big","Money","Rich","Bucks","Axis","Venture","Fine","Universal","Pro","Unlimited","brothers","Tube","Grow","Friends","Planet","People"," People"," Plastics"," Fashion"," Trending"," TV"," Games"," Toys"," Video Games"," Video"," Sports"," Pets"," Social"," Websites"," Marketing"," Sales"," Trading"," Export"," Politics"," Strategy"," Health"," Medecine"," Gardening"," Agriculture"," Editions"," Mining"," Transports"," Voyages"," Tourism"," Art"," Assassinations"," Healthcare"," Software"," Hardware"," Automobile"," Care"," Education"," Security"," Security Systems"," Crafts"," Production"," Services","Blood"," Space"," Transfer"," Backup"," Resources"," Secret Research"," Banking"," Funding"," Gambling"," Law"," Lawyers"," Pictures"," Religion"," Goods"," Weapons"," Laundering"," Cartoons"," Comics"," Agronomics"," Ergonomics"," Economics"," Supplies"," Things"," Stuff"," Printing"," Architecture"," Landscaping"," Construction"," Railroads"," Engineering"," Science"," News"," Testing"," Appliances"," Standards","Studio"," Recording"," Enrichment"," Extraction"," Frivolities"," Realty"," Publishing"," Entertainment"," Propane"," Energy"," Business Solutions"," Councelling"," Event-planning"," Fundraising"," Electronics"," Electrics"," Records"," Slavery"," Distribution"," Distributors"," Accessories"," Fuels"," Motors"," Insurance","Corp"," Procedurals"],[" "],["Inc.","Corp.","Company","L.P.","Ltd.","L.L.C.","L.C.","Associates","Partners","United","Merger","& Co","International","Conglomerate"]]);
new Thing("office worker",[".person"],"*PERSON*| (employee)");
new Thing("office boss",[".person"],"*PERSON*| (boss)");
new Thing("cubicle",["office worker,80%","office worker,10%","computer","computer,10%","small bookshelf,30%","fridge,2%","nameplate,8%","calendar,20%","office toy,0-3","desk","chair","panel,2-3"]);
new Thing("boss's office",["office boss","office worker,10%","office worker,5%","computer","computer,10%","water cooler,10%",["bookshelf","small bookshelf"],"cupboard,0-2","fridge,20%","nameplate","calendar,80%","office toy,0-6","desk","armchair,50%","chair,2-4","tv,10%"]);
new Thing("meeting room",["office boss,2%","office worker,0-8","cat,2%","computer,30%","computer,10%","water cooler,40%",["bookshelf","small bookshelf"],"cupboard,0-2","fridge,20%","nameplate,0-4","calendar,50%","office toy,0-6","table","chair,4-12","tv,60%"]);
new Thing("office toy",["plastic","metal"],["colorcube","colorsnake","snowglobe","figurine","souvenir","toy magnet","kinetic toy","bobblehead","spinning top","executive ball clicker","bouncing ball","slinky","stress ball","magic 8-ball","yo-yo"]);
new Thing("panel",["plastic"]);
new Thing("calendar",["paper","ink"],[["calendar ("],["firemen","sexy athletes","half-naked ladies","kittens","puppies","ducklings","flowery nature","tourism","sharks","inspirational quotes","famous people","bears","funny cartoons","popular TV show characters","mayan","haikus","1-word-a-day"],[")"]]);
new Thing("nameplate",[["plastic","wood","metal"]]);
new Thing("water cooler",["plastic","water","push-button"]);

//small shops
new Thing("shop",["clerk,1-6",["customer,0-3","customer,0-15"],"desk,1-3","chair,0-3","tv,20%","warehouse,20%",".building"]);
new Thing("clerk",[".person"],"*PERSON*| (clerk)");
new Thing("customer",[".person"],"*PERSON*| (customer)");

new Thing("game shop",["video game stand,2-12","video game console,1-4","tv,1-3","computer,0-3",".shop"],[["Game","Gamer","Play"],["pro","shop","hub","go","cash","buy","now","grrrlz","bro","chump"]]);
new Thing("video game stand",["video game,2-20","plastic"],"video game stand");
new Thing("fresh produce shop",["produce stall,2-12",".shop"],[["Fresh","Green","Bio","Nature","Eco","Yum","Tasty"],["Produce","Froots","Fruits","Veggies","Vegetables","Life","Food"]]);
new Thing("produce stall",[["fruit pile,1-4","vegetable pile,1-4"],"glass","plastic","insect,10%"],"produce stall");
new Thing("fruit pile",["sugar","plant cell","insect,10%"],[["a pile of "],["apples","oranges","pears","figs","watermelons","bananas","kiwis","coconuts","lemons","limes","strawberries","raspberries","berries","blackberries","nuts","grapes","grapefruits","melons","peaches","apricots","pineapples","cherries","chestnuts","ginger","mangos","passion fruits","mangosteens","plums","lychees","kumquats","tangerines","rhubarb","durians","mulberries"]]);
new Thing("vegetable pile",["plant cell","insect,10%"],[["a pile of "],["potatoes","carrots","leeks","onions","garlic","spices","turnips","cabbages","lettuce","corn cobs","spinach leaves","cress","broccoli","kale","peas","radish","beets","tomatoes","cucumbers","zucchinis","peppers","eggplants","gourds","pumpkins","avocados","cauliflowers","artichokes","fava beans","beans","green beans","chickpeas","peanuts","soybeans","celery","asparagus","rutabagas","yams","olives"]]);//I'm putting tomatoes with vegetables and you can't stop me
new Thing("pet shop",["pet container,2-12","bird cage,1-6","vivarium,1-6","aquarium,1-6",".shop"],[["Pet","Cute","Adopt","Ani","Anima","World","Care","Woof","Meow","Purr"],["woof","meow","purr","dogz","catz","nimals","friends"]]);
new Thing("pet container",[["dog,1-4","cat,1-4"],"plastic"],["pet cage","pet box"]);
new Thing("vivarium",[["reptile,1-4","amphibian,1-4","insect,1-4"],"plastic","glass","dirt"]);
new Thing("aquarium",[["fish,1-6","cnidaria,1-4","mollusk,1-4","crustacean,1-4"],["fish,50%","cnidaria,50%","mollusk,50%","crustacean,50%"],"plankton,0-3","plastic","glass","water"]);
new Thing("bird cage",["bird","plastic","metal"]);
new Thing("toy shop",["toy box,2-12","video game console,40%","video game console,20%",".shop"],[["Toy","Play","Kidz","Yay","Magi","Super","Cosmo"],["time","pretend","play","toyz","dolls","blocks","stuff","fun"]]);
new Thing("toy box",["office toy,20%","office toy,20%","toy,0-8","doll,0-4"]);
new Thing("toy",[["wood","plastic"]],["spinning top","building blocks","construction set","castle playset","city playset","village playset","animal playset","dinosaur playset","wizard playset","family playset","warrior playset","underwater playset","cow-boy playset","space playset","figurines","chef playset","market playset","toy car","toy racing car","race tracks","boat model","airplane model","spaceship model"]);
new Thing("doll",["plastic","cloth"],[["robot","trendy","fashion","cyborg","nurse","chef","firefighter","police","construction worker","singing","dancing","talking","super","baby-care","shopkeeper","knight","action hero","wizard","gardener","science","movie","TV","reporter","alien","cosmonaut","rocket","future","time-travel","ice-cream","lovely","romance","radical","pretend","plastic","mutant"],[" "],["Cindy","Stacy","Barbara","Lois","Milly","Emily","Anette","Gordon","Brandon","Steve","Marcus","Pascal","Barney","Boris","baby","unicorn","dragon","dinosaur","monster","pony","teddy bear","cat","dog","bunny","bird","shark"]]);
new Thing("bargain shop",["stuff box,2-12",".shop"],[["Cheap","Haggle","Price","Poor","Cent","Money","Best","Save","Get","Found","Salvage","Dump"],["more","less","buy","shark","bargain","stuff","things","worth","shop","store","market","mart"]]);
new Thing("stuff box",["office toy,0-2","souvenir,20%","book,0-2","pants,20%","shirt,20%","underwear,20%","coat,20%","socks,20%","shoes,20%","hat,20%","glasses,20%","toy,0-2","doll,30%","video game console,10%","video game console,10%","cog,30%","cog,10%","unusual stone,1%","helmet,1%","armor,1%","medieval weapon,1%","painting,20%","painting,10%","dust,40%","insect,10%"]);
new Thing("souvenir shop",["souvenir,6-12",".shop"],["souvenir shop","gift shop"]);
new Thing("souvenir",[["wood","plastic","metal","glass"]],[["tower","pyramid","dome","bridge","statue","palace","castle","cathedral","arena","opera","ark","city","monument"],[" "],["model","replica","souvenir"]]);

//museums
new Thing("museum",["painting,0-3","museum room,2-12","tourist,2-10","clerk,1-3","desk,1-2","chair,2-6","souvenir,0-3",".building"]);
new Thing("museum room",["painting,1-10","tourist,0-20","tv,5%","chair,0-2"],"exhibition room");
new Thing("painting",["paint","wooden frame"],"*PAINTING*");
new Thing("paint",["oil","pigment"]);
new Thing("wooden frame",["wood"]);

//services
new Thing("fire department",["fire,0.2%","firefighter,3-6","desk,0-3","chair,1-4","fridge,60%","tv,60%","fire truck",".building"]);
new Thing("firefighter",[".person"],"*PERSON*| (firefighter)");

new Thing("police station",["police officer,2-6","desk,0-2","tv,40%","small bookshelf,0-2","chair,0-4",".building"]);
new Thing("police officer",[".person"],"*PERSON*| (police officer)");

new Thing("library",["bookshelf,10-30","painting,50%","painting,50%","painting,50%","desk,0-4","computer,0-4","chair,0-4","librarian,1-4","person,0-12",".building"]);
new Thing("librarian",[".person"],"*PERSON*| (librarian)");

//war stuff
new Thing("battlefield",["soldier,10-30","corpse,10-30","blood"]);
new Thing("soldier",[".person","arsenal","blood,20%","bullet wound,0-3"],[["*PERSON*| "],["(soldier)","(soldier)","(soldier)","(soldier)","(soldier)","(soldier)","(officer)","(lieutenant)","(captain)","(major)"]]);
new Thing("arsenal",["gas mask,20%","rifle,90%","knife,80%","handgun,90%","handgun,50%","knife,30%","ammo pack,0-4","grenade,0-4","bullet,0-5"]);
new Thing("bullet",["copper","lead"]);
new Thing("rifle",["steel","aluminium,50%","polymers,20%","bullet,0-6"]);
new Thing("handgun",["steel","aluminium,50%","polymers,20%","bullet,0-6"]);
new Thing("gun",[".handgun"]);
new Thing("knife",["steel","blood,10%"]);
new Thing("wound",["blood","worm,5%"],"wound");
new Thing("ammo pack",["bullet,0-20",["metal","plastic"]]);
new Thing("grenade",["iron","TNT",["metal","plastic"]]);
new Thing("TNT",["carbon","hydrogen","oxygen","nitrogen"],"TNT");
new Thing("gas mask",["metal","polymers","cloth"]);
new Thing("bullet wound",["blood","worm,5%","bullet,50%","bullet,30%","bullet,10%","bullet,2%"],"wound");

//hospitals
new Thing("hospital",["doctor,2-4","nurse,2-4","intern,2-4","hospital room,3-8","patient,0-3","desk,0-2","chair,0-2",".building"]);
new Thing("hospital room",["doctor,10%","nurse,20%","intern,20%","bed,1-2","patient,0-2","tv","table,75%","chair,0-2",".room"]);
new Thing("nurse",[".woman","blood,10%"],"*WOMAN*| (nurse)");
new Thing("doctor",[".person","blood,5%"],"*PERSON*| (doctor)");
new Thing("intern",[".person","blood,10%"],"*PERSON*| (intern)");
new Thing("patient",[".person","blood,15%","wound,0-3"],"*PERSON*| (patient)");

//[DATA EXPUNGED]
new Thing("research facility",["researcher,2-8","security guard,1-4","soldier,0-6","doctor,0-2","nurse,0-2",["corpse,0-3","",""],"containment room,1-12","top secret drawer,1-6",".building"]);
new Thing("researcher",[".person"],"*PERSON*| (researcher)");
new Thing("security guard",[".person","handgun","ammo pack,0-1"],"*PERSON*| (security guard)");
new Thing("containment room",[["portal","space animal","space monster","sea monster","bird","poultry","cat","dog","cetacean","fish","mollusk","plankton","reptile","amphibian","snake","small mammal","predatory mammal","herbivorous mammal","clam","worm","monkey","bear","shark","horse","insect","crustacean","dragon","person","ghost","ectoplasm","abomination","corpse","house","tree","machine","dinosaur","visitor","visitor furniture","medieval person","caveman","painting","","",""],"portal,1%","fire,1%","researcher,5%","researcher,5%","soldier,5%","soldier,5%","corpse,5%","corpse,5%","corpse,5%","corpse,5%"]);
new Thing("top secret drawer",["top secret folder,1-8","note,0-8","pen,30%","pen,10%","pen,5%","donut box,5%","can,2%","book,20%","book,20%","book,5%","book,5%","button,10%","button,10%","dust,60%","lint,40%"],"classified files");
new Thing("top secret folder",["top secret file,2-8","paper"],[["Classified Folder n°"],["0","1","2","3","4","5","6","7","8","9","",""],["0","1","2","3","4","5","6","7","8","9","",""],["0","1","2","3","4","5","6","7","8","9"]]);
new Thing("top secret file",[],[
["File ","Document ","Report "],["X","Z","A","B","L","S","T"],["-"],["0","1","2","3","4","5","6","7","8","9","",""],["0","1","2","3","4","5","6","7","8","9","",""],["0","1","2","3","4","5","6","7","8","9"],["<br>-"],
["Containment breach ¤¤¤","Subject ¤¤¤ attempted escape","Unusual events occuring","Possible breach of security measures in","Subject ¤¤¤ sighted","Witnesses report a ¤¤¤","Rumors of ¤¤¤","Singularity event","Subject ¤¤¤ attempted singularity","Retrieval of subject ¤¤¤","Accidental termination of subject ¤¤¤","Recovery of subject ¤¤¤","Recovery of a number of ¤¤¤","Accidental loss of ¤¤¤","New leads on ¤¤¤","Subject ¤¤¤ must now be kept away from ¤¤¤ at all times to avoid repeating the security breach that occurred","Locals report sightings of ¤¤¤","Subject ¤¤¤ transported","A number of ¤¤¤ were sighted","Subject ¤¤¤ has been predicted to have been","Retrieving supplies","Accidental destruction of all subjects","Retrieval of artifact ¤¤¤","Sightings of artifact ¤¤¤","Subject ¤¤¤ tried to merge with ¤¤¤","Subject ¤¤¤ sighted with artifact ¤¤¤","Experimentation done on ¤¤¤","Research ongoing on ¤¤¤","True nature of ¤¤¤ revealed","Gate to ¤¤¤ opened","Portal to ¤¤¤ closed","Relations friendly with ¤¤¤","Relations hostile with ¤¤¤","A team has been sent to investigate ¤¤¤","No news from the team sent to","Mission ¤¤¤ presumed to have been a failure; no further teams should be sent","Met with subject ¤¤¤","Artifact ¤¤¤ damaged but not destroyed","Artifact ¤¤¤ suspected to have been destroyed","Subject ¤¤¤ presumed dead","Subject ¤¤¤ unfortunately still alive","Phenomenons possibly caused by ¤¤¤ spotted","Phenomenons matching ¤¤¤'s behavior have been observed","Discussions on the whereabouts of ¤¤¤ took place","Subject ¤¤¤ travelled from ¤¤¤ to ¤¤¤","Subject ¤¤¤ sighted shape-shifting from a ¤¤¤ to a ¤¤¤","Subject ¤¤¤ started duplicating","Subject ¤¤¤ resumed duplicating","Subject ¤¤¤ will have/has started to ¤¤¤","Collision event between ¤¤¤ and ¤¤¤","Evidence of ¤¤¤"],[" "],
["in sector","in zone","in secured location","in facility","near site"],[" "],["X","Z","A","B","L","S","T"],["-"],["0","1","2","3","4","5","6","7","8","9","",""],["0","1","2","3","4","5","6","7","8","9","",""],["0","1","2","3","4","5","6","7","8","9"],[" "],
["on ¤¤/¤¤/¤¤¤¤","the day preceding ¤¤¤","following the ¤¤¤","in the hours leading to the ¤¤¤ event","in the hours following the ¤¤¤ event","directly after ¤¤¤","during the ¤¤¤ event"],
["; all researchers involved terminated","; all personnel involved terminated","; casualties estimated high to very high","; no casualties reported","; proper measures have been triggered","; more research is necessary","; further testing still needed","; casualties include half the local population","; casualties include all local wildlife",". Once again, do not, I repeat DO NOT ¤¤¤",". Do not, under any circumstances, attempt to ¤¤¤","; locals have been terminated","; locals have no memory of the event","; consequences of the event have been dealt with","","","","","",""],["."]
]);

//cemeteries
new Thing("cemetery",["gravedigger,0-2","person,0-3","cemetery shed,0-2","mausoleum,0-3","grave,10-30","ghost,20%","ghost,10%"],"cemetery");
new Thing("gravedigger",[".person","shovel,30%"],"*PERSON*| (gravedigger)");
new Thing("shovel",["wood","metal"]);
new Thing("cemetery shed",["gravedigger,0-2","table,20%","tv,20%","fridge,30%","chair,0-2","shovel,0-3","corpse,1%","ghost,1%",".building"],"shed");
new Thing("mausoleum",["tourist,8%","coffin,1-6","ghost,4%",["concrete","rock","marble"]]);
new Thing("grave",["coffin","coffin,5%","worm,0-2","insect,0-1",["concrete","rock","marble"],"dirt"]);
new Thing("coffin",["person,0.2%","corpse,98%","corpse,2%","ghost,2%","worm,0-3","insect,0-2","wood","cloth","nails"]);

new Thing("ectoplasm",["proton,3-7"],[["purple","fetid","green","yellow","blood-red","shiny","wispy","sparkly"],[" "],["ectoplasm"]]);
new Thing("ghost",["ghost body","ghost thoughts"],[["depressed","sad","lonely","wailing","screaming","stretching","clinking","sneezing","breathing","screeching","spinning","gasping","moaning","regretful","remorseful","vengeful","friendly neighborhood","skeletal","tentacled","conjoined","grasping","slimy","floating","mournful"],[" "],["ghost","spirit","apparition","phantom","poltergeist","specter","hauntling"]]);
new Thing("ghost body",["ectoplasm"],["\"body\""]);
new Thing("ghost thoughts",["ghost thought","ghost thought,20%"],["thoughts"]);
new Thing("ghost thought",[],["if only - she could hear me -","he needs to know - I'm sorry -","alone - I - wait -","I am so - very lonely -","when - will it end -","will it be - over soon -","do I - deserve this -","I regret - so much -","I miss you - so much -","please - never - ever die -","I must - wait here -","how many - centuries -","such is - my burden -","I cannot - feel a thing -","I have lost - all hope -","abandoned -","I float - forever -","I wander - for how long -","so spooky - right now -","that slime - isn't mine -","I rest - at last -","let's - be pals -","I sense - a presence -","you can - see me?","who you - gonna call -","can you - hear me now -"]);


//infrastructure
new Thing("street",["traffic accident,1%","urban life","person,0-5","driven car,0-20","driven bike,0-3","car,0-5","road","pavement"],[["*PERSON*|"],[" "],["street","avenue","boulevard","road","alley","bend","drive","place","hill","plaza"]]);
new Thing("road",[["asphalt","stone"]]);
new Thing("pavement",["note,3%","coin,4%","stone","dirt,5%"]);
new Thing("asphalt",["oil",".concrete"]);
new Thing("car",["engine","mechanics","tire,4"],[["parked "],["blue","red","white","black","grey"],[" "],["Chr","F","Chevr","Cad","H","Hyund","Maz","Niss","Suz","Lex","Merc","Aud","Volv"],["ysler","ord","olet","illac","onda","ai","da","an","uki","us","edes","i","o"]]);
new Thing("driven car",["person,1-4",".car"],[["blue","red","white","black"],[" "],["Chr","F","Chevr","Cad","H","Hyund","Maz","Niss","Suz","Lex","Merc","Aud","Volv"],["ysler","ord","olet","illac","onda","ai","da","an","uki","us","edes","i","o"]]);
new Thing("tire",["rubber","metal"]);
new Thing("bike",["mechanics","tire,2"]);
new Thing("driven bike",["person","person,5%",".bike"],"bike");
//["Chr","F","Chevr","Cad","H","Hyun","Maz","Niss","Suz","Lex","Merc","Aud","Volv"],["ysler","ord","olet","illac","onda","dai","da","an","uki","us","edes","i","o"]

//rooms
new Thing("building",["walls","roof"]);
new Thing("roof",["cat,2%","bird,10%","bird,10%","nest,2%","roof tiles"]);
new Thing("roof tiles",["ceramic"],"tiles");
new Thing("room",["visitor,0.1%","ghost,0.1%","walls"]);
new Thing("walls",["door,1-4","window,0-6",["wall,4","wall,4-8"]]);
new Thing("wall",[["plaster","wood"],"dirt,5%"]);
new Thing("plaster",["calcium","sulfur"]);
new Thing("marble",["calcium"]);
new Thing("stone",["rock"]);
new Thing("concrete",["rock","cement","water"]);
new Thing("cement",["calcium"]);
new Thing("marble",["calcium"]);
new Thing("door",["wood frame","glass,10%"]);
new Thing("window",["wood frame","glass"]);
new Thing("living-room",[".room","person,0-4","cat,10%","cat,10%","stuff box,5%","tv,95%","armchair,50%","armchair,50%","couch,90%","living-room table,50%","chair,1-6","painting,70%","painting,20%","mirror,2%","bookshelf,0-3","small bookshelf,0-2","desk,40%","computer,40%"]);
new Thing("kitchen",[".room","person,40%","person,20%","tv,40%","kitchen sink","cabinet,1-5","fridge","oven","chair,0-3","computer,5%","small bookshelf,5%","painting,30%","painting,10%"]);
new Thing("bedroom",[".room","person,40%","person,10%","cat,5%","stuff box,5%","tv,60%","bed","chair,0-4",["cupboard,90%","closet,90%"],"mirror,50%","bookshelf,0-2","small bookshelf,0-3","desk,40%","computer,40%","painting,60%","painting,20%"]);
new Thing("bathroom",[".room","person,10%","person,1%","cat,1%","sink,95%",["bathtub","shower"],"toilet","painting,20%","mirror,80%"]);
new Thing("study",[".room","person,30%","person,5%","stuff box,20%","tv,20%","desk,95%","computer,90%","chair,1-4","bookshelf,0-6","painting,70%","painting,20%","mirror,5%"]);
new Thing("garden",["person,40%","person,10%","dog,20%","dog,5%","cat,15%","grass","tree,50%","tree,50%","tree,20%","tree,5%","flowers,30%","hole,1%","hole,1%","hole,1%","poultry,1%","bird,20%","bird,10%"],["garden","lawn","backyard"]);
new Thing("garage",["person,20%","cat,2%","stuff box,30%","stuff box,20%","chair,0-3","car,90%","car,40%","car,5%","bike,40%","bike,30%","bike,10%","computer,5%","small bookshelf,30%","hole,1%","hole,0.5%","small mammal,5%","insect,15%","insect,15%","dirt,50%"]);
new Thing("hole",["corpse,20%","corpse,5%","blood,20%","shovel,20%","hole,0.5%","insect,25%","insect,15%","dirt"]);
