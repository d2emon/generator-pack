from .matter import Matter


class Fire(Matter):
    state = Matter.GAS


class Ash(Matter):
    state = Matter.SOLID
