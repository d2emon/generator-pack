from . import Generated, FileGenerator


class World(Generated):
    title = "World"


class WorldGenerator(FileGenerator):
    generated_class = World
    data_file = "data/world.txt"
