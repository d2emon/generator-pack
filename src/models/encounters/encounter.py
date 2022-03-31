from models.model import Model


class Encounter(Model):
    allowed_at = []
    encounter_class_description = ''

    distance = Model.field_property('distance')
    is_surprised = Model.field_property('is_surprised', False)
    is_surprising = Model.field_property('is_surprising', False)

    def __init__(
        self,
        distance=None,
        is_surprised=False,
        is_surprising=False,
        *args,
        **kwargs,
    ):
        super().__init__(
            distance=distance,
            is_surprised=is_surprised,
            is_surprising=is_surprising,
            *args,
            **kwargs,
        )

    @property
    def field_names(self):
        yield "distance"
        yield "is_surprised"
        yield "is_surprising"
        yield "description"

    @property
    def description(self):
        value = self['description']
        return value if value is not None else self.encounter_class_description

    @description.setter
    def description(self, value):
        self['description'] = value

    def __str__(self):
        text = [
            self.distance,
            self.description,
        ]

        if self.is_surprising:
            text.append("Партия застигнута врасплох")

        if self.is_surprised:
            text.append("Столкновение застигнуто врасплох")

        return '\n'.join(map(str, text))
