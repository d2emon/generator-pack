from ..models import Model


Button = Model
Coin = Model
Computer = Model
Continent = Model
Crumbs = Model
CrustaceanClaw = Model
Donut = Model
Dust = Model
DysonSurface = Model
Ghost = Model
Glass = Model
Handgun = Model
Lint = Model
Memories = Model
Metal = Model
Note = Model
Ocean = Model
Pasta = Model
Pen = Model
Psyche = Model
Sky = Model
Stinger = Model
Thought = Model
Thoughts = Model
VisitorCity = Model
VisitorInstallation = Model
WeirdHardOrgan = Model
WeirdSoftOrgan = Model

TerraformedSky = Sky
FutureContinent = Continent
FutureSky = Sky
MedievalContinent = Continent
AncientContinent = Continent


# Biology
Bacteria = Model
Crustacean = Model
GalacticLife = Model
SpaceAnimal = Model
SpaceMonster = Model
Worm = Model


####


class Keratin(NestedItem):
    @classmethod
    def get_children(cls):
        yield materials.Proteins


class Sweat(NestedItem):
    @classmethod
    def get_children(cls):
        yield materials.Water
        yield materials.Salt
        yield materials.Glucids
