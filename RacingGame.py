import cx_Freeze
import random
import sys
from pygame import *
import pygame
import time

# base =None
# if sys.platform == 'win32':
#     base = "Win32GUI"
# shortcut_table = [
#     ("DesktopShortcut", # shortcut
#      "DesktopFolder", # Directory_
#      "Racing Game", # Name
#      "TARGETDIR", # Componet_
#      "[TARGETDIR]\RacingGame.exe", #Target
#      None, # Arguments
#      None, # Description
#      None, # Hotkey
#      None, # Icon
#      None, # IconIndex
#      None, # ShowCmd
#      "TARGETDIR", # wkDir
#      )
# ]
# msi_data = {"Shortcut":shortcut_table}
# bdist_msi_options = {'data':msi_data}
# executables = [cx_Freeze.Executable(script='RacingGame.py',icon='image/cc.ico',base=base)]

# cx_Freeze.setup(
#     version='1.0',
#     description='Racing game',
#     author="Krishna singh",
#     name ="Racing Game",
#     options={'build_exe':{'packages':['pygame','sys','random','time'],
#                          'include_files':['image/cc.ico','image/car1.png','image/car1.png','image/car2.png','image/car3.png','image/car4.png','image/car5.png','image/car6.png','image/car7.png','image/car8.png','image/car9.png','image/car10.png','image/road2.jpg','music/car_crash.wav','music/jazz.wav']},
#             'bdist_msi': bdist_msi_options,
#             },
#     executables = executables
# )





pygame.init()
gray=(119,118,110)
blue = (50, 153, 213)
black = (0, 0, 0)
green = (0, 255, 0)
red = (213, 50, 80)
bright_red = (255,99,71)
bright_green = (124,252,0)
bright_blue = 	(102,205,170)
white = (255, 255, 255)
display_width, display_height = 800, 550
gamedisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Car Game")

intro_background = pygame.image.load('image/natural.jpg')
instruction_background = pygame.image.load('image/bac.jpg')
backgroundpic  = pygame.image.load('image/road2.jpg')

pygame.mixer.music.load('music/jazz.wav')
car_crash = pygame.mixer.Sound('music/car_crash.wav')
clock = pygame.time.Clock()
x_incerement = 5
y2 = 7
mes = "YOU CRASHED"
obs_pic = ''

carimage = pygame.image.load('image/car6.png')
def scoreboard(score):
    font = pygame.font.SysFont(None, 30)
    text = font.render("SCORE: " +str(score), True, red)
    gamedisplay.blit(text, (0,5))
  


# def obstacle(obs_startx,obs_starty, obs_width, obs_height):
def obstacle(obs_startx,obs_starty,obs):

    if obs == 0:
        obs_pic=pygame.image.load('image/car1.png')
    elif obs == 1:
        obs_pic= pygame.image.load('image/car2.png')
    elif obs == 2:
        obs_pic = pygame.image.load('image/car3.png')
    elif obs == 3:
        obs_pic = pygame.image.load('image/car4.png')
    elif obs == 4:
        obs_pic = pygame.image.load('image/car5.png')
    elif obs == 5:
        obs_pic = pygame.image.load('image/car6.png')
    elif obs == 6:
        obs_pic = pygame.image.load('image/car7.png')
    elif obs == 7:
        obs_pic = pygame.image.load('image/car8.png')
    elif obs == 8:
        obs_pic = pygame.image.load('image/car9.png')
    elif obs == 9:
        obs_pic = pygame.image.load('image/car10.png')
    elif obs == 10:
        obs_pic = pygame.image.load('image/car4.png')                            
    gamedisplay.blit(obs_pic,(obs_startx,obs_starty))
    # background()
    # pygame.draw.rect(gamedisplay, red, [obs_startx, obs_starty, obs_width, obs_height])
    pygame.display.update()
    # elif obs == 4:
    #     obc_pic = pygame.image.load('image/car.PNG')

def background():
# <----------------------------left covaner--------------------------------------------------------->
    gamedisplay.blit(backgroundpic, (14, 0))

#<--------------------------------right_covaner------------------------------------------------------>
    # gamedisplay.blit(backgroundpic, (685, 0))
    
# <-----------------------------------yellow_strip------------------------------------------------->
    # gamedisplay.blit(yellow_strip, (400, 0))
    # gamedisplay.blit(yellow_strip, (400, 100))
    # gamedisplay.blit(yellow_strip, (400, 200))
    # gamedisplay.blit(yellow_strip, (400, 300))
    # gamedisplay.blit(yellow_strip, (400, 400))
    # gamedisplay.blit(yellow_strip, (400, 500))
