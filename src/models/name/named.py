from ..model import Model


class Named(Model):
    value = Model.field_property('name', '')

    name = Model.field_property('name', '')

    def __init__(self, name = '', *args, **kwargs):
        super().__init__(*args, name=name, **kwargs)

    @property
    def field_names(self):
        yield 'name'
