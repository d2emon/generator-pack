"""
- Water
- Dew
- Ice
- Snow
- Snowflakes
"""
from genesys.nested.models import Model
from .matter import Matter


class Water(Matter):
    class Factory(Matter.Factory):
        def children(self):
            yield from Matter.from_atoms('H', 'O')


class WaterState(Model):
    water = Model.child_property(Water)

    class Factory(Model.Factory):
        def children(self):
            yield Water


class Dew(WaterState):
    pass


class Ice(WaterState):
    pass


class Snowflakes(WaterState):
    pass


class Snow(Model):
    flakes = Model.child_property(Snowflakes)

    class Factory(Model.Factory):
        def children(self):
            yield Snowflakes
