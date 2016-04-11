import pygame
import time
import math


pygame.init()

#colors
bright_white = (200,200,200)
bright_black = (1,1,1)
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
display_width = 1000
display_height = 800

#Frequency game displayscreen
startDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Freguency')
clock = pygame.time.Clock()



#square pixel size
L = 30  
d = 5


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()    


  
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', large_text_fonts)
    TextSurf, TextRect = text_objects(text, largeText)
    textRect.center = ((display_width/2,), (display_height/2))
    startDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)


def button(msg,x,y,w,h,ic,ac,action=None):
     mouse = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()

     if x+w > mouse [0] > x and y+h > mouse [1] > y:
        pygame.draw.rect(startDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play":                           
                boardgame()
            elif action == "options":
                options()
            elif action == "quit":
                pygame.quit()
                quit()
           

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
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Frequency", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        startDisplay.blit(TextSurf, TextRect)

        button("Start game",200,600,100,50,black,bright_black,"play")
        button("Options",460,600,100,50,black,bright_black,"options")
        button("Quit",720,600,100,50,black,bright_black,"quit")



        pygame.display.update()
        clock.tick(15)
      

def block (x,y,width,heigth,colour):
    for i in range (width):
        for j in range (heigth):
                pygame.draw.rect(startDisplay,colour,((i+x)*(L+d),(j+y)*(L+d),L,L))

        pygame.display.update()
        
def boardgame():
    startDisplay.fill(black)

    block(0,0,7,7,red)
    block(7,0,4,7,blue)
    block(11,0,7,7,green)
    
    block(0,7,7,4,blue)
    block(7,7,4,4,yellow)
    block(11,7,7,4,blue)
    
    block(0,11,7,7,silver)
    block(7,11,4,7,blue)
    block(11,11,7,7,brown)
    
    block(6,5,1,2,blue)
    block(6,11,1,2,blue)
    block(11,5,1,2,blue)
    block(11,11,1,2,blue)

    block(5,6,1,1,blue)
    block(12,6,1,1,blue)
    block(5,11,1,1,blue)
    block(12,11,1,1,blue)

    button("Main Menu",800,600,100,50,black,bright_black,"quit")   
     
    pygame.display.update()
    clock.tick(15)

    gameExit = False

    while not gameExit :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
        

        
            

game_intro()
pygame.display.update()
pygame.quit()
quit()


       





