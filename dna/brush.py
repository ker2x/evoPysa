"""DNA brush class"""
from random import randint


class Brush:
    """DNA Brush class"""
    id = 0

    def __init__(self, rgba=(255, 255, 255, 255)):
        """
        a brush (just colors, really)
        :param rgba: (red, green, blue, alpha)
        """
        self.r = rgba[0]
        self.g = rgba[1]
        self.b = rgba[2]
        self.a = rgba[3]
        self.id = Brush.id
        Brush.id += 1

    def __str__(self):
        return f"Brush(r={self.r!r}, g={self.g!r}, b={self.b!r}, a={self.a!r}, id={self.id!r})"

    def __repr__(self):
        return f"({self.r!r}, {self.g!r}, {self.b!r}, {self.a!r})"

    def Randomize(self):
        """randomize the rgb values of this Brush"""
        self.r = randint(0, 255)
        self.g = randint(0, 255)
        self.b = randint(0, 255)
        self.a = randint(0, 255)

    def Mutate(self):
        """
        Mutate this brush
        """
        self.Randomize()


