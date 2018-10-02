from generator.generator.generated import ListGenerated
from generator.generator.generator_data import ListData

from fixtures.other.birthday_wish import birthday_wish


class BirthdayWish(ListGenerated):
    data = {'value': ListData(birthday_wish)}
