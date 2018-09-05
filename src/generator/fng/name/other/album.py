from generator.generator import ListGenerator
from generator.generator.generated import Generated
from generator.generator.generator_data import ListData
from fixtures.media.album import names


class Album(Generated):
    title = "Album"


class AlbumGenerator(ListGenerator):
    generated_class = Album
    data = { 'name': ListData(names) }
