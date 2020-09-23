from genesys.nested.factories.v2.thing_builder import ListFactory
from genesys.nested.models import Model
from generated.materials.chemistry import Water, Silica
from ..biology import Habitat
# from ..biology import Worm, Insect


class Soil(Habitat):
    silica = Habitat.child_property(Silica)
    water = Habitat.child_property(Water)

    default_name = 'dirt'

    class Factory(Model.Factory):
        @classmethod
        def life(cls):
            yield from next(ListFactory([
                # Worm.multiple(0, 2),
                [],
                [],
            ]))
            yield from next(ListFactory([
                # Insect.multiple(0, 2),
                [],
                [],
            ]))
            yield None

        def children(self):
            yield from self.life()
            yield Silica


class Mud(Soil):
    default_name = None

    class Factory(Soil.Factory):
        def children(self):
            yield from super().children()
            yield Water


class Sand(Soil):
    default_name = None

    class Factory(Soil.Factory):
        @classmethod
        def life(cls):
            yield None
