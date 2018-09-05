from generator.generator.generated import ListGenerated
from generator.generator.generator_data import FileData


class Idiom(ListGenerated):
    data = {'value': FileData("data/idiom.txt")}
