from models.model import Model


class WorldType(Model):
    value = Model.field_property('world_type', '')
    sizes = Model.field_property('sizes', [])

    @property
    def field_names(self):
        yield "world_type"
        yield "description"
        yield "encounters"
        yield "sizes"
