"""
- Salt
- Silica
- Rock
- Diamond
- Magma
- Iron
"""
from .matter import Matter, Molecule


class Salt(Matter):
    pass


class Silica(Molecule):
    pass


class Rock(Matter):
    pass


class Diamond(Rock):
    pass


class Magma(Rock):
    pass


class Carbon(Rock):
    pass


class Iron(Rock):
    pass
