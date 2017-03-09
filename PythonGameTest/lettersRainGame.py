## 触发鼠标、键盘事件，会显示当前事件内容
import pygame
from pygame.locals import  *
from sys import exit

pygame.init()
SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

font = pygame.font.SysFont("arial", 16)
font_height = font.get_linesize()
print("font.get_linesize is ", font_height)
font_high = font.get_height()
print("font.get_height is ", font_high)
event_text = []

while True:
    event = pygame.event.wait()
    event_text.append(str(event))
    event_text = event_text[-SCREEN_SIZE[1]//font_height:]
    ## python3 整数除/，会得到浮点类型，用//就不会，不然会报错typeError
    if event.type == QUIT:
        exit()
    screen.fill((0, 0, 0))

    y = SCREEN_SIZE[1]-font_height
    for text in reversed(event_text):
        screen.blit(font.render(text, True, (0, 255, 0), (0, 0, 0)), (0, y))
        y-=font_height

    pygame.display.update()