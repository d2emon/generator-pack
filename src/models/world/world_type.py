from models.model import Model
from models.serializable_model import SerializableModel


class WorldType(SerializableModel, Model):
    value = Model.field_property('world_type', '')
    sizes = Model.field_property('sizes', [])

    @property
    def field_names(self):
        yield "world_type"
        yield "description"
        yield "encounters"
        yield "sizes"
