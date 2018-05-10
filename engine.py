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
{'dimensions':[200.0, 200.0], 'layers':[50,2], 'position':[-100.0, -100.0, 0.0],
'movement':[0, 0, 0]},'relative':['dimension x, dimension y',
'topleft x, topleft y']} # a nested dict for absolute and relative values
box = {'absolute':\
{'dimensions':[50.0, 50.0], 'layers':[5,2], 'position':[-25.0, -25.0, 20.0],
'movement':[0, 0, 0]},'relative':['dimension x, dimension y',
'topleft x, topleft y']}

def modifyDimensions(item):
    for t in range(3):
        item['absolute']['position'][t] += (item['absolute']['movement'][t] *
        (1 - ((-0.01 * ((item['absolute']['position'][2] - 100) ** 2) + 100)/100)))

    item['relative'] = []
    for l in range(item['absolute']['layers'][0]):
        item['relative'].append([])
        '''
        f(z)=-0.01 * (z - 100) ** 2 + 100
        f(z)=(-0.01 * (((item['absolute']['position'][2] +
        (l * item['absolute']['layers'][1])) - 100) ** 2) + 100)/100
        (1 - (((((item['absolute']['position'][2] +
        (l * item['absolute']['layers'][1])) - 100) ** 2) + 100)/100))
        '''
        item['relative'][l] = \
        (item['absolute']['dimensions'][0] / 200 * WINDOWWIDTH *
        (1 - ((-0.01 * (((item['absolute']['position'][2] +
        (l * item['absolute']['layers'][1])) - 100) ** 2) + 100)/100)),

        item['absolute']['dimensions'][1] /200 * WINDOWHEIGHT *
        (1 - ((-0.01 * (((item['absolute']['position'][2] +
        (l * item['absolute']['layers'][1])) - 100) ** 2) + 100)/100)),

        (WINDOWWIDTH/2 + ((WINDOWWIDTH / 2) * (item['absolute']['position'][0] / 100) *
        (1 - ((-0.01 * (((item['absolute']['position'][2] +
        (l * item['absolute']['layers'][1])) - 100) ** 2) + 100)/100))) +
        crosshairx * ((-0.01 * (((item['absolute']['position'][2] +
        (l * item['absolute']['layers'][1])) - 100) ** 2) + 100)/100)),

        (WINDOWHEIGHT/2 + (WINDOWHEIGHT / 2) * (item['absolute']['position'][1] / 100) *
        (1 - ((-0.01 * (((item['absolute']['position'][2] +
        (l * item['absolute']['layers'][1])) - 100) ** 2) + 100)/100)) +
        crosshairy * ((-0.01 * (((item['absolute']['position'][2] +
        (l * item['absolute']['layers'][1])) - 100) ** 2) + 100)/100)))


def moveObject(item, axis, value):
    if axis == 'X':
        item['absolute']['movement'][0] = value
    if axis == 'Y':
        item['absolute']['movement'][1] = value
    if axis == 'Z':
        item['absolute']['movement'][2] = value



def shootTheBox():
        for l in range(box['absolute']['layers'][0]):
            if event.pos[0] >= box['relative'][l][2] and \
            event.pos[0] <= (box['relative'][l][2] + box['relative'][l][0]) and\
            event.pos[1] >= box['relative'][l][3] and \
            event.pos[1] <= (box['relative'][l][3] + box['relative'][l][1]):
                box['absolute']['position'] = \
                [random.randint(-100, (100 - box['absolute']['dimensions'][0])),
                random.randint(-100, (100 - box['absolute']['dimensions'][1])),
                random.randint(0, 75)]
                break
modifyDimensions(grid)
#print(grid)

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
                moveObject(box, 'Z', 3)
            if event.key == K_DOWN or event.key == ord('s'):
                moveObject(box, 'Z', -3)
            if event.key == K_UP or event.key == ord('a'):
                moveObject(box, 'X', -6)
            if event.key == K_DOWN or event.key == ord('d'):
                moveObject(box, 'X', 6)
            if event.key == K_UP or event.key == ord('q'):
                moveObject(box, 'Y', -6)
            if event.key == K_DOWN or event.key == ord('e'):
                moveObject(box, 'Y', 6)
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_UP or event.key == ord('w'):
                moveObject(box, 'Z', 0)
            if event.key == K_DOWN or event.key == ord('s'):
                moveObject(box, 'Z', 0)
            if event.key == K_UP or event.key == ord('a'):
                moveObject(box, 'X', 0)
            if event.key == K_DOWN or event.key == ord('d'):
                moveObject(box, 'X', 0)
            if event.key == K_UP or event.key == ord('q'):
                moveObject(box, 'Y', 0)
            if event.key == K_DOWN or event.key == ord('e'):
                moveObject(box, 'Y', 0);
        if event.type == MOUSEBUTTONUP:
            shootTheBox()
    windowSurface.fill(BLACK)
    modifyDimensions(grid)
    modifyDimensions(box)
    #print(grid)
    for o in range(grid['absolute']['layers'][0]):
        pygame.draw.rect(windowSurface,(185-3*o, 0, 0),
        (grid['relative'][o][2], grid['relative'][o][3],
        grid['relative'][o][0], grid['relative'][o][1]))
    for o in range(box['absolute']['layers'][0]):
        pygame.draw.rect(windowSurface,(0, 255-10*((box['absolute']['layers'][0]-1) - o), 0),
        (box['relative'][(box['absolute']['layers'][0]-1) - o][2],
        box['relative'][(box['absolute']['layers'][0]-1) - o][3],
        box['relative'][(box['absolute']['layers'][0]-1) - o][0],
        box['relative'][(box['absolute']['layers'][0]-1) - o][1]))
    pygame.display.update()
    time.sleep(0.02)
