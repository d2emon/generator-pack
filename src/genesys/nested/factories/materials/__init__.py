from .elements import NucleusFactory, AtomFactory, HydrogenAtomFactory, element_factories
from .fire import FireFactory, AshFactory
from .matter import MoleculeFactory, SteelFactory
from .minerals import AmmoniaMoleculeFactory, AmmoniaFactory, SilicaFactory, SaltFactory, RockFactory, DiamondFactory, \
    MagmaFactory, CarbonFactory, IronFactory
from .organics import OrganicMoleculeFactory, MethaneFactory, ChitinFactory, ProteinsFactory, LipidsFactory,\
    GlucidsFactory, AlcoholFactory, PolymersFactory, OrganicFactory, OilFactory, PolymericFactory, PlasticFactory, \
    RubberFactory
from .particles import ParticleFactory, ProtonFactory, NeutronFactory, QuarkFactory, UpQuarkFactory, DownQuarkFactory, \
    ElectronFactory, QwubbleFactory
from .portal import PortalFactory
from .water import WaterMoleculeFactory, WaterFactory, SteamFactory, DewFactory, IceFactory, SnowflakesFactory, \
    SnowFactory


FACTORIES = {
    'diamond': DiamondFactory(),
    'oil': OilFactory(),
    'magma': MagmaFactory(),
    'rock': RockFactory(),
    'silica': SilicaFactory(),
    'chitin': ChitinFactory(),
    'salt': SaltFactory(),
    'water': WaterFactory(),
    'fire': FireFactory(),
    'ash': AshFactory(),
    'dew': DewFactory(),
    'ice': IceFactory(),
    'snow': SnowFactory(),
    'snowflakes': SnowflakesFactory(),
    'ammonia': AmmoniaFactory(),
    'methane': MethaneFactory(),
    'hydrogen': element_factories['H'](),
    'hydrogen atom': HydrogenAtomFactory(),
    'plastic': PlasticFactory(),
    'rubber': RubberFactory(),
    'polymers': PolymersFactory(),
    'alcohol': AlcoholFactory(),
    'carbon': CarbonFactory(),
    'sodium': element_factories['Na'](),
    'chlorine': element_factories['Cl'](),
    'oxygen': element_factories['O'](),
    'helium': element_factories['He'](),
    'potassium': element_factories['K'](),
    'aluminium': element_factories['Al'](),
    'iron': IronFactory(),
    'copper': element_factories['Cu'](),
    'lead': element_factories['Pb'](),
    'steel': SteelFactory(),
    'gold': element_factories['Au'](),
    'silver': element_factories['Ag'](),
    'silicon': element_factories['Si'](),
    'calcium': element_factories['Ca'](),
    'nitrogen': element_factories['N'](),
    'sulfur': element_factories['S'](),
    'phosphorus': element_factories['P'](),
    # alright, I'm not doing the whole periodic table.
    'proteins': ProteinsFactory(),
    'lipids': LipidsFactory(),
    'glucids': GlucidsFactory(),
    'organic matter': OrganicFactory(),
    'atom': AtomFactory(),
    'molecule': MoleculeFactory(),
    'proton': ProtonFactory(),
    'neutron': NeutronFactory(),
    'electron': ElectronFactory(),
    'up quark': UpQuarkFactory(),
    'down quark': DownQuarkFactory(),
    'qwubble': QwubbleFactory(),
    'portal': PortalFactory(),
}
