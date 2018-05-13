from .generator import FileGenerator
from .generator.generated import Generated


class BattleCry(Generated):
    title = "BattleCry"


class BattleCryGenerator(FileGenerator):
    generated_class = BattleCry
    data_file = "data/battlecry.txt"
    text_format = "%s!"
