class DistanceGroup:
    def __init__(
        self,
        description=None,
        dice=None,
        avoidable=True,
        allowed_at=None,
    ):
        self.description = description
        self.dice = dice
        self.avoidable = avoidable
        self.allowed_at = allowed_at or []

    def __str__(self):
        return str(self.description)
