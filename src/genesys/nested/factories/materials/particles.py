from generated import materials
from ..factory import Factory


class QwubbleFactory(Factory):
    default_model = materials.Qwubble

    def children(self):
        # from ..space import Multiverse

        # yield from Multiverse.multiple(1, 5)
        yield from []


class QuarkFactory(Factory):
    default_model = materials.Quark

    def children(self):
        yield QwubbleFactory()


class UpQuarkFactory(QuarkFactory):
    default_model = materials.UpQuark


class DownQuarkFactory(QuarkFactory):
    default_model = materials.DownQuark


class ElectronFactory(QuarkFactory):
    default_model = materials.Electron


class ParticleFactory(Factory):
    default_model = materials.Particle
    up_quarks = 1
    down_quarks = 1

    def children(self):
        yield from UpQuarkFactory().multiple(self.up_quarks)
        yield from DownQuarkFactory().multiple(self.down_quarks)


class ProtonFactory(ParticleFactory):
    default_model = materials.Proton
    up_quarks = 2
    down_quarks = 1


class NeutronFactory(ParticleFactory):
    default_model = materials.Neutron
    up_quarks = 1
    down_quarks = 2
