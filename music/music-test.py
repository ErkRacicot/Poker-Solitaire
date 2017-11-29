import pygame, sys
from pygame.locals import *


file = 'poker solitare 1.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)

pygame.display.set_mode((1200,700))
