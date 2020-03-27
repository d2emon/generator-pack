from .time import Time


class Event:
    def __init__(
        self,
        time=None,
        encounter=None,
        max_time=None,
    ):
        self.__time = time
        self.__encounter = encounter
        self.__max_time = max_time

    @property
    def time(self):
        if self.__time is None:
            self.__time = self.generate_time(Time(max_time=self.__max_time))
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = value

    @property
    def minutes(self):
        return self.time.minutes

    @property
    def distance(self):
        return self.time.distance

    @distance.setter
    def distance(self, value):
        self.time.minutes = value * 6

    @property
    def encounter(self):
        return self.__encounter

    @encounter.setter
    def encounter(self, value):
        self.__encounter = value

    def generate_time(self, time):
        return time
