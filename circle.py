# E:\ppython\app\python.exe hello.py
import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()
WINDOWWIDTH = 500
WINDOWHEIGHT = 400
# set up the window
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('The game title')
# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# draw the window onto the screen



# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    windowSurface.fill(WHITE)
    for x in range(WINDOWWIDTH):
        for y in range(WINDOWHEIGHT):
            if (x - (WINDOWWIDTH/2))**2 + (y - WINDOWHEIGHT/2)**2 < (WINDOWHEIGHT/2)**2:
                pixArray = pygame.PixelArray(windowSurface)
                pixArray[x][y] = BLACK
                del pixArray
    pygame.display.update()
