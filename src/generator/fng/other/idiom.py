from generator.generator.generated import ListGenerated
from generator.generator.data_provider import FileProvider


class Idiom(ListGenerated):
    provider = FileProvider("data/idiom.txt")
