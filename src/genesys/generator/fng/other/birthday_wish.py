from genesys.generator import Generated
from genesys.generator import ListProvider

from sample_data.fixtures.other import birthday_wish


class BirthdayWish(Generated):
    provider = ListProvider(birthday_wish)
