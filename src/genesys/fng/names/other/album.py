from data.fixtures.fixtures import names
from factories.list_factory import ListFactory
from models.fng.names.name import Name


class Album(Name):
    title = "Album"


class AlbumGenerator(ListFactory):
    generated_class = Album
    data = {'name': ListFactory(names.names_data)}
