from models.name.named import Named


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
        while abs(self.size) < 1:
            self.dec_scale()

        while abs(self.size) > 10:
            self.inc_scale()

    def __str__(self):
        self.adjust()

        return f"{self.size:.2f}*10^{self.scale}m"


class Sized(Named):
    width = Named.field_property('width')
    length = Named.field_property('length')
    height = Named.field_property('height')

    def __init__(
        self,
        name='',
        length=None,
        width=None,
        height=None,
        *args,
        **kwargs,
    ):
        super().__init__(
            name=name,
            height=height,
            length=length,
            width=width,
            *args,
            **kwargs,
        )

    @property
    def field_names(self):
        yield from super().field_names
        yield "width"
        yield "length"
        yield "height"

    @property
    def sizes(self):
        return filter(
            None,
            [
                self.width,
                self.length,
                self.height,
            ],
        )

    def __str__(self):
        sizes = " x ".join(str(size) for size in self.sizes)
        return f"{self.name} ({sizes})"


class Distance(Sized):
    value = Named.field_property('length')

    def __init__(
        self,
        name='',
        distance=0,
        *args,
        **kwargs,
    ):
        Sized.__init__(
            self,
            name,
            length=distance,
            *args,
            **kwargs,
        )

    def __str__(self):
        return f"Расстояние {self.name} - {self.value}"
