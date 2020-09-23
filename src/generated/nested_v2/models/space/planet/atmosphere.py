from ..life import GasGiantLife, Habitat
from generated.materials.chemistry import Ammonia, Gas, Steam, Methane


class Atmosphere(Habitat):
    gases = Habitat.children_property(Gas)

    default_name = 'atmosphere'

    class Factory(Habitat.Factory):
        @classmethod
        def life(cls):
            yield None

        @classmethod
        def gases(cls):
            yield None

        def children(self):
            yield from self.life()
            yield from self.gases()


class GasGiantAtmosphere(Atmosphere):
    class Factory(Atmosphere.Factory):
        @classmethod
        def life(cls):
            yield GasGiantLife

        @classmethod
        def gases(cls):
            yield Gas.from_atoms('He')
            yield Gas.from_atoms('H')
            yield Steam.probable(50)
            yield Ammonia.probable(50)
            yield Methane.probable(50)
