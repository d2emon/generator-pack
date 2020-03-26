import random


class Named:
    def __init__(self, name):
        self.name = name


class Location:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)

    def __repr__(self):
        return str(self)


class Sized:
    def __init__(self, length=1, width=1, height=1):
        self.length = length
        self.width = width
        self.height = height

    def generate_coordinates(self):
        scale = 10
        return (
            random.randrange(self.length * scale) / scale,
            random.randrange(self.width * scale) / scale,
            random.randrange(self.height * scale) / scale,
        )


class Spheric(Sized):
    def __init__(self, radius=1):
        diameter = radius * 2
        super().__init__(diameter, diameter, diameter)

    @property
    def radius(self):
        return self.length / 2

    @property
    def diameter(self):
        return self.radius * 2

    """
    def generate_coordinates(self):
        angle_xy = random.randrange(360)
        angle_xz = random.randrange(360)
        r = random.randrange(int(self.radius))

        return (
            int(r * math.cos(angle_xy) + self.radius),
            int(r * math.sin(angle_xy) + self.radius),
            int(r * math.sin(angle_xz) + self.radius),
        )
    """
