from providers import ListProvider
from factories.generator import Generated

from sample_data.fixtures.other import birthday_wish


class BirthdayWish(Generated):
    provider = ListProvider(birthday_wish)
