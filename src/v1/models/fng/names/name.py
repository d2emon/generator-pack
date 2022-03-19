from v3.models import Model


class Name(Model):
    """
    Name model
    """

    @classmethod
    def prepare(cls, name) -> str:
        """
        Prepare name

        :param name: Unprepared name
        :return: Prepared name
        """
        name = cls.check_swear(name)
        return name.title()
