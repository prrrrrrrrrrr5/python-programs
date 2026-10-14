import math
class Sfera:
    def __init__(self,r):
        self.__r=r
    def volume(self):
        return (4/3)*math.pi*self.__r**3
    def superficie(self):
        return 4*math.pi*self.__r**2
