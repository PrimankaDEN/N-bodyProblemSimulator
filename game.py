__author__ = 'PrimankaDEN'

import pygame
from pygame import *

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
    _objects = SpaceObjectController()

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
        PLANET_SIZE = 7

        #Sun position

        #Sun mass
        M0 = 5000
        #Stop conditions
        CRASH_DIST = 10
        OUT_DIST = 1000

        #Screen init
        pygame.init()
        self._screen = pygame.display.set_mode(DISPLAY)
        pygame.display.set_caption("Solar Mechanics v0.1")

        #Space init
        self._space = Surface(DISPLAY)
        self._space.fill(Color(SPACE_COLOR), None, 0)

        #Sun init
        sun = SpaceObject("Sun", "star", Vector2(500, 0), Vector2(0, 3))
        sun.setMass(5000)
        sun.setColor("yellow")
        sun.setSize(15)
        #sun.setPositionFix(True)

        #Sun2 init
        sun2 = SpaceObject("Sun", "star", Vector2(-500, 0), Vector2(0, -3))
        sun2.setMass(5000)
        sun2.setColor("yellow")
        sun2.setSize(15)
        #sun2.setPositionFix(True)

        #Sun3 init
        sun3 = SpaceObject("Sun", "star", Vector2(0, 0), Vector2(0, -7))
        sun3.setMass(5000)
        sun3.setColor("yellow")
        sun3.setSize(15)
        sun3.setPositionFix(True)

        #Earth init
        earth = SpaceObject("Earth", "planet", Vector2(0, 100), Vector2(7, 1))
        earth.setMass(1)
        earth.setColor("blue")
        earth.setSize(4)

        #Moon init
        moon = SpaceObject("Moon", "planet", Vector2(100, -200), Vector2(1, 2))
        moon.setMass(20)
        moon.setColor("gray")
        moon.setSize(4)

        objects = SpaceObjectController()
        objects.append(sun)
        objects.append(sun2)
        objects.append(sun3)
        objects.append(earth)
        #objects.append(moon)
        objects.initAll(self._screen)

    def startMainScreen(self):

        #Space init
        bg = Surface((WIN_WIDTH, WIN_HEIGHT))
        bg.fill(Color(SPACE_COLOR))
        #draw.circle (bg, Color(SUN_COLOR), (X0, Y0), 10)

        #Timer init
        timer = pygame.time.Clock()
        done = False
        while GameController.isStarted():
            for e in pygame.event.get():
                if e.type == QUIT or e.type == KEYDOWN and e.key == K_ESCAPE:
                    done = True
                    break

            if not IS_PATH_SHOWN:
                self._screen.blit(self._space, (0, 0))
            self._objects.calculateAllAccels()
            self._objects.drawAll(self._screen)
            pygame.display.update()
