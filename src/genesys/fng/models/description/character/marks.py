from genesys.fng.providers.list_item import ListItemProvider


class Mark:
    types = []  # 12
    places_from = ListItemProvider([])  # 13
    places_through = ListItemProvider([])  # 14
    places_to = ListItemProvider([])  # 15
    memory_types = ListItemProvider([])  # 16
    memory_ofs = ListItemProvider([])  # 17

    def __init__(self, name_id):
        self.name_id = name_id


class Scar(Mark):
    pass


class Birthmark(Mark):
    places_from = ListItemProvider([])  # 13
    places_through = ListItemProvider([])  # 14
    places_to = ListItemProvider([])  # 15


class Moles(Mark):
    places_from = ListItemProvider([])  # 13
    places_through = ListItemProvider([])  # 14
    places_to = ListItemProvider([])  # 15


class Freckles(Mark):
    places_from = ListItemProvider([])  # 13
    places_through = ListItemProvider([])  # 14
    places_to = ListItemProvider([])  # 15
    memory_types = ListItemProvider([])  # 16
    memory_ofs = ListItemProvider([])  # 17


class SmoothSkin(Mark):
    places_from = ListItemProvider([])  # 13
    places_through = ListItemProvider([])  # 14
    places_to = ListItemProvider([])  # 15
    memory_types = ListItemProvider([])  # 16
    memory_ofs = ListItemProvider([])  # 17


class SoftSkin(Mark):
    places_from = ListItemProvider([])  # 13
    places_through = ListItemProvider([])  # 14
    places_to = ListItemProvider([])  # 15
    memory_types = ListItemProvider([])  # 16
    memory_ofs = ListItemProvider([])  # 17
