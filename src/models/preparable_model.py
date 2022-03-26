from .model import Model


class PreparableModel(Model):
    """
    Model with prepare data
    """

    @classmethod
    def prepare(cls, name) -> str:
        """
        Prepare model

        :param name: Unprepared model
        :return: Prepared model
        """
        return str(name)

    @classmethod
    def check_swear(cls, name) -> str:
        """
        Check name for bad words

        :param name: Uncleaned name
        :return: Cleaned name
        """
        return name
        
    @property
    def value(self) -> str:
        """
        :return: Model as string
        """
        return self.prepare(self['value'])
