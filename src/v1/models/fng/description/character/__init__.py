from v1.models.fng.description.description import Description


class CharacterDescription(Description):
    he_or_she = "it"
    him_or_her = "it"
    his_or_her = "its"

    @property
    def value_1(self):
        return f"{self.items[1]}, {self.items[2]} {self.items[3]} a {self.items[4]}, {self.items[5]} face. "\
            + f"{self.items[6]} {self.items[7]} eyes, set {self.items[8]} within their sockets, " \
            + f"watch {self.items[9]} over the {self.items[10]} they've {self.items[11]} for so long."

    @property
    def value_2(self):
        return f"{self.items[12]} {self.items[13]} {self.items[14]} {self.items[15]} and leaves {self.items[16]} " \
            + f"of {self.items[17]}."

    @property
    def value_3(self):
        return f"This is the face of {self.items[18]} {self.items[19]}, " \
            + f"a true {self.items[20]} among {self.items[21]}. " \
            + f"{self.he_or_she.title()} stands {self.items[22]} others, " \
            + f"despite {self.his_or_her} {self.items[23]} frame."

    @property
    def value_4(self):
        return f"There's something {self.items[24]} about {self.him_or_her}, " \
            + f"perhaps it's {self.items[25]} or perhaps it's simply {self.items[26]}. " \
            + f"But nonetheless, people tend to {self.items[27]}, while {self.items[28]}."

    @property
    def value(self):
        return f"{self.value_1}\n" \
            + f"{self.value_2}\n\n" \
            + f"{self.value_3}\n\n" \
            + f"{self.value_4}"


class MaleCharacterDescription(CharacterDescription):
    he_or_she = "he"
    him_or_her = "him"
    his_or_her = "his"


class FemaleCharacterDescription(CharacterDescription):
    he_or_she = "she"
    him_or_her = "her"
    his_or_her = "her"
