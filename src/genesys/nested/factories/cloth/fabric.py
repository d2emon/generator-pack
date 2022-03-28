from generated import cloth
from factories.nested_factory import NestedFactory as Factory
from ..materials import KeratinFactory


class TextileFibreFactory(Factory):
    default_model = cloth.TextileFibre

    def children(self):
        yield KeratinFactory()


class TextileFactory(Factory):
    default_model = cloth.Textile

    def children(self):
        yield TextileFibreFactory()


class ClothFactory(Factory):
    default_model = cloth.Cloth

    def children(self):
        yield TextileFactory()


class LeatherFactory(Factory):
    default_model = cloth.Leather

    def children(self):
        from genesys.nested.factories.life.animal_body.skin import SkinCellFactory

        yield SkinCellFactory()
