import logging
from generator_log import setup
from genesys.nested.universe import MultiverseFactory


if __name__ == "__main__":
    setup()

    multiverse_factory = MultiverseFactory()
    logging.debug(multiverse_factory)

    multiverse = multiverse_factory()
    logging.debug(multiverse)
