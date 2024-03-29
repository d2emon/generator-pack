"""
- Nucleus
- Atom
"""
from models.nested_model import NestedModel as Model
from .particles import Electron, Proton, Neutron


class Nucleus(Model):
    default_name = 'nucleus'

    protons = Model.children_property(Proton)
    neutrons = Model.children_property(Neutron)


class Atom(Model):
    default_name = 'atoms'

    electrons = Model.children_property(Electron)
    nucleus = Model.child_property(Nucleus)
