from generator.generator.generated import Generated
from generator.generator.data_provider import ListProvider


from fixtures.other.birthday_wish import birthday_wish


class BirthdayWish(Generated):
    provider = ListProvider(birthday_wish)
