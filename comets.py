# E:\ppython\app\python.exe comets.py

import pygame, sys, time, random
from pygame.locals import *

pygame.init()

SMALLSQUARESIDE = 20
SMALLSQUAREGAP = 30
crosshairx = 10
crosshairy = 10
WINDOWWIDTH = 333
WINDOWHEIGHT = 333
grid = []
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Comets')
comets = []

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def defineSquareField():
    global squareField
    squareField = (crosshairx - 41, crosshairy - 41, crosshairx + 41, crosshairy + 41)

def setGrid():
    global WINDOWWIDTH, WINDOWHEIGHT
    blocksHorizontally = int(WINDOWWIDTH / (SMALLSQUARESIDE + SMALLSQUAREGAP))
    blocksVertically = int(WINDOWHEIGHT / (SMALLSQUARESIDE + SMALLSQUAREGAP))
    for x in range(blocksHorizontally):
        for y in range(blocksVertically):
            grid.append([x*blocksVertically+y])
            grid[x*blocksVertically+y] = (
            SMALLSQUAREGAP + 3*SMALLSQUAREGAP + x *
            (0.1*SMALLSQUARESIDE + 0.1*SMALLSQUAREGAP),
            SMALLSQUAREGAP+ 3*SMALLSQUAREGAP + y *
            (0.1*SMALLSQUARESIDE + 0.1*SMALLSQUAREGAP),
            0.1*SMALLSQUARESIDE,
            1,
            20
            )

def moveComets():
    global comets
    if len(comets) >= 1:
        for c in range(len(comets)):
            comets[c] = (comets[c][0] - 2,
            comets[c][1] - 2,
            comets[c][2] + 4,
            comets[c][3] - 0.05,
            comets[c][4] + 5)
        if comets[0][3] < 0:
            comets.pop(0)

def addComets():
    global comets
    comets.append([])
    comets[len(comets)-1] = grid[random.randint(0,len(grid)-1)]

setGrid()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            crosshairx = WINDOWWIDTH / 2 - event.pos[0]
            crosshairy = WINDOWHEIGHT / 2 - event.pos[1]
    windowSurface.fill(BLACK)

    defineSquareField()
    moveComets()
    if random.randint(0, 50) > 49:
        addComets()
    for c in range(len(comets)):
        pygame.draw.rect(windowSurface, (comets[c][4], 0, 0),
        ((comets[c][0] + crosshairx*comets[c][3]),
        comets[c][1] + crosshairy*comets[c][3],
        comets[c][2],
        comets[c][2]))

    pygame.display.update()
    time.sleep(0.02)
