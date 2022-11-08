from data.fng.names import fantasy
from models.fng.names.name import Name
from .barbarian import BarbarianName, BarbarianName1, BarbarianName2, MaleBarbarianName3, FemaleBarbarianName3
from genesys.fng.factories.validators import item_is_unique, item_equals, item_is_not_empty


class AlienName(Name):
    @property
    def parts(self):
        return map(
            lambda item: str(self.data.get(item, '')),
            [
                'nm1',
                'nm2',
                'nm3',
                'nm4',
                'nm5',
            ],
        )

    @property
    def value(self):
        # test_swear(value)
        return "".join(self.parts)

    def __validate_nm4(self):
        def f(item):
            self.data['nm4'].item_id = 0
            return True

        if str(self.data['nm3']) == '':
            return f
        else:
            return item_is_not_empty()

    def __validators(self, method):
        return {
            'nm3': item_is_unique(self.data['nm1'], self.data['nm5']),
            'nm4': self.__validate_nm4() if method != 2 else None,
        }

    def validate(self, method):
        validators = self.__validators(method)

        for item_id, validator in validators:
            if validator is None:
                continue

            if not validator(self.data[item_id]):
                yield item_id


class AmazonName(Name):
    @property
    def parts(self):
        return map(
            lambda item: str(self.data.get(item, '')),
            [
                'nm1',
                'nm2',
                'nm3',
                'nm4',
                'nm5',
            ],
        )

    @property
    def value(self):
        return "".join(self.parts)


class AnansiName(Name):
    vowels = fantasy.anansi.names8

    @property
    def name_start(self):
        return self.data.get('nm0', '')

    @property
    def name_final(self):
        vowels_count = 0
        if self.name_start[-1] in self.vowels:
            vowels_count += 1
        if self.data['nm2'][0] in self.vowels:
            vowels_count += 1

        if vowels_count == 2 and len(self.data['nm2']) > 1:
            return self.data['nm2'][2:] if self.data['nm2'][1] in self.vowels else self.data['nm2'][1:]
        elif vowels_count == 1:
            return self.data['nm2']
        else:
            return f"{self.data['nm1']}{self.data['nm2']}"

    @property
    def value(self):
        return f"{self.name_start}{self.name_final}"


class AngelName(Name):
    value = property(lambda self: str(self.data.get('nm1', '')))


class AnimalSpeciesName(Name):
    @property
    def value(self):
        return f"{self.data['nm1']} {self.data['nm2']}"


class AnimatronicName(Name):
    @property
    def value(self):
        return f"{self.data['nm0']} {self.data['nm1']}"


class AnimeCharacterName(Name):
    @property
    def value(self):
        return f"{self.data['nm3']}{self.data['nm4']} {self.data['nm1']}{self.data['nm2']}"


class AnthousaiName(Name):
    @property
    def value(self):
        return f"{self.data['nm1']}"


class ApocalypseNickname(Name):
    @property
    def value(self):
        return f"{self.data['nm1']}"


class ArtificialIntelligenceName(Name):
    @property
    def value(self):
        return f"{self.data['nm1']}"


class BanditName(Name):
    @property
    def value(self):
        return f"{self.data['nm1']} {self.data['nm2']}"


class BansheeName(Name):
    @property
    def value(self):
        return f"The {self.data['nm1']} {self.data['nm2']}"
