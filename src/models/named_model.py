class NamedModel:
    default_name = None

    def __init__(self, name=None):
        self.__name = name

    @property
    def name(self):
        if self.__name is None:
            self.__name = self.default_name or self.__class__.__name__
        
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return "<{} \"{}\">".format(self.__class__.__name__, str(self))
