import random
from dice.dice import Dice
from generated.encounter import Day, EncounterEvent, DailyEvent, NightlyEvent
from generated.history.time import Time
from generated.history.encounters.fraction import Fraction
from sample_data.storm.encounter import ENCOUNTER_TYPES
from sample_data.storm.encounter.distance import DISTANCES


class EventFactory:
    default_model = EncounterEvent

    available_encounters = ENCOUNTER_TYPES
    encounter_distances = DISTANCES

    @classmethod
    def select(cls, values):
        return random.choice(values) if len(values) > 0 else None

    @classmethod
    def time(cls):
        raise NotImplementedError()

    @classmethod
    def max_time(cls):
        return None

    @classmethod
    def encounter_type(cls):
        return cls.select(cls.available_encounters)

    @classmethod
    def encounter_distance(cls):
        return cls.select(cls.encounter_distances)

    @classmethod
    def encounter(cls, *fractions):
        for fraction in fractions:
            fraction.check_surprise()
        encounter_type = cls.encounter_type()
        if encounter_type is None:
            return None
        return encounter_type(distance_type=cls.encounter_distance())

    def model_args(self):
        return {
            'time': self.time(),
            'encounter': self.encounter(
                Fraction(),
                Fraction(),
            ),
            'encounter_type': self.encounter_type(),
            # 'encounter_distance': self.encounter_distance(),
            'max_time': self.max_time(),
        }

    def __call__(
        self,
        *args,
        max_time=None,
        **kwargs,
    ):
        model_args = {**self.model_args()}
        model_args.update(kwargs)
        return self.default_model(**model_args)


class DailyEventFactory(EventFactory):
    default_model = DailyEvent

    available_encounters = [encounter for encounter in ENCOUNTER_TYPES if encounter.is_daily]
    encounter_distances = [distance for distance in DISTANCES if distance.is_daily]

    @classmethod
    def distance(cls):
        return next(Dice(max_value=20).roll())

    @classmethod
    def time(cls):
        return Time(minutes=cls.distance() * 6)

    @classmethod
    def max_time(cls):
        return 20 * 6

    def model_args(self):
        args = super().model_args()
        return {
            'time': args.get('time'),
            'encounter': args.get('encounter'),
            'encounter_type': args.get('encounter_type'),
            'max_time': args.get('max_time'),
            'distance': self.distance(),
        }


class NightlyEventFactory(EventFactory):
    default_model = NightlyEvent

    available_encounters = [encounter for encounter in ENCOUNTER_TYPES if encounter.is_nightly]
    encounter_distances = [distance for distance in DISTANCES if distance.is_nightly]

    @classmethod
    def time(cls):
        return Time(hours=next(Dice(max_value=6).roll()) - 1)

    @classmethod
    def max_time(cls):
        return 6 * 60

    def model_args(self):
        args = super().model_args()
        return {
            'time': args.get('time'),
            'encounter': args.get('encounter'),
            'encounter_type': args.get('encounter_type'),
            'max_time': args.get('max_time'),
        }


class EncounterFactory:
    def __init__(
        self,
        roll_on_double=True,
    ):
        self.roll_on_double = roll_on_double
        self.daily = DailyEventFactory()
        self.nightly = NightlyEventFactory()

    def __add_event(self):
        dice1, dice2 = Dice(count=2).roll()

        yield self.nightly() if dice1 % 2 else self.daily()

        if self.roll_on_double and (dice1 == dice2):
            yield from self.__add_event()

    def __events(self):
        yield self.daily()
        yield self.nightly()
        yield from self.__add_event()

    def __call__(self, day_id, *args, **kwargs):
        return Day(day_id, *self.__events())
