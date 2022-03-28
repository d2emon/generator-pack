import unittest
from factories.nested_factory import NestedFactory
from models.model import Model


class TestNestedFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.factory = NestedFactory()

    def test_nested_factory(self):
        self.assertIsNone(self.factory.model)

        # item = self.factory()
        # self.assertIsNone(item)


if __name__ == "__main__":
    unittest.main()
