import unittest
from models.nested_model import NestedModel


class TestNestedModel(unittest.TestCase):
    def setUp(self) -> None:
        class NewModel(NestedModel):
            value = NestedModel.child_property(NestedModel)
            values = NestedModel.children_property(NestedModel)

        self.items = [NestedModel() for _ in range(10)]
        self.model = NewModel(
            'Name',
            *self.items,
            parent="PARENT",
        )
        return super().setUp()

    def test_model(self):
        self.assertEqual(self.model.children, self.items)

    def test_placeholders(self):
        self.model.add_placeholder(NestedModel)
        self.assertEqual(len(self.model.children), len(self.items) + 1)
        for child in self.model.children_by_class(NestedModel):
            self.assertTrue(isinstance(child, NestedModel))

    def test_model_child(self):
        child = NestedModel()

        self.model.add_child(child)
        self.assertIn(child, self.model.children)
        self.assertEqual(child.parent, self.model)

        self.model.remove_child(NestedModel)
        self.model.remove_child(child)
        self.assertNotIn(child, self.model.children)

    def test_tree_model_properties(self):
        self.assertTrue(isinstance(self.model.value, NestedModel))

        for child in self.model.values:
            self.assertIn(child, self.model.children)
            self.assertTrue(isinstance(child, NestedModel))


if __name__ == "__main__":
    unittest.main()
