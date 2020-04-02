class Rank:
    min_xp = 0
    title = ''


class Novice:
    min_xp = 0
    title = 'Новичок'


class Boiled:
    min_xp = 20
    title = 'Закаленный'


class Veteran:
    min_xp = 40
    title = 'Ветеран'


class Hero:
    min_xp = 60
    title = 'Героический'


class Legend:
    min_xp = 80
    title = 'Легендарный'


RANKS = [
    Novice,
    Boiled,
    Veteran,
    Hero,
    Legend,
]


def rank(xp):
    return next((r for r in RANKS[::-1] if r.min_xp < xp), Novice)
