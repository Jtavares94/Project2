import pygame
import time




pygame.init()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

bright_white = (200,200,200)
bright_black = (1,1,1)

#display width and height
display_width = 800
display_height = 600

#Frequency game displayscreen
startDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Freguency')
clock = pygame.time.Clock()

    
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()    


  
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 90)
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
                #hier moet de game komen boardgame()
                boardgame()
            elif action == "settings":
                #settings menu
                settings()
            elif action == "quit":
                pygame.quit()
                quit()

     else:
        pygame.draw.rect(startDisplay, ic, (x,y,w,h))
             
     smallText = pygame.font.Font("freesansbold.ttf",20)
     textSurf, textRect = text_objects(msg, smallText)
     textRect.center = ( (x+(w/2)), (y+(h/2)) )
     startDisplay.blit(textSurf, textRect)


#Frequency start menu/options
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        startDisplay.fill(black)
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Frequency", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        startDisplay.blit(TextSurf, TextRect)

        button("Start game",150,450,100,50,black,bright_black,"play")
        button("Settings",360,450,100,50,black,bright_black,"settings")
        button("Quit",560,450,100,50,black,bright_black,"quit")
      

        pygame.display.update()
        clock.tick(15)



game_intro()
pygame.display.update()
pygame.quit()
quit()



       





