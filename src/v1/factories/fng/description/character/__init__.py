from v1.fixtures import genders
from v1.fixtures.fng import description
from v1.models.fng.description import MaleCharacterDescription, FemaleCharacterDescription
from v1.models.fng.description.character.race import get_race
from v1.models.fng.description.character.mark import get_mark
from v1.factories.fng.factory import load_data
from v1.factories.fng.name_factory import NameFactory, GenderNameFactory
from v1.factories.fng.validators import generate_while


class BaseCharacterFactory(NameFactory):
    blocks_map = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
        21: 21,
        22: 22,
        23: 23,
        24: 24,
        25: 25,
        26: 26,
        27: 27,
        28: 28,
    }

    @classmethod
    def race_blocks(cls, item):
        race = get_race(item)
        return load_data(race.male)

    @classmethod
    def mark_blocks(cls, item):
        mark = get_mark(item)
        return load_data(mark.male)

    def __update_from_race(self, items):
        blocks = self.race_blocks(items[21])
        update_blocks = [1, 2, 4, 7, 10, 18, 19]
        items.update({item_id: next(blocks[item_id]) for item_id in update_blocks})
        return items

    def __update_from_marks(self, items):
        blocks = self.mark_blocks(items[12])
        update_blocks = [13, 14, 15, 16, 17]
        items.update({item_id: next(blocks[item_id]) for item_id in update_blocks})
        return items

    def validate(self, items) -> dict:
        items = self.__update_from_race(items)
        items = self.__update_from_marks(items)
        items[26] = generate_while(items[26], lambda item: item.item_id == items[25].item_id, self.factory(26))

        return items


class CharacterFactory(GenderNameFactory):
    """Character Factory

    The generator does take into account which race is randomly picked, and changes some of the details accordingly. For
    example, if the character is an elf, they will have a higher chance of looking good and clean, they will, of course,
    have an elvish name, and tend to be related to more elvish related towns and people.

    I've made the descriptions as detailed as possible, while also withholding as many details as possible. This may
    sound odd, but I've done it by mostly describing how a character looks, rather than his or her personality. I've
    tried to make the character's looks and some vague personality traits dictate what kind of person he or she could
    be.

    For example, a character with a scar could've received it during battle, but in this generator it could also have
    been due to an ex-lover, an epic adventure, or a tale of regaining ones honor.
    I hope by doing this you will be able to let your imagination loose and fill in the blanks. One description could
    create hundreds of characters which all look the same, but are entirely different people."""

    class MaleCharacterFactory(BaseCharacterFactory):
        child_class = MaleCharacterDescription
        default_blocks = load_data({
            1: description.character.male_names1,
            2: description.character.male_names2,
            3: description.character.male_names3,
            4: description.character.male_names4,
            5: description.character.male_names5,
            6: description.character.male_names6,
            7: description.character.male_names7,
            8: description.character.male_names8,
            9: description.character.male_names9,
            10: description.character.male_names10,
            11: description.character.male_names11,
            12: description.character.male_names12,
            13: description.character.male_names13,
            14: description.character.male_names14,
            15: description.character.male_names15,
            16: description.character.male_names16,
            17: description.character.male_names17,
            18: description.character.male_names18,
            19: description.character.male_names19,
            20: description.character.male_names20,
            21: description.character.male_names21,
            22: description.character.male_names22,
            23: description.character.male_names23,
            24: description.character.male_names24,
            25: description.character.male_names25,
            26: description.character.male_names26,
            27: description.character.male_names27,
            28: description.character.male_names28,
        })

        @classmethod
        def race_blocks(cls, item):
            race = get_race(item)
            return load_data(race.male)

        @classmethod
        def mark_blocks(cls, item):
            mark = get_mark(item)
            return load_data(mark.male)

    class FemaleCharacterFactory(BaseCharacterFactory):
        child_class = FemaleCharacterDescription
        default_blocks = load_data({
            1: description.character.female_names1,
            2: description.character.female_names2,
            3: description.character.female_names3,
            4: description.character.female_names4,
            5: description.character.female_names5,
            6: description.character.female_names6,
            7: description.character.female_names7,
            8: description.character.female_names8,
            9: description.character.female_names9,
            10: description.character.female_names10,
            11: description.character.female_names11,
            12: description.character.female_names12,
            13: description.character.female_names13,
            14: description.character.female_names14,
            15: description.character.female_names15,
            16: description.character.female_names16,
            17: description.character.female_names17,
            18: description.character.female_names18,
            19: description.character.female_names19,
            20: description.character.female_names20,
            21: description.character.female_names21,
            22: description.character.female_names22,
            23: description.character.female_names23,
            24: description.character.female_names24,
            25: description.character.female_names25,
            26: description.character.female_names26,
            27: description.character.female_names27,
            28: description.character.female_names28,
        })

        @classmethod
        def race_blocks(cls, item):
            race = get_race(item)
            return load_data(race.female)

        @classmethod
        def mark_blocks(cls, item):
            mark = get_mark(item)
            return load_data(mark.female)

    factory_classes = {
        genders.MALE: MaleCharacterFactory,
        genders.FEMALE: FemaleCharacterFactory,
    }
