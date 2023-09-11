# TODO: Convert to Model
class Instance:
    def __init__(self, thing, parent=None):
        # self.id = uuid
        self.name = 'thing'

        self.parent = parent
        self.children = []

        # TODO: Rename to factory
        self.thing = thing

        self.__grown = False

    def grow(self):
        if self.__grown:
            return

        self.name = self.thing.name_factory()
        for child in self.thing.children_factory(self):
            self.children.append(child)

        self.__grown = True
