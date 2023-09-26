from models.nested_model import NestedModel
from models.materials.particles import Electron, Neutron, Proton


class Nucleus(NestedModel):
    default_name = 'nucleus'

    protons = NestedModel.children_property(Proton)
    neutrons = NestedModel.children_property(Neutron)


class Atom(NestedModel):
    default_name = 'atoms'

    electrons = NestedModel.children_property(Electron)
    nucleus = NestedModel.child_property(Nucleus)


class Molecule(NestedModel):
    default_name = 'molecules'

    atoms = NestedModel.contents_property()