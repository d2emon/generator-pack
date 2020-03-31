from genesys.nested.factories import Thing, ChildFactory


# addThing("planet",[".terraformed planet"],"telluric planet")
class Planet(Thing):
    pass


class TelluricPlanet(Planet):
    names_data = "telluric planet"


class BarrenPlanet(TelluricPlanet):
    child_generators = [
        ChildGenerator("galactic life", probability=10),
        ChildGenerator("rock"),
        ChildGenerator("ice", probability=50),
        ChildGenerator(".planet composition"),
    ]


class VisitorPlanet(TelluricPlanet):
    child_generators = [
        ChildGenerator("visitor city", (1, 8)),
        ChildGenerator("visitor installation", (2, 6)),
        ChildGenerator("galactic life"),
        ChildGenerator("rock"),
        ChildGenerator("ice", probability=50),
        ChildGenerator(".planet composition"),
    ]


class FuturePlanet(TelluricPlanet):
    child_generators = [
        ChildGenerator("future continent", (2, 7)),
        ChildGenerator("ocean", (1, 7)),
        ChildGenerator("future sky"),
        ChildGenerator(".future moon", probability=30),
        ChildGenerator(".planet composition"),
    ]


class TerraformedPlanet(TelluricPlanet):
    child_generators = [
        ChildGenerator("continent", (2, 7)),
        ChildGenerator("ocean", (1, 7)),
        ChildGenerator("terraformed sky"),
        ChildGenerator(".terraformed moon", probability=30),
        ChildGenerator(".planet composition"),
    ]


class MedievalPlanet(TelluricPlanet):
    child_generators = [
        ChildGenerator("medieval continent", (2, 4)),
        ChildGenerator("ancient continent", (0, 3)),
        ChildGenerator("ocean", (1, 7)),
        ChildGenerator("sky"),
        ChildGenerator(".planet composition"),
    ]


class AncientPlanet(TelluricPlanet):
    child_generators = [
        ChildGenerator("ancient continent", (2, 7)),
        ChildGenerator("ocean", (1, 7)),
        ChildGenerator("sky"),
        ChildGenerator(".planet composition"),
    ]


class PlanetComposition(Thing):
    child_generators = [
        ChildGenerator("planet core"),
        ChildGenerator("moon", probability=40),
        ChildGenerator("moon", probability=20),
        ChildGenerator("moon", probability=10)
    ]
    names_data = "planet"


class Moon(Planet):
    child_generators = [
        ChildGenerator("ghost", probability=0.1),
        ChildGenerator("rock"),
        ChildGenerator("planet core"),
    ]
    names_data = [
        ["young","old","large","small","pale","white","dark","black","old"],
        [" moon"],
    ]


class TerraformedMoon(Moon):
    child_generators = [
        ChildGenerator(".planet composition"),
        ChildGenerator("continent", (1, 4)),
        ChildGenerator("ocean", (1, 4)),
        ChildGenerator("sky"),
    ]
    names_data = [
        ["young", "old", "large", "small", "pale", "white", "dark", "black", "old", "green", "lush", "blue", "city", "colonized", "life"],
        [" moon"],
    ]


# addThing("earth",[".asteroid belt"],"Earth")


class Asteroid(Planet):
    child_generators = [
        ChildGenerator("space animal", probability=0.5),
        ChildGenerator("rock"),
        ChildGenerator("ice", probability=30)
    ]
    names_data = "asteroid"


class GasGiant(Planet):
    child_generators = [
        ChildGenerator("gas giant atmosphere"),
        ChildGenerator("planet core", probability=50),
        ChildGenerator("moon", (0, 3)),
        ChildGenerator("terraformed moon", probability=20),
        ChildGenerator("terraformed moon", probability=10),
    ]


class GasGiantAtmosphere(Thing):
    child_generators = [
        ChildGenerator("galactic life", probability=10),
        ChildGenerator("helium"),
        ChildGenerator("hydrogen"),
        ChildGenerator("water", probability=50),
        ChildGenerator("ammonia", probability=50),
        ChildGenerator("methane", probability=50),
    ]
    names_data = "atmosphere"


class PlanetCore(Thing):
    child_generators = [
        ChildGenerator("space monster", probability=0.5),
        ChildGenerator("iron"),
        ChildGenerator("rock"),
        ChildGenerator("diamond", probability=2),
        ChildGenerator("magma"),
    ]
    names_data = "core"
