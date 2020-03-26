class BodyPart:
    name = "Body"

    def __str__(self):
        return self.name


class Chest(BodyPart):
    name = "Chest"


class Thighs(BodyPart):
    name = "Thighs"


class Legs(BodyPart):
    name = "Legs"


class Feet(BodyPart):
    name = "Feet"
