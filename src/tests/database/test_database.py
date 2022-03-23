import random
import unittest
from uuid import uuid4
from database.database import BaseDatabase
from database.array_database import ArrayDatabase as BaseArrayDatabase


"""
    def random(self):
        items = list(self.all())
        return random.choice(items) if len(items) > 0 else None

"""


class ArrayDatabase(BaseArrayDatabase):
    def __init__(self, data) -> None:
        super().__init__()

        self.__data = [BaseArrayDatabase.to_record(items) for items in data]

    @property
    def data(self):
        return self.__data


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.values = [ random.uniform(0, 100) for _ in range(10) ]
        self.data = [ { "data": value } for value in self.values ]

    def test_db(self):
        item_id = uuid4()
        db = BaseDatabase()

        self.assertRaises(NotImplementedError, lambda: db.data)
        self.assertRaises(NotImplementedError, lambda: db.insert(self.data))
        self.assertRaises(NotImplementedError, lambda: db.replace(item_id, self.data))
        self.assertRaises(NotImplementedError, lambda: db.find(lambda item: True))
        self.assertRaises(NotImplementedError, lambda: db.first(lambda item: True))
        self.assertRaises(NotImplementedError, lambda: db.get(item_id))
        self.assertRaises(NotImplementedError, lambda: db.random())

    def test_array_db(self):
        db = ArrayDatabase(self.data)
        for item in db.data:
            self.assertIn(item.get("data"), self.values)

    def test_array_db_find(self):
        value = self.values[0]
        db = ArrayDatabase(self.data)

        items = list(db.find(lambda item: item.get("data") == value))
        for item in items:
            self.assertEqual(item.get("data"), value)

        first = db.first(lambda item: item.get("data") == value)
        self.assertEqual(first.get("data"), value)

    def test_array_db_all(self):
        db = ArrayDatabase(self.data)
        items = list(db.all())
        self.assertEqual(db.data, items)

    def test_array_db_get(self):
        db = ArrayDatabase(self.data)
        item = db.data[0]
        item_id = ArrayDatabase.get_item_id(item)
        found = db.get(item_id)
        self.assertEqual(found, item)

    def test_array_db_random(self):
        db = ArrayDatabase(self.data)
        item = db.random()
        self.assertIn(item, db.data)

    def test_array_db_insert(self):
        item = {
            "key1": random.uniform(0, 100),
            "key2": random.uniform(0, 100),
        }

        db = ArrayDatabase(self.data)
        db.insert(item)
        self.assertIn(item, db.data)

    def test_array_db_replace(self):
        item = {
            "key1": random.uniform(0, 100),
            "key2": random.uniform(0, 100),
        }

        db = ArrayDatabase(self.data)
        item_id = ArrayDatabase.get_item_id(db.data[0])

        db.replace(item_id, item)
        replaced = db.get(item_id)

        for k, v in item.items():
            self.assertEqual(v, replaced.get(k))

    def test_array_db_update(self):
        db = ArrayDatabase(self.data)
        items_count = len(db.data)
        item_id = ArrayDatabase.get_item_id(db.data[0])

        item2 = {
            "uuid": item_id, 
            "key1": random.uniform(0, 100),
            "key2": random.uniform(0, 100),
        }
        db.update(item2)
        self.assertEqual(len(db.data), items_count)
        replaced = db.get(item_id)
        for k, v in item2.items():
            self.assertEqual(v, replaced.get(k))

        item1 = {
            "key1": random.uniform(0, 100),
            "key2": random.uniform(0, 100),
        }
        db.update(item1)
        self.assertEqual(len(db.data), items_count + 1)
        self.assertIn(item1, db.data)


    def test_db_helpers(self):
        item_id = uuid4()
        values = {
            "key1": random.uniform(0, 100),
            "key2": random.uniform(0, 100),
        }
        item = {
            "uuid": item_id,
            **values,
        }

        self.assertEqual(BaseDatabase.get_item_id(item), item_id)

        record = BaseDatabase.to_record(values)

        self.assertIsNotNone(record.get("uuid"))
        self.assertIsInstance(record.get("uuid"), str)
        for field, value in values.items():
            self.assertEqual(record.get(field), value)

        record = BaseDatabase.to_record(item)

        self.assertIsNotNone(record.get("uuid"))
        for field, value in item.items():
            self.assertEqual(record.get(field), value)


if __name__ == "__main__":
    unittest.main()
