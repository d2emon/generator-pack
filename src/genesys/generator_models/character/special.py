from ..generator_models import Model


class SpecialSign(Model):
    def __init__(self):
        super().__init__()
        self.signtype = "A scar"
        self.memory = "a pleasant memory",
        self.origin = "a former life"

    @property
    def description(self):
        # names12[random12] + " " + names13[random13] + " " + names14[random14] + " " + names15[random15]
        return self.signtype

    def __repr__(self):
        # " leaves " + names16[random16] + " of " + names17[random17] + "."
        return "%s leaves %s of %s." % (
            self.description,
            self.memory,
            self.origin
        )


class Scar(SpecialSign):
    def __init__(self):
        SpecialSign.__init__(self)
        self.place_from = "stretching from just under the right eye"
        self.place_through = ", running across the nose"
        self.place_to = "and ending on {{his}} left cheek"

    @property
    def description(self):
        return "%s %s%s %s" % (
            self.signtype,
            self.place_from,
            self.place_through,
            self.place_to,
        )


class Tattoo(SpecialSign):
    def __init__(self):
        SpecialSign.__init__(self)
        self.form = "resembling a shield"
        self.visibility = "is almost hidden"
        self.placement = "on the right side of {{his}} neck"

    @property
    def description(self):
        return "%s %s %s %s" % (
            self.signtype,
            self.form,
            self.visibility,
            self.placement,
        )


class TribalMark(SpecialSign):
    def __init__(self):
        SpecialSign.__init__(self)
        self.signtype = "Tribal marks"
        self.form = "in the form of 1 stripe under {{his}} right eye"
        self.meaning = "marks {{his}} heritage"

    @property
    def description(self):
        return "%s %s %s but, more importantly" % (
            self.signtype,
            self.form,
            self.meaning,
        )


class Moles(SpecialSign):
    def __init__(self):
        SpecialSign.__init__(self)
        self.signtype = "Several moles"
        self.style = "charmingly"
        self.placement = "on {{his}} left cheek and"

    @property
    def description(self):
        return "%s are spread %s %s" % (
            self.signtype,
            self.style,
            self.placement,
        )


class Freckles(Moles):
    def __init__(self):
        SpecialSign.__init__(self)
        self.signtype = "Freckles"


class Beard(SpecialSign):
    def __init__(self):
        SpecialSign.__init__(self)
        self.style = "charmingly"
        self.placement = "eyes and"

    @property
    def description(self):
        return "%s %s compliments {{his}} %s" % (
            self.signtype,
            self.style,
            self.placement,
        )
