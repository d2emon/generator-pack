from rpg.pc import PlayerCharacter as BasePlayerCharacter


class PlayerCharacter(BasePlayerCharacter):
    triggers_count = 17
    items_count = 17

    def __init__(self, name=None):
        super().__init__(name)
        self.article_id = 0
        self.history = [self.article_id, ]
        self.triggers = [False for _ in range(self.triggers_count)]
        self.items = [None for _ in range(self.items_count)]

    def show(self):
        print(self.name)
        print(self.article_id)
        print("Метки:")
        for i, t in enumerate(self.triggers):
            print("%d:\t%s" % (i + 1, t))
        print("Предметы:")
        for i, t in enumerate(self.items):
            print("%d:\t%s" % (i + 1, t))

    def goto(self, article_id):
        self.article_id = article_id
        self.history.append(self.article_id)
        self.show()

    def goto_if(self, trigger, article_set, article_unset):
        if self.triggers[trigger]:
            self.goto(article_set)
        else:
            self.goto(article_unset)


class Conan(PlayerCharacter):
    def __init__(self):
        super().__init__("Конан")
