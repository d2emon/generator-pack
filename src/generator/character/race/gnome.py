from generator.character.hair import HairGenerator
from generator.character.face import FaceGenerator
from generator.character.name import NameGenerator
from generator.character.race import Race


class GnomeHairGenerator(HairGenerator):
    colors = [
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
    hairtypes = [
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


class GnomeNameGenerator(NameGenerator):
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


class Gnome(Race):
    name = "Gnome"
    plural = "gnomes"

    hair_generator = GnomeHairGenerator
    face_generator = GnomeFaceGenerator
    name_generator = GnomeNameGenerator
