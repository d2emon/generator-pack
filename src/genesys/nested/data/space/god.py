from .. import unknown
from genesys.nested.models import Model
from ..person.people import Body
from ..person.people.clothing import ClothingSet
from .. import lookups


class D2emonThoughts(unknown.Thoughts):
    class BaseFactory(Model.BaseFactory):
        default = lookups.d2emon_thoughts


class D2emonPsyche(Model):
    thoughts = Model.child_property(unknown.Thoughts)

    class NameFactory(Model.NameFactory):
        default = 'psyche'

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield D2emonThoughts


class D2emon(Model):
    body = Model.child_property(Body)
    psyche = Model.child_property(D2emonPsyche)
    clothes = Model.child_property(ClothingSet)
    computer = Model.child_property(unknown.Computer)

    class NameFactory(Model.NameFactory):
        default = 'psyche'

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Body
            yield D2emonPsyche
            yield ClothingSet
            yield unknown.Computer


class God(D2emon):
    pass
