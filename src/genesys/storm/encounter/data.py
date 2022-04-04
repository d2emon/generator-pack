import random
from data.storm.data.encounter.distance import distances_by_time
from data.storm.data.encounter.encounter_types import encounter_by_time


class EventDataProvider:
    def __init__(
        self,
        encounters,
        distances,
    ):
        self.encounters = encounters
        self.distances = distances

    @classmethod
    def __select(cls, values):
        return random.choice(values) if len(values) > 0 else None

    def encounters_by_time(self, time):
        return self.encounters(time)

    def distances_by_time(self, time):
        return self.distances(time)

    def encounter_factory(self, time=None, *args, **kwargs):
        return self.__select(self.encounters_by_time(time))

    def distance_factory(self, time=None, *args, **kwargs):
        return self.__select(self.distances_by_time(time))


DEFAULT_EVENT_DATA_PROVIDER = EventDataProvider(
    encounters = encounter_by_time,
    distances = distances_by_time,
)
