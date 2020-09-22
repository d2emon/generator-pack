from .campsite import BaseCampsiteFactory


class UnusualCampsiteFactory(BaseCampsiteFactory):
    @property
    def data(self):
        return [
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
