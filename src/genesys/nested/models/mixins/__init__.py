from ...data import unknown
from .. import Model


class EncounteredMixin:
    encounters = Model.children_property(
        unknown.Crustacean,
        unknown.GalacticLife,
        unknown.Ghost,
        unknown.SpaceAnimal,
        unknown.SpaceMonster,
    )


class TerraformedMixin:
    continents = Model.children_property(unknown.Continent)
    oceans = Model.children_property(unknown.Ocean)
    sky = Model.child_property(unknown.Sky)
