from . import dummy
from .. import town
from . import building


class MedievalVillage(town.Village):
    @classmethod
    def children_data(cls):
        yield building.Townwall.probable_factory(20)
        yield building.WatchTower.probable_factory(15)
        yield building.MedievalMonument.probable_factory(50)
        yield building.MedievalResidentialArea.multiple_factory(1, 4)
        yield building.MedievalCommercialArea.multiple_factory(1, 2)
        yield building.MedievalTemple.multiple_factory(0, 2)
        yield dummy.MedievalFarm.multiple_factory(4, 8)
        yield dummy.MedievalCemetery.probable_factory(50)
        yield dummy.WizardTower.probable_factory(5)


class MedievalCapital(town.Capital):
    capital_types = town.Capital.list_factory([
        "stronghold", "fortress", "fort", "hold", "palace", "main city", "citadel",
    ])

    @classmethod
    def generate_name(cls):
        return cls.capital_types.next()

    @classmethod
    def children_data(cls):
        yield building.Castle
        yield building.Townwall
        yield building.MedievalMonument.probable_factory(70)
        yield building.MedievalMonument.probable_factory(20)
        yield building.MedievalResidentialArea.multiple_factory(3, 12)
        yield building.MedievalMageQuarter.probable_factory(50)
        yield building.MedievalMageQuarter.probable_factory(20)
        yield building.MedievalTemple.multiple_factory(1, 3)
        yield building.MedievalCommercialArea.multiple_factory(2, 6)
        yield dummy.MedievalFarm.multiple_factory(2, 6)
        yield dummy.MedievalCemetery


"""
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
new Thing("medieval grave",["medieval corpse,98%","ghost,2%","worm,0-3","insect,0-1","rock","dirt"],"grave");


new Thing("medieval chair",["wood","nails,50%"],"chair");
new Thing("medieval bench",["stone"],"bench");
new Thing("tankard",["ale,20%","metal"]);
new Thing("ale keg",["ale,80%","wood","metal"]);
new Thing("medieval altar",["potion,0-3","unusual stone,0-2","unusual ingredient,0-1",["marble","stone"]],"altar");
new Thing("ale",["alcohol"]);
new Thing("loom",["wood frame","metal"],"loom");
new Thing("throne",["cloth","wood","metal"]);
new Thing("medieval table",["wood","nails,50%"],"table");
new Thing("medieval bed",["wood frame","cloth","pillow,0-3"],"bed");
new Thing("medieval chest",[".medieval chest content","wood frame","metal"],["coffer","chest","strongbox"]);
new Thing("medieval chest content",["medieval clutter,0-2",["medieval clutter,0-5","unusual stone,0-2","unusual plant,0-5","unusual ingredient,0-2","potion,0-5","sack of grain,0-3","sack of medieval food,0-3","medieval food,0-5","medieval meat,0-6","treasure,0-2"],"insect,10%","insect,10%"],["chest content"]);
new Thing("medieval clutter",[["metal","wood"]],["spoon","fork","knife","torch","broom","pot","jug","candlestick","goblet","flagon","plate","platter","bowl","ladle","clothes iron","figurine","hammer","tongs","bellows","spigot","axe","pickaxe","saw","hoe","shovel","quill","calipers","oar","paint brush","pitchfork","shears","weight"]);
new Thing("anvil",["steel"]);
new Thing("unusual stone",["rock"],["crystal","bezoar","agate","amber","amethyst","bloodstone","carnelian","garnet","hematite","jade","jasper","lapis","moonstone","obsidian","opal","sapphire","tiger's eye","turquoise","zircon"]);
new Thing("unusual ingredient",["organic matter"],["dragon tooth","dragon claw","dragon scale","unicorn horn","goblin mucus","giant snail shell","troll blood clot","imp nose","fairy fingers","pixie wings","demon tail","behemoth plate","mindsucker lips","slime porridge","ladyfly ocella","spider silk","gold cocoon","silver chrysalis","oaf bladder","angel larva","sugarfey fudge","whale blubber","mummified gembaby","basilisk feather","mage fingernails","screamfiber","brainpod","footface nipple","cephalite eyelashes"]);
new Thing("unusual plant",["plant cell"],["mandrake","myrrh","vervain","lotus","pomegranate","myrtle","blackroot","silkbean","drypod","pigweed","thistle","marigold","mistletoe","spearmint","mugwort","aconite","aloe","amaranth","anise","belladonna","bergamot","bladderwrack","cloves","clover","comphrey","dragonblood","eucalyptus","incense","garlic","ginger","ginseng","hemlock","holly","honeysuckle","licorice","jasmine","juniper","nutmeg","oakmoss","orchid","rue","saffron","sage","vetivert","wormwood","witchgrass","agaric","bolete"]);//http://www.janih.com/lady/herbs/magick/
new Thing("potion",["organic matter","water",["glass bottle","glass jar"]],[["stamina","health","beauty","endurance","strength","energy","lover's","blacksmith's","cook's","queen's","growth","witch's","hunter's","brawler's","knight's","cobbler's","clarity","perception","nimbleness","quickness","squire's","unicorn's","bear's","shark's","moon's","lady's","soldier's","wizard's","rest","sleep","paralysis","stone","shimmer","oil","eloquence","speech","bird's","vapor","void"],[" "],["poultice","salve","potion","elixir","poison","philter","draught","brew","remedy","balm","infusion","tincture","decoction","ointment","cordial","tonic"]]);
new Thing("pile of treasure",["treasure,1-4","gold coin,5-20"]);
new Thing("treasure",["unusual stone,20%","gold"],[["golden","gemmed","ornate","magic","cursed","blessed","enchanted","ancestral","holy","royal","diamond"],[" "],["goblet","cup","ring","necklace","medallion","locket","sword","mirror","shield","crown","trinket","scepter","tiara","casket","helm","figurine","egg","knife","arrow","wand"]]);

new Thing("medieval farm",["medieval house,1-3","medieval peasant,1-4","field,1-8","sack of grain,0-8","dog,50%","cat,10%","horse,30%","horse,30%","horse,30%","poultry,0-3"],"farm");
new Thing("sack of grain",["grain","cloth","worm,5%","worm,5%"],[["sack of "],["oats","wheat","corn","barley","ruined grain","rice","soy beans","rye"]]);
new Thing("sack of medieval food",["organic matter","cloth","worm,5%","worm,5%"],[["sack of "],["tomatoes","potatoes","apples","peanuts","raisins","leeks","dead mice"]]);
new Thing("medieval food",["organic matter","worm,5%"],["tomato","potato","apple","corn cob","roasted leeks","cheese wheel","bread loaf","meat pie","apple pie","peanut pie","fish pie","corn pie","mice pie","sludge pie","honey cake","butter cake","rabbit stew"]);
new Thing("medieval meat",["soft flesh"],[["cured ","prepared ","salted ","smoked ","breaded ","roasted "],["beef","pork","mutton","veal","horse","fish","ham","rabbit","pheasant","chicken","clams","bear"]]);
"""
