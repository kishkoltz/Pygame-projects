# E:\ppython\app\python.exe parallax.py

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


foreground = {'rect': pygame.Rect (0, 0, 1, 1), 'color': GREEN}
closeMidground = {'rect': pygame.Rect (0, 0, 1, 1), 'color': (0, 200, 0)}
midground = {'rect': pygame.Rect (0, 0, 1, 1), 'color': (0, 150, 0)}
farMidground = {'rect': pygame.Rect (0, 0, 1, 1), 'color': (0, 100, 0)}
background = {'rect': pygame.Rect (0, 0, 1, 1), 'color': BLACK}
squares = (foreground, closeMidground, midground, farMidground, background)

def settiles():
    global foreground, closeMidground, midground, farMidground, background
    foreground['rect'] = (WINDOWWIDTH/2 - 175 + int(0.2 * crosshairy),
        WINDOWHEIGHT/2 - 175 + int(0.2 * crosshairy), 350, 350)
    closeMidground['rect'] = (WINDOWWIDTH/2 - 120 + int(0.4 * crosshairx),
        WINDOWHEIGHT/2 - 120 + int(0.4 * crosshairy), 240, 240)
    midground['rect'] = (WINDOWWIDTH/2 - 90 + int(0.6 * crosshairx),
        WINDOWHEIGHT/2 - 90 + int(0.6 * crosshairy), 180, 180)
    farMidground['rect'] = (WINDOWWIDTH/2 - 60 + int(0.8 * crosshairx),
        WINDOWHEIGHT/2 - 60 + int(0.8 * crosshairy), 120, 120)
    background['rect'] = (WINDOWWIDTH/2 - 30 + crosshairx,
        WINDOWHEIGHT/2 - 30 + crosshairy, 60, 60)




while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            crosshairx = WINDOWWIDTH / 2 - event.pos[0]
            crosshairy = WINDOWHEIGHT / 2 - event.pos[1]

    windowSurface.fill(WHITE)
    settiles()
    for s in squares:
        pygame.draw.rect(windowSurface, s['color'], s['rect'])

    pygame.display.update()
    time.sleep(0.02)
