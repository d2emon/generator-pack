from .clothing import Clothing


class Accessory(Clothing):
    slots = Clothing.Slots.IN_HAND,


class Weapon(Clothing):
    slots = Clothing.Slots.IN_HAND,


class Shield(Clothing):
    slots = Clothing.Slots.SHIELD,


class Headdress(Clothing):
    slots = Clothing.Slots.HEAD,


class Collar(Clothing):
    slots = Clothing.Slots.NECK,


class Shendyt(Clothing):
    slots = Clothing.Slots.HIPS,


class Kalasiris(Clothing):
    slots = Clothing.Slots.TORSO, Clothing.Slots.HIPS,
