from generator_log import setup
from show_multiple import build_from_factories
from genesys.world import WorldFactory


DEBUG = True
COUNT = 10


def build_all():
    factories = [
        WorldFactory,
    ]
    build_from_factories(factories, COUNT)


if __name__ == "__main__":
    if DEBUG:
        setup()
    build_all()
