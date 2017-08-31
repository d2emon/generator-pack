from generator import Generated, ListGenerator


class Promise(Generated):
    def __init__(self):
        self.settlement = "village"
        self.promisetype = "protected"

    def __repr__(self):
        return "the %s they've %s for so long" % (
            self.settlement,
            self.promisetype,
        )


class PromiseGenerator(ListGenerator):
    generated_class = Promise
    settlements = [
        "village",
        "city",
        "lands",
        "people",
        "town",
        "families",
        "ships",
        "armies",
        "homes",
        "castle",
        "palace",
        "natives",
        "wildlife",
        "farms",
        "country",
        "haven",
        "mountains",
        "rivers",
        "river",
        "sea",
        "woods",
        "wastelands",
        "clan",
        "folk",
        "tribe",
        "ancestors",
        "children",
        "deserts",
        "mines",
        "spirits",
        "stronghold",
    ]
    promisetypes = [
        "protected",
        "sworn to protect",
        "come to love",
        "loved",
        "fought for",
        "bled for",
        "nearly died for",
        "looked after",
        "cared for",
        "defended",
        "safeguarded",
        "kept safe",
        "watched over",
        "stood guard for",
        "come to appreciate",
        "grown affactionate of",
        "become enchancted by",
        "worshipped",
        "befriended",
        "grieved with",
        "shown mercy on",
        "sought solace in",
        "felt at home at",
        "rarely felt at home at",
        "barely related to",
        "disassociated with",
        "felt disconnected from",
        "have been seperated from",
        "been seperated from",
        "been isolated from",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.settlement = cls.generate_value(cls.settlements)
        generated.promisetype = cls.generate_value(cls.promisetypes)
        return generated


class ElfPromiseGenerator(PromiseGenerator):
    settlements = [
        "elf",
    ]


class GoblinPromiseGenerator(PromiseGenerator):
    settlements = [
        "goblin",
    ]
