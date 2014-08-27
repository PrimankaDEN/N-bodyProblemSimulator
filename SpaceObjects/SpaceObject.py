__author__ = 'PrimankaDEN'

from pygame import *

from Utils.Properties import *
from Utils.Vector2 import Vector2


class SpaceObject:
    _name = "Name"
    _type = "Planet"
    _mass = 0
    _speed = Vector2(0.0, 0.0)
    _coord = Vector2(0.0, 0.0)
    _accel = Vector2(0.0, 0.0)
    _color = "#FFFFFF"
    _size = 10
    _layoutSize = Vector2(1, 1)
    _isPositionFixed = False
    _isPathShown = IS_PATH_SHOWN
    _offset = Vector2(0, 0)

    def __init__(self, name, type, coordVector, speedVector):
        self._name = name
        self._type = type
        self._coord = coordVector
        self._speed = speedVector

    def setCoords(self, coordVector):
        self._coord = coordVector

    def getCoords(self):
        return self._coord

    def setSpeed(self, speedVector):
        self._speed = speedVector

    def getSpeed(self):
        return self._speed

    def getModSpeed(self):
        return self._speed.getLength()

    def setColor(self, color):
        self._color = color

    def setPositionFix(self, isFixed):
        self._isPositionFixed = isFixed

    def isPositionFixed(self):
        return self._isPositionFixed

    # acceleration
    def addAccel(self, accelArg):
        self._accel = accelArg

    def calculateCoords(self):
        if not self._isPositionFixed:
            accel = self._accel
            self._speed.x += accel.x * DELTA_TIME
            self._speed.y += accel.y * DELTA_TIME
            self._coord.x += self._speed.x * DELTA_TIME
            self._coord.y += self._speed.y * DELTA_TIME

    def setSize(self, size):
        self._size = size

    # def setLayoutSize(self, layoutSize):
    #    self._layoutSize = layoutSize

    def setMass(self, mass):
        self._mass = mass

    def getMass(self):
        return self._mass

    def setPathShow(self, isPathShown):
        self._isPathShown = isPathShown

    def initDrawObject(self, screen):
        if self._layoutSize == Vector2(0, 0):
            self._layoutSize = Vector2(self._size, self._size)

        self.__planet = Surface((self._layoutSize.x, self._layoutSize.y))
        self.__planet.fill(Color(SPACE_COLOR))
        if not IS_PATH_SHOWN:
            draw.circle(self.__planet,
                        Color(self._color),
                        (self._layoutSize.x, self._layoutSize.y), self._size)
        else:
            draw.circle(self.__planet,
                        Color(self._color),
                        (self._layoutSize.x, self._layoutSize.x), self._size)
        screen.blit(self.__planet, (X0 + int(self._coord.x * SCALE), Y0 + int(self._coord.y * SCALE)))

    def drawObject(self, screen):
        screen.blit(self.__planet, (X0 + int(self._coord.x * SCALE), Y0 + int(self._coord.y * SCALE)))

    def drawObjectWithOffset(self, screen, offset):
        screen.blit(self.__planet,
                    (X0 + offset.x + int(self._coord.x * SCALE), Y0 + offset.y + int(self._coord.y * SCALE)))

    def calculateResistance(self, resistance):
        speed = self.getSpeed()
        speed.x*=1.0-resistance
        speed.y*=1.0-resistance
        self.setSpeed(speed)