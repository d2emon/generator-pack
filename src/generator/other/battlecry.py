from generator.generator import ListGenerator
from generator.generator.generated import Generated
from generator.generator.generator_data import FileData


class BattleCry(Generated):
    title = "BattleCry"


class BattleCryGenerator(ListGenerator):
    generated_class = BattleCry
    data = { 'name': FileData("data/battlecry.txt") }
    template = "{name}!"
