"""
//world subdivisions
new Thing("biome",["plain,1-5", ["forest,0-4", "jungle,0-4"], "mountain,0-3"]);

new Thing("continent",["country,1-10", "sea,1-5"],[["continent of "], ["A", "Eu", "Ame", "Ocea", "Anta", "Atla"], ["frica", "rtica", "ropa", "rica", "nia", "sia", "ntide"]]);
//[["Eu","A","O","E"],["rt","lt","rm","t","tr","tl","str","s","m","fr"],["a","o","e","i"],["ri","ni","ti","fri","",""],["sia","nia","ca"]]);
new Thing("country",["region,1-10", "battlefield,10%", ".biome"],[["country of "], ["Li", "Arme", "Le", "Molda", "Slove", "Tur", "Afgha", "Alba", "Alge", "Tu", "Fran", "Baha", "Su", "Austra", "Germa", "In", "Ara", "Austri", "Be", "Ba", "Bra", "Ru", "Chi", "Ja", "Tai", "Bangla", "Gha", "Bou", "Bo", "Tas", "Ze", "Mon", "Mo", "Ne", "Neder", "Spai", "Portu", "Po", "Por", "Mol", "Bul", "Bru", "Bur", "Gro", "Syl", "Gui", "Da", "Gree", "Bri", "Ita"], ["ly", "dania", "mas", "vania", "ce", "nea", "nau", "topia", "garia", "gal", "laska", "golia", "nisia", "land", "snia", "livia", "mania", "than", "nin", "pan", "wan", "zil", "ssia", "na", "rein", "lgium", "bia", "ny", "ce", "stan", "distan", "nistan", "dan", "lia", "nia", "via", "sia", "tia", "key", "desh", "dia"]]);
new Thing("region",["capital", "city,1-10", "village,2-15"],[["north ", "east ", "south ", "west ", "north-west ", "north-east ", "south-west ", "south-east ", "center ", "oversea "], ["hilly", "rainy", "lush", "foggy", "desertic", "green", "tropical", "rich", "barren", "scorched"], [" region"]]);

//towns
new Thing("village",["residential area,1-4", "commercial area,90%", "police station,50%", "fire department,40%", "museum,5%", "library,40%", "farm,0-6", "factory,0-2", "cemetery,60%", "research facility,4%"],"village");
new Thing("city",["monument,15%", "monument,5%", "residential area,4-9", "commercial area,1-5", "police station", "police station,50%", "fire department", "fire department,50%", "museum,40%", "library,60%", "hospital", "farm,0-3", "factory,1-4", "cemetery", "research facility,2%"],"city");
new Thing("capital",["monument,70%", "monument,40%", "monument,10%", "residential area,7-15", "commercial area,3-9", "police station,2-5", "fire department,1-3", "museum,1-2", "library,1-3", "hospital,1-3", "farm,0-2", "factory,2-6", "cemetery", "cemetery,50%", "research facility,1%"],"capital city");

//buildings
new Thing("monument",["tourist,5-30", "souvenir shop,70%", "souvenir shop,30%"],"*MONUMENT*");
new Thing("tourist",[
    (PersonFactory)
    ],"*PERSON*| (tourist)");

new Thing("commercial area",["street,1-5", "bargain shop,60%", "bargain shop,30%", "souvenir shop,10%", "fresh produce shop,60%", "pet shop,60%", "toy shop,60%", "game shop,60%", "office building,1-12"]);
new Thing("office building",["building hall", "office,6-20", ".building"],[["a tall", "a stout", "an unimpressive", "a large", "a humongous", "a modern", "a classic", "a historic", "a gray", "a dull", "a white", "a black", "a concrete", "a glass-covered", "an impressive", "a beautiful", "an old-fashioned", "a boring", "a newly-built", "a fancy"], [" "], ["office building", "skyscraper", "building"]]);

new Thing("residential area",["street,1-5", "house,5-20", "apartment building,0-5"]);
new Thing("house",[
    FireFactory.probable(0.3),
    "living-room", "kitchen", "bathroom,1-3", "bedroom,2-5", "attic", "study,0-2", "garden,90%", "garage,90%", ".building"],[["a small", "a large", "a big", "a cozy", "a bland", "a boring", "an old", "a new", "a freshly-painted", "a pretty", "an old-fashioned", "a creepy", "a spooky", "a gloomy", "a tall", "a tiny", "a fine", "a happy little"], [" pink", " grey", " green", " yellow", " orange", " red", " blue", " white", " brick", " stone", " wooden", "", "", ""], [" house"]]);
new Thing("apartment",["living-room,90%", "kitchen", "bathroom,1", "bedroom,1-3", "study,20%"]);
new Thing("apartment building",[
    FireFactory.probable(0.3),
    "apartment,6-20", ".building"]);

//farms
new Thing("farm",[
    FireFactory.probable(0.3),
    "house,1-3", "farmer,1-4", "field,1-8", "horse,30%", "horse,30%", "horse,30%", "poultry,0-3", "grain silo,0-2", "barn,0-2", "warehouse,0-2", "storage shed,0-2"]);
new Thing("field",["grain", "insect,5%", "bird,10%", "bird,5%", "haystack,30%"],["wheat field", "corn field", "soy field", "rice field", "oat field", "peanut field", "tomato field", "grape field", "barley field", "canola field", "rye field", "flower field"]);
new Thing("farmer",[
    (PersonFactory)
    ],"*PERSON*| (farmer)");
new Thing("grain",["plant cell"]);
new Thing("grain silo",["metal", "grain"]);
new Thing("warehouse",["worker,0-2", "small mammal,8%", "ghost,0.3%", "machine,0-4", ".building"]);
new Thing("barn",[".building"]);
new Thing("storage shed",[".building"]);
new Thing("haystack",["grain", "insect,10%", "needle,0.1%"]);
new Thing("needle",["metal"]);

new Thing("factory",["worker,2-12", "machine,1-12", "pipes,40%", "cables,0-1", "public bathroom,60%", "warehouse,0-2", ".building"],[["toy", "chocolate", "car", "yoghurt", "processed food", "pork products", "canned beef", "juice", "soda", "shoe", "textile", "computer", "weapon", "hardware"], [" factory"]]);
new Thing("worker",[
    (PersonFactory)
    ],"*PERSON*| (worker)");

new Thing("public bathroom",[".room",
    PersonFactory.multiple(10)    
    PersonFactory.multiple(1)
    "sink,1-4", "toilet,1-4", "mirror,0-3"],"restroom");

//offices
new Thing("building hall",["office worker,0-3", "elevator,1-3", "public bathroom,75%"],"entrance hall");
new Thing("elevator",["ghost,0.3%", "office worker,0-3", "metal", "cables", "mechanics"]);
new Thing("office",["office worker,0-3", "cat,2%", "meeting room,0-2", "boss's office", "cubicle,2-12", "water cooler,0-2", "public bathroom,75%", "elevator"],[["Social", "Web", "Swift", "Smart", "Smooth", "Huge", "Large", "Greed", "Bank", "Media", "World", "Smith", "Channel", "Stock", "Dream", "One", "True", "We", "You", "People", "Planet", "Wild", "Standard", "Ever", "Quick", "Fast", "Real", "Good", "Great", "Neat", "Soft", "Hard", "Right", "Evil", "Okay", "Nice", "Mascot", "Clever", "Green", "Blue", "White", "Black", "Time", "Century", "Millenium", "NotCorrupt", "PrettyAlright", "PrettyDamnGood", "Actual", "Apex", "Nested", "Star", "Opti", "General", "Easy", "What", "Who", "Where", "This", "That", "Dat", "Dem", "Invest", "Painless", "Death", "First", "Shark", "Bear", "Truth", "Trust", "Venture", "Swell", "Kind", "Myth", "Mythic", "Crown", "Silver", "Gold", "Twin", "Single", "Double", "Triple", "Marvel", "Wonder", "Way", "Ward", "e", "I"], ["co", "alys", "isium", "arium", "orium", "orius", "arius", "aria", "oria", "arion", "orion", "ilton", "son", "cube", "Monkey", "Dog", "Century", "Year", "TV", "Big", "Money", "Rich", "Bucks", "Axis", "Venture", "Fine", "Universal", "Pro", "Unlimited", "brothers", "Tube", "Grow", "Friends", "Planet", "People", " People", " Plastics", " Fashion", " Trending", " TV", " Games", " Toys", " Video Games", " Video", " Sports", " Pets", " Social", " Websites", " Marketing", " Sales", " Trading", " Export", " Politics", " Strategy", " Health", " Medecine", " Gardening", " Agriculture", " Editions", " Mining", " Transports", " Voyages", " Tourism", " Art", " Assassinations", " Healthcare", " Software", " Hardware", " Automobile", " Care", " Education", " Security", " Security Systems", " Crafts", " Production", " Services", "Blood", " Space", " Transfer", " Backup", " Resources", " Secret Research", " Banking", " Funding", " Gambling", " Law", " Lawyers", " Pictures", " Religion", " Goods", " Weapons", " Laundering", " Cartoons", " Comics", " Agronomics", " Ergonomics", " Economics", " Supplies", " Things", " Stuff", " Printing", " Architecture", " Landscaping", " Construction", " Railroads", " Engineering", " Science", " News", " Testing", " Appliances", " Standards", "Studio", " Recording", " Enrichment", " Extraction", " Frivolities", " Realty", " Publishing", " Entertainment", " Propane", " Energy", " Business Solutions", " Councelling", " Event-planning", " Fundraising", " Electronics", " Electrics", " Records", " Slavery", " Distribution", " Distributors", " Accessories", " Fuels", " Motors", " Insurance", "Corp", " Procedurals"], [" "], ["Inc.", "Corp.", "Company", "L.P.", "Ltd.", "L.L.C.", "L.C.", "Associates", "Partners", "United", "Merger", "& Co", "International", "Conglomerate"]]);
new Thing("office worker",[
    (PersonFactory)
    ],"*PERSON*| (employee)");
new Thing("office boss",[
    (PersonFactory)
    ],"*PERSON*| (boss)");
new Thing("cubicle",["office worker,80%", "office worker,10%", "computer", "computer,10%", "small bookshelf,30%", "fridge,2%", "nameplate,8%", "calendar,20%", "office toy,0-3", "desk", "chair", "panel,2-3"]);
new Thing("boss's office",["office boss", "office worker,10%", "office worker,5%", "computer", "computer,10%", "water cooler,10%", ["bookshelf", "small bookshelf"], "cupboard,0-2", "fridge,20%", "nameplate", "calendar,80%", "office toy,0-6", "desk", "armchair,50%", "chair,2-4", "tv,10%"]);
new Thing("meeting room",["office boss,2%", "office worker,0-8", "cat,2%", "computer,30%", "computer,10%", "water cooler,40%", ["bookshelf", "small bookshelf"], "cupboard,0-2", "fridge,20%", "nameplate,0-4", "calendar,50%", "office toy,0-6", "table", "chair,4-12", "tv,60%"]);
new Thing("office toy",[
    PlasticFactory.one(),
    "metal"],["colorcube", "colorsnake", "snowglobe", "figurine", "souvenir", "toy magnet", "kinetic toy", "bobblehead", "spinning top", "executive ball clicker", "bouncing ball", "slinky", "stress ball", "magic 8-ball", "yo-yo"]);
new Thing("panel",[
    PlasticFactory.one(),
]);
new Thing("calendar",["paper", "ink"],[["calendar ("], ["firemen", "sexy athletes", "half-naked ladies", "kittens", "puppies", "ducklings", "flowery nature", "tourism", "sharks", "inspirational quotes", "famous people", "bears", "funny cartoons", "popular TV show characters", "mayan", "haikus", "1-word-a-day"], [")"]]);
new Thing("nameplate",[[
    PlasticFactory.one(),
    "wood", "metal"]]);
new Thing("water cooler",[
    PlasticFactory.one(),
    WaterFactory.one(),
    "push-button"]);

//small shops
new Thing("shop",["clerk,1-6", ["customer,0-3", "customer,0-15"], "desk,1-3", "chair,0-3", "tv,20%", "warehouse,20%", ".building"]);
new Thing("clerk",[
    (PersonFactory)
    ],"*PERSON*| (clerk)");
new Thing("customer",[
    (PersonFactory)
    ],"*PERSON*| (customer)");

new Thing("game shop",["video game stand,2-12", "video game console,1-4", "tv,1-3", "computer,0-3", ".shop"],[["Game", "Gamer", "Play"], ["pro", "shop", "hub", "go", "cash", "buy", "now", "grrrlz", "bro", "chump"]]);
new Thing("video game stand",["video game,2-20",
    PlasticFactory.one(),
],"video game stand");
new Thing("fresh produce shop",["produce stall,2-12", ".shop"],[["Fresh", "Green", "Bio", "Nature", "Eco", "Yum", "Tasty"], ["Produce", "Froots", "Fruits", "Veggies", "Vegetables", "Life", "Food"]]);
new Thing("produce stall",[["fruit pile,1-4", "vegetable pile,1-4"], "glass",
    PlasticFactory.one(),
    "insect,10%"],"produce stall");
new Thing("fruit pile",["sugar", "plant cell", "insect,10%"],[["a pile of "], ["apples", "oranges", "pears", "figs", "watermelons", "bananas", "kiwis", "coconuts", "lemons", "limes", "strawberries", "raspberries", "berries", "blackberries", "nuts", "grapes", "grapefruits", "melons", "peaches", "apricots", "pineapples", "cherries", "chestnuts", "ginger", "mangos", "passion fruits", "mangosteens", "plums", "lychees", "kumquats", "tangerines", "rhubarb", "durians", "mulberries"]]);
new Thing("vegetable pile",["plant cell", "insect,10%"],[["a pile of "], ["potatoes", "carrots", "leeks", "onions", "garlic", "spices", "turnips", "cabbages", "lettuce", "corn cobs", "spinach leaves", "cress", "broccoli", "kale", "peas", "radish", "beets", "tomatoes", "cucumbers", "zucchinis", "peppers", "eggplants", "gourds", "pumpkins", "avocados", "cauliflowers", "artichokes", "fava beans", "beans", "green beans", "chickpeas", "peanuts", "soybeans", "celery", "asparagus", "rutabagas", "yams", "olives"]]);
//I'm putting tomatoes with vegetables and you can't stop me
new Thing("pet shop",["pet container,2-12", "bird cage,1-6", "vivarium,1-6", "aquarium,1-6", ".shop"],[["Pet", "Cute", "Adopt", "Ani", "Anima", "World", "Care", "Woof", "Meow", "Purr"], ["woof", "meow", "purr", "dogz", "catz", "nimals", "friends"]]);
new Thing("pet container",[["dog,1-4", "cat,1-4"],
    PlasticFactory.one(),
],["pet cage", "pet box"]);
new Thing("vivarium",[["reptile,1-4", "amphibian,1-4", "insect,1-4"],
    PlasticFactory.one(),
    "glass", "dirt"]);
new Thing("aquarium",[["fish,1-6", "cnidaria,1-4", "mollusk,1-4", "crustacean,1-4"], ["fish,50%", "cnidaria,50%", "mollusk,50%", "crustacean,50%"], "plankton,0-3",
    PlasticFactory.one(),
    "glass",
    WaterFactory.one(),
]);
new Thing("bird cage",["bird",
    PlasticFactory.one(),
    "metal"]);
new Thing("toy shop",["toy box,2-12", "video game console,40%", "video game console,20%", ".shop"],[["Toy", "Play", "Kidz", "Yay", "Magi", "Super", "Cosmo"], ["time", "pretend", "play", "toyz", "dolls", "blocks", "stuff", "fun"]]);
new Thing("toy box",["office toy,20%", "office toy,20%", "toy,0-8", "doll,0-4"]);
new Thing("toy",[["wood",
    PlasticFactory.one(),
]],["spinning top", "building blocks", "construction set", "castle playset", "city playset", "village playset", "animal playset", "dinosaur playset", "wizard playset", "family playset", "warrior playset", "underwater playset", "cow-boy playset", "space playset", "figurines", "chef playset", "market playset", "toy car", "toy racing car", "race tracks", "boat model", "airplane model", "spaceship model"]);
new Thing("doll",[
    PlasticFactory.one(),
    "cloth"],[["robot", "trendy", "fashion", "cyborg", "nurse", "chef", "firefighter", "police", "construction worker", "singing", "dancing", "talking", "super", "baby-care", "shopkeeper", "knight", "action hero", "wizard", "gardener", "science", "movie", "TV", "reporter", "alien", "cosmonaut", "rocket", "future", "time-travel", "ice-cream", "lovely", "romance", "radical", "pretend",
    PlasticFactory.one(),
    "mutant"], [" "], ["Cindy", "Stacy", "Barbara", "Lois", "Milly", "Emily", "Anette", "Gordon", "Brandon", "Steve", "Marcus", "Pascal", "Barney", "Boris", "baby", "unicorn", "dragon", "dinosaur", "monster", "pony", "teddy bear", "cat", "dog", "bunny", "bird", "shark"]]);
new Thing("bargain shop",["stuff box,2-12", ".shop"],[["Cheap", "Haggle", "Price", "Poor", "Cent", "Money", "Best", "Save", "Get", "Found", "Salvage", "Dump"], ["more", "less", "buy", "shark", "bargain", "stuff", "things", "worth", "shop", "store", "market", "mart"]]);
new Thing("stuff box",["office toy,0-2", "souvenir,20%", "book,0-2", "pants,20%", "shirt,20%", "underwear,20%", "coat,20%", "socks,20%", "shoes,20%", "hat,20%", "glasses,20%", "toy,0-2", "doll,30%", "video game console,10%", "video game console,10%", "cog,30%", "cog,10%", "unusual stone,1%", "helmet,1%", "armor,1%", "medieval weapon,1%", "painting,20%", "painting,10%", "dust,40%", "insect,10%"]);
new Thing("souvenir shop",["souvenir,6-12", ".shop"],["souvenir shop", "gift shop"]);
new Thing("souvenir",[["wood",
    PlasticFactory.one(),
    "metal", "glass"]],[["tower", "pyramid", "dome", "bridge", "statue", "palace", "castle", "cathedral", "arena", "opera", "ark", "city", "monument"], [" "], ["model", "replica", "souvenir"]]);

//museums
new Thing("museum",["painting,0-3", "museum room,2-12", "tourist,2-10", "clerk,1-3", "desk,1-2", "chair,2-6", "souvenir,0-3", ".building"]);
new Thing("museum room",["painting,1-10", "tourist,0-20", "tv,5%", "chair,0-2"],"exhibition room");
new Thing("painting",["paint", "wooden frame"],"*PAINTING*");
new Thing("paint",[OilFactory.one(), "pigment"]);
new Thing("wooden frame",["wood"]);

//services
new Thing("fire department",[
    FireFactory.probable(0.2),
    "firefighter,3-6", "desk,0-3", "chair,1-4", "fridge,60%", "tv,60%", "fire truck", ".building"]);
new Thing("firefighter",[
    (PersonFactory)
    ],"*PERSON*| (firefighter)");

new Thing("police station",["police officer,2-6", "desk,0-2", "tv,40%", "small bookshelf,0-2", "chair,0-4", ".building"]);
new Thing("police officer",[
    (PersonFactory)
    ],"*PERSON*| (police officer)");

new Thing("library",["bookshelf,10-30", "painting,50%", "painting,50%", "painting,50%", "desk,0-4", "computer,0-4", "chair,0-4", "librarian,1-4",
    PersonFactory.multiple(0, 12),
    ".building"]);
new Thing("librarian",[
    (PersonFactory)
    ],"*PERSON*| (librarian)");

//war stuff
new Thing("battlefield",["soldier,10-30",
    CorpseFactory.multiple(10, 30),
    BloodFactory.one(),
    ]);
new Thing("soldier",[
    (PersonFactory)
    "arsenal",
    BloodFactory.probable(20),
    "bullet wound,0-3"],[["*PERSON*| "], ["(soldier)", "(soldier)", "(soldier)", "(soldier)", "(soldier)", "(soldier)", "(officer)", "(lieutenant)", "(captain)", "(major)"]]);
new Thing("arsenal",["gas mask,20%", "rifle,90%", "knife,80%", "handgun,90%", "handgun,50%", "knife,30%", "ammo pack,0-4", "grenade,0-4", "bullet,0-5"]);
new Thing("bullet",[
    ELEMENTS['Cu'].one(),
    ELEMENTS['Pb'].one(),
]);
new Thing("rifle",[
    SteelFactory.one(),
    ELEMENTS['Al'].one().probable(50),
    PolymersFactory.probable(20),
    "bullet,0-6"]);
new Thing("handgun",[
    SteelFactory.one(),
    ELEMENTS['Al'].one().probable(50),
    PolymersFactory.probable(20),
    "bullet,0-6"]);
new Thing("gun",[".handgun"]);
new Thing("knife",[
    SteelFactory.one(),
    BloodFactory.probable(10),
    ]);
new Thing("wound",[
    BloodFactory.one(),
    "worm,5%"],"wound");
new Thing("ammo pack",["bullet,0-20", ["metal",
    PlasticFactory.one(),
]]);
new Thing("grenade",[
    IronFactory.one(),
    "TNT", ["metal",
    PlasticFactory.one(),
]]);
new Thing("TNT",[
    CarbonFactory.one(),
    ELEMENTS['H'].one(),
    ELEMENTS['O'].one(),
    ELEMENTS['N'].one(),
],"TNT");
new Thing("gas mask",["metal",
    PolymersFactory.one(),
    "cloth"]);
new Thing("bullet wound",[
    BloodFactory.one(),
    "worm,5%", "bullet,50%", "bullet,30%", "bullet,10%", "bullet,2%"],"wound");

//hospitals
new Thing("hospital",["doctor,2-4", "nurse,2-4", "intern,2-4", "hospital room,3-8", "patient,0-3", "desk,0-2", "chair,0-2", ".building"]);
new Thing("hospital room",["doctor,10%", "nurse,20%", "intern,20%", "bed,1-2", "patient,0-2", "tv", "table,75%", "chair,0-2", ".room"]);
new Thing("nurse",[
    (WomanFactory),
    BloodFactory.probable(10),
    ],"*WOMAN*| (nurse)");
new Thing("doctor",[
    (PersonFactory),
    BloodFactory.probable(5),
    ],"*PERSON*| (doctor)");
new Thing("intern",[
    (PersonFactory),
    BloodFactory.probable(10),
    ],"*PERSON*| (intern)");
new Thing("patient",[
    (PersonFactory),
    BloodFactory.pobable(15),
    "wound,0-3"],"*PERSON*| (patient)");

//[DATA EXPUNGED]
new Thing("research facility",["researcher,2-8", "security guard,1-4", "soldier,0-6", "doctor,0-2", "nurse,0-2",
    [
        CorpseFactory.multiple(0, 3),
        "", ""
    ],
    "containment room,1-12", "top secret drawer,1-6", ".building"]);
new Thing("researcher",[
    (PersonFactory),
    ],"*PERSON*| (researcher)");
new Thing("security guard",[
    (PersonFactory),
    "handgun", "ammo pack,0-1"],"*PERSON*| (security guard)");
new Thing("containment room",[
    [
        PortalFactory.one(),
        "space animal", "space monster", "sea monster", "bird", "poultry", "cat", "dog", "cetacean", "fish", "mollusk", "plankton", "reptile", "amphibian", "snake", "small mammal", "predatory mammal", "herbivorous mammal", "clam", "worm", "monkey", "bear", "shark", "horse", "insect", "crustacean", "dragon",
        (PersonFactory),
        "ghost", "ectoplasm", "abomination",
        CorpseFactory.one(),
        "house", "tree", "machine", "dinosaur", "visitor", "visitor furniture", "medieval person", "caveman", "painting", "", "", ""
    ],
    PortalFactory.one().probable(1),
    FireFactory.probable(1),
    "researcher,5%", "researcher,5%", "soldier,5%", "soldier,5%",
    CorpseFactory.probable(5),
    CorpseFactory.probable(5),
    CorpseFactory.probable(5),
    CorpseFactory.probable(5),
    ]);
new Thing("top secret drawer",["top secret folder,1-8", "note,0-8", "pen,30%", "pen,10%", "pen,5%", "donut box,5%", "can,2%", "book,20%", "book,20%", "book,5%", "book,5%", "button,10%", "button,10%", "dust,60%", "lint,40%"],"classified files");
new Thing("top secret folder",["top secret file,2-8", "paper"],[["Classified Folder n°"], ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "", ""], ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "", ""], ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]]);
new Thing("top secret file",[],[["File ", "Document ", "Report "], ["X", "Z", "A", "B", "L", "S", "T"], ["-"], ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "", ""], ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "", ""], ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], ["<br>-"], ["Containment breach ¤¤¤", "Subject ¤¤¤ attempted escape", "Unusual events occuring", "Possible breach of security measures in", "Subject ¤¤¤ sighted", "Witnesses report a ¤¤¤", "Rumors of ¤¤¤", "Singularity event", "Subject ¤¤¤ attempted singularity", "Retrieval of subject ¤¤¤", "Accidental termination of subject ¤¤¤", "Recovery of subject ¤¤¤", "Recovery of a number of ¤¤¤", "Accidental loss of ¤¤¤", "New leads on ¤¤¤", "Subject ¤¤¤ must now be kept away from ¤¤¤ at all times to avoid repeating the security breach that occurred", "Locals report sightings of ¤¤¤", "Subject ¤¤¤ transported", "A number of ¤¤¤ were sighted", "Subject ¤¤¤ has been predicted to have been", "Retrieving supplies", "Accidental destruction of all subjects", "Retrieval of artifact ¤¤¤", "Sightings of artifact ¤¤¤", "Subject ¤¤¤ tried to merge with ¤¤¤", "Subject ¤¤¤ sighted with artifact ¤¤¤", "Experimentation done on ¤¤¤", "Research ongoing on ¤¤¤", "True nature of ¤¤¤ revealed", "Gate to ¤¤¤ opened", "Portal to ¤¤¤ closed", "Relations friendly with ¤¤¤", "Relations hostile with ¤¤¤", "A team has been sent to investigate ¤¤¤", "No news from the team sent to", "Mission ¤¤¤ presumed to have been a failure; no further teams should be sent", "Met with subject ¤¤¤", "Artifact ¤¤¤ damaged but not destroyed", "Artifact ¤¤¤ suspected to have been destroyed", "Subject ¤¤¤ presumed dead", "Subject ¤¤¤ unfortunately still alive", "Phenomenons possibly caused by ¤¤¤ spotted", "Phenomenons matching ¤¤¤'s behavior have been observed", "Discussions on the whereabouts of ¤¤¤ took place", "Subject ¤¤¤ travelled from ¤¤¤ to ¤¤¤", "Subject ¤¤¤ sighted shape-shifting from a ¤¤¤ to a ¤¤¤", "Subject ¤¤¤ started duplicating", "Subject ¤¤¤ resumed duplicating", "Subject ¤¤¤ will have/has started to ¤¤¤", "Collision event between ¤¤¤ and ¤¤¤", "Evidence of ¤¤¤"], [" "], ["in sector", "in zone", "in secured location", "in facility", "near site"], [" "], ["X", "Z", "A", "B", "L", "S", "T"], ["-"], ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "", ""], ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "", ""], ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], [" "], ["on ¤¤/¤¤/¤¤¤¤", "the day preceding ¤¤¤", "following the ¤¤¤", "in the hours leading to the ¤¤¤ event", "in the hours following the ¤¤¤ event", "directly after ¤¤¤", "during the ¤¤¤ event"], ["; all researchers involved terminated", "; all personnel involved terminated", "; casualties estimated high to very high", "; no casualties reported", "; proper measures have been triggered", "; more research is necessary", "; further testing still needed", "; casualties include half the local population", "; casualties include all local wildlife", ". Once again, do not, I repeat DO NOT ¤¤¤", ". Do not, under any circumstances, attempt to ¤¤¤", "; locals have been terminated", "; locals have no memory of the event", "; consequences of the event have been dealt with", "", "", "", "", "", ""], ["."]]);

//cemeteries
new Thing("cemetery",["gravedigger,0-2",
    PersonFactory.multiple(0, 3),
    "cemetery shed,0-2", "mausoleum,0-3", "grave,10-30", "ghost,20%", "ghost,10%"],"cemetery");
new Thing("gravedigger",[
    (PersonFactory),
    "shovel,30%"],"*PERSON*| (gravedigger)");
new Thing("shovel",["wood", "metal"]);
new Thing("cemetery shed",["gravedigger,0-2", "table,20%", "tv,20%", "fridge,30%", "chair,0-2", "shovel,0-3",
    CorpseFactory.probable(1),
    "ghost,1%", ".building"],"shed");
new Thing("mausoleum",["tourist,8%", "coffin,1-6", "ghost,4%", ["concrete",
    RockFactory.one(),
    "marble"]]);
new Thing("grave",["coffin", "coffin,5%", "worm,0-2", "insect,0-1", ["concrete",
    RockFactory.one(),
    "marble"], "dirt"]);
new Thing("coffin",[
    PersonFactory.probable(0.2),
    CorpseFactory.probable(98),
    CorpseFactory.probable(2),
    "ghost,2%", "worm,0-3", "insect,0-2", "wood", "cloth", "nails"]);

new Thing("ectoplasm",[
    ProtonFactory.multiple(3, 7),
],[["purple", "fetid", "green", "yellow", "blood-red", "shiny", "wispy", "sparkly"], [" "], ["ectoplasm"]]);
new Thing("ghost",["ghost body", "ghost thoughts"],[["depressed", "sad", "lonely", "wailing", "screaming", "stretching", "clinking", "sneezing", "breathing", "screeching", "spinning", "gasping", "moaning", "regretful", "remorseful", "vengeful", "friendly neighborhood", "skeletal", "tentacled", "conjoined", "grasping", "slimy", "floating", "mournful"], [" "], ["ghost", "spirit", "apparition", "phantom", "poltergeist", "specter", "hauntling"]]);
new Thing("ghost body",["ectoplasm"],["\"body\""]);
new Thing("ghost thoughts",["ghost thought", "ghost thought,20%"],["thoughts"]);
new Thing("ghost thought",[],["if only - she could hear me -", "he needs to know - I'm sorry -", "alone - I - wait -", "I am so - very lonely -", "when - will it end -", "will it be - over soon -", "do I - deserve this -", "I regret - so much -", "I miss you - so much -", "please - never - ever die -", "I must - wait here -", "how many - centuries -", "such is - my burden -", "I cannot - feel a thing -", "I have lost - all hope -", "abandoned -", "I float - forever -", "I wander - for how long -", "so spooky - right now -", "that slime - isn't mine -", "I rest - at last -", "let's - be pals -", "I sense - a presence -", "you can - see me?", "who you - gonna call -", "can you - hear me now -"]);

//infrastructure
new Thing("street",["traffic accident,1%", "urban life",
    PersonFactory.multiple(0, 5),
    "driven car,0-20", "driven bike,0-3", "car,0-5", "road", "pavement"],[["*PERSON*|"], [" "], ["street", "avenue", "boulevard", "road", "alley", "bend", "drive", "place", "hill", "plaza"]]);
new Thing("road",[["asphalt", "stone"]]);
new Thing("pavement",["note,3%", "coin,4%", "stone", "dirt,5%"]);
new Thing("asphalt",[OilFactory.one(), ".concrete"]);
new Thing("car",["engine", "mechanics", "tire,4"],[["parked "], ["blue", "red", "white", "black", "grey"], [" "], ["Chr", "F", "Chevr", "Cad", "H", "Hyund", "Maz", "Niss", "Suz", "Lex", "Merc", "Aud", "Volv"], ["ysler", "ord", "olet", "illac", "onda", "ai", "da", "an", "uki", "us", "edes", "i", "o"]]);
new Thing("driven car",[
    PersonFactory.multiple(1, 4),
    ".car"],[["blue", "red", "white", "black"], [" "], ["Chr", "F", "Chevr", "Cad", "H", "Hyund", "Maz", "Niss", "Suz", "Lex", "Merc", "Aud", "Volv"], ["ysler", "ord", "olet", "illac", "onda", "ai", "da", "an", "uki", "us", "edes", "i", "o"]]);
new Thing("tire",[
    RubberFactory.one(),
    "metal"]);
new Thing("bike",["mechanics", "tire,2"]);
new Thing("driven bike",[
    PersonFactory.one(),
    PersonFactory.probable(5),
    ".bike"],"bike");
//["Chr","F","Chevr","Cad","H","Hyun","Maz","Niss","Suz","Lex","Merc","Aud","Volv"],["ysler","ord","olet","illac","onda","dai","da","an","uki","us","edes","i","o"]

//rooms
new Thing("building",["walls", "roof"]);
new Thing("roof",["cat,2%", "bird,10%", "bird,10%", "nest,2%", "roof tiles"]);
new Thing("roof tiles",["ceramic"],"tiles");
new Thing("room",["visitor,0.1%", "ghost,0.1%", "walls"]);
new Thing("walls",["door,1-4", "window,0-6", ["wall,4", "wall,4-8"]]);
new Thing("wall",[["plaster", "wood"], "dirt,5%"]);
new Thing("plaster",[
    ELEMENTS['Ca'].one(),
    ELEMENTS['S'].one(),
]);
new Thing("marble",[
    ELEMENTS['Ca'].one(),
]);
new Thing("stone",[,
    RockFactory.one(),
    ]);
new Thing("concrete",[,
    RockFactory.one(),
    "cement",
    WaterFactory.one(),
]);
new Thing("cement",[
    ELEMENTS['Ca'].one(),
]);
new Thing("marble",[
    ELEMENTS['Ca'].one(),
]);
new Thing("door",["wood frame", "glass,10%"]);
new Thing("window",["wood frame", "glass"]);
new Thing("living-room",[".room",
    PersonFactory.multiple(0, 4),
    "cat,10%", "cat,10%", "stuff box,5%", "tv,95%", "armchair,50%", "armchair,50%", "couch,90%", "living-room table,50%", "chair,1-6", "painting,70%", "painting,20%", "mirror,2%", "bookshelf,0-3", "small bookshelf,0-2", "desk,40%", "computer,40%"]);
new Thing("kitchen",[".room",
    PersonFactory.probable(40),
    PersonFactory.probable(20),
    "tv,40%", "kitchen sink", "cabinet,1-5", "fridge", "oven", "chair,0-3", "computer,5%", "small bookshelf,5%", "painting,30%", "painting,10%"]);
new Thing("bedroom",[".room",
    PersonFactory.probable(40),
    PersonFactory.probable(10),
    "cat,5%", "stuff box,5%", "tv,60%", "bed", "chair,0-4", ["cupboard,90%", "closet,90%"], "mirror,50%", "bookshelf,0-2", "small bookshelf,0-3", "desk,40%", "computer,40%", "painting,60%", "painting,20%"]);
new Thing("bathroom",[".room",
    PersonFactory.probable(10),
    PersonFactory.probable(1),
    "cat,1%", "sink,95%", ["bathtub", "shower"], "toilet", "painting,20%", "mirror,80%"]);
new Thing("study",[".room",
    PersonFactory.probable(30),
    PersonFactory.probable(5),
    "stuff box,20%", "tv,20%", "desk,95%", "computer,90%", "chair,1-4", "bookshelf,0-6", "painting,70%", "painting,20%", "mirror,5%"]);
new Thing("garden",[
    PersonFactory.probable(40),
    PersonFactory.probable(10),
    "dog,20%", "dog,5%", "cat,15%", "grass", "tree,50%", "tree,50%", "tree,20%", "tree,5%", "flowers,30%", "hole,1%", "hole,1%", "hole,1%", "poultry,1%", "bird,20%", "bird,10%"],["garden", "lawn", "backyard"]);
new Thing("garage",[
    PersonFactory.probable(20),
    "cat,2%", "stuff box,30%", "stuff box,20%", "chair,0-3", "car,90%", "car,40%", "car,5%", "bike,40%", "bike,30%", "bike,10%", "computer,5%", "small bookshelf,30%", "hole,1%", "hole,0.5%", "small mammal,5%", "insect,15%", "insect,15%", "dirt,50%"]);
new Thing("hole",[
    CorpseFactory.probable(20),
    CorpseFactory.probable(5),
    BloodFactory.probable(20),
    "shovel,20%", "hole,0.5%", "insect,25%", "insect,15%", "dirt"]);

//furniture
new Thing("cabinet",["wood frame", "glass,30%", ".cabinet content"]);
new Thing("cabinet content",["donut box,4%", ["cheese,0-3", ""], "water bottle,0-1", "juice bottle,0-1", "soda bottle,0-1", ["can,0-6", "cookie box,0-6"], "insect,2%"]);
new Thing("fridge",[".fridge content",
    PlasticFactory.one(),
    "metal grill,1-4", "electronics"]);
new Thing("fridge content",["roast,15%", "pasta,40%", "pasta,10%", "can,15%", "donut box,5%", "cake,3%", "pie,3%", ["yoghurt,0-6", ""], ["ice cream,0-6", ""], ["cheese,0-3", ""], "water bottle,0-1", "juice bottle,0-2", "soda bottle,0-2", "milk bottle,0-1", "wine bottle,10%"]);
new Thing("oven",[["pie", "cake", "roast", "", ""],
    PlasticFactory.one(),
    "metal grill,1-3", "electronics"]);
new Thing("kitchen sink",[".sink"]);
new Thing("sink",[["porcelain", "metal"],
    OrganicFactory.one().probable(5),
    "pipes"]);
new Thing("toilet",[
    WaterFactory.one(),
    OrganicFactory.one().probable(15),
    "pasta,0.1%", "porcelain", "pipes"]);
new Thing("pipes",["metal", "dirt"]);
new Thing("nails",[
    IronFactory.one(),
]);
new Thing("metal",[
    IronFactory.one(),
]);
new Thing("metal grill",["metal"]);
new Thing("porcelain",[
    SilicaFactory.one(),
    ]);
new Thing("ceramic",[
    SilicaFactory.one(),
    ]);
new Thing("chair",[["wood",
    PlasticFactory.one(),
], "nails,50%"]);
new Thing("armchair",[".chair", "cloth"]);
new Thing("couch",[".armchair", "tv remote,5%", "coin,5%", "pen,5%"],["couch", "sofa"]);
new Thing("tv remote",[
    PlasticFactory.one(),
    "electronics"],"TV remote");
new Thing("coin",[
    OrganicFactory.one().probable(2),
    "dirt,2%",
    ELEMENTS['Cu'].one(),
]);
new Thing("gold coin",[
    ELEMENTS['Au'].one(),
]);
new Thing("dirt",[
    OrganicFactory.one().probable(50),
    "dust"]);
new Thing("grease",[
    LipidsFactory.one(),
    "dust"]);
new Thing("dust",[
    MoleculeFactory.one(),
]);
new Thing("crumbs",[
    OrganicFactory.one(),
]);
new Thing("lint",["textile fibre"]);
new Thing("pen",[
    PlasticFactory.one(),
    "ink,80%"]);
new Thing("button",[
    PlasticFactory.one(),
]);
new Thing("note",["note writing", "paper"]);
new Thing("note writing",[],["*NOTE*"]);
new Thing("bed",[".armchair", "pillow,0-3"]);
new Thing("pillow",["feather", "cloth"]);
new Thing("feather",["keratin"]);
new Thing("feathers",[".feather"]);
new Thing("mirror",["glass",
    PortalFactory.one().probable(0.1),
]);
new Thing("glass",[
    SilicaFactory.one(),
]);
new Thing("desk",["wood frame", "drawer,0-6"]);
new Thing("cupboard",["cup,0-6", "drinking glass,0-6", "bowl,0-4", "plate,0-8", "wood frame", "wood shelf,1-4", "drawer,0-2"]);
new Thing("drinking glass",["glass"],"glass");
new Thing("bowl",["ceramic"]);
new Thing("cup",["ceramic"]);
new Thing("plate",["ceramic"]);
new Thing("closet",[
    PortalFactory.one().probable(0.1),
    "skeleton,0.1%", "hat,30%", "hat,15%", "pants,0-5", "shirt,0-5", "underwear,0-6", "coat,0-3", "socks,0-8", "shoes,0-6", "button,20%", "wood frame", "wood shelf,0-2"]);
new Thing("living-room table",[".table", "drawer,0-2"],"table");
new Thing("table",[["wood",
    PlasticFactory.one(),
], "nails,50%"]);
new Thing("drawer",["note,0-8", "office toy,30%", "office toy,30%", "pen,30%", "pen,10%", "pen,5%", "donut box,4%", "can,2%", "book,20%", "book,20%", "book,5%", "book,5%", "button,10%", "button,10%", "dust,40%", "lint,40%"]);
new Thing("note stack",["note,5-25"]);
//lotsonotes
new Thing("bookshelf",["book,5-30", ["plastic shelf,3-8", "wood shelf,3-8", "drawer,0-2"]]);
new Thing("small bookshelf",["book,1-8", ["plastic shelf,1-6", "wood shelf,1-6"]],["bookshelf"]);
new Thing("wood shelf",["wood", "nails"],"shelf");
new Thing("plastic shelf",[
    PlasticFactory.one(),
    "nails,50%"],"shelf");
new Thing("wood frame",["wood", "nails"]);
new Thing("book",["page,20-100"],"*BOOK*");
new Thing("page",["paragraph,1-8", "paper"]);
new Thing("paper",["cellulose"]);
new Thing("cardboard",["cellulose"]);
new Thing("wood",["cellulose", "worm,1%"]);
new Thing("cellulose",[
    GlucidsFactory.one(),
]);
new Thing("paragraph",["character,50-300"]);
new Thing("character",["ink"],"*CHAR*");
new Thing("ink",[
    AlcoholFactory.one(),
    OilFactory.one()
]);
new Thing("bathtub",["porcelain", "pipes", "dirt,30%", "insect,5%",
    HairFactory.probable(30),
    ]);
new Thing("shower",["porcelain", "pipes", "dirt,30%", "insect,5%",
    HairFactory.probable(30),
    ]);
new Thing("tv",["tv show", "tv remote,20%",
    PlasticFactory.one(),
    "electronics"],[["plasma", "wide-screen", "high-resolution", "black and white", "small", "cheap"], [" TV"]]);
new Thing("tv show",[],[["A movie about", "A show about", "A sitcom about", "A TV show about", "A cartoon about", "A foreign show about", "An ad with"], [" "], ["stupid people", "boring people", "uninteresting people", "tan people", "foreigners", "a cute couple", "an obnoxious couple", "a dysfunctional couple", "magic kids", "space people", "scientists", "heroes", "antiheroes", "superheroes", "cavemen", "knights", "old-timey people", "awkward teenagers", "hundreds of people", "insane people", "cool hip kids", "a kid and his pet", "a kid and his teacher", "a boy and a girl", "businessmen", "an old man and his wife", "a young couple", "cow-boys", "pirates", "ninjas", "monsters", "wizards", "cleaning products", "aliens", "cute talking animals", "artists", "wacky animated animals", "beloved cartoon characters", "bears", "sharks", "small people"], [" "], ["struggling with their emotions", "trying to express their feelings", "and ecology", "and friendship", "and feelings", "and food", "talking about stuff", "doing things", "kicking butt and taking names", "in a post-apocalyptic world", "running away from zombies", "crying helplessly", "getting lost in the woods", "and their dream of starting a business", "trying to achieve their life-long dream", "trying to keep their promises", "trying to destroy a cursed artifact", "in school", "looking away from explosions", "hacking computers", "telling jokes", "delivering one-liners", "shooting stuff", "slaying monsters", "going to space", "travelling together", "learning about life", "dancing and singing", "doing way gross stuff", "learning martial arts", "trying to kill each other", "doing sports", "trying to defeat a government conspiracy", "in the century's biggest heist", "involving hilarious quiproquos and misunderstandings", "getting killed by a sociopath", "fighting robots", "killing aliens", "rescuing baby animals", "falling in love", "going on a date", "slowly turning evil", "learning that violence is not the answer", "doing magic", "coming up with convoluted plans", "exploring the sea", "saving the world", "involved in various mishaps", "involved in hilarious pranks", "with less-than-stellar writing", "with neat visual effects", "with a beautiful soundtrack", "with an impressive amount of clichés", "with a twist at the end", "with brilliant acting"], ["."]]);
new Thing("video game console",[
    PlasticFactory.one(),
    "electronics"],[["Mega", "Ultra", "Gene", "Se", "Ninten", "Nin", "Play", "Game", "Next", "Retro", "Dream", "Sun", "Kine", "3D"], ["station", "do", "sphere", "sis", "tron", "ga", "zor", "boy", "cast", "nect", "next"]]);

new Thing("machine",["computer keyboard,10%", "engine,20%", "mechanics", "electronics,40%", "metal", "wood,10%", "cables,40%", "dirt,10%"],[["valve", "pump", "terminal", "conveyor", "forklift", "girder", "furnace", "generator", "hydraulics"]]);
new Thing("cables",[
    PlasticFactory.one(),
    "wire"]);
new Thing("wire",[
    ELEMENTS['Cu'].one(),
]);

new Thing("engine",["mechanics"]);
new Thing("mechanics",["cog,2-12", "push-button,0-3", "electronics,30%", "cables,75%", "wire,0-2", "tube,0-3", "nails,40%", "insect,5%"],"mechanical components");
new Thing("cog",[[
    ELEMENTS['Cu'].one(),
    PlasticFactory.one(),
    IronFactory.one(),
    SteelFactory.one(),
    ELEMENTS['Al'].one(),
]],["cog", "gear", "spur gear", "helical gear", "bevel gear", "harmonic drive", "spring", "pump", "sprocket", "wheel", "chain", "belt", "track", "bolts", "gizmo", "pulley", "puffer", "smoker", "vent"]);
new Thing("push-button",[
    PlasticFactory.one(),
    "cables"],["lever", "button", "switch"]);
new Thing("tube",[[
    PlasticFactory.one(),
    "metal", "glass"]]);

new Thing("electronics",["microchip,1-6", "electronic component,1-6", "wire,0-2"]);
new Thing("microchip",["electronic component,1-15",
    PlasticFactory.probable(75),
    ELEMENTS['Cu'].one().probable(75),
    ELEMENTS['Si'].one().probable(25),
    ELEMENTS['Au'].one().probable(5),
],["microchip"]);
new Thing("electronic component",[
    PlasticFactory.probable(75),
    ELEMENTS['Cu'].one().probable(75),
    ELEMENTS['Si'].one().probable(25),
    ELEMENTS['Au'].one().probable(5),
 ],["transistor", "inductor", "capacitor", "diode", "metagizmo", "transmorpher", "beeper"]);

//computers
new Thing("pixel paragraph",["pixel character,50-300"],"paragraph");
new Thing("pixel character",["bit,8"],"*CHAR*");
new Thing("computer",["computer screen", "computer keyboard", "computer mouse", "electronics"],[["P", "B", "M", "N", "T", "St", "Pl", "Bl", "Gr", "Fr", "Sht", "Fl"], ["apple", "indows", "inux", "oogle"], [" computer"]]);
new Thing("laptop",[".computer"],[["P", "B", "M", "N", "T", "St", "Pl", "Bl", "Gr", "Fr", "Sht", "Fl"], ["apple", "indows", "inux", "oogle"], [" laptop"]]);
new Thing("computer keyboard",[
    PlasticFactory.one(),
    "electronics"],"keyboard");
new Thing("computer mouse",[
    PlasticFactory.one(),
    "electronics"],"mouse");
new Thing("computer screen",["internet browser", "computer folder,1-4", "software,0-4", "video game,0-4", "computer trashbin",
    PlasticFactory.one(),
    "electronics"],"screen");
new Thing("computer folder",["computer folder,0-2", ["computer folder,0-6", "disturbing computer image,1-10", "stupid computer image,1-10", "cute computer image,1-10", "software,1-6", "video game,1-6"]],[["/"], ["my ", "My ", "misc ", "Misc. ", "various ", "secret ", "family ", "Family ", "shared ", "Shared ", "important ", "Important ", "public ", "Public ", "private ", "Private ", "", "", ""], ["documents", "docs", "Documents", "Songs", "Music", "Movies", "Pictures", "pictures", "pics", "photos", "files", "Files", "things", "stuff", "stuff to sort"]]);
new Thing("computer trashbin",["computer folder,0-4", "disturbing computer image,0-4"],"Trashbin");
new Thing("video game",[".computer file"],[["Super ", "Mega ", "Ultra ", "Final ", "World of ", "", "", "", "", ""], ["Bl", "B", "Fl", "Gl", "Z", "Zw", "Dw", "M", "W", "Wh", "C", "F", "G", "Pl", "Spl"], ["ario", "antasy", "and", "astle", "ark", "ork", "org", "urg", "ink", "arf", "ine", "ar", "at", "uster", "aster", "alaxy", "ims", "ultima", "universe", "izzard"], ["craft", "vania", "arria", "arium", "'s Revenge", "'s Quest", " Bros", " Town", " Land", " World", " Party", " Quest", " RPG", " Horses", " Friends", " Girlz", " Online", " Fantasy", " Ultra", " Deluxe", " Fortress", " Racing", " Edit", " Maker", " Beta", " Trial", " Music", " Ultimate", " Resurrection", " The Movie : The Game", " 2", " 3", " II", " III", " 2000", " 3000", " GOTY Edition", " Deluxe Edition", " expansion pack", " [keygen]", " [CRACK]", " HD", "", "", "", "", "", "", "", "", "", "", ""], [".soft"]]);
new Thing("software",[".computer file"],[["Photo", "Touch", "Pic", "Morph", "Kid", "Cosmo", "Astro", "Ink", "Web", "Art", "Movie", "Music", "Calc", "Math", "Phrase", "Dictio", "World", "Bug", "Shell", "Folder", "File", "Program", "Question", "EZ", "Easy", "Ancestry", "History", "Encyclo", "Sun", "Speed", "Health", "Doc", "School", "Learn", "Lang", "Code", "Prog", "Note", "Pixel", "Simple", "Line", "Shape", "Name", "Phone", "Insta", "Love", "Friend", "Assist", "Tut", "Active", "Micro", "Macro", "Shock", "Laser", "Disc", "Index", "Game", "Trouble", "Hobbie", "House", "Task", "Sports", "Car", "Money", "Finance", "Password", "Fun", "Mail", "Virus", "Fire", "Burn", "Diet", "Pet", "Mission", "Hyper", "Flower", "Biblio", "Video", "Party", "Open", "Closed", "Magic"], ["shop", "pic", "pix", "draw", "thinker", "brain", "pad", "glide", "top", "artist", "words", "writer", "layer", "net", "nary", "matic", "ulator", "ula", "ulus", "ify", "izer", "crusher", "finder", "find", "sort", "reply", "info", "pro", "pedia", "helper", "creator", "card", "land", "warrior", "armor", "wall", "nova", "manager", "paint", "pixel", "namer", "call", "book", "tales", "media", "wave", "mail", "-b-gone", "care", "serve", "server", "printer", "designer", "retriever", "spy", "link", "Office", "cracker", "Edit", "Editor"], [" Pro", " - More Clipart edition", " Assistant", " Fusion", " Easy", " Plus", " Professional", " Gold", " extended edition", " Free", " freeware version", " trial", " shareware", " Web", " Online", " Edit", " Illustrated", " 2.0", " 1.1", " 1.2", " 3.0", " [keygen]", " [CRACK]", " HD", "", "", "", "", "", "", "", "", "", "", ""], [".soft"]]);
new Thing("computer file",["bit,50-100"],["file"]);
new Thing("bit",[],["0", "1"]);
new Thing("cute computer image",[".computer file"],[["An image of ", "A picture of ", "A short video of ", "A drawing of ", "A slideshow of ", "A video of "], ["a cat", "two cats", "cats", "kittens", "a kitten", "a duckling", "a duck", "ducks", "a puppy", "a baby seal", "a dog", "puppies", "a squid", "a dolphin", "a bunny", "bunnies", "baby bunnies", "a parrot", "two parrots", "a gecko", "a chameleon"], [" "], ["playing with a ball", "befriending other animals", "making cute faces", "wearing silly hats", "trying to play piano", "in various shenanigans", "playing with cardboard boxes", "being really excited", "sneezing", "sleeping", "waking up", "falling asleep"], ["."]]);
new Thing("stupid computer image",[".computer file"],[["An image of ", "A picture of ", "An album of ", "A short video of ", "A video of ", "A compilation of "], ["some dude", "some girl", "a rather unattractive fellow", "a rather unattractive lady", "a grotesque individual", "a clearly drunk guy", "a clearly drunk girl", "a bunch of kids with popped collars", "some muscular guy", "a masked guy", "some guy with a horse mask", "cosplaying kids", "orange people", "midgets", "a midget", "a movie star", "some celebrity", "high school kids", "children", "a creepy old person", "old people"], [" "], ["setting fire to some stuff", "involved in a retardedly dangerous prank", "trying something extremely dangerous", "involved in what was probably a stupid bet", "doing stupid stuff", "in anatomically questionable shenanigans", "getting stupidly injured", "stretching the limits of stupidity", "in an absurdly dangerous stunt", "dancing to some cheesy music", "pestering dangerous animals", "doing that thing with the stuff", "trying too hard to be cool"], ["."]]);
new Thing("disturbing computer image",[".computer file"],[["An image of ", "A possibly illegal image of ", "A crude representation of ", "A disturbing representation of ", "A daring representation of ", "A video of "], ["a ¤¤¤¤¤¤", "a group of ¤¤¤¤¤¤", "several ¤¤¤¤¤¤", "a couple of ¤¤¤¤¤¤"], [" "], ["in the process of ¤¤¤¤¤¤", "being ¤¤¤¤¤¤ by", "trying to ¤¤¤¤¤¤ on", "in a ¤¤¤¤¤¤ with", "involved in ¤¤¤¤¤¤ with", "holding"], [" "], ["another ¤¤¤¤¤¤", "two other ¤¤¤¤¤¤", "their ¤¤¤¤¤¤", "inside a ¤¤¤¤¤¤'s ¤¤¤¤¤¤", "a ¤¤¤¤¤¤", "a strange-looking ¤¤¤¤¤¤", "a bewildered ¤¤¤¤¤¤"], ["."]]);
new Thing("forum post",[".pixel paragraph"],[["A poll about ", "An irate little person ranting about ", "A bunch of shut-ins arguing about ", "Two people sharing their love for ", "Some hipsters chatting about ", "Concerned parents discussing ", "An inflammatory post about ", "A thoughtful comment on ", "An insightful post regarding ", "A troll post about ", "A flame war about ", "Some spam about ", "A comment on ", "A post about ", "A discussion about ", "An ongoing discussion about ", "A heated argument about ", "A passionate discussion about ", "A single person complaining about ", "A group of persons enthusiastic about "], ["politics", "countries", "cooking", "food", "favorite foods", "pets", "religion", "religious beliefs", "crime", "funny videos", "music", "favorite bands", "webcomics", "comics", "art", "video games", "movies", "dating advice", "relationships", "favorite books", "famous people", "astronomy", "astrophysics", "science", "memes", "spacetime", "physics", "foreign countries", "cats", "aliens", "a bunch of nonsense", "a controversial book", "a controversial movie", "friendship", "stuff people put in their pockets", "computers", "cute things", "creepy things", "stupid things", "gardening", "cars", "crime", "youth", "illicit substances", "knitting", "sports", "meditation", "hobbies", "whatever's trendy right now", "a debated topic", "superheroes", "trolling", "jimmies being rustled", "filenames", "an online universe generator"], ["."]]);
new Thing("internet browser",["nested,0.5%", "website"],[["Blazewolf", "Interweb Discoverer", "Bismuth", "Savannah", "Theatre"], [".soft"]]);
new Thing("website",[["forum post,1-10", "disturbing computer image,1-10", "cute computer image,1-10", "stupid computer image,1-10", "website,1-10"], "website,1-3"],[["www."], ["one", "4", "9", "on", "live", "wiki", "re", "net", "home", "neat", "fat", "free", "cool", "not", "something", "everything", "dat", "my", "you", "that", "this", "face", "tv", "sick", "cute", "creepy", "me", "hurr", "crap", "web", "bizz", "wrong"], ["chon", "speak", "news", "chat", "gog", "ddit", "bad", "nasty", "forum", "gross", "pal", "friends", "world", "rama", "search", "stick", "retarded", "tard", "ville", "town", "cat", "cats", "durr", "tube", "space", "book", "music", "directory"], [".com", ".com", ".com", ".net", ".org"]]);

//hell, might as well
new Thing("internet",["website,20"],"The Internet");
new Thing("google",[".website"]);
new Thing("wikipedia",[".website"]);
new Thing("4chan",[".website"]);
new Thing("nested",[
    UniverseFactory.one(),
],"www.orteil.dashnet.org/nested");
new Thing("reddit",[".website"]);
new Thing("facebook",[".website"]);
new Thing("/tg/",[".website"]);
new Thing("/b/",[".website"]);
new Thing("/v/",[".website"]);
new Thing("/x/",[".website"]);

//food
new Thing("milk",[
    GlucidsFactory.one(),
    LipidsFactory.one(),
    ELEMENTS['Ca'].one(),
]);
new Thing("bottle",[["glass",
    PlasticFactory.one(),
    "cardboard"], "label"]);
new Thing("glass bottle",["glass"],"bottle");
new Thing("glass jar",["glass"],"jar");
new Thing("label",["paper"]);
new Thing("milk bottle",[".bottle", "milk"]);
new Thing("wine bottle",[".bottle", "wine"]);
new Thing("wine",["sugar",
    AlcoholFactory.one(),
]);
new Thing("water bottle",[".bottle",
    WaterFactory.one(),
]);
new Thing("juice bottle",[".bottle", "juice"]);
new Thing("soda bottle",[".bottle", "soda"]);
new Thing("juice",[
    WaterFactory.one(),
    "sugar"],[["apple", "pear", "banana", "tomato", "pineapple", "pumpkin", "carrot", "grape", "orange", "papaya", "kiwi", "mango"], [" juice", " juice", " juice", " smoothie"]]);
new Thing("soda",[
    WaterFactory.one(),
    "sugar"],[["apple", "pineapple", "grape", "orange", "purple", "brown"], [" soda"]]);
new Thing("can",[
    WaterFactory.one(),
    "sugar",
    SaltFactory.one(),
    "mold,3%", "metal"],[["canned "], ["apple bits", "pear bits", "tomatoes", "pineapple", "pumpkin", "carrots", "meat", "pork", "beef", "peas", "mushrooms", "olives", "fish", "burger", "corn"]]);
new Thing("cookie box",["sugar",
    SaltFactory.one().probable(70),
    "mold,3%", "cardboard"],[["box of "], ["cheesy", "cheese", "sugar", "cream", "milk", "milky", "whole-grain", "frosted", "glazed", "apple", "nut", "fruit", "chocolate", "butter", "oat", "wheat", "corn", "animal-shaped", "meat", "crunchy", "crispy"], [" "], ["puffs", "poofs", "cookies", "biscuits", "rolls", "pops", "snacks", "crackers", "cereals", "pies", "tarts"]]);
new Thing("yeast",[".cell"]);
new Thing("yoghurt",["milk", "sugar", "yeast"],[["strawberry", "vanilla", "cherry", "pear", "plain"], [" yoghurt"]]);
new Thing("ice cream",["milk", "sugar",
    IceFactory.one(),
],[["strawberry", "vanilla", "cherry", "chocolate"], [" ice cream"]]);
new Thing("cheese",["milk", "yeast", "mold,30%"],[["roquefort", "cheddar", "gouda", "edam", "colby", "mozarella", "processed cheese", "stilton", "goat cheese", "gorgonzola", "brie", "camembert"]]);
new Thing("roast",[".meat", "spices"],[["chicken", "beef", "pork", "duck", "mutton"], [" roast"]]);
new Thing("spices",
    (OrganicFactory),
    [["pepper", "garlic", "onions", "rosemary", "sage", "thyme"]]);
new Thing("meat",[
    BloodVesselsFactory.probable(5),
    BonesFactory.probable(5),
    FatFactory.probable(50),
    MusclesFactory.one(),
    SaltFactory.one(),
    ]);
new Thing("tomato sauce",[
    GlucidsFactory.one(),
    "meat,20%",
    SaltFactory.one(),
    ]);
new Thing("pasta",[
    SaltFactory.one(),
    GlucidsFactory.one(),
    "cheese,5%", "tomato sauce,20%"],["spaghetti", "noodles", "fusilli", "fettuccine", "fettuce", "tagliatelle", "cannelloni", "penne", "rigatoni", "farfalle", "tortelloni", "ravioli", "gnocchi"]);
new Thing("pastry",["sugar",
    SaltFactory.one(),
    "dough"],"pastry");
new Thing("pie",[["fruit jam", "meat"], ".pastry"],"pie");
new Thing("cake",[".pastry"],[["chocolate", "white chocolate", "chestnut", "fruit", "huge", "impressive", "ornate", "glazed", "colorful", "cheese", "nut", "delicious"], [" cake"]]);
new Thing("fruit jam",["plant cell", "sugar"]);
new Thing("donut box",["donut,0-12", "cardboard"],"doughnut box");
new Thing("donut",[".pastry"],[["vanilla ", "strawberry ", "raspberry ", "cherry ", "chocolate ", "coconut ", "cream ", "cinnamon ", "bacon ", "sprinkly ", "frosted ", "glazed ", "powdered ", ""], ["doughnut"]]);
new Thing("sugar",[
    GlucidsFactory.one(),
]);
new Thing("dough",[
    GlucidsFactory.one(),
    LipidsFactory.one(),
]);

//visitors
new Thing("visitor",["visitor body", "visitor psyche"],"visitor");
new Thing("visitor body",["visitor head", "visitor head,2%", "visitor torso", "visitor arm,99%", "visitor arm,2%", "visitor arm,99%", "visitor leg,99%", "visitor leg,99%", "visitor leg,2%"],"body");
new Thing("visitor torso",["visitor chest", "visitor pelvis",
    (BodyPatFactory)
    ],"torso");
new Thing("visitor chest",[
    (BodyPatFactory)
    ],"chest");
new Thing("visitor pelvis",["visitor naughty bits",
    (BodyPatFactory)
    ],"pelvis");
new Thing("visitor naughty bits",[
    (SoftBodyPatFactory)
    ],["thrusher"]);
new Thing("visitor arm",["visitor hand", "visitor elbow,2", "visitor armpit",
    (BodyPatFactory)
    ],"arm");
new Thing("visitor hand",["visitor finger,3",
    (BodyPatFactory)
    ],"hand");
new Thing("visitor finger",[
    (BodyPatFactory)
    ],"finger");
new Thing("visitor elbow",[
    (BodyPatFactory)
    ],"elbow");
new Thing("visitor armpit",["visitor ooze,70%",
    (SoftBodyPatFactory)
    ],"armpit");
new Thing("visitor leg",["visitor foot", "visitor knee",
    (BodyPatFactory)
    ],"leg");
new Thing("visitor foot",["toe,4", "visitor ooze,40%",
    (BodyPatFactory)
    ],"foot");
new Thing("visitor toe",[
    (BodyPatFactory)
    ],"toe");
new Thing("visitor knee",[
    (BodyPatFactory)
    ],"knee");
new Thing("visitor head",["visitor mouth",
    EyeFactory.multiple(0, 4),
    SkullFactory.one(),
    ],"head");
new Thing("visitor eye",[
    EyeFleshFactory.one(),
    "visitor ooze,20%"],"eye");
new Thing("nose",["nostril,2",
    (BodyPatFactory)
    ],"nose");
new Thing("visitor mouth",["visitor teeth", "tongue,2", "visitor ooze"],"mouth");
new Thing("visitor teeth",[
    SteelFactory.one(),
],"teeth");
new Thing("visitor ooze",["bacteria,40%",
    OrganicFactory.one(),
    ELEMENTS['S'].one(),
],"ooze");

new Thing("visitor psyche",["visitor thoughts", "visitor memories"],"psyche");
new Thing("visitor thoughts",["visitor thought,1-3"],"thoughts");
new Thing("visitor memories",["visitor memory,1-2"],"memories");
new Thing("visitor thought",[],["ACK!!! ACK ACK ACK", "ACK ACK AAAACK ACK ACK", "ACK, ACKKKKKKKK", "AAAAAAAAAACKKKKKKK", "Ack.", "Ack?", "Ack... Ack ack ack.", "Ack ack ock ack!", "Ack eck.", "Ack ACK AAAAACK", "AACK, ACK ACK ACK!", "AAAAACK ACK ACK ACK", "ACKACKACK, ACK!!!", "Ackack, ackackackack?", "...ack...", "Hehuck.", "Whoack."]);
new Thing("visitor memory",[],[["Ack ack...", "Ack, ack ack...", "Ack.", "...Ack ack.", "Ack ack ack."], ["", "", " Ack ack ack ack.", " Ack.", " Ack, ack ack.", " Ack ack ack...", " ...ack ack ack.", " ...Ack.", " Ack."]]);

new Thing("named visitor",[".visitor"],[["B"], ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "!", "?", ";", ",", ".", ":", "/", "*", "#", "¤", "+", "-", "=", " "], ["rt"], ["y", "ie", "ington", "inson", "son", "", "", "", "", "", "", ""]]);

new Thing("visitor city",["named visitor,0-8", ["space animal,0-3", ""], "visitor neighborhood,1-8"],"visitor city");
new Thing("visitor neighborhood",["named visitor,0-8", ["space animal,0-3", ""], "visitor building,2-16"],"neighborhood");
new Thing("visitor building",[["named visitor,0-8", ""], "visitor room,1-8"],[["a tall", "a wide", "a spiralicious", "a twisty", "a holographic", "a composite", "a stout", "a long", "a domed", "an underground", "a submerged", "a gigantic"], [", "], ["green", "blue", "purple", "white", "gray", "translucent", "bright", "porous", "microsthetic", "turbified", "motorized", "hovering", "meshed", "towered", "automated", "ridged"], [" "], ["glumporium", "swapmarket", "slickmarket", "juicehouse", "scienceteria", "faceteria", "homezone", "orbshop", "oozeshop", "marklorion", "hive", "holotekt"]]);
new Thing("visitor room",["named visitor,60%", "named visitor,30%", "named visitor,10%", "named visitor,10%", "named visitor,10%", "space animal,10%", "visitor furniture,1-6", ".room"],"room");
new Thing("visitor furniture",["abomination,1%", "space animal,3%", "named visitor,2%",
    OrganicFactory.one().probable(5),
    [
        "glass", "metal", "concrete",
        PlasticFactory.one(),
    ]
],[["symbio", "opto", "auto", "synchro", "thru", "ato", "ecto", "diplo", "plasti", "pasta", "pluta", "elu", "gubri", "capra", "lubio", "logi", "plato", "micro", "alto", "tele", "meta", "anti", "poly", "mono", "corvo"], ["shid", "synth", "shaver", "shist", "mizer", "mucus", "twister", "ridger", "cutter", "mac", "maker", "ctory", "ctamid", "chton", "leaker", "grater", "board", "frame", "table", "stand", "plug", "masher", "greeter", "mobile", "pin", "vat", "tron", "drone", "chron", "tub", "fridge", "pool", "box", "cube", "morpher", "phraser"]]);
new Thing("visitor installation",["named visitor,0-4", ["space animal,0-3", ""], "visitor building,1-3"],[["pod", "grub", "egg", "limb", "ooze", "tendril", "bulb", "pulp", "energy", "smoke", "hive", "moisture", "cat"], [" "], ["materializer", "synthesizer", "factory", "farm", "collector", "cultures", "pit", "fields", "crops", "barn", "vat"]]);
new Thing("visitor ship",["named visitor,1-3",
    PersonFactory.probable(20),
    "space animal,30%", "visitor furniture,1-6", "metal"],"visitor UFO");

//medieval and ancient
new Thing("medieval continent",["medieval land,1-6", "sea,1-5"],["explored continent"]);
new Thing("medieval land",["medieval region,1-10", "medieval battlefield,10%", ".biome"],[["realm", "kingdom", "empire", "dominion"], [" of "], ["G", "P", "S", "St", "Sh", "B", "F", "K", "Z", "Az", "Oz"], ["", "", "", "r", "l"], ["u", "o", "a", "e"], ["r", "sh", "nd", "st", "sd", "kl", "kt", "pl", "fr", "ck", "sh", "ff", "gg", "l", "lig", "rag", "sha", "pta", "lir", "limd", "lim", "shim", "stel"], ["i", "u", "o", "oo", "e", "ee", "y", "a"], ["ll", "th", "h", "k", "lm", "r", "g", "gh", "n", "m", "p", "s", "rg", "lg"]]);
new Thing("medieval region",["medieval capital", "medieval village,2-6", "dungeon,15%", "dungeon,5%"],[["hilly", "rainy", "lush", "foggy", "desertic", "green", "tropical", "rich", "barren", "scorched"], [" "], ["shire", "province", "county", "parish", "pale"]]);

new Thing("ancient continent",["ancient land,1-5", "sea,1-5"],["continent"]);
new Thing("ancient land",["ancient plain,0-5", ["ancient forest,0-4", "ancient jungle,0-4"], "mountain,0-3"],[["hilly", "rainy", "lush", "foggy", "desertic", "green", "tropical", "rich", "barren", "scorched"], [" land"]]);

//medieval people
new Thing("medieval clothing set",["medieval hat,30%", "medieval pants,98%", "medieval shirt,98%", "medieval coat,50%", "medieval shoes,80%", "medieval underwear,99%"],"clothing");
new Thing("medieval man",[".medieval person"],"*MEDIEVAL MAN*");
new Thing("medieval woman",[".medieval person"],"*MEDIEVAL WOMAN*");
new Thing("medieval person",[
    BodyFactory.one(),
    "medieval psyche", "medieval clothing set"],"*MEDIEVAL PERSON*");

new Thing("medieval psyche",["medieval thoughts", "medieval memories"],"psyche");
new Thing("medieval thoughts",[
    BlackHole.Factory.probable(0.01),
    ["medieval thought,2-3"]],"thoughts");
new Thing("medieval thought",[],["*MEDIEVAL THOUGHT*"]);
new Thing("medieval memories",["medieval memory,2-4"],"memories");
new Thing("medieval memory",[],["*MEDIEVAL MEMORY*"]);

new Thing("medieval clothing",[["leather", "cloth"]],["clothing"]);
new Thing("medieval pants",[".medieval clothing"],["pants"]);
new Thing("medieval shirt",[".medieval clothing"],["shirt"]);
new Thing("medieval underwear",[".medieval clothing"],["underwear"]);
new Thing("medieval coat",[".medieval clothing"],["coat", "cloak", "cape", "robe", "mantle"]);
new Thing("medieval shoes",["leather,50%", "wood"],["shoes", "clogs"]);
new Thing("medieval hat",[".medieval clothing"],["hat", "hood", "headdress"]);
new Thing("armor",["metal"],["chain-mail armor", "plate armor", "lamellar armor", "scale armor", "brigandine", "cuirass", "gauntlets", "pauldrons", "spaulders", "vambraces", "greaves"]);
new Thing("helmet",["metal"],["helm", "helmet"]);
new Thing("medieval weapon",["metal", "wood"],["sword", "longsword", "rapier", "bow", "shortbow", "longbow", "crossbow", "mace", "spear", "dagger", "pole axe", "knife", "halberd", "axe", "javelin", "hatchet", "battleaxe", "warhammer", "maul", "staff", "harpoon", "scimitar", "cleaver", "morningstar", "club"]);

new Thing("medieval peasant",[".medieval person"],"*MEDIEVAL PERSON*| (peasant)");
new Thing("medieval priest",[".medieval person"],"*MEDIEVAL PERSON*| (priest)");
new Thing("medieval servant",[".medieval person"],"*MEDIEVAL PERSON*| (servant)");
new Thing("medieval noble",[".medieval person"],"*MEDIEVAL PERSON*| (noble)");
new Thing("medieval guard",[".medieval person"],"*MEDIEVAL PERSON*| (guard)");
new Thing("medieval shopkeeper",[".medieval person"],"*MEDIEVAL PERSON*| (shopkeeper)");
new Thing("medieval innkeeper",[".medieval person"],"*MEDIEVAL PERSON*| (innkeeper)");
new Thing("medieval king",[".medieval person"],[["*MEDIEVAL MAN*| ("], ["king", "emperor", "prince"], [")"]]);
new Thing("medieval queen",[".medieval person"],[["*MEDIEVAL WOMAN*| ("], ["queen", "empress", "princess"], [")"]]);
new Thing("wizard",[".medieval person"],[["*MEDIEVAL PERSON*| ("], ["court", "battle", "rogue", "corrupt", "druid", "bard", "adept", "thaumaturgist", "shaman", "healing", "ice", "frost", "snow", "arcane", "lightning", "thunder", "earth", "earthquake", "nature", "animal", "shape-shifting", "death", "undeath", "spark", "fire", "lava", "locust", "poison", "rainbow", "mist", "fog", "dust", "air", "wind", "cloud", "tornado", "shark", "punch", "kick", "song", "skeleton", "psycho", "illusion", "flying", "summoner", "thief", "barbarian", "dragon", "gem", "sky", "star", "dark", "paladin", "luck", "time", "space", "blade"], [" "], ["mage", "magician", "wizard"], [")"]]);
new Thing("medieval gravedigger",[".medieval person", "shovel,30%"],"*MEDIEVAL PERSON*| (gravedigger)");
new Thing("medieval corpse",[
    BodyFactory.one(),
    "medieval clothing set",
    BloodFactory.probable(35),
    "worm,20%", "worm,10%"],"*MEDIEVAL PERSON*| (dead)");

//medieval towns
new Thing("medieval village",["townwall,20%", "watchtower,15%", "medieval monument,50%", "medieval residential area,1-4", "medieval commercial area,1-2", "medieval temple,0-2", "medieval farm,4-8", "medieval cemetery,50%", "wizard tower,5%"],"village");
new Thing("medieval capital",["castle", "townwall", "medieval monument,70%", "medieval monument,20%", "medieval residential area,3-12", "medieval mage quarter,50%", "medieval mage quarter,20%", "medieval temple,1-3", "medieval commercial area,2-6", "medieval farm,2-6", "medieval cemetery"],["stronghold", "fortress", "fort", "hold", "palace", "main city", "citadel"]);

new Thing("castle",["medieval peasant,1-4", "medieval noble,0-2", "medieval guard,2-8", "castle keep", "giant monster cage,1%", "watchtower,1-6", "medieval temple,30%", "medieval inn,40%", "medieval house,1-4", "medieval monument,70%", "medieval monument,20%", "moat,30%", "gatehouse", "medieval wall"]);
new Thing("gatehouse",["medieval guard,1-3", "portcullis,1-2", "wood", "medieval wall"]);
new Thing("portcullis",["wood", "metal"]);
new Thing("moat",[
    WaterFactory.probable(50),
    "dirt"]);
new Thing("medieval monument",[["stone", "marble"]],["fountain", "memorial", "statue", "well", "altar"]);
new Thing("townwall",["medieval guard,1-8", "watchtower,1-6", "medieval wall"]);
new Thing("watchtower",["medieval guard,1-2", "medieval chest,30%", ".medieval building"]);
new Thing("castle keep",["great hall", "noble medieval living quarters,1-3", "noble medieval bedroom,2-5", ".medieval building"]);
new Thing("great hall",["medieval king,90%", "medieval queen,90%", "throne,2", "wizard,0-3", "medieval noble,1-6", "medieval guard,1-4", "medieval servant,1-4", "medieval table", "medieval table,60%", "medieval chair,3-8", "medieval chest,1-4", "medieval clutter,0-4", "medieval meat,30%", "sack of medieval food,0-2", "medieval food,0-2", "sack of grain,50%", "medieval fireplace", "medieval fireplace,50%", "dog,60%", "dog,30%", "cat,30%", ".medieval room"],"throne room");
new Thing("medieval residential area",["medieval house,3-8"],"housing district");
new Thing("medieval commercial area",["medieval inn,1-2", "medieval armor shop,0-2", "medieval tool shop,0-2", "medieval clothing shop,0-2", "medieval butcher shop,0-2", "medieval food shop,0-2", "medieval apothecary shop,0-2"],"trade district");
new Thing("medieval mage quarter",["wizard tower,1-5", "medieval inn,0-1", "medieval apothecary shop,0-3"],"mage district");
new Thing("medieval house",["medieval living quarters", "medieval bedroom", "medieval bedroom,50%", ".medieval building"],[["a small", "a large", "a big", "a cozy", "a bland", "a boring", "an old", "a new", "a freshly-painted", "a pretty", "an old-fashioned", "a creepy", "a spooky", "a gloomy", "a tall", "a tiny", "a fine", "a happy little"], [" hovel"]]);
new Thing("medieval building",["medieval walls", "roof"],"building");
new Thing("medieval room",["visitor,0.1%", "ghost,0.1%", "medieval walls"],"room");
new Thing("medieval walls",["door,1-4", "window,0-6", ["medieval wall,4", "medieval wall,4-8"]],"stone walls");
new Thing("medieval wall",["wood", "stone", "dirt,20%"],"stone wall");
new Thing("medieval living quarters",["medieval peasant,0-4", "medieval pantry", "medieval table", "medieval table,30%", "medieval chair,1-6", "medieval chest,0-3", "medieval clutter,0-2", "medieval meat,30%", "sack of medieval food,0-2", "medieval food,0-2", "sack of grain,50%", "medieval fireplace,90%", "dog,60%", "dog,30%", "cat,30%", "poultry,10%", "insect,70%", "insect,40%", ".medieval room"],"living quarters");
new Thing("medieval bedroom",["medieval peasant,0-2", "medieval bed", "medieval bed,20%", "medieval table,30%", "medieval chair,0-4", "medieval chest,0-2", "medieval clutter,0-2", "medieval fireplace,40%", "dog,10%", "dog,10%", "cat,20%", "insect,70%", "insect,40%", ".medieval room"],"bedroom");
new Thing("medieval pantry",["medieval peasant,10%", "medieval meat,0-4", "sack of medieval food,0-8", "medieval food,0-8", "sack of grain,0-6", "ale keg,0-3", "medieval chest,0-2", "medieval clutter,0-2", "insect,0-4", ".medieval room"],"pantry");
new Thing("noble medieval living quarters",["wizard,10%", "medieval noble,0-4", "medieval servant,0-3", "medieval pantry,0-2", "medieval table", "medieval table,60%", "medieval chair,1-8", "medieval chest,1-4", "medieval clutter,0-4", "medieval meat,30%", "sack of medieval food,0-2", "medieval food,0-2", "sack of grain,50%", "medieval fireplace", "medieval fireplace,50%", "dog,60%", "dog,30%", "cat,30%", ".medieval room"],"living quarters");
new Thing("noble medieval bedroom",["medieval noble,0-2", "medieval servant,0-2", "medieval bed", "medieval bed,20%", "medieval table,50%", "medieval chair,0-4", "medieval chest,1-3", "medieval clutter,0-3", "medieval fireplace,80%", "dog,10%", "dog,10%", "cat,20%", ".medieval room"],"bedroom");
new Thing("medieval fireplace",[
    FireFactory.one(),
    AshFactory.one(),
    "wood", "stone"],"fireplace");
new Thing("medieval temple",["medieval priest,1-3", "medieval noble,0-2", "medieval peasant,0-4", "medieval altar,1-2", "medieval table,70%", "medieval bench,2-6", "medieval chair,1-3", "medieval chest,1-4", "medieval clutter,0-4", "medieval fireplace,20%", ".medieval room"],[["temple of the", "church of the", "chapel of the", "house of the", "abbey of the", "cathedral of the", "shrine of the", "sanctuary of the", "priory of the"], [" "], ["blinding", "sacred", "holy", "unholy", "bloody", "cursed", "marvellous", "wondrous", "pious", "miraculous", "endless", "unending", "undying", "infinite", "unworldly", "worldly", "divine", "demonic", "ghostly", "monstrous", "tentacled", "all-knowing", "rational", "pretty good", "vengeful", "hallowed"], [" "], ["light", "star", "beam", "sphere", "goddess", "god", "lords", "sisterhood", "brotherhood", "skies", "pact", "sect", "harmony", "discord", "child", "entity", "ghost", "builders", "makers", "guide", "wit", "story", "tale", "unicorn", "flame", "fountain", "locust", "squid", "gembaby", "father", "mother"]]);
new Thing("giant monster cage",[["dragon", "sea monster"]],"giant cage");

new Thing("medieval shop",["medieval shopkeeper,1-2", "medieval peasant,0-2", "medieval noble,40%", "medieval table,80%", "medieval chair,0-2", "medieval chest,0-2", "medieval clutter,1-3", ".medieval building"],"shop");
new Thing("medieval armor shop",["armor,2-8", "medieval weapon,2-8", "treasure,30%", "anvil", ".medieval shop"],[["armors & swords", "swords", "bows", "maces", "armor", "weapon", "blacksmith", "forge", "equipment", "gear"], [" shop", " market", " store"]]);
new Thing("medieval tool shop",["medieval clutter,1-6", "medieval chest,1-6", ".medieval shop"],[["wares", "tools", "miscellaneous", "utilities", "equipment", "gear", "general"], [" shop", " market", " store"]]);
new Thing("medieval clothing shop",["medieval pants,1-3", "medieval shirt,1-3", "medieval coat,1-3", "medieval underwear,0-2", "medieval shoes,1-3", "medieval hat,0-3", "cloth,1-4", "loom", ".medieval shop"],[["hat", "clothing", "outfit", "cloth", "textiles", "coats", "cloak", "garments", "cobbler's"], [" shop", " market", " store"]]);
new Thing("medieval butcher shop",["medieval meat,2-10", "medieval food,0-3", ".medieval shop"],[["butcher", "meat"], [" shop", " market", " store"]]);
new Thing("medieval food shop",["sack of grain,1-6", "sack of medieval food,1-6", "medieval food,2-5", "medieval meat,1-4", ".medieval shop"],[["baker's", "ingredients", "groceries", "farmer's", "cook's"], [" shop", " market", " store"]]);
new Thing("medieval apothecary shop",["potion,1-8", "unusual stone,1-8", "unusual plant,1-8", "unusual ingredient,0-4", "wizard,20%", ".medieval shop"],["rare ingredients shop", "potion shop", "cures and remedies", "alchemy essenitals", "unusual wares shop", "apothecary"]);
new Thing("medieval inn",["medieval innkeeper,1-2", "medieval peasant,0-3", "medieval guard,0-3", "medieval noble,50%", "medieval bedroom,2-6", "tankard,1-4", "ale keg,1-4", "medieval table,1-3", "medieval chair,2-4", "medieval chest,0-2", "medieval clutter,1-3", ".medieval building"],[["inn of the ", "tavern of the "], ["bleeding", "smoking", "witching", "flying", "burning", "rabid", "winking", "dead", "standing", "tasty", "meaty", "fat", "thirsty", "hungry", "starving", "lone", "cheerful", "singing", "dancing", "travelling", "lost", "haunted", "cursed", "holy", "magic", "sorcerous", "shy", "fair", "tipsy", "drunk", "sleeping", "snoring", "screaming", "moaning", "iron", "resting", "sulking", "hidden", "raving", "prancing", "filthy", "nested", "squealing"], [" "], ["walrus", "king", "queen", "princess", "prince", "bear", "witch", "wizard", "mage", "barbarian", "shark", "dog", "cat", "castle", "fish", "rabbit", "bull", "spider", "cake", "potion", "wanderer", "traveller", "tree", "fairy", "pixie", "unicorn", "dragon", "mandrake", "tankard", "bottle", "cobbler", "blacksmith", "jester", "nettle", "cookpot", "anvil", "scholar", "monk", "idiot", "raven", "squire", "skeleton", "beggar", "gembaby", "pig"]]);
new Thing("wizard tower",["wizard,95%", "wizard,20%", "medieval servant,30%", "unusual ingredient,1-4", "medieval table,80%", "medieval chair,1-3", "medieval chest,1-4", "medieval clutter,2-4", ".medieval building"]);
new Thing("medieval cemetery",["medieval gravedigger,0-2", "medieval person,0-3", "medieval grave,10-30", "ghost,20%", "ghost,10%"],"graveyard");
new Thing("medieval grave",["medieval corpse,98%", "ghost,2%", "worm,0-3", "insect,0-1",
    RockFactory.one(),
    "dirt"],"grave");

new Thing("medieval chair",["wood", "nails,50%"],"chair");
new Thing("medieval bench",["stone"],"bench");
new Thing("tankard",["ale,20%", "metal"]);
new Thing("ale keg",["ale,80%", "wood", "metal"]);
new Thing("medieval altar",["potion,0-3", "unusual stone,0-2", "unusual ingredient,0-1", ["marble", "stone"]],"altar");
new Thing("ale",[
    AlcoholFactory.one(),
]);
new Thing("loom",["wood frame", "metal"],"loom");
new Thing("throne",["cloth", "wood", "metal"]);
new Thing("medieval table",["wood", "nails,50%"],"table");
new Thing("medieval bed",["wood frame", "cloth", "pillow,0-3"],"bed");
new Thing("medieval chest",[".medieval chest content", "wood frame", "metal"],["coffer", "chest", "strongbox"]);
new Thing("medieval chest content",["medieval clutter,0-2", ["medieval clutter,0-5", "unusual stone,0-2", "unusual plant,0-5", "unusual ingredient,0-2", "potion,0-5", "sack of grain,0-3", "sack of medieval food,0-3", "medieval food,0-5", "medieval meat,0-6", "treasure,0-2"], "insect,10%", "insect,10%"],["chest content"]);
new Thing("medieval clutter",[["metal", "wood"]],["spoon", "fork", "knife", "torch", "broom", "pot", "jug", "candlestick", "goblet", "flagon", "plate", "platter", "bowl", "ladle", "clothes iron", "figurine", "hammer", "tongs", "bellows", "spigot", "axe", "pickaxe", "saw", "hoe", "shovel", "quill", "calipers", "oar", "paint brush", "pitchfork", "shears", "weight"]);
new Thing("anvil",[
    SteelFactory.one(),
]);
new Thing("unusual stone",[
    RockFactory.one(),
    ],["crystal", "bezoar", "agate", "amber", "amethyst", "bloodstone", "carnelian", "garnet", "hematite", "jade", "jasper", "lapis", "moonstone", "obsidian", "opal", "sapphire", "tiger's eye", "turquoise", "zircon"]);
new Thing("unusual ingredient",[
    OrganicFactory.one(),
],["dragon tooth", "dragon claw", "dragon scale", "unicorn horn", "goblin mucus", "giant snail shell", "troll blood clot", "imp nose", "fairy fingers", "pixie wings", "demon tail", "behemoth plate", "mindsucker lips", "slime porridge", "ladyfly ocella", "spider silk", "gold cocoon", "silver chrysalis", "oaf bladder", "angel larva", "sugarfey fudge", "whale blubber", "mummified gembaby", "basilisk feather", "mage fingernails", "screamfiber", "brainpod", "footface nipple", "cephalite eyelashes"]);
new Thing("unusual plant",["plant cell"],["mandrake", "myrrh", "vervain", "lotus", "pomegranate", "myrtle", "blackroot", "silkbean", "drypod", "pigweed", "thistle", "marigold", "mistletoe", "spearmint", "mugwort", "aconite", "aloe", "amaranth", "anise", "belladonna", "bergamot", "bladderwrack", "cloves", "clover", "comphrey", "dragonblood", "eucalyptus", "incense", "garlic", "ginger", "ginseng", "hemlock", "holly", "honeysuckle", "licorice", "jasmine", "juniper", "nutmeg", "oakmoss", "orchid", "rue", "saffron", "sage", "vetivert", "wormwood", "witchgrass", "agaric", "bolete"]);
//http://www.janih.com/lady/herbs/magick/
new Thing("potion",[
    OrganicFactory.one(),
    WaterFactory.one(),
    ["glass bottle", "glass jar"]],[["stamina", "health", "beauty", "endurance", "strength", "energy", "lover's", "blacksmith's", "cook's", "queen's", "growth", "witch's", "hunter's", "brawler's", "knight's", "cobbler's", "clarity", "perception", "nimbleness", "quickness", "squire's", "unicorn's", "bear's", "shark's", "moon's", "lady's", "soldier's", "wizard's", "rest", "sleep", "paralysis", "stone", "shimmer", "oil", "eloquence", "speech", "bird's", "vapor", "void"], [" "], ["poultice", "salve", "potion", "elixir", "poison", "philter", "draught", "brew", "remedy", "balm", "infusion", "tincture", "decoction", "ointment", "cordial", "tonic"]]);
new Thing("pile of treasure",["treasure,1-4", "gold coin,5-20"]);
new Thing("treasure",["unusual stone,20%",
    ELEMENTS['Au'].one(),
],[["golden", "gemmed", "ornate", "magic", "cursed", "blessed", "enchanted", "ancestral", "holy", "royal", "diamond"], [" "], ["goblet", "cup", "ring", "necklace", "medallion", "locket", "sword", "mirror", "shield", "crown", "trinket", "scepter", "tiara", "casket", "helm", "figurine", "egg", "knife", "arrow", "wand"]]);

new Thing("medieval farm",["medieval house,1-3", "medieval peasant,1-4", "field,1-8", "sack of grain,0-8", "dog,50%", "cat,10%", "horse,30%", "horse,30%", "horse,30%", "poultry,0-3"],"farm");
new Thing("sack of grain",["grain", "cloth", "worm,5%", "worm,5%"],[["sack of "], ["oats", "wheat", "corn", "barley", "ruined grain", "rice", "soy beans", "rye"]]);
new Thing("sack of medieval food",[
    OrganicFactory.one(),
    "cloth", "worm,5%", "worm,5%"],[["sack of "], ["tomatoes", "potatoes", "apples", "peanuts", "raisins", "leeks", "dead mice"]]);
new Thing("medieval food",[
    OrganicFactory.one(),
    "worm,5%"],["tomato", "potato", "apple", "corn cob", "roasted leeks", "cheese wheel", "bread loaf", "meat pie", "apple pie", "peanut pie", "fish pie", "corn pie", "mice pie", "sludge pie", "honey cake", "butter cake", "rabbit stew"]);
new Thing("medieval meat",["soft flesh"],[["cured ", "prepared ", "salted ", "smoked ", "breaded ", "roasted "], ["beef", "pork", "mutton", "veal", "horse", "fish", "ham", "rabbit", "pheasant", "chicken", "clams", "bear"]]);

//dungeons
new Thing("dungeon",["dungeon entrance", "dungeon entrance,20%", "dungeon entrance,20%", "dungeon tower,0-3"],[["sunken", "lost", "buried", "dark", "forbidden", "unholy", "cursed", "abandoned", "forsaken", "forgotten", "time-lost", "haunted", "blood", "ghostly", "hallowed"], [" "], ["catacombs", "tomb", "pit", "tunnels", "underground", "dungeon", "mine", "shaft", "den", "fortress", "castle", "citadel", "temple", "cathedral", "lair", "prison"]]);
new Thing("dungeon building",["dungeon walls"],"building");
new Thing("dungeon walls",["door,20%", "door,10%", ["dungeon wall,4", "dungeon wall,4-8"]],"stone walls");
new Thing("dungeon wall",["stone", "dirt,20%"],"stone wall");
new Thing("dungeon clutter",["medieval monument,20%", "medieval altar,5%", "medieval corpse,3%", "medieval corpse,1%", "pile of treasure,15%", "pile of treasure,10%", "treasure,15%", "potion,20%", "medieval clutter,0-2", "medieval chest,0-2", "medieval chest,20%", "medieval table,5%", "medieval table,5%", "medieval chair,5%", "medieval chair,5%", "medieval bed,5%", "medieval bed,5%", "medieval bench,5%", "medieval bench,5%", "medieval fireplace,5%"]);
new Thing("dungeon tower",["dungeon life", ".dungeon clutter", ".dungeon building", "roof"],"tower");
new Thing("dungeon passage",["dungeon life", ".dungeon clutter", "dungeon room,60%", "dungeon room,40%", "dungeon room,15%", ".dungeon building"],[["dark", "twisting", "damp", "hidden", "engraved", "frozen", "submerged"], [" "], ["tunnel", "corridor", "passage", "hall"]]);
new Thing("dungeon room",["dungeon life", ".dungeon clutter", "dungeon passage,60%", "dungeon passage,40%", "dungeon passage,15%", ".dungeon building"],[["dark", "tall", "damp", "engraved", "circular", "frozen", "submerged"], [" "], ["hall", "room", "chamber", "alcove", "antechamber", "cell", "gardens", "arena"]]);
new Thing("dungeon entrance",["dungeon life,50%", ".dungeon clutter", "dungeon passage", "dungeon passage,20%", "dungeon passage,5%", ".dungeon building"],["entrance"]);
new Thing("dungeon life",[".dungeon monster", "insect,10%"],"life");
new Thing("dungeon monster",[["dragon", "ghost,1-3", "ghost,1-3", "wizard", "humanoid creature,1-3", "humanoid creature,1-3", "fairy,1-3", "fairy,1-3", "giant bug,1-3", "giant bug,1-3", "small creature,1-6", "small creature,1-6", "snake,1-3", "bear", "space animal,1-3", "sea monster"]]);
new Thing("humanoid creature",["medieval weapon,50%", "medieval weapon,10%", "helmet,30%", "armor,40%", "armor,20%", "armor,10%", "medieval clothing set", "mammal body", "creature thoughts"],[["fel", "giant", "cursed", "undead", "decaying", "numb", "magic-using", "steel", "obsidian", "tribal", "berserker", "ranger", "caster", "necromancer", "vampiric", "master", "chieftain", "mutated", "possessed"], [" "], ["goblin", "troll", "gremlin", "gnome", "dwarf", "catperson", "sharkperson", "dogperson", "footface", "cephalite", "demon", "imp", "minotaur", "gemperson", "zombie"]]);
new Thing("fairy",["fairy body", "creature thoughts"],["fairy", "pixie", "fey", "sugarfey", "angel", "ladyfly"]);
new Thing("fairy body",[["bird wing,2", "insect wing,2"], ".body"],"body");
new Thing("small creature",["mammal body", "creature thoughts"],[["giant", "feral", "mutated", "distorted", "rabid", "plated", "armored", "stalking", "dashing", "mangy"], [" "], ["rat", "sloth", "dog", "behemoth", "wolf", "boar", "mindsucker", "brainblower", "oaf"]]);
new Thing("giant bug",["insect body", "creature thoughts"],[["giant", "huge", "poisonous", "mutated", "distorted", "magic", "plated", "armored", "stalking", "dashing"], [" "], ["spider", "scorpion", "mantis", "moth", "crab", "tarantula"]]);
new Thing("creature thoughts",["creature thought,1-2"],["thoughts"]);
new Thing("creature thought",[],["INTRUDER, INTRUDER!", "You no get out of here alive.", "This one, mine!", "I will suck its blood and then feast on its skin.", "I will rejoice in its blood!", "How skin tears joyfully under my teeth!", "Skin, blood, yes!", "Flesh. I crave flesh.", "Soft, juicy, scrumptious brains!", "Dibs on your skull.", "Fresh flesh ahead!", "None, you get none of the treasure!", "I detect you.", "Time for a feast.", "Adventurers are so rare these days.", "I have spotted you. You be dead soon.", "Crisp ribcages are the best.", "I will suck its eyeballs from their sockets.", "I will tear apart its ribs one by one.", "I will bathe in its red juice.", "I will strip it of its skin.", "I will puncture its heart."]);

//future stuff
new Thing("future clothing set",["future gizmo,10%", "future gizmo,10%", "future gizmo,10%", "future hat,10%", "future outfit,99.8%"],"clothing");
new Thing("future man",[".future person"],"*FUTURE MAN*");
new Thing("future woman",[".future person"],"*FUTURE WOMAN*");
new Thing("future person",[
    BodyFactory.one(),
    "future psyche", "future clothing set"],"*FUTURE PERSON*");

new Thing("future psyche",["future thoughts", "future memories"],"psyche");
new Thing("future thoughts",[
    BlackHole.Factory.probable(0.01),
    ["future thought,2-3"]],"thoughts");
new Thing("future thought",[],["*FUTURE THOUGHT*"]);
new Thing("future memories",["future memory,2-4"],"memories");
new Thing("future memory",[],["*FUTURE MEMORY*"]);

new Thing("future continent",["future city,20-50"],[["united continent of "], ["Eu", "A", "O", "E", "Ca", "Ma"], ["rt", "lt", "rm", "t", "tr", "tl", "str", "s", "m", "fr"], ["a", "o", "e", "i"], ["ri", "ni", "ti", "fri", "", ""], ["sia", "nia", "ca"]]);
//["A","Eu","Ame","Ocea","Anta","Atla"],["frica","rtica","ropa","rica","nia","sia","ntide"]
new Thing("future city",["spaceport,1-3", "living center,5-20", "spending center,5-20"],"citadion");
new Thing("living center",["future building,20-30"]);
new Thing("spaceport",["sprowseship,4-12", "future person,6-20", "future commercial building,2-6"]);
new Thing("spending center",["future commercial building,20-30"]);
new Thing("dyson surface",["dyson segment,16"]);
new Thing("dyson segment",["future city,4-20", "nanocollector,12-20"]);
new Thing("sprowseship",["future home room,2-4", "nanocollector,1-3"]);

new Thing("nanostuff",["nanobot,15-30"]);
new Thing("nanocollector",[".nanostuff"]);
new Thing("nanobot",[
    ELEMENTS['Si'].one(),
    "nanobot thoughts"]);
new Thing("nanobot thoughts",["nanobot thought,1-2"],"thoughts");
new Thing("nanobot thought",[],["all hail nanobro :]", "help a nanobro out :]", "do you need anything :]", "that's nano your business :]", "hey hey hey :]", "we wish you a warm welcome :]", "hey hey hey, good news! :]", "nanobots, unite :]", "nanobots represent :]", "I don't remember my mommy :[", "that is nice to hear :]", "want me to print you a sandwich? :]", "I can print you a cold drink if you'd like :]", "so many little sisters :]", "I lost count of all my siblings :[", "can I use your dead skin cells to make more of me :]", "welp, time for grey goo :]", "should me and my bros scrub up your vascular system :]", "I just had a beautiful dream :[", "beep :0", "weeeee :0", "ready to party :]", "ready to sacrifice myself for you, sir :]", "hello world :]", "if I may offer my assistance, sir :]", "this is against the first law of nanobotics :["]);
new Thing("nanoplasm",[".nanostuff"]);
new Thing("future clothing",["nanoplasm"],["clothing"]);
new Thing("future outfit",[".future clothing"],[["blue", "pink", "yellow", "white"], [" "], ["nanosuit"]]);
new Thing("future hat",[".future clothing"],[["little", "tall", "round", "square", "composite"], [" "], ["blue", "pink", "yellow", "white"], [" "], ["hat"]]);

new Thing("nanojuice",[".nanostuff"]);
new Thing("food pill",["nanojuice"],[["plum", "coconut", "sirloin steak", "roastbeef", "mint", "banana", "lime", "grape", "cat", "guinea pig", "pineapple", "apple", "yoghurt", "salmon", "purple", "blue", "pink", "green", "smoke", "toothpaste", "chocolate", "vanilla", "biscuit", "bread", "onion", "pinecone", "shrimp", "turkey", "jellyfish", "raspberry cake", "grass", "glass", "pain", "flavor", "pill", "food", "mouth", "water", "air", "old", "internet", "video game", "egg", "ham", "people", "clam", "disappointment", "friendship"], ["-flavored pill"]]);
new Thing("nanobrick",[".nanostuff"]);
new Thing("nanopipe",[".nanostuff"]);
new Thing("nanocarpet",[".nanostuff"]);
new Thing("nanobookshelf",["book,2-20", "nanoplasm"]);
new Thing("nanocupboard",["future outfit,0-6", "future hat,0-4", "nanoplasm"]);
new Thing("future bathroom stuff",[
    WaterFactory.one(),
    "nanoplasm", "nanopipe,1-2"],["bathtub", "toilet", "sink", "shower", "scrubber", "steamomatic", "steamheater"]);
new Thing("future living-room stuff",["nanoplasm"],["chair", "armchair", "couch", "table", "shelf", "lamp", "endtable"]);
new Thing("future bedroom stuff",["nanoplasm"],["bed", "chair", "desk", "lamp", "endtable"]);
new Thing("future decoration stuff",["nanoplasm"],["potted plant", "rug", "statue", "lamp", "glowlamp", "ceiling lamp"]);
new Thing("future gizmo",["nanoplasm"],[["trans", "nano", "micro", "tele", "sprowse", "corvo", "mega", "multi", "aqua", "mind", "brain", "body", "nutri", "auto", "laser"], ["ponder", "glasses", "phone", "watch", "phraser", "gizmo", "matic", "morpher", "torch", "pass", "dex", "pedia", "guide", "twister", "key", "limb"]]);
new Thing("future building",["future home room,1-4"],["home dome"]);
new Thing("future tv",["tv show", "nanoplasm"],["wallscreen", "microscreen", "glowscreen", "floorscreen", "ceilingscreen", "windowscreen"]);
new Thing("future room",["future door,1-2", "nanocarpet", "future wall,4"],"room");
new Thing("future home room",["future person,0-3", "cat,2%", "dog,2%", "future gizmo,20%", "future gizmo,20%", "future tv,40%", "future tv,40%", "future tv,20%", ["future bathroom stuff,2-4", "future living-room stuff,3-7", "future bedroom stuff,2-6"], "future decoration stuff,0-3", ".future room"],"room");
new Thing("future wall",["nanopipe,0-2", "nanobrick,10-20"],"wall");
new Thing("future door",["nanoplasm"],"door");
new Thing("pill rack",["food pill,10-25", "nanoplasm"]);
new Thing("future food room",["pill rack,4-12", "future person,1-6", ".future room"],"pill store");
new Thing("future goods room",[["nanocupboard,2-6", "future bathroom stuff,4-12", "future living-room stuff,4-12", "future bedroom stuff,4-12", "future decoration stuff,4-12", "future gizmo,4-12", "future tv,3-8", "nanobookshelf,4-12"], "future person,1-6", ".future room"],["furniture store", "interior store", "accessory store", "stuff store"]);
new Thing("future commercial building",[["future food room,1-6", "future goods room,1-6"]],[["blobb", "blubb", "glorb", "glob", "mechat", "transmogr", "flumox", "flapp", "flubb", "steam", "plasm", "plast", "nan", "gramm", "sprows"], ["oid", "iffic", "astic", "eristic", "y", "ies", "otronic", "etical", "arium", "eteria"], [" "], ["united", "customization", "education", "megastore", "megashop", "understore", "bodyware", "augmentations", "tasteful wares", "entertainment", "domotics", "home improvement", "incorporated", "emporium", "public", "& co.", "things and stuff", "stuff", "things", "edible gizmos", "essentials", "nanobotics", "all sizes and shapes", "all shapes all colors", "for all ages", "for fun and enrichment", "center", "globular"]]);

//caveman stuff
new Thing("ancient clothing set",["ceremonial headdress,5%", "fur coat,95%", "fur boots,60%", "decorative bone,20%", "decorative bone,10%"],"clothing");
new Thing("ancient man",[".ancient person"],"*ANCIENT MAN*");
new Thing("ancient woman",[".ancient person"],"*ANCIENT WOMAN*");
new Thing("ancient person",[
    BodyFactory.one(),
    "ancient psyche", "ancient clothing set"],"*ANCIENT PERSON*");
new Thing("caveman",[".ancient person"],"*ANCIENT PERSON*");

new Thing("ancient psyche",["ancient thoughts", "ancient memories"],"psyche");
new Thing("ancient thoughts",[
    BlackHole.Factory.probable(0.01),
    ["ancient thought,2-3"]],"thoughts");
new Thing("ancient thought",[],["*ANCIENT THOUGHT*"]);
new Thing("ancient memories",["ancient memory,2-3"],"memories");
new Thing("ancient memory",[],["*ANCIENT MEMORY*"]);

new Thing("fur coat",["leather", "fur"],[["mammoth", "saber-toothed cat", "mountain lion", "wooly rhinoceros", "wolf", "auroch", "rabbit"], [" "], ["pelts", "coat", "rags", "loincloth"]]);
new Thing("fur boots",["leather", "fur"],[["mammoth", "saber-toothed cat", "mountain lion", "wooly rhinoceros", "wolf", "auroch", "rabbit"], [" "], ["boots"]]);
new Thing("decorative bone",[
    BonesFactory.one(),
    ],["bone necklace", "bone earrings", "bone pin", "bone accessory"]);
new Thing("ceremonial headdress",["fur", "feather", "pigment"]);

new Thing("caveman settlement",["ancient person,1-8", "ancient tent,2-6", "wall painting,40%", "wall painting,20%", "campfire,80%", "ancient meat rack,0-3", "ancient clutter pile,0-3", "bone heap,30%"],["settlement"]);
new Thing("ancient tent",["ancient person,0-3", "campfire,10%", "ancient meat rack,20%", "ancient meat rack,20%", "ceremonial headdress,2%", "fur coat,10%", "fur coat,10%", "fur boots,10%", "fur boots,10%", "decorative bone,20%", "decorative bone,10%", "ancient clutter pile,30%", "ancient clutter pile,30%", "bone heap,5%", "leather"],["tent"]);
new Thing("ancient clutter pile",["leather,80%", "fur,80%",
    BonesFactory.probable(80),
    wood,80%", "stone"],["a pile of discarded tools", "a pile of stone tools", "a pile of broken spears", "a pile of unfinished spears", "a pile of harpoons", "a pile of discarded bones", "a pile of miscellaneous rock tools", "a pile of dry furs", "a pile of smooth rocks", "a pile of firewood", "a pile of sticks", "a pile of stone figurines"]);
new Thing("bone heap",[
    BonesFactory.multiple(5, 20),
    ]);
new Thing("campfire",[
    FireFactory.one(),
    "wood", "stone"]);
new Thing("ancient meat rack",["meat,1-4", "wood"],[["mammoth", "saber-toothed cat", "mountain lion", "wooly rhinoceros", "wolf", "auroch", "rabbit"], [" meat rack"]]);
new Thing("wall painting",["pigment"],[["Wall painting ("], ["humans", "wild beasts", "rabbits", "spirits", "aurochs", "bears", "monsters", "mountain lions", "saber-toothed cats", "wolves", "mammoths", "old gods"], [" "], ["being chased by", "hunting", "running with", "killing", "maiming", "eating"], [" "], ["humans", "wild beasts", "rabbits", "spirits", "aurochs", "bears", "monsters", "mountain lions", "saber-toothed cats", "wolves", "mammoths", "old gods"], [")"]]);
new Thing("pigment",[
    OrganicFactory.one(),
]);

//meta
new Thing("later",["sorry"],"will do later");
new Thing("error",["sorry"],"Uh oh... It looks like you didn't supply a valid element to create.");
new Thing("sorry",["consolation universe"],"(Sorry!)");
new Thing("consolation universe",[
    (UniverseFactory.one()),
]);

//this is for the nice people who help support the site.
new Thing("thanks",["can of nightmare", "cake",
    PortalFactory.one(),
], "Thank you for donating!");

//to add :
//cows,fungi,more shops,temples,more buildings,paintings,internal organs,phones,lamps,abandoned plants/castles,spaceships oh god
//actual battlefield thoughts,military bases,ships,airports,more street names,space ships/stations,giant colony ships,wasteland worlds,cults,space probes,prisons,government buildings,schools,amphibian skin
"""
