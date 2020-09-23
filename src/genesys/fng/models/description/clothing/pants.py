from .sleeves import Sleeves


class Pants(Sleeves):
    def __init__(self):
        super().__init__()
        self.name = "pants"
        self.style = "rough"

    def __str__(self):
        return "%s %s" % (
            self.style,
            self.name,
        )
