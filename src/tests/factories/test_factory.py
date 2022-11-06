import random
import unittest
from factories.factory import Factory as BaseFactory


class Factory(BaseFactory):
    def __call__(self, *args, **kwargs):
        return "Result"


class TestFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [random.uniform(0, 100) for _ in range(10)]

    def test_instance(self):
        factory = Factory.instance()
        self.assertIsInstance(factory, Factory)
        self.assertEqual(factory.instance(), factory)

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


if __name__ == "__main__":
    unittest.main()
