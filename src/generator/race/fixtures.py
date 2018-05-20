from fixtures import race
from generator import StaticData, ListData


class RaceFixtures:
    eyes_count = ListData(race.eyes_count)
    eyesockets = ListData(race.eyesockets)
    mouths = ListData(race.mouths)
    noses = ListData(race.noses)
    ears = ListData(race.ears)

    body1 = ListData(race.arms)
    body2 = ListData(race.legs)
    body3 = ListData(race.tails)


class MammalFixtures(RaceFixtures):
    pass


class AquaticFixtures(MammalFixtures):
    body1 = ListData(race.aquatic_tails)
    body2 = ListData(race.aquatic_arms)
    body3 = ListData(race.aquatic_dorsals)


class AmphibianFixtures(RaceFixtures):
    body3 = ListData(race.amphibian_tails)


class ReptileFixtures(RaceFixtures):
    body1 = ListData(race.reptilian_arms)
    body2 = StaticData() # ListData([""])
    body3 = ListData(race.reptilian_tails)


class FishFixtures(RaceFixtures):
    noses = ListData(race.fish_noses)
    ears = ListData(race.fish_ears)

    body1 = ListData(race.fish_tails)
    body2 = ListData(race.fish_sides)
    body3 = ListData(race.fish_dorsals)


class InvertebrateFixtures(RaceFixtures):
    body1 = ListData(race.invertebrate_arms)
    body2 = ListData(race.invertebrate_legs)
    body3 = ListData(race.invertebrate_tails)


class BirdFixtures(RaceFixtures):
    mouths = ListData(race.beaks)
    noses = None
    ears = ListData(race.bird_ears)

    body1 = ListData(race.bird_wings)
    body2 = ListData(race.bird_legs)
    body3 = ListData(race.bird_tails)
