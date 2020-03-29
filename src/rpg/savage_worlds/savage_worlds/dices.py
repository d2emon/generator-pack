class SavageWorldDice:
    DICE = [
        0,
        4,
        6,
        8,
        10,
        12,
    ]
    NAMES = [
        '0',
        'd4',
        'd6',
        'd8',
        'd10',
        'd12',
    ]

    def __init__(self, max_value):
        self.dice_id = self.DICE.index(max_value) or 0

    @property
    def max_value(self):
        return self.DICE[self.dice_id]

    def __str__(self):
        return self.NAMES[self.dice_id]

    def roll(self):
        print(self)
        return 1


D0 = SavageWorldDice(0)
D4 = SavageWorldDice(4)
D6 = SavageWorldDice(6)
D8 = SavageWorldDice(8)
D10 = SavageWorldDice(10)
D12 = SavageWorldDice(12)
