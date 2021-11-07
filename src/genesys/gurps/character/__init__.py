from .stat import ST, DX, IQ, HT
from . import build, size


class Character:
    def __init__(self, starting_points=150):
        self.__starting_points = starting_points
        self.__ready = False

        self.__stats = dict(
            st=ST(ST.default_value),
            dx=DX(DX.default_value),
            iq=IQ(IQ.default_value),
            ht=HT(HT.default_value),
        )

        self.hp_modifier = 0
        self.will_modifier = 0
        self.per_modifier = 0
        self.fp_modifier = 0
        self.basic_speed_modifier = 0
        self.basic_move_modifier = 0

        self.build = build.Average
        self.size = size.Average

    # Basic Stats

    @property
    def st(self):
        return self.__stats['st']

    @property
    def dx(self):
        return self.__stats['dx']

    @property
    def iq(self):
        return self.__stats['iq']

    @property
    def ht(self):
        return self.__stats['ht']

    # Secondary Stats

    @property
    def thrust_damage(self):
        return self.st.thrust_damage

    @property
    def swing_damage(self):
        return self.st.swing_damage

    @property
    def bl(self):
        return self.st.bl

    @property
    def hp(self):
        return self.st.value + self.hp_modifier

    @property
    def will(self):
        return self.iq.value + self.will_modifier

    @property
    def per(self):
        return self.iq.value + self.per_modifier

    @property
    def fp(self):
        return self.ht.value + self.fp_modifier

    @property
    def basic_speed(self):
        return (self.st.value + self.dx.value) / 4 + self.basic_speed_modifier

    @property
    def basic_move(self):
        return int(self.basic_speed) + self.basic_move_modifier

    # Points

    @property
    def max_disadvantages(self):
        return int(self.__starting_points / 2)

    @property
    def total_points(self):
        stat_points = sum(stat.points for stat in self.__stats.values)
        hp_points = self.hp_modifier * 2
        will_points = self.will_modifier * 5
        per_points = self.per_modifier * 5
        fp_points = self.fp_modifier * 3
        basic_speed_points = int(self.basic_speed_modifier * 4) * 5
        basic_move_points = self.basic_move_modifier * 5
        return sum([
            stat_points,
            hp_points,
            will_points,
            per_points,
            fp_points,
            basic_speed_points,
            basic_move_points,

            self.build.value,
            self.size.value,
        ])

    @property
    def points_left(self):
        return self.__starting_points - self.total_points

    @property
    def is_ready(self):
        return self.__ready

    def set_basic(
        self,
        st=10,
        dx=10,
        iq=10,
        ht=10,
        hp_modifier=0,
        will_modifier=0,
        per_modifier=0,
        fp_modifier=0,
        basic_speed_modifier=0,
        basic_move_modifier=0,
    ):
        self.st.value = st
        self.dx.value = dx
        self.iq.value = iq
        self.ht.value = ht

        self.hp_modifier = hp_modifier
        self.will_modifier = will_modifier
        self.per_modifier = per_modifier
        self.fp_modifier = fp_modifier
        self.basic_speed_modifier = basic_speed_modifier
        self.basic_move_modifier = basic_move_modifier

        return self

    def set_build(self, build=build.Average, size=size.Average):
        """Build (p. 18) and Age and Beauty
(p. 20). These sections describe the in-
game effects of height, weight, age,
looks, etc."""
        self.build = build
        self.size = size
        return self

    def set_background(self):
        """Social Background (p. 22), Wealth
and Influence (p. 25), Friends and Foes
(p. 31), and Identities (p. 31).
Determine what kind of society you
are from, where you stand in the game
world, how others regard you, and
who you can count on for support – or
for a knife in the back!"""
        return self

    def set_advantages(self):
        """Advantages (p. 32). Chapter 2 lists
dozens of special talents and powers.
Perks (p. 100) are special “mini-advan-
tages” that can help individualize your
character."""
        return self

    def set_disadvantages(self):
        """Disadvantages (p. 119). Chapter 3
lists a wide variety of negative traits,
from inconvenient to crippling.
Mental disadvantages and Quirks
(p. 162), special mini-disadvantages,
can help you define your personality."""
        return self

    def set_skills(self):
        """Skills (p. 167) and Techniques
(p. 229). The abilities in Chapter 4
describe what you can actually do. Be
sure to match your skills to your occu-
pation and character type."""
        self.__ready = True
        return self
