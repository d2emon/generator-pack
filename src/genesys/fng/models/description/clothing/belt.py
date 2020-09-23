from genesys.model.models import Model


class Belt(Model):
    def __init__(self):
        self.size = "thin"
        self.name = "leather belt"
        self.buckle = "a big belt buckle"
        self.decoration = "purely decorative and a sign of wealth",

    def __repr__(self):
        return self.name

    @property
    def description(self):
        return "%s %s, which is held together by %s" % (
            self.size,
            self.name,
            self.buckle,
        )


class FemaleBelt(Belt):
    def __repr__(self):
        return " ".join([
           self.size,
            self.name,
        ])


class SleeveBand(Belt):
    def __repr__(self):
        return "%s, %s %s" % (
            self.size,
            self.decoration,
            self.name,
        )
