from .item import Item
from .portal import Portal
from .world import World
from .conditions import Conditions
from .summary import Summary


class Movement(Item):
    data = [
        "advance", "cautiously venture", "force", "go", "move", "pass", "progress", "push", "step", "stride", "travel",
        "venture", "walk"
    ]


class Distance(Item):
    data = [
        "In the distance", "Nearby", "In the far-off distance", "Close around you", "Around you", "All around",
        "All around you", "Not far into the distance", "Far away", "Fairly nearby", "Close to your proximity",
        "In the nearby proximity", "Far behind you", "Off to the side", "Far off to the right", "Far off to the left"
    ]


class Feel(Item):
    data = [
        "hear the sounds", "hear screams", "hear whistles and sounds", "hear songs and growls",
        "hear growls and grunts", "hear songs and shrieks", "feel the presence", "feel air vibrations",
        "smell what must be the scents", "smell the sweet scents", "smell the pungent odors", "smell traces ",
        "see the silhouettes", "see countless colors", "see parts", "vaguely see silhouettes", "see strange shapes",
        "see bits and pieces"
    ]


class Source(Item):
    data = [
        "creatures you've never seen before", "beings you could've only dreamed of",
        "creatures never before seen by anyone of your kind", "beings beyond any of your own world",
        "the most bizarre looking creatures", "the strangest creatures you could've imagined",
        "creatures not too different from the ones you know", "odd looking creatures to say the least",
        "the most peculiar beings you've ever encountered", "somehow somewhat familiar creatures",
        "eerily familiar beings", "creatures of a literally and figuratively different world",
        "creatures myths and legends are made of", "the type of creatures they write stories about",
        "creatures stranger even than those of legends of old",
        "creatures almost disappointingly similar to those you know", "creatures nobody could've ever imagined",
        "beings literally and figuratively beyond your world", "beings so strange you almost feel like you're dreaming",
        "beings you thought only existed in the minds of dreamers"
    ]


class Behavior(Item):
    data = [
        "While they seem docile enough", "Although they seem perfectly friendly",
        "While they seem curious and amicable", "Even though they seem harmless and curious",
        "While they show you little interest", "Despite barely giving you any attention",
        "Despite looking friendly and docile", "Even though they seem good natured",
        "While they appear to be docile and safe", "Even though they don't seem to be bothered by your presence",
        "They seem to have taken notice of your presence", "Some have noticed you, and their interest has peaked",
        "Some eye you up in a way that makes you uncomfortable", "They keep an eye on you in a predatory manner",
        "Some keep an eye on you, possibly with the intent to respond to whatever you do",
        "Not all the creatures seem content with your presence",
        "Instinctively, some creatures treat you with fear or ferocity", "Many of them keep their distance from you",
        "Some see you as a strange and thus hostile being", "There's definitely some hostility going on"
    ]


class Conclusion(Item):
    data = [
        "you realise it's probably best to keep your distance", "you keep your distance just to be safe",
        "you try to avoid getting too close", "better safe than sorry, so you keep a good distance",
        "you realise it's best not to get too close", "you keep your guard up just to be safe",
        "the cautious path would be the best one", "now would be the time to be very cautious",
        "the time to take risks is definitely not now", "you keep an eye out for them just to be sure",
        "you keep your distance and an eye on them", "you make sure they don't get any closer",
        "for now you simply keep your distance"
    ]


class Spot(Item):
    data = [
        "It's clear there are", "You can make out", "You manage to find traces of", "You see traces of",
        "There are traces of", "You easily spot", "It's obvious there are", "There are definitely",
        "You manage to spot", "You can see"
    ]


class CreatureType(Item):
    data = [
        "aquatic", "bulky", "chunky", "crawling", "enormous", "feathered", "fluffy", "flying", "gliding", "hairy",
        "huge", "lean", "muscular", "scaly", "sliding", "slithering", "small", "thin", "tiny"
    ]


