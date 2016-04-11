import pygame, sys
from pygame.locals import *
import time
import math
import random
from game import *



pygame.init()

# bright colors
bright_white = (200,200,200)
bright_black = (1,1,1)
bright_red = (200,0,0)
bright_blue = (0,0,100)
bright_brown =  (200,130,90)
bright_silver = (190,190,190)
bright_green = (0,120,0)
bright_yellow = (240,240,0)

#colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,128)
green = (0,128,0)
yellow = (255,255,0)
silver = (205,201,201)
brown = (205,150,101)

#fonts
large_text_fonts = 90
small_text_fonts = 20

#display width and height
display_width = 1300
display_height = 700

#Frequency game displayscreen
startDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Frequency')
clock = pygame.time.Clock()
FPS = 60

#square pixel size
L = 36 
d = 3

#startbg
startbg = pygame.image.load('startschermbg.bmp')

#amount player choose
amountplayerbg = pygame.image.load('amountplayerbg.bmp')

#board
game_map = pygame.image.load('game_map.bmp')
bg_pos = [0,0]

#bases
Base_bos = pygame.image.load('bos.bmp')
Base_moeras = pygame.image.load('moeras.bmp')
Base_ijsvlakte = pygame.image.load('ijsvlakte.bmp')
Base_woestijn = pygame.image.load('woestijn.bmp')

#bases positions
Base_moeras_pos = [0,0]
Base_ijsvlakte_pos = [17,0]
Base_woestijn_pos = [0,17]
Base_bos_pos = [17,17]

#buttons
#start_button = pygame.image.load('startbutton.bmp')
#exit_button = pygame.image.load('exitbutton.bmp')
#manual_button = pygame.image.load('manualbutton.bmp')


#soldiers
soldier1 = pygame.image.load('soldaat.bmp')#moeras soldaten
soldier2 = pygame.image.load('soldaat2.bmp')#ijsvlakte soldaten
soldier3 = pygame.image.load('soldaat3.bmp')#woestijn soldaten
soldier4 = pygame.image.load('soldaat4.bmp')#bos soldaten
          
#players starting positions
soldier1pos = [1,0]
soldier2pos = [16,0]
soldier3pos = [0,16]
soldier4pos = [16,17]

class Game:
    def __init__(self, screen, start_tile):
        self.gameDisplay = screen
        self.start_tile = start_tile
        self.assets = []
        self.game_board = game_map

    def main_loop(self):
        

        while True:
            self.draw()
            pygame.display.update()
            clock.tick(FPS)

    def draw(self):
        gameDisplay.fill(black)
        gameDisplay.blit(game_map,(0,0))


        


            
    
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()    
 

