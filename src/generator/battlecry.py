from . import Generated, ListGenerator
from .data.battlecry import names


class BattleCry(Generated):
    def __repr__(self):
        return "BattleCry: \"%s\"" % (self.generated_text)


class BattleCryGenerator(ListGenerator):
    generated_class = BattleCry
    data_list = names
    text_format = "%s!"
