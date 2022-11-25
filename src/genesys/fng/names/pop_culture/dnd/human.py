"""
Human names - Dungeons & Dragons.

This name generator will give you human names fit for the various types of humans in the Dungeons &
Dragons universe.

Just like the real world, humans come in many different shapes, types and sizes. They have
countless different ambitions, dreams, and goals. What they lack in strength they make up for in
determination, and while their hearts may not always be pure, many will do anything to get what
their heart desires. As such, humans could make the perfect or worst party member. They could be a
glorious leader or filthy backstabber. They could do what's best for them or what's best for the
group.

As far as names go, human names are as diverse as humans themselves. I've covered each human race
mentioned in the player handbook (5e): Calashite, Chondathan, Damaran, Illuskan, Mulan, Rashemi,
Shou, and Turami.

You'll probably notice each of these races has names based on existing cultures, but they're often
tweaked enough to be different from the names we use in real life. That doesn't mean you can't
simply use real life names of course, it's a fantasy game in which you make up the world after all.

Old version: This name generator used to be simpler, generating only mostly English sounding names.
If you prefer this type of name, you can still use Old factory.
"""

import random
from data.fng.names.pop_culture import dnd
from genesys.fng.database import Database
from genesys.fng.factories.name_block_factory import MultipleFactoryNameFactory
from genesys.fng.factories.name_factory import ComplexFactory
from genesys.fng.validators import item_is_unique, item_is_not_empty, validate_if
from models.fng.names.name import Name


DB = Database('dnd.human', {
    1: dnd.human.nm1,
    2: dnd.human.nm2,
    3: dnd.human.nm3,
    4: dnd.human.nm4,

    5: dnd.human.nm5,
    6: dnd.human.nm6,
    7: dnd.human.nm7,
    8: dnd.human.nm8,

    9: dnd.human.nm9,
    10: dnd.human.nm10,
    11: dnd.human.nm11,
    12: dnd.human.nm12,

    13: dnd.human.nm13,
    14: dnd.human.nm14,
    15: dnd.human.nm15,
    16: dnd.human.nm16,

    17: dnd.human.nm17,
    18: dnd.human.nm18,
    19: dnd.human.nm19,
    20: dnd.human.nm20,

    21: dnd.human.nm21,
    22: dnd.human.nm22,

    23: dnd.human.nm23,
    24: dnd.human.nm24,
    25: dnd.human.nm25,
    26: dnd.human.nm26,

    27: dnd.human.nm27,
    28: dnd.human.nm28,
    29: dnd.human.nm29,

    30: dnd.human.nm30,
    31: dnd.human.nm31,
    32: dnd.human.nm32,
    33: dnd.human.nm33,

    34: dnd.human.nm34,
    35: dnd.human.nm35,
    36: dnd.human.nm36,
    37: dnd.human.nm37,

    38: dnd.human.nm38,
    39: dnd.human.nm39,
    40: dnd.human.nm40,

    # 41-42

    43: dnd.human.nm43,
    44: dnd.human.nm44,
    45: dnd.human.nm45,
    46: dnd.human.nm46,

    47: dnd.human.nm47,
    48: dnd.human.nm48,
    49: dnd.human.nm49,

    50: dnd.human.nm50,
    51: dnd.human.nm51,
    52: dnd.human.nm52,
    53: dnd.human.nm53,

    54: dnd.human.nm54,
    55: dnd.human.nm55,
    56: dnd.human.nm56,
    57: dnd.human.nm57,

    58: dnd.human.nm58,
    59: dnd.human.nm59,
    60: dnd.human.nm60,
    61: dnd.human.nm61,

    62: dnd.human.nm62,
    63: dnd.human.nm63,
    64: dnd.human.nm64,

    65: dnd.human.nm65,
    66: dnd.human.nm66,
    67: dnd.human.nm67,

    68: dnd.human.nm68,
    69: dnd.human.nm69,

    70: dnd.human.nm70,
    71: dnd.human.nm71,
    72: dnd.human.nm72,

    73: dnd.human.nm73,
    74: dnd.human.nm74,
    75: dnd.human.nm75,
    76: dnd.human.nm76,

    77: dnd.human.nm77,
    78: dnd.human.nm78,
    79: dnd.human.nm79,

    80: dnd.human.nm80,
    81: dnd.human.nm81,
    82: dnd.human.nm82,

    83: dnd.human.nm83,
    84: dnd.human.nm84,
})


class BaseNameFactory(ComplexFactory):
    """Base factory for surname."""

    default_data = DB
    model = Name


