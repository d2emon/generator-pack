"""
World name.

This name generator will give you random names for worlds, realms, and similar locations. The names
in this generator are similar to Middle Earth, All-World, and Discworld, for example. Names mostly
aimed at either alternative Earths, specific places on Earth, and similar vast expanses of land in
usually fantasy oriented universes.
"""

from data.fng.names.place.world import adjective, noun
from genesys.fng.database import Database
from genesys.fng.factories.name_factory import ComplexFactory
from models.fng.names.name import Name


DB = Database('world', {
    'adjective': adjective,
    'noun': noun,
})


class WorldName(Name):
    """World name model."""

    @property
    def value(self) -> str:
        """
        Get model value.

        Returns:
            str: Value for model
        """
        return " ".join(["The", *self.values])


class WorldFactory(ComplexFactory):
    """World name factory."""

    default_data = DB
    model = WorldName
    parts = [
        'adjective',
        'noun',
    ]
