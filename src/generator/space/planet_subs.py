class PlanetAtmosphere():
    def __init__(self, title, exist=True):
        self.title = title
        self.exist = exist
        
    def __repr__(self):
        return self.title
    

class PlanetType():
    earth = False
    max_moons = 60
        
    def __init__(self, image_id=1):
        self.image = image_id
        
    def __repr__(self):
        return self.image
    
    
class EarthPlanet(PlanetType):
    earth = True
    max_moons = 5
        
    def __repr__(self):
        if self.image < 10:
            image = "0" + str(self.image)
        else:
            image = str(self.image)
        return "earthPlanet%s" % (image)
    
    
class LayerPlanet(PlanetType):
    def __repr__(self):
        return "layerPlanet%s" % (self.image)
    
    
class TerPlanet(PlanetType):
    def __repr__(self):
        return "terplanet%s" % (self.image)
    
    
class MoonPlanet(PlanetType):
    def __repr__(self):
        return "moonPlanet%s" % (self.image)
    
    
class GasPlanet(PlanetType):
    def __repr__(self):
        return "gasPlanet%s" % (self.image)    