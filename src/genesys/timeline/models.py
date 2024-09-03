from models.model import Model


class Timeline(Model):
    def __init__(self, *args, **fields):
       super().__init__(*args, **fields)

    @property
    def events(self):
        return self.values

    @property
    def description(self):
        return "\n".join(str(event) for event in self.events)


class Event(Model):
    @property
    def year(self):
        return self.data.get('year', 0)

    @property
    def title(self):
        return self.data.get('title', '<UNKNOWN>')

    def __str__(self):
        return "{} лет назад: {}".format(self.year, self.title)
