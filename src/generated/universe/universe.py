from genesys.model.model import Model
from .galaxy import Galaxy


class Supercluster(Model):
    default_name = 'galactic supercluster'
    galaxies = Model.children_property(Galaxy)


class Universe(Model):
    clusters = Model.children_property(Supercluster)


class Multiverse(Model):
    universes = Model.children_property(Universe)
