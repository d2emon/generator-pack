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
    @property
    def multiverses(self):
        from ..space import Multiverse

        return list(self.children_by_class(Multiverse))

    class Factory(Model.Factory):
        def children(self):
            from ..space import Multiverse

            yield from Multiverse.multiple(1, 5)

    def enter(self):
        return self.multiverses


class Quark(Model):
    qwubbles = Model.children_property(Qwubble)

    class Factory(Model.Factory):
        def children(self):
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
        up_quarks = 1
        down_quarks = 1

        def children(self):
            yield from UpQuark.multiple(self.up_quarks)
            yield from DownQuark.multiple(self.down_quarks)


class Proton(Particle):
    class Factory(Particle.Factory):
        up_quarks = 2
        down_quarks = 1


class Neutron(Particle):
    class Factory(Particle.Factory):
        up_quarks = 1
        down_quarks = 2


class Atom(Model):
    core = Model.children_property(Particle)
    electrons = Model.children_property(Electron)

    default_name = 'atoms'

    class Factory(Model.Factory):
        has_neutron = True

        def children(self):
            yield Proton
            if self.has_neutron:
                yield Neutron
            yield Electron


class HydrogenAtom(Atom):
    class Factory(Model.Factory):
        has_neutron = True
