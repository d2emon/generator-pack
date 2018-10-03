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


class Event:
    def __init__(self, year=0, title="<UNKNOWN>"):
        self.year = year
        self.title = title

    def __str__(self):
        return "{} years ago: {}\n".format(self.year, self.title)

    def __repr__(self):
        return str(self)


def prehistory():
    """
    Any event that occurred before recorded history. In most cases, this era is described in speculative terms,
    typically describing how the setting came to be peopled and serving as a precursory justification of the setting’s
    ancient period (see below). As a result, prehistory events may or may not have actually happened, but because
    they’re so broadly foundational and there is little evidence (or need) to dispute them, they are offered with the
    weight of scholarly truth or religious faith. Roll 1d4 events, each spaced 1d10x1000 years apart:

    :return:
    """
    count = random.randint(1, 4)
    years = (random.randint(1, 10) * 1000 for _ in range(count))
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
    for year in years:
        event = random.choice(events)
        yield Event(year, event())


def ancient():
    """
    These events occurred during the setting’s distant past, typically describing the rise (and possible fall) of an
    ancestral race or explaining the remnants of a now-extinct culture. Like prehistory, ancient events are offered
    with a fair amount of speculation. However, unlike prehistory, there is more evidence of ancient culture (in the
    form of monuments, burial mounds and tombs, lost scrolls, et al.) to inspire scholarly debate and varied
    interpretation. As a result, there is usually enough doubt surrounding ancient events to prevent taking them at
    face value. Roll 2d6 events, each spaced 1d10x100 years apart:

    *   Cataclysm (d6: 1-2 technology gone awry; 3 magic gone awry; 4 demonic intrusion; 5 natural disaster; 6 cosmic event)
    *   Rise of an empire
    *   Fall of an empire
    *   Mass migration into region (d6: 1-4 human tribe; 5 humanoids; 6 monsters)
    *   Mass exodus from region (d6: 1-2 human tribe; 3-4 humanoids; 5-6 monsters)
    *   Discovery of (d6: 1 advanced agriculture; 2 energy source; 3 industrial material; 4 advanced manufacturing; 5 precious metal; 6 unusual substance)
    *   Historical figure (d6: 1 sorcerer; 2 sage; 3 prophet; 4 inventor; 5 artist; 6 slave)
    *   War (d6: 1-2 successful defence against invaders; 3-4 successful conquest over foreign power; 5 defeat by invaders; 6 failed invasion)
    *   Empire flourishes through (d6: 1-2 territorial expansion; 3-4 golden age; 5-6 renaissance)
    *   Empire declines through (d6: 1-2 territorial reduction; 3-4 imperial decadence; 5 technically backward; 6 militarily inferior)
    *   Religion (d6: 1-4 new religion founded; 5-6 old religion driven out)
    *   Astrological event (d6: 1 comet; 2 star alignment; 3 planetary alignment; 4 new star appears; 5 solar flare; 6 conjunction)

    :return:
    """
    pass


def past():
    """
    These events occurred after the setting’s ancient period but before the last living generation. About two-thirds of
    these events should provide general support for the setting’s background, while the remaining third forms the
    foundation for present-day adventure hooks. Depending on the setting’s age, this period can span a really long
    time; I recommend rolling 4d6 events, each spaced 1d10x10 years apart, but add as many more as you feel are
    necessary to represent sufficiently the era’s duration:

    *   Discovery of (d6: 1 advanced agriculture; 2 energy source; 3 industrial material; 4 advanced manufacturing; 5 precious metal; 6 unusual substance)
    *   Historical figure (d6: 1 -2 sage; 3 inventor; 4 explorer; 5 artist; 6 advisor)
    *   War hero (d6: 1-2 brilliant general; 3 leader of elite unit; 4 master spy; 5 battlefield heroine; 6 average soldier)
    *   War (d6: 1 successful defence against invaders; 2-3 successful conquest over foreign power; 4 defeat by invaders; 5-6 failed invasion)
    *   Kingdom flourishes through (d6: 1-3 territorial expansion; 4-5 resource surplus; 6 defeat of enemy)
    *   Kingdom declines through (d6: 1-2 territorial reduction; 3-4 loss of trading partners; 5-6 source of major resource lost)
    *   Natural disaster (d6: 1: fire; 2: flood; 3: earthquake; 4 meteors; 5 volcanoes; 6 violent storms)
    *   Man-made disaster (d6: 1: fire; 2 flood; 3 famine; 4 plague; 5-6 pollution)
    *   Kingdom expands (d6: 1-3 through conquest; 4 through colonisation; 5-6 through diplomatic means)
    *   Religion (d6: 1 new religion founded; 2-3 progressive split from orthodoxy; 4-5 cult founded; 6 old religion driven out)
    *   Astrological event (d6: 1 comet; 2 meteor shower; 3-4 eclipse; 5 solar flare; 6 conjunction)
    *   Rise of a kingdom
    *   Fall of a kingdom
    *   Rebellion (d6: 1-4 successful; 5-6 failed) perpetrated by (d6: 1 military; 2 peasants; 3 colony; 4 anarchists; 5 slaves; 6 prisoners)
    *   Political system (d6: 1-2 challenged; 3 created; 4 reformed; 5 replaced; 6 dissolved)
    *   Cult (d6: 1-3 formed; 4-5 rooted out; 6 assumes power)
    *   Strong leader (d6: 1-2 reigns; 3 dies of natural causes; 4 assassinated; 5 canonised; 6 abdicates)
    *   Weak leader (d6: 1 reigns; 2 dies of natural causes; 3-4 assassinated; 5-6 forcibly deposed)
    *   Genocide of (d6: 1-3 domestic racial minority; 4-5 foreign group; 6 religious sect)
    *   Population shift (d6 1-2 to follow resources; 3 following discovery; 4 resulting from disaster; 5 due to oppressive laws; 6 resulting from warfare)

    :return:
    """
    pass


