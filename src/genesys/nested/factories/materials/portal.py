from generated import materials
from ..factory import Factory


class PortalFactory(Factory):
    default_model = materials.Portal

    def children(self):
        from ..universe import UniverseFactory

        yield from UniverseFactory()
