import unittest
from genesys.nested.thing_factory import Factory
from genesys.nested.factories import Things


class SubItem1:
    value = ".NAME"


class SubItem2:
    value = 123


class Item:
    name = "item"
    factories = [
        [
            'a',
            'b',
            'c',
        ],
        SubItem1(),
        SubItem2(),
    ]


class TestThingFactory(unittest.TestCase):
    def test_from_contents(self):
        Things.from_contents([
            Item,
        ])

        item = Things.get_thing('item')
        self.assertTrue(isinstance(item, Item))

    def test_add_thing(self):
        Things.add_thing('NAME', [])

        item = Things.get_thing('NAME')
        self.assertTrue(isinstance(item, Factory))

    def test_get_factories(self):
        factories = Things.get_factories('item')

        self.assertEqual(len(factories), 2)
        self.assertIn(factories[0], ['a', 'b', 'c'])
        self.assertTrue(isinstance(factories[1], SubItem2))

    def test_get_no_factories(self):
        factories = Things.get_factories(None)

        self.assertEqual(len(factories), 0)


if __name__ == "__main__":
    unittest.main()
