from dice.dice import Dice
from factories.model_factory import ModelFactory
from models.events.event import Event, DailyEvent, NightlyEvent
from models.encounters.fraction import Fraction
from models.history.time import Time
from .distance import DistanceFactory
from .data import DEFAULT_EVENT_DATA_PROVIDER


class EventFactory(ModelFactory):
    def __init__(self, provider=DEFAULT_EVENT_DATA_PROVIDER):
        self.provider = provider
        self.data_group = None

    @classmethod
    def time(cls):
        raise NotImplementedError()

    @property
    def model(self):
        return Event

    def encounter_type_factory(self):
        return self.provider.encounter_factory(self.data_group)

    def distance_factory(self):
        distance = self.provider.distance_factory(self.data_group)
        return distance and DistanceFactory(distance)

    def encounter(self):
        party = Fraction()
        enemies = Fraction()

        party.check_surprise()
        enemies.check_surprise()

        distance_factory = self.distance_factory()
        distance = distance_factory and distance_factory()

        encounter_type = self.encounter_type_factory()

        return encounter_type and encounter_type(
            distance=distance,
            is_surprising=party.surprised,
            is_surprised=enemies.surprised,
        )

    def get_data(self, *args, **kwargs):
        return {
            'time': self.time(),
            'encounter': self.encounter(
                # Fraction(),
                # Fraction(),
            ),
            # 'encounter_type': self.encounter_type(),
            # 'encounter_distance': self.distance_factory(),
            **kwargs,
        }


class DailyEventFactory(EventFactory):
    def __init__(self, provider=DEFAULT_EVENT_DATA_PROVIDER):
        super().__init__(provider)

        self.data_group = Time.DAY

    @property
    def model(self):
        return DailyEvent

    @classmethod
    def distance(cls):
        return Dice(max_value=20).total()

    @classmethod
    def time(cls):
        # return Time(minutes=cls.distance() * Time.mile)
        return Time(minutes=Dice(2, 20).total() * 15)


class NightlyEventFactory(EventFactory):
    def __init__(self, provider=DEFAULT_EVENT_DATA_PROVIDER):
        super().__init__(provider)

        self.data_group = Time.NIGHT

    @property
    def model(self):
        return NightlyEvent

    @classmethod
    def time(cls):
        return Time(hours=Dice(max_value=6, modifier=-1).total())
