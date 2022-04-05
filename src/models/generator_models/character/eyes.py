from ..generator_models import Model


class Eyes(Model):
    def __init__(self):
        self.style = "Beady"
        self.color = "blue"
        self.depth = "deep"
        self.sight = "wearily"

    def __repr__(self):
        # names6[random6] + " " + names7[random7] + " eyes, set " + names8[random8] + " within their sockets, watch " + names9[random9]
        return "%s %s eyes, set %s within their sockets, watch %s" % (
            self.style,
            self.color,
            self.depth,
            self.sight,
        )
