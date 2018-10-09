from generator.generator.generated import ListGenerated
from generator.generator.data_provider import FileProvider


class Motto(ListGenerated):
    provider = FileProvider("data/motto.txt")
