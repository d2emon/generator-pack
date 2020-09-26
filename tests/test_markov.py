import pytest
import random

from genesys.fixtures.fixtures import streets
from genesys.generator import Street, StreetChain


@pytest.fixture
def count():
    return random.randrange(1, 255)


@pytest.fixture
def length():
    return random.randrange(1, 64)


def test_street():
    street = Street("Name")
    assert str(street)[:4] == "ул. "


def test_generate_street(count):
    for _ in range(count):
        street = Street.generate(64)
        assert str(street)[:4] == "ул. "


def test_street_chain(length):
    assert StreetChain().length == 3
    assert StreetChain(length=length).length == length
    assert StreetChain(streets).length == 3
    assert StreetChain(streets, length=length).length == length

