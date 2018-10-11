import pytest
import random

from generator.fng.name.fantasy import *


@pytest.fixture
def count():
    return random.randrange(1, 255)


@pytest.fixture
def generators():
    return [
        alien_name_generate,
        amazon_name_generate,
        angel_name_generate,
        animal_species_generate,
        animatronic_names_generate,
        anthousai_name_generate,
        apocalypse_nickname_generate,
        artificial_intelligence_name_generate,
        bandit_name_generate,
        banshee_name_generate,
        barbarian_name_generate,
    ]


def test_fantasy_names(count, generators):
    for generator in generators:
        print()
        for _ in range(count):
            name = generator()
            print("{:28s} ({})".format(str(name), name.generator.__name__))
            assert name is not None