def button(msg,x,y,w,h,ac,ic,action=None):
     mouse = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()

     if x+w > mouse [0] > x and y+h > mouse [1] > y:
        pygame.draw.rect(startDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play":
                start_tile = create_board(18,18)  
                Game(startDisplay, start_tile)                             
            elif action == "amount":
                choose_amount_of_players()                                                                                              
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "mainm":
                game_intro()
            elif action == "option":
                soldier()
            elif action == "manual":
                manual()
            elif action == "2players":
                start_tile = create_board(18,18)  
                Game(startDisplay, start_tile)
            elif action == "3players":
                game_with_3_players()

            
            

               
     else:
        pygame.draw.rect(startDisplay, ic, (x,y,w,h))
             
     smallText = pygame.font.Font("freesansbold.ttf",small_text_fonts)
     textSurf, textRect = text_objects(msg, smallText)
     textRect.center = ( (x+(w/2)), (y+(h/2)) )
     startDisplay.blit(textSurf, textRect)
               

#Frequency start menu/options
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        
                      
        startDisplay.fill(black)
        startDisplay.blit(startbg,(bg_pos[0]*(L+d),bg_pos[1]*(L+d)))
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Frequency", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        startDisplay.blit(TextSurf, TextRect)


        button("Start game",330,500,130,50,silver,bright_black,"amount")
        button("Manual", 630,500,100,50,silver,bright_black,'manual')
        button("Quit",870,500,100,50,silver,bright_black,"quit") 

        #startDisplay.blit(start_button,(330,580))
        #startDisplay.blit(exit_button,(830,580))
        #startDisplay.blit(manual_button,(590,580))
       
        
           
    
      
        pygame.display.update()
        clock.tick(FPS)

          
"""   
def boardgame():
    startDisplay.fill(black)
    
    
    block(0,0,7,7,black)#moeras
    block(7,0,4,7,black)#water
    block(11,0,7,7,black)#ijsvlakte
      
    block(0,7,7,4,black)#water
    block(7,7,4,4,black)#mine
    block(11,7,7,4,black)#water
    
    block(0,11,7,7,black)#woestijn
    block(7,11,4,7,black)#water
    block(11,11,7,7,black)#bos
    
    #water
    block(6,5,1,2,black)
    block(6,11,1,2,black)
    block(11,5,1,2,black)
    block(11,11,1,2,black)

    #water
    block(5,6,1,1,black)
    block(12,6,1,1,black)
    block(5,11,1,1,black)
    block(12,11,1,1,black)

    
    
    
    gameExit = False


    mapwidth = 18
    mapheight = 18

    while not gameExit :
        my,mx = pygame.mouse.get_pos()               
        for event in pygame.event.get():                     
            if event.type == pygame.QUIT:
                gameExit = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.MOUSEBUTTONDOWN == Base_moeras_pos:
                    pygame.quit()
            elif event.type == pygame.KEYDOWN:                              
                if event.key == pygame.K_RIGHT and soldier1pos[0] < mapheight - 1:
                        soldier1pos[0] += 1
                if event.key == pygame.K_LEFT and soldier1pos[0] > 0:
                        soldier1pos[0] -= 1                                              
                if event.key == pygame.K_UP and soldier1pos[1] > 0:
                        soldier1pos[1] -= 1                                                     
                if event.key == pygame.K_DOWN and soldier1pos[1] < mapwidth - 1:
                        soldier1pos[1] += 1

                    
        

        smallText = pygame.font.Font("freesansbold.ttf",small_text_fonts)
        
        font = pygame.font.SysFont("monospace", 20)
        text = font.render("Current player is:", 1, white)
        startDisplay.blit(text, (710, 10))

                    
        pygame.display.update()
        clock.tick(FPS)     
"""

def block():
    startDisplay.fill(black)

    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    for i in range (width):
        for j in range (heigth):
            pygame.draw.rect(startDisplay,ac,((i+x)*(L+d),(j+y)*(L+d),L,L))
            if x+width > mouse [0] > x and y+height > mouse [1] > y:
                pygame.draw.rect(startDisplay,ac,((i+x)*(L+d),(j+y)*(L+d),L,L))
    """

    startDisplay.blit(game_map,)

    #bases
    startDisplay.blit(Base_bos,)
    startDisplay.blit(Base_moeras,)
    startDisplay.blit(Base_woestijn,)
    startDisplay.blit(Base_ijsvlakte,)
        
    #startDisplay.blit(soldier1,(soldier1pos[0]*(L+d),soldier1pos[1]*(L+d)))
                                                
    button("Main Menu",1100,650,150,50,silver,bright_black,'mainm')

    button("Main Menu",1100,650,150,50,silver,bright_black,'mainm')         
    #button("Base options", 900,200,100,50,silver,bright_black,'option') 
     
    pygame.display.update()
    clock.tick(FPS)

def manual():
    startDisplay.fill(black)
    
    manual = False


    while not manual :                   
        for event in pygame.event.get():                     
            if event.type == pygame.QUIT:
                manual = True

    

        pygame.display.update()
        clock.tick(FPS)


def choose_amount_of_players():
    startDisplay.fill(black)

    amount_players = False

    while not amount_players:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                amount_players = True
        
        startDisplay.blit(amountplayerbg,(0,0))
        largeText = pygame.font.Font('freesansbold.ttf',60)
        TextSurf, TextRect = text_objects("Choose amount of players!", largeText)
        TextRect.center = ((650),(200))
        startDisplay.blit(TextSurf, TextRect)
        

        button("2 players", 240,400,150,50,silver,bright_black,"play")
        button("3 players",560,400,150,50,silver,bright_black,"play") 
        button("4 players",840,400,150,50,silver,bright_black,"play") 

        pygame.display.update()
        clock.tick(FPS)
       
game_intro()


