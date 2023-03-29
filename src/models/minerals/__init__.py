from models.named_model import NamedModel


class Mineral(NamedModel):
    field_names = [
        *NamedModel.field_names,
        'silicon',
        'oxygen',
        'lipids',
    ]


class Silica(Mineral):
    silicon = Mineral.field_property('silicon')
    oxygen = Mineral.field_property('oxygen')


class Oil(Mineral):
    # OrganicMatter
    lipids = Mineral.field_property('lipids')


class Rock(Mineral):
    field_names = [
        *Mineral.field_names,
        'silica',
        'aluminium',
        'iron',
        'potassium',
        'sodium',
        'calcium',
        # Additional
        'carbon',
        'lipids',
    ]

    silica = Mineral.field_property('silica')
    aluminium = Mineral.field_property('aluminium')
    iron = Mineral.field_property('iron')
    potassium = Mineral.field_property('potassium')
    sodium = Mineral.field_property('sodium')
    calcium = Mineral.field_property('calcium')


class Diamond(Rock):
    carbon = Rock.field_property('carbon')


class Magma(Rock):
    pass
