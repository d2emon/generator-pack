from genesys.fng.models.description.character import Character
from v1.fng.genesys.name_factory import NameFactory


class CharacterFactory(NameFactory):
    class Provider:
        @classmethod
        def races(cls):
            raise NotImplementedError()

        @classmethod
        def marks(cls):
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
        race = self.Provider.races()
        mark = self.Provider.marks()

        character = Character()
        character.race = race
        character.mark = mark
        character.mark_from = mark.places_from()
        character.mark_through = mark.places_through()
        character.mark_to = mark.places_to()
        character.memory_type = mark.memory_types()
        character.memory_of = mark.memory_ofs()
        character.first_name = race.first_name()
        character.last_name = race.last_name()
        character.random20 = self.Provider.names20()
        character.random22 = self.Provider.names22()
        character.random23 = self.Provider.names23()
        character.random24 = self.Provider.names24()
        character.random25 = self.Provider.names25()
        character.random26 = self.Provider.names26()
        while character.random25 and character.random26 == character.random25:
            character.random26 = self.Provider.names26()
        character.random27 = self.Provider.names27()
        character.random28 = self.Provider.names28()
        return character
