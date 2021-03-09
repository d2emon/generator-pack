from v1.models.fng.names.name import Name
from v1.fixtures.fng.names import fantasy


class AnansiName(Name):
    vowels = fantasy.anansi.names8

    @property
    def value(self):
        vowels_count = 0
        if self.items[0][-1] in self.vowels:
            vowels_count += 1
        if self.items[2][0] in self.vowels:
            vowels_count += 1

        if vowels_count == 2 and len(self.items[2]) > 1:
            name_final = self.items[2][2:] if self.items[2][1] in self.vowels else self.items[2][1:]
        elif vowels_count == 1:
            name_final = self.items[2]
        else:
            name_final = f"{self.items[1]}{self.items[2]}"

        return f"{self.items[0]}{name_final}"
