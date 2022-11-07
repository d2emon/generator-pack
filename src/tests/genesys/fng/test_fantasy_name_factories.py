import unittest
from genesys.fng.factories.names.fantasy.alien import AlienNameFactory
from genesys.fng.factories.names.fantasy.amazon import AmazonNameFactory
from genesys.fng.factories.names.fantasy.anansi import AnansiNameFactory
from genesys.fng.factories.names.fantasy.angel import AngelNameFactory
from genesys.fng.factories.names.fantasy.animal_species import AnimalSpeciesNameFactory
from genesys.fng.factories.names.fantasy.animatronic import AnimatronicNameFactory
from genesys.fng.factories.names.fantasy.anime_character import AnimeNameFactory
from genesys.fng.factories.names.fantasy.anthousai import AnthousaiNameFactory
from genesys.fng.factories.names.fantasy.apocalypse import ApocalypseNicknameFactory
from genesys.fng.factories.names.fantasy.artificial_itelligence import ArtificialIntelligenceNameFactory
from genesys.fng.factories.names.fantasy.bandit import BanditNameFactory
from genesys.fng.factories.names.fantasy.banshee import BansheeNameFactory
from genesys.fng.factories.names.fantasy.barbarian import BarbarianNameFactory


__factories = [
    AlienNameFactory,
    AmazonNameFactory,
    AnansiNameFactory,
    AngelNameFactory,
    AnimalSpeciesNameFactory,
    AnimatronicNameFactory,
    AnimeNameFactory,
    AnthousaiNameFactory,
    ApocalypseNicknameFactory,
    ArtificialIntelligenceNameFactory,
    BanditNameFactory,
    BansheeNameFactory,
    BarbarianNameFactory,
]


def load_factories():
    return { factory.model: factory() for factory in __factories }


class TestFantasyNameFactories(unittest.TestCase):
    def test_name_factories(self):
        print()
        for factory_id, factory in load_factories().items():
            for _ in range(10):
                model = factory()
                print(repr(model))
                self.assertEqual(model.__class__, factory_id)


if __name__ == "__main__":
    unittest.main()
