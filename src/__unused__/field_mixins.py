from models.model import Model


class WithDescription(Model):
    field_names = [
        'description',
    ]

    name = Model.field_property('description', '')
