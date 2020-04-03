from genesys.nested.models import models
from genesys.nested.factories.thing_builder import ThingBuilder
from genesys.nested.data import lookups


class Supercluster(ThingBuilder):
    model = models.Supercluster

    class ChildrenFactory(ThingBuilder.ChildrenFactory):
        def builders(self):
            # yield from Galaxy.multiple(10, 30)
            yield from []


class Universe(ThingBuilder):
    model = models.Universe

    class ChildrenFactory(ThingBuilder.ChildrenFactory):
        def builders(self):
            yield from Supercluster.multiple(10, 30)


class MultiverseBuilder(ThingBuilder):
    model = models.Multiverse

    class DataProvider:
        multiverse = lookups.multiverses.values

    class BaseFactory(ThingBuilder.BaseFactory):
        data = property(lambda self: self.provider.multiverse)

    class ChildrenFactory(ThingBuilder.ChildrenFactory):
        def builders(self):
            yield from Universe.multiple(10, 30)
