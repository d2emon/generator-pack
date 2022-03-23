from v1.fixtures import genders
from models.fng.description.description import Description
from models.model import Model
from .race import Race
from .mark import Mark, MarkDescription
from .hair import Hair
from .face import Face
from .eyes import Eyes
from .name import Name
from .personality import Personality


class Character(Model):
    gender = property(lambda self: self.items.get('gender'))
    race = property(lambda self: self.items.get('race'))
    hair = property(lambda self: self.items.get('hair'))
    face = property(lambda self: self.items.get('face'))
    eyes = property(lambda self: self.items.get('eyes'))
    origin = property(lambda self: self.items.get('origin'))
    origin_attitude = property(lambda self: self.items.get('origin_attitude'))
    mark_description = property(lambda self: self.items.get('mark_description'))
    name = property(lambda self: self.items.get('name'))
    profession = property(lambda self: self.items.get('profession'))
    height = property(lambda self: self.items.get('height'))
    width = property(lambda self: self.items.get('width'))
    personality = property(lambda self: self.items.get('personality'))


class CharacterDescription(Description):
    __he_or_she = {
        genders.MALE: "he",
        genders.FEMALE: "she",
    }
    __him_or_her = {
        genders.MALE: "him",
        genders.FEMALE: "her",
    }
    __his_or_her = {
        genders.MALE: "his",
        genders.FEMALE: "her",
    }

    character = property(lambda self: self.items.get('character'))

    he_or_she = property(lambda self: self.__he_or_she.get(self.character and self.character.gender, "it"))
    him_or_her = property(lambda self: self.__him_or_her.get(self.character and self.character.gender, "it"))
    his_or_her = property(lambda self: self.__his_or_her.get(self.character and self.character.gender, "its"))

    @property
    def __value_1(self):
        return f"{self.character.hair} a {self.character.face}. "\
            + (self.character.eyes.describe(
                f"{self.character.origin} they've {self.character.origin_attitude} for so long",
            ) if self.character.eyes else '')

    @property
    def __value_2(self):
        return self.character.mark_description

    @property
    def __value_3(self):
        return f"This is the face of {self.character.name}, " \
            + f"a true {self.character.profession} among {self.character.race}. " \
            + f"{self.he_or_she.title()} stands {self.character.height} others, " \
            + f"despite {self.his_or_her} {self.character.width} frame."

    @property
    def __value_4(self):
        return str(self.character.personality)

    @property
    def value(self):
        if not self.character:
            return ''

        return f"{self.__value_1}\n" \
            + f"{self.__value_2}\n\n" \
            + f"{self.__value_3}\n\n" \
            + f"{self.__value_4}"
