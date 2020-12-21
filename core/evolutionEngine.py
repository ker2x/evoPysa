"""Evolution Engine"""


class EvolutionEngine:
    """Evolution Engine class"""
    def __init__(self):
        self.isRunning = False
        self.generation = 0
        self.selected = 0
        self.numPoints = 0
        self.numPolygon = 0
        self.fitness = 0
        self.pointPerPolygon = 0


    def start(self):
        """engine go brrr"""
        self.isRunning = True
        raise NotImplementedError

    def stop(self):
        """stop the loop"""
        self.isRunning = False
        raise NotImplementedError

    def loop(self):
        """main evolution loop"""
        while self.isRunning:
            pass
        raise NotImplementedError

    def calculateStatistics(self):
        raise NotImplementedError