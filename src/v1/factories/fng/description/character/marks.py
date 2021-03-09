from v1.fixtures.genders import MALE, FEMALE
from v1.factories.fng.name_factory import NameFactory
from v1.models.fng.description.character.mark import Mark


class MarksFactories:
    male = {
        13: 'male_names13',
        14: 'male_names14',
        15: 'male_names15',
        16: 'male_names16',
        17: 'male_names17',
    }
    female = {
        13: 'female_names13',
        14: 'female_names14',
        15: 'female_names15',
        16: 'female_names16',
        17: 'female_names17',
    }

    def __init__(self, blocks):
        self.blocks = blocks

    def get_blocks_map_by_gender(self, gender=MALE):
        if gender == MALE:
            return self.male
        elif gender == FEMALE:
            return self.female
        else:
            return {}

    def get_factory_class(self, factory_id, gender=MALE):
        blocks_map = self.get_blocks_map_by_gender(gender)
        block_id = blocks_map.get(factory_id)
        return self.blocks.get(block_id)

    def get_factory(self, blocks, factory_id, gender=MALE):
        factory = self.get_factory_class(factory_id, gender)
        if factory is None:
            return lambda: None
        else:
            return factory(blocks)


class TattooFactories(MarksFactories):
    male = {
        13: 'tattoo_male_names13',
        14: 'tattoo_male_names14',
        15: 'tattoo_male_names15',
        16: 'male_names16',
        17: 'male_names17',
    }
    female = {
        13: 'tattoo_female_names13',
        14: 'tattoo_female_names14',
        15: 'tattoo_female_names15',
        16: 'female_names16',
        17: 'female_names17',
    }


class TribalMarkFactories(MarksFactories):
    male = {
        13: 'tribal_male_names13',
        14: 'tribal_male_names14',
        15: 'tribal_male_names15',
        16: 'male_names16',
        17: 'male_names17',
    }
    female = {
        13: 'tribal_female_names13',
        14: 'tribal_female_names14',
        15: 'tribal_female_names15',
        16: 'female_names16',
        17: 'female_names17',
    }


class MolesFactories(MarksFactories):
    male = {
        13: 'moles_male_names13',
        14: 'moles_male_names14',
        15: 'moles_male_names15',
        16: 'moles_male_names16',
        17: 'moles_male_names17',
    }
    female = {
        13: 'moles_female_names13',
        14: 'moles_female_names14',
        15: 'moles_female_names15',
        16: 'moles_female_names16',
        17: 'moles_female_names17',
    }


class FrecklesFactories(MarksFactories):
    male = {
        13: 'freckles_male_names13',
        14: 'freckles_male_names14',
        15: 'freckles_male_names15',
        16: 'freckles_male_names16',
        17: 'freckles_male_names17',
    }
    female = {
        13: 'freckles_female_names13',
        14: 'freckles_female_names14',
        15: 'freckles_female_names15',
        16: 'freckles_female_names16',
        17: 'freckles_female_names17',
    }


class SkinFactories(MarksFactories):
    male = {
        13: 'skin_male_names13',
        14: 'skin_male_names14',
        15: 'skin_male_names15',
        16: 'skin_male_names16',
        17: 'skin_male_names17',
    }
    female = {
        13: 'skin_female_names13',
        14: 'skin_female_names14',
        15: 'skin_female_names15',
        16: 'skin_female_names16',
        17: 'skin_female_names17',
    }


class MarksFactory(NameFactory):
    child_class = Mark
    blocks_map = {
        12: 12
    }

    @classmethod
    def get_child(cls, value):
        """
        Get child with value

        :param value: Generated value
        :return: Generated child
        """
        marks = cls.child_class(value.get(12))

        if 6 < marks.item_id < 9:
            marks.factories = TattooFactories
        elif marks.item_id == 9:
            marks.factories = TribalMarkFactories
        elif marks.item_id == 10:
            marks.factories = MolesFactories
        elif marks.item_id == 11:
            marks.factories = FrecklesFactories
        elif marks.item_id > 11:
            marks.factories = SkinFactories
        else:
            marks.factories = MarksFactories

        return marks
