from generator.album import AlbumGenerator
from generator.band import BandGenerator
from generator.battlecry import BattleCryGenerator
from generator.motivation import MotivationGenerator
from generator.concept import ArtConceptBeingGenerator, ArtConceptPlaceGenerator, ArtConceptGenerator, StoryConceptCharacterGenerator, StoryConceptEventGenerator, StoryConceptGenerator
from generator.demonym import DemonymGenerator, Demonym
from generator.haiku import HaikuGenerator
from generator.idiom import IdiomGenerator
from generator.motto import MottoGenerator
from generator.prayer import ForgivePrayerGenerator, AidPrayerGenerator, PrayerGenerator
from generator.riddle import RiddleGenerator
from generator.schoolSubject import SchoolSubjectGenerator
from generator.slogan import SloganGenerator
from generator.swear import SwearGenerator
from generator.wisdom import WisdomQuoteGenerator
from generator.world import WorldGenerator
from generator.race import RandomRaceGenerator

from generator.space.galaxy import GalaxyGenerator
from generator.space.star import StarGenerator
from generator.space.planet import PlanetGenerator

from generator.generator.markov import MarkovChain, MarkovGenerator

from fixtures.streets import streets

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


def print_result(data=[], title=None):
    print("=" * 80)
    if title is not None:
        print(title)
        print("-" * 80)
    for i, item in enumerate(data):
        print("{}:\n----\n{}\n----\n{}".format(
            i + 1,
            repr(item),
            item
        ))
        print('-' * 80)
        print(item.description)
        print("-" * 80)
    print("=" * 80)


def run_generator(name='', count=1, *args, **kwargs):
    try:
        count = int(count)
    except:
        count = 1
    print(name, count, args, kwargs)

    if name == 'street':
        data = [markov_street(streets, 64) for i in range(count)]
        print_result(data, ('Street', args, kwargs))
        return
    if name == 'lugansk':
        data = [Demonym('Lugansk') for i in range(count)]
        print_result(data, 'Lugansk')
        return
    if name == 'all':
        for name, g in generators.items():
            print(name)
            data = [g.generate() for i in range(count)]
            print_result(data, name)
        return

    g = generators.get(name)
    if g is None:
        print_result(generators.keys())
        return

    data = [g.generate(*args, **kwargs) for i in range(count)]
    print(args, kwargs)
    print_result(data, name)
