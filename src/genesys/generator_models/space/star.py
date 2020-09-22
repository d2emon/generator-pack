from ..generator_models import Model


class Star(Model):
    def __init__(self, sun_type=None, blue=False):
        super().__init__()
        self.star_type = sun_type
        self.title = sun_type
        self.image = sun_type
        self.blue = blue
        self.planets = []

    def __repr__(self):
        return "{}: {} ({}) - {}".format(
            'Star',
            self.title,
            self.blue,
            self.planets,
        )
