class Collection:
    def __init__(self, items):
        self.items = items

    def get_item(self, item_class):
        return next((item for item in self.items if isinstance(item, item_class)), None)
