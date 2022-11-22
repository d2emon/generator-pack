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


Method #1.
    n_ms = ''
    while n_ms == '':
        n_ms = nameFem()


Method #2.
    n_ms = ''
    while n_ms == '':
        n_ms = nameMas()


Method #3.
    n_ms = ''
    while n_ms == '':
        n_ms = next(nm83)


Method #4.
    n_ms = ''
    while n_ms == '':
        n_ms = next(nm84)


Surname.
    lname = ''
    while lname == '':
        lname = nameSur()


return f"{name} {surname}"


function nameMas() {
    if (i < 2) {
        rnd = Math.floor(Math.random() * nm1.length);
        rnd2 = Math.floor(Math.random() * nm2.length);
        rnd3 = Math.floor(Math.random() * nm3.length);
        rnd4 = Math.floor(Math.random() * nm2.length);
        rnd5 = Math.floor(Math.random() * nm4.length);
        nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd5];
    } else if (i < 4) {
        rnd = Math.floor(Math.random() * nm13.length);
        rnd2 = Math.floor(Math.random() * nm14.length);
        rnd3 = Math.floor(Math.random() * nm15.length);
        rnd4 = Math.floor(Math.random() * nm14.length);
        rnd5 = Math.floor(Math.random() * nm16.length);
        if (rnd5 < 3) {
            rnd3 = 0;
        } else {
            while (rnd3 === 0) {
                rnd3 = Math.floor(Math.random() * nm15.length);
            }
        }
        nMs = nm13[rnd] + nm14[rnd2] + nm15[rnd3] + nm14[rnd4] + nm16[rnd5];
    } else if (i < 6) {
        rnd = Math.floor(Math.random() * nm23.length);
        rnd2 = Math.floor(Math.random() * nm24.length);
        rnd5 = Math.floor(Math.random() * nm26.length);
        if (i === 4) {
            rnd3 = Math.floor(Math.random() * nm25.length);
            rnd4 = Math.floor(Math.random() * nm24.length);
            nMs = nm23[rnd] + nm24[rnd2] + nm25[rnd3] + nm24[rnd4] + nm26[rnd5];
        } else {
            nMs = nm23[rnd] + nm24[rnd2] + nm26[rnd5];
        }
    } else if (i < 8) {
        rnd = Math.floor(Math.random() * nm34.length);
        rnd2 = Math.floor(Math.random() * nm35.length);
        rnd5 = Math.floor(Math.random() * nm37.length);
        if (i === 6) {
            rnd3 = Math.floor(Math.random() * nm36.length);
            rnd4 = Math.floor(Math.random() * nm35.length);
            nMs = nm34[rnd] + nm35[rnd2] + nm36[rnd3] + nm35[rnd4] + nm37[rnd5];
        } else {
            nMs = nm34[rnd] + nm35[rnd2] + nm37[rnd5];
        }
    } else if (i < 10) {
        rnd = Math.floor(Math.random() * nm43.length);
        rnd2 = Math.floor(Math.random() * nm44.length);
        rnd3 = Math.floor(Math.random() * nm45.length);
        rnd4 = Math.floor(Math.random() * nm44.length);
        rnd5 = Math.floor(Math.random() * nm46.length);
        if (i === 8) {
            rnd6 = Math.floor(Math.random() * nm45.length);
            rnd7 = Math.floor(Math.random() * nm44.length);
            nMs = nm43[rnd] + nm44[rnd2] + nm45[rnd3] + nm44[rnd4] + nm45[rnd6] + nm44[rnd7]
                + nm46[rnd5];
        } else {
            nMs = nm43[rnd] + nm44[rnd2] + nm45[rnd3] + nm44[rnd4] + nm46[rnd5];
        }
    } else if (i < 12) {
        rnd = Math.floor(Math.random() * nm54.length);
        rnd2 = Math.floor(Math.random() * nm55.length);
        rnd3 = Math.floor(Math.random() * nm56.length);
        rnd4 = Math.floor(Math.random() * nm55.length);
        rnd5 = Math.floor(Math.random() * nm57.length);
        if (i === 10) {
            rnd6 = Math.floor(Math.random() * nm56.length);
            rnd7 = Math.floor(Math.random() * nm55.length);
            nMs = nm54[rnd] + nm55[rnd2] + nm56[rnd3] + nm55[rnd4] + nm56[rnd6] + nm55[rnd7]
                + nm57[rnd5];
        } else {
            nMs = nm54[rnd] + nm55[rnd2] + nm56[rnd3] + nm55[rnd4] + nm57[rnd5];
        }
    } else if (i < 14) {
        rnd = Math.floor(Math.random() * nm65.length);
        rnd2 = Math.floor(Math.random() * nm66.length);
        rnd3 = Math.floor(Math.random() * nm67.length);
        if (rnd3 < 3) {
            while (rnd < 2) {
                rnd = Math.floor(Math.random() * nm65.length);
            }
        }
        nMs = nm65[rnd] + nm66[rnd2] + nm67[rnd3];
    } else {
        rnd = Math.floor(Math.random() * nm73.length);
        rnd2 = Math.floor(Math.random() * nm74.length);
        rnd3 = Math.floor(Math.random() * nm75.length);
        rnd4 = Math.floor(Math.random() * nm74.length);
        rnd5 = Math.floor(Math.random() * nm76.length);
        if (i === 14) {
            rnd6 = Math.floor(Math.random() * nm75.length);
            rnd7 = Math.floor(Math.random() * nm74.length);
            nMs = nm73[rnd] + nm74[rnd2] + nm75[rnd3] + nm74[rnd4] + nm75[rnd6] + nm74[rnd7]
                + nm76[rnd5];
        } else {
            nMs = nm73[rnd] + nm74[rnd2] + nm75[rnd3] + nm74[rnd4] + nm76[rnd5];
        }
    }
    testSwear(nMs);
}
"""

import random
from data.fng.names.pop_culture import dnd
from data.fng.names import fantasy
from genesys.fng.database import Database
from genesys.fng.factories.name_block_factory import MultipleFactoryNameFactory
from genesys.fng.factories.name_factory import ComplexFactory
from genesys.fng.validators import item_is_unique, item_is_not_empty, validate_if
from models.fng.names.fantasy import AlienName
from models.fng.names.name import Name


DB = Database('dnd.human', {
    # 1: fantasy.alien.nm1,
    # 2: fantasy.alien.nm2,
    # 3: fantasy.alien.nm3,
    # 4: fantasy.alien.nm4,

    5: dnd.human.nm5,
    6: dnd.human.nm6,
    7: dnd.human.nm7,
    8: dnd.human.nm8,

    9: dnd.human.nm9,
    10: dnd.human.nm10,
    11: dnd.human.nm11,
    12: dnd.human.nm11,

    # 13

    14: dnd.human.nm14,

    # 15-16

    17: dnd.human.nm17,
    18: dnd.human.nm18,
    19: dnd.human.nm19,
    20: dnd.human.nm20,

    21: dnd.human.nm21,
    22: dnd.human.nm22,

    # 23

    24: dnd.human.nm24,

    # 25-26

    27: dnd.human.nm27,
    28: dnd.human.nm28,
    29: dnd.human.nm29,

    30: dnd.human.nm30,
    31: dnd.human.nm31,
    32: dnd.human.nm32,
    33: dnd.human.nm33,

    # 34-37

    38: dnd.human.nm38,
    39: dnd.human.nm39,
    40: dnd.human.nm40,

    # 41-46

    47: dnd.human.nm47,
    48: dnd.human.nm48,
    49: dnd.human.nm49,

    50: dnd.human.nm50,
    51: dnd.human.nm51,
    52: dnd.human.nm52,
    53: dnd.human.nm53,

    # 54-57

    58: dnd.human.nm58,
    59: dnd.human.nm59,
    60: dnd.human.nm60,
    61: dnd.human.nm61,

    62: dnd.human.nm62,
    63: dnd.human.nm63,
    64: dnd.human.nm64,

    # 65-67

    68: dnd.human.nm68,
    69: dnd.human.nm69,

    70: dnd.human.nm70,
    71: dnd.human.nm71,
    72: dnd.human.nm72,

    # 73-76

    77: dnd.human.nm77,
    78: dnd.human.nm78,
    79: dnd.human.nm79,

    80: dnd.human.nm80,
    81: dnd.human.nm81,
    82: dnd.human.nm82,
})


class BaseNameFactory(ComplexFactory):
    """Base factory for surname."""

    default_data = DB
    model = Name


class Names:
    """
    Summary.

    Raises:
        NotImplementedError: _description_
        NotImplementedError: _description_
        NotImplementedError: _description_
    """

    @classmethod
    def male(cls, subrace=0):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 0.

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError

    @classmethod
    def female(cls, subrace=0):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 0.

        Raises:
            NotImplementedError: _description_
        """
        raise NotImplementedError


