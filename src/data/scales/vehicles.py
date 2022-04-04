from models.scales import Sized as Scalable, ScalableSize as Size


class Vehicle(Scalable):
    def __init__(self, name, size, scale=0):
        super().__init__(name, Size(size, scale))


VEHICLES = [
    Vehicle("Skate", 0.8),
    Vehicle("Wheelchair", 1.2),
    Vehicle("Motorcycle (Ducati)", 2),
    Vehicle("Boat", 4),
    Vehicle("Carriaje", 4),
    Vehicle("Car (BMW X5)", 4.8),
    Vehicle("Tractor", 5),
    Vehicle("Van (Mercedes-Benz Sprinter)", 7),
    Vehicle("Tank (M1 Abrams)", 9),
    Vehicle("Helicopter (Hughes 500)", 9.4),
    Vehicle("Komatsu D575A-3", 11),
    Vehicle("Limousine", 13),
    Vehicle("Komatsu Haulpak", 15),
    Vehicle("Truck", 16),
    Vehicle("Balloon", 16),
    Vehicle("Jet Fighter (Eurofighter Typhoon)", 16),
    Vehicle("Helicopter (Apache)", 18),
    Vehicle("B2 Spirit", 21),
    Vehicle("Auto Tram Extra Grand (Bus)", 30),
    Vehicle("Trireme", 36),
    Vehicle("Space Shuttle", 37),
    Vehicle("Helicopter (Mil Mi-26)", 40),
    Vehicle("Concorde", 61),
    Vehicle("Airbus A380", 73),
    Vehicle("Zeppelin", 75),
    Vehicle("ISS", 109),
    Vehicle("Saturn V", 110),
    Vehicle("Submarine (Akula)", 175),
    Vehicle("High Speed Train (AVE)", 200),
    Vehicle("Bagger 293", 225),
    Vehicle("Hindenburg Zeppelin", 245),
    Vehicle("RMS Titanic", 269),
    Vehicle("USS Theodore Roosevelt", 332),
    Vehicle("Oasis of the Seas", 362),
    Vehicle("Prelude FLNG", 488),
    Vehicle("Mauritania Railway", 2500),
]