class NamesFactory(BaseNameFactory):
    """
    Summary.

    Raises:
        NotImplementedError: _description_
        NotImplementedError: _description_
        NotImplementedError: _description_
    """

    class SurnameFactory(BaseNameFactory):
        pass

    class MaleNameFactory(BaseNameFactory):
        pass

    class FemaleNameFactory(BaseNameFactory):
        pass

    @classmethod
    def get_factories(cls, data):
        """
        Create nested factories.

        Args:
            data (Database): Database for nested factories.

        Returns:
            dict[Factory]: Nested factories.
        """
        return {
            'surname': cls.SurnameFactory(data),
            'male': cls.MaleNameFactory(data),
            'female': cls.FemaleNameFactory(data),
        }


# 0-1
class CalashiteNames(NamesFactory):
    """
    Summary.

    Args:
        Names (_type_): _description_

    Returns:
        _type_: _description_
    """

    class SurnameFactory(BaseNameFactory):
        """Method #1."""

        parts = [9, 10, 11, 10, 12]

    class MaleNameFactory(BaseNameFactory):
        """Method #1."""

        parts = [1, 2, 3, 2, 4]

    class FemaleNameFactory(BaseNameFactory, MultipleFactoryNameFactory):
        class FemaleNameFactory1(BaseNameFactory):
            """Method #1."""

            parts = [5, 6, 7, 6, 7, 6, 8]

        class FemaleNameFactory2(BaseNameFactory):
            """Method #2."""

            parts = [5, 6, 7, 6, 8]

        factory_classes = [
            FemaleNameFactory1,
            FemaleNameFactory2,
        ]

# 2-3
class ChondathanNames(NamesFactory):
    """
    Summary.

    Args:
        Names (_type_): _description_

    Returns:
        _type_: _description_
    """

    class SurnameFactory(BaseNameFactory):
        """Method #2."""

        parts = [21, 12]
        validators = {
            1: lambda items: item_is_unique([items[0]]),
        }

    class MaleNameFactory(BaseNameFactory):
        """Method #1."""

        parts = [13, 14, 15, 14, 16]

        def chondathan_name_validator(items):
            """
            Check if item is not unique

            :param unique_with: Values to check
            :return: Item validator
            """

            def f(item):
                if items[4].item_id >= 3:
                    return item.item_id != 0

            return f

        validators = {
            2: chondathan_name_validator,
        }

        update_values = {
            2: lambda self, items: '' if items[4].item_id < 3 else items[2],
        }

    class FemaleNameFactory(BaseNameFactory, MultipleFactoryNameFactory):
        class FemaleNameFactory1(BaseNameFactory):
            """Method #1."""

            parts = [17, 18, 19, 18, 19, 18, 20]

        class FemaleNameFactory2(BaseNameFactory):
            """Method #2."""

            parts = [17, 18, 19, 18, 20]

        factory_classes = [
            FemaleNameFactory1,
            FemaleNameFactory2,
        ]


# 4-5
class DamaranNames(NamesFactory):
    """
    Summary.

    Args:
        Names (_type_): _description_

    Returns:
        _type_: _description_
    """

    class SurnameFactory(BaseNameFactory, MultipleFactoryNameFactory):
        class SurnameFactory1(BaseNameFactory):
            """Method #3.1."""

            parts = [30, 31, 33]

        class SurnameFactory2(BaseNameFactory):
            """Method #3.2."""

            parts = [30, 31, 32, 31, 33]

        factory_classes = [
            SurnameFactory1,
            SurnameFactory2,
        ]

    class MaleNameFactory(BaseNameFactory, MultipleFactoryNameFactory):
        class MaleNameFactory1(BaseNameFactory):
            """Method #1."""

            parts = [23, 24, 26]

        class MaleNameFactory2(BaseNameFactory):
            """Method #2."""

            parts = [23, 24, 25, 24, 26]

        factory_classes = [
            MaleNameFactory1,
            MaleNameFactory2,
        ]

    class FemaleNameFactory(BaseNameFactory, MultipleFactoryNameFactory):
        class FemaleNameFactory1(BaseNameFactory):
            """Method #1."""

            parts = [27, 24, 28, 24, 29]

        class FemaleNameFactory2(BaseNameFactory):
            """Method #2."""

            parts = [27, 24, 29]

        factory_classes = [
            FemaleNameFactory1,
            FemaleNameFactory2,
        ]


