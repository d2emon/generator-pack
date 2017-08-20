class PlayerCharacter():
    name = "player"
    triggers_count = 17
    items_count = 17

    def __init__(self):
        self.reset()

    def reset(self):
        self.article_id = 0
        self.history = [self.article_id, ]
        self.triggers = [False for t in range(self.triggers_count)]
        self.items = [None for i in range(self.items_count)]

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
    name = "Конан"
