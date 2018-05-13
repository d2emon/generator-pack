import random
from . import Generated, ListGenerator, ListData
from .data.album import names


class Album(Generated):
    title = "Album"


class AlbumGenerator(ListGenerator):
    generated_class = Album
    data_list = ListData(names)
