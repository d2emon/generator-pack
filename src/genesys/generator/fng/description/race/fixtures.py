from fixtures import race
from genesys.generator import StaticData, ListData


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

    horns = ListData(race.horns)
    covers = ListData(race.covers)


class MammalFixtures(RaceFixtures):
    pass


class AquaticFixtures(MammalFixtures):
    body1 = ListData(race.aquatic_tails)

    # tails = ListData(race.tails)
    arms = ListData(race.aquatic_arms)
    legs = ListData(race.aquatic_dorsals)

    covers = StaticData()
    horns = ListData(race.aquatic_horns)


class AmphibianFixtures(RaceFixtures):
    tails = ListData(race.amphibian_tails)

    covers = ListData(race.mucouses)


class ReptileFixtures(RaceFixtures):
    limbs = ListData(race.reptilian_arms)
    tails = ListData(race.reptilian_tails)

    covers = ListData(race.reptile_scales)


class FishFixtures(RaceFixtures):
    noses = ListData(race.fish_noses)
    ears = ListData(race.fish_ears)

    arms = ListData(race.fish_sides)
    legs = ListData(race.fish_dorsals)

    body1 = ListData(race.fish_tails)

    # tails = ListData(race.tails)

    covers = ListData(race.fish_scales)


class InvertebrateFixtures(RaceFixtures):
    arms = ListData(race.invertebrate_arms)
    legs = ListData(race.invertebrate_legs)
    tails = ListData(race.invertebrate_tails)


class BirdFixtures(RaceFixtures):
    mouths = ListData(race.beaks)
    noses = None
    ears = ListData(race.bird_ears)

    arms = ListData(race.bird_wings)
    legs = ListData(race.bird_legs)
    tails = ListData(race.bird_tails)

    horns = StaticData()
    # ears_generator = BirdEarsGenerator
    # mouth_generator = BeakGenerator
    # nose_generator = None
    covers = ListData(race.feathers)