# 6-7
class IlluskanNames(NamesFactory):
    """
    Summary.

    Args:
        DamaranNames (_type_): _description_
        ChondathanNames (_type_): _description_

    Returns:
        _type_: _description_
    """

    class SurnameFactory(BaseNameFactory):
        """Method #4."""

        parts = [21, 22]

        validators = {
            1: lambda items: item_is_unique([items[0]]),
        }

    class MaleNameFactory(BaseNameFactory, MultipleFactoryNameFactory):
        class MaleNameFactory1(BaseNameFactory):
            """Method #1."""

            parts = [34, 35, 36, 35, 37]

        class MaleNameFactory2(BaseNameFactory):
            """Method #2."""

            parts = [34, 35, 37]

        factory_classes = [
            MaleNameFactory1,
            MaleNameFactory2,
        ]

    class FemaleNameFactory(BaseNameFactory, MultipleFactoryNameFactory):
        class FemaleNameFactory1(BaseNameFactory):
            """Method #1."""

            parts = [38, 24, 39, 24, 39, 24, 40]

        class FemaleNameFactory2(BaseNameFactory):
            """Method #2."""

            parts = [38, 24, 39, 24, 40]

        factory_classes = [
            FemaleNameFactory1,
            FemaleNameFactory2,
        ]


# 8-9
class MulanNames(NamesFactory):
    """
    Summary.

    Args:
        ChondathanNames (_type_): _description_

    Returns:
        _type_: _description_
    """

    class SurnameFactory(BaseNameFactory, MultipleFactoryNameFactory):
        class SurnameFactory1(BaseNameFactory):
            """Method #5.1."""

            parts = [50, 51, 52, 51, 52, 51, 53]

        class SurnameFactory2(BaseNameFactory):
            """Method #5.2."""

            parts = [50, 51, 52, 51, 53]

        factory_classes = [
            SurnameFactory1,
            SurnameFactory2,
        ]

    class MaleNameFactory(BaseNameFactory, MultipleFactoryNameFactory):
        class MaleNameFactory1(BaseNameFactory):
            """Method #1."""

            parts = [43, 44, 45, 44, 45, 44, 46]

        class MaleNameFactory2(BaseNameFactory):
            """Method #2."""

            parts = [43, 44, 45, 44, 46]

        factory_classes = [
            MaleNameFactory1,
            MaleNameFactory2,
        ]

    class FemaleNameFactory(BaseNameFactory, MultipleFactoryNameFactory):
        class FemaleNameFactory1(BaseNameFactory):
            """Method #1."""

            parts = [47, 14, 48, 14, 48, 14, 49]

        class FemaleNameFactory2(BaseNameFactory):
            """Method #2."""

            parts = [47, 14, 48, 14, 49]

        factory_classes = [
            FemaleNameFactory1,
            FemaleNameFactory2,
        ]


# 10-11
class RashemiNames(NamesFactory):
    """
    Summary.

    Args:
        Names (_type_): _description_

    Returns:
        _type_: _description_
    """

    class SurnameFactory(BaseNameFactory, MultipleFactoryNameFactory):
        class SurnameFactory1(BaseNameFactory):
            """Method #6."""

            parts = [62, 63, 64, 63, 64, 63, 64, 63]

        class SurnameFactory2(BaseNameFactory):
            """Method #6."""

            parts = [62, 63, 64, 63, 64, 63]

        factory_classes = [
            SurnameFactory1,
            SurnameFactory2,
        ]

    class MaleNameFactory(BaseNameFactory, MultipleFactoryNameFactory):
        class MaleNameFactory1(BaseNameFactory):
            """Method #1."""

            parts = [54, 55, 56, 55, 56, 55, 57]

        class MaleNameFactory2(BaseNameFactory):
            """Method #2."""

            parts = [54, 55, 56, 55, 57]

        factory_classes = [
            MaleNameFactory1,
            MaleNameFactory2,
        ]

    class FemaleNameFactory(BaseNameFactory, MultipleFactoryNameFactory):
        class FemaleNameFactory1(BaseNameFactory):
            """Method #1."""

            parts = [58, 59, 60, 59, 60, 59, 61]

        class FemaleNameFactory2(BaseNameFactory):
            """Method #2."""

            parts = [58, 59, 60, 59, 61]

        factory_classes = [
            FemaleNameFactory1,
            FemaleNameFactory2,
        ]


# 12-13
class ShouNames(NamesFactory):
    """
    Summary.

    Args:
        Names (_type_): _description_

    Returns:
        _type_: _description_
    """

    class SurnameFactory(BaseNameFactory):
        """Method #7."""

        parts = [70, 71, 72]

        def shou_surname_validator(items):
            """
            Check if item is not unique

            :param unique_with: Values to check
            :return: Item validator
            """

            def f(item):
                if items[2].item_id < 3:
                    return item.item_id >= 3

            return f

        validators = {
            1: shou_surname_validator,
        }

    class MaleNameFactory(BaseNameFactory):
        """Method #1."""

        parts = [65, 66, 67]

        def shou_name_validator(items):
            """
            Check if item is not unique

            :param unique_with: Values to check
            :return: Item validator
            """

            def f(item):
                if items[2].item_id < 3:
                    return item.item_id >= 2

            return f

        validators = {
            1: shou_name_validator,
        }

    class FemaleNameFactory(BaseNameFactory):
        """Method #1."""

        parts = [68, 69]


