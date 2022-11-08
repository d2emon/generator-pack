import random
import unittest
import uuid
from database.data_block import NameItem, NameBlock, load_data, fill_data


class TestDataBlock(unittest.TestCase):
    def setUp(self):
        self.item_id = uuid.uuid4()
        self.block_id = random.uniform(0, 100)
        self.value = random.uniform(0, 100)
        self.data_item = NameItem(self.item_id, self.value, block_id=self.block_id)

        self.values = [ random.uniform(0, 100) for _ in range(10) ]
        items = [NameItem(uuid.uuid4(), value) for value in self.values]

        self.data = {
            f'item{item_id}': random.uniform(0, 100)
            for item_id in range(10)
        }
        other = {
            f'item{item_id}_other': random.uniform(0, 100)
            for item_id in range(10)
        }
        self.items = [
            self.data_item,
            *items,
            NameItem(
                uuid.uuid4(),
                random.uniform(0, 100),
                **self.data,
                **other,
            ),

        ]
        self.data_block = NameBlock(self.items)

    def test_item_id(self):
        self.assertEqual(self.data_item.item_id, self.item_id)

    def test_block_id(self):
        self.assertEqual(self.data_item.block_id, self.block_id)

    def test_value(self):
        value = str(self.value)
        self.assertEqual(self.data_item.value, self.value)
        self.assertEqual(str(self.data_item), value)
        self.assertEqual(len(self.data_item), len(value))

    def test_values(self):
        self.assertListEqual(self.data_block.values, self.items)


    def test_save(self):
        new_items = 10
        data = [ uuid.uuid4() for _ in range(new_items) ]
        values = { f'value{item_id}': uuid.uuid4() for item_id in range(10) }

        before = len(self.data_block.values)
        filled = self.data_block.fill(*data, **values)

        self.assertEqual(filled, self.data_block)
        self.assertEqual(len(self.data_block.values), before + len(data))
        data_values = self.data_block.values
        for value in data_values[-new_items:]:
            self.assertIsInstance(value, NameItem)
            self.assertIsInstance(value.item_id, int)
            self.assertIn(value.value, data)
            self.assertDictEqual(value.values, values)

    def test_by_id(self):
        item = self.data_block[self.item_id]
        self.assertIsInstance(item, NameItem)
        self.assertIn(item, self.data_block.values)
        self.assertEqual(item.item_id, self.item_id)

    def test_query(self):
        for item in self.data_block.search(lambda item: item.item_id == self.item_id):
            self.assertIn(item, self.data_block.values)
            self.assertIsInstance(item, NameItem)
            self.assertEqual(item.item_id, self.item_id)

    def test_query_all(self):
        for item in self.data_block.search():
            self.assertIn(item, self.data_block.values)
            self.assertIsInstance(item, NameItem)

    def test_query_values(self):
        for item in self.data_block.search_values(**self.data):
            self.assertIn(item, self.data_block.values)
            self.assertIsInstance(item, NameItem)
            for key, value in self.data.items():
                self.assertEqual(item.values[key], value)

    def test_filtered(self):
        filtered = self.data_block.filtered(**self.data)
        for found in filtered.values:
            self.assertIsInstance(found, NameItem)
            self.assertIn(found, self.data_block.values)
            for key, value in self.data.items():
                self.assertEqual(found.values[key], value)

    def test_random_item(self):
        item_id = self.data_block.get_random_id()
        self.assertIsInstance(item_id, uuid.UUID)

        item = self.data_block[item_id]
        self.assertIsInstance(item, NameItem)
        self.assertIn(item, self.data_block.values)
        self.assertEqual(item.item_id, item_id)

    def test_next_item(self):
        self.assertEqual(iter(self.data_block), self.data_block)
        for _ in range(10):
            item = next(self.data_block)

            self.assertIsInstance(item, NameItem)
            self.assertIn(item, self.data_block.values)

    def test_load_data(self):
        data = {
            uuid.uuid4(): [uuid.uuid4() for _ in range(10)]
            for _ in range(10)
        }

        data_blocks = load_data(data)

        for block_id, block in data_blocks.items():
            self.assertIn(block_id, data.keys())
            block_data = data[block_id]
            for item in block.values:
                self.assertEqual(item.value, block_data[item.item_id])

    def test_fill_data(self):
        data = {
            f'key{block_id}': [uuid.uuid4() for _ in range(10)]
            for block_id in range(10)
        }
        values = {
            uuid.uuid4(): [uuid.uuid4() for _ in range(10)]
            for _ in range(10)
        }

        data_blocks = fill_data(**data)(values)
        for block in data_blocks.values:
            self.assertIn(block.block_id, values.keys())
            self.assertIn(block.value, values[block.block_id])
            self.assertDictEqual(block.values, data)


if __name__ == "__main__":
    unittest.main()

