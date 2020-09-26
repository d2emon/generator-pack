class ScalableSize:
    def __init__(self, size, scale=0):
        self.size = size
        self.scale = scale
        self.adjust()

    def adjust(self):
        while self.size < 1:
            if self.size <= 0:
                break
            self.scale -= 1
            self.size *= 10

        while self.size > 10:
            self.scale += 1
            self.size /= 10

    def __repr__(self):
        self.adjust()
        return "{0:.2f}*10^{1}m".format(self.size, self.scale)


class Scalable:
    def __init__(self, name, width, scale=0, length=None):
        self.name = name
        self.width = ScalableSize(width, scale)
        self.length = length and ScalableSize(length, scale)

    def __repr__(self):
        if self.length is None:
            return "{} ({})".format(self.name, self.width)
        return "{} ({} x {})".format(self.name, self.width, self.length)


class Distance(Scalable):
    def __init__(self, name, size, scale=0):
        Scalable.__init__(self, name, size, scale)

    def __repr__(self):
        return "Расстояние {} - {}".format(self.name, self.width)
