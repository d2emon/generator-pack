from models.models.point import Point
from ..factory import Factory


class RadiationFactory(Factory):
    def __init__(
        self,
        provider=None,
        start_point=None,
        end_point=None,
        speed=None,
    ):
        """
        Radiation factory constructor

        :param provider: Data providers
        :param start_point: Starting point for radiation
        :param end_point: Ending point for radiation
        :param speed: Radiation speed
        """
        super().__init__(provider)
        self.start_point = start_point or Point.polar(
            next(self.provider.radius),
            next(self.provider.angle),
        )
        self.end_point = end_point or Point.polar(
            next(self.provider.radius),
            0,  # next(self.providers.angle),
        )
        self.speed = speed or next(self.provider.speed)

    def model(self, time=None, *args, **kwargs):
        """
        Get point by time

        :param time: Time from start
        :param args: Point args
        :param kwargs: Point kwargs
        :return: Point
        """
        if time is None:
            time = next(self.provider.time)

        return Point.diffuse(
            self.start_point,
            self.end_point.rotate(time * self.speed),
        )
