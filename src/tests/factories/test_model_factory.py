import unittest
from factories.model_factory import ModelFactory
from models.model import Model


class TestModelFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.factory = ModelFactory()

    def test_model_factory(self):
        self.assertEqual(self.factory.model, Model)

        item = self.factory()
        self.assertIsInstance(item, Model)


if __name__ == "__main__":
    unittest.main()