# 0-1
class CalashiteNames(Names):
    """
    Summary.

    Args:
        Names (_type_): _description_

    Returns:
        _type_: _description_
    """

    nm1 = dnd.human.nm1
    nm2 = dnd.human.nm2
    nm3 = dnd.human.nm3
    nm4 = dnd.human.nm4

    class SurnameFactory(BaseNameFactory):
        """Method #1."""

        parts = [
            9,
            10,
            11,
            10,
            12,
        ]

    @classmethod
    def male(cls, subrace=0):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 0.

        Returns:
            _type_: _description_
        """
        return "".join([
            random.choice(cls.nm1),
            random.choice(cls.nm2),
            random.choice(cls.nm3),
            random.choice(cls.nm2),
            random.choice(cls.nm4),
        ])

    class FemaleNameFactory1(BaseNameFactory):
        """Method #1."""

        parts = [
            5,
            6,
            7,
            6,
            7,
            6,
            8,
        ]

    class FemaleNameFactory2(BaseNameFactory):
        """Method #1."""

        parts = [
            5,
            6,
            7,
            6,
            8,
        ]


# 2-3
class ChondathanNames(Names):
    """
    Summary.

    Args:
        Names (_type_): _description_

    Returns:
        _type_: _description_
    """

    nm13 = dnd.human.nm13
    nm14 = dnd.human.nm14
    nm15 = dnd.human.nm15
    nm16 = dnd.human.nm16

    nm22 = dnd.human.nm22

    class SurnameFactory(BaseNameFactory):
        """Method #2."""

        parts = [
            21,
            12,
        ]
        validators = {
            1: lambda items: item_is_unique([items[0]]),
        }

    @classmethod
    def male(cls, subrace=2):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 2.

        Returns:
            _type_: _description_
        """
        rnd3 = random.choice(cls.nm15)
        rnd5 = random.choice(cls.nm16)
        if cls.nm16.index(rnd5) < 3:
            rnd3 = cls.nm15[0]
        else:
            while cls.nm15.index(rnd3) == cls.nm15[0]:
                rnd3 = random.choice(cls.nm15)

        return "".join([
            random.choice(cls.nm13),
            random.choice(cls.nm14),
            rnd3,
            random.choice(cls.nm14),
            rnd5,
        ])

    class FemaleNameFactory1(BaseNameFactory):
        """Method #1."""

        parts = [
            17,
            18,
            19,
            18,
            19,
            18,
            20,
        ]

    class FemaleNameFactory2(BaseNameFactory):
        """Method #1."""

        parts = [
            17,
            18,
            19,
            18,
            20,
        ]


