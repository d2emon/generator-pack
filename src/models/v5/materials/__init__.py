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


from ...materials.elements import Nucleus, Atom
from .particles import Qwubble, Quark, UpQuark, DownQuark, Electron, Particle, Proton, Neutron
from .portal import Portal

"""
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
