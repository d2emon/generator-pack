"""
- Atom
- Hydrogen Atom
- Proton
- Neutron
- Electron
- Up Quark
- Down Quark
- Qwubble

- Quark

new Thing("molecule",["atom"],["molecules"]);
"""
from genesys.nested.models import Model


class Qwubble(Model):
    def enter(self):
        # new Thing("qwubble",["multiverse,1-5"]);
        pass


class Quark(Model):
    qwubbles = Model.children_property(Qwubble)

    @classmethod
    def children_classes(cls):
        yield Qwubble


class UpQuark(Quark):
    pass


class DownQuark(Quark):
    pass


class Electron(Quark):
    pass


class Particle(Model):
    quarks = Model.children_property(Quark)

    class ChildrenFactory(Model.ChildrenFactory):
        up_quarks = 1
        down_quarks = 1

        def children_classes(self):
            yield from UpQuark.multiple(self.up_quarks)
            yield from DownQuark.multiple(self.down_quarks)


class Proton(Particle):
    class ChildrenFactory(Particle.ChildrenFactory):
        up_quarks = 2
        down_quarks = 1


class Neutron(Particle):
    class ChildrenFactory(Particle.ChildrenFactory):
        up_quarks = 1
        down_quarks = 2


class Atom(Model):
    core = Model.children_property(Particle)
    electrons = Model.children_property(Electron)

    class NameFactory(Model.NameFactory):
        default = 'atoms'

    class ChildrenFactory(Model.ChildrenFactory):
        has_neutron = True

        def children_classes(self):
            yield Proton
            if self.has_neutron:
                yield Neutron
            yield Electron


class HydrogenAtom(Atom):
    class ChildrenFactory(Atom.ChildrenFactory):
        has_neutron = True
