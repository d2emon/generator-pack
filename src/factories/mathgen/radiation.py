from genesys.model.models.point import Point
from ..factory import Factory


class RadiationFactory(Factory):
    """
    Generate radiated point
    """

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
        super().__init__()
        self.__provider = provider
        self.start_point = start_point or Point.polar(
            next(self.__provider.radius),
            next(self.__provider.angle),
        )
        self.end_point = end_point or Point.polar(
            next(self.__provider.radius),
            0,  # next(self.providers.angle),
        )
        self.speed = speed or next(self.__provider.speed)

    @property
    def data(self):
        return self.__provider

    def build(self, time=None, *args, **kwargs):
        """
        Get point by time

        :param time: Time from start
        :param args: Point args
        :param kwargs: Point kwargs
        :return: Point
        """
        if time is None:
            time = next(self.data.time)

        return Point.diffuse(
            self.start_point,
            self.end_point.rotate(time * self.speed),
        )
