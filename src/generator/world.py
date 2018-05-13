from .generator import FileGenerator
from .generator.generated import Generated


class World(Generated):
    title = "World"


class WorldGenerator(FileGenerator):
    generated_class = World
    data_file = "data/world.txt"
