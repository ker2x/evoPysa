"""DNA Polygon"""


class Polygon():
    """DNA Polygon class"""
    def __init__(self, points, brush):
        """
        Create a polygon made of [dns.points] and a brush
        :param points: a list of dna.point
        :param brush:  a dna.brush
        """
        self.points = points
        self.brush = brush

    def Randomize(self):
        """Randomize this Polygon"""
        raise NotImplementedError

    def Mutate(self):
        raise NotImplementedError
