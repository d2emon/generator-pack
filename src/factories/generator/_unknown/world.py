from factories.generator import ListGenerator
from factories.generator import Generated
from factories.generator import FileData


class World(Generated):
    title = "World"


class WorldGenerator(ListGenerator):
    generated_class = World
    data = { 'name': FileData("data/world.txt") }
