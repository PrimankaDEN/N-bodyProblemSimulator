__author__ = 'PrimankaDEN'
import math


class Vector2:
    x=0.0
    y=0.0

    def __init__(self, x,y):
        self.x=x
        self.y=y

    def __add__(self, other):
        return Vector2(self.x+other.x, self.y+other.y)

    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"

    def getLength(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __sub__(self, other):
        return Vector2(self.x-other.x, self.y-other.y)

    def __eq__(self, other):
        if self.x==other.x and self.y==other.y:
            return True
        return False
