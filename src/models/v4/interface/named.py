class NamedModelInterface:
    @property
    def name(self):
        """
        Get next name from factory.name_factory

        :return: Model name
        """
        raise NotImplementedError()
