class Generated:
    # title = "<UNTITLED>"
    title = None
    fields = []

    def __init__(self, value=None, **kwargs):
        self.value = value
        for field in self.fields:
            setattr(self, field, kwargs.get(field))

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        if self.title is None:
            return str(self)
        return "{item.title}:\t\"{item.value}\"".format(item=self)

    @property
    def generated_value(self):
        return self.value

    @property
    def description(self):
        return str(self)
