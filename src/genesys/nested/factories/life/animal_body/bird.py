from generated import life
from .body_parts import BodyPartFactory


class BirdLimbFactory(BodyPartFactory):
    def children(self):
        # Feathers
        yield from super().children()


class BirdWingFactory(BirdLimbFactory):
    default_model = life.BirdWing


class BirdLegFactory(BirdLimbFactory):
    default_model = life.BirdLeg


class BirdTailFactory(BirdLimbFactory):
    default_model = life.BirdTail
