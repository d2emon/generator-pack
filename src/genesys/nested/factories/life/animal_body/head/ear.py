from models.v5 import life
from ..body_parts import SoftBodyPartFactory


class EarFactory(SoftBodyPartFactory):
    default_model = life.Ear
