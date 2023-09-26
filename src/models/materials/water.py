from models.nested_model import NestedModel
from .matter import Matter


class Water(Matter):
    state = Matter.LIQUID


class Steam(Water):
    state = Water.GAS


class Dew(Water):
    state = Water.LIQUID


class Ice(Water):
    state = Water.SOLID


class Snowflakes(Water):
    state = Water.SOLID


class Snow(NestedModel):
    flakes = NestedModel.contents_property()
