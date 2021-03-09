from v1.fixtures.data_block import load_data
from v1.fixtures.fng.names import fantasy
from v1.models.fng.names.fantasy import AlienName
from v1.factories.fng.name_factory import NameFactory, ComplexNameFactory
from v1.factories.fng.validators import item_is_not_unique, item_equals, generate_while


class AlienNameFactory(ComplexNameFactory):
    """Alien Species Name Factory

    It's both easy and difficult to create alien names, as they can be anything in any language. But the names have to
    sound like a good fit for the species you've invented, so I've tried to make sure many different types of names can
    be generated, but they generally fit in 3 different categories."""

    class AlienNameFactory1(NameFactory):
        """The first 4 names have a much higher chance of having a more guttural sound to them, ideal for the stronger
        and brutish looking aliens."""
        name_class = AlienName
        blocks_map = {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 5,
        }

        def validate(self, items):
            items[3] = generate_while(
                items[3],
                item_is_not_unique([items[1], items[5]]),
                self.blocks[3],
            )
            items[4] = self.blocks[4][0] if str(items[3]) == '' else generate_while(
                items[4],
                item_equals(''),
                self.blocks[3],
            )

            return items

    class AlienNameFactory2(NameFactory):
        """The next 3 names have a much higher chance of having a more melodic sound to them, making them ideal for the
        softer and gentle looking aliens."""
        name_class = AlienName
        blocks_map = {
            1: 6,
            2: 7,
            3: 8,
            4: 10,
            5: 11,
        }

        def validate(self, items):
            items[3] = generate_while(
                items[3],
                item_is_not_unique([items[1], items[5]]),
                self.blocks[8],
            )

            return items

    class AlienNameFactory3(NameFactory):
        """The last 3 names can sound both guttural and melodic and anything in between. These names are more randomized
        than the previous 2 types and unlike the other 2 types, these aren't always easy to pronounce in English."""
        name_class = AlienName
        blocks_map = {
            1: 12,
            2: 13,
            3: 14,
            4: 15,
            5: 16,
        }

        def validate(self, items):
            items[3] = generate_while(
                items[3],
                item_is_not_unique([items[1], items[5]]),
                self.blocks[14],
            )
            items[4] = self.blocks[15][0] if str(items[3]) == '' else generate_while(
                items[4],
                item_equals(''),
                self.blocks[15],
            )

            return items

    factory_classes = {
        0: AlienNameFactory1,
        1: AlienNameFactory2,
        2: AlienNameFactory3,
    }
    default_blocks = load_data({
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

    def factory(self, factory_id):
        if factory_id < 40:
            return self.factories[0]
        elif factory_id < 70:
            return self.factories[1]
        else:
            return self.factories[2]
