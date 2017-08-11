import random
from . import Generated, DataGenerator
from .data.album import names


class Album(Generated):
    def __repr__(self):
        return "Album: \"%s\"" % (self.generated_text)


class AlbumGenerator(DataGenerator):
    generated_class = Album
    album_names = names

    @classmethod
    def generate_text(cls):
        return random.choice(cls.album_names)
