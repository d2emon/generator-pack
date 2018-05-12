#! /usr/bin/env python
from game_menu import show_menu
from media import simulate
from test_all import gen_all
from run_chainmail import play

import sys


def main(args):
    print(args)
    if 'menu' in args:
        show_menu()
    if 'media' in args:
        simulate(args)
    if 'all' in args:
        gen_all(args)
    if 'chainmail' in args:
        play(args)


if __name__ == "__main__":
    main(sys.argv)
