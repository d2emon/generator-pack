#! /usr/bin/python
import sys
from generator import album, band, battlecry, motivation
from generator.concept import ArtConceptGenerator, StoryConceptGenerator


def main(args):
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

    print("Battlecry")
    print("-" * 80)
    for i in range(10):
        print(battlecry.BattleCryGenerator.generate())
    print("-" * 80)

    print("Character goal")
    print("-" * 80)
    for i in range(10):
        print(motivation.MotivationGenerator.generate())
    print("-" * 80)

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


if __name__ == "__main__":
    main(sys.argv[1:])
