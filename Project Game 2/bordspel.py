import pygame
import time
import math




#colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,128)
green = (0,128,0)
yellow = (255,255,0)
silver = (205,201,201)
brown = (205,150,101)

#bases
Base_bos = pygame.image.load('bos.bmp')

#bases positions
Base_bos_pos = [0,0]

#players
player1 = pygame.image.load('soldaat.bmp')

#players starting postions
player1pos = [1,0]


#landscapes
bos         = 0
ijs         = 1
woestijn    = 2
moeras      = 3
water       = 4
goldmine    = 5

#landscape colours
Land = {
            bos     : green,
            ijs     : silver,
            woestijn: brown,
            moeras  : yellow,
            water   : blue,
            goldmine: black
        }

#list that represents our game map
tilemap = [ 
            [moeras, moeras, moeras, moeras, moeras, moeras, moeras, water, water, water, water, ijs, ijs, ijs, ijs, ijs, ijs, ijs],
            [moeras, moeras, moeras, moeras, moeras, moeras, moeras, water, water, water, water, ijs, ijs, ijs, ijs, ijs, ijs, ijs],
            [moeras, moeras, moeras, moeras, moeras, moeras, moeras, water, water, water, water, ijs, ijs, ijs, ijs, ijs, ijs, ijs],
            [moeras, moeras, moeras, moeras, moeras, moeras, moeras, water, water, water, water, ijs, ijs, ijs, ijs, ijs, ijs, ijs],
            [moeras, moeras, moeras, moeras, moeras, moeras, moeras, water, water, water, water, ijs, ijs, ijs, ijs, ijs, ijs, ijs],
            [moeras, moeras, moeras, moeras, moeras, moeras, water, water, water, water, water, water, ijs, ijs, ijs, ijs, ijs, ijs],
            [moeras, moeras, moeras, moeras,moeras, water, water, water, water, water, water, water, water, ijs, ijs, ijs, ijs, ijs],
            [water, water, water, water, water, water, water, goldmine, goldmine, goldmine, goldmine, water, water, water, water, water, water, water],
            [water, water, water, water, water, water, water, goldmine, goldmine, goldmine, goldmine, water, water, water, water, water, water, water],
            [water, water, water, water, water, water, water, goldmine, goldmine, goldmine, goldmine, water, water, water, water, water, water, water],
            [water, water, water, water, water, water, water, goldmine, goldmine, goldmine, goldmine, water, water, water, water, water, water, water],
            [woestijn, woestijn, woestijn, woestijn, woestijn, water, water, water, water, water, water, water, water, bos, bos, bos, bos, bos],
            [woestijn, woestijn, woestijn, woestijn, woestijn, woestijn, water, water, water, water, water, water, bos, bos, bos, bos, bos, bos],
            [woestijn, woestijn, woestijn, woestijn, woestijn, woestijn, woestijn, water, water, water, water, bos, bos, bos, bos, bos, bos, bos],
            [woestijn, woestijn, woestijn, woestijn, woestijn, woestijn, woestijn, water, water, water, water, bos, bos, bos, bos, bos, bos, bos],
            [woestijn, woestijn, woestijn, woestijn, woestijn, woestijn, woestijn, water, water, water, water, bos, bos, bos, bos, bos, bos, bos],
            [woestijn, woestijn, woestijn, woestijn, woestijn, woestijn, woestijn, water, water, water, water, bos, bos, bos, bos, bos, bos, bos],
            [woestijn, woestijn, woestijn, woestijn, woestijn, woestijn, woestijn, water, water, water, water, bos, bos, bos, bos, bos, bos, bos]
           ]

#display width and height
mapwidth = 18
mapheight = 18
TILESIZE = 40 

#Frequency game displayscreen
pygame.init()
startDisplay = pygame.display.set_mode((mapwidth*TILESIZE,mapheight*TILESIZE))

menu_data = (
    'Main',
    'Item 0',
    'Item 1',
    (
        'Things',
        'Item 0',
        'Item 1',
        'Item 2',
        (
            'More Things',
            'Item 0',
            'Item 1',
        ),
    ),
    'Quit',
)
PopupMenu(menu_data)
for e in pygame.event.get():
    if e.type == USEREVENT and e.code == 'MENU':

        if (e.name,e.text) == ('Main','Quit'):
            quit()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #elif event.type == KEYDOWN:

    for row in range(mapheight):
        for column in range(mapwidth):
            pygame.draw.rect(startDisplay, Land[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))
    startDisplay.blit(player1,(player1pos[0]*TILESIZE,player1pos[1]*TILESIZE))
    startDisplay.blit(Base_bos,(Base_bos_pos[0]*TILESIZE,Base_bos_pos[1]*TILESIZE))
    
    pygame.display.update()






