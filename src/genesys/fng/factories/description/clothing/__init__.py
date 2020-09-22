from genesys.fng.factories.factory import Factory
from genesys.fng.models.description.clothing import MaleClothing, FemaleClothing
from genesys.fng.providers.description.clothing import DataProvider
from genesys.generator_models.character import Male, Female

from .jacket import JacketFactory
from .shirt import ShirtFactory
from .belt import BeltFactory, FemaleBeltFactory
from .pants import PantsFactory
from .shoes import ShoesFactory
from .dress import DressFactory


class BaseClothingFactory(Factory):
    class DataProvider(DataProvider):
        pass

    def __next__(self):
        return MaleClothing(
            # race=next(self.providers.races)
            # mark = next(self.providers.marks)
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


class MaleClothingFactory(BaseClothingFactory):
    def __next__(self):
        return MaleClothing(
            jacket=next(JacketFactory()),
            shirt=next(ShirtFactory()),
            belt=next(BeltFactory()),
            pants=next(PantsFactory()),
            shoes=next(ShoesFactory()),
        )


class FemaleClothingFactory(BaseClothingFactory):
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


class ClothingFactory(Factory):
    class DataProvider(DataProvider):
        pass

    def get_factory(self, gender=None):
        factories = {
            Male: MaleClothingFactory(self.provider),
            Female: FemaleClothingFactory(self.provider),
        }
        gender = gender or next(self.provider.genders)
        return factories.get(gender)

    def __next__(self):
        factory = self.get_factory()
        return next(factory) if factory else None
