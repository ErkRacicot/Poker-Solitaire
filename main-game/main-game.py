import pygame, sys, os
from pygame.locals import *

pygame.init()
game = 1

Screen = pygame.display.set_mode((1200,700))
    
#bg = pygame.image.load(os.path.join('img', 'start.png'))
bg = pygame.image.load('start.jpg')

file = (os.path.join('music', 'poker-solitare-track-1.mp3'))

pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)
    
while game == 1:
    
    Screen.blit(bg, (0, 0))
    pygame.display.update()
    
    

    


