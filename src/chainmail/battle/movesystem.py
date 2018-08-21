class MoveSystem:
    def __init__(self):
        self.movers = None

    def start(self, movers):
        self.movers = movers

    def turn(self):
        raise NotImplementedError("Turn is not implemented")


class ChainmailMoveSystem(MoveSystem):
    def move_figures(self, mover):
        print("{} moves its figures".format(mover.title))

    def artillery(self):
        print("Artillery fire is taken")

    def missile(self):
        print("Missile fire is taken")

    def melee(self):
        print("Melees are resolved")


class MoveCounterMove(ChainmailMoveSystem):
    def turn(self):
        move, counter_move = self.movers.roll_order()
        self.move_figures(move)
        self.move_figures(counter_move)
        self.artillery()
        self.missile()
        self.melee()
