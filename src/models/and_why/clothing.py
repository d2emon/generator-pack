from . import slots

SLOTS = (
    slots.IN_HAND,
    slots.SHIELD,
    slots.HEAD,
    slots.NECK,
    slots.TORSO,
    slots.HIPS,
)


class Clothing:
    slots = ()

    def __init__(self, name):
        self.name = name


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
