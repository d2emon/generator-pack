from genesys.nested.models import Model
from generated.nested_v2.models.biology import SkinCell
from generated.materials.chemistry import Keratin


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
