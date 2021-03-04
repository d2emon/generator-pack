from .race import Race


class Character:
    __templates = [
        '{} a {}. {} over {}',
        '{} {} {} {} leaves {} of {}.',
        'This is the face of {} {}, a true {} among {}. He stands {} others, despite his {} frame.',
        'There\'s something {} about him, perhaps it\'s {} or perhaps it\'s simply {}. '
        'But nonetheless, people tend to {}, while {}.',
    ]

    def __init__(self, *args, **kwargs):
        self.race = Race()
        self.mark = ''
        self.mark_from = ''
        self.mark_through = ''
        self.mark_to = ''
        self.memory_type = ''
        self.memory_of = ''
        self.first_name = ''
        self.last_name = ''
        self.random20 = ''
        self.random22 = ''
        self.random23 = ''
        self.random24 = ''
        self.random25 = ''
        self.random26 = ''
        self.random27 = ''
        self.random28 = ''

    @property
    def __head(self):
        return self.__templates[0].format(
            self.race.hair,
            self.race.face,
            self.race.eyes,
            self.race.promise,
        )

    @property
    def __name2(self):
        return self.__templates[1].format(
            self.mark,
            self.mark_from,
            self.mark_through,
            self.mark_to,
            self.memory_type,
            self.memory_of,
        )

    @property
    def __name3(self):
        return self.__templates[2].format(
            self.first_name,
            self.last_name,
            self.random20,
            self.race,

            self.random22,
            self.random23,
        )

    @property
    def __name4(self):
        return self.__templates[3].format(
            self.random24,
            self.random25,
            self.random26,

            self.random27,
            self.random28,
        )

    @property
    def description(self):
        return '\n'.join([
            self.__head,
            self.__name2,
            self.__name3,
            self.__name4,
        ])
