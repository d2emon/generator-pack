from generated.history.time import Time
from models.model import Model
from .distance import Distance


class Event(Model):
    time_of_day = None

    def __init__(
        self,
        time=None,
        encounter=None,
        # encounter_type=None,
        # encounter_distance=None,
        max_time=None,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.time = time
        self.encounter = encounter
        self.__max_time = max_time
        # self.encounter_type = encounter_type
        # self.encounter_distance = encounter_distance

    @property
    def minutes(self):
        return self.time.minutes

    @property
    def distance(self):
        return self.time.distance

    @distance.setter
    def distance(self, value):
        if value is None:
            return
        self.time.minutes = value * Time.mile


class DailyEvent(Event):
    time_of_day = Time.DAY

    def __init__(
        self,
        time=None,
        encounter=None,
        encounter_type=None,
        # distance=None,
        max_time=20 * 6,
    ):
        super().__init__(
            time=time,
            encounter=encounter,
            encounter_type=encounter_type,
            max_time=max_time,
        )
        # self.distance = distance

    def __str__(self):
        return '\n'.join([
            f"Столкновение в пути ({self.time} / {Distance.km(self.time.distance)} км)",
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
    ):
        super().__init__(
            time=time,
            encounter=encounter,
            encounter_type=encounter_type,
            max_time=max_time,
        )

    def __str__(self):
        return '\n'.join([
            f"Столкновение во время отдыха ({self.time})",
            str(self.encounter),
        ])
