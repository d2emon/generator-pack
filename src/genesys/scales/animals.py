from .scalable import Scalable


class Animal(Scalable):
    def __init__(self, name, size, scale=0):
        Scalable.__init__(self, name, size, scale)


ANIMALS = [
    Animal("Tardigrade", 50, -6),
    Animal("Dust mite", 0.2, -3),
    Animal("Small Ant", 1, -3),
    Animal("Flea", 3, -3),
    Animal("Big Ant", 5, -3),
    Animal("House Fly", 7, -3),
    Animal("Spider", 20, -3),
    Animal("Beetle", 30, -3),
    Animal("Hummingbird", 50, -3),
    Animal("Common Frog", 70, -3),
    Animal("Mouse", 80, -2),
    Animal("Centipede", .3),
    Animal("Rabbit", .4),
    Animal("Cat", .46),
    Animal("Eagle", .8),
    Animal("Japanese Spider Crab", 1.2),
    Animal("Giant Tortoise", 1.3),
    Animal("Wolf", 1.5),
    Animal("Gorilla", 1.7),
    Animal("Human", 1.7),
    Animal("Reticulated Python", 8),
    Animal("Komodo Dragon", 2.6),
    Animal("Lion", 2.4),
    Animal("Horse", 2.4),
    Animal("Bear", 2.8),
    Animal("Hippopotamus", 3.3),
    Animal("White Rhinoceros", 4),
    Animal("Northern Elefant Seal", 4.8),
    Animal("African Elefant", 6),
    Animal("Killer Whale", 7),
    Animal("Whale Shark", 12),
    Animal("Sperm Whale", 24),
    Animal("Blue Whale", 33),
]
