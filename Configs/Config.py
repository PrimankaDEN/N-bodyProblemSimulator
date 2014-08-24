__author__ = 'PrimankaDEN"'
import ConfigParser

from SpaceObjects.SpaceObjectsController import *
from SpaceObjects.SpaceObject import *


class Config:
    system="SYSTEM"
    type = "TYPE"
    x = "X"
    y = "Y"
    vx = "VX"
    vy = "VY"
    mass = "MASS"
    color = "COLOR"
    size = "SIZE"
    is_position_fixed = "IS_POSITION_FIXED"

    def __init__(self):
        self._parser = ConfigParser()

    def getObjectFromConfig(self, path, sectionName):
        object = SpaceObject(sectionName, self._parser[sectionName][self.type],
                             Vector2(int(self._parser[sectionName][self.x]),
                                     int(self._parser[sectionName][self.y])),
                             Vector2(int(self._parser[sectionName][self.vx]),
                                     int(self._parser[sectionName][self.vy])))
        object.setMass(int(self._parser[sectionName][self.mass]))
        object.setColor(self._parser[sectionName][self.color])
        object.setSize(self._parser[sectionName][self.size])
        object.setPositionFix(bool(self._parser[sectionName][self.is_position_fixed]))

        return object

    def getControllerFromConfig(self, path):
        self._parser.read(path)
        objects = SpaceObjectsController()

        for sel in self._parser.sections():
            if (sel != self.system):
                continue
            objects.append(self.getObjectFromConfig(path, sel))
        return objects

    def _pars(self, path):
        self._parser.read(path);
