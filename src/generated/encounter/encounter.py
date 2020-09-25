class Encounter:
    description = None
    allowed_at = []

    def __init__(
        self,
        distance=None,
        is_surprised=False,
        is_surprising=False,
    ):
        self.distance = distance
        self.is_surprised = is_surprised
        self.is_surprising = is_surprising

    def __str__(self):
        text = [
            self.distance,
            self.description,
        ]
        if self.is_surprising:
            text.append("Партия застигнута врасплох")
        if self.is_surprised:
            text.append("Столкновение застигнуто врасплох")
        return '\n'.join(map(str, text))
