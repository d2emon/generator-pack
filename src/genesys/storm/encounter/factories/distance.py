from models.encounters.distance import Distance


class DistanceFactory:
    def __init__(self, distance):
        self.distance = distance

    def __call__(self, *args, **kwargs):
        if self.distance is None:
            return None

        return Distance(
            self.distance,
            self.distance.dice.total(),
        )
