from v1.fixtures.fng.names import fantasy
from models.fng.names.name import Name
from .barbarian import BarbarianName, BarbarianName1, BarbarianName2, MaleBarbarianName3, FemaleBarbarianName3


class AlienName(Name):
    @property
    def parts(self):
        return map(
            lambda item: str(self.items.get(item, '')),
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


class AmazonName(Name):
    @property
    def parts(self):
        return map(
            lambda item: str(self.items.get(item, '')),
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
        return self.items.get('nm0', '')

    @property
    def name_final(self):
        vowels_count = 0
        if self.name_start[-1] in self.vowels:
            vowels_count += 1
        if self.items['nm2'][0] in self.vowels:
            vowels_count += 1

        if vowels_count == 2 and len(self.items['nm2']) > 1:
            return self.items['nm2'][2:] if self.items['nm2'][1] in self.vowels else self.items['nm2'][1:]
        elif vowels_count == 1:
            return self.items['nm2']
        else:
            return f"{self.items['nm1']}{self.items['nm2']}"

    @property
    def value(self):
        return f"{self.name_start}{self.name_final}"


class AngelName(Name):
    value = property(lambda self: str(self.items.get('nm1', '')))


class AnimalSpeciesName(Name):
    @property
    def value(self):
        return f"{self.items['nm1']} {self.items['nm2']}"


class AnimatronicName(Name):
    @property
    def value(self):
        return f"{self.items['nm0']} {self.items['nm1']}"


class AnimeCharacterName(Name):
    @property
    def value(self):
        return f"{self.items['nm3']}{self.items['nm4']} {self.items['nm1']}{self.items['nm2']}"


class AnthousaiName(Name):
    @property
    def value(self):
        return f"{self.items['nm1']}"


class ApocalypseNickname(Name):
    @property
    def value(self):
        return f"{self.items['nm1']}"


class ArtificialIntelligenceName(Name):
    @property
    def value(self):
        return f"{self.items['nm1']}"


class BanditName(Name):
    @property
    def value(self):
        return f"{self.items['nm1']} {self.items['nm2']}"


class BansheeName(Name):
    @property
    def value(self):
        return f"The {self.items['nm1']} {self.items['nm2']}"
