import random
import unittest
from orm.models.data_item import DataItem


class TestDataItem(unittest.TestCase):
    def setUp(self):
        self.data = [ random.uniform(0, 100) for _ in range(10) ]
        self.data_item = DataItem()

    def test_data_item(self):
        self.assertIn('group_id', DataItem.fields)
        self.assertIn('value', DataItem.fields)
        self.assertIsInstance(DataItem.items, list)

    def test_group_id(self):
        self.assertEqual(self.data_item.group_id, self.data_item['group_id'])

    def test_value(self):
        self.assertEqual(self.data_item.value, self.data_item['value'])

    def test_save(self):
        before = len(DataItem.items)
        self.data_item.save()
        self.assertEqual(len(DataItem.items), before + 1)
        self.assertEqual(DataItem.items[-1], self.data_item)

    def test_all(self):
        for item in DataItem.all():
            self.assertIn(item, DataItem.items)

    def test_query(self):
        DataItem(value="To Search", search="SEARCH").save()

        for item in DataItem.all(lambda item: item["search"] == "SEARCH"):
            self.assertEqual(item["search"], "SEARCH")

    def test_add_values(self):
        DataItem.add_values('GROUP_ID', self.data)

        for item in DataItem.items[-10:]:
            self.assertIn(item.value, self.data)

    def test_by_group_id(self):
        DataItem.add_values('GROUP_ID1', self.data)

        values = []
        for item in DataItem.by_group_id('GROUP_ID1'):
            self.assertEqual(item['group_id'], 'GROUP_ID1')
            values.append(item.value)

        for item in self.data:
            self.assertIn(item, values)

    def test_values_by_group_id(self):
        DataItem.add_values('GROUP_ID2', self.data)

        values = list(DataItem.values_by_group_id('GROUP_ID2'))

        for item in self.data:
            self.assertIn(item, values)


if __name__ == "__main__":
    unittest.main()
