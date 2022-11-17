"""
Galaxy name.

This name generator will give you names fit for galaxies, star systems, and other astronomical
regions.

The names are all based on human naming conventions for astronomical bodies or regions, so while
your own alien species might use different naming conventions, this generator sticks to the 3 most
used types.
"""

from data.fng.names.place import galaxy
from factories.template import TemplateFactory
from genesys.fng.database import Database
from genesys.fng.factories.name_block_factory import MultipleFactoryNameFactory
from genesys.fng.factories.name_factory import ComplexFactory
from models.fng.names.name import Name


DB = Database('galaxy', {
    'nm1': galaxy.galaxy_names[0],
    'nm2': galaxy.galaxy_names[1],
    'nm3': galaxy.galaxy_names[2],
    'nm4': galaxy.galaxy_names[3],
    # 'nm5': galaxy.galaxy_names[5],
    # 'nm6': galaxy.galaxy_names[6],
})


class GalaxyName(Name):
    """Galaxy name model."""

    @property
    def value(self) -> str:
        """
        Get model value.

        Returns:
            str: Value for model
        """
        # if isinstance(self.built_with, AmusementParkFactory2):
        #     return " ".join(self.values)

        return " ".join(self.values)


class BaseGalaxyFactory(ComplexFactory):
    """Base factory for galaxy."""

    template = ""

    model = GalaxyName
    parts = [
        'nm1',
        'nm2',
    ]

    @property
    def text(self):
        """
        Generate text from factory data
        :return: str
        """
        return f"{self.data['part1']} {self.data['part2']}"


class GalaxyGenerator1(BaseGalaxyFactory):
    """
    Method #1.

    The first type are names of Greek origin. They're usually named after mythological figures from
    ancient Greece. 'Omega Centauri' and 'Andromeda Galaxy' are some names which we use today.

    Due to the random nature of a generator, some names could be names used in real life.
    """

    parts = [
        'nm1',
        'nm2',
    ]


class GalaxyGenerator2(BaseGalaxyFactory):
    """
    Method #2.

    The second type used in this generator are names based on the appearance of the galaxy. 'Black
    Eye Galaxy' and 'Sombrero Galaxy' are two names of actual Galaxies.

    I've tried to make sure all the names in the generator haven't been used in real life already,
    but it's possible some have slipped in.
    """

    parts = [
        'nm2',
        'nm4',
    ]


class GalaxyGenerator3(BaseGalaxyFactory):
    """
    Method #3.

    The second type used in this generator are names based on the appearance of the galaxy. 'Black
    Eye Galaxy' and 'Sombrero Galaxy' are two names of actual Galaxies.

    I've tried to make sure all the names in the generator haven't been used in real life already,
    but it's possible some have slipped in.
    """

    parts = [
        'nm3',
        'nm4',
    ]


class GalaxyGenerator4(TemplateFactory, BaseGalaxyFactory):
    """
    Method #4.

    The last type of names are code names, usually made up out of both numbers and letters.

    These names are catalog names. For example, the 'NGC' in 'NGC 1068 (also known as Messier 77 or
    M77)' stands for 'New General Catalog'. The numbers specify the entry in that catalog and the
    position of that galaxy in relation to our sky.

    I haven't used such acronyms in this generator, this way it's easier to create original names,
    and you might be able to come up with some cool catalogs of your own, perhaps named after an
    important scientist in your fictional world.
    """

    template = "{c}{c}-{n}{n}"


class GalaxyGenerator5(TemplateFactory, BaseGalaxyFactory):
    """
    Method #5.

    The last type of names are code names, usually made up out of both numbers and letters.

    These names are catalog names. For example, the 'NGC' in 'NGC 1068 (also known as Messier 77 or
    M77)' stands for 'New General Catalog'. The numbers specify the entry in that catalog and the
    position of that galaxy in relation to our sky.

    I haven't used such acronyms in this generator, this way it's easier to create original names,
    and you might be able to come up with some cool catalogs of your own, perhaps named after an
    important scientist in your fictional world.
    """

    template = "{c}{c}{c} {n}{n}{c}"


class GalaxyFactory(MultipleFactoryNameFactory):
    """Galaxy name factory."""

    default_data = DB
    factory_classes = [
        GalaxyGenerator1,
        GalaxyGenerator2,
        GalaxyGenerator3,
        GalaxyGenerator4,
        GalaxyGenerator5,
    ]
    model = GalaxyName
