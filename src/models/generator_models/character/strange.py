from ..generator_models import Model


class Strange(Model):
    def __init__(self):
        super().__init__()
        self.description = "Alluring"
        self.weirdnesses = []

    def __repr__(self):
        weirdness = " or perhaps it's simply ".join(self.weirdnesses)
        return "There's something %s about {{him}}, perhaps it's %s." % (
            self.description,
            weirdness,
        )
