import random
from .en import en
from .ru import ru


languages = {
    'ru': ru,
    'en': en,
}


class GeneratorData:
    def __init__(self, data):
        self._data = data or dict()

    def __getitem__(self, item):
        return self._data.get(item)

    def one(self, key):
        items = self[key] or []
        if len(items) < 1:
            return None
        return random.choice(items)


def load_lang(lang='en'):
    data = languages.get(lang, en)
    return GeneratorData(data)


generator_data = load_lang()
