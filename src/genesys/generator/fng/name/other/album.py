from genesys.generator import ListGenerator
from genesys.generator import Generated
from genesys.generator import ListData
from sample_data.fixtures import names


class Album(Generated):
    title = "Album"


class AlbumGenerator(ListGenerator):
    generated_class = Album
    data = { 'name': ListData(names) }
