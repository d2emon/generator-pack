from generated.nested_v2.models import Bear
from genesys.nested.factories.thing_builder import ListFactory
from genesys.nested.models import Model
from .soil import Sand, Soil
from ..biology import Habitat
# from ..biology import SeaLife, AbyssLife, BeachLife, RiverLife, LakeLife
from generated.chemistry import Water, Salt, Ice, WaterState


class Oceanic(Habitat):
    soil = Habitat.child_property(Soil)

    class Factory(Habitat.Factory):
        @classmethod
        def life(cls):
            yield None

        @classmethod
        def soil(cls):
            yield Sand

        def children(self):
            yield from self.life()
            yield from self.soil()


class Abyss(Oceanic):
    class Factory(Oceanic.Factory):
        @classmethod
        def life(cls):
            # yield AbyssLife
            yield None


class Beach(Oceanic):
    class Factory(Oceanic.Factory):
        @classmethod
        def life(cls):
            # yield BeachLife
            yield None

        @classmethod
        def soil(cls):
            yield Sand

        def children(self):
            yield from self.life()
            yield from self.soil()


class Iceberg(Oceanic):
    soil = Oceanic.child_property(Ice)

    class Factory(Oceanic.Factory):
        @classmethod
        def life(cls):
            yield Bear.probable(30)
            yield Bear.probable(10)

        @classmethod
        def soil(cls):
            yield Ice


class SeaWater(WaterState):
    salt = WaterState.child_property(Salt)

    class Factory(WaterState.Factory):
        def children(self):
            yield Water
            yield Salt


class Sea(Habitat):
    water = Habitat.child_property(WaterState)
    beaches = Habitat.children_property(Beach)

    # class BaseFactory(Model.BaseFactory):
    #     default = map(
    #         lambda color: '{} sea'.format(color),
    #         [
    #             'great', 'wide', 'big', 'old', 'young', 'large', 'small', 'dead', 'shallow', 'deep', 'red', 'yellow',
    #             'green', 'blue', 'orange', 'brown', 'grey', 'black', 'white', 'purple', 'shady', 'bright', 'silver',
    #         ],
    #     )

    class Factory(Model.Factory):
        @classmethod
        def water(cls):
            yield SeaWater

        @classmethod
        def life(cls):
            # yield SeaLife
            yield None

        @classmethod
        def beaches(cls):
            yield from Beach.multiple(2, 6)

        def children(self):
            yield from self.water()
            yield from self.life()
            yield from self.beaches()


class Ocean(Sea):
    abyss = Sea.child_property(Abyss)
    icebergs = Sea.children_property(Iceberg)

    class Factory(Sea.Factory):
        @classmethod
        def water(cls):
            yield SeaWater

        @classmethod
        def life(cls):
            # yield SeaLife
            yield None

        @classmethod
        def beaches(cls):
            yield from Beach.multiple(10, 20)

        @classmethod
        def icebergs(cls):
            yield from next(ListFactory([
                Iceberg.multiple(2, 6),
                [],
                [],
                [],
                [],
            ]))

        @classmethod
        def abyss(cls):
            yield Abyss

        def children(self):
            yield from super().children()
            yield from self.icebergs()
            yield from self.abyss()


# class River(Model):
#     class BaseFactory(Model.BaseFactory):
#         default = ['river', 'stream', 'brook', 'creek']
#
#     class Factory(Model.Factory):
#         def children(self):
#             yield RiverLife
#             yield Water
#             yield Soil
#             yield Mud


# class Lake(Model):
#     class BaseFactory(Model.BaseFactory):
#         default = ['lake', 'lagoon', 'pond', 'marsh', 'creek', 'cove']
#
#     class Factory(Model.Factory):
#         def children(self):
#             yield LakeLife
#             yield Water
#             yield Soil
#             yield Mud
