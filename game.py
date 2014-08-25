__author__ = 'PrimankaDEN'

import pygame
from pygame import *
from Configs.Config import *

from SpaceObjects.SpaceObject import *
from SpaceObjects.SpaceObjectsController import *

#rMax = 0.0
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

    _screenOffsetX=0
    _screenOffsetY=0

    def __init__(self):
        self.startMainScreen()

    @staticmethod
    def resume():
        GameController.isStarted = True;

    @staticmethod
    def pause():
        GameController.isStarted = False;

    @staticmethod
    def isStarted():
        return GameController._isStarted

    @staticmethod
    def start():
        GameController.resume()

    def __init__(self):

        DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

        #Screen init
        pygame.init()
        self._screen = pygame.display.set_mode(DISPLAY)
        pygame.display.set_caption("Solar Mechanics v0.1")

        #Space init
        self._space = Surface(DISPLAY)
        self._space.fill(Color(SPACE_COLOR), None, 0)

        #Sun init
        sun = SpaceObject("Sun", "star", Vector2(0, 0), Vector2(0, 0))
        sun.setMass(5000)
        sun.setColor("yellow")
        sun.setSize(15)
        sun.setPositionFix(True)

        #Earth init
        earth = SpaceObject("Earth", "planet", Vector2(0, 300), Vector2(3, 0))
        earth.setMass(1000)
        earth.setColor("blue")
        earth.setSize(4)

        #Earth init
        earth2 = SpaceObject("Earth", "planet", Vector2(0, -100), Vector2(2, -3))
        earth2.setMass(1)
        earth2.setColor("blue")
        earth2.setSize(4)

        self._objects = SpaceObjectsController()
        self._objects.append(sun)
        self._objects.append(earth)
        self._objects.append(earth2)
        self._objects.initAll(self._screen)
        print self._objects
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
                        self._screenOffsetX-=5;
                    elif e.key == K_RIGHT:
                        self._screenOffsetX+=5;
                    elif e.key == K_DOWN:
                        self._screenOffsetY+=5;
                    elif e.key == K_UP:
                        self._screenOffsetY-=5;
                    elif  e.key == K_ESCAPE:
                        done =True


            if not IS_PATH_SHOWN:
                self._screen.blit(self._space, (0, 0))
            self._objects.setOffset(Vector2(self._screenOffsetX, self._screenOffsetY))
            self._objects.calculateAllAccels()
            self._objects.drawAll(self._screen)
            pygame.display.update()


controller = GameController()
controller.startMainScreen()