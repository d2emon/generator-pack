from .generator import *

from generator.name.other.album import AlbumGenerator
from generator.name.other.band import BandGenerator
from generator.other.battlecry import BattleCryGenerator
from generator._unknown.motivation import MotivationGenerator
from generator.other.concept import ArtConceptBeingGenerator, ArtConceptPlaceGenerator, ArtConceptGenerator, StoryConceptCharacterGenerator, StoryConceptEventGenerator, StoryConceptGenerator
from generator.other.demonym import DemonymGenerator
from generator.other.haiku import HaikuGenerator
from generator.other.idiom import IdiomGenerator
from generator.other.motto import MottoGenerator
from generator.other.prayer import ForgivePrayerGenerator, AidPrayerGenerator, PrayerGenerator
from generator.other.riddle import RiddleGenerator
from generator.other.schoolSubject import SchoolSubjectGenerator
from generator.other.slogan import SloganGenerator
from generator.other.swear import SwearGenerator
from generator.other.wisdom import WisdomQuoteGenerator
from generator._unknown.world import WorldGenerator
from generator.description.race import RandomRaceGenerator

from generator._unknown.space import GalaxyGenerator
from generator._unknown.space import StarGenerator
from generator._unknown.space import PlanetGenerator

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
