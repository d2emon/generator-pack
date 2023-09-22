"""
//buildings
new Thing("monument",["tourist,5-30","souvenir shop,70%","souvenir shop,30%"],"*MONUMENT*");
new Thing("tourist",[
    (PersonFactory),
    ],"*PERSON*| (tourist)");

new Thing("commercial area",["street,1-5","bargain shop,60%","bargain shop,30%","souvenir shop,10%","fresh produce shop,60%","pet shop,60%","toy shop,60%","game shop,60%","office building,1-12"]);
new Thing("office building",["building hall","office,6-20",".building"],[["a tall","a stout","an unimpressive","a large","a humongous","a modern","a classic","a historic","a gray","a dull","a white","a black","a concrete","a glass-covered","an impressive","a beautiful","an old-fashioned","a boring","a newly-built","a fancy"],[" "],["office building","skyscraper","building"]]);

new Thing("residential area",["street,1-5","house,5-20","apartment building,0-5"]);
new Thing("house",[
    FireFactory.probable(0.3),
    "living-room","kitchen","bathroom,1-3","bedroom,2-5","attic","study,0-2","garden,90%","garage,90%",".building"],[["a small","a large","a big","a cozy","a bland","a boring","an old","a new","a freshly-painted","a pretty","an old-fashioned","a creepy","a spooky","a gloomy","a tall","a tiny","a fine","a happy little"],[" pink"," grey"," green"," yellow"," orange"," red"," blue"," white"," brick"," stone"," wooden","","",""],[" house"]]);
new Thing("apartment",["living-room,90%","kitchen","bathroom,1","bedroom,1-3","study,20%"]);
new Thing("apartment building",[
    FireFactory.probable(0.3),
    "apartment,6-20",".building"]);
"""
