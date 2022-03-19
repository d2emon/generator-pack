from .factory import Factory


class TextFactory(Factory):
    """
    Generate text
    """

    def text(self):
        """
        Generate text for result

        :return:
        """
        raise NotImplementedError()

    def __call__(self, *args, **kwargs):
        """
        Generate result

        :param args: Build args
        :param kwargs: Build kwargs
        :return: Result
        """
        value = self.text()
        return str(value) if value else None
