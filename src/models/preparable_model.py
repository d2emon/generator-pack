from .model import Model


class PreparableModel(Model):
    """
    Model with prepare data
    """

    @classmethod
    def check_swear(cls, value) -> str:
        """
        Check name for bad words

        :param name: Uncleaned name
        :return: Cleaned name
        """
        return value

    @classmethod
    def prepare(cls, value) -> str:
        """
        Prepare model

        :param name: Unprepared model
        :return: Prepared model
        """
        return cls.check_swear(str(value))
        
    @property
    def value(self) -> str:
        """
        :return: Model as string
        """
        return self.prepare(self['value'])
