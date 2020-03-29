from src.rpg.savage_worlds.savage_worlds.character import Character
from src.rpg.savage_worlds.savage_worlds import dices, skills, edge


class MadScientist(Character):
    def __init__(self):
        super().__init__()
        self.set_stats(
            agility=dices.D4,
            smarts=dices.D10,
            spirit=dices.D6,
            strength=dices.D6,
            vigor=dices.D6,
            skills_list={
                skills.Investigation: dices.D6,
                skills.Knowledge.Science: dices.D10,
                skills.Attention: dices.D6,
                skills.Melding: dices.D8,
            }
        )
        self.set_edges(
            edges=(
                edge.Inventor,
                edge.Mystic.MadScience,
            )
        )


class Driver(Character):
    def __init__(self):
        super().__init__()
        self.set_stats(
            agility=dices.D8,
            smarts=dices.D6,
            spirit=dices.D6,
            strength=dices.D6,
            vigor=dices.D6,
            skills_list={
                skills.Driving: dices.D8,
                skills.Brawling: dices.D4,
                skills.Attention: dices.D6,
                skills.Shooting: dices.D6,
            }
        )
        self.set_edges(
            edges=(
                edge.Ace,
                edge.Swift,
            )
        )


"""
Водитель
Харизма: — ; Шаг: 6; Защита: 4; Стойкость: 5;
Изъяны: один крупный, два мелких;
"""
