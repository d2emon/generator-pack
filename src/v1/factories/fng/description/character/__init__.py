from v1.fixtures import genders
from v1.fixtures.fng import description
from v1.fixtures.data_block import NameItem, NameBlock
from v1.models.fng.description import MaleCharacterDescription, FemaleCharacterDescription
from v1.factories.fng.factory import load_data
from v1.factories.fng.name_factory import NameFactory, GenderNameFactory
from v1.factories.fng.validators import generate_while
from .race import RaceFactory
from .marks import MarksFactory


def add_racial(
    gender_id,
    race_id,
    hair_color,
    hair_type,
    face_shape,
    eyes_color,
    origin,
    name,
    surname,
):
    return NameBlock().fill(
        # 1
        *hair_color,
        group_id="hair_color",
        gender_id=gender_id,
        race_id=race_id,
    ).fill(
        # 2
        *hair_type,
        group_id="hair_type",
        gender_id=gender_id,
        race_id=race_id,
    ).fill(
        # 4
        *face_shape,
        group_id="face_shape",
        gender_id=gender_id,
        race_id=race_id,
    ).fill(
        # 7
        *eyes_color,
        group_id="eyes_color",
        gender_id=gender_id,
        race_id=race_id,
    ).fill(
        # 10
        *origin,
        group_id="origin",
        gender_id=gender_id,
        race_id=race_id,
    ).fill(
        # 18
        *name,
        group_id="name",
        gender_id=gender_id,
        race_id=race_id,
    ).fill(
        # 19
        *surname,
        group_id="surname",
        gender_id=gender_id,
        race_id=race_id,
    ).values


