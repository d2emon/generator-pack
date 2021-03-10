from v1.fixtures import genders
from v1.fixtures.fng import description
from v1.factories.fng.description.character.marks import MarksFactory, add_mark_data
from .common import with_gender


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


def marks():
    mark_m = with_gender(genders.MALE, __default_values, add_mark_data)
    mark_f = with_gender(genders.FEMALE, __default_values, add_mark_data)

    yield from mark_m(
        mark_id=MarksFactory.MARKS,
    )
    yield from mark_m(
        mark_id=MarksFactory.TATTOO,
        mark_start=description.character.tattoo_male_names13,
        mark_middle=description.character.tattoo_male_names14,
        mark_finish=description.character.tattoo_male_names15,
    )
    yield from mark_m(
        mark_id=MarksFactory.TRIBAL_MARK,
        mark_start=description.character.tribal_male_names13,
        mark_middle=description.character.tribal_male_names14,
        mark_finish=description.character.tribal_male_names15,
    )
    yield from mark_m(
        mark_id=MarksFactory.MOLES,
        mark_start=description.character.moles_male_names13,
        mark_middle=description.character.moles_male_names14,
        mark_finish=description.character.moles_male_names15,
        mark_memory=description.character.moles_male_names16,
        mark_subject=description.character.moles_male_names17,
    )
    yield from mark_m(
        mark_id=MarksFactory.FRECKLES,
        mark_start=description.character.freckles_male_names13,
        mark_middle=description.character.freckles_male_names14,
        mark_finish=description.character.freckles_male_names15,
        mark_memory=description.character.freckles_male_names16,
        mark_subject=description.character.freckles_male_names17,
    )
    yield from mark_m(
        mark_id=MarksFactory.SKIN,
        mark_start=description.character.skin_male_names13,
        mark_middle=description.character.skin_male_names14,
        mark_finish=description.character.skin_male_names15,
        mark_memory=description.character.skin_male_names16,
        mark_subject=description.character.skin_male_names17,
    )
    yield from mark_f(
        mark_id=MarksFactory.MARKS,
    )
    yield from mark_f(
        mark_id=MarksFactory.TATTOO,
        mark_start=description.character.tattoo_female_names13,
        mark_middle=description.character.tattoo_female_names14,
        mark_finish=description.character.tattoo_female_names15,
    )
    yield from mark_f(
        mark_id=MarksFactory.TRIBAL_MARK,
        mark_start=description.character.tribal_female_names13,
        mark_middle=description.character.tribal_female_names14,
        mark_finish=description.character.tribal_female_names15,
    )
    yield from mark_f(
        mark_id=MarksFactory.MOLES,
        mark_start=description.character.moles_female_names13,
        mark_middle=description.character.moles_female_names14,
        mark_finish=description.character.moles_female_names15,
        mark_memory=description.character.moles_female_names16,
        mark_subject=description.character.moles_female_names17,
    )
    yield from mark_f(
        mark_id=MarksFactory.FRECKLES,
        mark_start=description.character.freckles_female_names13,
        mark_middle=description.character.freckles_female_names14,
        mark_finish=description.character.freckles_female_names15,
        mark_memory=description.character.freckles_female_names16,
        mark_subject=description.character.freckles_female_names17,
    )
    yield from mark_f(
        mark_id=MarksFactory.SKIN,
        mark_start=description.character.skin_female_names13,
        mark_middle=description.character.skin_female_names14,
        mark_finish=description.character.skin_female_names15,
        mark_memory=description.character.skin_female_names16,
        mark_subject=description.character.skin_female_names17,
    )
