import random
import unittest
from factories.list_factory import ListFactory


class TestListFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [random.uniform(0, 100) for _ in range(10)]
        self.factory = ListFactory(self.values)

    def test_list_factory(self):
        self.assertEqual(self.factory.data, self.values)
        self.assertIn(self.factory(), self.values)

    def test_list_factory_length(self):
        self.assertEqual(len(self.factory), 10)

    def test_list_factory_shuffle(self):
        used = []
        for item in self.factory.shuffle():
            self.assertIn(item, self.values)
            self.assertNotIn(item, used)
            used.append(item)

    def test_list_factory_unique(self):
        used = []
        for item in self.factory.unique(5):
            self.assertIn(item, self.values)
            self.assertNotIn(item, used)
            used.append(item)


if __name__ == "__main__":
    unittest.main()
