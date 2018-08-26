from generator.generator.generated import ListGenerated
from generator.generator.generator_data import FileData


class Slogan(ListGenerated):
    data = {'value': FileData("data/slogan.txt")}
