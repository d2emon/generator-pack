from fixtures import race
from generator import StaticData, ListData


class RaceFixtures:
    eyes_count = ListData(race.eyes_count)
    eyesockets = ListData(race.eyesockets)
    mouths = ListData(race.mouths)
    noses = ListData(race.noses)
    ears = ListData(race.ears)

    arms = ListData(race.arms)
    legs = ListData(race.legs)
    tails = ListData(race.tails)
    limbs = StaticData()
    wings = StaticData()

    body1 = StaticData()
    body2 = StaticData()
    body3 = StaticData()


class MammalFixtures(RaceFixtures):
    pass


class AquaticFixtures(MammalFixtures):
    body1 = ListData(race.aquatic_tails)
    body2 = ListData(race.aquatic_arms)
    body3 = ListData(race.aquatic_dorsals)

    # tails = ListData(race.tails)

class AmphibianFixtures(RaceFixtures):
    tails = ListData(race.amphibian_tails)


class ReptileFixtures(RaceFixtures):
    limbs = ListData(race.reptilian_arms)
    tails = ListData(race.reptilian_tails)


class FishFixtures(RaceFixtures):
    noses = ListData(race.fish_noses)
    ears = ListData(race.fish_ears)

    body1 = ListData(race.fish_tails)
    body2 = ListData(race.fish_sides)
    body3 = ListData(race.fish_dorsals)

    # tails = ListData(race.tails)


class InvertebrateFixtures(RaceFixtures):
    body1 = ListData(race.invertebrate_arms)

    legs = ListData(race.invertebrate_legs)
    tails = ListData(race.invertebrate_tails)


class BirdFixtures(RaceFixtures):
    mouths = ListData(race.beaks)
    noses = None
    ears = ListData(race.bird_ears)

    arms = StaticData()
    wings = ListData(race.bird_wings)
    legs = ListData(race.bird_legs)
    tails = ListData(race.bird_tails)
