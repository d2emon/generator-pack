class Generated:
    # title = "<UNTITLED>"
    title = None
    fields = []

    def __init__(self, value=None, **kwargs):
        self.value = value
        for field in self.fields:
            setattr(self, field, kwargs.get(field))

    def __repr__(self):
        if self.title is None:
            return str(self.value)
        return "{}:\t\"{}\"".format(self.title, self.value)

    @property
    def generated_value(self):
        return self.value

    @property
    def description(self):
        return str(self)
