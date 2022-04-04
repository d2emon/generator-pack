from .structures import Structure


class Skyscraper(Structure):
    def __init__(self, name, size, scale=0):
        super().__init__(name, size, scale)


SKYSCRAPERS = [
    Skyscraper("Puerta de Europa", 113),
    Skyscraper("BT Tower", 191),
    Skyscraper("Torre Espacio", 224),
    Skyscraper("Torre de Cristal", 249),
    Skyscraper("Baioke Tower II", 304),
    Skyscraper("The Shard", 306),
    Skyscraper("U.S. Bank Tower", 310.3),
    Skyscraper("Chrysler Building", 319),
    Skyscraper("Ryugyong hotel", 330),
    Skyscraper("Stratosphere Las Vegas", 350),
    Skyscraper("Bank of China Tower", 367),
    Skyscraper("Empire State Building", 381),
    Skyscraper("Trump International Hotel and Tower", 423),
    Skyscraper("Marina 101", 426),
    Skyscraper("Willis Tower", 442),
    Skyscraper("Petronas Tower", 452),
    Skyscraper("International Commerce Centre", 484),
    Skyscraper("SHanghai World Financial Center", 492),
    Skyscraper("Taipei 101", 509),
    Skyscraper("CTF Finance Centre", 530),
    Skyscraper("One World Trading Center", 541),
    Skyscraper("Lotte World Tower", 555),
    Skyscraper("Ping An Finance Center", 599),
    Skyscraper("Abraj Al Bait", 609),
    Skyscraper("Shanghai Tower", 632),
    Skyscraper("Burj Khalifa", 828),
]