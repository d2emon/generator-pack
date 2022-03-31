from models.model import Model


class Event(Model):
    year = Model.field_property('year', 0)
    title = Model.field_property('title', '<UNKNOWN>')

    def __init__(self, year=0, title="<UNKNOWN>", *args, **kwargs):
        super().__init__(
            year=year,
            title=title,
            *args,
            **kwargs,
        )

    @property
    def field_names(self):
        yield "year"
        yield "title"

    @property
    def value(self):
        return self.title

    def __str__(self):
        return "{} лет назад: {}".format(self.year, self.title)
