#! /usr/bin/python
import sys
from generator import album, band, battlecry


def main(args):
    print("Hello!")
    print("args:", args)

    print("Albums")
    print("-" * 80)
    for i in range(10):
        print(album.generate())
    print("-" * 80)

    print("Bands")
    print("-" * 80)
    for i in range(10):
        print(band.generate())
    print("-" * 80)

    print("Battlecry")
    print("-" * 80)
    for i in range(10):
        print(battlecry.generate())
    print("-" * 80)

if __name__ == "__main__":
    main(sys.argv[1:])
