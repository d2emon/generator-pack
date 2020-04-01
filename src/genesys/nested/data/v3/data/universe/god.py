from nestedg.model import Model
from nestedg.data import unknown, lookups

from nestedg.data.people import Body
from nestedg.data.people.clothing import ClothingSet


class D2emonThoughts(unknown.Thoughts):
    class BaseGenerator(Model.BaseGenerator):
        default = lookups.d2emon_thoughts


class D2emonPsyche(Model):
    thoughts = Model.child_property(unknown.Thoughts)

    class NameGenerator(Model.NameGenerator):
        default = 'psyche'

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield D2emonThoughts


class D2emon(Model):
    body = Model.child_property(Body)
    psyche = Model.child_property(D2emonPsyche)
    clothes = Model.child_property(ClothingSet)
    computer = Model.child_property(unknown.Computer)

    class NameGenerator(Model.NameGenerator):
        default = 'psyche'

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield Body
            yield D2emonPsyche
            yield ClothingSet
            yield unknown.Computer


class God(D2emon):
    pass
