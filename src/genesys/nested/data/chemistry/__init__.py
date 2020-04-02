"""
Basic chemistry and particles

- Ammonia
- Methane
- Hydrogen
- Plastic
- Rubber
- Polymers
- Alcohol
- Carbon
- Sodium
- Chlorine
- Oxygen
- Helium
- Potassium
- Aluminium
- Iron
- Copper
- Lead
- Steel
- Gold
- Silver
- Silicon
- Calcium
- Nitrogen
- Sulfur
- Phosphorus

- Molecule
- Matter

- Organic Molecule
- Organic Matter
- Chitin
- Proteins
- Lipids
- Glucids

- Ash
- Oil
- Keratin
- Sweat
"""
from .rocks import *
from .elements import *
from .matter import *
from .organics import *
from .particles import *
from genesys.nested.models import Model


class Fire(Model):
    atoms = Model.child_property(Atom)

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield elements['C']
            yield elements['O']


# Things.add_thing("portal",["universe"])
