import unittest
from models.named_model import NamedModel


class TestNamedModel(unittest.TestCase):
    def test_named_model(self):
        model = NamedModel()
        self.assertEqual(model.name, 'NamedModel')
        self.assertEqual(str(model), 'NamedModel')

        model.name = 'Name'
        self.assertEqual(model.name, 'Name')
        self.assertEqual(str(model), 'Name')


if __name__ == "__main__":
    unittest.main()
