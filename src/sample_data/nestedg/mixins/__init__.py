from nestedg.data import unknown
from nestedg.model import Model


class EncounteredMixin:
    encounters = Model.children_property(
        unknown.Crustacean,
        unknown.GalacticLife,
        unknown.Ghost,
        unknown.SpaceAnimal,
        unknown.SpaceMonster,
    )

    @property
    def children(self):
        raise NotImplementedError()


class TerraformedMixin:
    continents = Model.children_property(unknown.Continent)
    oceans = Model.children_property(unknown.Ocean)
    sky = Model.child_property(unknown.Sky)

    @property
    def children(self):
        raise NotImplementedError()
