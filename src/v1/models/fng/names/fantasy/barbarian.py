from v1.models.fng.names.name import Name


class BarbarianName(Name):
    pass


class BarbarianName1(BarbarianName):
    @property
    def value(self):
        return f"{self.items[1]}{self.items[2]}{self.items[3]}"


class BarbarianName2(BarbarianName):
    @property
    def value(self):
        return f"{self.items[1]}{self.items[2]}{self.items[5]}{self.items[4]}{self.items[3]}"


class MaleBarbarianName3(BarbarianName):
    @property
    def value(self):
        return f"{self.items[1]}{self.items[2]}{self.items[5]}{self.items[4]}{self.items[7]}{self.items[6]}" \
               f"{self.items[3]}"


class FemaleBarbarianName3(BarbarianName):
    @property
    def value(self):
        return f"{self.items[1]}{self.items[2]}{self.items[5]}{self.items[4]}{self.items[7]}{self.items[6]}"
