from uuid import uuid4


class Database:
    def __init__(self, *data):
        self.data = [{ "id": uuid4(), "value": value } for value in data]

    def find(self, condition):
        return (
            item
            for item in self.data
            if condition(item.get("value"))
        )

    def values(self):
        return [ item.get("value") for item in self.data ]
