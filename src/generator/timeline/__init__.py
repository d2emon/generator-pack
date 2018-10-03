"""
There’s nothing like working on a project to remind you of the tools you don’t have. I’m putting the final touches on
the Swords of Telm supplement and finding that I need to fill in a few historical gaps. While I have a relatively
complete history in my head (meaning the setting’s history, not my head’s), I don’t mind seeking some polyhedral
guidance.

The tables below cover four eras of a setting’s history. Setting is a loose term—it can apply to a kingdom, a
geographic area, or maybe even an entire world—regardless, it’s up to you to define, based on the size of your
campaign and how you choose to interpret the results. The events you generate represent major turning points—things
that you’d expect to read about in the history scrolls. And, since events often seem to become less significant with
age, you’ll note that the number of these turning points decreases as one travels back along the setting’s timeline.
The implication is that the more distant the era, the more pivotal the events.
"""
import random
from dice import d


class Event:
    def __init__(self, year=0, title="<UNKNOWN>"):
        self.year = year
        self.title = title

    def __str__(self):
        return "{} years ago: {}\n".format(self.year, self.title)

    def __repr__(self):
        return str(self)


class Era:
    count_dice = (1, 4)
    years_dice = (1, 10)
    years_mod = 1
    events = []

    @classmethod
    def generate_count(cls):
        return d(*cls.count_dice)

    @classmethod
    def generate_years(cls):
        return (d(*cls.years_dice) * cls.years_mod for _ in range(cls.generate_count()))

    @classmethod
    def generate(cls):
        for year in cls.generate_years():
            event = random.choice(cls.events)
            yield Event(year, event())


class Prehistory(Era):
    """
    Any event that occurred before recorded history. In most cases, this era is described in speculative terms,
    typically describing how the setting came to be peopled and serving as a precursory justification of the setting’s
    ancient period (see below). As a result, prehistory events may or may not have actually happened, but because
    they’re so broadly foundational and there is little evidence (or need) to dispute them, they are offered with the
    weight of scholarly truth or religious faith. Roll 1d4 events, each spaced 1d10x1000 years apart:

    :return:
    """
    count_dice = (1, 4)
    years_dice = (1, 10)
    years_mod = 1000
    events = [
        lambda: "Divine cleansing via {}".format(random.choice((
            "flood",
            "earthquake",
            "eruption",
            "disease",
            "cosmic event",
            "magic energy"
        ))),
        lambda: "Rise of {}".format(random.choice((
            "human sub-race",
            "human sub-race",
            "humanoid race",
            "humanoid race",
            "monsters",
            "planar beings"
        ))),
        lambda: "Decline of {}".format(random.choice((
            "human sub-race",
            "humanoid race",
            "humanoid race",
            "monsters",
            "monsters",
            "planar beings"
        ))),
        lambda: "Arrival of {}".format(random.choice((
            "new gods",
            "planar beings",
            "planar beings",
            "human tribe",
            "humanoid tribe",
            "extraterrestrials"
        ))),
        lambda: "Disappearance of {}".format(random.choice((
            "old gods",
            "old gods",
            "planar beings",
            "planar beings",
            "monster population",
            "powerful mortal race"
        ))),
        lambda: "Mortals attain knowledge of {}".format(random.choice((
            "writing",
            "basic technology",
            "basic technology",
            "divine order",
            "advanced technology",
            "psionics"
        ))),
        lambda: "Mortals punished for {}".format(random.choice((
            "excessive pride",
            "decadence",
            "worshiping false gods",
            "worshiping evil gods",
            "ignoring the gods",
            "succumbing to base urges"
        ))),
        lambda: "Mortals threatened by {}".format(random.choice((
            "planar beings",
            "rampaging monsters",
            "rampaging monsters",
            "rampant magic energy",
            "uncontrollable technology",
            "superior species"
        ))),
    ]


