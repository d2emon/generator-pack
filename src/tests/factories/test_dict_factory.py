import random
import unittest
from factories.list_factory import ListFactory
from factories.dict_factory import DictFactory


class TestDictFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [random.uniform(0, 100) for _ in range(10)]
        self.list_factory_1 = ListFactory(self.values)
        self.list_factory_2 = ListFactory(self.values)
        self.factories = {
            "list_factory_1": self.list_factory_1,
            "list_factory_2": self.list_factory_2,
        }
        self.factory = DictFactory(**self.factories)

    def test_dict_factory(self):
        self.assertEqual(self.factory.factories, self.factories)

        for key, value in self.factories.items():
            self.assertEqual(self.factory.factory(key), value)

        values = self.factory()
        self.assertIsInstance(values, dict)
        for key, value in values.items():
            self.assertIn(key, self.factories.keys())
            self.assertIn(value, self.values)

    def test_dict_factory_length(self):
        self.assertEqual(len(self.factory), 2)


if __name__ == "__main__":
    unittest.main()
