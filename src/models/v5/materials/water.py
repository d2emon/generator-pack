"""
- Water
- WaterState
- Steam
- Dew
- Ice
- Snowflakes
- Snow
"""
from models.nested_model import Model
from .matter import Matter


class Water(Matter):
    state = Matter.LIQUID


class Steam(Water):
    state = Matter.GAS


class Dew(Water):
    state = Matter.LIQUID


class Ice(Water):
    state = Matter.SOLID


class Snowflakes(Water):
    state = Matter.SOLID


class Snow(Model):
    flakes = Model.child_property(Snowflakes)
