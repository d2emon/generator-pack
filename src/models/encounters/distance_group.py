from models.model import Model


class DistanceGroup(Model):
    value = Model.field_property('description')

    description = Model.field_property('description')
    dice = Model.field_property('dice')
    avoidable = Model.field_property('avoidable')
    allowed_at = Model.field_property('allowed_at')

    def __init__(
        self,
        description=None,
        dice=None,
        avoidable=True,
        allowed_at=None,
        *args,
        **kwargs,
    ):
        super().__init__(
            description=description,
            dice=dice,
            avoidable=avoidable,
            allowed_at=allowed_at or [],
            *args,
            **kwargs,
        )
    
    @property
    def field_names(self):
        yield "description"
        yield "dice"
        yield "avoidable"
        yield "allowed_at"
