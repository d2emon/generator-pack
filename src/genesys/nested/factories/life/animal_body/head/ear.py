from generated import life
from genesys.nested.factories.life.animal_body.body_parts import SoftBodyPartFactory


class EarFactory(SoftBodyPartFactory):
    default_model = life.Ear
