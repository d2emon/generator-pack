class Formation():
    name = "Loose"
    footOnly = False
    to_column = 0
    to_line = 0
    to_square = 0


class Column(Formation):
    name = "Column"
    to_line = 1
    to_square = 1


class Line(Formation):
    name = "Line"
    to_column = 1
    to_square = 2


class Square(Formation):
    name = "Square"
    footOnly = True