# 14-15
class TuramiNames(NamesFactory):
    """
    Summary.

    Args:
        ChondathanNames (_type_): _description_

    Returns:
        _type_: _description_
    """

    class TuramiSurnameFactory(ComplexFactory):
        """Method #8."""

        parts = [80, 14, 81, 14, 81, 14, 82]

    class MaleNameFactory(BaseNameFactory, MultipleFactoryNameFactory):
        class MaleNameFactory1(BaseNameFactory):
            """Method #1."""

            parts = [73, 74, 75, 74, 75, 74, 76]

        class MaleNameFactory2(BaseNameFactory):
            """Method #2."""

            parts = [73, 74, 75, 74, 76]

        factory_classes = [
            MaleNameFactory1,
            MaleNameFactory2,
        ]

    class FemaleNameFactory(BaseNameFactory, MultipleFactoryNameFactory):
        class FemaleNameFactory1(BaseNameFactory):
            """Method #1."""

            parts = [77, 78, 79, 77, 79, 77]

        class FemaleNameFactory2(BaseNameFactory):
            """Method #2."""

            parts = [77, 78, 79, 77]

        factory_classes = [
            FemaleNameFactory1,
            FemaleNameFactory2,
        ]


class OldNames(NamesFactory):
    """
    Summary.

    Args:
        Names (_type_): _description_

    Raises:
        NotImplementedError: _description_

    Returns:
        _type_: _description_
    """

    nm83 = dnd.human.nm83
    nm84 = dnd.human.nm84

    @classmethod
    def surname(cls, surname=0):
        """
        Summary.

        Args:
            surname (int, optional): _description_. Defaults to 0.

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError

    @classmethod
    def female(cls, surname=0):
        """
        Summary.

        Args:
            surname (int, optional): _description_. Defaults to 0.

        Returns:
            _type_: _description_
        """
        return random.choice(cls.nm84)

    @classmethod
    def male(cls, surname=0):
        """
        Summary.

        Args:
            surname (int, optional): _description_. Defaults to 0.

        Returns:
            _type_: _description_
        """
        return random.choice(cls.nm83)


# 0-1 Calashite
# 2-3 Chondathan
# 4-5 Damaran
# 6-7 Illuskan (Chondathan)
# 8-9 Mulan
# 10-11 Rashemi
# 12-13 Shou
# 14-15 Turami
SUBRACES = {
    0: TuramiNames,
    1: CalashiteNames,
    2: ChondathanNames,
    3: DamaranNames,
    4: IlluskanNames,
    5: MulanNames,
    6: RashemiNames,
    7: ShouNames,
}


def names_list(subrace_id):
    """
    Summary.

    Args:
        subrace_id (_type_): _description_

    Returns:
        _type_: _description_
    """
    if subrace_id < 2:
        return CalashiteNames
    elif subrace_id < 4:
        return ChondathanNames
    elif subrace_id < 6:
        return DamaranNames
    elif subrace_id < 8:
        return IlluskanNames
    elif subrace_id < 10:
        return MulanNames
    elif subrace_id < 12:
        return RashemiNames
    elif subrace_id < 14:
        return ShouNames
    return TuramiNames


class __BaseNameFactory:
    model = Name

    def factory(self, subrace_id=None):
        if subrace_id is None:
            subrace_id = random.randrange(7)

        names_factory = SUBRACES.get(subrace_id)
        names = names_factory()
        return names

    def name(self, names):
        factory = names.factory('male')
        return factory()

    def surname(self, names):
        factory = names.factory('surname')
        return factory()

    def __call__(self, *args, subrace_id=None, **kwargs):
        names = self.factory(subrace_id)
        name = self.name(names)
        surname = self.surname(names)
        return self.model(value=f"{name} {surname}", built_with=names)


class __MaleNameFactory(__BaseNameFactory):

    def name(self, names):
        factory = names.factory('male')
        return factory()


class __FemaleNameFactory(__BaseNameFactory):

    def name(self, names):
        factory = names.factory('female')
        return factory()


def name_male(subrace_id=None):
    return __MaleNameFactory()


def name_female(subrace_id=None):
    return __FemaleNameFactory()


def name_male_old():
    return OldNames.male


def name_female_old():
    return OldNames.female


def name_gen(name_type=0, name_id=0):
    """
    Summary.

    Args:
        name_type (int, optional): _description_. Defaults to 0.

    Yields:
        _type_: _description_
    """

    subrace_id = int(name_id / 2)

    if name_type == 1:
        return name_female(subrace_id, name_id)
    elif name_type == 2:
        return name_male(subrace_id, name_id)
    elif name_type == 3:
        return name_male_old()
    elif name_type == 4:
        return name_female_old()
