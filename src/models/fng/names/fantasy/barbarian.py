from models.fng.names.name import Name


class BarbarianName(Name):
    @property
    def value(self):
        if len(self.data) == 3:
            return f"{self.data['nm1']}{self.data['nm2']}{self.data['nm3']}"

        if len(self.data) == 5:
            return f"{self.data['nm1']}{self.data['nm2']}{self.data['nm5']}{self.data['nm4']}{self.data['nm3']}"

        if len(self.data) == 6:
            return f"{self.data['nm1']}{self.data['nm2']}{self.data['nm5']}{self.data['nm4']}{self.data['nm7']}" \
                f"{self.data['nm6']}"

        if len(self.data) == 7:
            return f"{self.data['nm1']}{self.data['nm2']}{self.data['nm5']}{self.data['nm4']}{self.data['nm7']}" \
                f"{self.data['nm6']}{self.data['nm3']}"
    
        return "".join(self.data.values())


class BarbarianName1(BarbarianName):
    @property
    def value(self):
        return f"{self.data['nm1']}{self.data['nm2']}{self.data['nm3']}"


class BarbarianName2(BarbarianName):
    @property
    def value(self):
        return f"{self.data['nm1']}{self.data['nm2']}{self.data['nm5']}{self.data['nm4']}{self.data['nm3']}"


class MaleBarbarianName3(BarbarianName):
    @property
    def value(self):
        return f"{self.data['nm1']}{self.data['nm2']}{self.data['nm5']}{self.data['nm4']}{self.data['nm7']}{self.data['nm6']}" \
               f"{self.data['nm3']}"


class FemaleBarbarianName3(BarbarianName):
    @property
    def value(self):
        return f"{self.data['nm1']}{self.data['nm2']}{self.data['nm5']}{self.data['nm4']}{self.data['nm7']}{self.data['nm6']}"
