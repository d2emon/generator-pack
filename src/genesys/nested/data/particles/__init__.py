from genesys.nested.v1.thing import Thing
from genesys.nested.v1.children import ChildGenerator

class Atom(Thing):
    type_name = "atom"
    child_generators = [
        ChildGenerator("proton"),
        ChildGenerator("neutron"),
        ChildGenerator("electron"),
    ]
    names_data = ["atoms"]


# addThing("molecule",["atom"],["molecules"])

class Proton(Thing):
    type_name = "proton"
    child_generators = [
        ChildGenerator("up quark", (2,)),
        ChildGenerator("down quark"),
    ]


class Neutron(Thing):
    type_name = "neutron"
    child_generators = [
        ChildGenerator("up quark"),
        ChildGenerator("down quark", (2,)),
    ]


class Particle(Thing):
    child_generators = [ChildGenerator("qwubble")]


class Electron(Particle):
    type_name = "electron"


class UpQuark(Particle):
    type_name = "up quark"


class DownQuark(Particle):
    type_name = "down quark"


class Qwubble(Thing):
    type_name = "qwubble"
    child_generators = [ChildGenerator("multiverse", (1, 5))]


# addThing("portal",["universe"])


CONTENTS = [
    Atom,
    Proton,
    Neutron,
    Electron,
    UpQuark,
    DownQuark,
    Qwubble,
]