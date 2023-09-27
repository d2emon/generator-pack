from models.materials.matter import Matter
from models.v5.life import Life


class PlanetCore(Matter):
    default_name = 'core'
    life = Matter.child_property(Life)
