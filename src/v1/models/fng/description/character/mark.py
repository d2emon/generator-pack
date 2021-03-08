from v1.fixtures.fng.description import character


class Mark:
    def __init__(self, mark_id, name):
        self.mark_id = mark_id
        self.name = name

    @property
    def male(self):
        return {
            13: character.male_names13,
            14: character.male_names14,
            15: character.male_names15,
            16: character.male_names16,
            17: character.male_names17,
        }

    @property
    def female(self):
        return {
            13: character.female_names13,
            14: character.female_names14,
            15: character.female_names15,
            16: character.female_names16,
            17: character.female_names17,
        }


class Tattoo(Mark):
    @property
    def male(self):
        return {
            13: character.tattoo_male_names13,
            14: character.tattoo_male_names14,
            15: character.tattoo_male_names15,
            16: character.male_names16,
            17: character.male_names17,
        }

    @property
    def female(self):
        return {
            13: character.tattoo_female_names13,
            14: character.tattoo_female_names14,
            15: character.tattoo_female_names15,
            16: character.female_names16,
            17: character.female_names17,
        }


class TribalMark(Mark):
    @property
    def male(self):
        return {
            13: character.tribal_male_names13,
            14: character.tribal_male_names14,
            15: character.tribal_male_names15,
            16: character.male_names16,
            17: character.male_names17,
        }

    @property
    def female(self):
        return {
            13: character.tribal_female_names13,
            14: character.tribal_female_names14,
            15: character.tribal_female_names15,
            16: character.female_names16,
            17: character.female_names17,
        }


class Moles(Mark):
    @property
    def male(self):
        return {
            13: character.moles_male_names13,
            14: character.moles_male_names14,
            15: character.moles_male_names15,
            16: character.moles_male_names16,
            17: character.moles_male_names17,
        }

    @property
    def female(self):
        return {
            13: character.moles_female_names13,
            14: character.moles_female_names14,
            15: character.moles_female_names15,
            16: character.moles_female_names16,
            17: character.moles_female_names17,
        }


class Freckles(Mark):
    @property
    def male(self):
        return {
            13: character.freckles_male_names13,
            14: character.freckles_male_names14,
            15: character.freckles_male_names15,
            16: character.freckles_male_names16,
            17: character.freckles_male_names17,
        }

    @property
    def female(self):
        return {
            13: character.freckles_female_names13,
            14: character.freckles_female_names14,
            15: character.freckles_female_names15,
            16: character.freckles_female_names16,
            17: character.freckles_female_names17,
        }


class Skin(Mark):
    @property
    def male(self):
        return {
            13: character.skin_male_names13,
            14: character.skin_male_names14,
            15: character.skin_male_names15,
            16: character.skin_male_names16,
            17: character.skin_male_names17,
        }

    @property
    def female(self):
        return {
            13: character.skin_female_names13,
            14: character.skin_female_names14,
            15: character.skin_female_names15,
            16: character.skin_female_names16,
            17: character.skin_female_names17,
        }


def get_mark(data):
    item_id = data.item_id

    if 6 < item_id < 9:
        mark = Tattoo
    elif item_id == 9:
        mark = TribalMark
    elif item_id == 10:
        mark = Moles
    elif item_id == 11:
        mark = Freckles
    elif item_id > 11:
        mark = Skin
    else:
        mark = Mark

    return mark(item_id, data.value)
