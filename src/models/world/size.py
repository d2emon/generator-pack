import random
from models.complex_model import ComplexModel


class WorldSize(ComplexModel):
    field_names = [
        'name',
        'size_class',
        'size',
        'min_size',
        'max_size',
    ]

    value = property(lambda self: self.data.get('size_class', ''))
    size_class = property(lambda self: self.data.get('size_class', ''))
    name = property(lambda self: self.data.get('name', ''))
    size = property(lambda self: self.data.get('size', ''))

    @property
    def min_size(self):
        value = self.data.get('min_size', 0)
        return int(value) if value else 0

    @property
    def max_size(self):
        value = self.data.get('max_size', None)
        return int(value) if value else self.min_size

    @property
    def text(self):
        return "\n".join([
            f"Класс размера:\t{self.size_class}",
            f"Описание:\t\t{self.name}",
            f"Размер:\t\t\t{self.size}",
        ])
