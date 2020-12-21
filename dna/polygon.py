"""DNA Polygon"""


class Polygon:
    """DNA Polygon class"""
    id=0

    def __init__(self, points: [], brush):
        """
        Create a polygon made of [dns.points] and a brush
        :param points: a list of dna.point
        :param brush:  a dna.brush
        """
        self.points = points
        self.brush = brush
        self.id = Polygon.id
        Polygon.id += 1

    def __str__(self):
        return f"Polygon(points={self.points!r}, brush={self.brush!r}, id={self.id!r})"

    def __repr__(self):
        return f"({self.points!r}, {self.brush!r})"

    def Randomize(self):
        """Randomize this Polygon"""
        raise NotImplementedError

    def Mutate(self):
        """Mutate this point"""
        raise NotImplementedError

    def AddPoint(self):
        """Add a point to this polygon"""
        raise NotImplementedError

    def RemovePoint(self):
        """Remove a point from this polygon"""
        raise NotImplementedError