# 4-5
class DamaranNames(Names):
    """
    Summary.

    Args:
        Names (_type_): _description_

    Returns:
        _type_: _description_
    """

    nm23 = dnd.human.nm23
    nm25 = dnd.human.nm25
    nm26 = dnd.human.nm26

    class SurnameFactory1(BaseNameFactory):
        """Method #3.1."""

        parts = [
            30,
            31,
            33,
        ]

    class SurnameFactory2(BaseNameFactory):
        """Method #3.2."""

        parts = [
            30,
            31,
            32,
            31,
            33,
        ]

    @classmethod
    def male(cls, subrace=4):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 4.

        Returns:
            _type_: _description_
        """
        if subrace == 4:
            return "".join([
                random.choice(cls.nm23),
                random.choice(cls.nm24),
                random.choice(cls.nm25),
                random.choice(cls.nm24),
                random.choice(cls.nm26),
            ])
        return "".join([
            random.choice(cls.nm23),
            random.choice(cls.nm24),
            random.choice(cls.nm26),
        ])

    class FemaleNameFactory1(BaseNameFactory):
        """Method #1."""

        parts = [
            27,
            24,
            28,
            24,
            29,
        ]

    class FemaleNameFactory2(BaseNameFactory):
        """Method #1."""

        parts = [
            27,
            24,
            29,
        ]


