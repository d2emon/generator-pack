from .models import Character
from v1.fng.genesys.name_factory import NameFactory


class CharacterFactory(NameFactory):
    @classmethod
    def random_race(cls):
        raise NotImplementedError()

    @classmethod
    def random_mark(cls):
        raise NotImplementedError()

    @classmethod
    def names20(cls):
        raise NotImplementedError()

    @classmethod
    def names22(cls):
        raise NotImplementedError()

    @classmethod
    def names23(cls):
        raise NotImplementedError()

    @classmethod
    def names24(cls):
        raise NotImplementedError()

    @classmethod
    def names25(cls):
        raise NotImplementedError()

    @classmethod
    def names26(cls):
        raise NotImplementedError()

    @classmethod
    def names27(cls):
        raise NotImplementedError()

    @classmethod
    def names28(cls):
        raise NotImplementedError()

    def __call__(self, *args, **kwargs):
        race = self.random_race()
        mark = self.random_mark()

        character = Character(
            race=race,
            mark=mark,

            mark_from=mark.places_from(),
            mark_through=mark.places_through(),
            mark_to=mark.places_to(),
            memory_type=mark.memory_types(),
            memory_of=mark.memory_ofs(),

            first_name=race.first_name(),
            last_name=race.last_name(),

            random20=self.names20(),
            random22=self.names22(),
            random23=self.names23(),
            random24=self.names24(),
            random25=self.names25(),
            random26=self.names26(),
            random27=self.names27(),
            random28=self.names28(),
        )

        while character.random25 and character.random26 == character.random25:
            character.random26 = self.names26()

        return character
