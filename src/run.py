#! /usr/bin/python
import sys
from generator import album


def main(args):
    print("Hello!")
    print("args:", args)

    print("Albums")
    for i in range(10):
        print(album.generate())


if __name__ == "__main__":
    main(sys.argv[1:])
