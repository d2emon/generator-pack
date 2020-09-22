from ..generator_models import Model


class Promise(Model):
    def __init__(self):
        self.settlement = "village"
        self.promisetype = "protected"

    def __repr__(self):
        # "the " + names10[random10] + " they've " + names11[random11] + " for so long.";
        if "%s" in self.promisetype:
            return self.promisetype % (
                self.settlement,
            )
        return "the %s tey've %s for so long" % (
            self.settlement,
            self.promisetype,
        )
