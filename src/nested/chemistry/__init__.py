from ..thing import Thing
from ..children import ChildGenerator


def ElementGenerator(name):
    return Thing.from_str(name, [".atom"])


class Ammonia(Thing):
    type_name = "ammonia"
    child_generators = [
        ChildGenerator("hydrogen"),
        ChildGenerator("nitrogen"),
    ]


class Methane(Thing):
    type_name = "methane"
    child_generators = [
        ChildGenerator("hydrogen"),
        ChildGenerator("carbon"),
    ]


class Hydrogen(Thing):
    type_name = "hydrogen"
    child_data = [".hydrogen atom"]


class HydrogenAtom(Thing):
    type_name = "hydrogen atom"
    child_data = ["proton", "electron"]
    names_data = ["atoms"]


# addThing("plastic",["polymers"])
# addThing("rubber",["polymers"])
# addThing("polymers",[".glucids"])
# addThing("alcohol",[".glucids"])

Carbon = ElementGenerator("carbon")
# addThing("sodium",[".atom"])
# addThing("chlorine",[".atom"])
Oxygen = ElementGenerator("oxygen")
Helium = ElementGenerator("helium")
# addThing("potassium",[".atom"])
# addThing("aluminium",[".atom"])
Iron = ElementGenerator("iron")
# addThing("copper",[".atom"])
# addThing("lead",[".atom"])
# addThing("steel",["iron","carbon"])
# addThing("gold",[".atom"])
# addThing("silver",[".atom"])
# addThing("silicon",[".atom"])
# addThing("calcium",[".atom"])
Nitrogen = ElementGenerator("nitrogen")
Sulfur = ElementGenerator("sulfur")
# addThing("phosphorus",[".atom"])


CONTENTS = [
    Ammonia,
    Methane,
    Hydrogen,
    HydrogenAtom,
    Carbon,
    Oxygen,
    Helium,
    Iron,
    Nitrogen,
    Sulfur,
]