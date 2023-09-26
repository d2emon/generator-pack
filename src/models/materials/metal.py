from .matter import Matter


class Metal(Matter):
    state = Matter.SOLID


class Iron(Metal):
    pass


class Steel(Metal):
    pass
