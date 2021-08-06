from v3.models import ComplexModel


class WorldType(ComplexModel):
    field_names = [
        'world_type',
        'description',
        'encounters',
        'sizes',
    ]

    value = property(lambda self: self.data.get('world_type', ''))
    sizes = property(lambda self: self.data.get('sizes', []))
