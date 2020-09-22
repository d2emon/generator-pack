class Encounter:
    description = None
    is_daily = False
    is_nightly = False

    def __init__(
        self,
        distance_type=None,
        distance=None,
    ):
        self.distance_type = distance_type
        self.__distance = distance

    @property
    def distance(self):
        if self.__distance is None:
            self.__distance = self.generate_distance()
        return self.__distance

    @distance.setter
    def distance(self, value):
        self.__distance = value

    @property
    def meters(self):
        return int(self.distance / 3)

    @property
    def distance_description(self):
        return "Расстояние:\t{} м".format(self.distance)

    def generate_distance(self):
        return self.distance_type.generate() if self.distance_type else None

    def __str__(self):
        return "{}\n{}\n".format(self.distance_description, self.description)
