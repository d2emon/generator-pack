import unittest
from models.nested_model import Model


class TestNestedModel(unittest.TestCase):
    def setUp(self) -> None:
        class NewModel(Model):
            value = Model.child_property(Model)
            values = Model.children_property(Model)

        self.items = [Model() for _ in range(10)]
        self.model = NewModel(
            'Name',
            *self.items,
            parent="PARENT",
        )
        return super().setUp()

    def test_model(self):
        self.assertEqual(self.model.children, self.items)

    def test_placeholders(self):
        self.model.add_placeholder(Model)
        self.assertEqual(len(self.model.children), len(self.items) + 1)
        for child in self.model.children_by_class(Model):
            self.assertTrue(isinstance(child, Model))

    def test_model_child(self):
        child = Model()

        self.model.add_child(child)
        self.assertIn(child, self.model.children)
        self.assertEqual(child.parent, self.model)

        self.model.remove_child(Model)
        self.model.remove_child(child)
        self.assertNotIn(child, self.model.children)

    def test_tree_model_properties(self):
        self.assertTrue(isinstance(self.model.value, Model))

        for child in self.model.values:
            self.assertIn(child, self.model.children)
            self.assertTrue(isinstance(child, Model))


if __name__ == "__main__":
    unittest.main()
