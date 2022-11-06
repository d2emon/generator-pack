"""
Anime Character Name.

Anime and manga character names typically fall into one of three categories: real names, fake names
and unique or nicknames. Real names are usually just regular Japanese names, but can be from other
cultures too depending on the anime. Nicknames and unique names tend to be very specific and often
belong to the main character, like Ichigo from Bleach, Light from Death Note, or Naruto from
Naruto.
The fake names, which this generator focuses on, are similar to regular Japanese names, but you
generally wouldn't find them in real life. Sometimes they're used to add a fantasy feeling to a
story, sometimes they're used to avoid (accidental) matches with real life people, especially if a
character is portrayed in a negative way, and other times it may be a more personal choice of the
writer. Either way, this generator will generate a whole range of fake Japanese name fit for those
types of anime and manga characters.
Like regular Japanese names, the names in this generator are in surname - personal name order.
"""

from data.fng.names import fantasy
from genesys.fng.database import Database
from genesys.fng.factories.name_block_factory import GenderNameBlockFactory
from genesys.fng.factories.name_factory import ComplexNameFactory
from models.fng.names.fantasy import AnimeCharacterName


DB = Database('anime', {
    1: fantasy.anime_character.nm1,
    2: fantasy.anime_character.nm2,
    3: fantasy.anime_character.nm3,
    4: fantasy.anime_character.nm4,
    5: fantasy.anime_character.nm5,
    6: fantasy.anime_character.nm6,
})


class AnimeNameFactory(GenderNameBlockFactory):
    """Anime Character Name Factory."""

    class MaleNameFactory(ComplexNameFactory):
        """Method #1."""

        model = AnimeCharacterName
        block_map = {
            'nm1': 1,
            'nm2': 2,
            'nm3': 5,
            'nm4': 6,
        }

    class FemaleNameFactory(ComplexNameFactory):
        """Method #2."""

        model = AnimeCharacterName
        block_map = {
            'nm1': 3,
            'nm2': 4,
            'nm3': 5,
            'nm4': 6,
        }

    model = AnimeCharacterName
    default_data = DB
