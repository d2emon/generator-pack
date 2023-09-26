from models.nested_model import NestedModel


class Qwubble(NestedModel):
    multiverses = NestedModel.contents_property()


class Quark(NestedModel):
    quark_type = None

    qwubbles = NestedModel.contents_property()


class UpQuark(Quark):
    quark_type = 'up'


class DownQuark(Quark):
    quark_type = 'down'


class Electron(Quark):
    pass


class Particle(NestedModel):
    quarks = NestedModel.contents_property()

    @property
    def qwubble(self):
        for quark in self.quarks:
            yield from quark.qwubbles


class Proton(Particle):
    pass


class Neutron(Particle):
    pass
