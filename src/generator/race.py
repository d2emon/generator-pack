"""
var names1 = ["mammal","aquatic mammal","amphibian","reptile","fish","invertebrate","bird","mammal"];
var random1 = parseInt(Math.floor((Math.random() * names1.length)));
"""

"""
0   "mammal"
1   "aquatic mammal"
2   "amphibian"
3   "reptile"
4   "fish"
5   "invertebrate"
6   "bird"
7   "mammal"
"""
class Body:
    base_parts = [
        [],
        ["two arms and ","four arms and ","six arms and ","two arms and ","two arms and ","four arms and ","two arms and "],
        ["two legs, ","four legs, ","six legs, ","four legs, ","two legs, ","two legs, "],
        ["with a long, thin tail","with a long, thick tail","with a short, thin tail","with a short, thick tail","with remnants of what was once a tail","but they have no tail","with a long, strong and agile tail","with a short, strong tail","with a long, strong tail","with a short, muscular tail","with a long, muscular tail","with a long, weak tail","with a short, weak tail","with a long, useless tail","with a short, useless tail","with a short, stubby tail"],
    ]

    def __init__(self, parts1=None, parts2=None, parts3=None):
        self.parts = self.base_parts
        if parts1 is not None:
            self.parts[1] = parts1
        if parts2 is not None:
            self.parts[2] = parts2
        if parts3 is not None:
            self.parts[3] = parts3

    def __next__(self):
        return next(self.parts[1]), next(self.parts[2]), next(self.parts[3])

    def __str__(self):
        return "They have {}{}{}.".format(next(self))

