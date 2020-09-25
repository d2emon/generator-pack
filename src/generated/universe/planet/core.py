from genesys.model.model import Model
from ...materials import Rock


class PlanetCore(Model):
    # Habitat
    minerals = Model.children_property(Rock)

    default_name = 'core'
