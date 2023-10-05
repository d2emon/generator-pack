import logging
from generator_log import setup
from genesys.nested.universe import MultiverseFactory


def log_item(item):
    logging.debug('='*80)
    logging.debug('Item: %s', item)
    logging.debug('Parent: %s', item.parent)
    logging.debug('Data: %s', item.data)


if __name__ == "__main__":
    setup()

    multiverse_factory = MultiverseFactory()
    logging.debug(multiverse_factory)

    multiverse = multiverse_factory()
    log_item(multiverse)
    logging.debug('Universes: %s', multiverse.universes)

    universe = multiverse.universes[0]
    log_item(multiverse)
    logging.debug('Superclusters: %s', universe.superclusters)

    supercluster = universe.superclusters[0]
    log_item(supercluster)
    logging.debug('Galaxies: %s', supercluster.galaxies)
