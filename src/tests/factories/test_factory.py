import random
import unittest
from factories.factory import Factory as BaseFactory
from factories.list_factory import ListFactory
from factories.model_factory import ModelFactory
from models.model import Model


class Factory(BaseFactory):
    def __call__(self, *args, **kwargs):
        return "Result"


class TestFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [random.uniform(0, 100) for _ in range(10)]

    def test_next(self):
        factory = Factory()
        self.assertEqual(iter(factory), factory)
        self.assertEqual(factory(), "Result")
        self.assertEqual(next(factory), "Result")

    def test_items(self):
        factory = Factory()
        items = list(factory.items(10))
        self.assertEqual(len(items), 10)
        for item in items:
            self.assertEqual(item, "Result")

    def test_list_factory(self):
        factory = ListFactory(self.values)
        self.assertEqual(len(factory), 10)
        self.assertEqual(factory.data, self.values)
        self.assertIn(factory.build(), self.values)
        self.assertIn(factory(), self.values)

    def test_list_factory_shuffle(self):
        factory = ListFactory(self.values)
        used = []
        for item in factory.shuffle():
            self.assertIn(item, self.values)
            self.assertNotIn(item, used)
            used.append(item)

    def test_list_factory_unique(self):
        factory = ListFactory(self.values)
        used = []
        for item in factory.unique(5):
            self.assertIn(item, self.values)
            self.assertNotIn(item, used)
            used.append(item)

    def test_model_factory(self):
        factory = ModelFactory(self.values)
        self.assertEqual(factory.data, self.values)
        self.assertEqual(factory.model_class, Model)

        item = factory()
        self.assertIsInstance(item, Model)


if __name__ == "__main__":
    unittest.main()
