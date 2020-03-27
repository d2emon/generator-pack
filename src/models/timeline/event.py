class Event:
    def __init__(self, year=0, title="<UNKNOWN>"):
        self.year = year
        self.title = title

    def __str__(self):
        return "{} лет назад: {}".format(self.year, self.title)

    def __repr__(self):
        return str(self)
