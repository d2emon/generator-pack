from generator.generator.generated import ListGenerated
from generator.generator.generator_data import FileData


class Motto(ListGenerated):
    data = {'value': FileData("data/motto.txt")}
