from genesys.nested.data.unknown import Computer
from genesys.nested.models import Model
from .biology import Body, Thoughts
from .cloth import ClothingSet
from . import lookups


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
