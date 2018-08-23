from menu import Menu


class MenuHandler:
    @property
    def text(self):
        return ""

    @property
    def option(self):
        return self.text, self.handle

    def handle(self):
        menu = Menu(
            title=self.text,
            options=[
                ("Back", Menu.CLOSE),
                ("Exit", exit),
            ]
        )
        menu.open()
