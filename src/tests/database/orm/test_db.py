import random
import unittest
from uuid import UUID
from database.orm import Database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.data = [ { "data": random.uniform(0, 100) } for _ in range(10) ]
        self.db = Database(*self.data)

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

    def test_add_values(self):
        Database.add_to_group('GROUP_ID0', self.data)

        values = list(Database.get_from_group('GROUP_ID0'))

        for item in self.data:
            self.assertIn(item, values)


if __name__ == "__main__":
    unittest.main()
