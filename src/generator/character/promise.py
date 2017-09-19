from generator import Generated, ListGenerator


class Promise(Generated):
    def __init__(self):
        self.settlement = "village"
        self.promisetype = "protected"

    def __repr__(self):
        # "the " + names10[random10] + " they've " + names11[random11] + " for so long.";
        if "%s" in self.promisetype:
            return self.promisetype % (
                self.settlement,
            )
        return "the %s tey've %s for so long" % (
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

    def __init__(self, settlements=None, promisetypes=None):
        if settlements is not None:
            self.__class__.settlements = settlements
        if promisetypes is not None:
            self.__class__.promisetypes = promisetypes

    @classmethod
    def fill_generated(cls, generated):
        generated.settlement = cls.generate_value(cls.settlements)
        generated.promisetype = cls.generate_value(cls.promisetypes)
        return generated
