from factories.generator_factories import ListFactory
from models.generator_models.character.special import SpecialSign, Scar, Tattoo, TribalMark, Moles, Freckles, Beard


class SpecialSignFactory(ListFactory):
    generated_class = SpecialSign
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
        "{{his}} adventurous love life",
        "{{his}} ex-love",
        "{{his}} former lover",
        "{{his}} fortunate destiny",
        "{{his}} fortunate past",
        "{{his}} fortunate survival",
        "{{his}} fortunate upbringing",
        "{{his}} love",
        "{{his}} luck in battles",
        "{{his}} luck in love",
        "{{his}} luck",
        "{{his}} reckless luck",
        "{{his}} unfortunate past",
        "{{his}} unfortunate upbringing",
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


class ScarFactory(SpecialSignFactory):
    generated_class = Scar
    signtype = "A scar"
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
        ", first running towards {{his}} fairly big lips",
        ", running towards the right side of {{his}} lips",
        ", running towards the left side of {{his}} lips",
        ", running towards the tip of the nose",
        ", running towards {{his}} left nostril",
        ", running towards {{his}} right nostril",
        ", running towards {{his}} upper lip",
    ]
    places_to = [
        "and ending on {{his}} left cheek",
        "and ending on {{his}} left cheekbone",
        "and ending on {{his}} right cheek",
        "and ending on {{his}} right cheekbone",
        "and ending on {{his}} upper lip",
        "and ending on {{his}} chin",
        "and ending on {{his}} forehead",
        "and ending on {{his}} right nostril",
        "and ending on {{his}} left nostril",
        "and ending under {{his}} left eye",
        "and ending under {{his}} right eye",
        "and ending above {{his}} right eye",
        "and ending above {{his}} left eye",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.signtype = cls.signtype
        generated.place_from = cls.generate_value(cls.places_from)
        generated.place_through = cls.generate_value(cls.places_through)
        generated.place_to = cls.generate_value(cls.places_to)
        generated.memory = cls.generate_value(cls.memories)
        generated.origin = cls.generate_value(cls.origins)
        return generated


class TattooFactory(SpecialSignFactory):
    generated_class = Tattoo
    signtype = "A tattoo"
    forms = []
    visibilities = [
        "is almost hidden",
        "is displayed",
        "is subtly placed",
        "is prominently featured",
        "is proudly worn"
    ]
    placements = [
        "on the right side of {{his}} neck",
        "on the left side of {{his}} neck",
        "just below {{his}} right eye",
        "just below {{his}} left eye",
        "on the side of {{his}} right cheekbone",
        "on the side of {{his}} left cheekbone",
        "on the side of the left eye",
        "on the side of {{his}} right eye",
        "just above the side of {{his}} left eye",
        "just above the side of {{his}} right eye",
        "just above the right side of {{his}} right eyebrow",
        "just above the left side of {{his}} left eyebrow"
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.signtype = cls.signtype
        generated.form = cls.generate_value(cls.forms)
        generated.visibility = cls.generate_value(cls.visibilities)
        generated.placement = cls.generate_value(cls.placements)
        generated.memory = cls.generate_value(cls.memories)
        generated.origin = cls.generate_value(cls.origins)
        return generated


class MaleTattooFactory(TattooFactory):
    forms = [
        "resembling a shield",
        "resembling a sword",
        "resembling a skull",
        "resembling a flag",
        "resembling a tear",
        "of a small dragon",
        "of a small cross",
        "of a small star",
        "of a small eagle",
        "of a small swallow",
        "of a small lion",
        "of a small wolf",
        "of a small bear",
        "of a bear paw",
        "of a lion paw",
        "of an eagle claw",
        "of a talon",
        "of a dagger",
        "of a wolf paw",
        "of a shield",
        "of a sword",
        "of a skull",
        "of a flag",
        "of a tear",
        "resembling a small dragon",
        "resembling a small cross",
        "resembling a small star",
        "resembling a small eagle",
        "resembling a small swallow",
        "resembling a small lion",
        "resembling a small wolf",
        "resembling a small bear",
        "resembling a bear paw",
        "resembling a lion paw",
        "resembling an eagle claw",
        "resembling a talon",
        "resembling a dagger",
        "resembling a wolf paw",
    ]


class FemaleTattooFactory(TattooFactory):
    forms = [
        "resembling a rose",
        "resembling a petal",
        "of a heart",
        "resembling a shield",
        "resembling a sword",
        "resembling a skull",
        "resembling a flag",
        "resembling a tear",
        "of a small dragon",
        "of a small cross",
        "of a small star",
        "of a small eagle",
        "of a small swallow",
        "of a small lion",
        "of a small wolf",
        "of a small bear",
        "of a bear paw",
        "of a lion paw",
        "of an eagle claw",
        "of a talon",
        "of a dagger",
        "of a wolf paw",
        "of a shield",
        "of a sword",
        "of a skull",
        "of a flag",
        "of a tear",
        "resembling a small dragon",
        "resembling a small cross",
        "resembling a small star",
        "resembling a small eagle",
        "resembling a small swallow",
        "resembling a small lion",
        "resembling a small wolf",
        "resembling a small bear",
        "resembling a bear paw",
        "resembling a lion paw",
        "resembling an eagle claw",
        "resembling a talon",
        "resembling a dagger",
        "resembling a wolf paw",
    ]


class TribalMarkFactory(SpecialSignFactory):
    generated_class = TribalMark
    signtype = "Tribal marks"
    forms = [
        "in the form of 2 stripes running from above the eyes to the bottom of the cheeks",
        "in the form of 2 stripes on each side of the face, running from just above the eyes to the bottom of the cheeks",
        "in the form of 1 stripe under {{his}} right eye",
        "in the form of 1 stripe under {{his}} left eye",
        "in the form of 2 stripes under {{his}} right eye",
        "in the form of 2 stripes under {{his}} left eye",
        "in the form of 1 stripe under each eye",
        "in the form of 1 stripe under each eye",
        "in the form of 2 stripes under each eye",
        "in the form of 2 stripes under each eye",
        "in the form of a stripe above and below {{his}} right eye",
        "in the form of a stripe above and below {{his}} left eye",
        "in the form of a stripe above and below both {{his}} eyes",
        "in the form of 1 stripe above and 2 stripes below {{his}} right eye",
        "in the form of 1 stripe above and 2 stripes below {{his}} left eye",
        "in the form of 1 stripe above and 2 stripes below both {{his}} eyes",
        "in the form of a diagonal line across {{his}} right eye",
        "in the form of a diagonal line across {{his}} left eye",
        "resembling a lightning bolt under {{his}} right eye",
        "resembling a lightning bolt under {{his}} left eye",
        "resembling a horizontal lightning bolt under {{his}} right eye",
        "resembling a horizontal lightning bolt under {{his}} left eye",
        "resembling two large lightning bolts on each side of {{his}} face",
    ]
    meanings = [
        "marks {{his}} heritage",
        "marks {{his}} ancestry",
        "marks {{his}} skills in combat",
        "marks {{his}} rank",
        "marks {{his}} upbringing",
        "marks {{his}} legacy",
        "marks {{his}} birthright",
        "marks {{his}} heirship",
        "marks {{his}} descent",
        "marks {{his}} lineage",
        "marks {{his}} blood relation",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.signtype = cls.signtype
        generated.form = cls.generate_value(cls.forms)
        generated.meaning = cls.generate_value(cls.meanings)
        generated.memory = cls.generate_value(cls.memories)
        generated.origin = cls.generate_value(cls.origins)
        return generated


class MolesFactory(SpecialSignFactory):
    generated_class = Moles
    signtype = "Several moles"
    styles = [
        "charmingly",
        "gracefully",
        "beautifully",
        "elegantly",
        "seductively",
        "alluringly",
        "delightfully",
        "delicately",
        "graciously",
        "neatly",
        "oddly",
        "awkwardly",
        "grotesquely",
        "gracelessly",
        "unusually",
        "peculiarly",
    ]
    placements = [
        "on {{his}} left cheek and",
        "on {{his}} right cheek and",
        "across {{his}} whole face and",
        "across {{his}} forehead and",
        "around {{his}} nose and",
        "on {{his}} neck and",
    ]
    memories = [
        "a pleasant memory",
        "an aching memory",
        "a burning memory",
        "a stinging memory",
        "a tormenting memory",
        "a lasting burden",
        "an amusing memory",
        "a delightful memory",
        "a pleasurable memory",
        "a bittersweet memory",
        "a heartbreaking memory",
        "an agonizing memory",
        "a grievous memory",
        "a satisfying memory",
        "a fascinating memory",
        "a captivating memory",
        "an intriguing memory",
        "a compelling memory",
    ]
    origins = [
        "{{his}} past",
        "{{his}} upbringing",
        "{{his}} fortunate upbringing",
        "{{his}} former lovers",
        "{{his}} fortunate looks",
        "{{his}} fortunate survival",
        "{{his}} luck",
        "{{his}} luck in battles",
        "{{his}} luck in love",
        "{{his}} fortunate destiny",
        "{{his}} adventurous love life",
        "{{his}} reckless luck",
        "{{his}} fortunate adventures",
        "{{his}} unfortunate upbringing",
        "{{his}} unfortunate looks",
        "{{his}} lack of luck in love",
        "{{his}} unadventurous love life",
        "{{his}} unfortunate adventures",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.signtype = cls.signtype
        generated.style = cls.generate_value(cls.styles)
        generated.placement = cls.generate_value(cls.placements)
        generated.memory = cls.generate_value(cls.memories)
        generated.origin = cls.generate_value(cls.origins)
        return generated


class FrecklesFactory(MolesFactory):
    generated_class = Freckles
    signtype = "Freckles"
    styles = [
        "charmingly",
        "gracefully",
        "beautifully",
        "elegantly",
        "gorgeously",
        "handsomely",
        "seductively",
        "alluringly",
        "delightfully",
        "delicately",
        "graciously",
        "neatly",
    ]
    placements = [
        "around {{his}} cheeks and",
        "across {{his}} whole face and",
        "across {{his}} cheeks and",
        "across {{his}} cheeks and forehead and",
        "around {{his}} nose and cheekbones and",
    ]
    memories = [
        "a pleasant memory",
        "an amusing memory",
        "a delightful memory",
        "a gracious memory",
        "a pleasurable memory",
        "a bittersweet memory",
        "a heartbreaking memory",
        "a beautiful memory",
        "a satisfying memory",
        "a fascinating memory",
        "a captivating memory",
        "an intriguing memory",
        "a compelling memory",
    ]
    origins = [
        "{{his}} past",
        "{{his}} upbringing",
        "{{his}} fortunate upbringing",
        "{{his}} former lovers",
        "{{his}} fortunate looks",
        "{{his}} fortunate survival",
        "{{his}} luck",
        "{{his}} luck in battles",
        "{{his}} luck in love",
        "{{his}} fortunate destiny",
        "{{his}} adventurous love life",
        "{{his}} reckless luck",
        "{{his}} fortunate adventures",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.signtype = cls.signtype
        generated.style = cls.generate_value(cls.styles)
        generated.placement = cls.generate_value(cls.placements)
        generated.memory = cls.generate_value(cls.memories)
        generated.origin = cls.generate_value(cls.origins)
        return generated


class BeardFactory(SpecialSignFactory):
    generated_class = Beard
    signtype = "A beard"
    styles = [
        "charmingly",
        "gracefully",
        "beautifully",
        "elegantly",
        "gorgeously",
        "handsomely",
        "seductively",
        "alluringly",
        "delightfully",
        "graciously",
    ]
    placements = [
        "eyes and",
        "cheekbones and",
        "cheeks and",
        "mouth and",
        "hair and",
        "nose and",
        "nose and mouth and",
        "eyes and mouth and",
        "eyes and cheekbones and",
        "eyes and hair and",
        "hair and cheekbones and",
    ]
    memories = [
        "a pleasant memory",
        "an amusing memory",
        "a delightful memory",
        "a gracious memory",
        "a pleasurable memory",
        "a bittersweet memory",
        "a heartbreaking memory",
        "a beautiful memory",
        "a satisfying memory",
        "a fascinating memory",
        "a captivating memory",
        "an intriguing memory",
        "a compelling memory",
    ]
    origins = [
        "{{his}} past",
        "{{his}} upbringing",
        "{{his}} fortunate upbringing",
        "{{his}} former lovers",
        "{{his}} fortunate looks",
        "{{his}} fortunate survival",
        "{{his}} luck",
        "{{his}} luck in battles",
        "{{his}} luck in love",
        "{{his}} fortunate destiny",
        "{{his}} adventurous love life",
        "{{his}} reckless luck",
        "{{his}} fortunate adventures",
    ]

    @classmethod
    def fill_generated(cls, generated):
        generated.signtype = cls.signtype
        generated.style = cls.generate_value(cls.styles)
        generated.placement = cls.generate_value(cls.placements)
        generated.memory = cls.generate_value(cls.memories)
        generated.origin = cls.generate_value(cls.origins)
        return generated


class ScarsFactory(ScarFactory):
    signtype = "Scars"


class SwordMarkFactory(ScarFactory):
    signtype = "A sword left a mark"


class GunshotMarkFactory(ScarFactory):
    signtype = "A gunshot left a mark"


class DebryMarkFactory(ScarFactory):
    signtype = "Fallen debry left a mark"


class FireMarkFactory(ScarFactory):
    signtype = "Fire has left a mark"


class BirthmarkFactory(ScarFactory):
    signtype = "A birthmark"


class MaleOldTattooFactory(MaleTattooFactory):
    signtype = "An old tattoo"


class FemaleOldTattooFactory(FemaleTattooFactory):
    signtype = "An old tattoo"


class SmoothSkinFactory(BeardFactory):
    signtype = "Smooth skin"


class SoftSkinFactory(BeardFactory):
    signtype = "Soft skin"


class FairSkinFactory(BeardFactory):
    signtype = "Fair skin"


class LargeBeardFactory(BeardFactory):
    signtype = "A large beard"


class DarkStubbleFactory(BeardFactory):
    signtype = "Dark stubble"


class MoustacheFactory(BeardFactory):
    signtype = "A moustache"


class GoateeFactory(BeardFactory):
    signtype = "A goatee"


class MoustacheAndGoateeFactory(BeardFactory):
    signtype = "A moustache and goatee"
