import random


IN_HAND = 1
SHIELD = 2
HEAD = 3
NECK = 4
TORSO = 5
HIPS = 6


class Clothing:
    slots = ()

    def __init__(self, name):
        self.name = name


class Accessory(Clothing):
    slots = IN_HAND,


class Weapon(Clothing):
    slots = IN_HAND,


class Shield(Clothing):
    slots = SHIELD,


class Headdress(Clothing):
    slots = HEAD,


class Collar(Clothing):
    slots = NECK,


class Shendyt(Clothing):
    slots = HIPS,


class Kalasiris(Clothing):
    slots = TORSO, HIPS,


female = [
    Accessory('Чаша'),
    Accessory('Веер'),
    Headdress('Головной убор'),
    Headdress('Парик'),
    Collar('Воротник'),
    Collar('Воротник'),
    Shendyt('Схенти'),
    Shendyt('Схенти с юбкой'),
    Kalasiris('Калазирис'),
]


male = [
    Weapon('Копье'),
    Weapon('Секира'),
    Weapon('Бронзовый меч'),
    Weapon('Бронзовый кинжал'),
    Weapon('Меч'),
    Headdress('Шлем'),
    Headdress('Шлем'),
    Headdress('Парик'),
    Collar('Воротник'),
    Collar('Воротник'),
    Shendyt('Схенти'),
    Shield('Щит'),
]


class Doll:
    def __init__(self):
        self.slots = {}

    def __release(self, slot):
        item = self.slots.get(slot)
        if item is None:
            return
        self.take_off(item)

    def take_off(self, item):
        print("Takes off {}".format(item.name))
        for slot in item.slots:
            self.slots[slot] = None

    def put_on(self, item):
        for slot in item.slots:
            self.__release(slot)
        print("Puts on {}".format(item.name))
        for slot in item.slots:
            self.slots[slot] = item

    def fill(self, items):
        slots = (
            IN_HAND,
            SHIELD,
            HEAD,
            NECK,
            TORSO,
            HIPS,
        )
        for slot in slots:
            for_slot = [i for i in items if slot in i.slots]
            if len(for_slot) and random.randrange(100) < 75:
                self.put_on(random.choice(for_slot))
