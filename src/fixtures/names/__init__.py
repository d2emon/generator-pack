from .en import en


class NamesData:
    def __init__(self, data=None):
        self._data = data or dict()

    def __getitem__(self, item):
        return self._data.get(item)


def load_lang(lang='en'):
    # if lang == 'en':
    #     return en
    return NamesData(en)


names_data = load_lang('en')
