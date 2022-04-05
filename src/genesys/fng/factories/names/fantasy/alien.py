from database.data_block import fill_data
from data.fng.names import fantasy
from models.fng.names.fantasy import AlienName
from genesys.fng.factories.name_block_factory import NameBlockFactory
from genesys.fng.factories.name_factory import ComplexNameFactory
from genesys.fng.factories.validators import item_is_not_unique, item_equals, generate_while


class AlienNameFactory(NameBlockFactory):
    """Alien Species Name Factory

    It's both easy and difficult to create alien names, as they can be anything in any language. But the names have to
    sound like a good fit for the species you've invented, so I've tried to make sure many different types of names can
    be generated, but they generally fit in 3 different categories."""

    class AlienNameFactory1(ComplexNameFactory):
        """The first 4 names have a much higher chance of having a more guttural sound to them, ideal for the stronger
        and brutish looking aliens."""
        model = AlienName

        block_map = {
            'nm1': 1,
            'nm2': 2,
            'nm3': 3,
            'nm4': 4,
            'nm5': 5,
        }

        def validate(self, items):
            items['nm3'] = generate_while(
                items['nm3'],
                item_is_not_unique([items['nm1'], items['nm5']]),
                self['nm3'],
            )

            items['nm4'] = self['nm4'](item_id=0) if str(items['nm3']) == '' else generate_while(
                items['nm4'],
                item_equals(''),
                self['nm4'],
            )

            return items

    class AlienNameFactory2(ComplexNameFactory):
        """The next 3 names have a much higher chance of having a more melodic sound to them, making them ideal for the
        softer and gentle looking aliens."""
        model = AlienName

        block_map = {
            'nm1': 6,
            'nm2': 7,
            'nm3': 8,
            'nm4': 10,
            'nm5': 11,
        }

        def validate(self, items):
            items['nm3'] = generate_while(
                items['nm3'],
                item_is_not_unique([items['nm1'], items['nm5']]),
                self['nm3'],
            )

            return items

    class AlienNameFactory3(ComplexNameFactory):
        """The last 3 names can sound both guttural and melodic and anything in between. These names are more randomized
        than the previous 2 types and unlike the other 2 types, these aren't always easy to pronounce in English."""
        model = AlienName

        block_map = {
            'nm1': 12,
            'nm2': 13,
            'nm3': 14,
            'nm4': 15,
            'nm5': 16,
        }

        def validate(self, items):
            items['nm3'] = generate_while(
                items['nm3'],
                item_is_not_unique([items['nm1'], items['nm5']]),
                self['nm3'],
            )

            items['nm4'] = self['nm4'](item_id=0) if str(items['nm3']) == '' else generate_while(
                items['nm4'],
                item_equals(''),
                self['nm4'],
            )

            return items

    default_data = fill_data(group_id='aliens')({
        1: fantasy.alien.nm1,
        2: fantasy.alien.nm2,
        3: fantasy.alien.nm3,
        4: fantasy.alien.nm4,
        5: fantasy.alien.nm5,

        6: fantasy.alien.nm6,
        7: fantasy.alien.nm7,
        8: fantasy.alien.nm8,
        10: fantasy.alien.nm10,
        11: fantasy.alien.nm11,

        12: fantasy.alien.nm12,
        13: fantasy.alien.nm13,
        14: fantasy.alien.nm14,
        15: fantasy.alien.nm15,
        16: fantasy.alien.nm16,
    })

    factory_classes = {
        0: AlienNameFactory1,
        1: AlienNameFactory2,
        2: AlienNameFactory3,
    }

    def factory(self, percent):
        if percent < 40:
            return self.factories.get(0)
        elif percent < 70:
            return self.factories.get(1)
        elif percent < 100:
            return self.factories.get(2)
        else:
            return None
