from utils import genders
from data.fng import description
from .common import add_items, add_items_data


HUMAN = 1
ELF = 3
GNOME = 10
TROLL = 11
ORC = 12
GOBLIN = 13
DWARF = 14
GIANT = 15


def get_race_group_id(item_id):
    if 3 < item_id < 9:
        return ELF
    elif item_id == 10:
        return GNOME
    elif item_id == 11:
        return TROLL
    elif item_id == 12:
        return ORC
    elif item_id == 13:
        return GOBLIN
    elif item_id == 14:
        return DWARF
    elif 15 <= item_id <= 16:
        return GIANT
    else:
        return HUMAN


__default_values = {
    genders.MALE: {
        'hair_color': description.character.male_names1,
        'hair_type': description.character.male_names2,
        'hair_style': description.character.male_names3,
        'face_shape': description.character.male_names4,
        'face_style': description.character.male_names5,
        'eyes_style': description.character.male_names6,
        'eyes_color': description.character.male_names7,
        'eyes_sockets': description.character.male_names8,
        'sight': description.character.male_names9,
        'origin': description.character.male_names10,

        'name': description.character.male_names18,
        'surname': description.character.male_names19,
    },
    genders.FEMALE: {
        'hair_color': description.character.female_names1,
        'hair_type': description.character.female_names2,
        'hair_style': description.character.female_names3,
        'face_shape': description.character.female_names4,
        'face_style': description.character.female_names5,
        'eyes_style': description.character.female_names6,
        'eyes_color': description.character.female_names7,
        'eyes_sockets': description.character.female_names8,
        'sight': description.character.female_names9,
        'origin': description.character.female_names10,

        'name': description.character.female_names18,
        'surname': description.character.female_names19,
    },
}


def __add_race_group_id(item):
    item.values['race_group_id'] = get_race_group_id(item.item_id)
    return item


race_m = add_items('race', genders.MALE, __add_race_group_id)
race_data_m = add_items_data(genders.MALE, __default_values.get(genders.MALE, {}))

race_f = add_items('race', genders.FEMALE, __add_race_group_id)
race_data_f = add_items_data(genders.FEMALE, __default_values.get(genders.FEMALE, {}))


def races():
    __goblin_m = {
        'hair_type': description.character.goblin_male_names2,
        'face_shape': description.character.goblin_male_names4,
        'origin': description.character.goblin_male_names10,
    }
    __goblin_f = {
        'hair_type': description.character.goblin_female_names2,
        'face_shape': description.character.goblin_female_names4,
        'origin': description.character.goblin_female_names10,
    }
    __giant_m = {
        'hair_type': description.character.giant_male_names2,
        'face_shape': description.character.giant_male_names4,
    }
    __giant_f = {
        'hair_type': description.character.giant_female_names2,
        'face_shape': description.character.giant_female_names4,
    }

    yield from race_m(description.character.male_names21)
    yield from race_data_m(race_id=HUMAN)()
    yield from race_data_m(race_id=ELF)(
        hair_color=description.character.elf_male_names1,
        hair_type=description.character.elf_male_names2,
        face_shape=description.character.elf_male_names4,
        eyes_color=description.character.elf_male_names7,
        origin=description.character.elf_male_names10,
        name=description.character.elf_male_names18,
        surname=description.character.elf_male_names19,
    )
    yield from race_data_m(race_id=GNOME)(
        hair_color=description.character.gnome_male_names1,
        hair_type=description.character.gnome_male_names2,
        face_shape=description.character.gnome_male_names4,
        name=description.character.gnome_male_names18,
        surname=description.character.gnome_male_names19,
    )
    yield from race_data_m(race_id=TROLL)(
        **__goblin_m,
        name=description.character.troll_male_names18,
        surname=description.character.troll_male_names19,
    )
    yield from race_data_m(race_id=ORC)(
        **__goblin_m,
        name=description.character.orc_male_names18,
        surname=description.character.orc_male_names19,
    )
    yield from race_data_m(race_id=GOBLIN)(
        **__goblin_m,
        name=description.character.goblin_male_names18,
        surname=description.character.goblin_male_names19,
    )
    yield from race_data_m(race_id=DWARF)(
        **__giant_m,
        name=description.character.dwarf_male_names18,
        surname=description.character.dwarf_male_names19,
    )
    yield from race_data_m(race_id=GIANT)(**__giant_m)

    yield from race_f(description.character.female_names21)
    yield from race_data_f(race_id=HUMAN)()
    yield from race_data_f(race_id=ELF)(
        hair_color=description.character.elf_female_names1,
        hair_type=description.character.elf_female_names2,
        face_shape=description.character.elf_female_names4,
        eyes_color=description.character.elf_female_names7,
        origin=description.character.elf_female_names10,
        name=description.character.elf_female_names18,
        surname=description.character.elf_female_names19,
    )
    yield from race_data_f(race_id=GNOME)(
        hair_color=description.character.gnome_female_names1,
        hair_type=description.character.gnome_female_names2,
        face_shape=description.character.gnome_female_names4,
        name=description.character.gnome_female_names18,
        surname=description.character.gnome_female_names19,
    )
    yield from race_data_f(race_id=TROLL)(
        **__goblin_f,
        name=description.character.troll_female_names18,
        surname=description.character.troll_female_names19,
    )
    yield from race_data_f(race_id=ORC)(
        **__goblin_f,
        name=description.character.orc_female_names18,
        surname=description.character.orc_female_names19,
    )
    yield from race_data_f(race_id=GOBLIN)(
        **__goblin_f,
        name=description.character.goblin_female_names18,
        surname=description.character.goblin_female_names19,
    )
    yield from race_data_f(race_id=DWARF)(
        **__giant_f,
        name=description.character.dwarf_female_names18,
        surname=description.character.dwarf_female_names19,
    )
    yield from race_data_f(race_id=GIANT)(**__giant_f)
