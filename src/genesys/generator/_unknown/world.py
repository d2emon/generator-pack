from genesys.generator import ListGenerator
from genesys.generator import Generated
from genesys.generator import FileData


class World(Generated):
    title = "World"


class WorldGenerator(ListGenerator):
    generated_class = World
    data = { 'name': FileData("data/world.txt") }
