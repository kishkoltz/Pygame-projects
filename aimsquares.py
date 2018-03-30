# E:\ppython\app\python.exe aimsquares.py

import pygame, sys, time, random
from pygame.locals import *

pygame.init()

SMALLSQUARESIDE = 20
SMALLSQUAREGAP = 10
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

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
'''
1. establish aimsquare boundary
2. set a grid of top-left and down-right square corners
3. verify which fields from the grid fully fit in the aimsquare and draw them
'''
def defineSquareField(): # 1 completed
    global squareField
    squareField = (crosshairx - 41, crosshairy - 41, crosshairx + 41, crosshairy + 41)

def setGrid():
    global WINDOWWIDTH, WINDOWHEIGHT
    #print("x: %s, y: %s" % (WINDOWWIDTH, WINDOWHEIGHT))
    blocksHorizontally = int(WINDOWWIDTH / (SMALLSQUARESIDE + SMALLSQUAREGAP))
    #WINDOWWIDTH = (blocksHorizontally * (SMALLSQUARESIDE + SMALLSQUAREGAP))
    blocksVertically = int(WINDOWHEIGHT / (SMALLSQUARESIDE + SMALLSQUAREGAP))
    #WINDOWHEIGHT = (blocksVertically * (SMALLSQUARESIDE + SMALLSQUAREGAP))
    #print("Correction - x: %s, y: %s" % (WINDOWWIDTH, WINDOWHEIGHT))

    #input("There will be %s squares horizontally and %s vertically." % (blocksHorizontally, blocksVertically))
    for x in range(blocksHorizontally):
        for y in range(blocksVertically):
            grid.append([x*blocksVertically+y])
            grid[x*blocksVertically+y] = ((SMALLSQUAREGAP + x * (SMALLSQUARESIDE + SMALLSQUAREGAP)),
            (SMALLSQUAREGAP + y * (SMALLSQUARESIDE + SMALLSQUAREGAP)),
            (SMALLSQUAREGAP + SMALLSQUARESIDE + x * (SMALLSQUARESIDE + SMALLSQUAREGAP)),
            (SMALLSQUAREGAP + SMALLSQUARESIDE + y * (SMALLSQUARESIDE + SMALLSQUAREGAP)))

def drawFullSquares():
    for s in range(len(grid)):
        if grid[s][0] >= squareField[0]\
        and grid[s][1] >= squareField[1]\
        and grid[s][2] <= squareField[2]\
        and grid[s][3] <= squareField[3]:
            pygame.draw.rect(windowSurface, RED,
            (grid[s][0], grid[s][1], SMALLSQUARESIDE, SMALLSQUARESIDE))

