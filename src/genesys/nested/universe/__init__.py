"""
Universe stuff
"""
from genesys.nested.factories.nested_factory import NestedFactory
from models.universe import Supercluster, Universe, Multiverse
from utils.nested import select_item
from .galaxy import GalaxyFactory

# from .orbit import OrbitFactory, PlanetOrbitFactory, BarrenOrbitFactory, VisitorOrbitFactory, FutureOrbitFactory, \
#     TerraformedOrbitFactory, MedievalOrbitFactory, AncientOrbitFactory, GasGiantFactory, AsteroidBeltFactory, \
#     EarthFactory
# from .planet import *
# from .atmosphere import AtmosphereFactory, GasGiantAtmosphereFactory
# from .black_hole import EndOfUniverseNoteFactory, EverythingFactory, Answer42Factory, WhiteHoleFactory, \
#     InsideTheBlackHoleFactory, BlackHoleFactory
# from .god import D2emonThoughtsFactory, D2emonPsycheFactory, D2emonFactory, GodFactory


# Multiverse
# Universe
# Supercluster
# Galaxy factories in .galaxy
# Nebula factories in .nebula
# Star factories in .star
# Planet factories in .planet


class MultiverseFactory(NestedFactory):
    default_model = Multiverse

    def contents(self):
        yield UniverseFactory.multiple(10, 30)

    def name_factory(self, provider, *args, **kwargs):
        return select_item(*provider.multiverse)


class UniverseFactory(NestedFactory):
    default_model = Universe

    def contents(self):
        yield SuperclusterFactory.multiple(10, 30)


class SuperclusterFactory(NestedFactory):
    default_model = Supercluster
    deault_name = "galactic supercluster"

    def contents(self):
        yield GalaxyFactory.multiple(10, 30)


"""
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
