class MoveSystem():
    def move_figures(self, mover):
        print("%s moves its figures" % (mover.title))

    def artillery(self):
        print("Artillery fire is taken")

    def missile(self):
        print("Missile fire is taken")

    def melee(self):
        print("Melees are resolved")


class MoveCounterMove(MoveSystem):
    def start(self, opponents):
        self.opponents = opponents

    def turn(self):
        move, counter_move = self.opponents.roll_order()
        self.move_figures(move)
        self.move_figures(counter_move)
        self.artillery()
        self.missile()
        self.melee()
