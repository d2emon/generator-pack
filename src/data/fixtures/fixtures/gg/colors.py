class Color:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

dark = Color("Dark")


blond = Color("Blond")
black = Color("Black")
brown = Color("Brown")
auburn = Color("Auburn")
violet = Color("Violet")
blue = Color("Blue")
pink = Color("Pink")
red = Color("Red")
white = Color("White")
gray = Color("Gray")
checkered = Color("Checkered")
bee = Color("Bee")


hair_colors = (
    dark,
    blond,
    black,
    auburn,
)
