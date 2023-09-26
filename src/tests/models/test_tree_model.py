import unittest
from models.nested_model import TreeModel


class TestTreeModel(unittest.TestCase):
    def setUp(self) -> None:
        class NewTreeModel(TreeModel):
            value = TreeModel.child_property(TreeModel)

        self.items = [TreeModel() for _ in range(10)]
        self.model = NewTreeModel(*self.items, parent="PARENT")
        return super().setUp()

    def test_tree_model(self):
        self.assertEqual(self.model.children, self.items)
        self.assertEqual(self.model.parent, 'PARENT')

    def test_tree_model_children(self):
        new_items = [TreeModel() for _ in range(10)]
        self.model.children = new_items
        self.assertEqual(self.model.children, new_items)

        for child in self.model.children_by_class(TreeModel):
            self.assertTrue(isinstance(child, TreeModel))

    def test_tree_model_child(self):
        child = TreeModel()

        self.model.add_child(child)
        self.assertIn(child, self.model.children)
        self.assertEqual(child.parent, self.model)

        self.model.remove_child(TreeModel)
        self.model.remove_child(child)
        self.assertNotIn(child, self.model.children)

    def test_tree_model_properties(self):
        self.assertTrue(isinstance(self.model.value, TreeModel))

        for child in self.model.values:
            self.assertIn(child, self.model.children)
            self.assertTrue(isinstance(child, TreeModel))


if __name__ == "__main__":
    unittest.main()
