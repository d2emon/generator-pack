from models.model import Model


class WorldShape(Model):
    @property
    def field_names(self):
        yield "name"
        yield "description"