# 6-7
class IlluskanNames(DamaranNames, ChondathanNames):
    """
    Summary.

    Args:
        DamaranNames (_type_): _description_
        ChondathanNames (_type_): _description_

    Returns:
        _type_: _description_
    """

    nm34 = dnd.human.nm34
    nm35 = dnd.human.nm35
    nm36 = dnd.human.nm36
    nm37 = dnd.human.nm37


    class SurnameFactory(BaseNameFactory):
        """Method #4."""

        parts = [
            21,
            22,
        ]
        validators = {
            1: lambda items: item_is_unique([items[0]]),
        }

    @classmethod
    def male(cls, subrace=6):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 6.

        Returns:
            _type_: _description_
        """
        if subrace == 6:
            return "".join([
                random.choice(cls.nm34),
                random.choice(cls.nm35),
                random.choice(cls.nm36),
                random.choice(cls.nm35),
                random.choice(cls.nm37),
            ])
        return "".join([
            random.choice(cls.nm34),
            random.choice(cls.nm35),
            random.choice(cls.nm37),
        ])

    class FemaleNameFactory1(BaseNameFactory):
        """Method #1."""

        parts = [
            38,
            24,
            39,
            24,
            39,
            24,
            40,
        ]

    class FemaleNameFactory2(BaseNameFactory):
        """Method #1."""

        parts = [
            38,
            24,
            39,
            24,
            40,
        ]


# 8-9
class MulanNames(ChondathanNames):
    """
    Summary.

    Args:
        ChondathanNames (_type_): _description_

    Returns:
        _type_: _description_
    """

    nm43 = dnd.human.nm43
    nm44 = dnd.human.nm44
    nm45 = dnd.human.nm45
    nm46 = dnd.human.nm46

    class SurnameFactory1(BaseNameFactory):
        """Method #5.1."""

        parts = [
            50,
            51,
            52,
            51,
            52,
            51,
            53,
        ]

    class SurnameFactory2(BaseNameFactory):
        """Method #5.2."""

        parts = [
            50,
            51,
            52,
            51,
            53,
        ]

    @classmethod
    def male(cls, subrace=8):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 8.

        Returns:
            _type_: _description_
        """
        if subrace == 8:
            return "".join([
                random.choice(cls.nm43),
                random.choice(cls.nm44),
                random.choice(cls.nm45),
                random.choice(cls.nm44),
                random.choice(cls.nm45),
                random.choice(cls.nm44),
                random.choice(cls.nm46),
            ])
        return "".join([
            random.choice(cls.nm43),
            random.choice(cls.nm44),
            random.choice(cls.nm45),
            random.choice(cls.nm44),
            random.choice(cls.nm46),
        ])

    class FemaleNameFactory1(BaseNameFactory):
        """Method #1."""

        parts = [
            47,
            14,
            48,
            14,
            48,
            14,
            49,
        ]

    class FemaleNameFactory2(BaseNameFactory):
        """Method #1."""

        parts = [
            47,
            14,
            48,
            14,
            49,
        ]


