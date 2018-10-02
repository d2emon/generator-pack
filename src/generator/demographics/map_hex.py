class MapHex:
    """
    Hexes: It may be important for some GMs using this article to know how much land is in a hexagonal area! To
    determine the area of a hex, multiply its width by 0.9306049, and square the result. Thus, if your game-map has
    hexes 30 miles across, each hex represents about 780 square miles (and it's a convenient size for travel-times,
    since 30 miles is a good rule of thumb for a day's road travel on foot or horseback).
    """
    hex_area = .9305347  # .9306049

    def __init__(self, length=30):
        self.length = length

    @property
    def area(self):
        return (self.length * self.hex_area) ** 2

    def hexes(self, area):
        if self.area <= 0:
            return 0
        return area / self.area

    def describe(self, area):
        return "{hexes} hexes, each {hex.width}km across and roughly {hex.area}km^2 in area".format(
            hex=self,
            hexes=self.hexes(area),
        )