# <--------------------------------------while_strip------------------------------------------------->
    # gamedisplay.blit(while_strip, (110, 0))
    # gamedisplay.blit(while_strip, (685, 0))
# def background_moving(bg_x,bg_y,bg_rd):
#    if bg_rd == 0:
#        bg_pic= pygame.image.load('image/road2.jpg')
#    elif bc_rd == 1:
#         bc_pic= pygame.image.load('image/road2.jpg')   
#    gamedisplay.blit(bg_pic,(bg_x,bg_y))
#    pygame.display.update()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()    


def message(mes):
    font_style = pygame.font.Font("freesansbold.ttf", 60)
    mesg = font_style.render(mes, True, black)
    gamedisplay.blit(mesg, [int(display_width /4), int(display_height/4)])
    pygame.display.update()
    time.sleep(4)
    gameloop()

def car(x, y):
   
    gamedisplay.blit(carimage, (x, y))

def button(msg,x,y,w,h,ic,ac,action=None):
     mouse = pygame.mouse.get_pos()
     click = pygame.mouse.get_pressed()
     if x+w> mouse[0] >x and y+h > mouse[1] > y:
       pygame.draw.rect(gamedisplay,ac,(x,y,w,h))
       if click[0] ==1 and action != None:    
         if action == 'play':
            gameloop()
         elif action == 'quit':
             pygame.quit()
             quit()
             sys.exit()
         elif action=='intro':
             introduction()
         elif action=='menu':
             introloop()
     else:
        pygame.draw.rect(gamedisplay,ic,(x,y,w,h))
     smalltext = pygame.font.Font("freesansbold.ttf",20)
     textsurf,textrect = text_objects(msg,smalltext)
     textrect.center=((int(x+(w/2))),int((y+(h/2))))
     gamedisplay.blit(textsurf,textrect)   
                        
def introduction():
    intrduction = True
    while intrduction:
      for event in pygame.event.get():
         if  event.type == pygame.QUIT:
             pygame.quit()
             quit()
             sys.exit()
         gamedisplay.blit(intro_background,(0,0))
         largesttext = pygame.font.Font("freesansbold.ttf",80)
         smalltext = pygame.font.Font("freesansbold.ttf",20)
         mediumtext = pygame.font.Font("freesansbold.ttf",40)
         textSurf, textRect = text_objects("This is an car game in which you need score the coming cars",smalltext)
         textRect.center = ((350),(200))
         TextSurf, TextRect = text_objects("INTRODUCTION",largesttext)     
         textRect.center = ((400),(200))
         gamedisplay.blit(TextSurf,TextRect)
         gamedisplay.blit(textSurf,textRect)
         stextSurf, stextRect = text_objects("ARROW LEFT : LEFT TURN",smalltext) 
         stextRect.center=((150),(330))

         htextSurf, htextRect = text_objects("ARROW RIGHT : LEFT RIGHT",smalltext) 
         htextRect.center=((150),(370))
         atextSurf, atextRect = text_objects("ARROW UP : ACCELERATOR",smalltext) 
         atextRect.center=((150),(410))
         btextSurf, btextRect = text_objects("SPACE : BREAK",smalltext) 
         btextRect.center=((150),(450))
        #  stextSurf, stextRect = text_objects("ARROW LEFT : LEFT TURN",smalltext) 
        #  stextRect.center=((150),(400))
        #  stextSurf, stextRect = text_objects("ARROW LEFT : LEFT TURN",smalltext) 
        #  stextRect.center=((150),(400))
         
         gamedisplay.blit(stextSurf,stextRect)
        #  gamedisplay.blit(sTextSurf,sTextRect)
         gamedisplay.blit(htextSurf,htextRect)
         gamedisplay.blit(atextSurf,atextRect)
         gamedisplay.blit(btextSurf,btextRect)
         button("BACK",600,450,100,50,blue,bright_blue,"menu")
         pygame.display.update()
         clock.tick(30)


def introloop():
    intro = True
    while intro :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()
        gamedisplay.blit(intro_background,(0,0))
        largesttext = pygame.font.Font("freesansbold.ttf",115)
        TextSurf,TextRect = text_objects("CAR GAME",largesttext)
        TextRect.center=(400,100)
        gamedisplay.blit(TextSurf,TextRect)
        button("START",150,490,100,50,green,bright_green,"play")        
        button("QUIT",550,490,100,50,red,bright_green,"quit")
        button("INSTRUCTION",300,490,200,50,blue,bright_blue,"intro")
        
        pygame.display.update()
        clock.tick(50)
