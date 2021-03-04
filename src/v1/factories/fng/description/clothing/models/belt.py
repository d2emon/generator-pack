from .clothing_model import ClothingModel


class Belt(ClothingModel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size = "thin"
        self.name = "leather belt"
        self.buckle = "a big belt buckle"
        self.decoration = "purely decorative and a sign of wealth",

    def __str__(self):
        return self.name

    @property
    def description(self):
        return "%s %s, which is held together by %s" % (
            self.size,
            self.name,
            self.buckle,
        )


class FemaleBelt(Belt):
    def __str__(self):
        return " ".join([
            self.size,
            self.name,
        ])


class SleeveBand(Belt):
    def __str__(self):
        return "%s, %s %s" % (
            self.size,
            self.decoration,
            self.name,
        )
