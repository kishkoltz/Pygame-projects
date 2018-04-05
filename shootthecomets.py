# E:\ppython\app\python.exe shootthecomets.py

import pygame, sys, time, random
from pygame.locals import *

'''
Okay, it seems it's gonna be a space shooter after all. Things to do:

1. Generate a nebula on a startup. It's gonna have a random shape and gonna be
twinkling STATUS: something's there, not very nebula-like
2. Strands of nebula should pass the player by so that it suggests we're
getting closer
3. In the bottom-left corner there could be the starship's nose,
perhaps seen through some cockpit window
4. Enemy ships would overtake the player and stop some distance ahead so that
they can be shot down
'''

pygame.init()

SMALLSQUARESIDE = 5
SMALLSQUAREGAP = 5
crosshairx = 10
crosshairy = 10
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
grid = []
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Comets')
comets = []
tunnel = []
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
blocksHorizontally = 0
blocksVertically = 0
nebula = []
nebulaRim = []
randomNebula = []
cometsFarAway = []
def setGrid():
    global WINDOWWIDTH, WINDOWHEIGHT, blocksHorizontally, blocksVertically
    blocksHorizontally = int(WINDOWWIDTH / (SMALLSQUARESIDE + SMALLSQUAREGAP))
    blocksVertically = int(WINDOWHEIGHT / (SMALLSQUARESIDE + SMALLSQUAREGAP))
    for x in range(blocksHorizontally):
        for y in range(blocksVertically):
            grid.append([x*blocksVertically+y])
            grid[x*blocksVertically+y] = (
            SMALLSQUAREGAP + x *
            (SMALLSQUARESIDE + SMALLSQUAREGAP),
            SMALLSQUAREGAP + y *
            (SMALLSQUARESIDE + SMALLSQUAREGAP),
            SMALLSQUARESIDE,
            1,
            20
            )
def drawGrid():
    for s in range(random.choice(range(len(grid)))):
        pygame.draw.rect(windowSurface, BLACK,
        (grid[random.choice(range(len(grid)))][0],
        grid[random.choice(range(len(grid)))][1],
        SMALLSQUARESIDE, SMALLSQUARESIDE))
def getNebula():
        for x in range(WINDOWWIDTH):
            for y in range(WINDOWHEIGHT):
                if (x - (WINDOWWIDTH/2))**2 + (y - WINDOWHEIGHT/2)**2 < 20**2:
                    nebula.append([])
                    nebula[len(nebula)-1] = (x, y)
                if (x - (WINDOWWIDTH/2))**2 + (y - WINDOWHEIGHT/2)**2 == (WINDOWHEIGHT/2)**2 or (x - (WINDOWWIDTH/2))**2 + (y - WINDOWHEIGHT/2)**2 == (WINDOWHEIGHT/2-1)**2:
                    nebulaRim.append([])
                    nebulaRim[len(nebulaRim)-1] = (x, y, SMALLSQUARESIDE, 1, 20)
        for n in range(len(nebula)/20):
            randomNebula.append(random.randint(0,len(nebula)))

def createTunnel():
    global tunnel
    if len(tunnel) == 0:
        tunnel.append([0])
        tunnel[0] = (WINDOWWIDTH/2-(blocksHorizontally*
        (0.1*SMALLSQUARESIDE + 0.1*SMALLSQUAREGAP)/2),
        WINDOWHEIGHT/2 - (blocksVertically*
        (0.1*SMALLSQUARESIDE + 0.1*SMALLSQUAREGAP)/2),
        blocksHorizontally*(0.1*SMALLSQUARESIDE + 0.1*SMALLSQUAREGAP),
        blocksVertically*(0.1*SMALLSQUARESIDE + 0.1*SMALLSQUAREGAP), 1, 0)
    else:
        for t in range(len(tunnel)):
            tunnel[t] = (tunnel[t][0]-10,
            tunnel[t][1] -10,
            tunnel[t][2] + 20,
            tunnel[t][3] + 20,
            tunnel[t][4] - 0.05,
            tunnel[t][5] + 5)
        tunnel.append([len(tunnel)])
        tunnel[len(tunnel)-1] = (WINDOWWIDTH/2-(blocksHorizontally*
        (0.1*SMALLSQUARESIDE + 0.1*SMALLSQUAREGAP)/2),
        WINDOWHEIGHT/2 - (blocksVertically*
        (0.1*SMALLSQUARESIDE + 0.1*SMALLSQUAREGAP)/2),
        blocksHorizontally*(0.1*SMALLSQUARESIDE + 0.1*SMALLSQUAREGAP),
        blocksVertically*(0.1*SMALLSQUARESIDE + 0.1*SMALLSQUAREGAP), 1, 0)

    if tunnel[0][2] > 500 or tunnel[0][3] > 500:
            tunnel.pop(0)
