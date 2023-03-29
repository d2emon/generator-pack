"""
basic materials and particles
(these are very rough simplifications, don't hold all the inaccuracies against me)

Models:

models.minerals.Diamond
models.minerals.Oil
models.minerals.Magma
models.minerals.Rock
models.minerals.Silica

Need:

aluminium
calcium
carbon
iron
lipids
oxygen
potassium
silicon
sodium
"""


from .elements import Nucleus, Atom
from .fire import Fire, Ash
from .matter import Molecule, Matter, Gas, Steel
from .minerals import Ammonia, Salt, Carbon, Iron
from .organics import OrganicMolecule, Methane, Chitin, Proteins, Lipids, Glucids, Alcohol, Polymers, OrganicMatter, \
    Polymeric, Plastic, Rubber, Keratin, Sweat
from .particles import Qwubble, Quark, UpQuark, DownQuark, Electron, Particle, Proton, Neutron
from .portal import Portal
from .water import Water, Steam, Dew, Ice, Snowflakes, Snow

"""
new Thing("chitin",["carbon", "hydrogen", "oxygen", "nitrogen"]);
new Thing("salt",["chlorine", "sodium"]);
new Thing("water",["hydrogen", "oxygen"]);
new Thing("fire",["oxygen", "carbon"]);
new Thing("ash",["organic matter", "carbon"]);
new Thing("dew",["water"]);
new Thing("ice",["water"]);
new Thing("snow",["snowflakes"]);
new Thing("snowflakes",["water"]);
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
new Thing("organic matter",[["proteins", "lipids", "glucids"], ["proteins", "lipids", "glucids", ""], "salt,30%"]);
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