class BaseCharacterFactory(NameFactory):
    gender = genders.NEUTRAL
    blocks_map = {
        # 1: 1,
        # 2: 2,
        3: 3,
        # 4: 4,
        5: 5,
        6: 6,
        # 7: 7,
        8: 8,
        9: 9,
        # 10: 10,
        11: 11,
        12: 12,
        # 13: 13,
        # 14: 14,
        # 15: 15,
        # 16: 16,
        # 17: 17,
        # 18: 18,
        # 19: 19,
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
    data_items = NameBlock(
        # Male
        *add_racial(
            gender_id=genders.MALE,
            race_id=RaceFactory.HUMAN,
            hair_color=description.character.male_names1,
            hair_type=description.character.male_names2,
            face_shape=description.character.male_names4,
            eyes_color=description.character.male_names7,
            origin=description.character.male_names10,
            name=description.character.male_names18,
            surname=description.character.male_names19,
        ),
        *add_racial(
            gender_id=genders.MALE,
            race_id=RaceFactory.ELF,
            hair_color=description.character.elf_male_names1,
            hair_type=description.character.elf_male_names2,
            face_shape=description.character.elf_male_names4,
            eyes_color=description.character.elf_male_names7,
            origin=description.character.elf_male_names10,
            name=description.character.elf_male_names18,
            surname=description.character.elf_male_names19,
        ),
        *add_racial(
            gender_id=genders.MALE,
            race_id=RaceFactory.GNOME,
            hair_color=description.character.gnome_male_names1,
            hair_type=description.character.gnome_male_names2,
            face_shape=description.character.gnome_male_names4,
            eyes_color=description.character.male_names7,
            origin=description.character.male_names10,
            name=description.character.gnome_male_names18,
            surname=description.character.gnome_male_names19,
        ),
        *add_racial(
            gender_id=genders.MALE,
            race_id=RaceFactory.TROLL,
            hair_color=description.character.male_names1,
            hair_type=description.character.goblin_male_names2,
            face_shape=description.character.goblin_male_names4,
            eyes_color=description.character.male_names7,
            origin=description.character.goblin_male_names10,
            name=description.character.troll_male_names18,
            surname=description.character.troll_male_names19,
        ),
        *add_racial(
            gender_id=genders.MALE,
            race_id=RaceFactory.ORC,
            hair_color=description.character.male_names1,
            hair_type=description.character.goblin_male_names2,
            face_shape=description.character.goblin_male_names4,
            eyes_color=description.character.male_names7,
            origin=description.character.goblin_male_names10,
            name=description.character.orc_male_names18,
            surname=description.character.orc_male_names19,
        ),
        *add_racial(
            gender_id=genders.MALE,
            race_id=RaceFactory.GOBLIN,
            hair_color=description.character.male_names1,
            hair_type=description.character.goblin_male_names2,
            face_shape=description.character.goblin_male_names4,
            eyes_color=description.character.male_names7,
            origin=description.character.goblin_male_names10,
            name=description.character.goblin_male_names18,
            surname=description.character.goblin_male_names19,
        ),
        *add_racial(
            gender_id=genders.MALE,
            race_id=RaceFactory.DWARF,
            hair_color=description.character.male_names1,
            hair_type=description.character.giant_male_names2,
            face_shape=description.character.giant_male_names4,
            eyes_color=description.character.male_names7,
            origin=description.character.male_names10,
            name=description.character.dwarf_male_names18,
            surname=description.character.dwarf_male_names19,
        ),
        *add_racial(
            gender_id=genders.MALE,
            race_id=RaceFactory.GIANT,
            hair_color=description.character.male_names1,
            hair_type=description.character.giant_male_names2,
            face_shape=description.character.giant_male_names4,
            eyes_color=description.character.male_names7,
            origin=description.character.male_names10,
            name=description.character.male_names18,
            surname=description.character.male_names19,
        ),

        # Female
        *add_racial(
            gender_id=genders.FEMALE,
            race_id=RaceFactory.HUMAN,
            hair_color=description.character.female_names1,
            hair_type=description.character.female_names2,
            face_shape=description.character.female_names4,
            eyes_color=description.character.female_names7,
            origin=description.character.female_names10,
            name=description.character.female_names18,
            surname=description.character.female_names19,
        ),
        *add_racial(
            gender_id=genders.FEMALE,
            race_id=RaceFactory.ELF,
            hair_color=description.character.elf_female_names1,
            hair_type=description.character.elf_female_names2,
            face_shape=description.character.elf_female_names4,
            eyes_color=description.character.elf_female_names7,
            origin=description.character.elf_female_names10,
            name=description.character.elf_female_names18,
            surname=description.character.elf_female_names19,
        ),
        *add_racial(
            gender_id=genders.FEMALE,
            race_id=RaceFactory.GNOME,
            hair_color=description.character.gnome_female_names1,
            hair_type=description.character.gnome_female_names2,
            face_shape=description.character.gnome_female_names4,
            eyes_color=description.character.female_names7,
            origin=description.character.female_names10,
            name=description.character.gnome_female_names18,
            surname=description.character.gnome_female_names19,
        ),
        *add_racial(
            gender_id=genders.FEMALE,
            race_id=RaceFactory.TROLL,
            hair_color=description.character.female_names1,
            hair_type=description.character.goblin_female_names2,
            face_shape=description.character.goblin_female_names4,
            eyes_color=description.character.female_names7,
            origin=description.character.goblin_female_names10,
            name=description.character.troll_female_names18,
            surname=description.character.troll_female_names19,
        ),
        *add_racial(
            gender_id=genders.FEMALE,
            race_id=RaceFactory.ORC,
            hair_color=description.character.female_names1,
            hair_type=description.character.goblin_female_names2,
            face_shape=description.character.goblin_female_names4,
            eyes_color=description.character.female_names7,
            origin=description.character.goblin_female_names10,
            name=description.character.orc_female_names18,
            surname=description.character.orc_female_names19,
        ),
        *add_racial(
            gender_id=genders.FEMALE,
            race_id=RaceFactory.GOBLIN,
            hair_color=description.character.female_names1,
            hair_type=description.character.goblin_female_names2,
            face_shape=description.character.goblin_female_names4,
            eyes_color=description.character.female_names7,
            origin=description.character.goblin_female_names10,
            name=description.character.goblin_female_names18,
            surname=description.character.goblin_female_names19,
        ),
        *add_racial(
            gender_id=genders.FEMALE,
            race_id=RaceFactory.DWARF,
            hair_color=description.character.female_names1,
            hair_type=description.character.giant_female_names2,
            face_shape=description.character.giant_female_names4,
            eyes_color=description.character.female_names7,
            origin=description.character.female_names10,
            name=description.character.dwarf_female_names18,
            surname=description.character.dwarf_female_names19,
        ),
        *add_racial(
            gender_id=genders.FEMALE,
            race_id=RaceFactory.GIANT,
            hair_color=description.character.female_names1,
            hair_type=description.character.giant_female_names2,
            face_shape=description.character.giant_female_names4,
            eyes_color=description.character.female_names7,
            origin=description.character.female_names10,
            name=description.character.female_names18,
            surname=description.character.female_names19,
        ),
    )

    def __init__(self, blocks=None):
        super().__init__(blocks)
        self.race_factory = RaceFactory(self.factories)
        self.marks_factory = MarksFactory(self.factories)

    def get_items(self, *args, **kwargs) -> dict:
        """
        :return: Dict with generated data
        """
        values = super().get_items(*args, **kwargs)

        __race = self.race_factory()
        __race_id = self.race_factory.get_race_id(__race)
        __race_blocks = self.factories.get(f"race.{__race_id}")
        __race_factories = __race.factories(NameBlock(*self.data_items.search_values(
            gender_id=self.gender,
            race_id=__race_id,
        )))

        __marks = self.marks_factory()
        __marks_factories = __marks.factories(self.factories)
        blocks = [13, 14, 15, 16, 17]
        marks_values = {item_id: __marks_factories.get_factory(item_id, self.gender)() for item_id in blocks}

        values.update({
            'race': __race,
            'marks': __marks,
        })

        values.update({
            'hair_color': __race_factories.hair_color_factory(),
            'hair_type': __race_factories.hair_type_factory(),
            # 3
            'face_shape': __race_factories.face_shape_factory(),
            # 5
            # 6
            'eyes_color': __race_factories.eyes_color_factory(),
            # 8
            # 9
            'origin': __race_factories.origin_factory(),
            # 11
            # 12: values['marks'],
            13: marks_values[13],
            14: marks_values[14],
            15: marks_values[15],
            16: marks_values[16],
            17: marks_values[17],
            'name': __race_factories.name_factory(),
            'surname': __race_factories.surname_factory(),
            # 20
            # 21: __race,
            # 22
            # 23
            # 24
            # 25
            # 26
            # 27
            # 28
        })
        return values

    def validate(self, items) -> dict:
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
        gender = genders.MALE
        child_class = MaleCharacterDescription
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
        child_class = FemaleCharacterDescription
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
