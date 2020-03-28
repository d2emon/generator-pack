from genesys.fng.factories.factory import Factory
from genesys.fng.models.description.character import Character
from genesys.fng.providers.description.character import DataProvider


class CharacterFactory(Factory):
    class DataProvider(DataProvider):
        pass

    def __next__(self):
        race = next(self.provider.races)
        mark = next(self.provider.marks)

        character = Character()
        character.race = race
        character.mark = mark
        character.mark_from = next(mark.places_from)
        character.mark_through = next(mark.places_through)
        character.mark_to = next(mark.places_to)
        character.memory_type = next(mark.memory_types)
        character.memory_of = next(mark.memory_ofs)
        character.first_name = next(race.first_name)
        character.last_name = next(race.last_name)
        character.random20 = next(self.provider.names20)
        character.random22 = next(self.provider.names22)
        character.random23 = next(self.provider.names23)
        character.random24 = next(self.provider.names24)
        character.random25 = next(self.provider.names25)
        character.random26 = next(self.provider.names26)
        while character.random25 and character.random26 == character.random25:
            character.random26 = next(self.provider.names26)
        character.random27 = next(self.provider.names27)
        character.random28 = next(self.provider.names28)
        return character
