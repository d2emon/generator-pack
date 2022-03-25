from models.model import Model


class WorldSize(Model):
    value = Model.field_property('size_class', '')
    size_class = Model.field_property('size_class', '')
    name = Model.field_property('name', '')
    size = Model.field_property('size', '')

    @property
    def field_names(self):
        yield "max_size"
        yield "min_size"
        yield "name"
        yield "size_class"
        yield "size"

    @property
    def max_size(self):
        value = self.data.get('max_size', None)
        return int(value) if value else self.min_size

    @property
    def min_size(self):
        value = self.data.get('min_size', 0)
        return int(value) if value else 0

    @property
    def text(self):
        return "\n".join([
            f"Класс размера:\t{self.size_class}",
            f"Описание:\t\t{self.name}",
            f"Размер:\t\t\t{self.size}",
        ])
