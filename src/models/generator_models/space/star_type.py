class SunType:
    id = 0

    def __init__(self, title, blue=False):
        self.title = title
        self.image = title
        self.blue = blue
        
    def __repr__(self):
        if self.blue:
            return "%s.blue" % (self.title)
        return self.title