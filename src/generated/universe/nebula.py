from genesys.model.model import Model
from ..materials.matter import Gas
# from generated.universe.space.life import Habitat, NebulaLife
# from generated.universe.space.star import StarSystem, SingleStar
# from generated.materials.chemistry import Ammonia, Gas, Matter, Steam
# from genesys.nested.data import lookups


class InterstellarCloud(Gas):
    pass


class Nebula(Model):
    # Habitat
    # stars = Model.children_property(StarSystem)
    clouds = Model.children_property(InterstellarCloud)
