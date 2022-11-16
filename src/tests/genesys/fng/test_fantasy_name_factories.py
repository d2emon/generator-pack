import unittest
from genesys.fng.names.fantasy.alien import AlienNameFactory
from genesys.fng.names.fantasy.amazon import AmazonNameFactory
from genesys.fng.names.fantasy.anansi import AnansiNameFactory
from genesys.fng.names.fantasy.angel import AngelNameFactory
from genesys.fng.names.fantasy.animal_species import AnimalSpeciesNameFactory
from genesys.fng.names.fantasy.animatronic import AnimatronicNameFactory
from genesys.fng.names.fantasy.anime_character import AnimeNameFactory
from genesys.fng.names.fantasy.anthousai import AnthousaiNameFactory
from genesys.fng.names.fantasy.anzu import AnzuNameFactory
from genesys.fng.names.fantasy.apocalypse import ApocalypseNicknameFactory
from genesys.fng.names.fantasy.artificial_itelligence import ArtificialIntelligenceNameFactory
from genesys.fng.names.fantasy.bandit import BanditNameFactory
from genesys.fng.names.fantasy.banshee import BansheeNameFactory
from genesys.fng.names.fantasy.barbarian import BarbarianNameFactory
from genesys.fng.names.fantasy.basilisk import BasiliskNameFactory
####
from genesys.fng.names.place.amusement_park import AmusementParkFactory


__name_factories = [
    AlienNameFactory,
    AmazonNameFactory,
    AnansiNameFactory,
    AngelNameFactory,
    AnimalSpeciesNameFactory,
    AnimatronicNameFactory,
    AnimeNameFactory,
    AnthousaiNameFactory,
    AnzuNameFactory,
    ApocalypseNicknameFactory,
    ArtificialIntelligenceNameFactory,
    BanditNameFactory,
    BansheeNameFactory,
    BarbarianNameFactory,
    BasiliskNameFactory,
]


def load_factories():
    return { factory.model: factory() for factory in __name_factories }


class TestFantasyNameFactories(unittest.TestCase):
    def test_name_factories(self):
        print()
        for factory_id, factory in load_factories().items():
            for _ in range(10):
                model = factory()
                print(repr(model))
                self.assertEqual(model.__class__, factory_id)

    def test_place_factories(self):
        print()
        factory = AmusementParkFactory()
        for _ in range(10):
            model = factory()
            print(repr(model))
            self.assertEqual(model.__class__, AmusementParkFactory.model)


if __name__ == "__main__":
    unittest.main()
