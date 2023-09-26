from ..materials.matter import Gas, Matter


class Mineral(Matter):
    pass


class Oil(Mineral):
    pass


class Rock(Mineral):
    pass


class Carbon(Rock):
    pass


class Diamond(Carbon):
    pass


class Silica(Rock):
    pass


class Salt(Mineral):
    pass


class Magma(Mineral):
    pass


class Ammonia(Gas):
    pass


class Methane(Gas):
    pass
