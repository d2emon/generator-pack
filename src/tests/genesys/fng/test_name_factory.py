import unittest
import uuid
from genesys.fng.database import Database
from genesys.fng.factories.name_factory import BaseNameFactory, ComplexFactory, \
    PolymorphFactory, PercentFactory, GenderFactory
from models.fng.names.name import Name
from utils.genders import MALE, FEMALE


class NameFactory1(BaseNameFactory):
    default_data = Database(uuid.uuid4(), {
        'nm1': [
            uuid.uuid4(),
        ],
    })

class NameFactory2(BaseNameFactory):
    default_data = Database(uuid.uuid4(), {
        'nm1': [
            uuid.uuid4(),
        ],
    })

    def build_kwargs(self, *args, **kwargs) -> dict:
        """
        Build data for model.

        Returns:
            dict: Data for model.
        """

        return {
            'key': uuid.uuid4(),
        }


class ComplexFactory1(ComplexFactory):
    factory_classes = {
        'name1': NameFactory1,
    }


class PolymorphFactory1(PolymorphFactory):
    factory_classes = {
        'name1': NameFactory2,
    }


class PercentFactory1(PercentFactory):
    factory_classes = {
        100: NameFactory2,
    }

    @property
    def default_percent(self):
        return 100


class GenderFactory1(GenderFactory):
    factory_classes = {
        MALE: NameFactory2,
        FEMALE: NameFactory2,
    }


BLOCK_ID_1 = uuid.uuid4()
BLOCK_ID_2 = uuid.uuid4()
COUNT = 0


def validator(item):
    global COUNT

    COUNT += 1

    return COUNT % 5 == 0


class ComplexNameFactory1(ComplexFactory):
    block_map = {
        'name1': BLOCK_ID_1,
        'name2': BLOCK_ID_2,
        'name3': BLOCK_ID_1,
    }
    validators = {
        'name1': lambda items: lambda item: True,
        'name2': lambda items: validator,
    }



class TestNameFactory(unittest.TestCase):
    def setUp(self):
        self.group_id = uuid.uuid4()
        self.values = [uuid.uuid4() for _ in range(10)]
        self.data = {
            BLOCK_ID_1: self.values,
            BLOCK_ID_2: self.values,
        }
        self.db = Database(self.group_id, self.data)

        self.name_factory = NameFactory1(self.db)
        self.complex_factory = ComplexFactory1(self.db)
        self.complex_name_factory = ComplexNameFactory1(self.db)

    # Test NameFactory

    def test_default_name_factory_db(self):
        factory = NameFactory1()
        self.assertEqual(factory.data, factory.default_data)

    def test_name_factory_db(self):
        self.assertEqual(self.name_factory.data, self.db)

    def test_name_factory_build_kwargs(self):
        data = self.name_factory.build_kwargs()
        self.assertIsInstance(data, dict)

    def test_name_factory_run(self):
        value = self.name_factory()
        self.assertIsInstance(value, Name)

    # Test ComplexFactory

    def test_complex_factories_data(self):
        factories = ComplexFactory1.get_factories(self.db)
        for factory_id, factory in factories.items():
            self.assertIn(factory_id, ComplexFactory1.factory_classes.keys())
            self.assertIsInstance(factory, ComplexFactory1.factory_classes[factory_id])

    def test_complex_factory_data(self):
        for factory_id, factory in self.complex_factory.factories.items():
            self.assertIn(factory_id, ComplexFactory1.factory_classes.keys())
            self.assertIsInstance(factory, ComplexFactory1.factory_classes[factory_id])

    def test_complex_factory_factory(self):
        no_factory = self.complex_factory.factory('no-uuid')
        self.assertIsNone(no_factory)

        for factory_id in self.complex_factory.factory_classes.keys():
            factory = self.complex_factory.factory(factory_id)
            self.assertEqual(self.complex_factory[factory_id], factory)
            self.assertIsInstance(factory, ComplexFactory1.factory_classes[factory_id])

    def test_complex_factory_from_factory(self):
        for factory_id in self.complex_factory.factory_classes.keys():
            item = self.complex_factory.from_factory(factory_id)
            self.assertIsInstance(item, Name)

    # Test ComplexNameFactory

    def test_complex_name_factories_data(self):
        factories = ComplexNameFactory1.get_factories(self.db)
        for factory_id, factory in factories.items():
            self.assertIn(factory_id, ComplexNameFactory1.block_map.keys())

            item = factory()
            key = ComplexNameFactory1.block_map[factory_id]
            self.assertIn(item.value, self.data[key])

    def test_complex_name_factory_get_field(self):
        item = self.complex_name_factory.get_field('name1')
        self.assertIsNotNone(item)
        self.assertIn(item.value, self.data[BLOCK_ID_1])

    def test_complex_name_factory_get_field_not_exists(self):
        data = self.complex_name_factory.get_field('not_existing_field')
        self.assertIsNone(data)

    def test_complex_name_factory_build_kwargs(self):
        data = self.complex_name_factory.build_kwargs()
        self.assertIsInstance(data, dict)
        for factory_id, item in data.items():
            key = self.complex_name_factory.block_map[factory_id]
            self.assertIn(item.value, self.data[key])

    def test_complex_name_factory_validate_all(self):
        data = self.complex_name_factory.build_kwargs()

        valid = self.complex_name_factory.validate(data)
        for item in valid:
            self.assertIn(item, self.complex_name_factory.block_map.keys())

    def test_complex_name_factory_build(self):
        data = self.complex_name_factory()
        self.assertIsInstance(data, Name)
        for factory_id, item in data.data.items():
            key = self.complex_name_factory.block_map[factory_id]
            self.assertIn(item.value, self.data[key])

    # Test PolymorphFactory

    def test_polymorph_factory_build(self):
        factory = PolymorphFactory1(self.db)
        data = factory(factory_id='name1')
        self.assertIsInstance(data, Name)
        for item in data.data.values():
            self.assertIsInstance(item, uuid.UUID)

    # Test PercentFactory

    def test_percent_factory_percent(self):
        factory = PercentFactory(self.db)
        percent = factory.default_percent
        self.assertIn(percent, range(100))

    def test_percent_factory(self):
        factory = PercentFactory1(self.db)
        data = factory()
        self.assertIsInstance(data, Name)
        for item in data.data.values():
            self.assertIsInstance(item, uuid.UUID)

    # Test GenderFactory

    def test_gender_factory_gender(self):
        factory = GenderFactory1(self.db)
        gender = factory.default_gender
        self.assertIn(gender, [MALE, FEMALE])

    def test_gender_factory(self):
        factory = GenderFactory1(self.db)
        data = factory()
        self.assertIsInstance(data, Name)
        for item in data.data.values():
            self.assertIsInstance(item, uuid.UUID)


if __name__ == "__main__":
    unittest.main()
