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
    def name_initial(self):
        return str(self.data.get('name_initial', ''))

    @property
    def name_final(self):
        middle = str(self.data.get('name_medial', ''))
        final = str(self.data.get('name_final', ''))

        if len(final) < 1:
            return final

        vowels_count = 0
        if self.name_initial[-1] in self.vowels:
            vowels_count += 1
        if final[0] in self.vowels:
            vowels_count += 1

        if len(final) > 1 and vowels_count > 1:
            return final[2:] if final[1] in self.vowels else final[1:]
        elif vowels_count == 1:
            return final
        else:
            return f"{middle}{final}"

    @property
    def value(self):
        return f"{self.name_initial}{self.name_final}"


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
