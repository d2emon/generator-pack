from factories.generator import Generated
from factories.generator import ListProvider

from sample_data.fixtures.other import birthday_wish


class BirthdayWish(Generated):
    provider = ListProvider(birthday_wish)
