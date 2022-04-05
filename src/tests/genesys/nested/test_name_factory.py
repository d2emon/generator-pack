import random
import unittest
from genesys.nested.name_factory import NameFactory
from genesys.nested.child_factory import ChildFactory


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

        # self.assertEqual(repr(factory), "<NameFactory [['UNNAMED']]>")
        # self.assertEqual(factory.parts(), ['UNNAMED'])
        # self.assertEqual(next(factory), 'UNNAMED')


if __name__ == "__main__":
    unittest.main()
