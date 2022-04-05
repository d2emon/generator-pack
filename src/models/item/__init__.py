class Item:
    def __init__(
        self,
        description='',
        *args,
        **kwargs,
    ):
        self.description = description

    def __repr__(self):
        return f"<{self.__class__.__name__} \"{self}\": \"{self.description}\">"
