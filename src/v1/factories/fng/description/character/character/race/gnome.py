from . import Race
from v1.factories.fng.description.character.hair import MaleHairFactory, FemaleHairFactory
from v1.factories.fng.description.character.face import FaceFactory
from v1.factories.fng.description.character.name import NameFactory


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


class GnomeMaleHairFactory(MaleHairFactory):
    colors = gnome_hair_colors
    hairtypes = gnome_hairtypes


class GnomeFemaleHairFactory(FemaleHairFactory):
    colors = gnome_hair_colors
    hairtypes = gnome_hairtypes


class GnomeFaceFactory(FaceFactory):
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


class GnomeMaleNameFactory(NameFactory):
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


class GnomeFemaleNameFactory(GnomeMaleNameFactory):
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

    male_hair_generator = GnomeMaleHairFactory
    female_hair_generator = GnomeFemaleHairFactory

    face_generator = GnomeFaceFactory

    male_name_generator = GnomeMaleNameFactory
    female_name_generator = GnomeFemaleNameFactory
