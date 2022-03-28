from generated import life
from factories.nested_factory import NestedFactory as Factory
from .body_parts import BodyPartFactory, FleshFactory
from .skeleton import BonesFactory
from .head import EyeFactory, SkullFactory


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


class BeakFactory(BonesFactory):
    default_model = life.Beak


class BirdHeadFactory(BodyPartFactory):
    default_model = life.BirdHead

    @classmethod
    def mouth(cls):
        yield BeakFactory()

    @classmethod
    def nose(cls):
        yield None

    @classmethod
    def eyes(cls):
        yield from EyeFactory().multiple(2)

    @classmethod
    def ears(cls):
        yield None

    @classmethod
    def skull(cls):
        yield SkullFactory()

    @classmethod
    def fur(cls):
        # Feathers
        yield None

    def children(self):
        yield from self.mouth()
        yield from self.nose()
        yield from self.eyes()
        yield from self.ears()
        yield from self.skull()
        yield from self.fur()
        yield from super().children()


class BirdBodyFactory(Factory):
    default_model = life.BirdBody

    def children(self):
        yield BirdHeadFactory()
        # Feathers
        yield from BirdLegFactory().multiple(2)
        yield from BirdWingFactory().multiple(2)
        yield BirdTailFactory()
        yield FleshFactory()
