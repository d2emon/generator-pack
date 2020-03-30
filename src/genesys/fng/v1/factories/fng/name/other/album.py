from factories.factory import ListFactory
from factories.generator import ListGenerator
from factories.generator import Generated
from sample_data.fixtures import names


class Album(Generated):
    title = "Album"


class AlbumGenerator(ListGenerator):
    generated_class = Album
    data = {'name': ListFactory(None, names)}