def modern():
    """
    These are events that have occurred within the lifespan of the last living generation; only those living under the
    setting’s rocks will not have some memory of these events, either as a participant, a live observer, or as a direct
    relation to same. Because people tend to have relatively short attention spans, and because the effects of these
    events may still be felt, these events have artificial prominence that the stuff of older histories do not. As a
    rule of thumb, each of these events should form the basis for a current adventure hook, either as stand-alone
    instance or as an extension of an event from a previous era. Roll 2d6 events, each spaced 1d10 years apart:

    *   War (d6: 1 successful defence against invaders; 2 successful conquest over foreign power; 3 defeat on foreign shores; 4 is fought diplomatically; 5 ongoing defence; 6 ongoing invasion)
    *   Disaster (d6: 1 fire; 2 flood; 3 famine; 4 disease; 5 earthquake; 6 violent weather)
    *   Kingdom expands (d6: 1-2 through conquest; 3-4 through colonisation; 5-6 through diplomatic means)
    *   Religion (d6: 1 progressive split from orthodoxy; 2 resurgence of orthodoxy; 3 forced underground; 4 acquires secular authority; 5 purge of the “unfaithful”; 6 absorption of associated cult)
    *   Astrological event (d6: 1 comet; 2-3 meteor shower; 4 eclipse; 5-6 conjunction)
    *   Scandal (d6: 1-2 religious head; 3-4 ruling family; 5 military leader; 6 high-level bureaucrat)
    *   Formation of a county (or some subdivision of a kingdom)
    *   Dissolution of a county (or some subdivision of a kingdom)
    *   Rebellion (d6: 1 successful; 2-4 ongoing; 5-6 failed) perpetrated by (d6: 1-2 peasants; 3-4 anarchists; 5 slaves; 6 prisoners)
    *   Political party (d6: 1-2 challenged; 3 created; 4 reformed; 5 replaced; 6 dissolved)
    *   Cult (d6: 1-2 formed; 3-4 forced underground; 5 rises to legitimacy; 6 rooted out)
    *   Leader (d6: 1 found insane; 2 scandalised; 3 heralds prosperity; 4 assassinated; 5 abdicates; 6 roots out injustice)
    *   Schism between (d6: 1 political contenders; 2-3 noble families; 4-5 religious factions; 6 guilds)
    *   Political reform (d6: 1-3 improves; 4-6 worsens) (d6: 1-2 tax rates; 3 minority rights; 4 laws of conscription; 5 slavery; 6 system of law)
    *   Major monster (d6: 1-2 population increases; 3-4 hunted down; 5 establishes wilderness foothold; 6 eradicated from setting)
    *   Commerce (d6: 1 tax increase; 2 raider activity rising; 3 economic boom; 4 recession; 5 trade route discovered; 6 guild unrest)
    *   Population (d6: 1-2 boom; 3 decline; 4-5 divided; 6 whispers revolt)
    *   Creation of advanced (d6: 1 food production; 2 manufacturing; 3 weaponry; 4 medicine; 5 defence; 6 transport/communication)
    *   Criminal activity (d6: 1-2 rises in urban areas; 3-4 plagues the countryside; 5 is ruthlessly quashed; 6 prompts new laws)
    *   Ethnic minority (d6: 1-2 seeks diplomatic sovereignty; 3 suffers persecution; 4 foments sedition; 5 afforded special legal status; 6 migrates out of area)

    :return:
    """
    pass


"""
Final Words
You’re free to use these tables in whatever way best supports your vision of the setting. Determine a number of events 
from each era, then connect them however you see fit. The idea is to let the table results inspire patterns that 
explain how the setting got to be the way it is today. Suggestions are always welcome, and if you create a timeline 
you’re proud of, please post it in the comments section.

"""