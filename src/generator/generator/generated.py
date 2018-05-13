class Generated():
    title = None

    def __init__(self, value=""):
        self.value = value

    def __repr__(self):
        if self.title is None:
            return str(self.value)
        return "{}:\t\"{}\"".format(self.title, self.value)

    @property
    def generated_value(self):
        return self.value
