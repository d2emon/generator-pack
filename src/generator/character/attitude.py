from generator import Generated, ListGenerator


class Attitude(Generated):
    def __init__(self):
        self.attitude = "A scar"
        self.attitude2 = "A scar"

    def __repr__(self):
        return "people tend to %s, while %s." % (
            self.attitude,
            self.attitude2,
        )


class AttitudeGenerator(ListGenerator):
    generated_class = Attitude
    attitudes = [
        "keep their distance",
        "flock towards him",
        "worship him",
        "befriend him",
        "assist him",
        "follow him",
        "welcome him",
        "welcome him with open arms",
        "invite him into their homes",
        "hit it off with him",
        "ask him for favors",
        "shower him with gifts",
        "subtly ignore him",
        "pretend to be his friend",
        "pretend to be his best friend",
        "lie about knowing him to brag",
        "brag about knowing him",
        "take pride in knowing him",
        "take pride in knowing him as a friend",
        "wish to get to know him better",
        "become his friend",
        "socialize with him",
        "try to get him to marry their off-spring",
        "buy him a drink",
        "salute him in the streets",
        "stay on his good side",
        "thank him for his service",
        "ask him to tell stories",
        "ask him about his adventures",
        "ask him about his latest victory",
        "share local gossip with him",
        "be curious about him",
        "treat him like family",
    ]
    attitudes2 = [
        "a feeling of anguish",
        "a feeling of arogance",
        "a feeling of coldness",
        "a feeling of comfort",
        "a feeling of delight",
        "a feeling of guilt",
        "a feeling of hospitality",
        "a feeling of indifference",
        "a feeling of joy",
        "a feeling of regret",
        "a feeling of remorse",
        "a feeling of sadness",
        "a feeling of shame",
        "his attitude",
        "his bravery",
        "his clumsiness",
        "his company",
        "his composure",
        "his decency",
        "his disposition",
        "his fortunate past",
        "his friendly demeanor",
        "his gentleness",
        "his good looks",
        "his good will",
        "his goodwill",
        "his hatred",
        "his humility",
        "his kindness",
        "his odd companions",
        "his odd friends",
        "his painful past",
        "his patience",
        "his perseverance",
        "his persistence",
        "his personality",
        "his presence",
        "his reputation",
        "his sense of comradery",
        "his sense of honor",
        "his sense of humor",
        "his sense of justice",
        "his sensitivity",
        "his suffering",
        "his sympathy",
        "his tenderness",
        "his unfortunate past",
        "his unusual alliances",
        "his unusual looks",
        "his warmth",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.attitude = cls.generate_value(cls.attitudes)
        generated.attitude2 = cls.generate_value(cls.attitudes2)
        return generated
