from .body_parts import BodyPart


class Limb(BodyPart):
    pass


class Wing(BodyPart):
    # feathers = BodyPart.child_property(Feathers)
    pass


# class Tentacle(Limb, SkinlessSoftBodyPart):
#     pass


class Tail(BodyPart):
    pass
