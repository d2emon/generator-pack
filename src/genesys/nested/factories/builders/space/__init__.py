from genesys.nested.models import models
from genesys.nested.factories.thing_builder import ThingBuilder
from genesys.nested.data import lookups


class SuperclusterBuilder(ThingBuilder):
    model = models.Supercluster

    class ChildrenFactory(ThingBuilder.ChildrenFactory):
        def builders(self):
            # yield from Galaxy.multiple(10, 30)
            yield from []


class UniverseBuilder(ThingBuilder):
    model = models.Universe

    class ChildrenFactory(ThingBuilder.ChildrenFactory):
        def builders(self):
            yield from SuperclusterBuilder.multiple(10, 30)


class MultiverseBuilder(ThingBuilder):
    model = models.Multiverse

    class DataProvider:
        multiverses = lookups.multiverses.values

    class BaseFactory(ThingBuilder.BaseFactory):
        @property
        def data(self):
            return self.provider.multiverses

    class ChildrenFactory(ThingBuilder.ChildrenFactory):
        def builders(self):
            yield from UniverseBuilder.multiple(10, 30)
