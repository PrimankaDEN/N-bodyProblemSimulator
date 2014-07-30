__author__ = 'PrimankaDEN'

from Vector2 import Vector2
from Properties import *


class GravitationController:
    _objects = []

    def __init__(self):
        return 0

    def addObject(self, object):
        self._objects.append(object)

    def calculateAllAccels(self):
        for i in range(len(self._object)):
            accel = Vector2(0, 0)
            for j in range(len(self._object)):
                if i == j:
                    continue
                delta = Vector2.getDelta(self._objects[i].getCoords(), self._objects[j].getCoords())
                accel.add(GravitationController.calculateAccel(delta, self._objects[j].getMass()))
            self._objects[i].addAccel(accel)

    @staticmethod
    def calculateAccel(deltaCorrd, mass):
        force = Vector2(0, 0)
        force.x = GRAVITATION_CONSTANT * mass * (deltaCorrd.x / deltaCorrd.getLength())
        force.y = GRAVITATION_CONSTANT * mass * (deltaCorrd.y / deltaCorrd.getLength())
        return force