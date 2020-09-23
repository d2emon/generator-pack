from genesys.model.keyed.model import Model


class DataItem(Model):
    fields = [
        'group_id',
        'value',
    ]
    items = []

    @property
    def group_id(self):
        return self['group_id']

    @property
    def value(self):
        return self['value']

    def save(self):
        self.items.append(self)

    @classmethod
    def all(cls, query=lambda item: True):
        return filter(query, cls.items)

    # New methods

    @classmethod
    def add_values(cls, group_id, values):
        for value in values:
            cls(group_id=group_id, value=value).save()

    @classmethod
    def by_group_id(cls, group_id):
        return cls.all(lambda i: i.group_id == group_id)

    @classmethod
    def values_by_group_id(cls, group_id):
        return (item.value for item in cls.by_group_id(group_id))
