from generator.generator.generated import ListGenerated
from generator.generator.data_provider import ListProvider


from fixtures.other.birthday_wish import birthday_wish


class BirthdayWish(ListGenerated):
    provider = ListProvider(birthday_wish)
