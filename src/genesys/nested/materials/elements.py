from genesys.nested.factories.nested_factory import NestedFactory
from models.materials import elements
from .particles import ProtonFactory, NeutronFactory, ElectronFactory


class NucleusFactory(NestedFactory):
    model = elements.Nucleus

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
        yield ProtonFactory.multiple(self.protons)
        yield NeutronFactory.multiple(self.neutrons)


class AtomFactory(NestedFactory):
    model = elements.Atom

    electrons = 1
    neutrons = 1
    protons = 1

    def children(self):
        yield NucleusFactory(
            protons=self.protons,
            neutrons=self.neutrons,
        ).one()
        yield ElectronFactory().multiple(self.electrons)

    @classmethod
    def element_class_factory(
        cls,
        name,
        nucleus_neutrons=1,
        nucleus_protons=1,
    ):
        class ElementFactory(cls):
            default_name = name
            electrons = nucleus_protons
            neutrons = nucleus_neutrons
            protons = nucleus_protons


        return ElementFactory

    @classmethod
    def element_factory(cls, element):
        factory = ELEMENTS.get(element)
        if factory is not None:
            return factory.one()
        else:
            return None

    @classmethod
    def element_factories(cls, *elements):
        return (cls.element_factory(element) for element in elements)


class MoleculeFactory(NestedFactory):
    contents = []
    model = elements.Molecule

    @classmethod
    def element_factory(cls, element):
        return AtomFactory.element_factory(element)

    @classmethod
    def element_factories(cls, *elements):
        return AtomFactory.element_factories(*elements)

    def children(self):
        yield from self.element_factories(*self.contents)


ELEMENTS = {
    'H': AtomFactory.element_class_factory('H', 0, 1),
    'He': AtomFactory.element_class_factory('He'),

    # Li
    # Be
    # B
    'C': AtomFactory.element_class_factory('C'),
    'N': AtomFactory.element_class_factory('N'),
    'O': AtomFactory.element_class_factory('O'),
    # F
    # Ne

    'Na': AtomFactory.element_class_factory('Na'),
    # Mg
    'Al': AtomFactory.element_class_factory('Al'),
    'Si': AtomFactory.element_class_factory('Si'),
    'P': AtomFactory.element_class_factory('P'),
    'S': AtomFactory.element_class_factory('S'),
    'Cl': AtomFactory.element_class_factory('Cl'),
    # Ar

    'K': AtomFactory.element_class_factory('K'),
    'Ca': AtomFactory.element_class_factory('Ca'),
    # Sc
    # Ti
    # V
    # Cr
    # Mn
    'Fe': AtomFactory.element_class_factory('Fe'),
    # Co
    # Ni
    'Cu': AtomFactory.element_class_factory('Cu'),
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
    'Ag': AtomFactory.element_class_factory('Ag'),
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
    'Au': AtomFactory.element_class_factory('Au'),
    # Hg
    # Tl
    'Pb': AtomFactory.element_class_factory('Pb'),
    # Bi
    # Po
    # At
    # Rn
}