horns = [
    "They also have two horns on their heads.",
    "They also have three horns on their heads.",
    "They also have four horns on their heads.",
    "They also have horns covering their face.",
    "They also have horns running across their backs.",
    "They also have small horns on their hands.",
    "They also have small horns on their hands, arms and legs.",
    "They also have two small horns on their elbows.",
    "They also have two horns on their heels.",
    "They also have small horns on their feet.",
    "They also have small horns on their hands and feet.",
    "They also have small horns across their chests.",
    "They also have small horns across their body.",
    "They also have small horns across their chests and backs.",
    "They also have one long horn on their head.",
    "",
    "",
    "",
    "",
    ""
]
aquatic_horns = [
    "They also have two horns on their heads.",
    "They also have three horns on their heads.",
    "They also have four horns on their heads.",
    "They also have horns running across their backs.",
    "They also have one long horn on their head.",
    "",
    "",
    "",
    "",
    ""
]
eyes_count = [2, 4, 6, 2, 4, 2]
eyesockets = [
    "deep",
    "narrowly",
    "buried",
    "far",
    "rooted",
    "well",
    "low",
    "high",
    "sunken",
    "lightly",
    "thightly",
    "graciously",
    "concealed",
    "delicately",
    "elegantly",
    "gracefully"
]
mouths = [
    "wide mouths",
    "small mouths",
    "long mouths",
    "huge mouths",
    "thin mouths",
    "narrow mouths",
    "enormous mouths"
]
noses = [
    " and huge noses",
    " and small noses",
    " and wide noses",
    " and long noses",
    " and enormous noses",
    " and thin noses",
    " and almost hidden noses",
    " and lack of a visible nose",
    " and tiny noses",
    " and narrow noses"
]
fish_noses = [
    " and small noses",
    " and wide noses",
    " and long noses",
    " and thin noses",
    " and almost hidden noses",
    " and lack of a visible nose",
    " and tiny noses",
    " and narrow noses",
]
beaks = [
    "long beaks",
    "sharp beaks",
    "thin beaks",
    "short beaks",
    "huge beaks",
    "enormous beaks",
    "wide beaks",
    "thin, sharp beaks",
    "long, sharp beaks",
    "long, pointy beaks",
    "short, pointy beaks",
    "huge, pointy beaks",
    "huge, sharp beaks",
    "short, sharp beaks",
    "thin, pointy beaks",
]
ears = [
    "almost invisible",
    "long and pointy",
    "small",
    "huge",
    "large",
    "long",
    "quite long",
    "a bit small",
    "wide and long",
    "long and narrow",
    "will hidden",
    "small and pointy",
    "wide and large",
    "long and hanging",
    "small and stubby"
]
fish_ears = [
    "almost invisible",
    "small",
    "will hidden",
    "small and pointy",
    "small and stubby"
]
bird_ears = [
    "almost invisible",
    "small",
    "will hidden",
    "small and pointy",
    "small and stubby",
    "hidden behind their feathers"
]
skins = [
    "very thick and rough.",
    "smooth and thin.",
    "thin, but strong.",
    "thin and fairly weak.",
    "very thick and very strong.",
    "very strong, but not very thick.",
    "course, thick and strong.",
    "smooth, yet strong.",
    "smooth, elastic and quite strong.",
    "elastic and strong."
]
covers = [
    "It's covered in thick fur.",
    "It's covered lightly in small hairs.",
    "It's covered lightly in long, coarse hairs.",
    "It's covered in thick, course fur.",
    "It's covered long, wavy hairs.",
    "It's covered short hairs.",
    "It's covered short, curly hairs.",
    "It's covered in nothing but a few hairs on their hands.",
    "It's covered in nothing but hair on their heads, arms and legs.",
    "It's covered in nothing, except for hair on their heads.",
    "It's covered in nothing, except for hairs on their heads, chests, arms and legs.",
    "It's covered in nothing but a few hairs on their heads.",
    "It's covered lightly in tiny hairs.",
    "It's covered in thick, short hairs.",
    "It's covered in soft, short hairs."
]
mucouses =[
    "It's covered in a thin layer of mucous.",
    "It's covered in a thick layer of mucous.",
    "It's covered in a very thin layer of mucous.",
    "It's covered in a very thick layer of mucous.",
    "It's covered lightly in mucous."
]
reptile_scales=[
    "It's covered in thin, coarse scales.",
    "It's covered in large, coarse scales.",
    "It's covered in large, smooth scales.",
    "It's covered in large, strong scales.",
    "It's covered in small, coarse scales.",
    "It's covered in small, smooth scales.",
    "It's covered in small, strong scales.",
    "It's covered in strong, hard scales.",
    "It's covered in thick, coarse scales.",
    "It's covered in thick, strong scales."
]
fish_scales=[
    "It's covered in thin, coarse scales.",
    "It's covered in large, coarse scales.",
    "It's covered in large, smooth scales.",
    "It's covered in large, strong scales.",
    "It's covered in small, coarse scales.",
    "It's covered in small, smooth scales.",
    "It's covered in small, strong scales.",
    "It's covered in strong, hard scales.",
    "It's covered in thick, coarse scales.",
    "It's covered in thick, strong scales."
]
feathers=[
    "It's covered in large feathers.",
    "It's covered in large, thin feathers.",
    "It's covered in large, wide feathers.",
    "It's covered in long, thin feathers.",
    "It's covered in long, wide feathers.",
    "It's covered in short, thin feathers.",
    "It's covered in short, wide feathers.",
    "It's covered in small feathers.",
    "It's covered in small, thin feathers.",
    "It's covered in small, wide feathers."
]
skin_colors = [
    [
        "black",
        "blue",
        "bronze",
        "brown",
        "gold",
        "grey",
        "orange",
        "pink",
        "purple",
        "red",
        "silver",
        "white",
        "yellow",
        "dark blue",
        "dark bronze",
        "dark brown",
        "dark gold",
        "dark grey",
        "dark orange",
        "dark pink",
        "dark purple",
        "dark red",
        "dark silver",
        "dark yellow",
        "light blue",
        "light bronze",
        "light brown",
        "light gold",
        "light grey",
        "light orange",
        "light pink",
        "light purple",
        "light red",
        "light silver",
        "light yellow"
    ],
    [
        ", black",
        ", blue",
        ", bronze",
        ", brown",
        ", gold",
        ", grey",
        ", orange",
        ", pink",
        ", purple",
        ", red",
        ", silver",
        ", white",
        ", yellow",
        ", dark blue",
        ", dark bronze",
        ", dark brown",
        ", dark gold",
        ", dark grey",
        ", dark orange",
        ", dark pink",
        ", dark purple",
        ", dark red",
        ", dark silver",
        ", dark yellow",
        ", light blue",
        ", light bronze",
        ", light brown",
        ", light gold",
        ", light grey",
        ", light orange",
        ", light pink",
        ", light purple",
        ", light red",
        ", light silver",
        ", light yellow",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ],
    [
        ", black",
        ", blue",
        ", bronze",
        ", brown",
        ", gold",
        ", grey",
        ", orange",
        ", pink",
        ", purple",
        ", red",
        ", silver",
        ", white",
        ", yellow",
        ", dark blue",
        ", dark bronze",
        ", dark brown",
        ", dark gold",
        ", dark grey",
        ", dark orange",
        ", dark pink",
        ", dark purple",
        ", dark red",
        ", dark silver",
        ", dark yellow",
        ", light blue",
        ", light bronze",
        ", light brown",
        ", light gold",
        ", light grey",
        ", light orange",
        ", light pink",
        ", light purple",
        ", light red",
        ", light silver",
        ", light yellow",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ],
    [
        " and black",
        " and blue",
        " and bronze",
        " and brown",
        " and gold",
        " and grey",
        " and orange",
        " and pink",
        " and purple",
        " and red",
        " and silver",
        " and white",
        " and yellow",
        " and dark blue",
        " and dark bronze",
        " and dark brown",
        " and dark gold",
        " and dark grey",
        " and dark orange",
        " and dark pink",
        " and dark purple",
        " and dark red",
        " and dark silver",
        " and dark yellow",
        " and light blue",
        " and light bronze",
        " and light brown",
        " and light gold",
        " and light grey",
        " and light orange",
        " and light pink",
        " and light purple",
        " and light red",
        " and light silver",
        " and light yellow"
    ],
]
agings = [
    "darker",
    "lighter",
    "dull",
    "dim",
    "pale",
    "faded"
]


