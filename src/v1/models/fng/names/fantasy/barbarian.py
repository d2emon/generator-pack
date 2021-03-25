from v1.models.fng.names.name import Name


class BarbarianName(Name):
    pass


class BarbarianName1(BarbarianName):
    @property
    def value(self):
        return f"{self.items['nm1']}{self.items['nm2']}{self.items['nm3']}"


class BarbarianName2(BarbarianName):
    @property
    def value(self):
        return f"{self.items['nm1']}{self.items['nm2']}{self.items['nm5']}{self.items['nm4']}{self.items['nm3']}"


class MaleBarbarianName3(BarbarianName):
    @property
    def value(self):
        return f"{self.items['nm1']}{self.items['nm2']}{self.items['nm5']}{self.items['nm4']}{self.items['nm7']}{self.items['nm6']}" \
               f"{self.items['nm3']}"


class FemaleBarbarianName3(BarbarianName):
    @property
    def value(self):
        return f"{self.items['nm1']}{self.items['nm2']}{self.items['nm5']}{self.items['nm4']}{self.items['nm7']}{self.items['nm6']}"
