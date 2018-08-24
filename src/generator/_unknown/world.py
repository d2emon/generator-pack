from generator.generator import ListGenerator
from generator.generator.generated import Generated
from generator.generator.generator_data import FileData


class World(Generated):
    title = "World"


class WorldGenerator(ListGenerator):
    generated_class = World
    data = { 'name': FileData("data/world.txt") }
