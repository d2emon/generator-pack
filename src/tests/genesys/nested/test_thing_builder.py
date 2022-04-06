from email.mime import base
import random
import unittest
from genesys.nested.factories.thing_factory import Factory
from genesys.nested.factories.thing_builder import ProviderFactory, ListFactory, ThingBuilder


class TestThingBuilder(unittest.TestCase):
    def test_provider_factory(self):
        factory = ProviderFactory('PROVIDER')

        self.assertEqual(iter(factory), factory)
        self.assertEqual(factory.provider, 'PROVIDER')

    def test_list_factory(self):
        items = [random.uniform(0, 100) for _ in range(10)]
        factory = ListFactory(items)

        self.assertEqual(iter(factory), factory)
        self.assertIn(next(factory), items)

    def test_thing_base_factory(self):
        items = [random.uniform(0, 100) for _ in range(10)]
        base_factory = ThingBuilder.BaseFactory('PROVIDER')
        factory_class = base_factory.factory(items)
        factory = factory_class()
        self.assertIn(next(factory), items)

    def test_thing_builder_probable(self):
        probable = ThingBuilder.probable(0)
        self.assertIsNone(probable)

    def test_thing_builder_multiple(self):
        min_value = random.randrange(1, 10)
        max_value = min_value + random.randrange(1, 10)
        items = [random.uniform(0, 100) for _ in range(10)]

        exact_items = list(ThingBuilder.multiple(min_value))
        self.assertEqual(len(exact_items), min_value)

        range_items = list(ThingBuilder.multiple(min_value, max_value))
        self.assertGreaterEqual(len(range_items), min_value)
        self.assertLessEqual(len(range_items), max_value)

        selected = ThingBuilder.choice(items)
        self.assertIn(selected, items)

    def test_thing_builder(self):
        factory = ThingBuilder()

        self.assertIsNone(next(factory.name))

        children = list(factory.children())
        self.assertEqual(len(children), 0)

        build = factory.build()
        name = build.get('name')
        children = build.get('children')
        self.assertEqual(name, None)
        self.assertEqual(len(children), 0)



if __name__ == "__main__":
    unittest.main()
