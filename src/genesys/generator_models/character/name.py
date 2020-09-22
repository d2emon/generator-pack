from ..generator_models import Model


class Name(Model):
    def __init__(self):
        super().__init__()
        self.firstname = "Adam"
        self.lastname = "Adwell"
        self.title = ""

    def __repr__(self):
        # names18[random18] + " " + names19[random19] + ", a true " + names20[random20]
        return "%s %s, a true %s" % (
            self.firstname,
            self.lastname,
            self.title,
        )
