class DistanceGroup:
    def __init__(
        self,
        description=None,
        dice=None,
        avoidable=True,
        allowed_at=None,
    ):
        self.allowed_at = allowed_at or []
        self.avoidable = avoidable
        self.description = description
        self.dice = dice

    def __str__(self) -> str:
        return self.description