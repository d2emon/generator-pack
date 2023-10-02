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

    contents = NestedModel.contents_property()


class Universe(NestedModel):
    contents = NestedModel.contents_property()


class Multiverse(NestedModel):
    field_names = [
        'universes',
    ]

    universes = NestedModel.field_property('universes')
