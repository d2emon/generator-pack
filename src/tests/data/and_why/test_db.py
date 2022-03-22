import random
import unittest
from data.and_why import db, egypt, genders, slots
from uuid import UUID


class TestDatabase(unittest.TestCase):
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
        self.db = db.Database(*self.data)

    def test_init_db(self):
        for item in self.db.data:
            id = item.get('id')
            self.assertIsInstance(id, UUID)

            value = item.get('value')
            self.assertIsNotNone(value)
            self.assertIn(value, self.data)

    def test_find(self):
        for item in self.db.find(lambda item: True):
            id = item.get('id')
            self.assertIsInstance(id, UUID)

            value = item.get('value')
            self.assertIsNotNone(value)
            self.assertIn(value, self.data)

    def test_values(self):
        self.assertEqual(self.db.values(), self.data)

    def test_egypt(self):
        self.assertIsInstance(egypt.EGYPT, db.Database)

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
                id = item.get('id')
                self.assertIsInstance(id, UUID)

                value = item.get('value')
                self.assertIsNotNone(value)

                self.assertEqual(value.get('gender'), gender)

    def test_genders(self):
        self.assertEqual(genders.DEFAULT, genders.MALE)

        self.assertIsInstance(genders.GENDERS, db.Database)

        for value in genders.GENDERS.values():
            self.assertIn(value, self.genders_data)

    def test_slots(self):
        self.assertIsInstance(slots.SLOTS, db.Database)

        for value in slots.SLOTS.values():
            self.assertIn(value, self.slots_data)


if __name__ == "__main__":
    unittest.main()
