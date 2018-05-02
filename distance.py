# E:\ppython\app\python.exe distance.py

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


def createTunnel():
    global tunnel
    if len(tunnel) == 0:
        tunnel.append([0])
        tunnel[0] = (180, 180, 40, 40, 1, (random.randint(0, 255), 0, 0))
    else:
        for t in range(len(tunnel)):
            tunnel[(len(tunnel)-1) - t] = \
            (tunnel[(len(tunnel)-1) - t][0]-(0.5+0.5*(t*1.01)),
            tunnel[(len(tunnel)-1) - t][1]-(0.5+0.5*(t*1.01)),
            tunnel[(len(tunnel)-1) - t][2]+(2*(0.5+0.5*(t*1.01))),
            tunnel[(len(tunnel)-1) - t][3]+(2*(0.5+0.5*(t*1.01))),
            tunnel[(len(tunnel)-1) - t][4] - (0.5*(t*1.5)),
            tunnel[(len(tunnel)-1) - t][5])
        tunnel.append([len(tunnel)])
        tunnel[len(tunnel)-1] = (180, 180, 40, 40, 1, (0, 0, 0))
        tunnel[len(tunnel)-2] = (170, 170, 60, 60, 0.95, (random.randint(0, 255), 0, 0))

    if tunnel[0][2] > 290 or tunnel[0][3] > 290:
            tunnel.pop(0)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            crosshairx = WINDOWWIDTH / 2 - event.pos[0]
            crosshairy = WINDOWHEIGHT / 2 - event.pos[1]

    windowSurface.fill(BLACK)

    createTunnel()
    for t in range(len(tunnel)):
        pygame.draw.rect(windowSurface, tunnel[t][5],
        (tunnel[t][0] + crosshairx*tunnel[t][4],
        tunnel[t][1] + crosshairy*tunnel[t][4],
        tunnel[t][2], tunnel[t][3]))

    pygame.display.update()
    time.sleep(0.04)
