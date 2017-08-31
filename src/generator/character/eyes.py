from generator import Generated, ListGenerator


class Eyes(Generated):
    def __init__(self):
        self.style = "Beady"
        self.color = "blue"
        self.depth = "deep"
        self.sight = ""

    def __repr__(self):
        return "%s %s eyes, set %s within their sockets, watch %s" % (
            self.style,
            self.color,
            self.depth,
            self.sight,
        )


class EyesGenerator(ListGenerator):
    generated_class = Eyes
    styles = [
        "Beady",
        "Big, round",
        "Bloodshot",
        "Bright",
        "Bulging",
        "Clear",
        "Dancing",
        "Darting",
        "Dead",
        "Expressive",
        "Gentle",
        "Glinting",
        "Glistening",
        "Glittering",
        "Heavy",
        "Hollow",
        "Hooded",
        "Lidded",
        "Narrow",
        "Piercing",
        "Round",
        "Shining",
        "Shuttered",
        "Small",
        "Smart",
        "Sparkling",
        "Squinting",
        "Wide",
        "Woeful",
    ]
    colors = [
        "blue",
        "brown",
        "hazel",
        "black",
        "green",
        "amber",
        "gray",
    ]
    depths = [
        "deep",
        "narrowly",
        "buried",
        "far",
        "rooted",
        "well",
        "low",
        "high",
        "sunken",
        "lightly",
        "thightly",
        "graciously",
        "concealed",
        "delicately",
        "elegantly",
        "handsomely",
        "a-symmetrically",
        "gracefully",
        "seductively",
        "appealingly",
        "charmingly",
        "dreadfully",
        "wickedly",
    ]
    sights = [
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.style = cls.generate_value(cls.styles)
        generated.color = cls.generate_value(cls.colors)
        generated.depth = cls.generate_value(cls.depths)
        generated.sight = cls.generate_value(cls.sights)
        return generated


class ElfEyesGenerator(EyesGenerator):
    colors = [
        "Elf",
    ]
