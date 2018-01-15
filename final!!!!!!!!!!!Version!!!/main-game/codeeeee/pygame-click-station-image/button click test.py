import pygame, sys
from pygame.locals import *

pygame.init()
watercycle = pygame.display.set_mode((700,400))
x = 600
y = 120
w = 120
h = 25
BLUE = (0,0,255)
CYAN = (255,0,0)
msg = "start"
running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        def button (msg, x, y, w, h, ic, ac, action=None ):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if (x+w > mouse[0] > x) and (y+h > mouse[1] > y):
                pygame.draw.rect(watercycle, CYAN, (x, y, w, h))
                if (click[0] == 1 and action != None):
                    if  (action == "Start"):
                        game_loop()
                   # elif  (action == "Load"):
                    elif  (action == "Exit"):
                          pygame.quit()

            else:
                pygame.draw.rect(watercycle, BLUE, (x, y, w, h))
                smallText = pygame.font.Font("comic sans MS", 20)
                textSurf, textRect = text_objects(msg, smallText)
                textRect.center = ( (x+(w/2)), (y+(h/2)) )
                watercycle.blit(textSurf, textRect)
