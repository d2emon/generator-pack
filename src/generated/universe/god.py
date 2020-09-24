from genesys.model.model import Model
from generated.nested_v2.models import Computer
from generated.nested_v2.models.biology import Body, Thoughts
from generated.nested_v2.models.cloth import ClothingSet
from genesys.nested.data import lookups


class D2emonThoughts(Thoughts):
    class BaseFactory(Model.BaseFactory):
        default = lookups.d2emon_thoughts


class D2emonPsyche(Model):
    thoughts = Model.child_property(Thoughts)

    class NameFactory(Model.NameFactory):
        default = 'psyche'

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield D2emonThoughts


class D2emon(Model):
    body = Model.child_property(Body)
    psyche = Model.child_property(D2emonPsyche)
    clothes = Model.child_property(ClothingSet)
    computer = Model.child_property(Computer)

    class NameFactory(Model.NameFactory):
        default = 'psyche'

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Body
            yield D2emonPsyche
            yield ClothingSet
            yield Computer


class God(D2emon):
    pass
