from data.fixtures.fixtures.other.birthday_wish import birthday_wish
from factories.list_factory import ListFactory
from models.fng.names.name import Name


class BirthdayWish(Name):
    provider = ListFactory(birthday_wish)
