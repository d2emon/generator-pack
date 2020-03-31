from ..character import Character


class CharacterBuilder:
    CREATE_CHARACTER = 0
    SET_RACE = 1
    SET_TRAITS = 2
    SET_EDGES = 3
    SET_EQUIPMENT = 4
    SET_BIO = 5
    IS_DONE = 6

    STAT_POINTS = 10
    SKILL_POINTS = 15
    MIN_WEALTH = 1
    EDGES = 0
    MINOR_HINDRANCES = 2
    MAJOR_HINDRANCES = 1

    def __init__(self, character=None):
        self.character = character
        self.wealth = 1
        self.stage = self.CREATE_CHARACTER

    def new_character(self, character=None):
        self.character = character or Character()
        self.stage = self.SET_RACE
        return self

    def set_race(self, race=None):
        if race is not None:
            self.character.race = race
        self.stage = self.SET_TRAITS
        return self

    def set_traits(
        self,
        agility=None,
        smarts=None,
        spirit=None,
        strength=None,
        vigor=None,
        skills=None,
    ):
        if agility is not None:
            self.character.agility.value = agility
        if smarts is not None:
            self.character.smarts.value = smarts
        if spirit is not None:
            self.character.spirit.value = spirit
        if strength is not None:
            self.character.strength.value = strength
        if vigor is not None:
            self.character.vigor.value = vigor

        self.character.skills.set_values(skills or {})

        self.stage = self.SET_EDGES
        return self

    def set_edges(
        self,
        *edges,
        wealth=1,
    ):
        self.character.edges.set_values(edges)
        self.wealth = wealth
        self.stage = self.SET_EQUIPMENT
        return self

    def set_equipment(
        self,
        *equipment,
        money=None,
    ):
        if money is not None:
            self.character.money = money * self.wealth

        self.character.equipment.set_values(equipment)

        self.stage = self.SET_BIO
        return self

    def set_bio(
        self,
        name=None,
        bio=None,
    ):
        if name is not None:
            self.character.name = name

        if bio is not None:
            self.character.bio = bio

        self.stage = self.IS_DONE
        return self

    @property
    def next_stage(self):
        return {
            self.CREATE_CHARACTER: self.new_character,
            self.SET_RACE: self.set_race,
            self.SET_TRAITS: self.set_traits,
            self.SET_EDGES: self.set_edges,
            self.SET_EQUIPMENT: self.set_equipment,
            self.SET_BIO: self.set_bio,
        }.get(self.stage, lambda: self)

    # Unused points
    @property
    def stats_left(self):
        return self.STAT_POINTS - self.character.stats.cost

    @property
    def skills_left(self):
        return self.SKILL_POINTS - self.character.skills.cost

    @property
    def wealth_left(self):
        return self.MIN_WEALTH - self.wealth

    @property
    def edges_left(self):
        return self.EDGES - self.character.traits.cost

    @property
    def major_hindrances_left(self):
        return self.MAJOR_HINDRANCES - len(self.character.traits.major_hindrances)

    @property
    def minor_hindrances_left(self):
        return self.MINOR_HINDRANCES - len(self.character.traits.minor_hindrances)

    @property
    def points_left(self):
        return sum([
            self.stats_left,
            self.skills_left,
            self.wealth_left,
            self.edges_left,
        ])

    def build(self):
        return self.new_character()\
            .set_race()\
            .set_traits()\
            .set_edges()\
            .set_equipment()\
            .set_bio()\
            .character
