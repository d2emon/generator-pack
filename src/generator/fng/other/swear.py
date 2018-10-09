from generator.generator.generated import ListGenerated
from generator.generator.data_provider import FileProvider


class Curse(ListGenerated):
    provider = FileProvider("data/swear.txt")
