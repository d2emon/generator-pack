from models.models import Model


class Factory:
    class DataProvider:
        default = ''
        text_format = '{}'

        def __iter__(self):
            return self

        def __next__(self):
            raise NotImplementedError()

        def value(self):
            return self.text_format.format(next(self))

    model_class = Model

    @classmethod
    def model(cls, *args, **kwargs):
        return cls.model_class(
            value=cls.DataProvider().value(),
            # *args,
            **kwargs,
        )
