import logging


FORMAT = '%(asctime)s\t%(name)s:%(levelname)s\t%(message)s'
LEVEL = logging.DEBUG


def setup():
    logging.basicConfig(
        format=FORMAT,
        level=LEVEL,
    )
    
    # logger = logging.getLogger('factory')
    # logger.setLevel(LEVEL)


setup()
