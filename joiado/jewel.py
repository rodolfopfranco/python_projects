import random

class Jewel:
    def __init__(self):
        self.color = random.randint(1, 5)

    def __str__(self):
        return str(self.color)

    def getColor(self):
        return self.color

    def setColor(self,newColor):
        self.color = newColor