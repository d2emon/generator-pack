import random
from .generator import ListGenerator
from .generator.generated import Generated
from .generator.generator_data import ListData
from data.album import names


class Album(Generated):
    title = "Album"


class AlbumGenerator(ListGenerator):
    generated_class = Album
    data_list = ListData(names)
