from genesys.nested.models import Model
from ..skin import Dandruff
from ...single_celled import Bacteria
from generated.materials.chemistry import Keratin
from genesys.nested.data import lookups


class Hair(Model):
    bacterias = Model.child_property(Bacteria)
    keratin = Model.child_property(Keratin)

    class Factory(Model.Factory):
        class ChildrenFactory(Model.Factory.ChildrenFactory):
            def builders(self):
                yield Bacteria.probable(30)
                yield Keratin


class HeadHair(Hair):
    class Factory(Hair.Factory):
        class BaseFactory(Hair.Factory.BaseFactory):
            default = lookups.hair

        class ChildrenFactory(Hair.Factory.ChildrenFactory):
            def builders(self):
                yield Dandruff
                yield from super().builders()
