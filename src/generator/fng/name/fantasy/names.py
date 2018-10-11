import random

GENDER_NEUTRAL = 0
GENDER_MALE = 1
GENDER_FEMALE = 2


class Names:
    data = []

    @classmethod
    def get_parts(cls):
        return [random.choice(parts) for parts in cls.data]

    @classmethod
    def apply_rules(cls, parts):
        return parts

    @classmethod
    def test_swear(cls, name):
        return name

    @classmethod
    def glue(cls, parts):
        return "".join(parts)

    @classmethod
    def generate(cls, gender=GENDER_NEUTRAL):
        name = None
        while not name:
            parts = cls.get_parts()
            parts = cls.apply_rules(parts)
            name = cls.test_swear(cls.glue(parts))
        return name


def random_class(selector, max_value=10):
    return selector(random.randrange(max_value))
