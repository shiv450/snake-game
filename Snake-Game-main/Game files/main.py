import pygame as py
import random as r
import math
from time import time
py.init()

game_over = False

bg = py.image.load("snake texture.jpg")

screen = py.display.set_mode((400,400))
Bg = py.image.load("snake texture.jpg")
Bg = py.transform.scale(Bg,(400,400))

font0 = py.font.Font("freesansbold.ttf",20)
font1 = py.font.Font("freesansbold.ttf",155)

def Game_0ver(game_over_message, gx,gy):
    text = font0.render(game_over_message,True,"Black")
    screen.blit(text,(gx,gy))

def scoreboard(textx,texty,score):
    tex = font0.render("score:" + str(score),True,(255,255,255))
    screen.blit(tex,(textx,texty))

snakeX = 200
snakeY = 200
snakeXmove = 0
snakeYmove = 0

fruitX = r.randint(50,350)
fruitY = r.randint(50,350)

list_of_coords = [(200,200)]

fruits_collected = 0

disfruitX = r.randrange(0,100)//10 * 10
disfruitY = r.randrange(0,100)//10 * 10


def snake_movement(coordsX,coordsY,Xmove,Ymove):
    global fruitX,fruitY
    global disfruitX,disfruitY
    global game_over
    global fruits_collected
    global list_of_coords
    screen.fill("Yellow")
    list_of_coords.append((coordsX,coordsY))
    distance = math.sqrt(math.pow(fruitX - snakeX, 2)+ math.pow(fruitY - snakeY, 2))
    dispearingfrdis = math.sqrt(math.pow(disfruitX - snakeX, 2)+ math.pow(disfruitY - snakeY, 2))
    # dupe_list = list_of_coords
    # dupe_list.remove(list_of_coords[-1])
    # print(dupe_list)

    if distance <= 5:
        fruitX = r.randrange(0,400)//10 * 10
        fruitY = r.randrange(0,400)//10 * 10
        list_of_coords.append((coordsX,coordsY))
        fruits_collected += 1
    
    else:
        list_of_coords.remove(list_of_coords[0])
    
    if list_of_coords[-1] in list_of_coords[0:-2:1]:
        index = list_of_coords[0:-2:1].index(list_of_coords[-1])
        try:
            for i in range(index,len(list_of_coords)-2):
                list_of_coords.pop(i)
        except:
            pass
    var = 0
    for (i , j) in list_of_coords:
        if var%2 == 0:
            py.draw.rect(screen, "Green", [i,j,10,10])
        else:
            py.draw.rect(screen, "Black", [i,j,10,10])
        var += 1

    if dispearingfrdis <= 5:
        disfruitX = 10000
        disfruitY = 10000
        fruits_collected += 5
        # list_of_coords.append((coordsX,coordsY))
        list_of_coords.append((coordsX+Xmove,coordsY+Ymove))
        # list_of_coords.append((coordsX+20,coordsY+20))


def fruit(x, y):
    py.draw.rect(screen, "Red", (x, y, 10, 10))


i = 0

# while i < 100:
#     k = int(time())%10
#     print(k)

def disappearing_fruit(x,y):
    fruit = py.image.load("strawberry.png")
    square = py.draw.rect(screen, "Black", (x, y, 1, 1))
    screen.blit(fruit,square)


screen.blit(Bg, (0,0))

while game_over is not True:
    for event in py.event.get():
        if event.type == py.QUIT:
            game_over = True
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                snakeYmove = 0
                snakeXmove = -10
            if event.key == py.K_RIGHT:
                snakeYmove = 0
                snakeXmove = 10
            if event.key == py.K_DOWN:
                snakeXmove = 0
                snakeYmove = 10
            if event.key == py.K_UP:
                snakeXmove = 0
                snakeYmove = -10
        snakeX += snakeXmove
        snakeY += snakeYmove
        if snakeX > 399:
            snakeX = 0
        if snakeY > 399:
            snakeY = 0
        if snakeX < 0:
            snakeX = 399
        if snakeY < 0:
            snakeY = 399
        
        snake = py.draw.rect(screen,'#ffffff',py.Rect(snakeX,snakeY,10,10))
        snake_movement(snakeX,snakeY,snakeXmove,snakeYmove)
        fruit(fruitX,fruitY)
        scoreboard(25,25,fruits_collected)
        if int(time())%10 < 5:
            disappearing_fruit(disfruitX,disfruitY)
        else: 
            disfruitX = r.randrange(0,100)//10 * 10
            disfruitY = r.randrange(0,100)//10 * 10
    py.display.update()