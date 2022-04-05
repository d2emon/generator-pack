from factories.generator import Generated
from factories.list_factory import ListFactory

from genesys.fixtures.fixtures.other.birthday_wish import birthday_wish


class BirthdayWish(Generated):
    provider = ListFactory(birthday_wish)
