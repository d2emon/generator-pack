from models.history.time import Time
from models.history.event import Event as HistoryEvent
from .distance import Distance


class Event(HistoryEvent):
    time_of_day = None

    time = HistoryEvent.field_property('time', None)
    encounter = HistoryEvent.field_property('encounter', None)
    encounter_type = HistoryEvent.field_property('encounter_type', None)
    # encounter_distance = HistoryEvent.field_property('encounter_distance', None)

    def __init__(
        self,
        time=None,
        encounter=None,
        encounter_type=None,
        # encounter_distance=None,
        max_time=None,
        *args,
        **kwargs,
    ):
        super().__init__(
            time=time,
            encounter=encounter,
            encounter_type=encounter_type,
            # encounter_distance=encounter_distance
            *args,
            **kwargs,
        )

        if self.time is not None and max_time is not None:
            self.time.max_time = max_time

    @property
    def field_names(self):
        yield from super().field_names
        yield "time"
        yield "encounter"
        yield "encounter_type"
        # yield "encounter_distance"

    @property
    def minutes(self):
        return self.time.minutes if self.time is not None else None

    @minutes.setter
    def minutes(self, value):
        if self.time is None:
            return

        self.time.minutes = value

    @property
    def distance(self):
        return self.time.distance if self.time is not None else None

    @distance.setter
    def distance(self, value):
        if self.time is None:
            return

        self.time.distance = value


class DailyEvent(Event):
    time_of_day = Time.DAY

    def __init__(
        self,
        time=None,
        encounter=None,
        encounter_type=None,
        # distance=None,
        max_time=20 * 6,
        *args,
        **kwargs,
    ):
        super().__init__(
            time=time,
            encounter=encounter,
            encounter_type=encounter_type,
            # distance=distance
            max_time=max_time,
            *args,
            **kwargs,
        )

    def __str__(self):
        return '\n'.join([
            f"Столкновение в пути ({self.time} / {Distance.miles_to_km(self.distance)} км)",
            str(self.encounter),
        ])


class NightlyEvent(Event):
    time_of_day = Time.NIGHT

    def __init__(
        self,
        time=None,
        encounter=None,
        encounter_type=None,
        max_time=6 * 60,
        *args,
        **kwargs,
    ):
        super().__init__(
            time=time,
            encounter=encounter,
            encounter_type=encounter_type,
            max_time=max_time,
            *args,
            **kwargs,
        )

    def __str__(self):
        return '\n'.join([
            f"Столкновение во время отдыха ({self.time})",
            str(self.encounter),
        ])
