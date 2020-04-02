from ....unknown import Bacteria, Keratin
from genesys.nested.models import Model
from ..skin import Dandruff
from .... import lookups


class Hair(Model):
    bacterias = Model.child_property(Bacteria)
    keratin = Model.child_property(Keratin)

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Bacteria.probable(30)
            yield Keratin


class HeadHair(Hair):
    class BaseFactory(Model.BaseFactory):
        default = lookups.hair

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Dandruff
            yield from super().children_classes()
