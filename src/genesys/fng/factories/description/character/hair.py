from genesys.fng.factories.name_factory import NameFactory
from models.fng.description import Hair


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
