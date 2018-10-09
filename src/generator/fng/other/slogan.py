from generator.generator.generated import ListGenerated
from generator.generator.data_provider import FileProvider


class Slogan(ListGenerated):
    provider = FileProvider("data/slogan.txt")
