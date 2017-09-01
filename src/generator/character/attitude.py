from generator import Generated, ListGenerator


class Attitude(Generated):
    def __init__(self):
        self.attitude = "A scar"
        self.attitude2 = "A scar"

    def __repr__(self):
        return "people tend to %s, while %s" % (
            self.attitude,
            self.attitude2,
        )


class AttitudeGenerator(ListGenerator):
    generated_class = Attitude
    attitudes = [
        "keep their distance",
        "flock towards {{him}}",
        "worship {{him}}",
        "befriend {{him}}",
        "assist {{him}}",
        "follow {{him}}",
        "welcome {{him}}",
        "welcome {{him}} with open arms",
        "invite {{him}} into their homes",
        "hit it off with {{him}}",
        "ask {{him}} for favors",
        "shower {{him}} with gifts",
        "subtly ignore {{him}}",
        "pretend to be {{his}} friend",
        "pretend to be {{his}} best friend",
        "lie about knowing {{him}} to brag",
        "brag about knowing {{him}}",
        "take pride in knowing {{him}}",
        "take pride in knowing {{him}} as a friend",
        "wish to get to know {{him}} better",
        "become {{his}} friend",
        "socialize with {{him}}",
        "try to get {{him}} to marry their off-spring",
        "buy {{him}} a drink",
        "salute {{him}} in the streets",
        "stay on {{his}} good side",
        "thank {{him}} for {{his}} service",
        "ask {{him}} to tell stories",
        "ask {{him}} about {{his}} adventures",
        "ask {{him}} about {{his}} latest victory",
        "share local gossip with {{him}}",
        "be curious about {{him}}",
        "treat {{him}} like family",
        # "hopelessly try to seduce her",
    ]
    attitudes2 = [
        "trying to subtlely stare",
        "secretly admiring {{him}}",
        "trying to hide from {{him}}",
        "trying to avoid {{him}}",
        "trying to please {{him}}",
        "secretly dispising {{him}}",
        "jealousy consumes them",
        "wishing they were more like {{him}}",
        "thinking of ways to become {{his}} friend",
        "wanting to fight along {{his}} side in battle",
        "hoping to one day follow in {{his}} footsteps",
        "secretly training to become more like {{him}}",
        "trying to subtly look more like {{him}}",
        "befriending {{his}} friends to get closer to {{him}}",
        "learning as much about {{him}} as possible",
        "commending {{him}} for {{his}} deeds",
        "hoping {{he}} will one day be their leader",
        "hoping their sons will grow up to be like {{him}}",
        "helping {{him}} out in any way they can",
        "awkwardly avoid talking about {{his}} past",
        "spreading rumors about {{him}} behind {{his}} back",
        "spreading stories about {{him}}",
        "making up bigger stories about {{him}}",
        "training with {{him}} whenever he's available",
        "treating {{him}} to a good meal when he's around",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.attitude = cls.generate_value(cls.attitudes)
        generated.attitude2 = cls.generate_value(cls.attitudes2)
        return generated
