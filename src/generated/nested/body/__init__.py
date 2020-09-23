"""
//body stuff
new Thing("body part",["bacteria,30%","bacteria,10%","skin","blood vessels","bones","fat","muscles"],"body part");
new Thing("soft body part",["bacteria,30%","bacteria,10%","skin","blood vessels","fat","muscles"],"body part");
new Thing("skinless body part",["bacteria,30%","bacteria,10%","blood vessels","bones","fat","muscles"],"body part");
new Thing("skinless soft body part",["bacteria,30%","bacteria,10%","blood vessels","fat","muscles"],"body part");
new Thing("blood vessels",["bacteria,30%","blood"],"blood vessels");
new Thing("blood",["blood cell"],"blood");
new Thing("blood cell",[".cell"],["blood cells"]);
new Thing("skin",["bacteria,1-3","scar,0.5%","pores","skin cell","dead skin","dust,20%","sweat,20%"],"skin");
new Thing("scar",["dead skin"]);
new Thing("pores",["bacteria,1-3","skin cell","dead skin,50%","sweat,40%"],"pores");
new Thing("skin cell",[".cell"],["skin cells"]);
new Thing("dead skin",["skin cell"]);
new Thing("bone",[".bones"],"bone");
new Thing("bones",["bone cell","calcium"],"bones");
new Thing("bone cell",[".cell"],["bone cells"]);
new Thing("muscles",["muscle cell"],"muscles");
new Thing("muscle cell",[".cell"],["muscle cells"]);
new Thing("fat",["lipids"],"fat");
new Thing("brain cell",[".cell"],["brain cells"]);
new Thing("dandruff",["dead skin"]);

new Thing("clothing set",["hat,2%","glasses,20%","pants,98%","shirt,98%","coat,50%","socks,80%","shoes,80%","underwear,99%"],"clothing");
new Thing("man",[".person"],"*MAN*");
new Thing("woman",[".person"],"*WOMAN*");
new Thing("person",["body","psyche","clothing set"],"*PERSON*");
new Thing("corpse",["body","clothing set","blood,35%","worm,20%","worm,10%"],"*PERSON*| (dead)");
new Thing("body",["head","torso","arm,99%","arm,99%","leg,99%","leg,99%"],"body");
new Thing("torso",["chest","pelvis",".body part"]);
new Thing("chest",["nipple,2","bellybutton",".body part"]);
new Thing("bellybutton",["skin","lint,0-1"]);
new Thing("nipple",["skin"]);
new Thing("pelvis",["naughty bits","butt",".body part"]);
new Thing("naughty bits",[".soft body part"]);
new Thing("butt",["pasta,0.01%","sweat,50%",".body part"]);
new Thing("arm",["hand","elbow","armpit",".body part"],"arm");
new Thing("hand",["finger,5",".body part"]);
new Thing("finger",["fingernail",".body part"],"finger");
new Thing("fingernail",["dust,30%","keratin"],"fingernail");
new Thing("elbow",[".body part"]);
new Thing("armpit",["armpit hair","sweat,80%",".soft body part"]);
new Thing("armpit hair",[".hair"],"hair");
new Thing("leg",["foot","knee",".body part"],"leg");
new Thing("foot",["toe,5","sweat,30%",".body part"]);
new Thing("toe",["toenail",".body part"],"toe");
new Thing("toenail",["dust,40%","keratin"],"toenail");
new Thing("knee",[".body part"],"knee");
new Thing("head",["mouth","nose","eye,99%","eye,99%","ear,2","skull","head hair,85%",".body part"],"head");
new Thing("eye",["eyelashes","eye flesh","tear,2%"],"eye");
new Thing("eye flesh",["water","blood vessels","fat"],"eyeball");
new Thing("eyelashes",[".hair"],"eyelashes");
new Thing("tear",["water","salt"]);
new Thing("ear",[".soft body part"],"ear");
new Thing("brain",["bacteria,20%","brain cell"],"brain");
new Thing("skull",["brain",".bones"]);
new Thing("head hair",[".hair","dandruff,10%"],[["brown","black","gray","light","blonde","red","dark"],[" hair"]]);
new Thing("hair",["bacteria,30%","keratin"],"hair");
new Thing("nose",["nostril,2",".body part"],"nose");
new Thing("nostril",["nostril hair","boogers,0-1",".soft body part"],"nostril");
new Thing("nostril hair",[".hair"],"nostril hair");
new Thing("boogers",["organic matter"]);
new Thing("mouth",["teeth","tongue"],"mouth");
new Thing("teeth",["calcium","phosphorus"],"teeth");
new Thing("tongue",["muscles"],"tongue");

new Thing("abomination",["abomination body","abomination psyche"],"*PERSON*| (abomination)");//nonononononono
new Thing("abomination psyche",["abomination thoughts","memories"],"psyche");
new Thing("abomination thoughts",["black hole,0.01%","abomination thought"],"thoughts");
new Thing("abomination thought",[],["P-please...","Don't look at me...","Please... kill me...","Kill... me...","Why would I ever ask for this...","I only wish for death.","I only long for death now.","I only demand... death...","End my misery... I beg you...","This is a mockery of existence...","I miss her so much...","I miss him so much...","I miss my family...","Why would they do that to me...","How could they do this to me...","What have I become...","I feel... different...","I can't feel... anything...","I can't... see anything..."]);
new Thing("abomination body",["abomination head","abomination head,5%","abomination torso",["arm,0-8","arm,0-4"],["leg,0-8","leg,0-4"],"crustacean claw,2%","stinger,2%","weird soft organ,10%","weird soft organ,10%","weird hard organ,10%","weird hard organ,10%"],"misshapen body");
new Thing("abomination head",["mouth,0-2","nose,0-2","eye,0-8","ear,0-4","skull,90%","weird soft organ,20%","weird hard organ,20%","head hair,65%",".body part"],"misshapen head");
new Thing("abomination torso",["chest","chest,10%","pelvis","pelvis,10%","weird soft organ,20%","weird hard organ,20%",".body part"],"misshapen torso");

"""