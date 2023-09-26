"""
- Particle
- Proton
- Neutron
- Quark
- Electron
- UpQuark
- DownQuark
- Qwubble
"""
from models.nested_model import TreeModel as Model


class Qwubble(Model):
    multiverses = property(lambda self: self.children)


class Quark(Model):
    qwubble = Model.child_property(Qwubble)


class UpQuark(Quark):
    pass


class DownQuark(Quark):
    pass


class Electron(Quark):
    pass


class Particle(Model):
    quarks = Model.children_property(Quark)
    qwubble = property(lambda self: [quark.qwubble for quark in self.quarks])


class Proton(Particle):
    pass


class Neutron(Particle):
    pass
