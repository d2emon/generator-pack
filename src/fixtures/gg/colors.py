class Color:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


blond = Color("Blond")
black = Color("Black")
auburn = Color("Auburn")
violet = Color("Violet")
blue = Color("Blue")
pink = Color("Pink")
red = Color("Red")
white = Color("White")
gray = Color("Gray")
checkered = Color("Checkered")


hair_colors = (
    blond,
    black,
    auburn,
)
