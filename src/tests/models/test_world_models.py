import random
import unittest
from models.world import World
from models.world.shape import WorldShape
from models.world.size import WorldSize
from models.world.world_type import WorldType


class TestWorldsModel(unittest.TestCase):
    def test_world_shape_model(self):
        name = str(random.uniform(0, 100))
        description = str(random.uniform(0, 100))

        model = WorldShape(
            name=name,
            description=description,
        )

        self.assertEqual(model.value, name)

        self.assertEqual(model.description, description)

    def test_world_type_model(self):
        world_type = str(random.uniform(0, 100))
        description = str(random.uniform(0, 100))
        encounters = str(random.uniform(0, 100))
        sizes = [random.uniform(0, 100) for _ in range(random.randint(1, 10))]

        model = WorldType(
            world_type=world_type,
            description=description,
            encounters=encounters,
            sizes=sizes,
        )

        self.assertEqual(model.value, world_type)

        self.assertEqual(model.description, description)
        self.assertEqual(model.encounters, encounters)
        self.assertEqual(model.sizes, sizes)

        self.assertEqual(model['world_type'], world_type)

    def test_world_size_model(self):
        min_size = random.randint(0, 100)
        max_size = min_size + random.randint(0, 100)
        name = str(random.uniform(0, 100))
        size = random.randint(min_size, max_size)
        size_class = str(random.uniform(0, 100))
        description = "\n".join([
            f"Класс размера:\t{size_class}",
            f"Описание:\t\t{name}",
            f"Размер:\t\t\t{size}",
        ])

        model = WorldSize(
            min_size=min_size,
            max_size=max_size,
            name=name,
            size=size,
            size_class=size_class,
        )

        self.assertEqual(model.value, size_class)

        self.assertEqual(model.name, name)
        self.assertEqual(model.size, size)
        self.assertEqual(model.size_class, size_class)
        self.assertEqual(model.min_size, min_size)
        self.assertEqual(model.max_size, max_size)

        self.assertEqual(model.description, description)

    def test_min_world_size_model(self):
        min_size = random.randint(0, 100)
        max_size = min_size + random.randint(0, 100)
        name = str(random.uniform(0, 100))
        size = random.randint(min_size, max_size)
        size_class = str(random.uniform(0, 100))

        min_model = WorldSize(
            min_size=min_size,
            name=name,
            size=size,
            size_class=size_class,
        )
        self.assertEqual(min_model.max_size, min_size)

    def test_max_world_size_model(self):
        min_size = random.randint(0, 100)
        max_size = min_size + random.randint(0, 100)
        name = str(random.uniform(0, 100))
        size = random.randint(min_size, max_size)
        size_class = str(random.uniform(0, 100))

        max_model = WorldSize(
            max_size=max_size,
            name=name,
            size=size,
            size_class=size_class,
        )
        self.assertEqual(max_model.min_size, 0)


    def test_world_model(self):
        world_size = random.randint(0, 100)
        size_class = WorldSize(
            name="WORLD SIZE DESCRIPTION",
            size_class="WORLD SIZE CLASS",
            size="WORLD SIZE",
        )
        shape = WorldShape(
            name="WORLD SHAPE",
            description="WORLD SHAPE DESCRPTION",
        )
        world_type = WorldType(
            world_type="WORLD TYPE",
            description="WORLD TYPE DESCRIPTION",
            encounters=[
                "ENCOUNTER 1",
                "ENCOUNTER 2",
            ]
        )
        description = "\n".join([
            f"{world_type} {shape} ({world_size} миль)",
            f"{world_type.description}",
            f"Возможные столкновения: {world_type.encounters}",
            f"{shape.description}",
            f"{size_class.description}",
        ])

        model = World(
            world_size=world_size,
            size_class=size_class,
            shape=shape,
            world_type=world_type,
        )

        # self.assertEqual(model.value, size_class)

        self.assertEqual(model.world_size, world_size)
        self.assertEqual(model.size_class, size_class)
        self.assertEqual(model.shape, shape)
        self.assertEqual(model.world_type, world_type)

        self.assertEqual(model.description, description)


if __name__ == "__main__":
    unittest.main()
