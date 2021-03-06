from .body import Chest, Thighs, Legs, Feet


class Clothing:
    def __init__(self, name, color=None):
        self.name = name
        self.color = color
        self.order = None
        self.parts = set([])

    @property
    def is_underwear(self):
        return self.order == 0

    def __str__(self):
        if not self.color:
            return self.name
        return "{} {}".format(self.color, self.name).title()


class Underwear(Clothing):
    def __init__(self, name, color=None):
        super().__init__(name, color)
        self.order = 0


class Bra(Underwear):
    def __init__(self, name, color=None):
        super().__init__(name, color)
        self.order = 0
        self.parts = {Chest, }


class Panties(Underwear):
    def __init__(self, name, color=None):
        super().__init__(name, color)
        self.order = 0
        self.parts = {Thighs, }


class UpClothing(Clothing):
    def __init__(self, name, color=None):
        super().__init__(name, color)
        self.order = 10
        self.parts = {Chest, }


class Jacket(UpClothing):
    def __init__(self, name, color=None):
        super().__init__(name, color)
        self.order = 20


class Coat(Jacket):
    def __init__(self, name, color=None):
        super().__init__(name, color)
        self.parts = {Chest, Thighs, }


class DownClothing(Clothing):
    def __init__(self, name, color=None):
        super().__init__(name, color)
        self.order = 10
        self.parts = {Thighs, Legs, }


class Stockings(Clothing):
    def __init__(self, name, color=None):
        super().__init__(name, color)
        self.order = 5
        self.parts = {Legs, Feet, }


class Socks(Clothing):
    def __init__(self, name, color=None):
        super().__init__(name, color)
        self.order = 5
        self.parts = {Feet, }


class Shoes(Clothing):
    def __init__(self, name, color=None):
        super().__init__(name, color)
        self.order = 10
        self.parts = {Feet, }


class Boots(Clothing):
    def __init__(self, name, color=None):
        super().__init__(name, color)
        self.order = 10
        self.parts = {Feet, }


class Blouse(UpClothing):
    pass


class Chemise(UpClothing):
    pass


class TShirt(UpClothing):
    pass


class Sweater(UpClothing):
    pass


class Skirt(DownClothing):
    def __init__(self, name, color=None):
        super().__init__(name, color)
        self.order = 10
        self.parts = {Thighs, }


class Trousers(DownClothing):
    pass


class Jeans(Trousers):
    pass
