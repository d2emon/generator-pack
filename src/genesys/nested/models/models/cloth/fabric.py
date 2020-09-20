from genesys.nested.models import Model
from genesys.nested.models.models.biology import SkinCell
from ..chemistry import Keratin


class TextileFibre(Model):
    class NameFactory(Model.NameFactory):
        default = 'textile fibres'

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Keratin


class Textile(Model):
    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield TextileFibre


class Cloth(Model):
    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Textile


class Leather(Cloth):
    class ChildrenFactory(Cloth.ChildrenFactory):
        def children_classes(self):
            yield SkinCell
