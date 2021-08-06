import os
from factories import DictFactory
from providers.file_provider import FileProvider
from v3.models import ComplexModel


class WorldDataProvider:
    def __init__(self):
        self.__name = FileProvider(os.path.join('data', 'world.txt'))

    @property
    def name(self):
        return self.__name


class World(ComplexModel):
    fields = [
        'name',
    ]

    def __str__(self):
        return str(self['name'])


class WorldFactory(DictFactory):
    def __init__(self, provider=None):
        super().__init__(provider or WorldDataProvider())
        self.data = {
            'name': self.provider.name,
        }

    @property
    def model_class(self):
        return World
