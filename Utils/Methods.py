__author__ = 'PrimankaDEN'

from Utils.Vector2 import *
from Utils.Properties import *

RUNGE_KUTTA_4="Methods.RUNGE_KUTTA_4"
RUNGE_KUTTA_7="Methods.RUNGE_KUTTA_7"
EULER_METHOD ="Methods.EULER_METHOD"

class Methods:

    _coords=Vector2(0,0)
    _speed=Vector2(0,0)
    _accel=Vector2(0,0)


    def __init__(self, method, coords, speed, accel):
        self._coords=coords
        self._speed=speed
        self._accel=accel

        if (method==RUNGE_KUTTA_4):
            print 1
        elif (method==RUNGE_KUTTA_7):
            print 2
        elif (method==EULER_METHOD):
            print 3

    def eulerMethod(self):
        self._speed.x+=self._accel.x*DELTA_TIME
        self._speed.y+=self._accel.y*DELTA_TIME
        self._coords.x+=self._speed.x*DELTA_TIME
        self._coords.y+=self._speed.y*DELTA_TIME

    def rungeKutta4Method(self):
        1


    def getNewSpeed(self):
        return self._speed

    def getNewCoords(self):
        return self._coords

    def objectAccel(self, coord, speed):
        1
