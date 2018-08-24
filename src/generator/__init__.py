from .generator import *
from .generator.markov import MarkovChain

from .name.other.album import AlbumGenerator
from .name.other.band import BandGenerator
from ._unknown.motivation import MotivationGenerator
from ._unknown.world import WorldGenerator
from ._unknown.space import GalaxyGenerator
from ._unknown.space import StarGenerator
from ._unknown.space import PlanetGenerator
from .other.battlecry import BattleCryGenerator
from .other.concept import ArtConceptBeingGenerator, ArtConceptPlaceGenerator, ArtConceptGenerator, StoryConceptCharacterGenerator, StoryConceptEventGenerator, StoryConceptGenerator
from .other.demonym import DemonymGenerator
from .other.haiku import HaikuGenerator
from .other.idiom import IdiomGenerator
from .other.motto import MottoGenerator
from .other.prayer import ForgivePrayerGenerator, AidPrayerGenerator, PrayerGenerator
from .other.riddle import RiddleGenerator
from .other.schoolSubject import SchoolSubjectGenerator
from .other.slogan import SloganGenerator
from .other.swear import SwearGenerator
from .other.wisdom import WisdomQuoteGenerator
from .description.race import RandomRaceGenerator


generators = {
    "album": AlbumGenerator,
    "band": BandGenerator,
    "battlecry": BattleCryGenerator,
    "concept-art-place": ArtConceptPlaceGenerator,
    "concept-art-being": ArtConceptBeingGenerator,
    "concept-art": ArtConceptGenerator,
    "concept-story-character": StoryConceptCharacterGenerator,
    "concept-story-event": StoryConceptEventGenerator,
    "concept-story": StoryConceptGenerator,
    "demonym": DemonymGenerator,
    "motivation": MotivationGenerator,
    "haiku": HaikuGenerator,
    "idiom": IdiomGenerator,
    "motto": MottoGenerator,
    "prayer-forgive": ForgivePrayerGenerator,
    "prayer-aid": AidPrayerGenerator,
    "prayer": PrayerGenerator,
    "riddle": RiddleGenerator,
    "subject": SchoolSubjectGenerator,
    "slogan": SloganGenerator,
    "swear": SwearGenerator,
    "wisdom": WisdomQuoteGenerator,
    "world": WorldGenerator,
    "galaxy": GalaxyGenerator,
    "star": StarGenerator,
    "planet": PlanetGenerator,
    "alien": RandomRaceGenerator,
}


def markov_street(data, length=32):
    g = MarkovChain(data_list=data, length=3).generator()
    return "ул. {}".format(g.generate(length))
