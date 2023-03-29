from models.named_model import NamedModel


class WorldShape(NamedModel):
    field_names = [
        *NamedModel.field_names,
        'description',
    ]

    description = NamedModel.field_property('description', '')
