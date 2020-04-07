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
"""
from genesys.nested.models import Model


class Qwubble(Model):
    def enter(self):
        # new Thing("qwubble",["multiverse,1-5"]);
        pass


class Quark(Model):
    qwubbles = Model.children_property(Qwubble)

    class Factory(Model.Factory):
        class ChildrenFactory(Model.Factory.ChildrenFactory):
            def builders(self):
                yield Qwubble


class UpQuark(Quark):
    pass


class DownQuark(Quark):
    pass


class Electron(Quark):
    pass


class Particle(Model):
    quarks = Model.children_property(Quark)

    class Factory(Model.Factory):
        class ChildrenFactory(Model.Factory.ChildrenFactory):
            up_quarks = 1
            down_quarks = 1

            def builders(self):
                yield from UpQuark.multiple(self.up_quarks)
                yield from DownQuark.multiple(self.down_quarks)


class Proton(Particle):
    class Factory(Particle.Factory):
        class ChildrenFactory(Particle.Factory.ChildrenFactory):
            up_quarks = 2
            down_quarks = 1


class Neutron(Particle):
    class Factory(Particle.Factory):
        class ChildrenFactory(Particle.Factory.ChildrenFactory):
            up_quarks = 1
            down_quarks = 2


class Atom(Model):
    core = Model.children_property(Particle)
    electrons = Model.children_property(Electron)

    default_name = 'atoms'

    class Factory(Model.Factory):
        class ChildrenFactory(Model.Factory.ChildrenFactory):
            has_neutron = True

            def builders(self):
                yield Proton
                if self.has_neutron:
                    yield Neutron
                yield Electron


class HydrogenAtom(Atom):
    class Factory(Model.Factory):
        class ChildrenFactory(Model.Factory.ChildrenFactory):
            has_neutron = True
