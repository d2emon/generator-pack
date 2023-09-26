from genesys.nested.factories.nested_factory import NestedFactory
from models.materials import particles


class QwubbleFactory(NestedFactory):
    model = particles.Qwubble

    def children(self):
        from ..universe import MultiverseFactory

        yield MultiverseFactory.multiple(1, 5)


# Quarks


class QuarkFactory(NestedFactory):
    model = particles.Quark

    def children(self):
        yield QwubbleFactory.one()


class UpQuarkFactory(QuarkFactory):
    model = particles.UpQuark


class DownQuarkFactory(QuarkFactory):
    model = particles.DownQuark


class ElectronFactory(QuarkFactory):
    model = particles.Electron


# Particles


class ParticleFactory(NestedFactory):
    model = particles.Particle
    up_quarks = 1
    down_quarks = 1

    def children(self):
        yield from UpQuarkFactory.multiple(self.up_quarks)
        yield from DownQuarkFactory.multiple(self.down_quarks)


class ProtonFactory(ParticleFactory):
    model = particles.Proton
    up_quarks = 2
    down_quarks = 1


class NeutronFactory(ParticleFactory):
    model = particles.Neutron
    up_quarks = 1
    down_quarks = 2