class Ancient(Era):
    """
    These events occurred during the setting’s distant past, typically describing the rise (and possible fall) of an
    ancestral race or explaining the remnants of a now-extinct culture. Like prehistory, ancient events are offered
    with a fair amount of speculation. However, unlike prehistory, there is more evidence of ancient culture (in the
    form of monuments, burial mounds and tombs, lost scrolls, et al.) to inspire scholarly debate and varied
    interpretation. As a result, there is usually enough doubt surrounding ancient events to prevent taking them at
    face value. Roll 2d6 events, each spaced 1d10x100 years apart:

    :return:
    """
    count_dice = (2, 6)
    years_dice = (1, 10)
    years_mod = 100
    events = [
        lambda: "Cataclysm ({})".format(random.choice((
            "technology gone awry",
            "technology gone awry",
            "magic gone awry",
            "demonic intrusion",
            "natural disaster",
            "cosmic event"
        ))),
        lambda: "Rise of an empire",
        lambda: "Fall of an empire",
        lambda: "Mass migration into region ({})".format(random.choice((
            "human tribe",
            "human tribe",
            "human tribe",
            "human tribe",
            "humanoids",
            "monsters"
        ))),
        lambda: "Mass exodus from region ({})".format(random.choice((
            "human tribe",
            "human tribe",
            "humanoids",
            "humanoids",
            "monsters",
            "monsters"
        ))),
        lambda: "Discovery of ({})".format(random.choice((
            "advanced agriculture",
            "energy source",
            "industrial material",
            "advanced manufacturing",
            "precious metal",
            "unusual substance",
        ))),
        lambda: "Historical figure ({})".format(random.choice((
            "sorcerer",
            "sage",
            "prophet",
            "inventor",
            "artist",
            "slave",
        ))),
        lambda: "War ({})".format(random.choice((
            "successful defence against invaders",
            "successful defence against invaders",
            "successful conquest over foreign power",
            "successful conquest over foreign power",
            "defeat by invaders",
            "failed invasion",
        ))),
        lambda: "Empire flourishes through ({})".format(random.choice((
            "territorial expansion",
            "territorial expansion",
            "golden age",
            "golden age",
            "renaissance",
            "renaissance",
        ))),
        lambda: "Empire declines through ({})".format(random.choice((
            "territorial reduction",
            "territorial reduction",
            "imperial decadence",
            "imperial decadence",
            "technically backward",
            "militarily inferior",
        ))),
        lambda: "Religion ({})".format(random.choice((
            "new religion founded",
            "new religion founded",
            "new religion founded",
            "new religion founded",
            "old religion driven out",
            "old religion driven out",
        ))),
        lambda: "Astrological event ({})".format(random.choice((
            "comet",
            "star alignment",
            "planetary alignment",
            "new star appears",
            "solar flare",
            "conjunction",
        ))),
    ]


