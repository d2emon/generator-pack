from v1.fng.genesys.name import Name


class NameFactory:
    name_class = Name
    factory_classes = []
    blocks_map = {}
    default_blocks = {}

    def __init__(self, blocks):
        super().__init__(blocks)
        # self.providers = providers or self.default_providers
        self.blocks = blocks or self.default_blocks
        self.__factories = [factory(self.blocks) for factory in self.factory_classes]

    @property
    def factories(self):
        return self.__factories

    def get_items(self):
        return {item_id: next(self.blocks[block_id]) for item_id, block_id in self.blocks_map.items()}

    def get_factory(self, item_id):
        return self

    def get_name(self, item_id):
        factory = self.get_factory(item_id)

        name = ''
        while name == '':
            name = factory()

        return name

    def names(self):
        return [self.get_name(item_id) for item_id in range(10)]

    def validate(self, items):
        return items

    def __items(self):
        items = self.get_items()
        return self.validate(items)

    def __call__(self, *args, **kwargs):
        return self.name_class(self.__items())
