import random
import unittest
from genesys.storm.world import WorldFactory
from genesys.storm.world.size import SizeFactory, SizeClassFactory
from genesys.storm.world.world_type import WorldTypeFactory
from models.world import World


class TestWorldFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [random.uniform(0, 100) for _ in range(10)]

    def test_world_factory(self):
        factory = WorldFactory()

        data1 = factory.get_data(value_1="VALUE1")
        world1 = factory(value_1="VALUE1")
        self.assertEqual(data1.get("value_1"), "VALUE1")
        # world_type = kwargs.get('world_type') or self.world_type_factory()
        self.assertIsInstance(world1, World)
        # data = self.get_data(**kwargs)
        # return World(*args, **data)

        world_type_factory = WorldTypeFactory()
        world_type = world_type_factory()

        size_class_factory = SizeClassFactory()

        size_class_1 = size_class_factory.by_world_type(world_type)
        size_factory_1 = SizeFactory(size_class=size_class_1)
        world_size_1 = size_factory_1()

        data2 = factory.get_data(world_type=world_type, world_size=world_size_1)
        world2 = factory(
            world_type=world_type,
            size_class=size_class_1,
            world_size=world_size_1,
        )
        self.assertEqual(data2.get("world_type"), world_type)
        self.assertEqual(data2.get("world_size"), world_size_1)
        self.assertIsInstance(world2, World)
        # data = self.get_data(**kwargs)
        # return World(*args, **data)

        size_class_2 = size_class_factory.by_world_type(world_type)
        size_factory_2 = SizeFactory(size_class=size_class_2)
        world_size_2 = size_factory_2()

        data3 = factory.get_data(world_size=world_size_2)
        world3 = factory(
            size_class=size_class_2,
            world_size=world_size_2,
        )
        self.assertEqual(data3.get("world_size"), world_size_2)
        self.assertIn(size_class_2.value, world_type.sizes)
        self.assertIsInstance(world3, World)
        # data = self.get_data(**kwargs)
        # return World(*args, **data)

    def test_size_factory(self):
        world_type_factory = WorldTypeFactory()
        size_class_factory = SizeClassFactory()

        size_class_1 = size_class_factory.by_world_type(world_type_factory())
        size_class_2 = size_class_factory.by_world_type(world_type_factory())

        factory = SizeFactory(size_class=None)
        size0 = factory()
        self.assertEqual(size0, 0)

        factory = SizeFactory(size_class=size_class_1)
        size1 = factory()
        self.assertEqual(factory.size_class, size_class_1)
        self.assertGreaterEqual(size1, size_class_1.min_size)
        self.assertLessEqual(size1, size_class_1.max_size)

        factory = size_class_factory.size_factory(size_class=size_class_2.size_class)
        size3 = factory()
        self.assertEqual(factory.size_class.value, size_class_2.size_class)
        # self.size_class = self.first(lambda item: item.get('size_class') == size_class)
        self.assertGreaterEqual(size3, size_class_2.min_size)
        self.assertLessEqual(size3, size_class_2.max_size)
        # if self.size_class.min_size >= self.size_class.max_size:
        # return self.size_class.min_size


if __name__ == "__main__":
    unittest.main()