class Past(Era):
    """
    These events occurred after the setting’s ancient period but before the last living generation. About two-thirds of
    these events should provide general support for the setting’s background, while the remaining third forms the
    foundation for present-day adventure hooks. Depending on the setting’s age, this period can span a really long
    time; I recommend rolling 4d6 events, each spaced 1d10x10 years apart, but add as many more as you feel are
    necessary to represent sufficiently the era’s duration:

    :return:
    """
    count_dice = (4, 6)
    years_dice = (1, 10)
    years_mod = 10
    events = [
        lambda: "Discovery of {}".format(random.choice((
            "advanced agriculture",
            "energy source",
            "industrial material",
            "advanced manufacturing",
            "precious metal",
            "unusual substance",
        ))),
        lambda: "Historical figure ({})".format(random.choice((
            "sage",
            "sage",
            "inventor",
            "explorer",
            "artist",
            "advisor",
        ))),
        lambda: "War hero ({})".format(random.choice((
            "brilliant general",
            "brilliant general",
            "leader of elite unit",
            "master spy",
            "battlefield heroine",
            "average soldier",
        ))),
        lambda: "War ({})".format(random.choice((
            "successful defence against invaders",
            "successful conquest over foreign power",
            "successful conquest over foreign power",
            "defeat by invaders",
            "failed invasion",
            "failed invasion",
        ))),
        lambda: "Kingdom flourishes through ({})".format(random.choice((
            "territorial expansion",
            "territorial expansion",
            "territorial expansion",
            "resource surplus",
            "resource surplus",
            "defeat of enemy",
        ))),
        lambda: "Kingdom declines through {}".format(random.choice((
            "territorial reduction",
            "territorial reduction",
            "loss of trading partners",
            "loss of trading partners",
            "source of major resource lost",
            "source of major resource lost",
        ))),
        lambda: "Natural disaster ({})".format(random.choice((
            "fire",
            "flood",
            "earthquake",
            "meteors",
            "volcanoes",
            "violent storms"
        ))),
        lambda: "Man-made disaster ({})".format(random.choice((
            "fire",
            "flood",
            "famine",
            "plague",
            "pollution",
            "pollution"
        ))),
        lambda: "Kingdom expands {}".format(random.choice((
            "through conquest",
            "through conquest",
            "through colonisation",
            "through colonisation",
            "through diplomatic means",
            "through diplomatic means",
        ))),
        lambda: "Religion ({})".format(random.choice((
            "new religion founded",
            "progressive split from orthodoxy",
            "progressive split from orthodoxy",
            "cult founded",
            "cult founded",
            "old religion driven out",
        ))),
        lambda: "Astrological event ({})".format(random.choice((
            "comet",
            "meteor shower",
            "eclipse",
            "eclipse",
            "solar flare",
            "conjunction",
        ))),
        lambda: "Rise of a kingdom",
        lambda: "Fall of a kingdom",
        lambda: "Rebellion ({}) perpetrated by {}".format(
            random.choice((
                "successful",
                "successful",
                "successful",
                "successful",
                "failed",
                "failed",
            )),
            random.choice((
                "military",
                "peasants",
                "colony",
                "anarchists",
                "slaves",
                "prisoners",
            )),
        ),
        lambda: "Political system {}".format(random.choice((
            "challenged",
            "challenged",
            "created",
            "reformed",
            "replaced",
            "dissolved",
        ))),
        lambda: "Cult {}".format(random.choice((
            "formed",
            "formed",
            "formed",
            "rooted out",
            "rooted out",
            "assumes power",
        ))),
        lambda: "Strong leader {}".format(random.choice((
            "reigns",
            "reigns",
            "dies of natural causes",
            "assassinated",
            "canonised",
            "abdicates",
        ))),
        lambda: "Weak leader {}".format(random.choice((
            "reigns",
            "dies of natural causes",
            "assassinated",
            "assassinated",
            "forcibly deposed",
            "forcibly deposed",
        ))),
        lambda: "Genocide of {}".format(random.choice((
            "domestic racial minority",
            "domestic racial minority",
            "domestic racial minority",
            "foreign group",
            "foreign group",
            "religious sect",
        ))),
        lambda: "Population shift {}".format(random.choice((
            "to follow resources",
            "to follow resources",
            "following discovery",
            "resulting from disaster",
            "due to oppressive laws",
            "resulting from warfare",
        ))),
    ]


