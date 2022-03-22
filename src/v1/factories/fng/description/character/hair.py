from v1.factories.fng.name_factory import NameFactory
from v1.models.fng.description import Hair


class HairFactory(NameFactory):
    child_class = Hair
    blocks_map = {
        'color': 'color',
        'hair_type': 'hair_type',
        'style': 'style',
    }


# TODO: Remove it
class MaleHairFactory(HairFactory):
    pass


class FemaleHairFactory(HairFactory):
    pass