def gameloop():
    global level
    pygame.mixer.music.play()
    car_speed = 40
    x_change, y_change = 0, 0
    x, y = (display_width*0.45), (display_height*0.76)
    gameclose = False
    # gameover = False
    obstacle_speed = 4
    score = 0 
    obs = 0
    obs_startx =  random.randrange(101, 645)
    # obs_startx =  random.randrange(200, (display_width-200))
    obs_starty = -750
    # obs_width =56
    obs_width =60
    # obs_height = 125
    obs_height = 125
    car_width = 70
    while not gameclose:
        # while gameover == True:
        #     gamedisplay.fill(blue)
        #     messg = "You Lose !! Press Q --> Quit or C---->Play Again"
            # message(messg)
            # pygame.display.update()
            # for event in pygame.event.get():
            #     if event.type == pygame.KEYDOWN:
            #         if event.key == pygame.K_q:
            #             game_over = True
            #             game_close = False
            #         elif event.key == pygame.K_c:
            #             gameloop()
        for event in pygame.event.get():
             if(event.type == pygame.QUIT):
                 gameclose = True
             if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_LEFT:
                         x_change = - x_incerement
                         y_change = 0
                     elif event.key == pygame.K_RIGHT:
                         x_change = x_incerement
                         y_change = 0
                        
                     elif event.key == pygame.K_UP:
                         
                        # y_change = -x_incerement
                    #     x_change = 0
                         obstacle_speed += 2
                     elif event.key == pygame.K_DOWN:
                        # y_change = x_incerement
                    #     x_change = 0
                         obstacle_speed -= 2
                     elif event.key == pygame.K_SPACE:
                        obstacle_speed = 0     


        x += x_change
        y += y_change
        gamedisplay.fill(gray)
        
        # real_y = y2%(backgroundpic.get_rect().width)
        # gamedisplay.blit(backgroundpic,(0,real_y-backgroundpic.get_rect().width))
        # gamedisplay.blit(backgroundpic,(700,real_y-backgroundpic.get_rect().width))
        # if real_y < 800:
        #     gamedisplay.blit(backgroundpic,(0,real_y))
        #     gamedisplay.blit(backgroundpic,(700,real_y))
        #     gamedisplay.blit(backgroundpic,(400,real_y))
        #     gamedisplay.blit(backgroundpic,(400,real_y+100))
        #     gamedisplay.blit(backgroundpic,(400,real_y+200))
        #     gamedisplay.blit(backgroundpic,(400,real_y+300))
        #     gamedisplay.blit(backgroundpic,(400,real_y+400))
        #     gamedisplay.blit(backgroundpic,(400,real_y+500))
        #     gamedisplay.blit(backgroundpic,(4000,real_y-100))
        #     gamedisplay.blit(backgroundpic,(120,real_y-200))
        #     gamedisplay.blit(backgroundpic,(120,real_y+20))
        #     gamedisplay.blit(backgroundpic,(120,real_y+30))
        #     gamedisplay.blit(backgroundpic,(680,real_y-100))
        #     gamedisplay.blit(backgroundpic,(680,real_y+20))
        #     gamedisplay.blit(backgroundpic,(680,real_y+30))
        # y2 += obstacle_speed   


        background()
        scoreboard(score)
        car(int(x),int(y))
       
       
      
        # obs_starty -=(obstacle_speed/4)
        # obstacle(obs_startx, obs_starty, obs_width, obs_height)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty += obstacle_speed
      

        # if x <= 145 or x >= 570 :
        # if x > display_width-car_width or x < 0:
             # gameover = True
             # gameclose = True
            #  message(mes)
        if x > display_width-(car_width+30) or x <30:
            pygame.mixer.music.pause()
            car_crash.play()
            message(mes)
        if obs_starty > display_height:
           obs_starty = 0-obs_height
           obs_startx = random.randrange(31, 700)
           obs = random.randrange(0,11)
           score += 5
           obstacle_speed += 1
        #    for background move 
        #    background_x = 14
        #    background_y = 0
        #    background_random = random.randrange(0,2)
        #    background_moving(background_x,background_y,background_random)
        #    print(obs_startx)
        #    obs_startx = random.randrange(0, (display_width))
          
        if y < obs_starty+obs_height:
            # print("y crossover")
            if x>obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width:
                #   print("x crossover")
                  pygame.mixer.music.pause()
                  car_crash.play()
                  message(mes)
        # score_level(score)          

        pygame.display.update()
        clock.tick(car_speed)
        
        
    pygame.quit()
    quit()
introloop()
        
