from factories.factory import Factory
from models.scales.distance import Distance


class DistanceFactory(Factory):
    def __init__(
        self,
        distance_group=None,
    ):
        self.distance_group = distance_group

    def __call__(self, *args, **kwargs):
        if self.distance_group is None:
            return None

        return Distance(
            distance=self.distance_group.dice.total(),
            distance_group=self.distance_group,
        )
