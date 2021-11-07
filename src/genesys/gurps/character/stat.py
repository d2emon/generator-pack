from .damage import Damage


class Stat:
    name = ''
    cost = 10
    default_value = 10

    def __init__(self, value):
        self.value = value

    @property
    def points(self):
        return (self.value - self.default_value) * self.cost


class ST(Stat):
    name = 'ST'
    cost = 10
    default_value = 10

    @property
    def thrust_damage(self):
        return Damage(1, -2)

    @property
    def swing_damage(self):
        return Damage(1, 0)

    @property
    def bl(self):
        bl = (self.value * self.value) / 5
        return int(bl) if bl >= 10 else bl


class DX(Stat):
    name = 'DX'
    cost = 20
    default_value = 10


class IQ(Stat):
    name = 'IQ'
    cost = 20
    default_value = 10


class HT(Stat):
    name = 'HT'
    cost = 10
    default_value = 10
