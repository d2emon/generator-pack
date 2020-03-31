from genesys.nested.factories import Thing, ChildFactory


class DysonSphere(Thing):
    type_name = "dyson sphere"
    child_generators = [
        ChildGenerator("star"),
        ChildGenerator("star", probability=3),
        ChildGenerator("dyson surface"),
        ChildGenerator("future planet", (1, 8)),
        ChildGenerator("barren planet", probability=60),
        ChildGenerator("barren planet", probability=40),
        ChildGenerator("barren planet", probability=20),
        ChildGenerator("gas giant", probability=60),
        ChildGenerator("gas giant", probability=40),
        ChildGenerator("gas giant", probability=20),
        ChildGenerator("gas giant", probability=10),
        ChildGenerator("asteroid belt", (0, 2)),
    ]


class DysonSurface(Thing):
    type_name = "dyson surface"
    child_generators = [ChildGenerator("dyson segment", (16,))]


class DysonSegment(Thing):
    type_name = "dyson segment"
    child_generators = [
        ChildGenerator("future city", (4, 20)),
        ChildGenerator("nanocollector", (12, 20)),
    ]