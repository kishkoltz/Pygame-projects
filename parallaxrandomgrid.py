# E:\ppython\app\python.exe parallaxrandomgrid.py

import pygame, sys, time, random
from pygame.locals import *

pygame.init()

SMALLSQUARESIDE = 20
SMALLSQUAREGAP = 30
crosshairx = 10
crosshairy = 10
WINDOWWIDTH = 333
WINDOWHEIGHT = 333
squareField = (0, 0, 0, 0)
squaresXmultiplier = 0
squaresYmultiplier = 0
squaresXmultiplierInside = 0
squaresYmultiplierInside = 0
grid = []
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Aim Squares')

eatables = []

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
    for l in range(4):
        grid.append([])
        for x in range(blocksHorizontally):
            for y in range(blocksVertically):
                grid[l].append([x*blocksVertically+y])
                grid[l][x*blocksVertically+y] = (
                SMALLSQUAREGAP + (3-l)*SMALLSQUAREGAP + x *
                ((1+l)*0.25*SMALLSQUARESIDE + (1+l)*0.25*SMALLSQUAREGAP),
                SMALLSQUAREGAP+ (3-l)*SMALLSQUAREGAP + y *
                ((1+l)*0.25*SMALLSQUARESIDE + (1+l)*0.25*SMALLSQUAREGAP),
                (1+l)*0.25*SMALLSQUARESIDE,
                (4-l)*0.25,
                (0, 10 + 50 * l, 0)
                )

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


    # random display
    for l in range(len(grid)):
        for s in range(random.choice(range(len(grid[l])))):
            pygame.draw.rect(windowSurface, grid[l][0][4],
            (grid[l][random.choice(range(len(grid[l])))][0] + crosshairx*grid[l][0][3],
            grid[l][random.choice(range(len(grid[l])))][1] + crosshairy*grid[l][0][3],
            grid[l][0][2],grid[l][0][2]))
    '''
    # constant display
    for l in range(len(grid)):
        for g in range(len(grid[l])):
            pygame.draw.rect(windowSurface, grid[l][g][4],
            ((grid[l][g][0] + crosshairx*grid[l][g][3]),
            grid[l][g][1] + crosshairy*grid[l][g][3],
            grid[l][g][2],
            grid[l][g][2]))
    '''
    pygame.display.update()
    time.sleep(0.02)
