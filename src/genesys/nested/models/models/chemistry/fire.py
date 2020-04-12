from genesys.nested.models import Model
from .elements import elements, Atom
from .matter import Matter
from .organics import OrganicMatter


class Fire(Model):
    atoms = Model.child_property(Atom)

    class Factory(Model.Factory):
        def children(self):
            yield elements['C']
            yield elements['O']


class Ash(Matter):
    contents = Matter.children_property(OrganicMatter, Atom)

    class Factory(Matter.Factory):
        def children(self):
            yield OrganicMatter
            yield elements['C']


# Things.add_thing("portal",["universe"])
