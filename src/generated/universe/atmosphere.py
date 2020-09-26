from genesys.model.model import Model
from ..materials import Gas


class Atmosphere(Model):
    # Habitat
    gases = Model.children_property(Gas)

    default_name = 'atmosphere'
