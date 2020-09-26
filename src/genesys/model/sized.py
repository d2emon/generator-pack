class ScalableSize:
    def __init__(self, size, scale=0):
        self.size = size
        self.scale = scale
        self.adjust()

    def dec_scale(self):
        self.scale -= 1
        self.size *= 10

    def inc_scale(self):
        self.scale += 1
        self.size /= 10

    def adjust(self):
        while 0 < self.size < 1:
            self.dec_scale()

        while self.size > 10:
            self.inc_scale()

    def __str__(self):
        self.adjust()
        return f"{self.size:.2f}*10^{self.scale}m"


class Named:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)


class Sized(Named):
    def __init__(
        self,
        name,
        width=1,
        length=None,
        height=None,
        scale=0,
    ):
        super().__init__(name)
        self.width = width and ScalableSize(width, scale)
        self.length = length and ScalableSize(length, scale)
        self.height = height and ScalableSize(height, scale)

    def __str__(self):
        sizes = " x ".join(filter(
            None,
            [
                self.width,
                self.length,
                self.height,
            ],
        ))
        return f"{self.name} ({sizes})"


class Distance(Sized):
    def __init__(
        self,
        name,
        distance,
        scale=0,
    ):
        Sized.__init__(
            self,
            name,
            width=distance,
            scale=scale,
        )

    def __str__(self):
        return f"Расстояние {self.name} - {self.width}"
