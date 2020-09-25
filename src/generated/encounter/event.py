class Event:
    def __init__(
        self,
        time=None,
        encounter=None,
        max_time=None,
    ):
        self.time = time
        self.encounter = encounter
        self.__max_time = max_time

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
        self.time.minutes = value * 6


class EncounterEvent(Event):
    is_daily = False
    is_nightly = False

    def __init__(
        self,
        time=None,
        encounter=None,
        encounter_type=None,
        encounter_distance=None,
        max_time=None,
        *args,
        **kwargs,
    ):
        super().__init__(
            time=time,
            encounter=encounter,
            max_time=max_time,
        )
        self.encounter_type = encounter_type
        self.encounter_distance = encounter_distance


class DailyEvent(EncounterEvent):
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
        self.distance = distance

    def __str__(self):
        return "Столкновение после {} миль пути ({})\n{}".format(
            self.time.distance,
            self.time,
            self.encounter,
        )


class NightlyEvent(EncounterEvent):
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

    def __str__(self):
        return "Столкновение во время отдыха ({})\n{}".format(
            self.time,
            self.encounter,
        )