class Actions(Item):
    data = [
        "You'll have to gather some supplies from the world around you", "You're glad you brought plenty of supplies",
        "With some rationing your supplies should last for a while",
        "This world seems to offer plenty to replenish most supplies",
        "You decide to make some final preparations around the portal entrance",
        "You decide to create a makeshift back-up camp around the portal",
        "You create an easy to spot landmark so you can find your way back more easily",
        "Strange as this world may be, you feel confident enough your supplies will last",
        "You can feel your excitement rising", "You make sure to check all your gear and supplies one last time",
        "With a final check of your supplies you ready yourself",
        "With everything sorted you look around one more time", "You know you've got everything sorted and prepared",
        "You look at the sky as if to try and figure out the time", "With your eyes on the horizon you move forward"
    ]


class Reason(Item):
    data = [
        "you're about to set upon the adventure of a lifetime", "discovery after discovery is waiting to be made",
        "a whole new world will unfold before your very eyes", "you're about to set foot upon uncharted terrain",
        "a realm of mysteries awaits you, for better or worse", "there's a world of wonders at your finger tips",
        "you set upon a world beyond your imagination", "you take your first steps into a world unknown",
        "you begin your life as a wanderer, explorer, and adventurer in this new world",
        "you begin a journey unlike any other"
    ]


class MindState(Item):
    data = [
        "some solid planning", "a few back-up plans", "a good amount of courage", "a great sense of adventure",
        "a curious mind", "some resourcefulness", "a bit of tenacity", "perseverance", "a little creative thinking",
        "a bag of tricks", "a good sense of direction", "an eye for details", "some scouting experience",
        "self-defense skills", "a cautious nature", "a bit of luck"
    ]


class Intro(Item):
    data = [
        "you should be able to explore this realm for all it has to offer",
        "you know you'll be able to make the most of this adventure", "you know this is a chance you won't let slip by",
        "you might actually end up being able to call this place home",
        "you know you can fulfill this opportunity with everything you have",
        "you'll be able to make the most of this most wonderful opportunity",
        "you know you can charter this uncharted land",
        "you'll be able to make the most of this once in a lifetime opportunity",
        "you'll be able to create the first foothold in this world",
        "you'll be able to register this world for those in your own"
    ]


def generate_realm():
    move = Movement.choice()
    portal = Portal.generate()
    world = World.choice()

    conditions = Conditions.choice()
    summary = Summary.choice()

    distance = Distance.choice()
    feel = Feel.choice()
    source = Source.choice()
    behavior = Behavior.choice()
    conclusion = Conclusion.choice()
    spot = Spot.choice()
    creature_types = CreatureType.choice_unique(3)

    actions = Actions.choice()
    reason = Reason.choice()
    mind_states = MindState.choice_unique(3)

    intro = Intro.choice()

    sent1 = "You {move} forward through {portal}.".format(
        move=move,
        portal=portal,
    )
    sent2 = "You're immediately met by {world}.".format(
        world=world,
    )
    sent3 = " ".join(world.description)
    sent4 = "{distance} you {feel} of {source}.".format(
        distance=distance,
        feel=feel,
        source=source,
    )
    sent5 = "{behavior}, {conclusion}.".format(
        behavior=behavior,
        conclusion=conclusion,
    )
    sent6 = "{actions} as {reason}.".format(
        actions=actions,
        reason=reason,
    )
    sent7 = "But, with {mind_states.0}, {mind_states.1}, and {mind_states.2}, {intro}.".format(
        mind_states=mind_states,
        intro=intro,
    )
    creatures = "{spot} {creature_types.0} creatures, {creature_types.1} creatures, and what you think might be {creature_types.2} creatures of some sort.".format(
        spot=spot,
        creature_types=creature_types,
    )

    name = " ".join([sent1, sent2, sent3])
    name2 = " ".join([conditions, summary])
    name3 = " ".join([sent4, sent5, creatures])
    name4 = " ".join([sent6, sent7])
    return "\n".join([
        name,
        name2,
        name3,
        name4,
    ])