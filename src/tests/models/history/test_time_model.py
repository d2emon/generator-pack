import random
import unittest
from models.history.time import Time


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
        hours = random.randrange(1, 24)
        time_text = f"{hours} ч. {minutes} мин."

        time = Time(
            hours=hours,
            minutes=minutes,
        )

        self.assertEqual(str(time), time_text)


if __name__ == "__main__":
    unittest.main()
