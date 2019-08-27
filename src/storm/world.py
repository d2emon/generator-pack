import random
import uuid
from .database.worlds import types, shapes, sizes, worlds
"""
Если исключить надоевшие планеты по типу Земли, какие ещё обитаемые
пространства можно встретить на необъятных просторах фэнтези-космоса?
Существует несметное множество небесных тел, разных форм, типов и размеров. Это
может быть и Первичное тело Хрустальных Сфер (звезда, вокруг которой вращаются
планеты ее планетарной системы) или быть самостоятельными планетами
(уединенными мирами, бегущими сквозь космический сумрак по беговой дорожке
орбиты), а могут существовать в виде большой группы (например, астероиды имеют
свойства объединяться в пояса и кластеры).

3 Типы Миров
3.1 Воздушные Миры
3.2 Земляные Миры
3.3 Огненные миры
3.4 Водные Миры
3.5 Живой мир

Формы миров

Да, как я говорил выше, типов небесных тел великое множество. Тут впору было бы
запутаться, но привычка классифицировать все и вся на этот раз сослужила мне
хорошую службу, и потому я поведаю вам о том, как разложить по полочкам все это
«разнообразие видов» космических достопримечательностей и чувствовать себя в
космических дебрях, как рыба в воде. Ну или что-то вроде того.

Итак, первая характерная особенность — это форма космического объекта. Хотя
большинство миров — это сферы, хотя бы приблизительно, встречаются и
многочисленные примеры небесных тел, форма которых отличается от «стандартной».

Размер миров

Миры — очень большие объекты, даже в космическом масштабе. Наименьшие из таких
объектов имеют размер С, а те что еще меньше — уже попадают в разряд
планетоидов. Верхнего предела размерности нет, но даже самые большие звезды,
редко бывают больше 10 миллионов миль в диаметре.

Обычно водные и земные миры редко превышают размер F, а воздушные и огненные,
соответственно, редко бывают меньше размера D.

Обратите внимание: оригинальные правила Spelljammer классифицируют миры от А до
J и эта классификация используется большинством игроков. Но когда вышла 3, а
затем и 3.5 редакция правил Подземелий и Драконов, для измерения размеров стали
использоваться новые правила.

В этой таблице приводятся соотношения и тех и других измерений, дабы не обидеть
ни одну из сторон. Оба набора измерений правильны и могут использоваться
одновременно. К примеру, мир, размер которого по диаметру составляет 8000 миль,
можно свободно рассматривать как планету размера E, или как планету среднего
размера.

Какую именно шкалу использовать в игре — целиком и полностью зависит от выбора
ведущего.

Типы Миров

По типу, миры классифицируются исходя из того, какой элемент доминирует в их
составе. Большая часть миров попадает в четыре большие категории: воздушные,
земляные, огненные, водные. Некоторые культуры добавляют еще и пятый элемент —
жизнь, но как правило, таких миров очень мало — планета сплошь состоящая из
гигантских растений или являющаяся живой, в прямом смысле этого слова, даже в
бескрайнем космосе не встречается на каждом шагу.
"""


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
