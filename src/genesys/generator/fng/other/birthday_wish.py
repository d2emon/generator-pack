from genesys.generator import Generated
from genesys.generator import ListProvider


from fixtures.other import birthday_wish


class BirthdayWish(Generated):
    provider = ListProvider(birthday_wish)
