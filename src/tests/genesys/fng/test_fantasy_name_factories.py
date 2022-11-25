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
from genesys.fng.names.place.galaxy import GalaxyFactory
from genesys.fng.names.place.world import WorldFactory
####
from genesys.fng.names.pop_culture.dnd.human import name_male, name_male_old, name_female, \
    name_female_old


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
    ####
    AmusementParkFactory,
    GalaxyFactory,
    WorldFactory,
]


def load_factories():
    return { factory.model: factory() for factory in __name_factories }


class TestFantasyNameFactories(unittest.TestCase):
    def test_name_factories(self):
        print()
        for factory_id, factory in load_factories().items():
            for _ in range(10):
                model = factory()
                built_with = model.built_with
                factory_name = 'UNKNOWN'
                if built_with is not None:
                    factory_name = built_with.__class__
                print(f"{repr(model)}:\t{factory_name}")
                self.assertEqual(model.__class__, factory_id)

    def test_dnd_human_name_factories(self):
        print()
        factories = [
            name_male(),
            # name_male_old,
            name_female(),
            # name_female_old,
        ]
        for factory in factories:
            for _ in range(10):
                model = factory()
                built_with = model.built_with
                factory_name = 'UNKNOWN'
                if built_with is not None:
                    factory_name = built_with.__class__
                print(f"{repr(model)}:\t{factory_name}")
                self.assertEqual(model.__class__, factory.model)


if __name__ == "__main__":
    unittest.main()
