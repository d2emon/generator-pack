from genesys.nested.models import Model
from .elements import elements, Atom
from .matter import Matter, Silica


class Rock(Matter):
    contents = Model.children_property(Silica, Atom)

    class Factory(Matter.Factory):
        class ChildrenFactory(Matter.Factory.ChildrenFactory):
            def builders(self):
                yield Silica
                yield elements['Al'].probable(30)
                yield elements['Fe'].probable(20)
                yield elements['K'].probable(20)
                yield elements['Na'].probable(50)
                yield elements['Ca'].probable(50)


class Diamond(Rock):
    class Factory(Rock.Factory):
        class ChildrenFactory(Rock.Factory.ChildrenFactory):
            def builders(self):
                yield elements['C']


class Magma(Rock):
    pass