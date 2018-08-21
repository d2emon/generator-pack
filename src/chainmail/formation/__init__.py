class Formation:
    name = ""
    footOnly = False
    change = dict()

    @classmethod
    def to_change(cls, new_formation):
        return cls.change.get(new_formation, 0)


class LooseFormation(Formation):
    name = "Loose"


class Column(Formation):
    name = "Column"
    change = {
        "Line": 1,
        "Square": 1,
    }


class Line(Formation):
    name = "Line"
    change = {
        "Column": 1,
        "Square": 2,
    }


class Square(Formation):
    name = "Square"
    footOnly = True
