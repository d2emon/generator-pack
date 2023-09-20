from factories.thing.nested_factory import NestedFactory
from models.v5 import universe
from utils.nested import select_item
from ..cloth import ClothingSetFactory
from ..life import BodyFactory
from ..temporary import ComputerFactory


class D2emonThoughtsFactory(Factory):
    # TODO: Refactor it
    default_model = universe.GodThoughts
    thoughts = [
        "OH MY GOD WHAT ARE YOU DOING HERE TURN BACK IMMEDIATELY", "WHAT IS WRONG WITH YOU", "WHAT THE HELL GO AWAY",
        "WHAT ARE YOU DOING OH GOD", "WHY THE HELL ARE YOU HERE", "I DO WHAT I WANT OKAY", "NO I DON'T CARE GO AWAY",
        "WHAT DID I EVEN DO TO YOU", "OH NO WHY THIS",
        "OKAY JUST <a href=\"http://orteil.deviantart.com\">GO THERE ALREADY</a>",
        "<a href=\"http://twitter.com/orteil42\">WHATEVER</a>"
    ]

    def generate_name(self):
        return select_item(*self.thoughts)


class D2emonPsycheFactory(Factory):
    # TODO: Refactor it
    default_model = universe.GodPsyche

    def children(self):
        yield D2emonThoughtsFactory()


class D2emonFactory(NestedFactory):
    default_name = 'D2emon'
    model = universe.God

    def children(self):
        yield BodyFactory.one()
        yield D2emonPsycheFactory.one()
        yield ClothingSetFactory.one()
        yield ComputerFactory.one()


class GodFactory(D2emonFactory):
    # TODO: Refactor it
    pass
