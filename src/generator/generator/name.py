import random

GENDER_NEUTRAL = 0
GENDER_MALE = 1
GENDER_FEMALE = 2


def random_generator(selector, generator_id=None, max_value=10):
    if generator_id is None:
        generator_id = random.randrange(max_value)
    return selector(generator_id)


class Name:
    def __init__(self, name, generator=None):
        self._name = name
        self.generator = generator

    @classmethod
    def test_name(cls, name):
        return name

    @property
    def name(self):
        return self.test_name(self._name).title()

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class NameGenerator:
    data = []
    glue = ""

    @classmethod
    def generate_parts(cls, *args, **kwargs):
        return [random.choice(parts) for parts in cls.data]

    @classmethod
    def update_parts(cls, parts):
        return parts

    @classmethod
    def generate(cls, gender=GENDER_NEUTRAL, *args, **kwargs):
        parts = cls.generate_parts(gender=gender, *args, **kwargs)
        parts = cls.update_parts(parts)
        return Name(cls.glue.join(parts), cls)

    def __iter__(self):
        return self

    def __next__(self):
        return self.generate()
