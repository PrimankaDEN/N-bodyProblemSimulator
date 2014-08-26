__author__ = 'PrimankaDEN"'
from ConfigParser import *

from SpaceObjects.SpaceObjectsController import *
from SpaceObjects.SpaceObject import *


class Config:
    system = "SYSTEM"
    type = "TYPE"
    x = "X"
    y = "Y"
    vx = "VX"
    vy = "VY"
    mass = "MASS"
    color = "COLOR"
    size = "SIZE"
    is_position_fixed = "IS_POSITION_FIXED"
    _path = "Configs/main1.ini"

    def __init__(self, path):
        self._path=path
        self._parser = RawConfigParser()

    def getObjectFromConfig(self, sectionName):
        object = SpaceObject(sectionName, self._parser.get(sectionName,self.type),
                             Vector2(self._parser.getfloat(sectionName,self.x),
                                     self._parser.getfloat(sectionName,self.y)),
                             Vector2(self._parser.getfloat(sectionName,self.vx),
                                     self._parser.getfloat(sectionName,self.vy)))
        object.setMass(self._parser.getint(sectionName,self.mass))
        object.setColor(self._parser.get(sectionName,self.color))
        object.setSize(self._parser.getint(sectionName,self.size))
        object.setPositionFix(self._parser.getboolean(sectionName,self.is_position_fixed))
        return object

    def getControllerFromConfig(self):
        self._parser.readfp(open(self._path))
        objects = SpaceObjectsController()
        for sel in self._parser.sections():
            if (sel == self.system):
                continue
            objects.append(self.getObjectFromConfig(sel))
        return objects

    #def _pars(self, path):
    #    self._parser.read(path);
