from genesys.generator import Generated, ListGenerator


class Hair(Generated):
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


class HairGenerator(ListGenerator):
    generated_class = Hair
    colors = [
        "Black",
        "Gray",
        "White",
        "Blonde",
        "Brown",
        "Red",
        "Ginger",
        "Chestnut",
        "Silver",
    ]
    hairtypes = [
        "short hair",
        "short spiky hair",
        "short bristly hair",
        "well groomed hair",
        "crinkly hair",
        "sleek hair",
        "flowing hair",
        "shaggy hair",
        "well groomed hair",
        "long hair",
        "curly hair",
        "straight hair",
        "wavy hair",
        "frizzy hair",
        "coily hair",
        "long hair",
        "curly hair",
        "straight hair",
        "wavy hair",
        "frizzy hair",
        "coily hair",
        "dreadlocks",
        "shoulder-length hair",
    ]
    hairstyles = [
        "hangs over",
        "slightly reveals",
        "tight in a ponytail reveals",
        "gently hangs over",
        "slightly covers",
        "almost fully covers",
        "clumsily hangs over",
        "awkwardly hangs over",
        "neatly coiffured to reveal",
        "is pulled back to reveal",
    ]

    @classmethod
    def fill_generated(cls, generated, sex=0):
        generated.color = cls.generate_value(cls.colors)
        generated.hairtype = cls.generate_value(cls.hairtypes)
        generated.hairstyle = cls.generate_value(cls.hairstyles)
        return generated


class MaleHairGenerator(HairGenerator):
    pass


class FemaleHairGenerator(HairGenerator):
    hairtypes = [
        "short hair",
        "short curly hair",
        "short layered hair",
        "well groomed hair",
        "crinkly hair",
        "sleek hair",
        "flowing hair",
        "shaggy hair",
        "well groomed hair",
        "long hair",
        "curly hair",
        "straight hair",
        "wavy hair",
        "frizzy hair",
        "coily hair",
        "short hair",
        "long hair",
        "curly hair",
        "straight hair",
        "wavy hair",
        "frizzy hair",
        "coily hair",
        "dreadlocks",
        "hip-length hair",
        "shoulder-length hair",
    ]
    hairstyles = [
        "hangs over",
        "slightly reveals",
        "braided to reveal",
        "double braided to reveal",
        "tight in a bun reveals",
        "tight in a ponytail reveals",
        "gently hangs over",
        "slightly covers",
        "almost fully covers",
        "clumsily hangs over",
        "awkwardly hangs over",
        "neatly coiffured to reveal",
        "is pulled back to reveal",
    ]
