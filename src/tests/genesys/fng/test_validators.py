import unittest
import uuid
from genesys.fng.validators import item_is_not_unique, item_equals, generate_while


class TestValidators(unittest.TestCase):
    def test_item_is_not_unique(self):
        data = [uuid.uuid4() for _ in range(10)]
        validator = item_is_not_unique(data)
        self.assertFalse(validator(uuid.uuid4()))
        for item in data:
            self.assertTrue(validator(item))

    def test_item_equals(self):
        data = uuid.uuid4()
        validator = item_equals(str(data))
        self.assertFalse(validator(uuid.uuid4()))
        self.assertTrue(validator(data))

    def test_generate_while(self):
        def validator(item):
            return item is not None

        value = None
        result = generate_while(
            value,
            validator,
            uuid.uuid4,
        )

        self.assertNotEqual(result, validator)
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()
