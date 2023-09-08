import unittest
from factories.thing.nested_factory import NestedFactory
from models.model import Model


class TestNestedFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.factory = NestedFactory(provider=None)

    def test_nested_factory(self):
        self.assertEqual(self.factory.model, Model)

        # item = self.factory()
        # self.assertIsNone(item)


if __name__ == "__main__":
    unittest.main()
