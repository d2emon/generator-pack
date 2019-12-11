from genesys.generator import ListGenerator
from genesys.generator import Generated
from genesys.generator import ListData
from fixtures.media import names


class Album(Generated):
    title = "Album"


class AlbumGenerator(ListGenerator):
    generated_class = Album
    data = { 'name': ListData(names) }
