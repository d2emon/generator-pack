class Sex():
    name = "Asexual"
    id = 0
    replaces = {
        "{{He}}": "It",
        "{{he}}": "it",
        "{{him}}": "it",
        "{{his}}": "it",
    }

    def __repr__(self):
        return self.name


class Male(Sex):
    name = "Male"
    id = 0
    replaces = {
        "{{He}}": "He",
        "{{he}}": "he",
        "{{him}}": "him",
        "{{his}}": "his",
    }


class Female(Sex):
    name = "Female"
    id = 1
    replaces = {
        "{{He}}": "She",
        "{{he}}": "she",
        "{{him}}": "her",
        "{{his}}": "her",
    }
