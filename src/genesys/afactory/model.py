class Model:
    default_name = 'Item'

    def __init__(self):
        self.__name = self.default_name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value


class Item(Model):
    type_id = 0
    default_name = 'Item'

    def __init__(self):
        super().__init__()
        self.value = 0

    def __str__(self):
        return '{} {} {} {}'.format(self.name, self.__name, self.value, self.type_id)


class Item1(Item):
    type_id = 1
    default_name = 'Item 1'


class Item2(Item):
    type_id = 2
    default_name = 'Item 2'


class SubItem(Model):
    default_name = 'SubItem'

    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def __str__(self):
        return '{} {}'.format(self.parent, self.name)


class SubItem1(SubItem):
    default_name = 'SubItem 1'


class SubItem2(SubItem):
    default_name = 'SubItem 2'
