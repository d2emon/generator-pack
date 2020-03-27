class Material:
    name = ''
    material_type = ''
    path = '{}'

    @classmethod
    def url(cls, gender, item_id, **kwargs):
        return gender.url(cls.path.format(item_id))

    @classmethod
    def background_url(cls, gender, item_id, **kwargs):
        background_item_id = "b" + item_id
        return gender.url(cls.path.format(background_item_id))


class Plate(Material):
    name = 'Plate'
    material_type = 'plate'

    @classmethod
    def url(cls, gender, item_id, breastplate=True, **kwargs):
        if breastplate:
            return gender.url("b{}".format(item_id))
        else:
            return gender.url(item_id)


class Leather(Material):
    name = 'Leather / Hide'
    material_type = 'leather'
    path = 'leather/{}'


class Cloth(Material):
    name = 'Cloth / Robes'
    material_type = 'cloth'
    path = 'cloth/{}'
