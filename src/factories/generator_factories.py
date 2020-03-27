class ListFactory:
    # factories.generator.ListGenerator
    pass


class MarkovFactory:
    # factories.generator.MarkovGenerator
    def __init__(self):
        self.name = ''


class FileFactory:
    # factories.generator.FileData
    def __init__(self, filename):
        self.filename = filename
