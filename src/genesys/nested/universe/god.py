from models.v5 import universe
from factories.thing.nested_factory import NestedFactory as Factory
from ..cloth import ClothingSetFactory
from ..life import BodyFactory
from ..temporary import ComputerFactory


class D2emonThoughtsFactory(Factory):
    default_model = universe.GodThoughts
    thoughts = [
        "OH MY GOD WHAT ARE YOU DOING HERE TURN BACK IMMEDIATELY", "WHAT IS WRONG WITH YOU", "WHAT THE HELL GO AWAY",
        "WHAT ARE YOU DOING OH GOD", "WHY THE HELL ARE YOU HERE", "I DO WHAT I WANT OKAY", "NO I DON'T CARE GO AWAY",
        "WHAT DID I EVEN DO TO YOU", "OH NO WHY THIS",
        "OKAY JUST <a href=\"http://orteil.deviantart.com\">GO THERE ALREADY</a>",
        "<a href=\"http://twitter.com/orteil42\">WHATEVER</a>"
    ]

    def generate_name(self):
        return self.select_item(*self.thoughts)


class D2emonPsycheFactory(Factory):
    default_model = universe.GodPsyche

    def children(self):
        yield D2emonThoughtsFactory()


class D2emonFactory(Factory):
    default_model = universe.God
    default_name = 'D2emon'

    def children(self):
        yield BodyFactory()
        yield D2emonPsycheFactory()
        yield ClothingSetFactory()
        yield ComputerFactory()


class GodFactory(D2emonFactory):
    pass
