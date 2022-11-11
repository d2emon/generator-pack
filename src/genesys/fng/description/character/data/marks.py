from utils import genders
from data.fng import description
from .common import add_items, add_items_data

MARKS = 1
TATTOO = 6
TRIBAL_MARK = 9
MOLES = 10
FRECKLES = 11
SKIN = 12


def get_mark_group_id(item_id):
    if 6 < item_id < 9:
        return TATTOO
    elif item_id == 9:
        return TRIBAL_MARK
    elif item_id == 10:
        return MOLES
    elif item_id == 11:
        return FRECKLES
    elif item_id > 11:
        return SKIN
    else:
        return MARKS


__default_values = {
    genders.MALE: {
        'mark_start': description.character.male_names13,
        'mark_middle': description.character.male_names14,
        'mark_finish': description.character.male_names15,
        'mark_memory': description.character.male_names16,
        'mark_subject': description.character.male_names17,
    },
    genders.FEMALE: {
        'mark_start': description.character.female_names13,
        'mark_middle': description.character.female_names14,
        'mark_finish': description.character.female_names15,
        'mark_memory': description.character.female_names16,
        'mark_subject': description.character.female_names17,
    },
}


def __add_mark_group_id(item):
    item.values['mark_group_id'] = get_mark_group_id(item.item_id)
    return item


mark_m = add_items('mark', genders.MALE, __add_mark_group_id)
mark_data_m = add_items_data(genders.MALE, __default_values.get(genders.MALE, {}))

mark_f = add_items('mark', genders.FEMALE, __add_mark_group_id)
mark_data_f = add_items_data(genders.FEMALE, __default_values.get(genders.FEMALE, {}))


def marks():
    yield from mark_m(description.character.male_names12)
    yield from mark_data_m(mark_id=MARKS)()
    yield from mark_data_m(mark_id=TATTOO)(
        mark_start=description.character.tattoo_male_names13,
        mark_middle=description.character.tattoo_male_names14,
        mark_finish=description.character.tattoo_male_names15,
    )
    yield from mark_data_m(mark_id=TRIBAL_MARK)(
        mark_start=description.character.tribal_male_names13,
        mark_middle=description.character.tribal_male_names14,
        mark_finish=description.character.tribal_male_names15,
    )
    yield from mark_data_m(mark_id=MOLES)(
        mark_start=description.character.moles_male_names13,
        mark_middle=description.character.moles_male_names14,
        mark_finish=description.character.moles_male_names15,
        mark_memory=description.character.moles_male_names16,
        mark_subject=description.character.moles_male_names17,
    )
    yield from mark_data_m(mark_id=FRECKLES)(
        mark_start=description.character.freckles_male_names13,
        mark_middle=description.character.freckles_male_names14,
        mark_finish=description.character.freckles_male_names15,
        mark_memory=description.character.freckles_male_names16,
        mark_subject=description.character.freckles_male_names17,
    )
    yield from mark_data_m(mark_id=SKIN)(
        mark_start=description.character.skin_male_names13,
        mark_middle=description.character.skin_male_names14,
        mark_finish=description.character.skin_male_names15,
        mark_memory=description.character.skin_male_names16,
        mark_subject=description.character.skin_male_names17,
    )

    yield from mark_f(description.character.female_names12)
    yield from mark_data_f(mark_id=MARKS)()
    yield from mark_data_f(mark_id=TATTOO)(
        mark_start=description.character.tattoo_female_names13,
        mark_middle=description.character.tattoo_female_names14,
        mark_finish=description.character.tattoo_female_names15,
    )
    yield from mark_data_f(mark_id=TRIBAL_MARK)(
        mark_start=description.character.tribal_female_names13,
        mark_middle=description.character.tribal_female_names14,
        mark_finish=description.character.tribal_female_names15,
    )
    yield from mark_data_f(mark_id=MOLES)(
        mark_start=description.character.moles_female_names13,
        mark_middle=description.character.moles_female_names14,
        mark_finish=description.character.moles_female_names15,
        mark_memory=description.character.moles_female_names16,
        mark_subject=description.character.moles_female_names17,
    )
    yield from mark_data_f(mark_id=FRECKLES)(
        mark_start=description.character.freckles_female_names13,
        mark_middle=description.character.freckles_female_names14,
        mark_finish=description.character.freckles_female_names15,
        mark_memory=description.character.freckles_female_names16,
        mark_subject=description.character.freckles_female_names17,
    )
    yield from mark_data_f(mark_id=SKIN)(
        mark_start=description.character.skin_female_names13,
        mark_middle=description.character.skin_female_names14,
        mark_finish=description.character.skin_female_names15,
        mark_memory=description.character.skin_female_names16,
        mark_subject=description.character.skin_female_names17,
    )
