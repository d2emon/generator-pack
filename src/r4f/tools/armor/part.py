from .material import Plate


class Part:
    name = ''

    def __init__(self, item_id, material=Plate):
        self.item_id = item_id
        self.background_item_id = item_id
        self.material = material

    def url(self, gender):
        return self.material.url(gender, self.item_id)


class Helm(Part):
    name = 'Helm'


class Chest(Part):
    name = 'Chest'

    def __init__(self, item_id):
        super().__init__(item_id)
        self.breastplate = True

    def url(self, gender):
        return self.material.url(gender, self.item_id, breastplate=self.breastplate)


class Feet(Part):
    name = 'Feet'

    def background_url(self, gender):
        if self.material.material_type == 'cloth':
            background_item_id = 'feet01'
        else:
            background_item_id = self.item_id
        return self.material.background_url(gender, background_item_id)


class ShoulderLeft(Part):
    name = 'Shoulder Left'


class Legs(Part):
    name = 'Legs'

    def url(self, gender):
        return gender.url(self.item_id)


class Hands(Part):
    name = 'Gloves'


class ShoulderRight(Part):
    name = 'Shoulder Right'


class Cloak(Part):
    name = 'Cloak'

    def url(self, gender):
        return gender.url(self.item_id)

    def background_url(self, gender):
        return gender.url(self.background_item_id)


class Crown(Part):
    name = 'Crown'

    def url(self, gender):
        return gender.url(self.item_id)


class Wings(Part):
    name = 'Wings'

    def url(self, gender):
        return gender.url(self.item_id)
