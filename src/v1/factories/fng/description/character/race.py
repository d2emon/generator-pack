from v1.fixtures.data_block import NameBlock
from v1.factories.fng.factory import FactoriesBlock
from v1.factories.fng.name_factory import NameFactory
from v1.models.fng.description import Race, Hair, Face, Eyes, Name


class RaceFactories(FactoriesBlock):
    HUMAN = 1
    ELF = 3
    GNOME = 10
    TROLL = 11
    ORC = 12
    GOBLIN = 13
    DWARF = 14
    GIANT = 15

    def __init__(self, model, blocks):
        super().__init__(model, blocks.filtered(
            race_id=model.race_group_id,
        ))

    @property
    def hair_color_factory(self):
        return self.factory('hair_color')

    @property
    def hair_type_factory(self):
        return self.factory('hair_type')

    @property
    def hair_style_factory(self):
        return self.factory('hair_style')

    @property
    def face_shape_factory(self):
        return self.factory('face_shape')

    @property
    def face_style_factory(self):
        return self.factory('face_style')

    @property
    def eyes_style_factory(self):
        return self.factory('eyes_style')

    @property
    def eyes_color_factory(self):
        return self.factory('eyes_color')

    @property
    def eyes_sockets_factory(self):
        return self.factory('eyes_sockets')

    @property
    def sight_factory(self):
        return self.factory('sight')

    @property
    def origin_factory(self):
        return self.factory('origin')

    @property
    def name_factory(self):
        return self.factory('name')

    @property
    def surname_factory(self):
        return self.factory('surname')

    @property
    def hair_factory(self):
        def f(*args, gender_id=None, **kwargs):
            return Hair({
                'color': self.hair_color_factory(gender_id=gender_id),  # 1
                'hair_type': self.hair_type_factory(gender_id=gender_id),  # 2
                'style': self.hair_style_factory(gender_id=gender_id),  # 3
            })
        return f

    @property
    def face_factory(self):
        def f(*args, gender_id=None, **kwargs):
            return Face({
                'shape': self.face_shape_factory(gender_id=gender_id),  # 4
                'style': self.face_style_factory(gender_id=gender_id),  # 5
            })
        return f

    @property
    def eyes_factory(self):
        def f(*args, gender_id=None, **kwargs):
            return Eyes({
                'style': self.eyes_style_factory(gender_id=gender_id),  # 6
                'color': self.eyes_color_factory(gender_id=gender_id),  # 7
                'sockets': self.eyes_sockets_factory(gender_id=gender_id),  # 8
                'sight': self.sight_factory(gender_id=gender_id),  # 9
            })
        return f

    @property
    def character_name_factory(self):
        def f(*args, gender_id=None, **kwargs):
            return Name({
                'name': self.name_factory(gender_id=gender_id),  # 18
                'surname': self.surname_factory(gender_id=gender_id),  # 19
            })
        return f


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
        'value': 21
    }

    @classmethod
    def get_race_group_id(cls, value):
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

    def get_value(self, *args, **kwargs):
        value = super().get_value(*args, **kwargs)
        return value.get('value')

    def get_child(self, value):
        """
        Get child with value

        :param value: Generated value
        :return: Generated child
        """
        item = self.child_class(
            value,
            race_group_id=self.get_race_group_id(value),
        )
        item.factories = RaceFactories(
            item,
            self.data_blocks,
        )
        return item
