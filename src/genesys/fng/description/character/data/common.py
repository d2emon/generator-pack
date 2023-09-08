from models.name_block import NameBlock


def with_gender(f, gender_id, default_values=None):
    values = {
        'gender_id': gender_id,
    }

    if default_values is not None:
        values.update(default_values.get(gender_id, {}))

    def wrapped(**kwargs):
        result = {**values}
        result.update(**kwargs)
        yield from f(**result)
    return wrapped


def add_items(group_id, gender_id, map_item=lambda item: item):
    def f(items):
        blocks = NameBlock.filled(
            *items,
            group_id=group_id,
            gender_id=gender_id,
        )
        return map(map_item, blocks.values)
    return f


def add_items_data(gender_id, default_values):
    def wrapper(**options):
        def f(**kwargs):
            values = {**default_values}
            values.update(kwargs)

            result = NameBlock()
            for group_id, items in values.items():
                result = result.fill(
                    *items,
                    **options,
                    group_id=group_id,
                    gender_id=gender_id,
                )
            return result.values
        return f
    return wrapper
