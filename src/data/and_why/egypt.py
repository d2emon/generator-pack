from .genders import MALE, FEMALE
from .db import Database


def __inject_gender(gender, items):
    return [{ "gender": gender, **item } for item in items]


__FEMALE = __inject_gender(FEMALE, [
    {'type': 'Accessory', 'name': 'Чаша'},
    {'type': 'Accessory', 'name': 'Веер'},
    {'type': 'Headdress', 'name': 'Головной убор'},
    {'type': 'Headdress', 'name': 'Парик'},
    {'type': 'Collar', 'name': 'Воротник'},
    {'type': 'Collar', 'name': 'Воротник'},
    {'type': 'Shendyt', 'name': 'Схенти'},
    {'type': 'Shendyt', 'name': 'Схенти с юбкой'},
    {'type': 'Kalasiris', 'name': 'Калазирис'},
])


__MALE = __inject_gender(MALE, [
    {'type': 'Weapon', 'name': 'Копье'},
    {'type': 'Weapon', 'name': 'Секира'},
    {'type': 'Weapon', 'name': 'Бронзовый меч'},
    {'type': 'Weapon', 'name': 'Бронзовый кинжал'},
    {'type': 'Weapon', 'name': 'Меч'},
    {'type': 'Headdress', 'name': 'Шлем'},
    {'type': 'Headdress', 'name': 'Шлем'},
    {'type': 'Headdress', 'name': 'Парик'},
    {'type': 'Collar', 'name': 'Воротник'},
    {'type': 'Collar', 'name': 'Воротник'},
    {'type': 'Shendyt', 'name': 'Схенти'},
    {'type': 'Shield', 'name': 'Щит'},
])


class EgyptDatabase(Database):
    def by_gender(self, gender):
        return self.find(lambda item: item.get("gender") == gender)


EGYPT = EgyptDatabase(
    *__MALE,
    *__FEMALE,
)