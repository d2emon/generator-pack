#! /usr/bin/env python
import sys
from generator import album, band
from generator.battlecry import BattleCryGenerator
from generator.motivation import MotivationGenerator
from generator.concept import ArtConceptGenerator, StoryConceptGenerator
from generator.demonym import DemonymGenerator, makeDemonym
from generator.haiku import HaikuGenerator
from generator.idiom import IdiomGenerator
from generator.motto import MottoGenerator
from generator.prayer import PrayerGenerator
from generator.riddle import RiddleGenerator
from generator.schoolSubject import SchoolSubjectGenerator
from generator.slogan import SloganGenerator
from generator.swear import SwearGenerator
from generator.wisdom import WisdomQuoteGenerator

from generator.space.galaxy import GalaxyGenerator
from generator.markov import MarkovChain, MarkovGenerator


def gen_other():
    generators = {
        "Battlecry": BattleCryGenerator,
        "Motivation": MotivationGenerator,
        "Haiku": HaikuGenerator,
        "Idiom": IdiomGenerator,
        "Motto": MottoGenerator,
        "Riddle": RiddleGenerator,
        "SchoolSubject": SchoolSubjectGenerator,
        "Slogan": SloganGenerator,
        "Swear": SwearGenerator,
        "Wisdom quote": WisdomQuoteGenerator,
        "Galaxy": GalaxyGenerator,
    }
    for title, g in generators.items():
        print("=" * 80)
        print("%s:" % (title))
        print("-" * 80)
        for i in range(10):
            print(g.generate())
    print("=" * 80)

    print("Art concept (being)")
    print("-" * 80)
    for i in range(10):
        print(ArtConceptGenerator.generate(being=True))
    print("-" * 80)
    print("Art concept (place)")
    print("-" * 80)
    for i in range(10):
        print(ArtConceptGenerator.generate(being=False))
    print("-" * 80)

    print("Story concept (event)")
    print("-" * 80)
    for i in range(10):
        print(StoryConceptGenerator.generate(character=False))
    print("-" * 80)
    print("Story concept (character)")
    print("-" * 80)
    for i in range(10):
        print(StoryConceptGenerator.generate(character=True))
    print("-" * 80)

    print("Demonymes")
    print("-" * 80)
    for i in range(10):
        d = DemonymGenerator.generate()
        print(d, "%s from %s" % (d.demonym, d.base))
        print(makeDemonym("Lugansk"))
    print("-" * 80)

    print("Prayer (aid)")
    print("-" * 80)
    for i in range(5):
        print(PrayerGenerator.generate(forgive=False))
    print("-" * 80)
    print("Prayer (forgiveness)")
    print("-" * 80)
    for i in range(10):
        print(PrayerGenerator.generate(forgive=True))
    print("-" * 80)

    street_mc = MarkovChain(data_list=[
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
    ], length=3)
    street_mg = MarkovGenerator(street_mc)
    print("ул. %s" % (street_mg.generate_chain(32)))


def gen_all(args):
    print("Hello!")
    print("args:", args)

    print("Albums")
    print("-" * 80)
    for i in range(10):
        print(album.AlbumGenerator.generate())
    print("-" * 80)

    print("Bands")
    print("-" * 80)
    for i in range(10):
        print(band.BandGenerator.generate())
    print("-" * 80)

    gen_other()


if __name__ == "__main__":
    gen_all(sys.argv[1:])
