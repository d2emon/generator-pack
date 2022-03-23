from providers.list_provider import ListProvider
from factories.generator import Generated

from genesys.fixtures.fixtures.other.birthday_wish import birthday_wish


class BirthdayWish(Generated):
    provider = ListProvider(birthday_wish)
