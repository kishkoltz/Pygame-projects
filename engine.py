# E:\ppython\app\python.exe engine.py
'''
Setting up rules for every element separately is bothersome. I will try to
create an engine which will process the information about the elements and
modify it accordingly.
The engine should contain the following functionalities:

1. Ability to modify the coordinates according to the mouse position and the
depth of the given element.
2. A unified system of maintaining the depth and correct perspective for all
elements
3. An easy method of moving the element on all 3 axes

Grid:
    0,0 centered on the grid instead of topleft corner;
    XYZ axes valued from -100 to 100 in order to make them scalable

Objects:
    Absolute data:
        constant dimensions - width, length, depth;
        position on the grid;
        if the object is influenced by mouse position
        movement speed and direction
    Relative data:
        dimensions modified by the grid position;
        variable for mouse position sensitivity
        visible movement affected by depth - so that the object can be
        closing in slowly from the distance and quickly pass by


FIRST CHALLENGE: Prepare the engine to display a 3d grid which takes
the distance perception into consideration
'''
import pygame, sys, time, random, math
from pygame.locals import *
pygame.init()
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('the Engine')
crosshairx = 0
crosshairy = 0
BLACK = (0, 0, 0)

grid = {'absolute':\
{'dimensions':[200, 200], 'layers':[15,1], 'position':[-100, -100, 0], 'movement':[0, 0, 0]},
'relative':['dimension x, dimension y', 'topleft x, topleft y']} # a nested dict for absolute and relative values
def modifyDimensions(item):
    copycat = item['absolute']['position'][:]
    print(copycat)
    item['absolute']['position'] = []
    for t in range(3):
        item['absolute']['position'].append(copycat[t]+item['absolute']['movement'][t])
    #for o in item['absolute']['position'][:]:
    #    item['absolute']['position'][o] = o + item['absolute']['movement'][o]
    #print(len(item['relative']))
    item['relative'] = []
    for i in range(item['absolute']['layers'][0]):
        item['relative'].append([])

    #item['relative'] = ([] * item['absolute']['layers'][0])
    #print(item['relative'])
    #for l in range(item['absolute']['layers'][0]):
    #    item['relative'].append()
    for l in range(item['absolute']['layers'][0]):
        #print('layer %s' % (l+1))
        #print(item['relative'][l])
        '''
        relative multiplier = 100
        for multiplier in range(Z position + (layer number * layer depth)):
            relative multiplier -= 1 - (multiplier*0,5)
        relative dimensions = absolute dimensions * (Z position +
        (layer number * layer depth)) * ((1+cos(0.03Z))/2)<-= seems ok

        '''
        item['relative'][l] = ((item['absolute']['dimensions'][0] *
        (math.cos(0.015 * (item['absolute']['position'][2] +
        (l * item['absolute']['layers'][1]))))) /200 * WINDOWWIDTH,

        (item['absolute']['dimensions'][1] *
        (math.cos(0.015 * (item['absolute']['position'][2] +
        (l * item['absolute']['layers'][1]))))) /200 * WINDOWHEIGHT,

        (WINDOWWIDTH/2 + ((WINDOWWIDTH / 2) * (item['absolute']['position'][0] / 100) *
        ((math.cos(0.015 * (item['absolute']['position'][2] +
        (l * item['absolute']['layers'][1])))))) +
        crosshairx * ((math.sin(0.015 *
        (item['absolute']['position'][2] + (l * item['absolute']['layers'][1])))))),

        (WINDOWHEIGHT/2 + (WINDOWHEIGHT / 2) * (item['absolute']['position'][1] / 100) *
        ((math.cos(0.015 * (item['absolute']['position'][2] +
        (l * item['absolute']['layers'][1]))))) +
        crosshairy * ((math.sin(0.015 * (item['absolute']['position'][2] +
        (l * item['absolute']['layers'][1])))))))
        #print(item['relative'][l])

def moveObject(item, destination, phase):
    if destination == 'forward' and phase == 'start':
        item['absolute']['movement'][2] = 3
    if destination == 'forward' and phase == 'stop':
        item['absolute']['movement'][2] = 0
    if destination == 'backward' and phase == 'start':
        item['absolute']['movement'][2] = -3
    if destination == 'backward' and phase == 'stop':
        item['absolute']['movement'][2] = 0

modifyDimensions(grid)
print(grid)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEMOTION:
            crosshairx = WINDOWWIDTH / 2 - event.pos[0]
            crosshairy = WINDOWHEIGHT / 2 - event.pos[1]
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == ord('w'):
                moveObject(grid, 'forward', 'start')
            if event.key == K_DOWN or event.key == ord('s'):
                moveObject(grid, 'backward', 'start')
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_UP or event.key == ord('w'):
                moveObject(grid, 'forward', 'stop')
            if event.key == K_DOWN or event.key == ord('s'):
                moveObject(grid, 'backward', 'stop')
        #if event.type == MOUSEBUTTONUP:
        #    shootTheComet()
    windowSurface.fill(BLACK)
    modifyDimensions(grid)
    #print(grid)
    for o in range(grid['absolute']['layers'][0]):
        pygame.draw.rect(windowSurface,(50+3*o, 0, 0),
        (grid['relative'][o][2], grid['relative'][o][3],
        grid['relative'][o][0], grid['relative'][o][1]))
    pygame.display.update()
    time.sleep(0.02)
