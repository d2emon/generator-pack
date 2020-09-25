class Distance:
    def __init__(
        self,
        distance_group,
        distance=None,
    ):
        self.distance_group = distance_group
        self.distance = distance

    @property
    def meters(self):
        return int(self.distance * 0.3048)

    @classmethod
    def km(cls, miles):
        return int(miles / 0.621371)

    def __str__(self):
        return f"Расстояние:\t{self.meters} м\t{self.distance_group.description}"
