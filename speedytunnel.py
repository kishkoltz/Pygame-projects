# E:\ppython\app\python.exe speedytunnel.py

import pygame, sys, time, random
from pygame.locals import *

pygame.init()

crosshairx = 0
crosshairy = 0
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Parallax Test')

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

tunnel = []
obstacles = []


def createTunnel():
    global tunnel
    if len(tunnel) == 0:
        tunnel.append([0])
        tunnel[0] = (180, 180, 40, 40, 1, (random.randint(0, 255), 0, 0))
    else:
        for t in range(len(tunnel)):
            tunnel[t] = (tunnel[t][0]-10, tunnel[t][1]-10, tunnel[t][2]+20, tunnel[t][3]+20, tunnel[t][4] - 0.05, tunnel[t][5])
        tunnel.append([len(tunnel)])
        tunnel[len(tunnel)-1] = (180, 180, 40, 40, 1, (0, 0, 0))
        tunnel[len(tunnel)-2] = (170, 170, 60, 60, 0.95, (random.randint(0, 255), 0, 0))

    if tunnel[0][2] > 500 or tunnel[0][3] > 500:
            tunnel.pop(0)

def addObstacles():
    global obstacles
    obstacles.append([len(obstacles)])
    side = random.randint(1,4)
    if side == 1:
        #left
        obstacles[len(obstacles)-1] = (170, 170, 30, 60, 0.95,
        (0, 255, 0), 1)
    if side == 2:
        #top
        obstacles[len(obstacles)-1] = (170, 170, 60, 30, 0.95,
        (0, 255, 0), 2)
    if side == 3:
        #right
        obstacles[len(obstacles)-1] = (200, 170, 30, 60, 0.95,
        (0, 255, 0), 3)
    if side == 4:
        #bottom
        obstacles[len(obstacles)-1] = (170, 200, 60, 30, 0.95,
        (0, 255, 0), 4)

def moveObstacles():
    global obstacles
    if len(obstacles) >= 1:
        for o in range(len(obstacles)):
            if obstacles[o][6] == 1: #left
                obstacles[o] = (obstacles[o][0]-10, obstacles[o][1]-10,
                obstacles[o][2]+10, obstacles[o][3]+20, obstacles[o][4] - 0.05,
                obstacles[o][5], obstacles[o][6])
            if obstacles[o][6] == 2: #top
                obstacles[o] = (obstacles[o][0]-10, obstacles[o][1]-10,
                obstacles[o][2]+20, obstacles[o][3]+10, obstacles[o][4] - 0.05,
                obstacles[o][5], obstacles[o][6])
            if obstacles[o][6] == 3: #right
                obstacles[o] = (obstacles[o][0], obstacles[o][1]-10,
                obstacles[o][2]+10, obstacles[o][3]+20, obstacles[o][4] - 0.05,
                obstacles[o][5], obstacles[o][6])
            if obstacles[o][6] == 4: #bottom
                obstacles[o] = (obstacles[o][0]-10, obstacles[o][1],
                obstacles[o][2]+20, obstacles[o][3]+10, obstacles[o][4] - 0.05,
                obstacles[o][5], obstacles[o][6])

        if obstacles[0][2] > 400 or obstacles[0][3] > 400:
            obstacles.pop(0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            crosshairx = WINDOWWIDTH / 2 - event.pos[0]
            crosshairy = WINDOWHEIGHT / 2 - event.pos[1]

    windowSurface.fill(BLACK)
    #settiles()
    createTunnel()
    for t in range(len(tunnel)):
        pygame.draw.rect(windowSurface, tunnel[t][5],
        (tunnel[t][0] + crosshairx*tunnel[t][4],
        tunnel[t][1] + crosshairy*tunnel[t][4],
        tunnel[t][2], tunnel[t][3]))

    moveObstacles()
    if random.randint(0, 50) > 49:
        addObstacles()

    for o in range(len(obstacles)):
        pygame.draw.rect(windowSurface, obstacles[o][5],
        (obstacles[o][0] + crosshairx*obstacles[o][4],
        obstacles[o][1] + crosshairy*obstacles[o][4],
        obstacles[o][2], obstacles[o][3]))
    #print (len(tunnel))

    pygame.display.update()
    time.sleep(0.04)
