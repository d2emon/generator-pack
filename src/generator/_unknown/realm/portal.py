from .item import Item


class Description(Item):
    data = [
        "alluring", "animated", "beckoning", "brilliant", "broad", "dark", "delicate", "eerie", "enticing", "faded",
        "faint", "familiar", "florid", "glistening", "grand", "grim", "hefty", "impressive", "light", "lively",
        "menacing", "narrow", "newly created", "ominous", "pleasing", "prismatic", "strange", "temporary", "tempting",
        "unfamiliar", "untried", "vibrant", "vigorous", "vivid", "weak"
    ]


class Placement(Item):
    data = [
        "hidden among the trees", "locked in a forgotten basement", "in this sacred temple",
        "in this desolate fortress", "in this secured room", "part of a greater altar",
        "that once looked like a regular door", "hidden behind a waterfall", "at the end of a long cave system",
        "at the top of a dormant volcano", "hidden in plain sight in an alley", "formed by two bended trees",
        "that looked like a small pond before", "at the top of a pyramid", "resembling a star gate",
        "resembling a campfire", "at the end of a hallway", "seemingly disguised as a cave entrance",
        "hidden high atop a mountain among a layer of clouds", "part of long forgotten ruins",
        "revealed only by fire", "revealed only during a full moon", "revealed only with the right elements",
        "previously locked behind intricate locks and traps", "hidden in plain sight in a public park"
    ]


class Portal:
    def __init__(self, description, placement):
        self.description = description
        self.placement = placement

    @classmethod
    def generate(cls):
        description = Description.choice()
        placement = Placement.choice()
        return cls(description, placement)

    def __str__(self):
        return "the {description} portal {placement}".format(
            description=self.description,
            placement=self.placement,
        )
