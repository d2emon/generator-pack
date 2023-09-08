import random
import unittest
from uuid import UUID
from data.and_why import egypt
from genesys.and_why.data import genders, slots
from genesys.and_why.database.genders import GENDERS
from genesys.and_why.database.slots import SLOTS


class TestAndWhy(unittest.TestCase):
    genders_data = [
        'MALE',
        'FEMALE',
    ]

    types_data = [
        'Accessory',
        'Collar',
        'Headdress',
        'Kalasiris',
        'Shendyt',
        'Shield',
        'Weapon',
    ]

    slots_data = [
        slots.IN_HAND,
        slots.SHIELD,
        slots.HEAD,
        slots.NECK,
        slots.TORSO,
        slots.HIPS,
    ]

    def setUp(self):
        self.data = [ { "data": random.uniform(0, 100) } for _ in range(10) ]

    def test_egypt(self):
        for value in egypt.EGYPT.values():
            self.assertIsNotNone(value)

            gender = value.get('gender')
            name = value.get('name')
            type = value.get('type')

            self.assertIn(gender, self.genders_data)
            self.assertIn(type, self.types_data)
            self.assertIsInstance(name, str)

    def test_by_gender(self):
        for gender in self.genders_data:
            for item in egypt.EGYPT.by_gender(gender):
                value = item.get('value')
                self.assertIsNotNone(value)

                self.assertEqual(value.get('gender'), gender)

    def test_genders(self):
        self.assertEqual(genders.DEFAULT, genders.MALE)

        for value in GENDERS.values():
            self.assertIn(value, self.genders_data)

    def test_slots(self):
        for value in SLOTS.values():
            self.assertIn(value, self.slots_data)


if __name__ == "__main__":
    unittest.main()
