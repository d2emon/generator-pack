from ..generator_models import Model


class Face(Model):
    def __init__(self):
        self.facetype = "thin"
        self.expression = "time-worn"

    def __repr__(self):
        # names4[random4] + ", " + names5[random5] + " face. "
        return "%s, %s face" % (self.facetype, self.expression)
