from genesys.fixtures.fixtures import race
from factories.factory import Factory
from factories.list_factory import ListFactory


class RaceFixtures:
    eyes_count = ListFactory(race.eyes_count)
    eyesockets = ListFactory(race.eyesockets)
    mouths = ListFactory(race.mouths)
    noses = ListFactory(race.noses)
    ears = ListFactory(race.ears)

    arms = ListFactory(race.arms)
    legs = ListFactory(race.legs)
    tails = ListFactory(race.tails)
    limbs = Factory()
    wings = Factory()

    body1 = Factory()
    body2 = Factory()
    body3 = Factory()

    horns = ListFactory(race.horns)
    covers = ListFactory(race.covers)


class MammalFixtures(RaceFixtures):
    pass


class AquaticFixtures(MammalFixtures):
    body1 = ListFactory(race.aquatic_tails)

    # tails = ListFactory(race.tails)
    arms = ListFactory(race.aquatic_arms)
    legs = ListFactory(race.aquatic_dorsals)

    covers = Factory()
    horns = ListFactory(race.aquatic_horns)


class AmphibianFixtures(RaceFixtures):
    tails = ListFactory(race.amphibian_tails)

    covers = ListFactory(race.mucouses)


class ReptileFixtures(RaceFixtures):
    limbs = ListFactory(race.reptilian_arms)
    tails = ListFactory(race.reptilian_tails)

    covers = ListFactory(race.reptile_scales)


class FishFixtures(RaceFixtures):
    noses = ListFactory(race.fish_noses)
    ears = ListFactory(race.fish_ears)

    arms = ListFactory(race.fish_sides)
    legs = ListFactory(race.fish_dorsals)

    body1 = ListFactory(race.fish_tails)

    # tails = ListFactory(race.tails)

    covers = ListFactory(race.fish_scales)


class InvertebrateFixtures(RaceFixtures):
    arms = ListFactory(race.invertebrate_arms)
    legs = ListFactory(race.invertebrate_legs)
    tails = ListFactory(race.invertebrate_tails)


class BirdFixtures(RaceFixtures):
    mouths = ListFactory(race.beaks)
    noses = None
    ears = ListFactory(race.bird_ears)

    arms = ListFactory(race.bird_wings)
    legs = ListFactory(race.bird_legs)
    tails = ListFactory(race.bird_tails)

    horns = Factory()
    # ears_generator = BirdEarsGenerator
    # mouth_generator = BeakGenerator
    # nose_generator = None
    covers = ListFactory(race.feathers)