# 10-11
class RashemiNames(Names):
    """
    Summary.

    Args:
        Names (_type_): _description_

    Returns:
        _type_: _description_
    """

    nm54 = dnd.human.nm54
    nm55 = dnd.human.nm55
    nm56 = dnd.human.nm56
    nm57 = dnd.human.nm57

    class SurnameFactory1(BaseNameFactory):
        """Method #6."""

        parts = [
            62,
            63,
            64,
            63,
            64,
            63,
            64,
            63,
        ]

    class SurnameFactory2(BaseNameFactory):
        """Method #6."""

        parts = [
            62,
            63,
            64,
            63,
            64,
            63,
        ]

    @classmethod
    def male(cls, subrace=10):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 10.

        Returns:
            _type_: _description_
        """
        if subrace == 10:
            return "".join([
                random.choice(cls.nm54),
                random.choice(cls.nm55),
                random.choice(cls.nm56),
                random.choice(cls.nm55),
                random.choice(cls.nm56),
                random.choice(cls.nm55),
                random.choice(cls.nm57),
            ])
        return "".join([
            random.choice(cls.nm54),
            random.choice(cls.nm55),
            random.choice(cls.nm56),
            random.choice(cls.nm55),
            random.choice(cls.nm57),
        ])

    class FemaleNameFactory1(BaseNameFactory):
        """Method #1."""

        parts = [
            58,
            59,
            60,
            59,
            60,
            59,
            61,
        ]

    class FemaleNameFactory2(BaseNameFactory):
        """Method #1."""

        parts = [
            58,
            59,
            60,
            59,
            61,
        ]


# 12-13
class ShouNames(Names):
    """
    Summary.

    Args:
        Names (_type_): _description_

    Returns:
        _type_: _description_
    """

    nm65 = dnd.human.nm65
    nm66 = dnd.human.nm66
    nm67 = dnd.human.nm67

    class SurnameFactory(BaseNameFactory):
        """Method #7."""

        parts = [
            70,
            71,
            72,
        ]

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

    @classmethod
    def male(cls, subrace=12):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 12.

        Returns:
            _type_: _description_
        """
        rnd1 = random.choice(cls.nm65)
        rnd3 = random.choice(cls.nm67)
        if cls.nm67.index(rnd3) < 3:
            while cls.nm65.index(rnd1) < 2:
                rnd1 = random.choice(cls.nm65)
        return "".join([
            rnd1,
            random.choice(cls.nm66),
            rnd3,
        ])

    class FemaleNameFactory(BaseNameFactory):
        """Method #1."""

        parts = [
            68,
            69,
        ]


# 14-15
class TuramiNames(ChondathanNames):
    """
    Summary.

    Args:
        ChondathanNames (_type_): _description_

    Returns:
        _type_: _description_
    """

    nm73 = dnd.human.nm73
    nm74 = dnd.human.nm74
    nm75 = dnd.human.nm75
    nm76 = dnd.human.nm76

    class TuramiSurnameFactory(ComplexFactory):
        """Method #8."""

        default_data = DB
        model = Name
        parts = [
            80,
            14,
            81,
            14,
            81,
            14,
            82,
        ]

    @classmethod
    def male(cls, subrace=10):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 10.

        Returns:
            _type_: _description_
        """
        if subrace == 14:
            return "".join([
                random.choice(cls.nm73),
                random.choice(cls.nm74),
                random.choice(cls.nm75),
                random.choice(cls.nm74),
                random.choice(cls.nm75),
                random.choice(cls.nm74),
                random.choice(cls.nm76),
            ])
        return "".join([
            random.choice(cls.nm73),
            random.choice(cls.nm74),
            random.choice(cls.nm75),
            random.choice(cls.nm74),
            random.choice(cls.nm76),
        ])

    class FemaleNameFactory1(BaseNameFactory):
        """Method #1."""

        parts = [
            77,
            78,
            79,
            77,
            79,
            77,
        ]

    class FemaleNameFactory2(BaseNameFactory):
        """Method #1."""

        parts = [
            77,
            78,
            79,
            77,
        ]


class OldNames(Names):
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
__SUBRACES = {
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


def __name_male(subrace_id, name_id):
    names = __SUBRACES.get(subrace_id)

    name = names.male(name_id).title()
    surname = names.surname(name_id).title()

    return name + " " + surname


def __name_female(subrace_id, name_id):
    names = __SUBRACES.get(subrace_id)

    name = names.female(name_id).title()
    surname = names.surname(name_id).title()

    return name + " " + surname


def __name_male_old():
    return OldNames.male().title()


def __name_female_old():
    return OldNames.female().title()


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
        return __name_female(subrace_id, name_id)
    elif name_type == 2:
        return __name_male(subrace_id, name_id)
    elif name_type == 3:
        return __name_male_old()
    elif name_type == 4:
        return __name_female_old()
