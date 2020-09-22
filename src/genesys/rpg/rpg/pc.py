class PlayerCharacter:
    default_name = "Player"

    def __init__(self, name=None):
        self.name = name or self.default_name

    def show(self):
        print(self.name)
