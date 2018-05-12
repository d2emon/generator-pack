from . import Generated, FileGenerator


class BattleCry(Generated):
    def __repr__(self):
        return "BattleCry: \"%s\"" % (self.generated_value)


class BattleCryGenerator(FileGenerator):
    generated_class = BattleCry
    data_file = "data/battlecry.txt"
    text_format = "%s!"
