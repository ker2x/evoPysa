"""DNA Point class"""
from random import randint


class Point:
    """A simple DNA point, only x and y"""
    id = 0

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y
        self.id = Point.id
        Point.id += 1

    def __str__(self):
        return f"Point(x={self.x!r}, y={self.y!r}, id={self.id!r})"

    def __repr__(self):
        return f"({self.x!r}, {self.y!r})"

    def Randomize(self):
        """
        Randomize coordinates
        """
        self.x = randint(0, 255)
        self.y = randint(0, 255)

    def Mutate(self):
        """
        Mutate this point
        """
        self.Randomize()
