from generator.generator.generated import ListGenerated
from generator.generator.generator_data import FileData


class Curse(ListGenerated):
    data = {'value': FileData("data/swear.txt")}