def drawTunnel():
    for t in range(len(tunnel)):
        pygame.draw.rect(windowSurface, (0, tunnel[t][5],0),
        (tunnel[t][0] + crosshairx*tunnel[t][4],
        tunnel[t][1] + crosshairy*tunnel[t][4],
        tunnel[t][2], tunnel[t][3]))
def addComets():
    global comets
    for s in range(random.randint(1, 20)):
        if random.randint(0, 50) > 15:
            choice = random.randint(0,len(grid)-1)
            comets.append([])
            comets[len(comets)-1] = \
            (WINDOWWIDTH/2-grid[choice][0],
            WINDOWHEIGHT/2-grid[choice][1],
            grid[choice][2],
            grid[choice][3], grid[choice][4], 0.04)
def addCometsFarAway():
    global cometsFarAway
    #for s in range(random.randint(1, 20)):
    if random.randint(0, 50) > 49:
        choice = random.randint(0,len(nebulaRim)-1)
        cometsFarAway.append([])
        cometsFarAway[len(cometsFarAway)-1] = \
        (WINDOWWIDTH/2-nebulaRim[choice][0],
        WINDOWWIDTH/2-nebulaRim[choice][1],
        nebulaRim[choice][2]*2,
        nebulaRim[choice][3], nebulaRim[choice][4], 0.09)
def moveComets():
    global comets
    if len(comets) >= 1:
        for c in range(len(comets)):
            comets[c] = (comets[c][0],
            comets[c][1],
            comets[c][2],
            comets[c][3] - 0.05,
            comets[c][4] + 5,
            comets[c][5] + 0.04)
        for x in comets[:]:
            if x[5] >= 1:
                comets.remove(x)
def moveCometsFarAway():
    global cometsFarAway
    if len(cometsFarAway) >= 1:
        for c in range(len(cometsFarAway)):
            cometsFarAway[c] = (cometsFarAway[c][0],
            cometsFarAway[c][1],
            cometsFarAway[c][2],
            cometsFarAway[c][3],
            cometsFarAway[c][4] + 5,
            cometsFarAway[c][5] * 1.01)
        for x in cometsFarAway[:]:
            if x[5] >= 2:
                cometsFarAway.remove(x)
def drawComets():
    for c in range(len(comets)):
        pygame.draw.rect(windowSurface, (comets[c][4], comets[c][4], comets[c][4]),
        ((WINDOWWIDTH/2 - (comets[c][5] * comets[c][0]) + crosshairx*comets[c][3]),
        WINDOWHEIGHT/2 - (comets[c][5] * comets[c][1]) + crosshairy*comets[c][3],
        comets[c][2]*comets[c][5],
        comets[c][2]*comets[c][5]))
def drawCometsFarAway():
    for f in range(len(cometsFarAway)):
        pygame.draw.rect(windowSurface, (240, 100, 100),
        ((WINDOWWIDTH/2 - (cometsFarAway[f][5] * cometsFarAway[f][0]) +
        crosshairx*cometsFarAway[f][3]),
        WINDOWHEIGHT/2 - (cometsFarAway[f][5] * cometsFarAway[f][1]) +
        crosshairy*cometsFarAway[f][3],
        cometsFarAway[f][2]*cometsFarAway[f][5],
        cometsFarAway[f][2]*cometsFarAway[f][5]))
def shootTheComet():
    target = []
    if len(cometsFarAway) >= 1:
        for f in range(len(cometsFarAway[:])):
            target.append([])
            target[f].append(WINDOWWIDTH/2 -
            (cometsFarAway[f][5] * cometsFarAway[f][0]) +
            crosshairx*cometsFarAway[f][3])
            target[f].append(WINDOWHEIGHT/2 -
            (cometsFarAway[f][5] * cometsFarAway[f][1]) +
            crosshairy*cometsFarAway[f][3])
            target[f].append(cometsFarAway[f][2])
        for t in range(len(target)):
            if event.pos[0] in range(int(target[t][0]-target[t][2]),
            int(target[t][0]+target[t][2]))
            and event.pos[1] in range(int(target[t][1]-target[t][2]),
            int(target[t][1]+target[t][2])):
                print("poof")
                cometsFarAway.pop(t)
setGrid()
getNebula()
#createTunnel()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            crosshairx = WINDOWWIDTH / 2 - event.pos[0]
            crosshairy = WINDOWHEIGHT / 2 - event.pos[1]
        if event.type == MOUSEBUTTONUP:
            shootTheComet()
    windowSurface.fill(BLACK)
    #drawTunnel
    for n in range(len(randomNebula)):
        pygame.draw.rect(windowSurface,(random.randint(0,255), 100, 100),
        (nebula[randomNebula[n]][0]+crosshairx,
        nebula[randomNebula[n]][1]+crosshairy,
        2, 2))
    moveComets()
    moveCometsFarAway()
    addComets()
    addCometsFarAway()
    drawComets()
    drawCometsFarAway()
    pygame.display.update()
    time.sleep(0.02)
    #let's try to branch this thing
