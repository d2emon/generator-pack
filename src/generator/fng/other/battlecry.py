from generator.generator.generated import ListGenerated
from generator.generator.generator_data import FileData


class BattleCry(ListGenerated):
    data = {'value': FileData("data/battlecry.txt")}

    def __str__(self):
        return "{}!".format(self.value)
