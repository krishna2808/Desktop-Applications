# ------------------------------------import module----------------------------------->
import random
import pygame
# --------------------------------------load-modules of pygame-------------------------->
pygame.init()
screen_height, screen_weight = 600, 400
dis = pygame.display.set_mode((screen_height, screen_weight))
pygame.display.set_caption('Snake game')
pygame.display.update()
# <------------------------------------color--> RGB(red,green,blue) all of zero tuple for black-------->
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
# <-----------if we have out in game then it's game over and if close game then it's game_close---->
game_close, game_over = False, False
# <--------------------------x,y place for snake on display---------------------------------------->
x1, y1= 300,300
snake_size = 10
snake_speed = 10
# <----------------------- if x and y change then store in x1_change,y1_chang--------------------->
x1_change, y1_change = 0, 0
clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
font_score = pygame.font.SysFont("comicsansms", 25)
def message(mes, color):
    mesg = font_style.render(mes, True, color)
    dis.blit(mesg, [screen_weight/4, screen_height/4])

def our_snake(snake_size, snake_list):
     for i in snake_list:
        pygame.draw.rect(dis, black, [int(i[0]), int(i[1]), snake_size, snake_size])

def score(your_score):
    value = font_score.render("Your Score: " + str(your_score), True, yellow)
    dis.blit(value, [0, 0])

# <================================this is game loop for always run until we are out===========>
def gameloop():
    game_over = False
    game_close = False
    x1, y1 = screen_height/2, screen_weight/2
    x1_change, y1_change = 0, 0
    length_snake = 1
    pygame.mixer.init()
    pygame.mixer.music.load('snakehit.wav')

    snake_list = []
    foodx = int(round(random.randrange(0, screen_weight - snake_size)/ 10.0) * 10.0)
    foody = int(round(random.randrange(0, screen_height - snake_size)/ 10.0) * 10.0)



    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message("You Lose !! Press Q --> Quit or C---->Play Again", red)
            pygame.display.update()
            for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over=True
                        game_close = False
                    elif event.key == pygame.K_c:
                        gameloop()


        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 game_over = True
             if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_LEFT:
                      x1_change = -snake_size
                      y1_change = 0
                  elif event.key == pygame.K_RIGHT:
                      x1_change = snake_size
                      y1_change = 0
                  elif event.key == pygame.K_UP:
                      y1_change = -snake_size
                      x1_change=0
                  elif event.key == pygame.K_DOWN:
                      y1_change = snake_size
                      x1_change = 0
        if x1 <= 0 or y1 <= 0 or y1 >= screen_height or x1 >= screen_weight:
             game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, red, [foodx, foody, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_snake:
            del snake_list[0]
        for i in snake_list[:-1]:
            if i == snake_head:
                game_close = True
        our_snake(snake_size, snake_list)

        score(length_snake-1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = int(round(random.randrange(0, screen_weight - snake_size)/ 10.0) * 10.0)
            foody = int(round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0)
            pygame.mixer.music.play()
            length_snake += 1

        clock.tick(snake_speed)


    pygame.quit()
    quit()

gameloop()