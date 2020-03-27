from factories.generator import MaleHairGenerator, FemaleHairGenerator
from factories.generator import FaceGenerator
from factories.generator import NameGenerator
from factories.generator import Race


gnome_hair_colors = [
    "Purple",
    "Blue",
    "Green",
    "Red",
    "White",
    # "Blonde",
    "Brown",
    "Light blue",
    "Light green",
    # "Pink",
    "Orange",
    "Silver",
    "Golden",
    "Yellow",
    "Black",
    "Blue",
    "Brown",
    "Hazel",
    "Black",
    "Green",
    "Amber",
    "Gray",
]  # 1

gnome_hairtypes = [
    "short hair",
    "short hair",
    "short hair",
    # "perfectly groomed hair",
    # "well groomed hair",
    # "sleek hair",
    "long hair",
    "curly hair",
    "straight hair",
    # "flowing hair",
    # "wavy hair",
    "sleek hair",
    "frizzy hair",
    "shaggy hair",
    "shoulder-length hair",
]  # 2


class GnomeMaleHairGenerator(MaleHairGenerator):
    colors = gnome_hair_colors
    hairtypes = gnome_hairtypes


class GnomeFemaleHairGenerator(FemaleHairGenerator):
    colors = gnome_hair_colors
    hairtypes = gnome_hairtypes


class GnomeFaceGenerator(FaceGenerator):
    facetypes = [
        "thin",
        # "chiseled",
        # "craggy",
        "fine",
        "fresh",
        "full",
        # "furrowed",
        "handsome",
        # "sculpted",
        # "strong",
        # "long",
        "round",
        "bony",
        "lean",
        "skinny",
        "fat",
    ]


class GnomeMaleNameGenerator(NameGenerator):
    firstnames = [
        "Glinoflonk",
        "Bonlebick",
        "Bimbik",
        "Gnobflink",
        "Binflonk",
        "Nittlewizz",
        "Gimkink",
        "Merbibus",
        "Totonk",
        "Dinnus",
    ]
    lastnames = [
        "Steambonk",
        "Berryspark",
        "Spannerwhistle",
        "Steamspanner",
        "Tosslefuse",
        "Draxlespanner",
        "Finewizzle",
        "Puddleblast",
        "Stormgauge",
        "Shinesprocket",
    ]


class GnomeFemaleNameGenerator(GnomeMaleNameGenerator):
    firstnames = [
        "Glinkeefonk",
        "Binfink",
        "Tolikink",
        "Katbrick",
        "Tiltinkle",
        "Tinkeeflonk",
        "Bonfinkle",
        "Tyntinkle",
        "Mittlefink",
        "Talmink",
    ]


class Gnome(Race):
    name = "Gnome"
    plural = "gnomes"

    male_hair_generator = GnomeMaleHairGenerator
    female_hair_generator = GnomeFemaleHairGenerator

    face_generator = GnomeFaceGenerator

    male_name_generator = GnomeMaleNameGenerator
    female_name_generator = GnomeFemaleNameGenerator
