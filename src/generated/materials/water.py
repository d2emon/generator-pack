"""
- Water
- WaterState
- Steam
- Dew
- Ice
- Snowflakes
- Snow
"""
from genesys.model.model import Model
from .matter import Gas, Matter


class Water(Matter):
    state = Matter.LIQUID


class WaterState(Model):
    state = Matter.LIQUID

    water = Model.child_property(Water)


class Steam(WaterState, Gas):
    state = Matter.GAS


class Dew(WaterState):
    state = Matter.LIQUID


class Ice(WaterState):
    state = Matter.SOLID


class Snowflakes(WaterState):
    state = Matter.SOLID


class Snow(Model):
    flakes = Model.child_property(Snowflakes)
