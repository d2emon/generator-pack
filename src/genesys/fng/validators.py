def item_is_unique(unique_with):
    """
    Check if item is not unique

    :param unique_with: Values to check
    :return: Item validator
    """

    def f(item):
        return str(item) not in map(str, unique_with)

    return f


def item_is_not_unique(unique_with):
    """
    Check if item is not unique

    :param unique_with: Values to check
    :return: Item validator
    """

    def f(item):
        return str(item) in map(str, unique_with)

    return f


def item_is_not_empty():
    """
    Check if item is not empty

    :return: Item validator
    """

    def f(item):
        return str(item) != ''

    return f


def item_equals(value):
    """
    Check if item equals value

    :param value: Value to check
    :return: Item validator
    """

    def f(item):
        return str(item) == value

    return f


def validate_if(condition, validator):
    """
    Check if item equals value

    :param value: Value to check
    :return: Item validator
    """

    def f(item):
        if not condition():
            return True

        return validator(item)

    return f


def generate_while(item, condition, factory):
    """
    Generate item while condition is true

    :param item: Item value
    :param condition: Condition to check
    :param factory: Data factory for item
    :return: Item value
    """
    while not condition(item):
        item = factory()
    return item