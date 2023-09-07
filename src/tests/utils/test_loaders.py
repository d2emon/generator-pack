import os
import random
import unittest
from unittest.mock import patch, mock_open
from utils.loaders import load_lines, load_text


class TestLoaders(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [str(random.uniform(0, 100)) for _ in range(10)]
        self.text = '\n'.join(self.values)
        self.current_path = os.path.abspath(os.path.join(os.path.curdir))
        self.filename = str(random.uniform(0, 100))
        self.full_path = os.path.join(self.current_path, self.filename)

    def test_load_lines(self):
        with patch("builtins.open", mock_open(read_data=self.text)) as mock_open_file:
            for line in load_lines(self.filename):
                self.assertIn(line, self.values)

        mock_open_file.assert_called_with(self.full_path, 'r', encoding='utf-8')

    def test_load_text(self):
        with patch("builtins.open", mock_open(read_data=self.text)) as mock_open_file:
            text = load_text(self.filename)
            self.assertEqual(text, self.text)

        mock_open_file.assert_called_with(self.full_path, 'r', encoding='utf-8')


if __name__ == "__main__":
    unittest.main()
