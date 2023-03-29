from models.field_mixins import WithName


class WorldShape(WithName):
    field_names = [
        *WithName.field_names,
        'description',
    ]

    description = WithName.field_property('description', '')
