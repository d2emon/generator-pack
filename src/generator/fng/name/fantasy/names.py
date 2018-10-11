import random


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
    def generate(cls):
        name = None
        while not name:
            parts = cls.get_parts()
            parts = cls.apply_rules(parts)
            name = cls.test_swear("".join(parts))
        return name


def random_class(selector, max_value=10):
    return selector(random.randrange(max_value))
