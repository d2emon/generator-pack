from v1.factories.fng import NameBlock


class Mark:
    types = NameBlock()  # 12
    places_from = NameBlock()  # 13
    places_through = NameBlock()  # 14
    places_to = NameBlock()  # 15
    memory_types = NameBlock()  # 16
    memory_ofs = NameBlock()  # 17

    def __init__(self, name_id):
        self.name_id = name_id


class Scar(Mark):
    pass


class Birthmark(Mark):
    places_from = NameBlock()  # 13
    places_through = NameBlock()  # 14
    places_to = NameBlock()  # 15


class Moles(Mark):
    places_from = NameBlock()  # 13
    places_through = NameBlock()  # 14
    places_to = NameBlock()  # 15


class Freckles(Mark):
    places_from = NameBlock()  # 13
    places_through = NameBlock()  # 14
    places_to = NameBlock()  # 15
    memory_types = NameBlock()  # 16
    memory_ofs = NameBlock()  # 17


class SmoothSkin(Mark):
    places_from = NameBlock()  # 13
    places_through = NameBlock()  # 14
    places_to = NameBlock()  # 15
    memory_types = NameBlock()  # 16
    memory_ofs = NameBlock()  # 17


class SoftSkin(Mark):
    places_from = NameBlock()  # 13
    places_through = NameBlock()  # 14
    places_to = NameBlock()  # 15
    memory_types = NameBlock()  # 16
    memory_ofs = NameBlock()  # 17
