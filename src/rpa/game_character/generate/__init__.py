Human = 1
RealWorld = 1
SimpleMethod = 1


class CharacterGenerator:
    def __init__(self, classes=None, race=Human):
        self.classes = classes  # [{class: BARD, level:1}, {}, {}]
        self.race = race
        self.name_generator = RealWorld
        self.throw_method = SimpleMethod
        self.random_spells = 3
        
    def add(self):
        pass
    
    def over(self):
        pass
    
    def select(self):
        pass


class PartyGenerator:
    class PartyCharacter:
        def __init__(self, character_class, level=1):
            self.character_class = character_class
            self.level = level
    
    def __init__(self, group="NPC"):
        self.gropup = group
        self.characters = [
            PartyCharacter("Fighter", 1),
        ]
        
    def insert(self, character_class, race, name_generator, dice_points=10):
        pass
    
    def remove(self):
        pass
    
    def generate_party(self):
        pass


def generate_options(skills=True, saving_throws=True, abilities=True, appearance=True, experience=True, hd=True, name=True, spells=True, spheres=False, proficiences=True, turn=True):
    pass
