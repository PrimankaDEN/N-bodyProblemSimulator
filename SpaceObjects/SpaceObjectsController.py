__author__ = 'Home'

from Utils.Vector2 import *
from Utils.Properties import *


class SpaceObjectController:
    _objects = []

    def __init__(self):
        self._objects = []

    def __getitem__(self, item):
        return self._objects[item]

    def __setitem__(self, key, value):
        self._objects[key] = value

    def append(self, value):
        self._objects.append(value)

    def calculateAllAccels(self):
        for i in range(len(self._objects)):
            summaryAccel = Vector2(0.0, 0.0)
            for j in range(len(self._objects)):
                if i == j:
                    continue
                summaryAccel = summaryAccel + SpaceObjectController.calculateAccel(self._objects[i], self._objects[j])
            self._objects[i].addAccel(summaryAccel)
        for i in range(len(self._objects)):
            self._objects[i].calculateCoords()

    @staticmethod
    def calculateAccel(object1, object2):
        accel = Vector2(0.0, 0.0)
        deltaCoord = object2.getCoords() - object1.getCoords()
        accel.x = (GRAVITATION_CONSTANT * object2.getMass() * deltaCoord.x) / (deltaCoord.getLength()**3)
        accel.y = (GRAVITATION_CONSTANT * object2.getMass() * deltaCoord.y) / (deltaCoord.getLength()**3)
        return accel

    def initAll(self, screen):
        for i in range(len(self._objects)):
            self._objects[i].initDrawObject(screen)

    def drawAll(self, screen):
        for i in range(len(self._objects)):
            self._objects[i].drawObject(screen)

    def __str__(self):
        str=""
        for i in range(len(self._objects)):
            str += self._objects[i]._name + " "
        return str