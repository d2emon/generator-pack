class Encounter:
    allowed_at = []
    encounter_class_description = ''

    def __init__(
        self,
        distance=None,
        is_surprised=False,
        is_surprising=False,
        description=None,
        *args,
        **kwargs,
    ):
        self.__description = description
        self.distance = distance
        self.is_surprised = is_surprised
        self.is_surprising = is_surprising

    @property
    def description(self):
        value = self.__description
        return value if value is not None else self.encounter_class_description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def text(self):
        text = [
            self.distance,
            self.description,
        ]

        if self.is_surprising:
            text.append("Партия застигнута врасплох")

        if self.is_surprised:
            text.append("Столкновение застигнуто врасплох")

        return '\n'.join(map(str, text))

    def __str__(self):
        return self.description
