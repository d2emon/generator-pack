import random


class Campsite:
    def __init__(self):
        self.description = ""
        self.resources = []
        self.encounters = []


class CampsiteGenerator:
    data = []

    @classmethod
    def generate(cls):
        campsite = Campsite()
        campsite.description = random.choice(cls.data)
        campsite.resources = cls.generate_resources()
        campsite.encounters = cls.generate_encounters()
        return campsite

    @classmethod
    def generate_resources(cls):
        """
        Next roll twice (once for each column) on Table 2 (When was the camp last
        used and what resources are available?)

        :return:
        """
        return []

    @classmethod
    def generate_encounters(cls):
        """
        Finally roll for occurrences as often as you'd like. Table 3 is split into 3a, 3b,
        3c, and 3d. Roll a d12 to pick the column to use (this spans the 4 sub-tables),
        then roll again to pick the row.

        :return:
        """
        return []


class SimpleCampsiteGenerator(CampsiteGenerator):
    data = [
        "None, but resources to build a simple lean - to( or similar) are nearby.",
        "A few standing stones to block  weather.",
        "Some brush set up against a large fallen log.",
        "The inside corner of a stone wall has brush stacked as a lean - to.",
        "Small  one - room cave.",
        "A well used fire pit.Bare spots are obvious places for tents.",
        "A damaged and turned over wagon can be used as an ad-hoc structure.",
        "A bridge across a small river / large stream or a dried riverbed protects from the wind and prevents a fire "
        "from being seen.",
        "A ruined watchtower.Only two stone walls remain.",
        "A group of travelers already set up, their wagons surround a fire.",
        "Abandoned log cabin, in reasonable condition.",
        "Small three-walled stone shrine to a travel god.",
    ]


class UnusualCampsiteGenerator(CampsiteGenerator):
    data = [
        "A piece of a giant creature's shell or wing has been set up as a lean-to.",
        "The ruins of a forgotten village. A couple structures are still sturdy.",
        "A shipwreck provides shelter. (Fallen airship? Was there a sea here? Some other magic?)",
        "Area of campsites maintained by low level druid, small donation requested.",
        "A magical doorway to a safe 20'x20' area of extra-dimensional space.",
        "Once a battleground, many damaged shields are used as a simple structure's roof.",
        "Pieces of an enormous fallen statue form a ring, blocking the weather.",
        "Abandoned farmhouse or cabin, moldy food still on the table.",
        "A 20' diameter hollowed out mushroom. It is still living.",
        "A large depression caused by a meteor strike many years ago.",
        "A huge hollowed out tree stump.",
        "A giant nest fallen to the ground.",
    ]


def generate_campsite(roll=None):
    if roll is None:
        roll = random.randrange(12)

    if roll < 11:
        generator = SimpleCampsiteGenerator
    else:
        generator = UnusualCampsiteGenerator

    return generator.generate()