def drawBorderSquares():
    for s in range(len(grid)):
        #left side: WORKS
        if grid[s][0] < squareField[0]\
        and grid[s][1] >= squareField[1]\
        and grid[s][2] >= squareField[0]\
        and grid[s][2] < squareField[0] + SMALLSQUARESIDE\
        and grid[s][3] <= squareField[3]:
            pygame.draw.rect(windowSurface, RED,
            (squareField[0], grid[s][1] + (squareField[0] - grid[s][0])/2,
            grid[s][2] - squareField[0],
            grid[s][2] - squareField[0]))
        #Top side: WORKS
        if grid[s][0] >= squareField[0]\
        and grid[s][1] < squareField[1]\
        and grid[s][2] <= squareField[2]\
        and grid[s][3] >= squareField[1]\
        and grid[s][3] < squareField[1] + SMALLSQUARESIDE:
            pygame.draw.rect(windowSurface, RED,
            (grid[s][0] + (squareField[1] - grid[s][1])/2, squareField[1],
            grid[s][3] - squareField[1],
            grid[s][3] - squareField[1]))
        #Right side: WORKS
        if grid[s][0] <= squareField[2]\
        and grid[s][2] < squareField[2] + SMALLSQUARESIDE\
        and grid[s][1] >= squareField[1]\
        and grid[s][2] > squareField[2]\
        and grid[s][3] <= squareField[3]:
            pygame.draw.rect(windowSurface, RED,
            (grid[s][0], grid[s][1] + (grid[s][2] - squareField[2])/2,
            squareField[2] - grid[s][0],
            squareField[2] - grid[s][0]))
        #Bottom side: WORKS
        if grid[s][0] >= squareField[0]\
        and grid[s][1] < squareField[3]\
        and grid[s][2] <= squareField[2]\
        and grid[s][3] > squareField[3]:
            pygame.draw.rect(windowSurface, RED,
            (grid[s][0]+ (grid[s][3] - squareField[3])/2, grid[s][1],
            squareField[3] - grid[s][1],
            squareField[3] - grid[s][1]))
        #Top-left corner: SO SO
        if grid[s][0] < squareField[0]\
        and grid[s][1] < squareField[1]\
        and grid[s][2] > squareField[0]\
        and grid[s][2] < squareField[0] + SMALLSQUARESIDE\
        and grid[s][3] > squareField[1]\
        and grid[s][3] < squareField[1] + SMALLSQUARESIDE:
            if grid[s][2] - squareField[0] < grid[s][3] - squareField[1]:
                pygame.draw.rect(windowSurface, RED,
                (squareField[0], squareField[1],
                grid[s][2] - squareField[0],
                grid[s][2] - squareField[0]))
            else:
                pygame.draw.rect(windowSurface, RED,
                (squareField[0], squareField[1],
                grid[s][3] - squareField[1],
                grid[s][3] - squareField[1]))
        #Top-right corner: so so
        if grid[s][0] < squareField[2]\
        and grid[s][0] > squareField[2] - SMALLSQUARESIDE\
        and grid[s][1] < squareField[1]\
        and grid[s][2] > squareField[2]\
        and grid[s][3] > squareField[1]\
        and grid[s][3] < squareField[1] + SMALLSQUARESIDE:
            #GET THE SQUAREFIELD TOP-RIGHT coordinates
            if squareField[2] - grid[s][0] < grid[s][3] - squareField[1]:
                pygame.draw.rect(windowSurface, RED,
                (grid[s][0],
                squareField[1],
                squareField[2] - grid[s][0],
                squareField[2] - grid[s][0]))
            else:
                pygame.draw.rect(windowSurface, RED,
                (squareField[2] - (grid[s][3] - squareField[1]),
                squareField[1],
                grid[s][3] - squareField[1],
                grid[s][3] - squareField[1]))
        #bottom-left corner: okay
        if grid[s][0] < squareField[0]\
        and grid[s][0] > squareField[0] - SMALLSQUARESIDE\
        and grid[s][1] < squareField[3]\
        and grid[s][2] > squareField[0]\
        and grid[s][3] > squareField[3]\
        and grid[s][3] < squareField[3] + SMALLSQUARESIDE:
            if grid[s][2] - squareField[0] < squareField[3] - grid[s][1]:
                pygame.draw.rect(windowSurface, RED,
                (squareField[0], squareField[3] - (grid[s][2] - squareField[0]),
                grid[s][2] - squareField[0],
                grid[s][2] - squareField[0]))
            else:
                pygame.draw.rect(windowSurface, RED,
                (squareField[0], grid[s][1],
                squareField[3] - grid[s][1],
                squareField[3] - grid[s][1]))
        #Bottom-right corner: okay
        if grid[s][0] < squareField[2]\
        and grid[s][0] > squareField[2] - SMALLSQUARESIDE\
        and grid[s][1] < squareField[3]\
        and grid[s][1] > squareField[3] - SMALLSQUARESIDE\
        and grid[s][2] > squareField[2]\
        and grid[s][3] > squareField[3]:
            #GET THE SQUAREFIELD BOTTOM-RIGHT coordinates
            if squareField[2] - grid[s][0] < squareField[3] - grid[s][1]:
                pygame.draw.rect(windowSurface, RED,
                (grid[s][0],
                squareField[3] - (squareField[2] - grid[s][0]),
                squareField[2] - grid[s][0],
                squareField[2] - grid[s][0]))
            else:
                pygame.draw.rect(windowSurface, RED,
                (squareField[2] - (squareField[3] - grid[s][1]),
                grid[s][1],
                squareField[3] - grid[s][1],
                squareField[3] - grid[s][1]))

setGrid()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            crosshairx = int(event.pos[0])
            crosshairy = int(event.pos[1])
    windowSurface.fill(BLACK)
    defineSquareField()
    '''
    for s in range(random.choice(range(len(grid)))):
        pygame.draw.rect(windowSurface, GREEN, (grid[random.choice(range(len(grid)))][0], grid[random.choice(range(len(grid)))][1], SMALLSQUARESIDE, SMALLSQUARESIDE))
    '''
    drawFullSquares()
    drawBorderSquares()
    pygame.display.update()
    time.sleep(0.02)
