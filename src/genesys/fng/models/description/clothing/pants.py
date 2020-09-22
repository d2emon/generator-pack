class Pants(Sleeves):
    def __init__(self):
        self.name = "pants"
        self.style = "rough"

    def __repr__(self):
        return "%s %s" % (
            self.style,
            self.name,
        )
