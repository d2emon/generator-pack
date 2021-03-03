def item_is_not_unique(unique_with):
    def f(item):
        return str(item) in map(str, unique_with)

    return f


def item_equals(value):
    def f(item):
        return str(item) == value

    return f


def generate_while(item, condition=lambda item: True, block=None):
    if block is None:
        return item

    while condition(item):
        item = next(block)

    return item
