class MoveSystem():
    pass


class MoveCounterMove():
    def start(self, opponents):
        self.opponents = opponents

    def turn(self):
        move, counter_move = self.select_move()
        self.move_figures(move)
        self.move_figures(counter_move)
        self.artillery()
        self.missile()
        self.melee()

    def select_move(self):
        rolls = [[0, None], [0, None]]
        while rolls[0][0] == rolls[1][0]:
            rolls = [[o.roll(), o] for o in self.opponents.players[:2]]
            print(rolls)
        rolls = {r[0]: r[1] for r in rolls}
        print(rolls)
        order = sorted(rolls)
        return rolls[order[0]], rolls[order[1]]

    def move_figures(self, mover):
        print("%s moves its figures" % (mover.title))

    def artillery(self):
        print("Artillery fire is taken")

    def missile(self):
        print("Missile fire is taken")

    def melee(self):
        print("Melees are resolved")
