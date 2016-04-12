import pygame, sys
from pygame.locals import *
import time
import math
import random
from game import *
from classes import *



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
Base_bosImage = pygame.image.load('bos.bmp')
Base_moerasImage = pygame.image.load('moeras.bmp')
Base_ijsvlakteImage = pygame.image.load('ijsvlakte.bmp')
Base_woestijnImage = pygame.image.load('woestijn.bmp')

#bases positions
Base_moeras_pos = [0,0]
Base_ijsvlakte_pos = [17,0]
Base_woestijn_pos = [0,17]
Base_bos_pos = [17,17]

bases = []
bases.append(Assets("base", Base_moerasImage, Base_moeras_pos, 1, 1))
bases.append(Assets("base", Base_ijsvlakteImage, (Base_ijsvlakte_pos[0]*(L+d),Base_ijsvlakte_pos[1]*(L+d)), 1, 1))
bases.append(Assets("base", Base_bosImage, (Base_bos_pos[0]*(L+d),Base_bos_pos[1]*(L+d)), 1, 1))
bases.append(Assets("base", Base_woestijnImage, (Base_woestijn_pos[0]*(L+d),Base_woestijn_pos[1]*(L+d)), 1, 1))


#buttons
#start_button = pygame.image.load('startbutton.bmp')
#exit_button = pygame.image.load('exitbutton.bmp')
#manual_button = pygame.image.load('manualbutton.bmp')


#soldiers
soldier1Image = pygame.image.load('soldaat.bmp')#moeras soldaten
soldier2Image = pygame.image.load('soldaat2.bmp')#ijsvlakte soldaten
soldier3Image = pygame.image.load('soldaat3.bmp')#woestijn soldaten
soldier4Image = pygame.image.load('soldaat4.bmp')#bos soldaten
          

class Game:
    def __init__(self, screen, gameboard):
        self.gameDisplay = screen
        
        self.spelbord = gameboard
        self.game_board = game_map
        self.main_loop()

    def main_loop(self):
        
        running = True;
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False;
                    pygame.quit()
                    
            if self.spelbord.turnsLeft == 0:
                self.spelbord.endTurn()
            self.update()
            self.draw()
            pygame.display.update()
            clock.tick(FPS)
            time.sleep(0.5)
    
    def update(self):
        for asset in self.spelbord.assets:
            if asset.asset != 'base':
                asset.position = [random.randint(0, 17)*(L + d), random.randint(0, 17)*(L + d)]


    def draw(self):
        startDisplay.fill(black)
        startDisplay.blit(game_map,(0,0))

        button("Main Menu",1100,650,150,50,silver,bright_black,'mainm')

        # Draw Assets
        for asset in self.spelbord.assets:
            startDisplay.blit(asset.image, asset.position)


                   
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()    

def createGame(playerCount):
    playerts =[]
    startTile = create_board(18, 18)
    board = Board(startTile, playerts)
    for i in range(0, playerCount):
        newPlayer = Player("Henk")
        newPlayer.assets.append(bases[i])
        board.assets.append(bases[i])
        board.players.append(newPlayer)
    board.current_player = board.players[0]
    return board
    
    
    
    

def button(msg,x,y,w,h,ac,ic,action=None):
     mouse = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()

     if x+w > mouse [0] > x and y+h > mouse [1] > y:
        pygame.draw.rect(startDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play":
                

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
                Game(startDisplay, createGame(2))
            elif action == "3players":
                Game(startDisplay, createGame(3))
            elif action == "4player":
                Game(startDisplay, createGame(4))


            
            

               
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
        startDisplay.blit(startbg,(0,0))
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Frequency", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        startDisplay.blit(TextSurf, TextRect)

        button("Start game",330,500,130,50,silver,bright_black,"amount")
        button("Manual", 630,500,100,50,silver,bright_black,'manual')
        button("Quit",870,500,100,50,silver,bright_black,"quit") 

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
        

        button("2 players", 240,400,150,50,silver,bright_black,"2players")
        button("3 players",560,400,150,50,silver,bright_black,"3players") 
        button("4 players",840,400,150,50,silver,bright_black,"4player") 

        pygame.display.update()
        clock.tick(FPS)
       
game_intro()


