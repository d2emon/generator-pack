import pytest
import random

from generator_runner import generators, markov_street

from generator.demonym import Demonym
from fixtures.streets import streets


@pytest.fixture
def count():
    return random.randrange(255)


def test_street(count):
    data = [markov_street(streets, 64) for _ in range(count)]
    assert data is None


def test_lugansk(count):
    data = [Demonym('Lugansk') for _ in range(count)]
    assert data is None


def test_all(count):
    for name, g in generators.items():
        print(name)
        data = [g.generate() for _ in range(count)]
        assert data is None


def test_other(count):
    name = random.choice(generators.keys())
    g = generators.get(name)
    data = [g.generate() for _ in range(count)]
    assert data is None
