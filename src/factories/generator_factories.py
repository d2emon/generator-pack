class ListData:
    # factories.generator.ListData
    def __init__(self, *args):
        self.args = args

    def __next__(self):
        return ''


class DataFactory:
    # factories.generator.DataGenerator
    pass


class ListFactory:
    # factories.generator.ListGenerator
    @classmethod
    def generated(cls):
        return ''

    @classmethod
    def generate_value(cls, *args, **kwargs):
        return ''


class PercentFactory:
    # factories.generator.PercentGenerator
    pass


class TemplateFactory:
    # factories.generator.TemplateGenerator
    pass


class MarkovFactory:
    # factories.generator.MarkovGenerator
    def __init__(self):
        self.name = ''


class FileFactory:
    # factories.generator.FileData
    def __init__(self, filename):
        self.filename = filename
