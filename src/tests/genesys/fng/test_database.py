import random
import unittest
import uuid
from database.data_block import NameItem, NameBlock, load_data, fill_data
from genesys.fng.database import Database


class TestDataBlock(unittest.TestCase):
    def setUp(self):
        self.group_id = uuid.uuid4()
        self.block_id = uuid.uuid4()
        self.values = [uuid.uuid4() for _ in range(10)]
        self.data = { self.block_id: self.values }
        self.db = Database(self.group_id, self.data)

    def test_db(self):
        for block in self.db.data.values:
            self.assertEqual(block.values.get('group_id'), self.group_id)
            self.assertIn(block.block_id, self.data.keys())
            self.assertIn(block.value, self.data[block.block_id])

    def test_find_block_id(self):
        search = self.db.find(self.block_id)

        item1 = search()
        self.assertIn(item1.value, self.values)

        item2 = search(item_id=uuid.uuid4())
        self.assertIsNone(item2)

        item_id = 1
        item3 = search(item_id=item_id)
        self.assertIn(item3.value, self.values)
        self.assertEqual(item3.value, self.values[item_id])

    def test_find_no_block_id(self):
        item = self.db.find(uuid.uuid4())()
        self.assertIsNone(item)


if __name__ == "__main__":
    unittest.main()

