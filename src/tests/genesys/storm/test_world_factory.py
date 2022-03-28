import random
import unittest
from genesys.storm.world import WorldFactory
from genesys.storm.world.shape import ShapeFactory
from genesys.storm.world.size import SizeFactory, SizeClassFactory
from genesys.storm.world.world_type import WorldTypeFactory
from models.world import World, WorldType
from models.world.shape import WorldShape
from models.world.size import WorldSize
from models.world.world_type import WorldType


class TestWorldFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.values = [random.uniform(0, 100) for _ in range(10)]

    def test_world_type(self):
        factory = WorldTypeFactory()
        model = factory()
        self.assertIsInstance(model, WorldType)

    def test_world_shape(self):
        factory = ShapeFactory()
        model = factory()
        self.assertIsInstance(model, WorldShape)

    def test_size(self):
        factory = SizeClassFactory()
        model = factory()
        self.assertIsInstance(model, WorldSize)
        # self.size_class = self.first(lambda item: item.get('size_class') == size_class)

    def test_size_class(self):
        size_class = 'A'

        factory = SizeClassFactory()
        model = factory(size_class=size_class)
        self.assertEqual(model.size_class, size_class)

    def test_by_world_type(self):
        sizes = ['A', 'B', 'C']
        world_type = WorldType(sizes=sizes)

        factory = SizeClassFactory()
        model = factory.by_world_type(world_type=world_type)
        self.assertIn(model.value, sizes)

    def test_no_world_type(self):
        sizes = []
        world_type = WorldType(sizes=sizes)

        factory = SizeClassFactory()
        model = factory.by_world_type(world_type=world_type)
        self.assertIsNotNone(model.value)

    def test_size_factory_by_class(self):
        size_class = 'A'       

        factory = SizeClassFactory()
        size_factory = factory.size_factory()
        self.assertIsInstance(size_factory, SizeFactory)
        self.assertIsNone(size_factory.size_class)
 
        size_factory = factory.size_factory(size_class=size_class)
        self.assertIsNotNone(size_factory.size_class)
        self.assertEqual(size_factory.size_class.value, size_class)

    def test_size_factory_no_size_class(self):
        factory = SizeFactory()
        size = factory()
        self.assertEqual(size, 0)

    def test_size_factory_wrong_size_class(self):
        max_size = random.randrange(1, 10)
        min_size = max_size + random.randrange(1, 10)
        size_class = WorldSize(
            min_size=min_size,
            max_size=max_size,
        )
        factory = SizeFactory(
            size_class=size_class,
        )
        size = factory()
        self.assertEqual(size, min_size)

    def test_size_factory(self):
        min_size = random.randrange(1, 10)
        max_size = min_size + random.randrange(1, 10)
        size_class = WorldSize(
            size_class='SIZE_CLASS',
            min_size=min_size,
            max_size=max_size,
        )
        factory = SizeFactory(
            size_class=size_class,
        )
        size = factory()
        self.assertEqual(factory.size_class.value, size_class.value)
        self.assertGreaterEqual(size, min_size)
        self.assertLessEqual(size, max_size)

    def test_world_factory(self):
        factory = WorldFactory()
        model = factory()
        self.assertIsInstance(model, World)

    def test_world_factory_size_class(self):
        size_class_factory = SizeClassFactory()
        size_class = size_class_factory()

        factory = WorldFactory()
        model = factory(size_class=size_class)
        self.assertEqual(model.size_class, size_class)

    def test_world_factory_size(self):
        world_size = random.randrange(0, 10)
        factory = WorldFactory()
        model = factory(world_size=world_size)
        self.assertEqual(model.world_size, world_size)


if __name__ == "__main__":
    unittest.main()
