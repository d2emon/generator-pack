from orm.models.models import Model


class SleeveLength:
    def __init__(self, name="long", is_long= False):
        self.name = name
        self.is_long = is_long

    def __repr__(self):
        return self.name


class Sleeves(Model):
    def __init__(self):
        super().__init__()
        self.length = SleeveLength("long", True)
        self.width = "incredibly wide"
        self.reach = "his hands"
        self.decoration = "a single thread lining from top to bottom"

    def __repr__(self):
        return "%s and reach down to %s, they're decorated with %s" % (
            self.width,
            self.reach,
            self.decoration,
        )
