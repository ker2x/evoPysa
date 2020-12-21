"""DNA Point class"""


class Point():
    """A simple DNA point, only x and y"""
    def __init__(self, x:int = 0, y:int = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x!r}, {self.y!r})"

    def __repr__(self):
        return '{x:' + self.x + ', y:' + self.y + '}'

    def Mutate(self):
        raise NotImplementedError
