"""
Basic materials and particles
(these are very rough simplifications, don't hold all the inaccuracies against me)

.minerals.DiamondFactory
.organics.OilFactory
.minerals.MagmaFactory
.minerals.RockFactory
.minerals.SilicaFactory
.organics.ChitinFactory
.minerals.SaltFactory
.water.WaterFactory
.fire.FireFactory
.fire.AshFactory
.water.DewFactory
.water.IceFactory
.water.SnowFactory
.water.SnowflakesFactory
.minerals.AmmoniaFactory
.organics.MethaneFactory
.elements.element_factories[H]
.elements.HydrogenAtomFactory
.organics.PlasticFactory
.organics.RubberFactory
.organics.PolymersFactory
.organics.AlcoholFactory
.minerals.CarbonFactory
.elements.element_factories[Na]
.elements.element_factories[Cl]
.elements.element_factories[O]
.elements.element_factories[He]
.elements.element_factories[K]
.elements.element_factories[Al]
.minerals.IronFactory
.elements.element_factories[Cu]
.elements.element_factories[Pb]
.elements.element_factories[Na]
.matter.SteelFactory
.elements.element_factories[Au]
.elements.element_factories[Ag]
.elements.element_factories[Si]
.elements.element_factories[Ca]
.elements.element_factories[N]
.elements.element_factories[S]
.elements.element_factories[P]

//alright, I'm not doing the whole periodic table.

new Thing("proteins",[".molecule"]);
new Thing("lipids",[".molecule"]);
new Thing("glucids",[
    CarbonFactory.one(),
    element_factory['H'].one(),
    element_factories['O'].one(),
],"glucose");
new Thing("organic matter",[["proteins", "lipids", "glucids"], ["proteins", "lipids", "glucids", ""], SaltFactory.one().probable(30)]);
new Thing("atom",["proton", "neutron", "electron"],["atoms"]);
new Thing("molecule",["atom"],["molecules"]);
new Thing("proton",["up quark,2", "down quark"]);
new Thing("neutron",["down quark,2", "up quark"]);
new Thing("electron",["qwubble"]);
new Thing("up quark",["qwubble"]);
new Thing("down quark",["qwubble"]);
new Thing("qwubble",["multiverse,1-5"]);
new Thing("portal",["universe"]);
"""

# particles
# portal

from .elements import NucleusFactory, AtomFactory, HydrogenAtomFactory, element_factories
from .fire import FireFactory, AshFactory
from .matter import MoleculeFactory, SteelFactory
from .minerals import AmmoniaMoleculeFactory, AmmoniaFactory, SilicaFactory, SaltFactory, RockFactory, DiamondFactory, \
    MagmaFactory, CarbonFactory, IronFactory
from .organics import OrganicMoleculeFactory, MethaneFactory, ChitinFactory, ProteinsFactory, LipidsFactory,\
    GlucidsFactory, AlcoholFactory, PolymersFactory, OrganicFactory, OilFactory, PolymericFactory, PlasticFactory, \
    RubberFactory, KeratinFactory, SweatFactory
from .particles import ParticleFactory, ProtonFactory, NeutronFactory, QuarkFactory, UpQuarkFactory, DownQuarkFactory, \
    ElectronFactory, QwubbleFactory
from .portal import PortalFactory
from .water import WaterMoleculeFactory, WaterFactory, SteamFactory, DewFactory, IceFactory, SnowflakesFactory, \
    SnowFactory


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
    'hydrogen': element_factories['H'],
    'hydrogen atom': HydrogenAtomFactory,
    'plastic': PlasticFactory,
    'rubber': RubberFactory,
    'polymers': PolymersFactory,
    'alcohol': AlcoholFactory,
    'carbon': CarbonFactory,
    'sodium': element_factories['Na'],
    'chlorine': element_factories['Cl'],
    'oxygen': element_factories['O'],
    'helium': element_factories['He'],
    'potassium': element_factories['K'],
    'aluminium': element_factories['Al'],
    'iron': IronFactory,
    'copper': element_factories['Cu'],
    'lead': element_factories['Pb'],
    'steel': SteelFactory,
    'gold': element_factories['Au'],
    'silver': element_factories['Ag'],
    'silicon': element_factories['Si'],
    'calcium': element_factories['Ca'],
    'nitrogen': element_factories['N'],
    'sulfur': element_factories['S'],
    'phosphorus': element_factories['P'],

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
