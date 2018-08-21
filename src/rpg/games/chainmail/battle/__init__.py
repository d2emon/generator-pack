class Battle:
    def __init__(self, move_system, opponents):
        self.move_system = move_system
        self.opponents = opponents
        self.__turns = 5

    def start(self):
        self.__turns = 5
        self.move_system.start(self.opponents)
        print("Battle stated")

    def finish(self):
        print("Battle finished")

    @property
    def is_finished(self):
        return self.__turns <= 0

    def turn(self):
        print("Next turn")
        self.move_system.turn()
        self.__turns -= 1

    def process(self):
        self.start()
        while not self.is_finished:
            self.turn()
        self.finish()
