import random
import uuid
from .database.worlds import types, shapes, sizes, worlds


class Model:
    database = None
    fields = []
    children = {}

    def __init__(self, **fields):
        self.uuid = None
        for k, v in fields.items():
            self.__setattr__(k, v)

    def save(self):
        self.database.update(self.__serialize())
        self.database.save()

    def __serialize(self):
        result = {}
        for field in (self.fields + list(self.children.keys())):
            value = self.__getattribute__(field)
            result[field] = value if not isinstance(value, Model) else value.uuid
        return result

    @classmethod
    def __deserialize(cls, data=None):
        return cls(**data) if data is not None else None

    @classmethod
    def __all(cls, query=lambda item: True):
        return filter(query, cls.database.data)

    @classmethod
    def get(cls, item_id):
        return cls.first(lambda item: item.get('uuid') == item_id)

    @classmethod
    def random(cls):
        fields = {'uuid': uuid.uuid4()}

        records = list(cls.__all())
        if records:
            fields.update(random.choice(records))

        for k, v in cls.children.items():
            fields[k] = fields.get(k, v.random())

        return cls.__deserialize(fields)

    @classmethod
    def all(cls, query=lambda item: True):
        return map(cls.__deserialize, cls.__all(query))

    @classmethod
    def first(cls, query=lambda item: True):
        return cls.__deserialize(next(cls.__all(query), None))


class WorldShape(Model):
    database = shapes
    fields = [
        'name',
        'description',
    ]

    def __init__(self, **fields):
        self.name = None
        self.description = None
        super().__init__(**fields)


class WorldSize(Model):
    database = sizes
    fields = [
        'name',
        'size_class',
        'size',
        'min_size',
        'max_size',
    ]

    def __init__(self, **fields):
        self.name = None
        self.size_class = None
        self.size = None
        self.min_size = None
        self.max_size = None
        super().__init__(**fields)
        self.min_size = int(self.min_size) if self.min_size else 0
        self.max_size = int(self.max_size) if self.max_size else None

    @property
    def text(self):
        return "\n".join([
            "Класс размера:\t{size_class.size_class}",
            "Описание:\t\t{size_class.name}",
            "Размер:\t\t\t{size_class.size}",
        ]).format(size_class=self)

    def generate_size(self):
        if self.min_size is None:
            return random.randrange(self.max_size)
        if self.max_size is None:
            return self.min_size
        if self.min_size == self.max_size:
            return self.min_size
        return random.randrange(self.min_size, self.max_size)


class WorldType(Model):
    database = types
    fields = [
        'world_type',
        'description',
        'encounters',
        'sizes',
    ]

    def __init__(self, **fields):
        self.world_type = None
        self.description = None
        self.encounters = None
        self.sizes = None
        super().__init__(**fields)

    def generate_size(self):
        if not self.sizes:
            return None
        size_class = random.choice(self.sizes)
        return WorldSize.first(lambda item: item.get('size_class') == size_class)


class World(Model):
    database = worlds
    fields = [
        'size',
        'size_class',
    ]
    children = {
        'shape': WorldShape,
        'world_type': WorldType,
        # 'size_class': WorldSize,
    }

    def __init__(
        self,
        size_class=None,
        size=None,
        **fields,
    ):
        self.shape = None
        self.world_type = None
        self.__size_class = size_class
        self.__size = size
        super().__init__(**fields)

    @property
    def size_class(self):
        if self.__size_class is None:
            self.__size_class = self.world_type.generate_size() if self.world_type else None
        return self.__size_class

    @property
    def size(self):
        if self.__size is None:
            size_class = self.size_class
            self.__size = size_class.generate_size() if size_class else None
        return self.__size

    @property
    def description(self):
        return "\n".join([
            "{world_type.world_type} {shape.name} ({size} миль)",
            "{world_type.description}",
            "Возможные столкновения: {world_type.encounters}",
            "{shape.description}",
            "{size_class.text}",
        ]).format(
            size=self.size,
            shape=self.shape,
            size_class=self.size_class,
            world_type=self.world_type,
        )
