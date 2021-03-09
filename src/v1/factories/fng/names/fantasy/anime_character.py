from v1.fixtures import genders
from v1.fixtures.data_block import load_data
from v1.fixtures.fng.names import fantasy
from v1.models.fng.names.fantasy import AnimeCharacterName
from v1.factories.fng.name_factory import NameFactory, GenderNameFactory


class AnimeNameFactory(GenderNameFactory):
    """Anime Character Name Factory

    Anime and manga character names typically fall into one of three categories: real names, fake names and unique or
    nicknames. Real names are usually just regular Japanese names, but can be from other cultures too depending on the
    anime. Nicknames and unique names tend to be very specific and often belong to the main character, like Ichigo from
    Bleach, Light from Death Note, or Naruto from Naruto.
    The fake names, which this generator focuses on, are similar to regular Japanese names, but you generally wouldn't
    find them in real life. Sometimes they're used to add a fantasy feeling to a story, sometimes they're used to avoid
    (accidental) matches with real life people, especially if a character is portrayed in a negative way, and other
    times it may be a more personal choice of the writer. Either way, this generator will generate a whole range of fake
    Japanese name fit for those types of anime and manga characters.
    Like regular Japanese names, the names in this generator are in surname - personal name order."""

    class MaleAnimeNameFactory(NameFactory):
        name_class = AnimeCharacterName
        blocks_map = {
            1: 1,
            2: 2,
            3: 5,
            4: 6,
        }

    class FemaleAnimeNameFactory(NameFactory):
        name_class = AnimeCharacterName
        blocks_map = {
            1: 3,
            2: 4,
            3: 5,
            4: 6,
        }

    factory_classes = {
        genders.MALE: MaleAnimeNameFactory,
        genders.FEMALE: FemaleAnimeNameFactory,
    }
    default_blocks = load_data({
        1: fantasy.anime_character.nm1,
        2: fantasy.anime_character.nm2,
        3: fantasy.anime_character.nm3,
        4: fantasy.anime_character.nm4,
        5: fantasy.anime_character.nm5,
        6: fantasy.anime_character.nm6,
    })
