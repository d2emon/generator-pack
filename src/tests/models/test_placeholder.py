import random
import unittest
from models.model import Model
from models.placeholder import Placeholder


class Factory:
    def build(self):
        return Model()


class TestPlaceholder(unittest.TestCase):
    def test_placeholder(self):
        placeholder = Placeholder(Factory())

        self.assertEqual(placeholder.placeholder, placeholder)
        self.assertEqual(placeholder.model.__class__, Model)
        self.assertEqual(placeholder.build(), placeholder.model)

        model = Model()
        placeholder.model = model
        self.assertEqual(placeholder.model, model)



if __name__ == "__main__":
    unittest.main()
