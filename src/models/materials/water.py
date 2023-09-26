"""
- Water
- WaterState
- Steam
- Dew
- Ice
- Snowflakes
- Snow
"""
from models.nested_model import NestedModel
from .matter import Matter, Gas


class Water(Matter):
    state = Matter.LIQUID


class Steam(Gas):
    state = Matter.GAS


class Dew(Water):
    state = Matter.LIQUID


class Ice(Water):
    state = Matter.SOLID


class Snowflakes(Water):
    state = Matter.SOLID


class Snow(NestedModel):
    flakes = NestedModel.child_property(Snowflakes)
