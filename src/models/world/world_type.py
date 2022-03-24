from models.complex_model import ComplexModel


class WorldType(ComplexModel):
    field_names = [
        'world_type',
        'description',
        'encounters',
        'sizes',
    ]

    value = property(lambda self: self.data.get('world_type', ''))
    sizes = property(lambda self: self.data.get('sizes', []))
