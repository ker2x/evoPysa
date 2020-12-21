"""Fitness Calculator"""


class FitnessCalculator:
    """Fitness Calculator class"""
    def __init__(self):
        pass

    def getColorFitness(self, original:(int,int,int), generated:(int,int,int)):
        """
        :param original: the original image (r,g,b) pixel
        :param generated: the generated image (r,g,b) pixel
        :return: an error level (0 = no error)
        """
        r = original.r - generated.r
        g = original.g - generated.g
        b = original.b - generated.b
        return r*r + g*g + b*b