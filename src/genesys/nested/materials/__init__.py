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
.water.Snow
.water.Snowflakes

new Thing("ammonia",["hydrogen", "nitrogen"]);
new Thing("methane",["hydrogen", "carbon"]);
new Thing("hydrogen",[".hydrogen atom"]);
new Thing("hydrogen atom",["proton", "electron"],["atoms"]);
new Thing("plastic",["polymers"]);
new Thing("rubber",["polymers"]);
new Thing("polymers",[".glucids"]);
new Thing("alcohol",[".glucids"]);
new Thing("carbon",[".atom"]);
new Thing("sodium",[".atom"]);
new Thing("chlorine",[".atom"]);
new Thing("oxygen",[".atom"]);
new Thing("helium",[".atom"]);
new Thing("potassium",[".atom"]);
new Thing("aluminium",[".atom"]);
new Thing("iron",[".atom"]);
new Thing("copper",[".atom"]);
new Thing("lead",[".atom"]);
new Thing("steel",["iron", "carbon"]);
new Thing("gold",[".atom"]);
new Thing("silver",[".atom"]);
new Thing("silicon",[".atom"]);
new Thing("calcium",[".atom"]);
new Thing("nitrogen",[".atom"]);
new Thing("sulfur",[".atom"]);
new Thing("phosphorus",[".atom"]);
//alright, I'm not doing the whole periodic table.
new Thing("proteins",[".molecule"]);
new Thing("lipids",[".molecule"]);
new Thing("glucids",["carbon", "hydrogen", "oxygen"],"glucose");
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

# elements
# matter
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
    'diamond': DiamondFactory(),
    'oil': OilFactory(),
    'magma': MagmaFactory(),
    'rock': RockFactory(),
    'silica': SilicaFactory(),
    'chitin': ChitinFactory(),
    'salt': SaltFactory(),
    ####
    'water': WaterFactory(),
    'fire': FireFactory(),
    'ash': AshFactory(),
    'dew': DewFactory(),
    'ice': IceFactory(),
    'snow': SnowFactory(),
    'snowflakes': SnowflakesFactory(),
    ####
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
