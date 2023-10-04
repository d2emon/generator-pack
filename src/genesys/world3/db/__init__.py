import uuid


class DB:
    __RECORDS = []

    @classmethod
    def find(cls, query=lambda record: True):
        return (record for record in cls.__RECORDS if query(record))

    @classmethod
    def get(cls, record_id):
        return next(cls.find(lambda record: record.record_id == record_id), None)

    @classmethod
    def add(cls, record):
        record.record_id = record.record_id or uuid.uuid4()
        cls.__RECORDS.append(record)
        return record

    @classmethod
    def delete(cls, record_id):
        record = cls.get(record_id)
        if record is None:
            return
        cls.__RECORDS.remove(record)

    @classmethod
    def update(cls, record):
        cls.delete(record.record_id)
        return cls.add(record)


class Model:
    def __init__(
        self,
        record_id=None,
        name=None,
        group_id=None,
        parent_id=None,
        parent=None,
    ):
        self.record_id = record_id
        self.name = name
        self.group_id = group_id
        self.parent_id = parent.parent_id if parent else parent_id

    @property
    def parent(self):
        return DB.get(self.parent_id)

    @parent.setter
    def parent(self, value):
        self.parent_id = value.parent_id if value else None

    @property
    def neighbours(self):
        return DB.find(lambda record: record.parent_id == self.parent_id)

    @property
    def children(self):
        return DB.find(lambda record: record.parent_id == self.record_id)

    @classmethod
    def find(cls, query=lambda record: True):
        return DB.find(query)

    @classmethod
    def get(cls, record_id):
        return DB.get(record_id)

    def save(self):
        return DB.update(self)


class NestedModel(Model):
    def __init__(
        self,
        model,
        record_id=None,
        name=None,
        parent_id=None,
        parent=None,
    ):
        self.model = model
        super().__init__(
            record_id=record_id,
            name=name,
            group_id=model.__class__,
            parent_id=parent_id,
            parent=parent,
        )
