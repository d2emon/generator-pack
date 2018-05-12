#! /usr/bin/env python
from game_menu import show_menu
from media import simulate
from run_chainmail import play
from generator_runner import run_generator

import sys


def main(args):
    print(args)
    if 'menu' in args:
        show_menu()
    if 'media' in args:
        simulate(args)
    if 'chainmail' in args:
        play(args)

    if (len(args) > 0) and (args[0] == 'generate'):
        run_generator(*args[1:])


if __name__ == "__main__":
    main(sys.argv[1:])
