from .clothing_model import ClothingModel


class SleeveLength:
    def __init__(self, name="long", is_long= False):
        self.name = name
        self.is_long = is_long

    def __str__(self):
        return self.name


class Sleeves(ClothingModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.length = SleeveLength("long", True)
        self.width = "incredibly wide"
        self.reach = "his hands"
        self.decoration = "a single thread lining from top to bottom"

    def __str__(self):
        return "%s and reach down to %s, they're decorated with %s" % (
            self.width,
            self.reach,
            self.decoration,
        )
