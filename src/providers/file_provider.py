import os
from .list_provider import ListProvider
from utils.loaders import load_lines


class FileProvider(ListProvider):
    def __init__(self, filename=""):
        self.filename = os.path.abspath(os.path.join("../factories", filename))
        data = load_lines(self.filename)
        super().__init__(data)