class Modern(Era):
    """
    These are events that have occurred within the lifespan of the last living generation; only those living under the
    setting’s rocks will not have some memory of these events, either as a participant, a live observer, or as a direct
    relation to same. Because people tend to have relatively short attention spans, and because the effects of these
    events may still be felt, these events have artificial prominence that the stuff of older histories do not. As a
    rule of thumb, each of these events should form the basis for a current adventure hook, either as stand-alone
    instance or as an extension of an event from a previous era. Roll 2d6 events, each spaced 1d10 years apart:

    :return:
    """
    count_dice = (2, 6)
    years_dice = (1, 10)
    years_mod = 1
    events = [
        lambda: "War ({})".format(random.choice((
            "successful defence against invaders",
            "successful conquest over foreign power",
            "defeat on foreign shores",
            "is fought diplomatically",
            "ongoing defence",
            "ongoing invasion",
        ))),
        lambda: "Disaster ({})".format(random.choice((
            "fire",
            "flood",
            "famine",
            "disease",
            "earthquake",
            "violent weather"
        ))),
        lambda: "Kingdom expands {}".format(random.choice((
            "through conquest",
            "through conquest",
            "through colonisation",
            "through colonisation",
            "through diplomatic means",
            "through diplomatic means",
        ))),
        lambda: "Religion ({})".format(random.choice((
            "progressive split from orthodoxy",
            "resurgence of orthodoxy",
            "forced underground",
            "acquires secular authority",
            "purge of the “unfaithful”",
            "absorption of associated cult",
        ))),
        lambda: "Astrological event ({})".format(random.choice((
            "comet",
            "meteor shower",
            "meteor shower",
            "eclipse",
            "conjunction",
            "conjunction",
        ))),
        lambda: "Scandal ({})".format(random.choice((
            "religious head",
            "religious head",
            "ruling family",
            "ruling family",
            "military leader",
            "high-level bureaucrat",
        ))),
        lambda: "Formation of a county (or some subdivision of a kingdom)",
        lambda: "Dissolution of a county (or some subdivision of a kingdom)",
        lambda: "Rebellion ({}) perpetrated by {}".format(
            random.choice((
                "successful",
                "ongoing",
                "ongoing",
                "ongoing",
                "failed",
                "failed",
            )),
            random.choice((
                "peasants",
                "peasants",
                "anarchists",
                "anarchists",
                "slaves",
                "prisoners",
            )),
        ),
        lambda: "Political party {}".format(random.choice((
            "challenged",
            "challenged",
            "created",
            "reformed",
            "replaced",
            "dissolved",
        ))),
        lambda: "Cult {}".format(random.choice((
            "formed",
            "formed",
            "forced underground",
            "forced underground",
            "rises to legitimacy",
            "rooted out",
        ))),
        lambda: "Leader {}".format(random.choice((
            "found insane",
            "scandalised",
            "heralds prosperity",
            "assassinated",
            "abdicates",
            "roots out injustice",
        ))),
        lambda: "Schism between {}".format(random.choice((
            "political contenders",
            "noble families",
            "noble families",
            "religious factions",
            "religious factions",
            "guilds",
        ))),
        lambda: "Political reform {} {}".format(
            random.choice((
                "improves",
                "improves",
                "improves",
                "worsens",
                "worsens",
                "worsens",
            )),
            random.choice((
                "tax rates",
                "tax rates",
                "minority rights",
                "laws of conscription",
                "slavery",
                "system of law",
            )),
        ),
        lambda: "Major monster {}".format(random.choice((
            "population increases",
            "population increases",
            "hunted down",
            "hunted down",
            "establishes wilderness foothold",
            "eradicated from setting",
        ))),
        lambda: "Commerce {}".format(random.choice((
            "tax increase",
            "raider activity rising",
            "economic boom",
            "recession",
            "trade route discovered",
            "guild unrest",
        ))),
        lambda: "Population {}".format(random.choice((
            "boom",
            "boom",
            "decline",
            "divided",
            "divided",
            "whispers revolt",
        ))),
        lambda: "Creation of advanced {}".format(random.choice((
            "food production",
            "manufacturing",
            "weaponry",
            "medicine",
            "defence",
            "transport/communication",
        ))),
        lambda: "Criminal activity {}".format(random.choice((
            "rises in urban areas",
            "rises in urban areas",
            "plagues the countryside",
            "plagues the countryside",
            "is ruthlessly quashed",
            "prompts new laws",
        ))),
        lambda: "Ethnic minority {}".format(random.choice((
            "seeks diplomatic sovereignty",
            "seeks diplomatic sovereignty",
            "suffers persecution",
            "foments sedition",
            "afforded special legal status",
            "migrates out of area",
        ))),
    ]


"""
Final Words
You’re free to use these tables in whatever way best supports your vision of the setting. Determine a number of events 
from each era, then connect them however you see fit. The idea is to let the table results inspire patterns that 
explain how the setting got to be the way it is today. Suggestions are always welcome, and if you create a timeline 
you’re proud of, please post it in the comments section.

"""