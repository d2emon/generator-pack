from generator import Generated, ListGenerator


class Hair(Generated):
    def __init__(self):
        self.color = "Black"
        self.hairtype = "short hair"
        self.hairstyle = "hangs over"

    def __repr__(self):
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
    def fill_generated(cls, generated):
        generated.color = cls.generate_value(cls.colors)
        generated.hairtype = cls.generate_value(cls.hairtypes)
        generated.hairstyle = cls.generate_value(cls.hairstyles)
        return generated


class ElfHairGenerator(HairGenerator):
    colors = [
        "Elf",
    ]  # 1
    hairtypes = [
        "Elf",
    ]  # 2


class GnomeHairGenerator(HairGenerator):
    colors = [
        "Gnome",
    ]  # 1
    hairtypes = [
        "Gnome",
    ]  # 2


class GoblinHairGenerator(HairGenerator):
    hairtypes = [
        "Goblin",
    ]  # 2


class GiantHairGenerator(HairGenerator):
    hairtypes = [
        "Giant",
    ]  # 2
