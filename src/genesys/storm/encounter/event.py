import random
from dice.dice import Dice
from models.storm.encounters.event import Event as EventModel
from sample_data.storm.encounter import ENCOUNTER_TYPES
from sample_data.storm.encounter.distance import DISTANCES
from models.storm.encounters.fraction import Fraction


class Event(EventModel):
    available_encounters = ENCOUNTER_TYPES
    encounter_distances = DISTANCES
    is_daily = False
    is_nightly = False

    def __init__(
        self,
        time=None,
        encounter=None,
        encounter_type=None,
        encounter_distance=None,
        max_time=None,
    ):
        super().__init__(
            time=time,
            encounter=encounter,
            max_time=max_time,
        )
        self.__encounter = encounter
        self.__encounter_type = encounter_type
        self.__encounter_distance = encounter_distance
        self.__fractions = [
            Fraction(),
            Fraction(),
        ]

    @property
    def encounter_type(self):
        if self.__encounter_type is None:
            self.__encounter_type = random.choice(self.available_encounters)\
                if len(self.available_encounters) > 0\
                else None
        return self.__encounter_type

    @property
    def encounter_distance(self):
        if self.__encounter_distance is None:
            self.__encounter_distance = random.choice(self.encounter_distances)\
                if len(self.encounter_distances) > 0\
                else None
        return self.__encounter_distance

    @property
    def encounter(self):
        if self.__encounter is None:
            self.__encounter = self.generate(*self.__fractions)
        return self.__encounter

    @encounter.setter
    def encounter(self, value):
        self.__encounter = value

    def generate(self, *fractions):
        [fraction.check_surprise() for fraction in fractions]
        return self.encounter_type(distance_type=self.encounter_distance)


class DailyEvent(Event):
    available_encounters = [encounter for encounter in ENCOUNTER_TYPES if encounter.is_daily]
    encounter_distances = [distance for distance in DISTANCES if distance.is_daily]
    is_daily = True
    is_nightly = False

    def __init__(
        self,
        time=None,
        encounter=None,
        encounter_type=None,
        distance=None,
        max_time=20 * 6,
    ):
        super().__init__(
            time=time,
            encounter=encounter,
            encounter_type=encounter_type,
            max_time=max_time,
        )
        if distance is not None:
            self.distance = distance

    @classmethod
    def generate_distance(cls):
        return next(Dice(max_value=20).roll())

    def generate_time(self, time):
        time.minutes = self.generate_distance() * 6
        return time

    def __str__(self):
        return "Столкновение после {} миль пути ({})\n{}".format(
            self.time.distance,
            self.time,
            self.encounter,
        )


class NightlyEvent(Event):
    available_encounters = [encounter for encounter in ENCOUNTER_TYPES if encounter.is_nightly]
    encounter_distances = [distance for distance in DISTANCES if distance.is_nightly]
    is_daily = False
    is_nightly = True

    def __init__(
        self,
        time=None,
        encounter=None,
        encounter_type=None,
        max_time=6 * 60,
    ):
        super().__init__(
            time=time,
            encounter=encounter,
            encounter_type=encounter_type,
            max_time=max_time,
        )

    def generate_time(self, time):
        time.hours = next(Dice(max_value=6).roll()) - 1
        return time

    def __str__(self):
        return "Столкновение во время отдыха ({})\n{}".format(
            self.time,
            self.encounter,
        )