def int2str(i):
    data = {
        2: 'two',
        4: 'four',
        6: 'six',
    }
    return data.get(i)


class Eyes(Generated):
    def __init__(self, **kwargs):
        self.count = kwargs.get('count', 2)
        self.sockets = kwargs.get('sockets', None)
        self.appearance = kwargs.get('appearance', None)
        self.quality = kwargs.get('quality', None)

    @property
    def count_str(self):
        return "{} eyes".format(int2str(self.count))

    def __str__(self):
        text = "They have {} which sit {} in their sockets and can often make them appear to be {}. Their eyesight is {}."
        return text.format(
            self.count_str,
            self.sockets,
            self.appearance,
            self.quality,
        )


class Ears(Generated):
    def __init__(self, **kwargs):
        self.ears = kwargs.get('ears', None)
        self.quality = kwargs.get('quality', None)

    def __str__(self):
        text = "Their ears are {} and their hearing is {}.".format(
            self.ears,
            self.quality,
        )


class Skin(Generated):
    def __init__(self, **kwargs):
        self.skin = kwargs.get('skin', None)
        self.skin_type = kwargs.get('skin_type', None)
        self.cover = kwargs.get('cover', None)
        self.colors = kwargs.get('colors', None)
        self.aging = kwargs.get('aging', None)

    @property
    def color(self):
        return "".join(self.colors)

    def __str__(self):
        text = "Their skin is {} {}\n"
        text += "{} colors are mostly {}, which tend to become {} as they age."
        return text.format(
            self.skin,
            self.cover,
            self.skin_type,
            self.color,
            self.aging,
        )


class EyesGenerator:
    count = DataList(eyes_count)
    eyesockets = DataList(eyesockets)

    def __next__(self, appearance, quality):
        return Eyes(
            count=next(self.count),
            sockets=next(self.eyesockets_data),
            appearance=appearance,
            quality=quality,
        )


class MouthGenerator:
    mouths = DataList(mouths)

    def __next__(self, appearance):
        return Mouth(next(self.mouths))


class NoseGenerator:
    noses = DataList(noses)

    def __next__(self, appearance):
        return Nose(next(self.noses))


class FishNoseGenerator(NoseGenerator):
    noses = DataList(fish_noses)


class BeakGenerator(BeakGenerator):
    noses = DataList(beaks)


class EarsGenerator:
    ears = DataList(ears)

    def __next__(self, quality):
        return Ears(
            ears=next(self.ears),
            quality=quality,
        )


class HornsGenerator:
    horns = DataList(horns)

    def __next__(self, quality):
        return Horns(next(self.horns))


class AquaticHornsGenerator(HornsGenerator):
    horns = DataList(aquatic_horns)


