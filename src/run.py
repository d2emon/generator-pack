#! /usr/bin/env python
from game_menu import show_menu
from media import simulate
from run_chainmail import play
from generator_runner import run_generator
from noise import fill1d, fill2d, fill3d

import sys


def main(args):
    print(args)
    if 'menu' in args:
        show_menu()
    if 'media' in args:
        simulate(args)
    if 'chainmail' in args:
        play(args)
    if 'noise' in args:
        print(
            [(int) (i * 8) for i in fill1d(16)],
            # fill2d(16, 16),
            # fill3d(16, 16, 16),
        )

    if (len(args) > 0) and (args[0] == 'generate'):
        run_generator(*args[1:])


if __name__ == "__main__":
    main(sys.argv[1:])
