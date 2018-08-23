import pytest
import random

from generator_runner import markov_street
from fixtures.streets import streets


@pytest.fixture
def count():
    return random.randrange(255)


def test_street(count):
    data = [markov_street(streets, 64) for i in range(count)]
    assert data is None
