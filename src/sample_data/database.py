__DATA = []


def add_item(item):
    __DATA.append(item)


def get_items(query=lambda item: True):
    return (item for item in __DATA if query(item))


def add_to_group(group_id, value):
    add_item({
        'group_id': group_id,
        'value': value,
    })


def get_from_group(group_id):
    return get_items(lambda item: item.get('group_id') == group_id)
