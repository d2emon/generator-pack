from v1.fixtures import genders
from v1.fixtures.fng import description
from v1.fixtures.data_block import NameItem, NameBlock
from models.fng.description import Character, CharacterDescription, Hair, Face, Eyes, MarkDescription, Name, \
    Personality
from v1.fixtures.data_block import load_data
from v1.factories.fng.name_factory import NameFactory, GenderNameFactory
# from v1.factories.fng.validators import generate_while
from .race import RaceFactory
from .marks import MarksFactory
from .hair import HairFactory
from .data import data_items


class BaseCharacterFactory(NameFactory):
    gender = genders.NEUTRAL
    him_or_her = "it"
    child_class = CharacterDescription
    data_items = data_items

    def __init__(self, blocks=None):
        super().__init__(blocks)

        # Additional factories
        self.race_factory = RaceFactory(self.data_items)
        self.marks_factory = MarksFactory(self.data_items)
        self.hair_factory = HairFactory(self.factories)

    def get_items(self, *args, **kwargs) -> dict:
        """
        :return: Dict with generated data
        """
        print("Race")
        __race = self.race_factory(gender_id=self.gender)
        # __race = self.race_factory(gender_id=genders.NEUTRAL)
        print(__race)

        print("Marks")
        __marks = self.marks_factory(gender_id=self.gender)
        print(__marks)

        print("Personality")
        __personality = Personality({
            'him_or_her': self.him_or_her,
            24: self.factory(24)(),  # 24
            25: self.factory(25)(),  # 25
            26: self.factory(26)(),  # 26
            27: self.factory(27)(),  # 27
            28: self.factory(28)(),  # 28
        })
        print(__personality)
        return {
            'character': Character(
                gender=self.gender,
                hair=__race.factories.hair_factory(gender_id=self.gender),
                face=__race.factories.face_factory(gender_id=self.gender),
                eyes=__race.factories.eyes_factory(gender_id=self.gender),
                origin=__race.factories.origin_factory(gender_id=self.gender),  # 10
                origin_attitude=self.factory(11)(),  # 11
                mark_description=__marks.factories.description_factory(gender_id=self.gender),
                name=__race.factories.character_name_factory(gender_id=self.gender),
                profession=self.factory(20)(),  # 20
                race=__race,
                height=self.factory(22)(),  # 22
                width=self.factory(23)(),  # 23
                personality=__personality,
            ),
        }

    def validate(self, items) -> dict:
        # items[26] = generate_while(items[26], lambda item: item.item_id == items[25].item_id, self.factory(26))

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
        gender = genders.MALE
        him_or_her = "him"
        default_blocks = {
            **load_data({
                # 1: description.character.male_names1,
                # 2: description.character.male_names2,
                3: description.character.male_names3,
                # 4: description.character.male_names4,
                5: description.character.male_names5,
                6: description.character.male_names6,
                # 7: description.character.male_names7,
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
        }

    class FemaleCharacterFactory(BaseCharacterFactory):
        gender = genders.FEMALE
        him_or_her = "her"
        default_blocks = load_data({
            # 1: description.character.female_names1,
            # 2: description.character.female_names2,
            3: description.character.female_names3,
            # 4: description.character.female_names4,
            5: description.character.female_names5,
            6: description.character.female_names6,
            # 7: description.character.female_names7,
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

    factory_classes = {
        genders.MALE: MaleCharacterFactory,
        genders.FEMALE: FemaleCharacterFactory,
    }
