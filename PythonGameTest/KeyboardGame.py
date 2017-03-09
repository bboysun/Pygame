background_image_filename = 'resources/sushiplate.jpg'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filename).convert()

x, y = 0, 0
# move_x, move_y = 0, 0
move = {K_LEFT:0, K_RIGHT:0, K_UP:0, K_DOWN:0}

while True:
    # for event in pygame.event.get():
    #     if event.type == QUIT:
    #         exit()
    #     if event.type == KEYDOWN:
    #         ## 键盘按下
    #         if event.key == K_LEFT:
    #             move_x = -1
    #         elif event.key == K_RIGHT:
    #             move_x = 1
    #         elif event.key == K_UP:
    #             move_y = -1
    #         elif event.key == K_DOWN:
    #             move_y = 1
    #     elif event.type == KEYUP:
    #         ## 键盘松开
    #         move_x = 0
    #         move_y = 0
    # x+= move_x
    # y+= move_y
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            move[event.key] = 1
        elif event.type == KEYUP:
            move[event.key] = 0

    CATONKEYBOARD = USEREVENT + 1
    my_event = pygame.event.Event(CATONKEYBOARD, message = "Bad cat")
    pygame.event.post(my_event)

    for event in pygame.event.get():
        if event.type == CATONKEYBOARD:
            print(event.message)
    x -= move[K_LEFT]
    x += move[K_RIGHT]
    y -= move[K_UP]
    y += move[K_DOWN]

    screen.fill((0, 0, 0))
    screen.blit(background, (x, y))
    pygame.display.update()


