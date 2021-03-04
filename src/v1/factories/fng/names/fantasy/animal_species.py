from v1.fixtures.data_block import load_data
from v1.fixtures.fng.names import fantasy
from v1.models.fng.names.fantasy import AnimalSpeciesName
from v1.factories.fng.name_factory import NameFactory, ComplexNameFactory


class AnimalSpeciesNameFactory(ComplexNameFactory):
    """Animal Species Name Factory

    This animal species name generator will generate names for (mostly) non-existing animal species, perfect for fantasy
    creatures. However, due to the random nature of this generator, every once in a while you may get a name of an
    existing animal."""

    class AnimalSpeciesNameFactory1(NameFactory):
        """The first 4 names are names of animals combined with an adjective.
        For example: 'Almond Albatross'."""
        name_class = AnimalSpeciesName
        blocks_map = {
            1: 1,
            2: 2,
        }

    class AnimalSpeciesNameFactory2(NameFactory):
        """The next 2 names will be names of animals with characteristic specific names.
        For example: 'Flame-Eyed Mongoose'."""
        name_class = AnimalSpeciesName
        blocks_map = {
            1: 3,
            2: 2,
        }

    class AnimalSpeciesNameFactory3(NameFactory):
        """The last 4 names will be two animal names combined, which will form a new animal (with a little imagination).
        A great example of this are the animals in the Avatar (Last Airbender/Korra) series, like the Turtle-Duck and
        the Lion-Turtle."""
        name_class = AnimalSpeciesName
        blocks_map = {
            1: 2,
            2: 2,
        }

    factory_classes = {
        0: AnimalSpeciesNameFactory1,
        1: AnimalSpeciesNameFactory2,
        2: AnimalSpeciesNameFactory3,
    }
    default_blocks = load_data({
        1: fantasy.animal_species.nm1,
        2: fantasy.animal_species.nm2,
        3: fantasy.animal_species.nm3,
    })

    def get_factory(self, factory_id):
        if factory_id < 40:
            return self.factories[0]
        elif factory_id < 60:
            return self.factories[1]
        else:
            return self.factories[2]



