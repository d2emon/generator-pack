SPHERE_MAGE = 1
SPHERE_CLERIC = 2
SPHERE_PSIONIC = 3


class Sphere:
    def __init__(self, name="", sphere_type=None):
        self.name = name
        self.sphere_type = sphere_type
        self.deities = ""
        self.granted_powers = ""  # Multiline
        self.free_skills = ""
