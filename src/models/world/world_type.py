from models.model import Model


class WorldType(Model):
    value = Model.field_property('world_type', '')

    encounters = Model.field_property('encounters', [])
    sizes = Model.field_property('sizes', [])
    description = Model.field_property('description', '')

    @property
    def field_names(self):
        yield "description"
        yield "encounters"
        yield "sizes"
        yield "world_type"
