__author__ = 'PrimankaDEN'

import pygame
from pygame import *

from SpaceObjects.SpaceObject import *
from SpaceObjects.SpaceObjectsController import *


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
screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("Solar Mechanics v0.1")

#Space init
space = Surface(DISPLAY)
space.fill(Color(SPACE_COLOR),None,0)

#Sun init
sun = SpaceObject("Sun", "star", Vector2(0,0 ), Vector2(0, 0))
sun.setMass(5000)
sun.setColor("yellow")
sun.setSize(15)
sun.initDrawObject(screen)
sun.setPositionFix(True)

#Earth init
earth = SpaceObject("Earth", "planet", Vector2(200, 200), Vector2(3, -3))
earth.setMass(500)
earth.setColor("blue")
earth.setSize(PLANET_SIZE)
earth.initDrawObject(screen)

#Moon init
moon = SpaceObject("Moon", "planet", Vector2(-200, -200), Vector2(-3, 3))
moon.setMass(500)
moon.setColor("gray")
moon.setSize(4)
moon.initDrawObject(screen)

objects = SpaceObjectController()
objects.append(sun)
objects.append(earth)
objects.append(moon)
objects.initAll(screen)


def startMainScreen():
    #Space init
    bg = Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(Color(SPACE_COLOR))
    #draw.circle (bg, Color(SUN_COLOR), (X0, Y0), 10)
    sun.drawObject(screen)
    earth.drawObject(screen)
    #Timer init
    timer = pygame.time.Clock()
    done = False
    while not done:
        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == K_ESCAPE:
                done = True
                break

        if not IS_PATH_SHOWN:
            screen.blit(space, (0, 0))
        objects.calculateAllAccels()
        objects.drawAll(screen)
        pygame.display.update()


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



startMainScreen()
