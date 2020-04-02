"""
Cloth stuff
"""
from nestedg.data import unknown, materials
from nestedg.model import Model
from genesys.nested.data.biology.body.body import DeadSkin, Sweat, Keratin, SkinCell


class Leather(Model):
    @classmethod
    def children_classes(cls):
        yield SkinCell


class TextileFibre(Model):
    @classmethod
    def children_classes(cls):
        yield Keratin

    @classmethod
    def _generate_name(cls):
        return 'textile fibres'


class Textile(Model):
    @classmethod
    def children_classes(cls):
        yield TextileFibre


class Cloth(Model):
    @classmethod
    def children_classes(cls):
        yield Textile


class Pocket(Model):
    @classmethod
    def children_classes(cls):
        yield unknown.Dust.probable(20)
        yield unknown.Crumbs.probable(20)
        yield unknown.Lint.probable(30)
        yield unknown.Donut.probable(1)
        yield unknown.Coin.probable(20)
        yield unknown.Coin.probable(20)
        yield unknown.Coin.probable(10)
        yield unknown.Pen.probable(10)
        yield unknown.Pen.probable(2)
        yield unknown.Button.probable(10)
        yield unknown.Button.probable(5)
        yield unknown.Button.probable(1)
        yield unknown.Note.probable(15)
        yield unknown.Note.probable(5)
        yield unknown.Handgun.probable(0.4)
        yield unknown.Pasta.probable(0.2)
        yield Textile


class Clothing(Model):
    @classmethod
    def children_classes(cls):
        yield Textile
        yield DeadSkin.probable(40)
        yield Sweat.probable(15)


class Glasses(Clothing):
    glass_types = ['glasses', 'glasses', 'glasses', 'sunglasses', 'monocle', 'ski mask']

    @classmethod
    def children_classes(cls):
        yield materials.Plastic
        yield unknown.Glass
        yield unknown.Metal.probable(10)

    @classmethod
    def _generate_name(cls):
        return cls.choice(cls.glass_types)


class Hat(Clothing):
    hat_types = ['cap', 'hat', 'hat', 'hat', 'hat', 'beret', 'party hat', 'top-hat']

    @classmethod
    def _generate_name(cls):
        return cls.choice(cls.hat_types)


class Shoes(Clothing):
    shoes_types = ['shoes', 'boots', 'sneakers', 'sandals']

    @classmethod
    def children_classes(cls):
        yield Leather.probable(40)
        yield materials.Plastic

    @classmethod
    def _generate_name(cls):
        return cls.choice(cls.shoes_types)


class Socks(Clothing):
    pass


class CozyVonPocketworth(Clothing):
    @classmethod
    def children_classes(cls):
        yield Pocket.multiple(20, 40)
        yield from super().children_classes()
        yield Leather.probable(30)

    @classmethod
    def _generate_name(cls):
        return 'Cozy von Pocketworth'


class Coat(Clothing):
    coat_types = ['coat', 'jacket', 'hoodie']

    @classmethod
    def children_classes(cls):
        yield Pocket.multiple(0, 4)
        yield from super().children_classes()
        yield Leather.probable(30)

    @classmethod
    def _generate_name(cls):
        return cls.choice(cls.coat_types)


class Underwear(Clothing):
    pass


class Shirt(Clothing):
    shirt_types = ['shirt', 'sweater', 't-shirt']

    @classmethod
    def _generate_name(cls):
        return cls.choice(cls.shirt_types)


class Pants(Clothing):
    pants_types = ['pants', 'trousers', 'sweatpants', 'bermuda shorts', 'shorts', 'jeans', 'cargo pants']

    @classmethod
    def children_classes(cls):
        yield Pocket.multiple(0, 4)
        yield from super().children_classes()

    @classmethod
    def _generate_name(cls):
        return cls.choice(cls.pants_types)
