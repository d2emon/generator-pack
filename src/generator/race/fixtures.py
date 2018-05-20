from fixtures import race
from generator import ListData


class RaceFixtures:
    eyes_count = ListData(race.eyes_count)
    eyesockets = ListData(race.eyesockets)
    mouths = ListData(race.mouths)
    noses = ListData(race.noses)
    ears = ListData(race.ears)


class FishFixtures(RaceFixtures):
    noses = ListData(race.fish_noses)
    ears = ListData(race.fish_ears)


class BirdFixtures(RaceFixtures):
    noses = ListData(race.beaks)
    ears = ListData(race.bird_ears)
