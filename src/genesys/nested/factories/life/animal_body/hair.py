from generated import life
from ...factory import Factory
from ...materials import KeratinFactory


class HairFactory(Factory):
    default_model = life.Hair

    def children(self):
        # yield Bacteria.probable(30)
        yield KeratinFactory()


class FurFactory(HairFactory):
    default_model = life.Fur

    def children(self):
        yield KeratinFactory()


class WhiskersFactory(FurFactory):
    default_model = life.Whiskers
