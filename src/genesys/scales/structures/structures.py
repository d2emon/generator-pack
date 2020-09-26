from scale.scalable import Scalable


class Structure(Scalable):
    def __init__(self, name, size, scale=0):
        Scalable.__init__(self, name, size, scale)


STRUCTURES = [
    Structure("Parthenon", 13.7),
    Structure("Radio Telescope", 15),
    Structure("Kaaba", 15.2),
    Structure("Great Sphinx of Giza", 20.2),
    Structure("Templo de Kukulcan", 24),
    Structure("Brandenburg Gate", 26),
    Structure("Christ the Redemeer", 39.6),
    Structure("Sultan Ahmed Mosque", 43),
    Structure("Saint Basil's Cathedral", 47.5),
    Structure("Colosseum", 48),
    Structure("Tower of Pisa", 55),
    Structure("Neuschwanstein", 65),
    Structure("Sydney Opera House", 65),
    Structure("Angkor Wat", 65),
    Structure("The Motherland Calls", 85),
    Structure("United States Capitol", 88),
    Structure("Wind Turbine", 90),
    Structure("Statue of Liberty", 93),
    Structure("Atomium", 102),
    Structure("Palace of Westminster", 102),
    Structure("Monumental flag of Mexico", 125),
    Structure("London Eye", 135),
    Structure("St Peter's Basilica", 136),
    Structure("Great Piramid of Giza", 138),
    Structure("Kingda Ka", 139),
    Structure("Spring Temple Buddha", 153),
    Structure("Washington Monument", 169),
    Structure("Sagrada Familia", 170),
    Structure("Hoover Dam", 221),
    Structure("Cooling Tower", 200),
    Structure("Eiffel Tower", 300),
    Structure("Radio Telescope FAST", 500),
    Structure("KVLY-TV mast", 628),
    # Burj Khalifa
    Structure("Akashi Kaikyo Bridge", 3911),
]