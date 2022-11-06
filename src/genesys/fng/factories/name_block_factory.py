import random
from .name_factory import ComplexFactory, ComplexNameFactory
from utils import genders


class SimpleNameBlockFactory(ComplexFactory):
    def build10(self, *args, **kwargs):
        """
        Build 10 models

        :param count: Count of models
        :param args: Model args
        :param kwargs: Fields to search in data
        :return: Models, built by factory
        """
        for _ in range(10):
            yield self(*args, **kwargs)


class NameBlockFactory(ComplexFactory):
    def __get_percent(self):
        return random.uniform(0.0, 100.0)

    def by_percent_2(self, percent):
        if percent < 50:
            return self.factories[0]
        if percent < 100:
            return self.factories[1]
        
        return None

    def by_percent_3(self, percent):
        if percent < 40:
            return self.factories.get(0)
        if percent < 70:
            return self.factories.get(1)
        if percent < 100:
            return self.factories.get(2)

        return None

    def by_percent(self, percent):
        if len(self.factories) == 1:
            return self.factories[0]

        if len(self.factories) == 2:
            return self.by_percent_2(percent)

        if len(self.factories) == 3:
            return self.by_percent_3(percent)

        raise NotImplementedError()

    def __call__(self, *args, percent=None, **kwargs):
        if percent is None:
            percent = self.__get_percent()

        factory = self.by_percent(percent)
        return factory(*args, **kwargs)

    def build10(self, *args, **kwargs):
        """
        Build 10 models

        :param count: Count of models
        :param args: Model args
        :param kwargs: Fields to search in data
        :return: Models, built by factory
        """
        for item_id in range(10):
            yield self(*args, percent=item_id * 10, **kwargs)


class GenderNameBlockFactory(NameBlockFactory):
    class MaleNameFactory(ComplexNameFactory):
        pass

    class FemaleNameFactory(ComplexNameFactory):
        pass

    class NeutralNameFactory(ComplexNameFactory):
        pass

    @property
    def genders(self):
        return self.factories.keys()

    @classmethod
    def get_factories(cls, factory_data):
        return {
            genders.MALE: cls.MaleNameFactory(factory_data),
            genders.FEMALE: cls.FemaleNameFactory(factory_data),
            genders.NEUTRAL: cls.NeutralNameFactory(factory_data),
        }

    def __get_gender(self):
        return genders.MALE

    def factory(self, gender=None):
        return self.factories.get(gender if gender is not None else self._get_gender())

    def by_percent(self, percent):
        return self.factory(percent)

    def __call__(self, *args, gender=None, **kwargs):
        return self.from_factory(
            gender if gender is not None else self.__get_gender(),
            *args,
            **kwargs,
        )

    def build10(self, *args, **kwargs):
        """
        Build 10 models

        :param count: Count of models
        :param args: Model args
        :param kwargs: Fields to search in data
        :return: Models, built by factory
        """
        for gender in self.genders:
            yield ''
            if gender == genders.MALE:
                yield 'MALE'
            elif gender == genders.FEMALE:
                yield 'FEMALE'
            elif gender == genders.NEUTRAL:
                yield 'NEUTRAL'
            else:
                yield gender        
            yield '----'

            for item_id in range(10):
                yield self(*args, gender=gender, **kwargs)
