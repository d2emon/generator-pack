from ..model import Model


class Portal(Model):
    def __init__(self, **kwargs):
        super().__init__()
        self.contents = [
            kwargs.get('universe'),
        ]
