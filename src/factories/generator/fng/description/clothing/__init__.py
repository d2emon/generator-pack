import random
from factories.factory import Factory
from genesys.fng.v0.character import Male, Female
from .jacket import JacketFactory
from .shirt import ShirtGenerator
from .belt import BeltGenerator, FemaleBeltGenerator
from .pants import PantsGenerator
from .shoes import ShoesGenerator
from .dress import DressGenerator
from .models import MaleClothing, FemaleClothing


class ClothingFactory(Factory):
    def __init__(self):
        self.providers = {
            Male: MaleClothingFactory(),
            Female: FemaleClothingFactory(),
        }

    def get_provider(self, gender=None):
        gender = gender or random.choice(self.providers.keys())
        provider = self.providers.get(gender)
        return next(provider) if provider else None

    def __next__(self):
        return self.get_provider()


class BaseClothingFactory(Factory):
    def __next__(self):
        return MaleClothing(
            jacket=next(JacketFactory()),
            shirt=next(ShirtFactory()),
            belt=next(BeltFactory()),
            pants=next(PantsFactory()),
            shoes=next(ShoesFactory()),
            # if model.sex == 1:
            #     specials = female_specials
            # else:
            #     specials = male_specials
            # special_generator = random.choice(specials)

            # g = model.race.generators(self.sex)
            # model.hair = g.hair.generate()
            # model.face = g.face.generate()
            # model.eyes = g.eyes.generate()
            # model.promise = g.promise.generate()
            # model.special = special_generator.generate()
            # model.name = g.name.generate()
            # model.frame = self.frame_generator.generate()
            # model.strange = self.strange_generator.generate()
            # model.attitude = g.attitude.generate()
        )


class MaleClothingFactory(Factory):
    def __next__(self):
        return MaleClothing(
            jacket=next(JacketFactory()),
            shirt=next(ShirtFactory()),
            belt=next(BeltFactory()),
            pants=next(PantsFactory()),
            shoes=next(ShoesFactory()),
        )


class FemaleClothingFactory(Factory):
    def __next__(self):
        return FemaleClothing(
            dress=next(DressFactory),
            underdress=next(DressFactory()),
            # jacket=next(JacketFactory),
            # shirt=next(ShirtFactory),
            belt=next(FemaleBeltFactory),

            # pants=next(PantsFactory)
            # shoes=next(ShoesFactory)
        )
