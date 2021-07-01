class Director:
    def __init__(self, builder):
        self.builder = builder

    def build(self, *args, **kwargs):
        self.builder.reset()
        # Some actions with builder
        return self.builder.result
