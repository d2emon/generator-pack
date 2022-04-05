import random
from .name_factory import ComplexFactory
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
        return random.randrange(100)

    def factory(self, percent=None):
        raise NotImplementedError()

    def __call__(self, *args, percent=None, **kwargs):
        return self.from_factory(
            percent if percent is not None else self.__get_percent(),
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
        for item_id in range(10):
            yield self(*args, percent=item_id * 10, **kwargs)


class GenderNameBlockFactory(NameBlockFactory):
    @property
    def genders(self):
        return self.factories.keys()

    def __get_gender(self):
        return genders.MALE

    def factory(self, gender=None):
        return self.factories.get(gender if gender is not None else self._get_gender())

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
