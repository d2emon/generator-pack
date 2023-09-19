from factories.thing.nested_factory import NestedFactory as Factory
from models.v5 import materials


class QwubbleFactory(Factory):
    model = materials.Qwubble

    def children(self):
        from ..universe import MultiverseFactory

        yield from MultiverseFactory.multiple(1, 5)


# Quarks


class QuarkFactory(Factory):
    model = materials.Quark

    def children(self):
        yield QwubbleFactory.one()


class UpQuarkFactory(QuarkFactory):
    model = materials.UpQuark


class DownQuarkFactory(QuarkFactory):
    model = materials.DownQuark


class ElectronFactory(QuarkFactory):
    model = materials.Electron


# Particles


class ParticleFactory(Factory):
    model = materials.Particle
    up_quarks = 1
    down_quarks = 1

    def children(self):
        yield from UpQuarkFactory.multiple(self.up_quarks)
        yield from DownQuarkFactory.multiple(self.down_quarks)


class ProtonFactory(ParticleFactory):
    model = materials.Proton
    up_quarks = 2
    down_quarks = 1


class NeutronFactory(ParticleFactory):
    model = materials.Neutron
    up_quarks = 1
    down_quarks = 2
