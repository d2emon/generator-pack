import random
import unittest
from genesys.nested.name_factory import NameFactory
from genesys.nested.child_factory import ChildFactory
from genesys.nested.thing_factory import Factory as BaseFactory, Thing as BaseThing
from models.model import Model


class Factory(BaseFactory):
    class ChildrenFactory(BaseFactory.ChildrenFactory):
        default_factory = ['VALUE', 10]

    model_type = Model


class Thing(BaseThing):
    model_type = Model


class TestNameFactory(unittest.TestCase):
    def test_name_factory(self):
        factory = NameFactory()

        self.assertEqual(repr(factory), "<NameFactory [['UNNAMED']]>")
        self.assertEqual(factory.parts(), ['UNNAMED'])
        self.assertEqual(next(factory), 'UNNAMED')

    def test_child_factory(self):
        factory = ChildFactory(
            value='VALUE',
            probability=100,
            min_amount=5,
        )

        self.assertEqual(factory.factory(), factory)
        self.assertEqual(iter(factory), factory)
        self.assertEqual(next(factory), ['VALUE'] * 5)
        self.assertEqual(repr(factory), "<Generator \"VALUE\" 5 >")

    def test_child_factory_probability(self):
        factory = ChildFactory(
            probability=50,
        )

        self.assertFalse(factory.check_probability(75))

    def test_child_factory_no_probability(self):
        min_amount = random.randrange(1, 10)
        factory = ChildFactory(
            probability=0,
            min_amount=min_amount,
        )

        self.assertEqual(factory.amount(), 0)

    def test_child_factory_amount(self):
        min_amount = random.randrange(1, 10)
        factory = ChildFactory(
            min_amount=min_amount,
        )

        self.assertEqual(factory.amount(), min_amount)

    def test_child_factory_random_amount(self):
        min_amount = random.randrange(1, 10)
        max_amount = min_amount + random.randrange(1, 10)
        factory = ChildFactory(
            min_amount=min_amount,
            max_amount=max_amount,
        )

        amount = factory.amount()
        self.assertGreaterEqual(amount, min_amount)
        self.assertLessEqual(amount, max_amount)

    def test_thing_children_factory(self):
        factory = Factory.ChildrenFactory()

        for child in factory.factories:
            self.assertTrue(isinstance(child, ChildFactory))

        self.assertEqual(iter(factory), factory)

        for models in next(factory):
            for model in models:
                self.assertEqual(model, "VALUE")

    def test_thing_image_factory(self):
        factory = Factory.ImageFactory("IMAGE")
        self.assertEqual(iter(factory), factory)
        self.assertEqual(next(factory), "IMAGE")

    def test_thing_position_factory(self):
        factory = Factory.PositionFactory([[1, 10]] * 10)
        self.assertEqual(iter(factory), factory)
        for position in next(factory):
            self.assertGreaterEqual(position, 1)
            self.assertLessEqual(position, 10)

    def test_factory(self):
        factory = Factory()

        self.assertTrue(isinstance(factory(), Factory))
        self.assertEqual(iter(factory), factory)

        model = next(factory)
        self.assertTrue(isinstance(model, Model))
        self.assertEqual(model.name, "Factory")
        self.assertEqual(model.image, "factory")

        children = factory.children
        for child in children:
            for item in child:
                self.assertEqual(item, "VALUE")

        self.assertEqual(factory.children, children)

    def test_thing(self):
        factory = Thing.from_str(
            'NAME',
            [
                "CHILD",
            ],
            'NAME FACTORY',
        )

        self.assertTrue(isinstance(factory(), Thing))
        self.assertEqual(iter(factory), factory)

        model = next(factory)
        self.assertTrue(isinstance(model, Model))
        self.assertEqual(model.name, "NAME FACTORY")
        self.assertEqual(model.image, "NAME")

        for child in factory.children:
            for item in child:
                self.assertEqual(item, "CHILD")

        # self.assertEqual(repr(factory), "<NameFactory [['UNNAMED']]>")
        # self.assertEqual(factory.parts(), ['UNNAMED'])
        # self.assertEqual(next(factory), 'UNNAMED')


if __name__ == "__main__":
    unittest.main()
