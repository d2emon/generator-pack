"""
//medieval towns
new Thing("medieval village",["townwall,20%","watchtower,15%","medieval monument,50%","medieval residential area,1-4","medieval commercial area,1-2","medieval temple,0-2","medieval farm,4-8","medieval cemetery,50%","wizard tower,5%"],"village");
new Thing("medieval capital",["castle","townwall","medieval monument,70%","medieval monument,20%","medieval residential area,3-12","medieval mage quarter,50%","medieval mage quarter,20%","medieval temple,1-3","medieval commercial area,2-6","medieval farm,2-6","medieval cemetery"],["stronghold","fortress","fort","hold","palace","main city","citadel"]);

new Thing("castle",["medieval peasant,1-4","medieval noble,0-2","medieval guard,2-8","castle keep","giant monster cage,1%","watchtower,1-6","medieval temple,30%","medieval inn,40%","medieval house,1-4","medieval monument,70%","medieval monument,20%","moat,30%","gatehouse","medieval wall"]);
new Thing("gatehouse",["medieval guard,1-3","portcullis,1-2","wood","medieval wall"]);
new Thing("portcullis",["wood","metal"]);
new Thing("moat",["Water,50%","dirt"]);
new Thing("medieval monument",[["stone","marble"]],["fountain","memorial","statue","well","altar"]);
new Thing("townwall",["medieval guard,1-8","watchtower,1-6","medieval wall"]);
new Thing("watchtower",["medieval guard,1-2","medieval chest,30%",".medieval building"]);
new Thing("castle keep",["great hall","noble medieval living quarters,1-3","noble medieval bedroom,2-5",".medieval building"]);
new Thing("great hall",["medieval king,90%","medieval queen,90%","throne,2","wizard,0-3","medieval noble,1-6","medieval guard,1-4","medieval servant,1-4","medieval table","medieval table,60%","medieval chair,3-8","medieval chest,1-4","medieval clutter,0-4","medieval meat,30%","sack of medieval food,0-2","medieval food,0-2","sack of grain,50%","medieval fireplace","medieval fireplace,50%","dog,60%","dog,30%","cat,30%",".medieval room"],"throne room");
new Thing("medieval residential area",["medieval house,3-8"],"housing district");
new Thing("medieval commercial area",["medieval inn,1-2","medieval armor shop,0-2","medieval tool shop,0-2","medieval clothing shop,0-2","medieval butcher shop,0-2","medieval food shop,0-2","medieval apothecary shop,0-2"],"trade district");
new Thing("medieval mage quarter",["wizard tower,1-5","medieval inn,0-1","medieval apothecary shop,0-3"],"mage district");
new Thing("medieval house",["medieval living quarters","medieval bedroom","medieval bedroom,50%",".medieval building"],[["a small","a large","a big","a cozy","a bland","a boring","an old","a new","a freshly-painted","a pretty","an old-fashioned","a creepy","a spooky","a gloomy","a tall","a tiny","a fine","a happy little"],[" hovel"]]);
new Thing("medieval building",["medieval walls","roof"],"building");
new Thing("medieval room",["visitor,0.1%","ghost,0.1%","medieval walls"],"room");
new Thing("medieval walls",["door,1-4","window,0-6",["medieval wall,4","medieval wall,4-8"]],"stone walls");
new Thing("medieval wall",["wood","stone","dirt,20%"],"stone wall");
new Thing("medieval living quarters",["medieval peasant,0-4","medieval pantry","medieval table","medieval table,30%","medieval chair,1-6","medieval chest,0-3","medieval clutter,0-2","medieval meat,30%","sack of medieval food,0-2","medieval food,0-2","sack of grain,50%","medieval fireplace,90%","dog,60%","dog,30%","cat,30%","poultry,10%","insect,70%","insect,40%",".medieval room"],"living quarters");
new Thing("medieval bedroom",["medieval peasant,0-2","medieval bed","medieval bed,20%","medieval table,30%","medieval chair,0-4","medieval chest,0-2","medieval clutter,0-2","medieval fireplace,40%","dog,10%","dog,10%","cat,20%","insect,70%","insect,40%",".medieval room"],"bedroom");
new Thing("medieval pantry",["medieval peasant,10%","medieval meat,0-4","sack of medieval food,0-8","medieval food,0-8","sack of grain,0-6","ale keg,0-3","medieval chest,0-2","medieval clutter,0-2","insect,0-4",".medieval room"],"pantry");
new Thing("noble medieval living quarters",["wizard,10%","medieval noble,0-4","medieval servant,0-3","medieval pantry,0-2","medieval table","medieval table,60%","medieval chair,1-8","medieval chest,1-4","medieval clutter,0-4","medieval meat,30%","sack of medieval food,0-2","medieval food,0-2","sack of grain,50%","medieval fireplace","medieval fireplace,50%","dog,60%","dog,30%","cat,30%",".medieval room"],"living quarters");
new Thing("noble medieval bedroom",["medieval noble,0-2","medieval servant,0-2","medieval bed","medieval bed,20%","medieval table,50%","medieval chair,0-4","medieval chest,1-3","medieval clutter,0-3","medieval fireplace,80%","dog,10%","dog,10%","cat,20%",".medieval room"],"bedroom");
new Thing("medieval fireplace",["Fire","Ash","wood","stone"],"fireplace");
new Thing("medieval temple",["medieval priest,1-3","medieval noble,0-2","medieval peasant,0-4","medieval altar,1-2","medieval table,70%","medieval bench,2-6","medieval chair,1-3","medieval chest,1-4","medieval clutter,0-4","medieval fireplace,20%",".medieval room"],[["temple of the","church of the","chapel of the","house of the","abbey of the","cathedral of the","shrine of the","sanctuary of the","priory of the"],[" "],["blinding","sacred","holy","unholy","bloody","cursed","marvellous","wondrous","pious","miraculous","endless","unending","undying","infinite","unworldly","worldly","divine","demonic","ghostly","monstrous","tentacled","all-knowing","rational","pretty good","vengeful","hallowed"],[" "],["light","star","beam","sphere","goddess","god","lords","sisterhood","brotherhood","skies","pact","sect","harmony","discord","child","entity","ghost","builders","makers","guide","wit","story","tale","unicorn","flame","fountain","locust","squid","gembaby","father","mother"]]);
new Thing("giant monster cage",[["dragon","sea monster"]],"giant cage");

new Thing("medieval shop",["medieval shopkeeper,1-2","medieval peasant,0-2","medieval noble,40%","medieval table,80%","medieval chair,0-2","medieval chest,0-2","medieval clutter,1-3",".medieval building"],"shop");
new Thing("medieval armor shop",["armor,2-8","medieval weapon,2-8","treasure,30%","anvil",".medieval shop"],[["armors & swords","swords","bows","maces","armor","weapon","blacksmith","forge","equipment","gear"],[" shop"," market"," store"]]);
new Thing("medieval tool shop",["medieval clutter,1-6","medieval chest,1-6",".medieval shop"],[["wares","tools","miscellaneous","utilities","equipment","gear","general"],[" shop"," market"," store"]]);
new Thing("medieval clothing shop",["medieval pants,1-3","medieval shirt,1-3","medieval coat,1-3","medieval underwear,0-2","medieval shoes,1-3","medieval hat,0-3","cloth,1-4","loom",".medieval shop"],[["hat","clothing","outfit","cloth","textiles","coats","cloak","garments","cobbler's"],[" shop"," market"," store"]]);
new Thing("medieval butcher shop",["medieval meat,2-10","medieval food,0-3",".medieval shop"],[["butcher","meat"],[" shop"," market"," store"]]);
new Thing("medieval food shop",["sack of grain,1-6","sack of medieval food,1-6","medieval food,2-5","medieval meat,1-4",".medieval shop"],[["baker's","ingredients","groceries","farmer's","cook's"],[" shop"," market"," store"]]);
new Thing("medieval apothecary shop",["potion,1-8","unusual stone,1-8","unusual plant,1-8","unusual ingredient,0-4","wizard,20%",".medieval shop"],["rare ingredients shop","potion shop","cures and remedies","alchemy essenitals","unusual wares shop","apothecary"]);
new Thing("medieval inn",["medieval innkeeper,1-2","medieval peasant,0-3","medieval guard,0-3","medieval noble,50%","medieval bedroom,2-6","tankard,1-4","ale keg,1-4","medieval table,1-3","medieval chair,2-4","medieval chest,0-2","medieval clutter,1-3",".medieval building"],[["inn of the ","tavern of the "],
["bleeding","smoking","witching","flying","burning","rabid","winking","dead","standing","tasty","meaty","fat","thirsty","hungry","starving","lone","cheerful","singing","dancing","travelling","lost","haunted","cursed","holy","magic","sorcerous","shy","fair","tipsy","drunk","sleeping","snoring","screaming","moaning","iron","resting","sulking","hidden","raving","prancing","filthy","nested","squealing"],[" "],
["walrus","king","queen","princess","prince","bear","witch","wizard","mage","barbarian","shark","dog","cat","castle","fish","rabbit","bull","spider","cake","potion","wanderer","traveller","tree","fairy","pixie","unicorn","dragon","mandrake","tankard","bottle","cobbler","blacksmith","jester","nettle","cookpot","anvil","scholar","monk","idiot","raven","squire","skeleton","beggar","gembaby","pig"]]);
new Thing("wizard tower",["wizard,95%","wizard,20%","medieval servant,30%","unusual ingredient,1-4","medieval table,80%","medieval chair,1-3","medieval chest,1-4","medieval clutter,2-4",".medieval building"]);
new Thing("medieval cemetery",["medieval gravedigger,0-2","medieval person,0-3","medieval grave,10-30","ghost,20%","ghost,10%"],"graveyard");
new Thing("medieval grave",["medieval corpse,98%","ghost,2%","worm,0-3","insect,0-1","Rock","dirt"],"grave");


new Thing("medieval chair",["wood","nails,50%"],"chair");
new Thing("medieval bench",["stone"],"bench");
new Thing("tankard",["ale,20%","metal"]);
new Thing("ale keg",["ale,80%","wood","metal"]);
new Thing("medieval altar",["potion,0-3","unusual stone,0-2","unusual ingredient,0-1",["marble","stone"]],"altar");
new Thing("ale",["Alcohol"]);
new Thing("loom",["wood frame","metal"],"loom");
new Thing("throne",["Сloth","wood","metal"]);
new Thing("medieval table",["wood","nails,50%"],"table");
new Thing("medieval bed",["wood frame","Сloth","pillow,0-3"],"bed");
new Thing("medieval chest",[".medieval chest content","wood frame","metal"],["coffer","chest","strongbox"]);
new Thing("medieval chest content",["medieval clutter,0-2",["medieval clutter,0-5","unusual stone,0-2","unusual plant,0-5","unusual ingredient,0-2","potion,0-5","sack of grain,0-3","sack of medieval food,0-3","medieval food,0-5","medieval meat,0-6","treasure,0-2"],"insect,10%","insect,10%"],["chest content"]);
new Thing("medieval clutter",[["metal","wood"]],["spoon","fork","knife","torch","broom","pot","jug","candlestick","goblet","flagon","plate","platter","bowl","ladle","clothes iron","figurine","hammer","tongs","bellows","spigot","axe","pickaxe","saw","hoe","shovel","quill","calipers","oar","paint brush","pitchfork","shears","weight"]);
new Thing("anvil",["Steel"]);
new Thing("unusual stone",["Rock"],["crystal","bezoar","agate","amber","amethyst","bloodstone","carnelian","garnet","hematite","jade","jasper","lapis","moonstone","obsidian","opal","sapphire","tiger's eye","turquoise","zircon"]);
new Thing("unusual ingredient",["OrganicMatter"],["dragon tooth","dragon claw","dragon scale","unicorn horn","goblin mucus","giant snail shell","troll blood clot","imp nose","fairy fingers","pixie wings","demon tail","behemoth plate","mindsucker lips","slime porridge","ladyfly ocella","spider silk","gold cocoon","silver chrysalis","oaf bladder","angel larva","sugarfey fudge","whale blubber","mummified gembaby","basilisk feather","mage fingernails","screamfiber","brainpod","footface nipple","cephalite eyelashes"]);
new Thing("unusual plant",["plant cell"],["mandrake","myrrh","vervain","lotus","pomegranate","myrtle","blackroot","silkbean","drypod","pigweed","thistle","marigold","mistletoe","spearmint","mugwort","aconite","aloe","amaranth","anise","belladonna","bergamot","bladderwrack","cloves","clover","comphrey","dragonblood","eucalyptus","incense","garlic","ginger","ginseng","hemlock","holly","honeysuckle","licorice","jasmine","juniper","nutmeg","oakmoss","orchid","rue","saffron","sage","vetivert","wormwood","witchgrass","agaric","bolete"]);//http://www.janih.com/lady/herbs/magick/
new Thing("potion",["OrganicMatter","Water",["glass bottle","glass jar"]],[["stamina","health","beauty","endurance","strength","energy","lover's","blacksmith's","cook's","queen's","growth","witch's","hunter's","brawler's","knight's","cobbler's","clarity","perception","nimbleness","quickness","squire's","unicorn's","bear's","shark's","moon's","lady's","soldier's","wizard's","rest","sleep","paralysis","stone","shimmer","oil","eloquence","speech","bird's","vapor","void"],[" "],["poultice","salve","potion","elixir","poison","philter","draught","brew","remedy","balm","infusion","tincture","decoction","ointment","cordial","tonic"]]);
new Thing("pile of treasure",["treasure,1-4","gold coin,5-20"]);
new Thing(
    "treasure",
    ["unusual stone,20%","Gold"],
    [
        ["golden","gemmed","ornate","magic","cursed","blessed","enchanted","ancestral","holy","royal","diamond"],
        [" "],
        [
            "goblet","cup","ring","necklace","medallion","locket","sword","mirror","shield","crown","trinket","scepter",
            "tiara","casket","helm","figurine","egg","knife","arrow","wand"
        ]
    ]
);

new Thing("medieval farm",["medieval house,1-3","medieval peasant,1-4","field,1-8","sack of grain,0-8","dog,50%","cat,10%","horse,30%","horse,30%","horse,30%","poultry,0-3"],"farm");
new Thing("sack of grain",["grain","Сloth","worm,5%","worm,5%"],[["sack of "],["oats","wheat","corn","barley","ruined grain","rice","soy beans","rye"]]);
new Thing("sack of medieval food",["OrganicMatter","Сloth","worm,5%","worm,5%"],[["sack of "],["tomatoes","potatoes","apples","peanuts","raisins","leeks","dead mice"]]);
new Thing("medieval food",["OrganicMatter","worm,5%"],["tomato","potato","apple","corn cob","roasted leeks","cheese wheel","bread loaf","meat pie","apple pie","peanut pie","fish pie","corn pie","mice pie","sludge pie","honey cake","butter cake","rabbit stew"]);
new Thing("medieval meat",["soft flesh"],[["cured ","prepared ","salted ","smoked ","breaded ","roasted "],["beef","pork","mutton","veal","horse","fish","ham","rabbit","pheasant","chicken","clams","bear"]]);
"""
