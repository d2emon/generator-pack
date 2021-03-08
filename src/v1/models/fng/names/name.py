from v1.models.fng.model import Model


class Name(Model):
    """
    Name model
    """

    @classmethod
    def test_swear(cls, name) -> str:
        """
        Check name for bad words

        :param name: Uncleaned name
        :return: Cleaned name
        """
        return name

    @classmethod
    def prepare(cls, name) -> str:
        """
        Prepare name

        :param name: Unprepared name
        :return: Prepared name
        """
        name = cls.test_swear(name)
        return name.title()

    def __repr__(self):
        return f"<Name: \"{self}\">"
