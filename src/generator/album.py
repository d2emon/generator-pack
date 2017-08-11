import random
from . import Generated, ListGenerator
from .data.album import names


class Album(Generated):
    def __repr__(self):
        return "Album: \"%s\"" % (self.generated_text)


class AlbumGenerator(ListGenerator):
    generated_class = Album
    data_list = names
