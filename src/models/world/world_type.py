from models.model import Model


class WorldType(Model):
    field_names = [
        'description',
        'encounters',
        'sizes',
        'world_type',
    ]
    value_field_name = 'world_type'

    world_type = Model.field_property('world_type')
    encounters = Model.field_property('encounters', [])
    sizes = Model.field_property('sizes', [])
    description = Model.field_property('description', '')
