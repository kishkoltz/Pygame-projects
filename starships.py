# E:\ppython\app\python.exe starships.py

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

starship = []
secondStarship = []
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

def getStarship():
    global starship
    for x in range(5):
        starship.append([])

def getSecondStarship():
    global secondStarship
    for x in range(5):
        secondStarship.append([])

def modifyStarship():
    global starship
    for x in range(5):
        starship[x] = {'color':(90+10*x, 90+15*x, 90+30*x),
        'topleft':(WINDOWWIDTH/2 - ((5*(3**0.5))+(x*(3**0.5))) + int((0.4 - (0.05*x)) * crosshairx),
        WINDOWHEIGHT/2 - (5+x) + int((0.4 - (0.05*x)) * crosshairy)),
        'topright':(WINDOWWIDTH/2 + ((5*(3**0.5))+(x*(3**0.5))) + int((0.4 - (0.05*x)) * crosshairx),
        WINDOWHEIGHT/2 - (5+x) + int((0.4 - (0.05*x)) * crosshairy)),
        'bottom':(WINDOWWIDTH/2 + int((0.4 - (0.05*x)) * crosshairx),
        WINDOWHEIGHT/2 + (10+x) + int((0.4 - (0.05*x)) * crosshairy))}
def modifySecondStarship():
    global secondStarship
    for x in range(5):
        secondStarship[x] = {'color':(90+10*x, 90+15*x, 90+30*x),
        'topleft':\
        (WINDOWWIDTH/2 + (50+x*2.5) - ((5*(3**0.5))+(x*(3**0.5))) +
        int((0.4 - (0.05*x)) * crosshairx),
        WINDOWHEIGHT/2 + (50+x*2.5) - (5+x) +
        int((0.4 - (0.05*x)) * crosshairy)),
        'topright':\
        (WINDOWWIDTH/2 + (50+x*2.5) + ((5*(3**0.5))+(x*(3**0.5))) +
        int((0.4 - (0.05*x)) * crosshairx),
        WINDOWHEIGHT/2 + (50+x*2.5) - (5+x) +
        int((0.4 - (0.05*x)) * crosshairy)),
        'bottom':\
        (WINDOWWIDTH/2 + (50+x*2.5) +
        int((0.4 - (0.05*x)) * crosshairx),
        WINDOWHEIGHT/2 + (50+x*2.5) + (10+x) +
        int((0.4 - (0.05*x)) * crosshairy))}
def drawTop(vessel):
    pygame.draw.polygon(windowSurface, (0, 255, 0),
    (vessel[0]['topleft'], vessel[0]['topright'],
    vessel[4]['topright'], vessel[4]['topleft']))
def drawLeft(vessel):
    pygame.draw.polygon(windowSurface, (255, 0, 0),
    (vessel[0]['topleft'], vessel[4]['topleft'],
    vessel[4]['bottom'], vessel[0]['bottom']))
def drawRight(vessel):
    pygame.draw.polygon(windowSurface, (0, 0, 255),
    (vessel[0]['topright'], vessel[4]['topright'],
    vessel[4]['bottom'], vessel[0]['bottom']))
def drawBack(vessel):
    pygame.draw.polygon(windowSurface, (255, 255, 255),
    (vessel[4]['topleft'], vessel[4]['topright'],
    vessel[4]['bottom']))
