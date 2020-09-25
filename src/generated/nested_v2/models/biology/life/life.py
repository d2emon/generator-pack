from genesys.nested.factories.v2.thing_builder import ListFactory
from genesys.nested.models import Model
# from ..cnidaria import Cnidaria
# from ..crustacean import Crustacean
# from ..fish import Fish, Shark
# from ..insect import Insect, Anthill, Beehive
# from ..mammal import Cetacean
# from ..mollusk import Clam, Mollusk
# from ..monsters import SeaMonster, SpaceMonster, SpaceAnimal
# from ..plankton import Plankton
# from ..vegetation import Tree, GrassBlade
# from ..worm import Worm
# from ...person import Person


class Life(Model):
    # trees = Model.children_property(Tree)

    default_name = 'Life'

    class Factory(Model.Factory):
        @classmethod
        def life_types(cls):
            return ListFactory([
                # Bird,
                # Poultry,
                # Fish,
                # Shark,
                # Crustacean,
                # Cnidaria,
                # Worm,
                # Mollusk,
                # Clam,
                # Plankton,
                # Reptile,
                # Amphibian,
                # Snake,
                # SmallMammal,
                # HerbivorousMammal,
                # PredatoryMammal,
                # Monkey,
                # Bear,
                # Horse,
                # Cat,
                # Dinosaur,
                # MedievalPerson,
                # Caveman,
                # Dragon,
                # Person,
                # SpaceAnimal,
                # Insect,
                # Tree,
                # GrassBlade,
            ])

        def children(self):
            yield next(self.life_types())


class Habitat(Model):
    life = Model.child_property(Life)


class SeaLife(Life):
    class Factory(Life.Factory):
        def children(self):
            # yield SeaMonster.probable(0.5)
            # yield from Fish.multiple(5, 10)
            # yield from Cetacean.multiple(0, 4)
            # yield from Shark.multiple(0, 4)
            # yield from Crustacean.multiple(1, 4)
            # yield from Cnidaria.multiple(1, 4)
            # yield from Mollusk.multiple(1, 4)
            # yield from Clam.multiple(1, 4)
            # yield from Plankton.multiple(2, 8)
            yield None


class AbyssLife(SeaLife):
    class Factory(SeaLife.Factory):
        def children(self):
            # yield SeaMonster.probable(2)
            # yield from Fish.multiple(3, 6)
            # yield from Cetacean.multiple(0, 2)
            # yield from Shark.multiple(0, 2)
            # yield from Crustacean.multiple(2, 5)
            # yield from Cnidaria.multiple(2, 5)
            # yield from Mollusk.multiple(2, 5)
            # yield from Clam.multiple(2, 5)
            # yield from Plankton.multiple(2, 8)
            yield None


class BeachLife(Life):
    class Factory(Life.Factory):
        def children(self):
            # yield from Bird.multiple(0, 3)
            # yield HerbivorousMammal.probable(5)
            # yield Amphibian.probable(2)
            # yield Reptile.probable(2)
            # yield Snake.probable(2)
            # yield PredatoryMammal.probable(5)
            # yield from SmallMammal.multiple(2, 5)
            # yield from Insect.multiple(3, 10)
            # yield from Clam.multiple(3, 8)
            yield None


class RiverLife(Life):
    class Factory(Life.Factory):
        def children(self):
            # yield from Fish.multiple(5, 15)
            # yield from Crustacean.multiple(0, 10)
            # yield from Plankton.multiple(2, 8)
            # yield from Bird.multiple(0, 5)
            # yield from SmallMammal.multiple(0, 2)
            # yield from Amphibian.multiple(0, 5)
            # yield from Reptile.multiple(0, 1)
            # yield from Snake.multiple(0, 1)
            # yield from Insect.multiple(3, 10)
            yield None


