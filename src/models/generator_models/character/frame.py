from ..generator_models import Model


class Frame(Model):
    def __init__(self):
        self.height = "tall among"
        self.frame = "thin"

    def __repr__(self):
        return "{{He}} stands %s others, despite {{his}} %s frame." % (
            self.height,
            self.frame,
        )
