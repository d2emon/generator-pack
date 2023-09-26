from .matter import Matter


class Mineral(Matter):
    pass


class Rock(Mineral):
    state = Matter.SOLID


class Carbon(Rock):
    pass


class Diamond(Rock):
    pass


class Magma(Rock):
    state = Rock.LIQUID


class Silica(Mineral):
    pass


class Salt(Mineral):
    pass
