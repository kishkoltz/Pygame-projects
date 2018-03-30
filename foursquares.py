# E:\ppython\app\python.exe foursquares.py

import pygame, sys, time, random
from pygame.locals import *

pygame.init()
minusrange = (-4, -3, -2)
plusrange = (2, 3, 4)
directionrange = (plusrange, minusrange)
directionx = random.choice(random.choice(directionrange))
directiony = random.choice(random.choice(directionrange))
crosshairx = 95
crosshairy = 95
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
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
blocks = [b1a, b1b, b2a, b2b]

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

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    windowSurface.fill(BLACK)
    setdirection()
    movecrosshair()
    settiles()
    for b in blocks:
        pygame.draw.rect(windowSurface, b['color'], b['rect'])
    #b1a['rect'].width += random.randint(-2,2)
    #b1a['rect'].height += random.randint(-2,2)
    #pygame.draw.rect(windowSurface, b1a['color'], b1a['rect'])
    #pygame.draw.rect(windowSurface, RED, ((b1a['rect'].width + 10), (b1a['rect'].height + 10), (WINDOWWIDTH - b1a['rect'].width - 15), (WINDOWHEIGHT - b1a['rect'].height - 15)))
    pygame.display.update()
    time.sleep(0.02)
