from .clothing_set import ClothingSetFactory
from .fabric import ClothFactory, LeatherFactory, TextileFactory, TextileFibreFactory
from ..materials import KeratinFactory, SweatFactory
from .clothing import ClothingFactory, PocketFactory


"""
//cloth stuff

# new Thing("pants",["pocket,0-4",".clothing"],["pants","trousers","sweatpants","bermuda shorts","shorts","jeans","cargo pants"]);
# new Thing("shirt",[".clothing"],["shirt","sweater","t-shirt"]);
# new Thing("underwear",[".clothing"]);
# new Thing("coat",["pocket,0-4",".clothing","leather,30%"],["coat","jacket","hoodie"]);
# new Thing("cozy von pocketworth",["pocket,20-40",".clothing","leather,30%"],["Cozy von Pocketworth"]);//lotsopokkits
# new Thing("socks",[".clothing"]);
# new Thing("shoes",["leather,40%","Plastic"],["shoes","boots","sneakers","sandals"]);//crocs //okay seriously no
# new Thing("hat",[".clothing"],["cap","hat","hat","hat","hat","beret","party hat","top-hat"]);
# new Thing("glasses",["Plastic","glass","metal,10%"],["glasses","glasses","glasses","sunglasses","monocle","ski mask"]);
"""

FACTORIES = {
    'cloth': ClothFactory(),
    'leather': LeatherFactory(),
    'textile': TextileFactory(),
    'textile fibre': TextileFibreFactory(),
    'keratin': KeratinFactory(),
    'sweat': SweatFactory(),
    'clothing': ClothingFactory(),
    'pocket': PocketFactory(),

}
