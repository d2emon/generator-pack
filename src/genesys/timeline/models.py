from models.model import Model


class Event(Model):
    @property
    def year(self):
        return self.data.get('year', 0)

    @property
    def title(self):
        return self.data.get('title', '<UNKNOWN>')

    def __str__(self):
        return "{} лет назад: {}".format(self.year, self.title)
