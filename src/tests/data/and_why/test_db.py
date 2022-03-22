import os
import random
import unittest
from data.and_why.db import Database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.data = [ { "data": random.uniform(0, 100) } for _ in range(10) ]
        self.db = Database(*self.data)

    def test_init_db(self):
        for item in self.db.data:
            self.assertIsNotNone(item.get('id'))
            self.assertIsNotNone(item.get('value'))
            self.assertIn(item.get('value'), self.data)

    def test_find(self):
        for item in self.db.find(lambda item: True):
            self.assertIsNotNone(item.get('id'))
            self.assertIsNotNone(item.get('value'))
            self.assertIn(item.get('value'), self.data)

    def test_values(self):
        self.assertEqual(self.db.values(), self.data)


if __name__ == "__main__":
    unittest.main()
