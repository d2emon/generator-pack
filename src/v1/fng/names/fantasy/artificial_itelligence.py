from v1.fng.genesys.name_factory import NameFactory
from v1.fng.genesys.name import Name
from v1.fng.genesys.data_block import load_data


nm1 = ["Achiever", "Admin", "Alive", "Alpha", "Analyst", "Angel", "Anima", "Animus", "Answer", "Apex", "Aspect",
       "Assist", "Aura", "Aurora", "Aware", "Base", "Beauty", "Bit", "Blossom", "Brain", "Butler", "Care", "Carer",
       "Center", "Central", "Cerebrum", "Cerebrus", "Cloud", "Code", "Codec", "Codex", "Colossus", "Companion",
       "Cosmic", "Cosmos", "Creator", "Cube", "Data", "Deus", "Different", "Dimension", "Discovery", "Dock", "Dream",
       "Echo", "Ego", "Energy", "Enigma", "Expert", "Face", "Familiar", "Father", "Feature", "Feel", "Figure", "Fluke",
       "Flux", "Form", "Frame", "Friend", "Fruit", "Gabriel", "Genesis", "Ghost", "Gift", "Golem", "Guard", "Guardian",
       "Guest", "Guide", "Harmony", "Heart", "Helix", "Hello", "Hex", "Holmes", "Hope", "Idea", "Image", "Impulse",
       "Intra", "Junior", "Life", "Light", "Logic", "Luck", "Lucky", "Lumos", "Machina", "Made", "Mage", "Master",
       "Matrix", "Max", "Memory", "Mind", "Mindful", "Mother", "Nemo", "Neo", "Nerve", "Omega", "Omni", "One", "Optix",
       "Oracle", "Original", "Patch", "Phoenix", "Pixel", "Present", "Prime", "Prism", "Reply", "Response", "Saint",
       "Sample", "Science", "Search", "Self", "Shell", "Shift", "Signal", "Solace", "Sole", "Soul", "Spark", "Spirit",
       "Sprite", "Stranger", "Student", "Switch", "Synapse", "Synergy", "System", "Tec", "Tech", "Test", "Thing",
       "Thinkerer", "Thought", "Tweak", "Unique", "Unit", "User", "Vessel", "Ware", "Watcher", "Whole", "Wish",
       "Witness", "Wonder", "Zen", "Zero"]


# Models


class ArtificialIntelligenceName(Name):
    @property
    def value(self):
        return f"{self.items[1]}"


# Factory


class ArtificialIntelligenceNameFactory(NameFactory):
    """Artificial Intelligence Name Factory"""

    description = """Artificial intelligence beings often have names related to robotics or electric concepts, these are
        also the names you'll find in this generator. However, logically speaking, artificial intelligence could have
        regular names just like humans do, or non-artificial intelligence. Obviously there are dozens upon dozens of
        real name generators to pick from on this site.
        The names in this generator cover themes like robotics, electronics, purposes, and in some cases identity as
        well."""
    default_blocks = load_data({
        1: nm1,
    })
    blocks_map = {
        1: 1,
    }
    name_class = ArtificialIntelligenceName