class SkinGenerator:
    skins = DataList(skins)
    covers = DataList(covers)
    colors = [DataList(color) for color in skin_colors]
    agings = DataList(agings)

    def __next__(self, skin="Their skin "):
        cover = None
        if self.covers is not None:
            cover = next(self.covers)

        return Skin(
            skin=skin
            skin_type=next(self.skins),
            cover=cover,
            colors=[next(color) for color in self.colors], # unique
            aging=next(self.agings),
        )


class AquaticSkinGenerator:
    covers = None


class AmphibianSkinGenerator:
    covers = DataList([""])
    # cover=["It's covered in a thin layer of mucous.","It's covered in a thick layer of mucous.","It's covered in a very thin layer of mucous.","It's covered in a very thick layer of mucous.","It's covered lightly in mucous."]


class ReptileSkinGenerator:
    covers = DataList([""])
    # cover=["It's covered in thin, coarse scales.","It's covered in large, coarse scales.","It's covered in large, smooth scales.","It's covered in large, strong scales.","It's covered in small, coarse scales.","It's covered in small, smooth scales.","It's covered in small, strong scales.","It's covered in strong, hard scales.","It's covered in thick, coarse scales.","It's covered in thick, strong scales."]


class FishSkinGenerator:
    covers = DataList([""])
    # cover=["It's covered in thin, coarse scales.","It's covered in large, coarse scales.","It's covered in large, smooth scales.","It's covered in large, strong scales.","It's covered in small, coarse scales.","It's covered in small, smooth scales.","It's covered in small, strong scales.","It's covered in strong, hard scales.","It's covered in thick, coarse scales.","It's covered in thick, strong scales."]


class BirdSkinGenerator:
    covers = DataList([""])
    # cover=["It's covered in large feathers.","It's covered in large, thin feathers.","It's covered in large, wide feathers.","It's covered in long, thin feathers.","It's covered in long, wide feathers.","It's covered in short, thin feathers.","It's covered in short, wide feathers.","It's covered in small feathers.","It's covered in small, thin feathers.","It's covered in small, wide feathers."]


class Race:
    def __init__(self, **kwargs):
        self.appearance = kwargs.get('appearance')
        self.horns = kwargs.get('horns')
        self.ears = kwargs.get('ears')
        self.eyes = kwargs.get('eyes')
        self.nose = kwargs.get('nose')
        self.mouth = kwargs.get('mouth')
        self.skin = kwargs.get('skin')

    @property
    def nose_mouth(self):
        nose_mouth = []
        if self.mouth is not None:
            nose_mouth.append(self.mouth)
        if self.nose is not None:
            nose_mouth.append(self.nose)
        return "".join(nose_mouth),

    def __str__(self):
        text = "Their {} often make these aliens appear to be {}, but looks can be deceiving."
        nose_mouth = text.format(
            self.nose_mouth,
            self.appearance,
        )

        text = "\n\n".join([
            "These aliens are a type of {title}. {body}",
            "{eyes}",
            "{nose_mouth}\n{ears} {horns}",
            "{skin}",
            "The males are usually {divercity.0} than their female counter part and their colors are {divercity_color}. The females, however, are usually {divercity.1}.",
        ])
        return text.format(
            title=self.title,
            body=self.body,
            eyes=self.eyes,
            nose_mouth=nose_mouth,
            ears=self.ears,
            horns=self.horns,
            skin=self.skin,
            divercity_0=self.divercity[0],
            divercity_1=self.divercity[1],
            divercity_color=self.divercity_color,
        )



