"""
Universe stuff

- D2emon
- God
- D2emon Psyche
- D2emon Thoughts
"""
from models.nested_model import NestedModel


class Supercluster(NestedModel):
    default_name = 'galactic supercluster'
    galaxies = NestedModel.group_property('galaxies')


class Universe(NestedModel):
    superclusters = NestedModel.group_property('superclusters')


class Multiverse(NestedModel):
    universes = NestedModel.group_property('universes')
