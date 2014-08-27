__author__ = 'PrimankaDEN'

import pygame
from pygame import *
from Configs.Config import *

from math import *
from SpaceObjects.SpaceObject import *
from SpaceObjects.SpaceObjectsController import *

# rMax = 0.0
#rMin = 1000000.0
#rPrev = 0.0
#rPrevPrev = 0.0
#i = 0


#done = False
#while not done:
#    timer.tick(50)
#    for e in pygame.event.get():
#       if e.type == QUIT:
#           done = True
#           break

#r = (sun.getCoords() - earth.getCoords()).getLength()

#if r > rMax:
#    rMax = r
#    print "max ", rMax
#if r < rMin:
#    rMin = r
#    print "min ", rMin

#if r < rPrev and rPrev > rPrevPrev:
#    print "cur max ", rPrev, ", max ", rMax, ", delta ", rMax - rPrev
#if r > rPrev and rPrev < rPrevPrev:
#    print "cur min ", rPrev, ", min ", rMin

#rPrevPrev = rPrev
#rPrev = r


class GameController:
    _isStarted = False
    _objects = SpaceObjectsController()

    _screenOffsetX = 0
    _screenOffsetY = 0


    def __init__(self):

        DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

        #Screen init
        pygame.init()
        self._screen = pygame.display.set_mode(DISPLAY)
        pygame.display.set_caption("Solar Mechanics v0.1")

        #Space init
        self._space = Surface(DISPLAY)
        self._space.fill(Color(SPACE_COLOR), None, 0)

    def setObjectsController(self, controller):
        self._objects = controller

    def initToDraw(self):
        self._objects.initAll(self._screen)

    def addObject(self, object):
        self._objects.append(object)

    def startMainScreen(self):

        #Space init
        bg = Surface((WIN_WIDTH, WIN_HEIGHT))
        bg.fill(Color(SPACE_COLOR))
        #draw.circle (bg, Color(SUN_COLOR), (X0, Y0), 10)
        #Timer init
        timer = pygame.time.Clock()
        done = False
        while not done:

            for e in pygame.event.get():
                if e.type == QUIT:
                    done = True
                if e.type == KEYDOWN:
                    if e.key == K_LEFT:
                        self._screenOffsetX -= 5;
                    elif e.key == K_RIGHT:
                        self._screenOffsetX += 5;
                    elif e.key == K_DOWN:
                        self._screenOffsetY += 5;
                    elif e.key == K_UP:
                        self._screenOffsetY -= 5;
                    elif e.key == K_ESCAPE:
                        done = True

            if not IS_PATH_SHOWN:
                self._screen.blit(self._space, (0, 0))
            self._objects.setOffset(Vector2(self._screenOffsetX, self._screenOffsetY))
            self._objects.calculateAllAccels()
            self._objects.drawAll(self._screen)
            pygame.display.update()

    def setResistance(self, res):
        self._objects.setResistance(res)

controller = GameController()
parser = Config("Configs/main.ini")
controller.setObjectsController(parser.getControllerFromConfig())

number =100

for i in range(number):
    object = SpaceObject("star", "Star", Vector2(600 * sin(2*math.pi*i/number), 600*cos(2*math.pi*i/number)), Vector2(0, 0))
    object.setMass(-1000)
    object.setColor("yellow")
    object.setSize(10);
    object.setPositionFix(True)
    controller.addObject(object)

controller.setResistance(0.0001)
controller.initToDraw()
controller.startMainScreen()