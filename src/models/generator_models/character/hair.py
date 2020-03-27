from ..generator_models import Model


class Hair(Model):
    def __init__(
        self,
        color="Black",
        hairtype="short hair",
        hairstyle="hangs over"
    ):
        self.color = color
        self.hairtype = hairtype
        self.hairstyle = hairstyle

    def __repr__(self):
        # names1[random1] + ", " + names2[random2] + " " + names3[random3]
        return "%s, %s %s" % (self.color, self.hairtype, self.hairstyle)
