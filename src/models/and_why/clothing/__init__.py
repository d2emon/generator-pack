from .clothing import Clothing
from .. import slots


class Accessory(Clothing):
    slots = slots.IN_HAND,


class Weapon(Clothing):
    slots = slots.IN_HAND,


class Shield(Clothing):
    slots = slots.SHIELD,


class Headdress(Clothing):
    slots = slots.HEAD,


class Collar(Clothing):
    slots = slots.NECK,


class Shendyt(Clothing):
    slots = slots.HIPS,


class Kalasiris(Clothing):
    slots = slots.TORSO, slots.HIPS,
