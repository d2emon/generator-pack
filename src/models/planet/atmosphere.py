from models.materials.matter import Matter
from models.v5.life import Life


class Atmosphere(Matter):
    default_name = 'atmosphere'
    state = Matter.GAS
    life = Matter.child_property(Life)
