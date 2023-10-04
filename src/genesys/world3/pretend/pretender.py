import random


class Button:
    def __init__(self, name, is_new=False, selected=False, on_click=lambda: None):
        self.__name = name
        self.is_new = is_new
        self.selected = selected
        self.on_click = on_click

    @property
    def name(self):
        if self.is_new:
            return '{} [new]'.format(self.__name)
        else:
            return self.name

    @property
    def class_name(self):
        if self.is_new:
            return 'new'
        elif self.selected:
            return 'selected'
        else:
            return ''


class Action:
    action_click = 0

    def __init__(self, names, subactions):
        self.names = names
        self.subactions = subactions

    @classmethod
    def parse(cls, s):
        items = s.split('|')
        names, subactions = [item.split('/') for item in items]
        return cls(names, subactions)

    @classmethod
    def __become(cls, params):
        Pretender.find(random.choice(params)).play_soon()

    @classmethod
    def __unlock(cls, params):
        for name in params:
            item = Pretender.find(name)
            if item is None:
                continue
            item.unlock()
        Game.list_things()

    def action(self):
        subaction = self.subactions[self.action_click % len(self.subactions)]
        self.action_click += 1

        for name in self.names[1:]:
            action, params = name.split(':')
            params = params.split(',')
            if action == 'become':
                return self.__become(params)
            if action == 'unlock':
                return self.__unlock(params)


class Pretender:
    ITEMS = []

    becoming = False

    def __init__(
        self,
        name='',
        level=0,
        actions=(),
        namegen=None,
        unlocks=None,
    ):
        self.name = name
        self.level = level
        self.unlocked = False
        self.played = False
        self.actions = [Action.parse(a) for a in actions]
        self.namegen = namegen or [self.name]
        self.__unlocks = unlocks or []
        self.discovery = 0
        self.ITEMS.append(self)

        self.text = ''

    @property
    def buttons(self):
        for action in self.actions:
            yield Button(
                action.names[0],
                on_click=lambda: self.action(action),
            )

    @property
    def new_name(self):
        if len(self.namegen) == 1:
            return self.namegen[0]
        return ''.join(random.choice(names) for names in self.namegen)

    @property
    def unlocks(self):
        items = (self.find(name) for name in self.__unlocks)
        return (item for item in items if item is not None)

    @classmethod
    def find(cls, name):
        return next((item for item in cls.ITEMS if item.name == name), None)

    def unlock(self):
        if self.unlocked:
            return

        self.unlocked = True
        self.discovery = Game.discovery
        Game.discovery += 1

    def play(self, time=None):
        if time is None:
            if Game.switching_player:
                return lambda: None
            else:
                Game.switching_player = True
                return lambda: self.play(0)

        if time >= 19:
            Game.switching_player = False
            return lambda: None

        if time != 9:
            return lambda: self.play(time + 1)

        name = self.new_name
        self.text = 'You are {} <b>{}</b>.\n\n'.format(an(name), name)

        self.played = True
        self.unlock()
        for unlock in self.unlocks:
            unlock.unlock()

        Action.action_click = 0
        playing = self

        Game.list_things()

        return lambda: self.play(time + 1)

    def __on_time(self):
        self.becoming = False
        return self.play()

    def play_soon(self):
        if self.becoming:
            return lambda: None

        self.becoming = True
        return self.__on_time

    def action(self, action):
        if self.becoming:
            return

        return action.action()


class Game:
    discovery = 0

    switching_player = False

    @classmethod
    def list_things(cls):
        unlocked = (item for item in Pretender.ITEMS if item.unlocked)
        buttons = [
            Button(i.name, is_new=not i.played, on_click=lambda: i.play())
            for i in sorted(unlocked, key=lambda item: item.discovery, reverse=True)
        ]
        return '(Pick a thing to embody.)\n', buttons


def an(s):
    """
    what = what.charAt(0).toLowerCase();
    if (what == "a" || what == "e" || what == "i" || what == "o" || what == "u")
        return "an";
    else
        return "a";

    :param s:
    :return:
    """
    return 'a'
