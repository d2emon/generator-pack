"""
Basic materials and particles
(these are very rough simplifications, don't hold all the inaccuracies against me)
"""

from .particles import ParticleFactory, ProtonFactory, NeutronFactory, QuarkFactory, UpQuarkFactory, DownQuarkFactory, \
    ElectronFactory, QwubbleFactory
from .elements import AtomFactory, MoleculeFactory, ELEMENTS
from .metal import IronFactory, SteelFactory
from .minerals import CarbonFactory, DiamondFactory, MagmaFactory, RockFactory, SilicaFactory
from .water import WaterMoleculeFactory, WaterFactory, SteamFactory, DewFactory, IceFactory, SnowflakesFactory, \
    SnowFactory
from .organics import AmmoniaFactory, AlcoholFactory, ChitinFactory, GlucidsFactory, LipidsFactory, MethaneFactory, OilFactory, \
    OrganicFactory, PlasticFactory, PolymersFactory, ProteinsFactory, RubberFactory, SaltFactory
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
