import random
import unittest
from generated.encounter.day import Day
from genesys.storm.encounter import EncountersManager


class TestEncounterManager(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [random.uniform(0, 100) for _ in range(10)]

    def test_roll_on_double(self):
        encounters_manager_1 = EncountersManager(roll_on_double=True)
        # TODO: Check for encounters_manager_1.__factory(roll_on_double)

        encounters_manager_2 = EncountersManager(roll_on_double=False)
        # TODO: Check for encounters_manager_1.__factory(roll_on_double)

        self.assertNotEqual(encounters_manager_1, encounters_manager_2)

    def test_events_for_day(self):
        day_1 = EncountersManager.events_for_day(roll_on_double=True)
        self.assertIsInstance(day_1, Day)

        day_2 = EncountersManager.events_for_day(roll_on_double=False)
        self.assertIsInstance(day_2, Day)

    def test_show_day(self):
        day_id = random.randint(1, 10)
        day = Day(day_id)
        result = None # EncountersManager.show_day(day)
        # TODO: Check for day
        """
        for event in day.events:
            print('-' * 80)
            print(event)
        """
        self.assertNotEqual(result, self.values)

    def test_show_days(self):
        days = []
        result = None # EncountersManager.show_days(*days)
        # TODO: Check for day
        """
        for day in days:
            print('=' * 80)
            print(day)
            cls.show_day(day)
        print('=' * 80)
        """
        self.assertNotEqual(result, self.values)

    def test_encounters(self):
        count = random.randrange(10)

        encounters_manager_1 = EncountersManager(roll_on_double=True)
        result1 = encounters_manager_1.encounters(count)
        """
        days = (self.__factory(f'День {day_id + 1} из {count}', **kwargs) for day_id in range(count))
        self.show_days(*days)
        """

        encounters_manager_2 = EncountersManager(roll_on_double=False)
        result2 = encounters_manager_2.encounters(count)
        """
        days = (self.__factory(f'День {day_id + 1} из {count}', **kwargs) for day_id in range(count))
        self.show_days(*days)
        """

        self.assertNotEqual(encounters_manager_1, encounters_manager_2)


if __name__ == "__main__":
    unittest.main()
