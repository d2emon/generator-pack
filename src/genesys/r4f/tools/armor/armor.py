class ArmorSet:
    def __init__(self):
        self.symmetric_shoulders = False

        self.crown = None
        self.wings = None
        self.helm = None
        self.__shoulder_right = None
        self.__shoulder_left = None
        self.chest = None
        self.legs = None
        self.cloak = None, None
        self.feet = None, None
        self.hands = None
        self.gender = None

    @property
    def shoulder_left(self):
        if self.symmetric_shoulders:
            return self.__shoulder_left or self.__shoulder_right
        return self.__shoulder_left

    @shoulder_left.setter
    def shoulder_left(self, value):
        self.__shoulder_left = value
        if self.symmetric_shoulders:
            self.__shoulder_right = value

    @property
    def shoulder_right(self):
        if self.symmetric_shoulders:
            return self.__shoulder_left or self.__shoulder_right
        return self.__shoulder_right

    @shoulder_right.setter
    def shoulder_right(self, value):
        self.__shoulder_right = value
        if self.symmetric_shoulders:
            self.__shoulder_left = value
