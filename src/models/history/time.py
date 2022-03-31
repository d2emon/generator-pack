from models.model import Model


class Time(Model):
    DAY = 'DAY'
    NIGHT = 'NIGHT'

    # mile = 20
    mile = 6

    max_time = Model.field_property('max_time')
    value = Model.field_property('minutes', 0)

    def __init__(self, hours=0, minutes=0, *args, **fields):
        __minutes = minutes + hours * 60

        super().__init__(
            *args,
            minutes=__minutes,
            **fields,
        )

    @property
    def field_names(self):
        yield "minutes"
        yield "max_time"

    @property
    def minutes(self):
        minutes = self.value

        if self.max_time is None:
            return minutes
        else:
            return minutes % self.max_time

    @minutes.setter
    def minutes(self, value):
        self.value = value

    @property
    def hours(self):
        return int(self.minutes / 60)

    @hours.setter
    def hours(self, value):
        self.value = value * 60

    @property
    def distance(self):
        return int(self.minutes / self.mile)

    def __str__(self):
        text = []

        hours = self.hours
        if hours:
            text.append('{} ч.'.format(hours))

        minutes = self.minutes % 60
        text.append('{} мин.'.format(minutes))

        return ' '.join(text)
