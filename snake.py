import pygame

import time

import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

disWidth = 800
disHeight = 600
dis = pygame.display.set_mode((disWidth, disHeight))

pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

snakeBlock = 10
snakeSpeed = 15
fontStyle = pygame.font.SysFont("bahnschrift", 25)

scoreFont = pygame.font.SysFont("comicsansms", 25)

def ourSnake(snakeBlock, snakeList):
    for x in snakeList:
        pygame.draw.rect(dis, black, [x[0], x[1], snakeBlock, snakeBlock])

def message(msg,color):
   mesg = fontStyle.render(msg, True, color)
   dis.blit(mesg, [disWidth/6, disHeight/3])

def YourScore(score):
    value = scoreFont.render("Ваш счёт: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def gameLoop():
    gameOver = False
    gameClose = False
    x1 = disWidth / 2
    y1 = disHeight / 2
    x1_change = 0
    y1_change = 0
    typeFood = 0
    snakeList = []
    LengthOfSnake = 1
    foodx = round(random.randrange(0, disWidth - snakeBlock) / 10.0) * 10.0

    foody = round(random.randrange(0, disHeight - snakeBlock) / 10.0) * 10.0

    while not gameOver:
        while gameClose == True:
            dis.fill(blue)
            message("Вы проиграли! Нажмите Q для выхода или C для повторной игры ", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snakeBlock
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snakeBlock
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snakeBlock
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snakeBlock
                    x1_change = 0
        if x1 >= disWidth or x1 < 0 or y1 >= disHeight or y1 < 0:
            gameClose = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        if typeFood == 0:
            pygame.draw.rect(dis, red, [foodx, foody, snakeBlock, snakeBlock]) # first commit in thirdBranch
        else:
            pygame.draw.rect(dis, green, [foodx, foody, snakeBlock, snakeBlock]) # second commit in thirdBranch

        snakeHead = []
        snakeHead.append(x1)
        snakeHead.append(y1)
        snakeList.append(snakeHead) # third commit in thirdBranch берем из master

        if len(snakeList) > LengthOfSnake:
            del snakeList[0]

        for x in snakeList[:-1]:
            if x == snakeHead:
                gameClose = True # third commit in thirdBranch берем из feature

        ourSnake(snakeBlock, snakeList)
        YourScore(LengthOfSnake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:

            foodx = round(random.randrange(0, disWidth - snakeBlock) / 10.0) * 10.0 # third commit in thirdBranch берем из обеих веток
            foody = round(random.randrange(0, disHeight - snakeBlock) / 10.0) * 10.0

            if typeFood == 0:
                LengthOfSnake += 2 # fourth commit in thirdBranch
            else:
                LengthOfSnake += 3
            if random.random() > 0.5:
                typeFood = 0
            else:
                typeFood = 1

        clock.tick(snakeSpeed)

    pygame.quit()
    quit()

gameLoop()
