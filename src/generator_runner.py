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


streets = [
    "Оборонная",
    "Советская",
    "Бетховена",
    "Щербакова",
    "Студенческая",
    "Качалова",
    "Баумана",
    "Комбайная",
    "Фестивальная",
    "Ватутина",
    "Буденного",
    "Жданова",
    "Феликса",
    "Учебная",
    "Тухачевского",
    "30 лет Победы",
    "Якира",
    "Молодежная",
    "Дружбы",
    "50 лет Октября",
    "Дзержинского",
    "60 лет образования СССР",
    "Гагарина",
    "Солнечная",
    "Жукова",
    "Левченко",
    "Комарова",
    "Волкова",
    "Газеты Луганская Правда",
    "Оборонная",
    "Победоносная",
    "Насосная",
    "Карла Маркса",
    "Карла Либкнехта",
    "Пролетариата Донбасса",
    "Краснознаменная",
    "Яблочная",
    "Вишневая",
    "Грушевая",
    "Сосновая",
    "Заречная",
    "А. Линева",
    "Красноармейская",
    "Красная",
    "Белая",
    "Зеленая",
]


def markov_street(data, length=32):
    g = MarkovChain(data_list=data, length=3).generator()
    return "ул. {}".format(g.generate(length))


def print_result(data=[], title=None):
    print("=" * 80)
    if title is not None:
        print(title)
        print("-" * 80)
    for i, item in enumerate(data):
        print("{}:\t{}".format(
            i + 1,
            item
        ))
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

    # print("Art concept (being)")
    # print(ArtConceptGenerator.generate(being=True))
    # print("Art concept (place)")
    # print(ArtConceptGenerator.generate(being=False))

    # print("Story concept (event)")
    # print(StoryConceptGenerator.generate(character=False))
    # print("Story concept (character)")
    # print(StoryConceptGenerator.generate(character=True))

    # print(d, "%s from %s" % (d.demonym, d.base))
    # print(makeDemonym("Lugansk"))

    # print("Prayer (aid)")
    # print(PrayerGenerator.generate(forgive=False))
    # print("Prayer (forgiveness)")
    # print(PrayerGenerator.generate(forgive=True))
