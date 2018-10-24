class PartyCharacter:
    def __init__(self, name):
        self.name = name
        self.stats = []
        self.hp = 10
        self.ac = 10
        self.save_throws = [None, None, None]
        self.hands = [None, None]
        self.level = {
            "level": 1,
            "xp": 0
        }


party = [
]