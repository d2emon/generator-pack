import unittest
from uuid import uuid4
from models.complex_model import ComplexModel as BaseComplexModel


class ComplexModel(BaseComplexModel):
    children = {
        "child_model_field": BaseComplexModel(value="value1"),
        "child_value_field": "VALUE",
        "pregenerated_child": "OLD_PREGENERATED",
    }

    static_field_names = [
        "value",
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.child_model_field = BaseComplexModel(value="value2")
        self.child_model_field.uuid = uuid4()


class TestComplexModel(unittest.TestCase):
    def test_fill(self):
        model = ComplexModel(value="old value")

        model.fill(value="new value")
        self.assertEqual(model.value, "new value")

    def test_with_children(self):
        model = ComplexModel(
            pregenerated_child="NEW_PREGENERATED"
        )

        for k in model.children.keys():
            if k == "pregenerated_child":
                self.assertEqual(model.data.get(k), "NEW_PREGENERATED")
            else:
                self.assertIsNone(model.data.get(k))

        with_children = model.with_children()

        self.assertEqual(with_children, model)

        for k in model.children.keys():
            self.assertIsNotNone(with_children.data.get(k))


if __name__ == "__main__":
    unittest.main()
