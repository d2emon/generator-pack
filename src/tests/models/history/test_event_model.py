import random
import unittest
from models.history.time import Time
from models.history.event import Event

"""
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
        return int(self.minutes / self.mile)

    def __str__(self):
        text = []

        hours = self.hours
        if hours:
            text.append('{} ч.'.format(hours))

        minutes = self.minutes % 60
        text.append('{} мин.'.format(minutes))

        return ' '.join(text)
"""


class TestEventModel(unittest.TestCase):
    def test_event_model(self):
        year = random.randrange(0, 100)
        title = str(random.uniform(0, 100))
        event_text = f"{year} лет назад: {title}"

        event = Event(
            year=year,
            title=title,
        )

        self.assertEqual(event.value, title)
        self.assertEqual(str(event), event_text)


if __name__ == "__main__":
    unittest.main()
