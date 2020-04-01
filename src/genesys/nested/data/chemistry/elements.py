from .particles import Atom, HydrogenAtom


def element(atom=Atom):
    class ChemicalElement(atom):
        pass

    return ChemicalElement


elements = {
    'H': element(HydrogenAtom),
    'He': element(),

    # Li
    # Be
    # B
    'C': element(),
    'N': element(),
    'O': element(),
    # F
    # Ne

    'Na': element(),
    # Mg
    'Al': element(),
    'Si': element(),
    'P': element(),
    'S': element(),
    'Cl': element(),
    # Ar

    'K': element(),
    'Ca': element(),
    # Sc
    # Ti
    # V
    # Cr
    # Mn
    'Fe': element(),
    # Co
    # Ni
    'Cu': element(),
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
    'Ag': element(),
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
    'Au': element(),
    # Hg
    # Tl
    'Pb': element(),
    # Bi
    # Po
    # At
    # Rn
}
# alright, I'm not doing the whole periodic table.
