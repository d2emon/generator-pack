"""Human names for DnD."""

import random
from data.fng.names.pop_culture import dnd


def test_swear(name):
    """
    Summary.

    Args:
        name (_type_): _description_

    Returns:
        _type_: _description_
    """
    return name


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

    @classmethod
    def surname(cls, subrace=0):
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

    nm5 = dnd.human.nm5
    nm6 = dnd.human.nm6
    nm7 = dnd.human.nm7
    nm8 = dnd.human.nm8

    nm9 = dnd.human.nm9
    nm10 = dnd.human.nm10
    nm11 = dnd.human.nm11
    nm12 = dnd.human.nm12

    @classmethod
    def surname(cls, subrace=0):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 0.

        Returns:
            _type_: _description_
        """
        return "".join([
            random.choice(cls.nm9),
            random.choice(cls.nm10),
            random.choice(cls.nm11),
            random.choice(cls.nm10),
            random.choice(cls.nm12),
        ])

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

    @classmethod
    def female(cls, subrace=0):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 0.

        Returns:
            _type_: _description_
        """
        if subrace == 0:
            return "".join([
                random.choice(cls.nm5),
                random.choice(cls.nm6),
                random.choice(cls.nm7),
                random.choice(cls.nm6),
                random.choice(cls.nm7),
                random.choice(cls.nm6),
                random.choice(cls.nm8),
            ])
        return "".join([
            random.choice(cls.nm5),
            random.choice(cls.nm6),
            random.choice(cls.nm7),
            random.choice(cls.nm6),
            random.choice(cls.nm8),
        ])


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

    nm17 = dnd.human.nm17
    nm18 = dnd.human.nm18
    nm19 = dnd.human.nm19
    nm20 = dnd.human.nm20

    nm21 = dnd.human.nm21
    nm22 = dnd.human.nm22

    @classmethod
    def surname(cls, subrace=2):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 2.

        Returns:
            _type_: _description_
        """
        rnd1 = random.choice(cls.nm21)
        rnd2 = rnd1
        while rnd2 == rnd1:
            rnd2 = random.choice(cls.nm22)
        return "".join([rnd1, rnd2])

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

    @classmethod
    def female(cls, subrace=2):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 2.

        Returns:
            _type_: _description_
        """
        if subrace == 2:
            return "".join([
                random.choice(cls.nm17),
                random.choice(cls.nm18),
                random.choice(cls.nm19),
                random.choice(cls.nm18),
                random.choice(cls.nm19),
                random.choice(cls.nm18),
                random.choice(cls.nm20),
            ])
        return "".join([
            random.choice(cls.nm17),
            random.choice(cls.nm18),
            random.choice(cls.nm19),
            random.choice(cls.nm18),
            random.choice(cls.nm20),
        ])


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
    nm24 = dnd.human.nm24
    nm25 = dnd.human.nm25
    nm26 = dnd.human.nm26

    nm27 = dnd.human.nm27
    nm28 = dnd.human.nm28
    nm29 = dnd.human.nm29

    nm30 = dnd.human.nm30
    nm31 = dnd.human.nm31
    nm32 = dnd.human.nm32
    nm33 = dnd.human.nm33

    @classmethod
    def surname(cls, subrace=4):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 4.

        Returns:
            _type_: _description_
        """
        if subrace == 4:
            return "".join([
                random.choice(cls.nm30),
                random.choice(cls.nm31),
                random.choice(cls.nm33),
            ])
        return "".join([
            random.choice(cls.nm30),
            random.choice(cls.nm31),
            random.choice(cls.nm32),
            random.choice(cls.nm31),
            random.choice(cls.nm33),
        ])

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

    @classmethod
    def female(cls, subrace=4):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 4.

        Returns:
            _type_: _description_
        """
        if subrace == 4:
            return "".join([
                random.choice(cls.nm27),
                random.choice(cls.nm24),
                random.choice(cls.nm28),
                random.choice(cls.nm24),
                random.choice(cls.nm29),
            ])
        return "".join([
            random.choice(cls.nm27),
            random.choice(cls.nm24),
            random.choice(cls.nm29),
        ])


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

    nm38 = dnd.human.nm38
    nm39 = dnd.human.nm39
    nm40 = dnd.human.nm40

    @classmethod
    def surname(cls, subrace=0):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 0.

        Returns:
            _type_: _description_
        """
        rnd1 = random.choice(cls.nm21)
        rnd2 = rnd1
        while rnd2 == rnd1:
            rnd2 = random.choice(cls.nm22)
        return "".join([rnd1, rnd2])

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

    @classmethod
    def female(cls, subrace=6):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 6.

        Returns:
            _type_: _description_
        """
        if subrace == 6:
            return "".join([
                random.choice(cls.nm38),
                random.choice(cls.nm24),
                random.choice(cls.nm39),
                random.choice(cls.nm24),
                random.choice(cls.nm39),
                random.choice(cls.nm24),
                random.choice(cls.nm40),
            ])
        return "".join([
            random.choice(cls.nm38),
            random.choice(cls.nm24),
            random.choice(cls.nm39),
            random.choice(cls.nm24),
            random.choice(cls.nm40),
        ])


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

    nm47 = dnd.human.nm47
    nm48 = dnd.human.nm48
    nm49 = dnd.human.nm49

    nm50 = dnd.human.nm50
    nm51 = dnd.human.nm51
    nm52 = dnd.human.nm52
    nm53 = dnd.human.nm53

    @classmethod
    def surname(cls, subrace=8):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 8.

        Returns:
            _type_: _description_
        """
        if subrace == 8:
            return "".join([
                random.choice(cls.nm50),
                random.choice(cls.nm51),
                random.choice(cls.nm52),
                random.choice(cls.nm51),
                random.choice(cls.nm52),
                random.choice(cls.nm51),
                random.choice(cls.nm53),
            ])
        return "".join([
            random.choice(cls.nm50),
            random.choice(cls.nm51),
            random.choice(cls.nm52),
            random.choice(cls.nm51),
            random.choice(cls.nm53),
        ])

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

    @classmethod
    def female(cls, subrace=8):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 8.

        Returns:
            _type_: _description_
        """
        if subrace == 8:
            return "".join([
                random.choice(cls.nm47),
                random.choice(cls.nm14),
                random.choice(cls.nm48),
                random.choice(cls.nm14),
                random.choice(cls.nm48),
                random.choice(cls.nm14),
                random.choice(cls.nm49),
            ])
        return "".join([
            random.choice(cls.nm47),
            random.choice(cls.nm14),
            random.choice(cls.nm48),
            random.choice(cls.nm14),
            random.choice(cls.nm49),
        ])


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

    nm58 = dnd.human.nm58
    nm59 = dnd.human.nm59
    nm60 = dnd.human.nm60
    nm61 = dnd.human.nm61

    nm62 = dnd.human.nm62
    nm63 = dnd.human.nm63
    nm64 = dnd.human.nm64

    @classmethod
    def surname(cls, subrace=10):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 10.

        Returns:
            _type_: _description_
        """
        if subrace == 10:
            return "".join([
                random.choice(cls.nm62),
                random.choice(cls.nm63),
                random.choice(cls.nm64),
                random.choice(cls.nm63),
                random.choice(cls.nm64),
                random.choice(cls.nm63),
                random.choice(cls.nm64),
                random.choice(cls.nm63),
            ])
        return "".join([
            random.choice(cls.nm62),
            random.choice(cls.nm63),
            random.choice(cls.nm64),
            random.choice(cls.nm63),
            random.choice(cls.nm64),
            random.choice(cls.nm63),
        ])

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

    @classmethod
    def female(cls, subrace=10):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 10.

        Returns:
            _type_: _description_
        """
        if subrace == 10:
            return "".join([
                random.choice(cls.nm58),
                random.choice(cls.nm59),
                random.choice(cls.nm60),
                random.choice(cls.nm59),
                random.choice(cls.nm60),
                random.choice(cls.nm59),
                random.choice(cls.nm61),
            ])
        return "".join([
            random.choice(cls.nm58),
            random.choice(cls.nm59),
            random.choice(cls.nm60),
            random.choice(cls.nm59),
            random.choice(cls.nm61),
        ])


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

    nm68 = dnd.human.nm68
    nm69 = dnd.human.nm69

    nm70 = dnd.human.nm70
    nm71 = dnd.human.nm71
    nm72 = dnd.human.nm72

    @classmethod
    def surname(cls, subrace=12):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 12.

        Returns:
            _type_: _description_
        """
        rnd1 = random.choice(cls.nm70)
        rnd2 = random.choice(cls.nm71)
        rnd3 = random.choice(cls.nm72)
        if cls.nm72.index(rnd3) < 3:
            while cls.nm70.index(rnd1) < 3:
                rnd1 = random.choice(cls.nm70)
        return "".join([rnd1, rnd2, rnd3])

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

    @classmethod
    def female(cls, subrace=12):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 12.

        Returns:
            _type_: _description_
        """
        return "".join([
            random.choice(cls.nm68),
            random.choice(cls.nm69),
        ])


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

    nm77 = dnd.human.nm77
    nm78 = dnd.human.nm78
    nm79 = dnd.human.nm79

    nm80 = dnd.human.nm80
    nm81 = dnd.human.nm81
    nm82 = dnd.human.nm82

    @classmethod
    def surname(cls, subrace=10):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 10.

        Returns:
            _type_: _description_
        """
        return "".join([
            random.choice(cls.nm80),
            random.choice(cls.nm14),
            random.choice(cls.nm81),
            random.choice(cls.nm14),
            random.choice(cls.nm81),
            random.choice(cls.nm14),
            random.choice(cls.nm82),
        ])

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

    @classmethod
    def female(cls, subrace=10):
        """
        Summary.

        Args:
            subrace (int, optional): _description_. Defaults to 10.

        Returns:
            _type_: _description_
        """
        if subrace == 10:
            return "".join([
                random.choice(cls.nm77),
                random.choice(cls.nm78),
                random.choice(cls.nm79),
                random.choice(cls.nm77),
                random.choice(cls.nm79),
                random.choice(cls.nm77),
            ])
        return "".join([
            random.choice(cls.nm77),
            random.choice(cls.nm78),
            random.choice(cls.nm79),
            random.choice(cls.nm77),
        ])


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


def name_gen(name_type=0):
    """
    Summary.

    Args:
        name_type (int, optional): _description_. Defaults to 0.

    Yields:
        _type_: _description_
    """
    # $('#placeholder').css('textTransform', 'capitalize');
    for i in range(16):
        names = names_list(i)

        name = ""
        surname = ""
        while not surname:
            surname = test_swear(names.surname(i)).title()

        if name_type == 1:
            while not name:
                name = test_swear(names.female(i)).title()
            yield name + " " + surname
        elif name_type == 3:
            yield OldNames.male().title()
        elif name_type == 4:
            yield OldNames.female().title()
        else:
            while not name:
                name = test_swear(names.male(i)).title()
            yield name + " " + surname
