from providers import ListProvider
from factories.generator import Generated

from genesys.fixtures.fixtures.other import birthday_wish


class BirthdayWish(Generated):
    provider = ListProvider(birthday_wish)
