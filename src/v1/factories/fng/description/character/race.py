from v1.fixtures.data_block import NameBlock
from v1.factories.fng.factory import DataFactory
from v1.factories.fng.name_factory import NameFactory
from v1.models.fng.description.character.race import Race


class RaceFactories:
    def __init__(self, blocks):
        self.blocks = blocks

    def factory(self, factory_id):
        values = self.blocks.search_values(group_id=factory_id)
        return DataFactory(NameBlock(*values))

    @property
    def hair_color_factory(self):
        return self.factory('hair_color')

    @property
    def hair_type_factory(self):
        return self.factory('hair_type')

    @property
    def face_shape_factory(self):
        return self.factory('face_shape')

    @property
    def eyes_color_factory(self):
        return self.factory('eyes_color')

    @property
    def origin_factory(self):
        return self.factory('origin')

    @property
    def name_factory(self):
        return self.factory('name')

    @property
    def surname_factory(self):
        return self.factory('surname')


class RaceFactory(NameFactory):
    HUMAN = 1
    ELF = 3
    GNOME = 10
    TROLL = 11
    ORC = 12
    GOBLIN = 13
    DWARF = 14
    GIANT = 15

    child_class = Race
    blocks_map = {
        21: 21
    }

    @classmethod
    def get_race_id(cls, value):
        """
        Get child with value

        :param value: Generated value
        :return: Generated child
        """
        if 3 < value.item_id < 9:
            return cls.ELF
        elif value.item_id == 10:
            return cls.GNOME
        elif value.item_id == 11:
            return cls.TROLL
        elif value.item_id == 12:
            return cls.ORC
        elif value.item_id == 13:
            return cls.GOBLIN
        elif value.item_id == 14:
            return cls.DWARF
        elif 15 <= value.item_id <= 16:
            return cls.GIANT
        else:
            return cls.HUMAN

    @classmethod
    def get_child(cls, value):
        """
        Get child with value

        :param value: Generated value
        :return: Generated child
        """
        race = cls.child_class(value.get(21))
        race.factories = RaceFactories
        return race
