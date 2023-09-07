import os
import random
import unittest
from unittest.mock import patch, mock_open
from factories.list_factory import ListFactory


class TestListFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [random.uniform(0, 100) for _ in range(10)]
        self.factory = ListFactory(self.values)

    def test_list_factory(self):
        self.assertEqual(self.factory.data, self.values)
        self.assertIn(self.factory(), self.values)

    def test_list_factory_length(self):
        self.assertEqual(len(self.factory), 10)

    def test_list_factory_shuffle(self):
        used = []
        for item in self.factory.shuffle():
            self.assertIn(item, self.values)
            self.assertNotIn(item, used)
            used.append(item)

    def test_list_factory_unique(self):
        used = []
        for item in self.factory.unique(5):
            self.assertIn(item, self.values)
            self.assertNotIn(item, used)
            used.append(item)

    def test_from_text_file(self):
        text_values = [str(value) for value in self.values]
        text = '\n'.join(text_values)
        current_path = os.path.abspath(os.path.join(os.path.curdir))
        filename = str(random.uniform(0, 100))
        full_path = os.path.join(current_path, filename)

        with patch("builtins.open", mock_open(read_data=text)) as mock_open_file:
            factory = ListFactory.from_text_file(filename)
            self.assertEqual(factory.data, text_values)

        mock_open_file.assert_called_with(full_path, 'r', encoding='utf-8')


if __name__ == "__main__":
    unittest.main()
