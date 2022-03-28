from models.model import Model


class WorldShape(Model):
    value = Model.field_property('name', '')

    description = Model.field_property('description', '')

    @property
    def field_names(self):
        yield "description"
        yield "name"
