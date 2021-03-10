from v1.fixtures.data_block import NameBlock
from v1.factories.fng.factory import FactoriesBlock
from v1.factories.fng.name_factory import NameFactory
from v1.models.fng.description.character.mark import Mark, MarkDescription


class MarksFactories(FactoriesBlock):
    @property
    def mark_start_factory(self):
        return self.factory('mark_start')

    @property
    def mark_middle_factory(self):
        return self.factory('mark_middle')

    @property
    def mark_finish_factory(self):
        return self.factory('mark_finish')

    @property
    def mark_memory_factory(self):
        return self.factory('mark_memory')

    @property
    def mark_subject_factory(self):
        return self.factory('mark_subject')

    @property
    def description_factory(self):
        return MarkDescription({
            'mark': self.model,  # 12
            'start': self.mark_start_factory(),  # 13
            'middle': self.mark_middle_factory(),  # 14
            'finish': self.mark_finish_factory(),  # 15
            'memory': self.mark_memory_factory(),  # 16
            'subject': self.mark_subject_factory(),  # 17
        })


class MarksFactory(NameFactory):
    MARKS = 1
    TATTOO = 6
    TRIBAL_MARK = 9
    MOLES = 10
    FRECKLES = 11
    SKIN = 12

    child_class = Mark
    blocks_map = {
        12: 12
    }

    @classmethod
    def get_mark_id(cls, value):
        """
        Get child with value

        :param value: Generated value
        :return: Generated child
        """

        if 6 < value.item_id < 9:
            return cls.TATTOO
        elif value.item_id == 9:
            return cls.TRIBAL_MARK
        elif value.item_id == 10:
            return cls.MOLES
        elif value.item_id == 11:
            return cls.FRECKLES
        elif value.item_id > 11:
            return cls.SKIN
        else:
            return cls.MARKS

    @classmethod
    def get_child(cls, value):
        marks = cls.child_class(value.get(12))
        marks.factories = MarksFactories
        return marks


def add_mark_data(
    gender_id,
    mark_id,
    mark_start,
    mark_middle,
    mark_finish,
    mark_memory,
    mark_subject,
):
    return NameBlock().fill(
        # 13
        *mark_start,
        group_id="mark_start",
        gender_id=gender_id,
        mark_id=mark_id,
    ).fill(
        # 14
        *mark_middle,
        group_id="mark_middle",
        gender_id=gender_id,
        mark_id=mark_id,
    ).fill(
        # 15
        *mark_finish,
        group_id="mark_finish",
        gender_id=gender_id,
        mark_id=mark_id,
    ).fill(
        # 16
        *mark_memory,
        group_id="mark_memory",
        gender_id=gender_id,
        mark_id=mark_id,
    ).fill(
        # 17
        *mark_subject,
        group_id="mark_subject",
        gender_id=gender_id,
        mark_id=mark_id,
    ).values
