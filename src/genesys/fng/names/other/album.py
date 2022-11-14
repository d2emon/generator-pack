from factories.list_factory import ListFactory
from factories.generator import ListGenerator
from factories.generator import Generated
from data.fixtures.fixtures import names


class Album(Generated):
    title = "Album"


class AlbumGenerator(ListGenerator):
    generated_class = Album
    data = {'name': ListFactory(names.names_data)}
