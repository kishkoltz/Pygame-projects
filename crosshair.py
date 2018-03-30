# E:\ppython\app\python.exe crosshair.py

import pygame, sys, time, random
from pygame.locals import *

pygame.init()
minusrange = (-4, -3, -2)
plusrange = (2, 3, 4)
directionrange = (plusrange, minusrange)
directionx = random.choice(random.choice(directionrange))
directiony = random.choice(random.choice(directionrange))
SMALLSQUARESIDE = 40
SMALLSQUAREGAP = 20
crosshairx = 95
crosshairy = 95
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
#smallsquareswide = 0
#smallsquareshigh = 0
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Four Rectangles')

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#generic tile database
b1a = {'rect': pygame.Rect (0, 0, 1, 1), 'color': GREEN}
b1b = {'rect': pygame.Rect (1, 1, 1, 1), 'color': GREEN}
b2a = {'rect': pygame.Rect (0, 1, 1, 1), 'color': GREEN}
b2b = {'rect': pygame.Rect (1, 0, 1, 1), 'color': GREEN}
blocks = [b1b, b2a, b2b]

def setdirection():
    global crosshairx, crosshairy, directionx, directiony
    #check X boundaries:
    if crosshairx < 10:
        directionx = random.choice(plusrange)
    elif crosshairx > WINDOWWIDTH - 20:
        directionx = random.choice(minusrange)
    #check y boundaries
    if crosshairy < 10:
        directiony = random.choice(plusrange)
    elif crosshairy > WINDOWHEIGHT - 20:
        directiony = random.choice(minusrange)
def movecrosshair():
    global crosshairx, crosshairy, directionx, directiony
    crosshairx += directionx
    crosshairy += directiony

def settiles():
    global b1a, b1b, b2a, b2b
    b1a['rect'] = (5, 5, crosshairx, crosshairy)
    #downright
    b1b['rect'] = ((crosshairx + 10), (crosshairy + 10), (WINDOWWIDTH - crosshairx - 15), (WINDOWHEIGHT - crosshairy - 15))
    #upright
    b2a['rect'] = ((crosshairx + 10), 5, (WINDOWWIDTH - crosshairx - 15), crosshairy)
    #downleft
    b2b['rect'] = (5, (crosshairy + 10), crosshairx, (WINDOWHEIGHT - crosshairy - 15))

def setsmalltiles():
    #global smallsquareswide, smallsquareshigh
    #divide width by smallsquarewidth + smallsquare gap
    b1awide = float((crosshairx+SMALLSQUAREGAP)/(SMALLSQUARESIDE + SMALLSQUAREGAP))
    b1ahigh = float((crosshairy+SMALLSQUAREGAP)/(SMALLSQUARESIDE + SMALLSQUAREGAP))
    b2awide = float((WINDOWWIDTH - crosshairx - 15 + SMALLSQUAREGAP)/(SMALLSQUARESIDE + SMALLSQUAREGAP))
    b2ahigh = float((WINDOWHEIGHT - crosshairy - 15 + SMALLSQUAREGAP)/(SMALLSQUARESIDE + SMALLSQUAREGAP))
    #print ("%s small squares can be fit horizontally into the topleft rectangle" % smallsquareswide)
    #print ("%s small squares can be fit vertically into the topleft rectangle" % smallsquareshigh)
    #for wide:
    #for high:
    #draw line of squares, one under another
    b1axrest = ((crosshairx+SMALLSQUAREGAP)%(SMALLSQUARESIDE + SMALLSQUAREGAP)-SMALLSQUAREGAP)
    b1ayrest = ((crosshairy+SMALLSQUAREGAP)%(SMALLSQUARESIDE + SMALLSQUAREGAP)-SMALLSQUAREGAP)
    for x in range(int(b1awide)):
        for y in range(int(b1ahigh)):
            pygame.draw.rect(windowSurface, GREEN, (5+x*(SMALLSQUARESIDE+SMALLSQUAREGAP), 5+y*(SMALLSQUARESIDE+SMALLSQUAREGAP), SMALLSQUARESIDE, SMALLSQUARESIDE))
#    for s in range(int(b2awide)):
#        for a in range(int(b2ahigh)):
#            pygame.draw.rect(windowSurface, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (WINDOWWIDTH-5-SMALLSQUARESIDE-s*(SMALLSQUARESIDE+SMALLSQUAREGAP), WINDOWHEIGHT-5-SMALLSQUARESIDE-a*(SMALLSQUARESIDE+SMALLSQUAREGAP), SMALLSQUARESIDE, SMALLSQUARESIDE))
    if b1axrest > 0:
        for y in range(int(b1ahigh)):
            pygame.draw.rect(windowSurface, GREEN, (5+b1awide*(SMALLSQUARESIDE+SMALLSQUAREGAP),5+y*(SMALLSQUARESIDE+SMALLSQUAREGAP)+(SMALLSQUARESIDE-b1axrest)/2, b1axrest, b1axrest))
    if b1ayrest > 0:
        for o in range(int(b1awide)):
            pygame.draw.rect(windowSurface, GREEN, (5+o*(SMALLSQUARESIDE+SMALLSQUAREGAP)+(SMALLSQUARESIDE-b1ayrest)/2,5+b1ahigh*(SMALLSQUARESIDE+SMALLSQUAREGAP), b1ayrest, b1ayrest))
    if b1axrest > 0 and b1ayrest > 0:
        if b1axrest < b1ayrest:
            pygame.draw.rect(windowSurface, GREEN, (5+b1awide*(SMALLSQUARESIDE+SMALLSQUAREGAP),5+b1ahigh*(SMALLSQUARESIDE+SMALLSQUAREGAP), b1axrest, b1axrest))
        else:
            pygame.draw.rect(windowSurface, GREEN, (5+b1awide*(SMALLSQUARESIDE+SMALLSQUAREGAP),5+b1ahigh*(SMALLSQUARESIDE+SMALLSQUAREGAP), b1ayrest, b1ayrest))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            crosshairx = event.pos[0]-7
            crosshairy = event.pos[1]-7
    windowSurface.fill(BLACK)
    setdirection()
    #movecrosshair()
    settiles()
    for b in blocks:
        pygame.draw.rect(windowSurface, b['color'], b['rect'])
    setsmalltiles()
    #b1a['rect'].width += random.randint(-2,2)
    #b1a['rect'].height += random.randint(-2,2)
    #pygame.draw.rect(windowSurface, b1a['color'], b1a['rect'])
    #pygame.draw.rect(windowSurface, RED, ((b1a['rect'].width + 10), (b1a['rect'].height + 10), (WINDOWWIDTH - b1a['rect'].width - 15), (WINDOWHEIGHT - b1a['rect'].height - 15)))
    pygame.display.update()
    time.sleep(0.02)
