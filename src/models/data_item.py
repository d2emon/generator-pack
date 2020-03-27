class DataItem:
    items = []

    def __init__(self, group_id, value):
        self.group_id = group_id
        self.value = value

    @classmethod
    def add_item(cls, item):
        cls.items.append(item)

    @classmethod
    def add_value(cls, group_id, value):
        cls.add_item(cls(group_id, value))

    @classmethod
    def add_values(cls, group_id, values):
        for value in values:
            cls.add_value(group_id, value)

    @classmethod
    def get_items(cls, query=lambda item: True):
        return (item for item in cls.items if query(item))

    @classmethod
    def get_by_group(cls, group_id):
        return cls.get_items(lambda i: i.group_id == group_id)

    @classmethod
    def get_values_by_group(cls, group_id):
        return (item.value for item in cls.get_by_group(group_id))
