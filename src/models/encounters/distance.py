from models.model import Model


class Distance(Model):
    KILOMETERS_IN_MILE = 0.621371
    METERS_IN_FOOT = 1 / 0.3048

    distance = Model.field_property('distance', 0)
    distance_group = Model.field_property('distance_group', None)

    def __init__(
        self,
        distance=0,
        distance_group=None,
        *args,
        **kwargs,
    ):
        super().__init__(
            distance=distance,
            distance_group=distance_group,
            *args,
            **kwargs,
        )

    @classmethod
    def ft_to_m(cls, feet):
        return round(feet / cls.METERS_IN_FOOT)

    @classmethod
    def m_to_ft(cls, meters):
        return round(meters * cls.METERS_IN_FOOT)

    @classmethod
    def miles_to_km(cls, miles):
        return round(miles / cls.KILOMETERS_IN_MILE)

    @classmethod
    def km_to_miles(cls, kilometers):
        return round(kilometers * cls.KILOMETERS_IN_MILE)

    @property
    def field_names(self):
        yield "distance"
        yield "distance_group"

    @property
    def feet(self):
        return self.distance

    @feet.setter
    def feet(self, value):
        self['distance'] = value

    @property
    def meters(self):
        return round(self.distance / self.METERS_IN_FOOT)

    @meters.setter
    def meters(self, value):
        self['distance'] = value * self.METERS_IN_FOOT

    @property
    def value(self):
        return self.meters

    @value.setter
    def value(self, value):
        self.meters = value

    def __str__(self):
        return f"Расстояние:\t{self.meters} м\t{self.distance_group.description}"
