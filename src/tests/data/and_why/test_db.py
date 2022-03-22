import random
import unittest
from data.and_why.db import Database
from data.and_why.egypt import EGYPT
from uuid import UUID


class TestDatabase(unittest.TestCase):
    genders = [
        'MALE',
        'FEMALE',
    ]

    types = [
        'Accessory',
        'Collar',
        'Headdress',
        'Kalasiris',
        'Shendyt',
        'Shield',
        'Weapon',
    ]

    def setUp(self):
        self.data = [ { "data": random.uniform(0, 100) } for _ in range(10) ]
        self.db = Database(*self.data)

    def test_init_db(self):
        for item in self.db.data:
            self.assertIsNotNone(item.get('id'))
            self.assertIsInstance(item.get('id'), UUID)
            self.assertIsNotNone(item.get('value'))
            self.assertIn(item.get('value'), self.data)

    def test_find(self):
        for item in self.db.find(lambda item: True):
            self.assertIsNotNone(item.get('id'))
            self.assertIsInstance(item.get('id'), UUID)
            self.assertIsNotNone(item.get('value'))
            self.assertIn(item.get('value'), self.data)

    def test_values(self):
        self.assertEqual(self.db.values(), self.data)

    def test_egypt(self):
        self.assertIsInstance(EGYPT, Database)

        for item in EGYPT.data:
            id = item.get('id')
            self.assertIsInstance(id, UUID)

            value = item.get('value')
            self.assertIsNotNone(value)

            gender = value.get('gender')
            name = value.get('name')
            type = value.get('type')

            self.assertIn(gender, self.genders)
            self.assertIn(type, self.types)
            self.assertIsInstance(name, str)

    def test_by_gender(self):
        for gender in self.genders:
            for item in EGYPT.by_gender(gender):
                id = item.get('id')
                self.assertIsInstance(id, UUID)

                value = item.get('value')
                self.assertIsNotNone(value)

                self.assertEqual(value.get('gender'), gender)


if __name__ == "__main__":
    unittest.main()