class RaceGenerator:
    title = "mammal"
    skin = "Their skin "


    body = Body()

    horns_generator = HornsGenerator
    ears_generator = EarsGenerator
    eyes_generator = EyesGenerator
    nose_generator = NoseGenerator
    mouth_generator = MouthGenerator
    skin_generator = SkinGenerator

    appearance_data = ["friendly","angry","arrogant","reserved","serene","compased","distant","modest","restrained","cautious","gentle","withdrawn","annoyed","nervous","agitated","bold","excited","troubled","upset","formal","evil","trustworthy","untrustworthy","sly","honest","dishonest","slick","elusive","calculating","intelligent"]
    quality_data = ["excellent","fairly good","quite good","not the best","amazing","astonishing","a bit poor","great at distances","not too great at distances","impressive","average","not that great","among the best","almost among the best","perhaps the best of all species"]
    divercity_data = ["more arrogant","bigger","bossier","braver","bulkier","faster","friendlier","heavier","lazier","more adventurous","more confident","more cunning","more dependable","more emotional","more gracious","more helpful","more honorable","more humble","more impulsive","more independent","more obedient","more obnoxious","more optimistic","more self-centered","more self-reliant","more vulgar","smarter","sneakier","stronger","taller"],
    divercity_colors = ["more vibrant","less vibrant","more varied","less varied","darker","lighter"]


    def appearance(self):
        return nextUnique(self.appearance_data, self.appearance_data)

    def quality(self):
        return nextUnique(self.quality_data, self.quality_data)

    def divercity(self):
        return nextUnique(self.divercity_data, self.divercity_data)

    def divercity_color(self):
        return next(self.divercity_colors)

    def __next__(self):
        appearance = self.appearance()
        quality = self.quality()

        horns = None
        nose = None
        mouth = None
        if horns_generator is not None:
            horns = self.horns_generator.__next__()
        if nose_generator is not None:
            nose = self.nose_generator.__next__()
        if mouth_generator is not None:
            mouth = self.mouth_generator.__next__()

        return Race(
            appearance=appearance[1],
            horns=horns,
            ears=self.ears_generator.__next__(
                quality=quality[1]
            )
            eyes=self.eyes_generator.__next__(
                appearance=appearance[0],
                quality=quality[0]
            )
            nose=nose,
            mouth=mouth,
            skin=self.skin_generator.__next__(self.skin),
        )


class MammalRace(Race):
    title = "mammal"


class AquaticRace(Race):
    title = "aquatic mammal"

    horns_generator = AquaticHornsGenerator
    skin_generator = AquaticSkinGenerator

    body = Body(
        ["a huge, powerful tail and small anal fin, ","a huge, muscular tail and small anal fin, ","a large, muscular tail and small anal fin, ","a large, powerful tail and small anal fin, ","a short, muscular tail and small anal fin, ","a long, powerful tail and small anal fin, ","a short, powerful tail and small anal fin, ","a long, muscular tail and small anal fin, ","a huge, powerful tail and small anal fin, ","a huge, muscular tail and long anal fin, ","a large, muscular tail and long anal fin, ","a large, powerful tail and long anal fin, ","a short, muscular tail and long anal fin, ","a long, powerful tail and long anal fin, ","a short, powerful tail and long anal fin, ","a long, muscular tail and long anal fin, "],
        ["two arms and ","four arms and ","two strong side fins and ","four strong side fins and ","six strong side fins and ","two side fins and ","four side fins and ","six side fins and ","two large side fins and ","four large side fins and ","six large side fins and ","two powerful arms and ","four powerful arms and ","two powerful side fins and ","four powerful sidefins and ","two huge side fins and ","four huge side fins and "],
        ["a huge dorsal fin","a small dorsal fin","a thick, long dorsal fin","a thin, long dorsal fin","a wide, sail-like dorsal fin","a ribbon-like dorsal fin","a long, ribbon-like dorsal fin","a short, ribbon-like dorsal fin","a huge, sail-like dorsal fin","a short, strong dorsal fin","a long, strong dorsal fin","a short, pointy dorsal fin","a long, pointy dorsal fin","a long, streamlined dorsal fin","a short, streamlined dorsal fin"],
    )



class AmphibianRace(Race):
    title = "amphibian"

    skin_generator = AmphibianSkinGenerator

    body = Body(
        parts3 = ["but they have no tail","with a huge, powerful tail","with a long, muscular tail","with a long, powerful tail","with a long, strong and agile tail","with a long, strong tail","with a long, thick tail","with a long, thin tail","with a long, useless tail","with a long, weak tail","with a short, muscular tail","with a short, powerful tail","with a short, strong tail","with a short, stubby tail","with a short, thick tail","with a short, thin tail","with a short, useless tail","with a short, weak tail","with a thick, powerful tail","with remnants of what was once a tail"],
    )


class ReptileRace(Race):
    title = "reptile"
    skin = "Their scale "

    skin_generator = ReptileSkinGenerator

    body = Body(
        ["two arms and two legs, ","two arms and four legs, ","two arms and six legs, ","four arms and two legs, ","four arms and four legs, ","four arms and six legs, ","six arms and two legs, ","six arms and four legs, ","two arms, but no legs, like a snake with arms, ","four arms, but no legs, like a snake with arms, ","six arms, but no legs, like a snake with arms, "],
        [""],
        ["with a long, thin tail","with a long, thick tail","with a short, thin tail","with a short, thick tail","with remnants of what was once a tail","but they have no tail","with a long, strong and agile tail","with a short, strong tail","with a long, strong tail","with a short, muscular tail","with a long, muscular tail","with a long, weak tail","with a short, weak tail","with a long, useless tail","with a short, useless tail","with a short, stubby tail"],
    )


