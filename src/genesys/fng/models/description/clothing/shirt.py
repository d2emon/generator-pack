from orm.models.models import Model


class Shirt(Model):
    def __init__(self):
        self.name = "shirt"
        self.style = "rough"
        self.sleeves = SleevesGenerator.generate()

    def __repr__(self):
        return "%s %s" % (
            self.style,
            self.name,
        )
