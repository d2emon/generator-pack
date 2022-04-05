from ..generator_models import Model


class Attitude(Model):
    def __init__(self):
        self.attitude = "A scar"
        self.attitude2 = "A scar"

    def __repr__(self):
        return "people tend to %s, while %s" % (
            self.attitude,
            self.attitude2,
        )
