__author__ = 'Home'

from Utils.Vector2 import *
from Utils.Properties import *


class SpaceObjectsController:
    _objects = []
    _offset = Vector2(0, 0)
    _resistanse=0.0

    def __init__(self):
        self._objects = []

    def __getitem__(self, item):
        return self._objects[item]

    def __setitem__(self, key, value):
        self._objects[key] = value

    def setOffset(self, offset):
        self._offset = offset

    def append(self, value):
        self._objects.append(value)

    def calculateAllAccels(self):
        for i in range(len(self._objects)):
            if self._objects[i].isPositionFixed():
                continue
            summaryAccel = Vector2(0.0, 0.0)
            for j in range(len(self._objects)):
                if i == j:
                    continue
                summaryAccel = summaryAccel + SpaceObjectsController.calculateAccel(self._objects[i], self._objects[j])
            self._objects[i].addAccel(summaryAccel)
            self._objects[i].calculateResistance(self._resistanse)
        for i in range(len(self._objects)):
            self._objects[i].calculateCoords()

    @staticmethod
    def calculateAccel(object1, object2):
        accel = Vector2(0.0, 0.0)
        deltaCoord = object2.getCoords() - object1.getCoords()
        accel.x = (GRAVITATION_CONSTANT * object2.getMass() * deltaCoord.x) / (deltaCoord.getLength() ** 3)
        accel.y = (GRAVITATION_CONSTANT * object2.getMass() * deltaCoord.y) / (deltaCoord.getLength() ** 3)
        return accel

    def initAll(self, screen):
        for i in range(len(self._objects)):
            self._objects[i].initDrawObject(screen)

    def drawAll(self, screen):
        for i in range(len(self._objects)):
            self._objects[i].drawObjectWithOffset(screen, self._offset)

    def __str__(self):
        str = ""
        for i in range(len(self._objects)):
            str += self._objects[i]._name + " "
        return str

    def setResistance(self,res):
        self._resistanse=res