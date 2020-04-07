from genesys.nested.models import Model
from .elements import elements, Atom


class Fire(Model):
    atoms = Model.child_property(Atom)

    class Factory(Model.Factory):
        class ChildrenFactory(Model.Factory.ChildrenFactory):
            def builders(self):
                yield elements['C']
                yield elements['O']


# Things.add_thing("portal",["universe"])
