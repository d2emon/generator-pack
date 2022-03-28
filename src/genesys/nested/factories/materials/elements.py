from generated import materials
from factories.nested_factory import NestedFactory as Factory
from .particles import ProtonFactory, NeutronFactory, ElectronFactory


class NucleusFactory(Factory):
    default_model = materials.Nucleus

    def __init__(
        self,
        model=None,
        name=None,
        protons=1,
        neutrons=1,
    ):
        super().__init__(model, name)
        self.protons = protons
        self.neutrons = neutrons

    def children(self):
        yield from ProtonFactory().multiple(self.protons)
        yield from NeutronFactory().multiple(self.neutrons)


class AtomFactory(Factory):
    default_model = materials.Atom
    protons = 1
    neutrons = 1
    electrons = 1

    def children(self):
        yield NucleusFactory(
            protons=self.protons,
            neutrons=self.neutrons,
        )
        yield from ElectronFactory().multiple(self.electrons)


class HydrogenAtomFactory(AtomFactory):
    neutrons = 0


def element_factory(name, factory=AtomFactory):
    return factory.create_factory(materials.Atom, name)


element_factories = {
    'H': element_factory('H', HydrogenAtomFactory),
    'He': element_factory('He'),

    # Li
    # Be
    # B
    'C': element_factory('C'),
    'N': element_factory('N'),
    'O': element_factory('O'),
    # F
    # Ne

    'Na': element_factory('Na'),
    # Mg
    'Al': element_factory('Al'),
    'Si': element_factory('Si'),
    'P': element_factory('P'),
    'S': element_factory('S'),
    'Cl': element_factory('Cl'),
    # Ar

    'K': element_factory('K'),
    'Ca': element_factory('Ca'),
    # Sc
    # Ti
    # V
    # Cr
    # Mn
    'Fe': element_factory('Fe'),
    # Co
    # Ni
    'Cu': element_factory('Cu'),
    # Zn
    # Ga
    # Ge
    # As
    # Se
    # Br
    # Kr

    # Rb
    # Sr
    # Y
    # Zr
    # Nb
    # Mo
    # Tc
    # Ru
    # Rh
    # Pd
    'Ag': element_factory('Ag'),
    # Cd
    # In
    # Sn
    # Sb
    # Te
    # I
    # Xe

    # Cs
    # Ba
    # La
    # Hf
    # Ta
    # W
    # Re
    # Os
    # Ir
    # Pt
    'Au': element_factory('Au'),
    # Hg
    # Tl
    'Pb': element_factory('Pb'),
    # Bi
    # Po
    # At
    # Rn
}
