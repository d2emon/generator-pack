from generated.materials import Portal
from ..factory import Factory


class PortalFactory(Factory):
    default_model = Portal

    def children(self):
        # from ..space import Universe

        # yield UniverseFactory()
        yield from []
