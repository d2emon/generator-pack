from genesys.nested.models.models.unknown import Bacteria
from genesys.nested.factories.thing_builder import ThingBuilder
from genesys.nested.models import Model
from ..skin import Dandruff
from ....chemistry import Keratin
from genesys.nested.data import lookups


class Hair(Model):
    bacterias = Model.child_property(Bacteria)
    keratin = Model.child_property(Keratin)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield Bacteria.probable(30)
                yield Keratin


class HeadHair(Hair):
    class BaseFactory(Model.BaseFactory):
        default = lookups.hair

    class Factory(Hair.Factory):
        class ChildrenFactory(Hair.Factory.ChildrenFactory):
            def builders(self):
                yield Dandruff
                yield from super().builders()
