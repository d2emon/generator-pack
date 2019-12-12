class DataItem:
    items = []

    def __init__(self, group_id, value):
        self.group_id = group_id
        self.value = value

    @classmethod
    def add_item(cls, item):
        cls.items.append(item)

    @classmethod
    def get_items(cls, query=lambda item: True):
        return (item for item in cls.items if query(item))


def add_to_group(group_id, value):
    DataItem.add_item(DataItem(group_id, value))


def get_from_group(group_id):
    return (item.value for item in DataItem.get_items(lambda i: i.group_id == group_id))
