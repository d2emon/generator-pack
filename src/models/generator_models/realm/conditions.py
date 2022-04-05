from .item import Item


class Description(Item):
    data = [
        " you don't feel like you're in danger", " you feel relatively safe at the moment",
        " you get the feeling you're not in immediate danger", " you're at ease and you feel secure in this world",
        " you don't feel a sense of dread or danger",

        " you feel like you're constantly in danger", " you can't help but feel danger lurks around every corner",
        " you feel slightly panicked as danger hides everywhere",
        " you can't escape the feeling of dread that your life is in danger", " you feel exposed and in jeopardy",

        " and you can't wait to explore it all", " and a sense of excitement takes hold of you",
        " and a childish curiosity takes over your mind", " and it is all yours to explore",
        " and a sea of time to explore it in",

        ", but not everything that's hidden may be as pleasant as this world",
        ", but now is not the time to get complacent and reckless",
        ", but safety still comes first, it is a strange new world after all",
        ", but it's important to remember that danger can lurk anywhere", ", but some things may be best left a secret"

    ]


    @property
    def conditions_type(self):
        if self.item_id < 5:
            return Conditions.BAD
        elif self.item_id < 10:
            return Conditions.GOOD
        elif self.item_id < 15:
            return Conditions.NORMAL
        else:
            return Conditions.UNKNOWN

    @classmethod
    def choice(cls, data=None, conditions=None, **kwargs):
        if data is None:
            data = cls.data

        if conditions is not None:
            if conditions.conditions_type == Conditions.BAD:
                data = data[:5]
            elif conditions.conditions_type == Conditions.GOOD:
                data = data[5:10]
            elif conditions.conditions_type == Conditions.NORMAL:
                data = data[10:15]
            elif conditions.conditions_type == Conditions.UNKNOWN:
                data = data[15:]

        return super().choice(data, **kwargs)


class Conditions(Item):
    BAD = 1
    NORMAL = 2
    GOOD = 3
    UNKNOWN = 4

    data = [
        "Despite the uncomfortable atmosphere", "Even though this world's harsh", "Even with these rough conditions",
        "Regardless of the horrible conditions", "In spite of the treacherous landscape",

        "Largely due to these conditions", "Because of this rough environment", "Due to these dreadful surroundings",
        "Because of these horrible conditions", "It's because of this awful landscape",

        "The conditions in this world are excellent", "The landscape is astonishing",
        "A seemingly pristine landscape awaits you", "A spectacular world welcomes you",
        "Perfect conditions in a perfect world",

        "Much remains to be discovered here", "It's a world of hidden mysteries",
        "Who knows what secrets this world holds", "Uncharted territory as far as the eye can see",
        "There's so much to learn in this world"
    ]

    @property
    def conditions_type(self):
        if self.item_id < 5:
            return self.BAD
        elif self.item_id < 10:
            return self.GOOD
        elif self.item_id < 15:
            return self.NORMAL
        else:
            return self.UNKNOWN

    def __init__(self, item_id, text, description=None):
        super().__init__(item_id, text)

        self.description = []
        if description is None:
            self.description = Description.choice(conditions=self)
        else:
            self.description = description

    def __str__(self):
        return "{}{}.".format(self.text, self.description)
