from .particles import Atom, HydrogenAtom


def element(name, atom=Atom):
    class ChemicalElement(atom):
        default_name = name

    return ChemicalElement


elements = {
    'H': element('H', HydrogenAtom),
    'He': element('He'),

    # Li
    # Be
    # B
    'C': element('C'),
    'N': element('N'),
    'O': element('O'),
    # F
    # Ne

    'Na': element('Na'),
    # Mg
    'Al': element('Al'),
    'Si': element('Si'),
    'P': element('P'),
    'S': element('S'),
    'Cl': element('Cl'),
    # Ar

    'K': element('K'),
    'Ca': element('Ca'),
    # Sc
    # Ti
    # V
    # Cr
    # Mn
    'Fe': element('Fe'),
    # Co
    # Ni
    'Cu': element('Cu'),
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
    'Ag': element('Ag'),
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
    'Au': element('Au'),
    # Hg
    # Tl
    'Pb': element('Pb'),
    # Bi
    # Po
    # At
    # Rn
}
# alright, I'm not doing the whole periodic table.