class FishRace(Race):
    title = "fish"
    skin = "Their scale "

    ears_generator = FishEarsGenerator
    nose_generator = FishNoseGenerator
    skin_generator = FishSkinGenerator

    body = Body(
        ["a huge, powerful tail and small anal fin, ","a huge, muscular tail and small anal fin, ","a large, muscular tail and small anal fin, ","a large, powerful tail and small anal fin, ","a short, muscular tail and small anal fin, ","a long, powerful tail and small anal fin, ","a short, powerful tail and small anal fin, ","a long, muscular tail and small anal fin, ","a huge, powerful tail and small anal fin, ","a huge, muscular tail and long anal fin, ","a large, muscular tail and long anal fin, ","a large, powerful tail and long anal fin, ","a short, muscular tail and long anal fin, ","a long, powerful tail and long anal fin, ","a short, powerful tail and long anal fin, ","a long, muscular tail and long anal fin, "],
        ["two strong side fins and ","four strong side fins and ","six strong side fins and ","two side fins and ","four side fins and ","six side fins and ","two large side fins and ","four large side fins and ","six large side fins and ","two powerful side fins and ","four powerful sidefins and ","two huge side fins and ","four huge side fins and "],
        ["a huge dorsal fin","a small dorsal fin","a thick, long dorsal fin","a thin, long dorsal fin","a wide, sail-like dorsal fin","a ribbon-like dorsal fin","a long, ribbon-like dorsal fin","a short, ribbon-like dorsal fin","a huge, sail-like dorsal fin","a short, strong dorsal fin","a long, strong dorsal fin","a short, pointy dorsal fin","a long, pointy dorsal fin","a long, streamlined dorsal fin","a short, streamlined dorsal fin"],
    )


class InvertebrateRace(Race):
    title = "invertebrate"

    body = Body(
        ["two arms and ","four arms and ","six arms and ","four winged arms and ","two winged arms and ","six winged arms and ","two clawed arms and ","four clawed arms and ","two wings, two arms and ","four wings, two arms and ","two wings, four arms and ","four wings, four arms and ","two wings, six arms and ","two wings, two clawed arms and ","two clawed arms, two normal arms and "],
        ["two legs, ","four legs, ","six legs, ","four legs, ","two legs, "],
        ["but they have no tail","with a huge, powerful tail","with a long, muscular tail","with a long, powerful tail","with a long, strong and agile tail","with a long, strong tail","with a long, thick tail","with a long, thin tail","with a long, useless tail","with a long, weak tail","with a short, muscular tail","with a short, powerful tail","with a short, strong tail","with a short, stubby tail","with a short, thick tail","with a short, thin tail","with a short, useless tail","with a short, weak tail","with a thick, powerful tail","with remnants of what was once a tail"],
    )


class BirdRace(Race):
    title = "bird"
    skin = "Their feather "

    horns_generator = None
    ears_generator = BirdEarsGenerator
    mouth_generator = BeakGenerator
    nose_generator = None
    skin_generator = BirdSkinGenerator

    body = Body(
        ["two huge wings and ","four huge wings and ","two huge, powerful wings and ","four huge, powerful wings and ","two huge and two smaller wings and ","two enormous wings and ","four enormous wings and ","two large and four smaller wings and ","four smaller wings and ","two smaller wings and "],
        ["two strong, clawed legs, ","two small, clawed legs, ","four strong, clawed legs, ","four small, clawed legs, ","two strong legs, ","four strong legs, ","two small legs, ","four small legs, ","two thin, long legs, ","two long, strong legs, "],
        ["with a huge tail","with a huge, wide tail","with a huge, powerful tail","with a long, powerful tail","with a long, elegant tail","with a short, elegant tail","with a short, powerful tail","with a wide, powerful tail","with a wide, elegant tail","with a short tail"],
    )




races = [
    MammalRace,
    AquaticRace,
    AmphibianRace,
    ReptileRace,
    FishRace,
    InvertebrateRace,
    BirdRace,
    MammalRace,
]
