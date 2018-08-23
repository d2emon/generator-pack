from .generator import *

from .album import AlbumGenerator
from .band import BandGenerator
from .battlecry import BattleCryGenerator
from .motivation import MotivationGenerator
from .concept import ArtConceptBeingGenerator, ArtConceptPlaceGenerator, ArtConceptGenerator, StoryConceptCharacterGenerator, StoryConceptEventGenerator, StoryConceptGenerator
from .demonym import DemonymGenerator, Demonym
from .haiku import HaikuGenerator
from .idiom import IdiomGenerator
from .motto import MottoGenerator
from .prayer import ForgivePrayerGenerator, AidPrayerGenerator, PrayerGenerator
from .riddle import RiddleGenerator
from .schoolSubject import SchoolSubjectGenerator
from .slogan import SloganGenerator
from .swear import SwearGenerator
from .wisdom import WisdomQuoteGenerator
from .world import WorldGenerator
from .race import RandomRaceGenerator

from .space.galaxy import GalaxyGenerator
from .space.star import StarGenerator
from .space.planet import PlanetGenerator

from .generator.markov import MarkovChain

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