def drawStarship():
    '''
    b = y intercept = x==0, y == b
    f(y)=(3**0.5)*x + b
    b = y - (3**0.5)*x
    '''
    smallLeftIntercept = starship[0]['topleft'][1] - \
    ((3**0.5)*starship[0]['topleft'][0])
    biggerLeftIntercept = starship[1]['topleft'][1] - \
    ((3**0.5)*starship[1]['topleft'][0])
    '''
    c = y intercept = x == WINDOWWIDTH, y == c
    '''
    smallRightIntercept = starship[0]['topright'][1] - \
    ((-1*(3**0.5))*starship[0]['topright'][0])
    biggerRightIntercept = starship[1]['topright'][1] - \
    ((-1*(3**0.5))*starship[1]['topright'][0])
    '''
    if smallY < bigY:
        I. if smallLeftIntercept >= biggerLeftIntercept and
            smallRightIntercept <= biggerRightIntercept:
            draw the top and left sides
        II. ifsmallLeftIntercept <= biggerRightIntercept and
            smallRightIntercept >= biggerRightIntercept:
            draw the top and right sides
        III. ifsmallLeftIntercept <= biggerLeftIntercept and
            smallRightIntercept <= biggerRightIntercept:
            draw only the top side
    if smallY > bigY:
        I. if smallLeftIntercept >= biggerLeftIntercept and
            smallRightIntercept >= biggerRightIntercept:
            draw the left and right sides
        II. if smallLeftIntercept >= biggerLeftIntercept and
            smallRightIntercept <= biggerRightIntercept:
            draw only the left side
        III. if smallLeftIntercept <= biggerLeftIntercept and
            smallRightIntercept >= biggerRightIntercept:
            draw only the right side
    '''
    drawBack(starship)
    if starship[0]['topleft'][1] < starship[1]['topleft'][1]:
        drawTop(starship)
        if smallLeftIntercept > biggerLeftIntercept and \
        smallRightIntercept < biggerRightIntercept:
            drawLeft(starship)
        if smallLeftIntercept < biggerLeftIntercept and \
        smallRightIntercept > biggerRightIntercept:
            drawRight(starship)
    if starship[0]['topleft'][1] >= starship[1]['topleft'][1]:
        if smallLeftIntercept > biggerLeftIntercept and \
        smallRightIntercept > biggerRightIntercept:
            drawLeft(starship), drawRight(starship)
        if smallLeftIntercept > biggerLeftIntercept and \
        smallRightIntercept < biggerRightIntercept:
            drawLeft(starship)
        if smallLeftIntercept < biggerLeftIntercept and \
        smallRightIntercept > biggerRightIntercept:
            drawRight(starship)
def drawSecondStarship():
    smallLeftIntercept = secondStarship[0]['topleft'][1] - \
    ((3**0.5)*secondStarship[0]['topleft'][0])
    biggerLeftIntercept = secondStarship[1]['topleft'][1] - \
    ((3**0.5)*secondStarship[1]['topleft'][0])

    smallRightIntercept = secondStarship[0]['topright'][1] - \
    ((-1*(3**0.5))*secondStarship[0]['topright'][0])
    biggerRightIntercept = secondStarship[1]['topright'][1] - \
    ((-1*(3**0.5))*secondStarship[1]['topright'][0])

    drawBack(secondStarship)
    if secondStarship[0]['topleft'][1] < secondStarship[1]['topleft'][1]:
        drawTop(secondStarship)
        if smallLeftIntercept > biggerLeftIntercept and \
        smallRightIntercept < biggerRightIntercept:
            drawLeft(secondStarship)
        if smallLeftIntercept < biggerLeftIntercept and \
        smallRightIntercept > biggerRightIntercept:
            drawRight(secondStarship)
    if secondStarship[0]['topleft'][1] >= secondStarship[1]['topleft'][1]:
        if smallLeftIntercept > biggerLeftIntercept and \
        smallRightIntercept > biggerRightIntercept:
            drawLeft(secondStarship), drawRight(secondStarship)
        if smallLeftIntercept > biggerLeftIntercept and \
        smallRightIntercept < biggerRightIntercept:
            drawLeft(secondStarship)
        if smallLeftIntercept < biggerLeftIntercept and \
        smallRightIntercept > biggerRightIntercept:
            drawRight(secondStarship)


getStarship()
getSecondStarship()
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
    modifyStarship()
    modifySecondStarship()

    drawStarship()
    drawSecondStarship()
    pygame.display.update()
    time.sleep(0.02)


'''
starship drawing rules:
1. get the triangles from the farthest to the nearest
2. get their coordinates with the mouse position taken into consideration
3. the polygons would be drawn according to the relationship between the
    intercepts of the farthest and the nearest triangle
    (details in drawStarship)
'''
