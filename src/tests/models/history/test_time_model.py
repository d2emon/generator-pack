import random
import unittest
from models.history.time import Time


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


class TestTimeModel(unittest.TestCase):
    def test_time_model(self):
        self.assertEqual(Time.DAY, 'DAY')
        self.assertEqual(Time.NIGHT, 'NIGHT')

    def test_no_minutes(self):
        time = Time(minutes=False)
        self.assertEqual(time.minutes, 0)

    def test_minutes(self):
        minutes = random.randrange(0, 60)
        hours = random.randrange(0, 24)

        time = Time(
            hours=hours,
            minutes=minutes,
        )

        self.assertEqual(time.minutes, minutes + hours * 60)

        new_minutes = random.randrange(0, 60)

        time.minutes = new_minutes

        self.assertEqual(time.minutes, new_minutes)

    def test_hours(self):
        time = Time()

        hours = random.randrange(0, 24)
        time.hours = hours

        self.assertEqual(time.hours, hours)
        self.assertEqual(time.minutes, hours * 60)

    def test_max_time(self):
        minutes = random.randrange(0, 60)
        hours = random.randrange(0, 24)

        time = Time(
            hours=hours,
            minutes=minutes,
        )
        time.max_time = 60

        self.assertLessEqual(time.minutes, 60)

    def test_distance(self):
        miles = random.randrange(0, 10)
        minutes = miles * Time.mile

        time = Time(minutes=minutes)

        self.assertEqual(Time.mile, 6)
        self.assertEqual(time.distance, miles)

    def test_str_no_hours(self):
        minutes = random.randrange(0, 60)
        time_text = f"{minutes} мин."

        time = Time(
            minutes=minutes,
        )

        self.assertEqual(str(time), time_text)

    def test_str(self):
        minutes = random.randrange(0, 60)
        hours = random.randrange(0, 24)
        time_text = f"{hours} ч. {minutes} мин."

        time = Time(
            hours=hours,
            minutes=minutes,
        )

        self.assertEqual(str(time), time_text)


if __name__ == "__main__":
    unittest.main()
