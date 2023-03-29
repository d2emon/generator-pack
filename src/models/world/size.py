from models.model import Model
from models.field_mixins import WithName


class WorldSize(WithName):
    field_names = [
        *WithName.field_names,
        'max_size',
        'min_size',
        'size',
        'size_class',
    ]

    size = WithName.field_property('size', '')
    size_class = WithName.field_property('size_class', '')

    value = WithName.field_property('size_class', '')

    @property
    def max_size(self):
        value = self.data.get('max_size', None)
        return int(value) if value else self.min_size

    @property
    def min_size(self):
        value = self.data.get('min_size', 0)
        return int(value) if value else 0

    @property
    def description(self):
        return "\n".join([
            f"Класс размера:\t{self.size_class}",
            f"Описание:\t\t{self.name}",
            f"Размер:\t\t\t{self.size}",
        ])
