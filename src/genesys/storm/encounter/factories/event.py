import random
from dice.dice import Dice
from generated.history.time import Time
from generated.encounter.fraction import Fraction
from .distance import DistanceFactory
from genesys.storm.data.encounter.distance import distances_by_time
from genesys.storm.data.encounter.encounter_types import encounter_by_time
from models.encounters.event import Event, DailyEvent, NightlyEvent


class EventFactory:
    default_model = Event

    available_encounters = encounter_by_time()
    available_distances = distances_by_time()

    @classmethod
    def select(cls, values):
        return random.choice(values) if len(values) > 0 else None

    @classmethod
    def time(cls):
        raise NotImplementedError()

    @classmethod
    def encounter_type(cls):
        return cls.select(cls.available_encounters)

    @classmethod
    def distance_factory(cls):
        distance = cls.select(cls.available_distances)
        return distance and DistanceFactory(distance)

    @classmethod
    def encounter(cls):
        party = Fraction()
        enemies = Fraction()

        party.check_surprise()
        enemies.check_surprise()

        encounter_type = cls.encounter_type()
        if not encounter_type:
            return None

        distance_factory = cls.distance_factory()
        distance = distance_factory and distance_factory()
        return encounter_type(
            distance=distance,
            is_surprising=party.surprised,
            is_surprised=enemies.surprised,
        )

    def model_args(self):
        return {
            'time': self.time(),
            'encounter': self.encounter(
                # Fraction(),
                # Fraction(),
            ),
            # 'encounter_type': self.encounter_type(),
            # 'encounter_distance': self.distance_factory(),
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

    available_encounters = encounter_by_time(Time.DAY)
    available_distances = distances_by_time(Time.DAY)

    @classmethod
    def distance(cls):
        return Dice(max_value=20).total()

    @classmethod
    def time(cls):
        # return Time(minutes=cls.distance() * Time.mile)
        return Time(minutes=Dice(2, 20).total() * 15)


class NightlyEventFactory(EventFactory):
    default_model = NightlyEvent

    available_encounters = encounter_by_time(Time.NIGHT)
    available_distances = distances_by_time(Time.NIGHT)

    @classmethod
    def time(cls):
        return Time(hours=Dice(max_value=6, modifier=-1).total())
