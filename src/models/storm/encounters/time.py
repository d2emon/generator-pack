class Time:
    def __init__(self, hours=0, minutes=0, max_time=None):
        self.__minutes = minutes + hours * 60
        self.max_time = None

    @property
    def minutes(self):
        minutes = self.__minutes or 0
        if self.max_time is None:
            return minutes
        else:
            return minutes % self.max_time

    @minutes.setter
    def minutes(self, value):
        self.__minutes = value

    @property
    def hours(self):
        return int(self.minutes / 60)

    @hours.setter
    def hours(self, value):
        self.__minutes = value * 60

    @property
    def distance(self):
        return int(self.minutes / 6)

    def __str__(self):
        text = []

        hours = self.hours
        if hours:
            text.append('{} ч.'.format(hours))

        minutes = self.minutes % 60
        text.append('{} мин.'.format(minutes))

        return ' '.join(text)
