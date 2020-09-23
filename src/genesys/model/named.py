class NamedModel:
    default_name = None

    def __init__(self, name=None):
        self.__name = name or self.__default_name

    @property
    def __default_name(self):
        return self.default_name or self.__class__.__name__

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return "<{} \"{}\">".format(self.__class__.__name__, str(self))
