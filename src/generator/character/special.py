from generator import Generated, ListGenerator


class SpecialSign(Generated):
    def __init__(self):
        self.signtype = "A scar"
        self.place_from = "stretching from just under the right eye"
        self.place_through = ", running across the nose"
        self.place_to = "and ending on his left cheek"
        self.memory = "a pleasant memory",
        self.origin = "a former life"

    def __repr__(self):
        return "%s %s %s %s leaves %s of %s." % (
            self.signtype,
            self.place_from,
            self.place_through,
            self.place_to,
            self.memory,
            self.origin
        )


class SpecialSignGenerator(ListGenerator):
    generated_class = SpecialSign
    signtypes = [
        "A scar",
        "Scars",
        "A sword left a mark",
        "A gunshot left a mark",
        "Fallen debry left a mark",
        "Fire has left a mark",
        "A birthmark",
        "An old tattoo",
        "A tattoo",
        "Tribal marks",
        "Several moles",
        "Freckles",
        "Smooth skin",
        "Soft skin",
        "Fair skin",
        "A beard",
        "A large beard",
        "Dark stubble",
        "A moustache",
        "A goatee",
        "A moustache and goatee",
    ]
    places_from = [
        "stretching from just under the right eye",
        "stretching from just under the left eye",
        "stretching from just under the right eyebrow",
        "stretching from just under the left eyebrow",
        "stretching from just under the right eye",
        "stretching from the top of the right cheek",
        "stretching from the top of the left cheek",
        "stretching from the bottom of the right cheek",
        "stretching from the bottom of the left cheek",
        "stretching from the bottom of the right cheekbone",
        "stretching from the bottom of the left cheekbone",
        "stretching from the right side of the forehead",
        "stretching from the left side of the forehead",
        "reaching from just under the right eye",
        "reaching from just under the left eye",
        "reaching from just under the right eyebrow",
        "reaching from just under the left eyebrow",
        "reaching from just under the right eye",
        "reaching from the top of the right cheek",
        "reaching from the top of the left cheek",
        "reaching from the bottom of the right cheek",
        "reaching from the bottom of the left cheek",
        "reaching from the bottom of the right cheekbone",
        "reaching from the bottom of the left cheekbone",
        "reaching from the right side of the forehead",
        "reaching from the left side of the forehead",
    ]
    places_through = [
        ", running across the nose",
        ", running towards the other eye",
        ", first running towards thin lips",
        ", first running towards his fairly big lips",
        ", running towards the right side of his lips",
        ", running towards the left side of his lips",
        ", running towards the tip of the nose",
        ", running towards his left nostril",
        ", running towards his right nostril",
        ", running towards his upper lip",
    ]
    places_to = [
        "and ending on his left cheek",
        "and ending on his left cheekbone",
        "and ending on his right cheek",
        "and ending on his right cheekbone",
        "and ending on his upper lip",
        "and ending on his chin",
        "and ending on his forehead",
        "and ending on his right nostril",
        "and ending on his left nostril",
        "and ending under his left eye",
        "and ending under his right eye",
        "and ending above his right eye",
        "and ending above his left eye",
    ]
    memories = [
        "a pleasant memory",
        "an aching memory",
        "a burning memory",
        "a stinging memory",
        "a tormenting memory",
        "an aching burden",
        "a stinging burden",
        "a tormenting burden",
        "a painful burden",
        "a lasting punishment",
        "a lasting burden",
        "an amusing memory",
        "a delightful memory",
        "a gracious memory",
        "a pleasurable memory",
        "a bittersweet memory",
        "a heartbreaking memory",
        "an agonizing memory",
        "a grievous memory",
        "a beautiful memory",
        "a satisfying memory",
        "a fascinating memory",
        "a captivating memory",
        "an intriguing memory",
        "a compelling memory",
    ]
    origins = [
        "a former life",
        "a great reputation",
        "a new life",
        "a reclaimed home",
        "an unusual alliance",
        "battles long forgotten",
        "battles past",
        "companionship",
        "deceased love",
        "deceased loved ones",
        "defended homes",
        "defended honor",
        "defended lands",
        "departed love",
        "departed loved ones",
        "famed glory",
        "forbidden adventures",
        "forbidden love",
        "former lives",
        "former love",
        "fortunate adventures",
        "heroic liberations",
        "hidden talents",
        "his adventurous love life",
        "his ex-love",
        "his former lover",
        "his fortunate destiny",
        "his fortunate past",
        "his fortunate survival",
        "his fortunate upbringing",
        "his love",
        "his luck in battles",
        "his luck in love",
        "his luck",
        "his reckless luck",
        "his unfortunate past",
        "his unfortunate upbringing",
        "innocence long lost",
        "lands long forgotten",
        "liberated love",
        "lost comrades",
        "lost friends",
        "lost honor",
        "lost love",
        "reclaimed honor",
        "reclaimed lands",
        "redeemed honor",
        "redeemed love",
        "redemption",
        "restored honor",
        "return to home",
        "true friendship",
        "unexpected friendship",
        "unfortunate adventures",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.signtype = cls.generate_value(cls.signtypes)
        generated.place_from = cls.generate_value(cls.places_from)
        generated.place_through = cls.generate_value(cls.places_through)
        generated.place_to = cls.generate_value(cls.places_to)
        generated.memory = cls.generate_value(cls.memories)
        generated.origin = cls.generate_value(cls.origins)
        return generated
