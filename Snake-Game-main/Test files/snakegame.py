import pygame
import random
import time
import sys

pygame.init()

screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption("The Snake Game")

# icon = pygame.image.load("snake.png")
# pygame.display.set_icon(icon)

FPS = 10

clock = pygame.time.Clock()

# Designing Snake for the Snake Game
snakeX = 200 # Position of Snake in terms of X-Axis
snakeY = 200 # Position of Snake in terms of Y-Axis
snakeXVel = 0 # Velocity of Snake in terms of X-Axis
snakeYVel = 0 # Velocity of Snake in terms of Y-Axis
fruitX = random.randrange(0, 400)//10 * 10
fruitY = random.randrange(0, 400)//10 * 10
bodyList = [(snakeX, snakeY)]

def fruit(x, y):
    pygame.draw.rect(screen, "Red", (x, y, 10, 10))

gameOver = False

def snake(x, y):
    global gameOver
    global fruitX, fruitY
    screen.fill("black")
    bodyList.append((x, y))
    if (x, y) in bodyList:
        gameOver = False
    if fruitX == x and fruitY == y:
        while (fruitX, fruitY) in bodyList:
            fruitX = random.randrange(0, 400)//10 * 10
            fruitY = random.randrange(0, 400)//10 * 10
    else:
        del bodyList[0]
    for (i, j) in bodyList:
        pygame.draw.rect(screen, "White", [i, j, 10, 10])

while gameOver is False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if snakeXVel != 10:
                    snakeXVel = - 10
                snakeYVel = 0
            elif event.key == pygame.K_RIGHT:
                if snakeXVel != -10:
                    snakeXVel = 10
                    snakeYVel = 0
            elif event.key == pygame.K_UP:
                snakeXVel = 0
                if snakeYVel != 10:
                    snakeYVel = -10
            elif event.key == pygame.K_DOWN:
                snakeXVel = 0
                if snakeYVel != -10:
                    snakeYVel = 10
            else:
                continue

    snakeX = snakeX + snakeXVel
    snakeY = snakeY + snakeYVel

    if snakeX <= 0:
        gameOver = True
    elif snakeX >= 400:
        gameOver = True
    if snakeY <= 0:
        gameOver = True
    elif snakeY >= 400:
        gameOver = True

    snake(snakeX, snakeY)
    fruit(fruitX, fruitY)

    clock.tick(FPS)

    pygame.display.update()