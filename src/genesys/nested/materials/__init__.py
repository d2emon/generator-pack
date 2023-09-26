"""
Basic materials and particles
(these are very rough simplifications, don't hold all the inaccuracies against me)
"""

from .particles import DownQuarkFactory, ElectronFactory, NeutronFactory, ProtonFactory, QwubbleFactory, UpQuarkFactory
from .elements import AtomFactory, MoleculeFactory, ELEMENTS
from .gases import AmmoniaFactory, MethaneFactory
from .metal import IronFactory, SteelFactory
from .minerals import CarbonFactory, DiamondFactory, MagmaFactory, RockFactory, SaltFactory, SilicaFactory
from .water import WaterFactory, DewFactory, IceFactory, SnowflakesFactory, SnowFactory
    # SteamFactory
from .organics import AlcoholFactory, ChitinFactory, GlucidsFactory, LipidsFactory, OilFactory, OrganicFactory, PlasticFactory, \
    PolymersFactory, ProteinsFactory, RubberFactory
    # KeratinFactory, SweatFactory
from .fire import AshFactory, FireFactory
from .portal import PortalFactory


FACTORIES = {
    'diamond': DiamondFactory,
    'oil': OilFactory,
    'magma': MagmaFactory,
    'rock': RockFactory,
    'silica': SilicaFactory,
    'chitin': ChitinFactory,
    'salt': SaltFactory,
    'water': WaterFactory,
    'fire': FireFactory,
    'ash': AshFactory,
    'dew': DewFactory,
    'ice': IceFactory,
    'snow': SnowFactory,
    'snowflakes': SnowflakesFactory,
    'ammonia': AmmoniaFactory,
    'methane': MethaneFactory,
    'hydrogen': ELEMENTS['H'],
    'hydrogen atom': ELEMENTS['H'],
    'plastic': PlasticFactory,
    'rubber': RubberFactory,
    'polymers': PolymersFactory,
    'alcohol': AlcoholFactory,
    'carbon': CarbonFactory,
    'sodium': ELEMENTS['Na'],
    'chlorine': ELEMENTS['Cl'],
    'oxygen': ELEMENTS['O'],
    'helium': ELEMENTS['He'],
    'potassium': ELEMENTS['K'],
    'aluminium': ELEMENTS['Al'],
    'iron': IronFactory,
    'copper': ELEMENTS['Cu'],
    'lead': ELEMENTS['Pb'],
    'steel': SteelFactory,
    'gold': ELEMENTS['Au'],
    'silver': ELEMENTS['Ag'],
    'silicon': ELEMENTS['Si'],
    'calcium': ELEMENTS['Ca'],
    'nitrogen': ELEMENTS['N'],
    'sulfur': ELEMENTS['S'],
    'phosphorus': ELEMENTS['P'],

    # alright, I'm not doing the whole periodic table.

    'proteins': ProteinsFactory,
    'lipids': LipidsFactory,
    'glucids': GlucidsFactory,
    'organic matter': OrganicFactory,

    'atom': AtomFactory,
    'molecule': MoleculeFactory,
    'proton': ProtonFactory,
    'neutron': NeutronFactory,
    'electron': ElectronFactory,
    'up quark': UpQuarkFactory,
    'down quark': DownQuarkFactory,
    'qwubble': QwubbleFactory,
    'portal': PortalFactory,
}
