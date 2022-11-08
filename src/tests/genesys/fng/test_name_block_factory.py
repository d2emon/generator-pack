import random
import unittest
import uuid
from genesys.fng.database import Database
from genesys.fng.factories.name_factory import BaseNameFactory, ComplexNameFactory
from genesys.fng.factories.name_block_factory import MultipleFactoryNameFactory, GenderNameBlockFactory
from utils.genders import MALE, FEMALE, NEUTRAL


GENDERS = [
    MALE,
    FEMALE,
    NEUTRAL,
]

class NameFactory1(BaseNameFactory):
    default_data = Database(uuid.uuid4(), {
        'nm1': [
            uuid.uuid4(),
        ],
    })


class NameBlockFactory1(MultipleFactoryNameFactory):
    factory_classes = [
        NameFactory1,
    ]


class NameBlockFactory2(MultipleFactoryNameFactory):
    factory_classes = [
        NameFactory1,
        NameFactory1,
    ]


class NameBlockFactory3(MultipleFactoryNameFactory):
    factory_classes = [
        NameFactory1,
        NameFactory1,
        NameFactory1,
    ]


class TestNameBlockFactory(unittest.TestCase):
    def test_name_block_factory(self):
        factory = NameBlockFactory1()
        for item_id in range(10):
            model = factory(percent=item_id * 10)
            self.assertEqual(model.__class__, factory.model)

    def test_name_block_factory_2(self):
        factory = NameBlockFactory2()
        for item_id in range(10):
            model = factory(percent=item_id * 10)
            self.assertEqual(model.__class__, factory.model)

    def test_name_block_factory_3(self):
        factory = NameBlockFactory3()
        for item_id in range(10):
            model = factory(percent=item_id * 10)
            self.assertEqual(model.__class__, factory.model)

    def test_gender_name_block_factory(self):
        factory = GenderNameBlockFactory()

        for gender, gender_factory in factory.factories.items():
            self.assertIn(gender, GENDERS)
            self.assertIsInstance(gender_factory, ComplexNameFactory)

        for gender in factory.genders:
            self.assertIn(gender, GENDERS)

    def test_gender_name_block_factory_subfactory(self):
        factory = GenderNameBlockFactory()
        gender_factory = factory.factory()
        self.assertIsInstance(gender_factory, ComplexNameFactory)

    def test_gender_name_block_factory_by_percent(self):
        factory = GenderNameBlockFactory()
        gender_factory = factory.by_percent(random.choice(GENDERS))
        self.assertIsInstance(gender_factory, ComplexNameFactory)

    def test_gender_name_block_factory_call(self):
        factory = GenderNameBlockFactory()
        for item_id in range(10):
            for gender in GENDERS:
                model = factory(gender=gender, percent=item_id * 10)
                self.assertEqual(model.__class__, factory.model)


if __name__ == "__main__":
    unittest.main()