class LakeLife(Life):
    class Factory(Life.Factory):
        def children(self):
            # yield SeaMonster.probable(1)
            # yield from Fish.multiple(5, 15)
            # yield from Amphibian.multiple(0, 5)
            # yield from Crustacean.multiple(0, 10)
            # yield from Bird.multiple(0, 5)
            # yield from Plankton.multiple(5, 15)
            # yield from SmallMammal.multiple(0, 2)
            # yield from Reptile.multiple(0, 1)
            # yield from Snake.multiple(0, 1)
            # yield from Insect.multiple(3, 10)
            yield None


class LandLife(Life):
    class Factory(Life.Factory):
        def children(self):
            # yield from HerbivorousMammal.multiple(2, 8)
            # yield Horse.probable(5)
            # yield from PredatoryMammal.multiple(0, 4)
            # yield from SmallMammal.multiple(5, 10)
            # yield from Amphibian.multiple(0, 2)
            # yield from Reptile.multiple(0, 2)
            # yield from Snake.multiple(0, 2)
            # yield from Bird.multiple(0, 5)
            # yield Anthill.probable(30)
            # yield from Insect.multiple(5, 10)
            yield None


class ForestLife(LandLife):
    class Factory(LandLife.Factory):
        def children(self):
            # yield from HerbivorousMammal.multiple(2, 8)
            # yield from PredatoryMammal.multiple(0, 4)
            # yield from Bear.multiple(0, 5)
            # yield from SmallMammal.multiple(5, 10)
            # yield from Amphibian.multiple(0, 3)
            # yield from Reptile.multiple(0, 3)
            # yield from Snake.multiple(0, 3)
            # yield from Bird.multiple(2, 10)
            # yield Beehive.probable(30)
            # yield Anthill.probable(30)
            # yield from Insect.multiple(5, 10)
            yield None


class JungleLife(ForestLife):
    class Factory(ForestLife.Factory):
        def children(self):
            # yield from HerbivorousMammal.multiple(1, 5)
            # yield from PredatoryMammal.multiple(0, 4)
            # yield from Monkey.multiple(1, 5)
            # yield from SmallMammal.multiple(5, 10)
            # yield from Amphibian.multiple(0, 3)
            # yield from Reptile.multiple(0, 3)
            # yield from Snake.multiple(0, 5)
            # yield from Bird.multiple(2, 10)
            # yield Beehive.probable(30)
            # yield Anthill.probable(30)
            # yield from Insect.multiple(5, 10)
            yield None


class MountainLife(LandLife):
    class Factory(LandLife.Factory):
        def children(self):
            # yield from HerbivorousMammal.multiple(1, 6)
            # yield from PredatoryMammal.multiple(0, 4)
            # yield from Bear.multiple(2, 6)
            # yield from SmallMammal.multiple(5, 10)
            # yield from Amphibian.multiple(0, 2)
            # yield from Reptile.multiple(0, 2)
            # yield from Snake.multiple(0, 2)
            # yield from Bird.multiple(2, 10)
            # yield Beehive.probable(30)
            # yield Anthill.probable(30)
            # yield from Insect.multiple(5, 10)
            yield None


class CaveLife(LandLife):
    class Factory(LandLife.Factory):
        def children(self):
            # yield HerbivorousMammal.probable(10)
            # yield PredatoryMammal.probable(10)
            # yield Bear.probable(20)
            # yield SmallMammal.probable(20)
            # yield SmallMammal.probable(20)
            # yield SmallMammal.probable(20)
            # yield Amphibian.probable(20)
            # yield Reptile.probable(20)
            # yield Snake.probable(10)
            # yield Bird.probable(15)
            # yield Bird.probable(5)
            # yield from Insect.multiple(5, 10)
            yield None


class UrbanLife(LandLife):
    class Factory(LandLife.Factory):
        def children(self):
            # yield from Bird.multiple(0, 8)
            # yield from SmallMammal.multiple(5, 10)
            # yield Anthill.probable(30)
            # yield from Insect.multiple(10, 20)
            yield None


class SkyLife(LandLife):
    class Factory(LandLife.Factory):
        def children(self):
            # yield Shark.probable(1)
            # yield from Bird.multiple(5, 20)
            # yield from Insect.multiple(0, 2)
            yield None