from nestedg.model import Model


class Qwubble(Model):
    def enter(self):
        # new Thing("qwubble",["multiverse,1-5"]);
        pass


class Quark(Model):
    @classmethod
    def children_classes(cls):
        yield Qwubble


class UpQuark(Quark):
    pass


class DownQuark(Quark):
    pass


class Electron(Model):
    @classmethod
    def children_classes(cls):
        yield Qwubble


class Particle(Model):
    quarks = Model.children_property(Quark)

    class ChildrenGenerator(Model.ChildrenGenerator):
        up_quarks = 1
        down_quarks = 1

        def children_classes(self):
            yield from UpQuark.multiple(self.up_quarks)
            yield from DownQuark.multiple(self.down_quarks)


class Proton(Particle):
    class ChildrenGenerator(Particle.ChildrenGenerator):
        up_quarks = 2
        down_quarks = 1


class Neutron(Particle):
    class ChildrenGenerator(Particle.ChildrenGenerator):
        up_quarks = 1
        down_quarks = 2


class Atom(Model):
    particles = Model.children_property(Particle)

    class NameGenerator(Model.NameGenerator):
        default = 'atoms'

    class ChildrenGenerator(Model.ChildrenGenerator):
        has_neutron = True

        def children_classes(self):
            yield Proton
            if self.has_neutron:
                yield Neutron
            yield Electron


class HydrogenAtom(Atom):
    class ChildrenGenerator(Atom.ChildrenGenerator):
        has_neutron = True
