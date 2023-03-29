from models.named_model import NamedModel


class WorldSize(NamedModel):
    field_names = [
        *NamedModel.field_names,
        'max_size',
        'min_size',
        'size',
        'size_class',
    ]

    size = NamedModel.field_property('size', '')
    size_class = NamedModel.field_property('size_class', '')

    value = NamedModel.field_property('size_class', '')

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
